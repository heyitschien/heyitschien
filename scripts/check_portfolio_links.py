#!/usr/bin/env python3
"""Validate tracked portfolio evidence paths without flaky live-site checks."""

from __future__ import annotations

import argparse
import html
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK_RE = re.compile(
    r"!?\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))(?:\s+[\"'][^\"']*[\"'])?\s*\)"
)
HTML_LINK_RE = re.compile(r"""(?:href|src)=["']([^"']+)["']""", re.IGNORECASE)
FENCED_CODE_RE = re.compile(r"```.*?```", re.DOTALL)
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
GITHUB_HOSTS = {"github.com", "raw.githubusercontent.com"}
SKIPPED_SCHEMES = {"data", "javascript", "mailto", "tel"}


def tracked_markdown_files() -> list[Path]:
    """Return tracked README/docs Markdown files, excluding local untracked drafts."""
    result = subprocess.run(
        ["git", "ls-files", "README.md", "docs/**/*.md", "docs/*.md"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return sorted({ROOT / line for line in result.stdout.splitlines() if line})


def extract_links(path: Path) -> set[str]:
    """Extract Markdown and inline HTML links outside fenced code blocks."""
    content = FENCED_CODE_RE.sub("", path.read_text(encoding="utf-8"))
    links = {
        html.unescape(match.group(1) or match.group(2))
        for match in MARKDOWN_LINK_RE.finditer(content)
    }
    links.update(html.unescape(match) for match in HTML_LINK_RE.findall(content))
    return links


def github_slug(heading: str) -> str:
    """Approximate GitHub's Markdown heading slug for local-fragment checks."""
    value = re.sub(r"<[^>]+>", "", heading).strip().lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    value = re.sub(r"\s+", "-", value)
    return re.sub(r"-+", "-", value).strip("-")


def markdown_anchors(path: Path) -> set[str]:
    """Collect heading anchors with GitHub-style duplicate suffixes."""
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    content = FENCED_CODE_RE.sub("", path.read_text(encoding="utf-8"))
    for heading in HEADING_RE.findall(content):
        base = github_slug(heading)
        count = counts.get(base, 0)
        anchor = base if count == 0 else f"{base}-{count}"
        counts[base] = count + 1
        anchors.add(anchor)
    return anchors


def validate_local_link(source: Path, destination: str) -> str | None:
    """Return an error for a missing local target or Markdown anchor."""
    parsed = urllib.parse.urlsplit(destination)
    if parsed.scheme or parsed.netloc:
        return None

    relative_path = urllib.parse.unquote(parsed.path)
    target = source if not relative_path else source.parent / relative_path
    target = target.resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        return f"{source.relative_to(ROOT)}: path escapes repository: {destination}"

    if not target.exists():
        return f"{source.relative_to(ROOT)}: missing local target: {destination}"

    if parsed.fragment and target.suffix.lower() == ".md":
        fragment = urllib.parse.unquote(parsed.fragment).lower()
        if fragment not in markdown_anchors(target):
            return (
                f"{source.relative_to(ROOT)}: missing Markdown anchor "
                f"#{parsed.fragment} in {target.relative_to(ROOT)}"
            )
    return None


def check_http_url(
    url: str, timeout: float, *, conservative: bool
) -> tuple[str | None, str | None]:
    """Return (error, warning), retrying transient GitHub/network failures."""
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/json",
        "User-Agent": "heyitschien-portfolio-link-check",
    }
    request = urllib.request.Request(url, headers=headers, method="GET")
    last_failure = ""
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                if response.status < 400:
                    return None, None
                last_failure = f"{url}: HTTP {response.status}"
        except urllib.error.HTTPError as error:
            last_failure = f"{url}: HTTP {error.code}"
            if error.code in {400, 401, 404, 410, 422}:
                return last_failure, None
        except (urllib.error.URLError, TimeoutError) as error:
            last_failure = f"{url}: {error}"

        if not conservative:
            return last_failure, None
        if attempt < 2:
            time.sleep(0.5 * (attempt + 1))

    return None, f"transient check warning after retries: {last_failure}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check-external",
        action="store_true",
        help="Also check non-GitHub live sites; skipped in CI by default to avoid flakiness.",
    )
    parser.add_argument("--timeout", type=float, default=15.0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    files = tracked_markdown_files()
    errors: list[str] = []
    warnings: list[str] = []
    github_urls: set[str] = set()
    external_urls: set[str] = set()

    for source in files:
        for destination in extract_links(source):
            parsed = urllib.parse.urlsplit(destination)
            if parsed.scheme.lower() in SKIPPED_SCHEMES:
                continue
            if parsed.scheme in {"http", "https"}:
                if parsed.hostname in GITHUB_HOSTS:
                    github_urls.add(destination)
                else:
                    external_urls.add(destination)
                continue
            error = validate_local_link(source, destination)
            if error:
                errors.append(error)

    for url in sorted(github_urls):
        error, warning = check_http_url(url, args.timeout, conservative=True)
        if error:
            errors.append(error)
        if warning:
            warnings.append(warning)

    if args.check_external:
        for url in sorted(external_urls):
            error, warning = check_http_url(url, args.timeout, conservative=False)
            if error:
                errors.append(error)
            if warning:
                warnings.append(warning)

    print(
        f"Checked {len(files)} tracked Markdown files, "
        f"{len(github_urls)} GitHub URLs, and local relative/image paths."
    )
    if external_urls and not args.check_external:
        print(
            f"Skipped {len(external_urls)} non-GitHub live URLs by design; "
            "run with --check-external for a manual best-effort check."
        )
    if warnings:
        print("\nLink validation warnings:", file=sys.stderr)
        for warning in warnings:
            print(f"- {warning}", file=sys.stderr)
    if errors:
        print("\nLink validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Portfolio link validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
