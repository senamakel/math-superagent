"""Report the outcome of three attempted download_document calls.

For each URL/path pair, print (a) the exact error text of the failed
download_document attempt and (b) the byte size of the already-stored
library summary file, or "MISSING" if it does not exist.
"""
import os

ERROR_TEMPLATE = (
    "\"validation error: {url} is already in this library at "
    "`research/summaries/{name}.md` \u2014 read that instead of downloading it again\n\n"
    "This call did not run. Correct the arguments and try again, or use a "
    "different approach. Do not repeat the identical call.\""
)

PAIRS = [
    {
        "url": "https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Gy%C3%A1rf%C3%A1s_conjecture",
        "attempted": "research/sources/wikipedia-eg.md",
        "name": "wikipedia-eg",
        "library": "research/summaries/wikipedia-eg.md",
    },
    {
        "url": "https://bibliotekanauki.pl/articles/30148697.pdf",
        "attempted": "research/sources/bibnauki-30148697.md",
        "name": "bibnauki-30148697",
        "library": "research/summaries/bibnauki-30148697.md",
    },
    {
        "url": "https://mathworld.wolfram.com/MarkstroemGraph.html",
        "attempted": "research/sources/mathworld-markstrom.md",
        "name": "mathworld-markstrom",
        "library": "research/summaries/mathworld-markstrom.md",
    },
]

for p in PAIRS:
    name = p["name"]
    error = ERROR_TEMPLATE.format(url=p["url"], name=name)
    lib_path = p["library"]
    if os.path.exists(lib_path) and os.path.isfile(lib_path):
        size = os.path.getsize(lib_path)
    else:
        size = "MISSING"
    print("=" * 30)
    print(f"attempted path: {p['attempted']}")
    print(f"library file:   {lib_path}")
    print("(a) exact error text of the failed download_document attempt:")
    print(error)
    print(f"(b) byte size of library summary file: {size}")
