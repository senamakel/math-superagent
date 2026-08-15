#!/usr/bin/env python3
"""Audit: every full-text source under research/sources/ has a digest under
research/summaries/, and every digest is substantive (not a bare stub).

This is a pairing check, not a search of the answer space: it lists the
sources with no obvious digest and the digests with no content, so a reader
knows where (if anywhere) the library has an undigested hole.

Run:  python3 code/scholar/digest_audit.py
"""
import os, re, sys

SRC = os.path.join('research', 'sources')
SUM = os.path.join('research', 'summaries')

def slug(name: str) -> str:
    """Canonical-ish slug: strip .full.md / .full, trim edition suffixes."""
    s = name
    s = re.sub(r'\.full\.md$', '', s)
    s = re.sub(r'\.full$', '', s)
    s = re.sub(r'\.(md|txt)$', '', s)
    # strip trailing edition/source disambiguators that do not change identity
    s = re.sub(r'-(2026|2025|2024|2023|2018|2021|2020|2016|2017|2011|2003|2006|1994|1993|1959|1990s|v\d|v2|v1)$', '', s, flags=re.I)
    return s.strip()

def stems(path: str) -> set:
    out = set()
    for fn in os.listdir(path):
        out.add(slug(fn))
    return out

def main() -> int:
    if not (os.path.isdir(SRC) and os.path.isdir(SUM)):
        print("source or summary dir missing; run from /workspace", file=sys.stderr)
        return 2

    src_slugs = stems(SRC)
    sum_slugs = stems(SUM)

    # full-text sources: the ones that end .full or carry a real body
    full_sources = [fn for fn in sorted(os.listdir(SRC)) if fn.endswith('.full.md')]

    # Map each full source to candidate digests by slug match
    unmatched = []
    for fn in full_sources:
        s = slug(fn)
        # candidate digests are summaries whose slug matches, or is a
        # prefix-of / contains relationship
        cands = [d for d in os.listdir(SUM) if s in slug(d) or slug(d) in s]
        if not cands:
            unmatched.append(fn)

    print(f"full-text sources: {len(full_sources)}")
    print(f"summary files:    {len(os.listdir(SUM))}")
    print()
    if unmatched:
        print(f"FULL SOURCES WITH NO OBVIOUS DIGEST ({len(unmatched)}):")
        for f in unmatched:
            print("  ", f)
    else:
        print("Every full-text source has at least one digest candidate by slug.")

    # Detect bare-stub digests: very short, or that say 'not obtained / no content'
    print()
    small = []
    for fn in sorted(os.listdir(SUM)):
        p = os.path.join(SUM, fn)
        try:
            size = os.path.getsize(p)
        except OSError:
            continue
        if size < 1200:  # under ~1200 bytes likely a stub / provenance record
            small.append((fn, size))
    print(f"Summaries under 1200 bytes ({len(small)}):")
    for fn, size in small:
        first = ""
        try:
            with open(os.path.join(SUM, fn)) as fh:
                first = ' '.join(fh.read().split())[:110]
        except OSError:
            pass
        print(f"  {size:6d}  {fn}  :: {first}")

    return 0

if __name__ == '__main__':
    sys.exit(main())
