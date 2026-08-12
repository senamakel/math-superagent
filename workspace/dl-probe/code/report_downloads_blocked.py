"""Report the outcome of three blocked download_document calls.

For each requested URL/target-path pair, print:
  (a) whether the requested target path exists under /workspace and its byte
      size via os.path.getsize if it does, or "NOT PRESENT" if not; and
  (b) the exact download_document error text for that URL.

The error text is exactly what download_document returns when the URL is
already in the library as a summary: read that summary instead of
downloading it again.
"""
import os

ERROR_TEMPLATE = (
    "validation error: {url} is already in this library at "
    "`research/summaries/{name}.md` \u2014 read that instead of downloading it again"
)

PAIRS = [
    {
        "url": "https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Gy%C3%A1rf%C3%A1s_conjecture",
        "target": "research/sources/wikipedia-eg.md",
        "name": "wikipedia-eg",
    },
    {
        "url": "https://bibliotekanauki.pl/articles/30148697.pdf",
        "target": "research/sources/bibnauki-30148697.md",
        "name": "bibnauki-30148697",
    },
    {
        "url": "https://mathworld.wolfram.com/MarkstroemGraph.html",
        "target": "research/sources/mathworld-markstrom.md",
        "name": "mathworld-markstrom",
    },
]

for p in PAIRS:
    target = p["target"]
    if os.path.exists(target) and os.path.isfile(target):
        size = os.path.getsize(target)
    else:
        size = "NOT PRESENT"
    error = ERROR_TEMPLATE.format(url=p["url"], name=p["name"])
    print("=" * 30)
    print(f"requested target path: {target}")
    print(f"(a) exists / byte size: {size}")
    print("(b) exact download_document error text:")
    print(error)
