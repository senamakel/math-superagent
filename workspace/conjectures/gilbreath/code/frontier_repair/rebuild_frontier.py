#!/usr/bin/env python3
"""Rebuild research/FRONTIER.md from the operator-recovered committed frontier.

Source of truth: research/notes/frontier-recovered-2026-08-13.md (commit db36fc23).
Steps, all mechanical:
  1. Extract every table row from the recovered note (lines whose first cell is a
     positive integer: the "Cited by" count).
  2. Apply the share/bookmark URL filter to each row's Source URL (2nd column).
     Patterns: intent/tweet, sharer.php, shareArticle, /submit?url=,
     BibtexHandler, /import/?url=, follow/publon, /follow/, plus a host-level
     blocklist of the share-button vendors seen in the 2026-08-13 collapse
     (twitter, facebook, linkedin, reddit, delicious, bibsonomy, mendeley,
     publons).
  3. Exclude the Gatti 2020 preprints.org wrapper row
     (https://www.preprints.org/manuscript/202003.0145) per operator directive:
     NOT PEER-REVIEWED, 0 views/downloads/comments; its full text contains no
     lemma testable against code/out/blocks_depth1000.json; not a frontier lead.
  4. Write the rebuilt research/FRONTIER.md with a header that reports the
     recovered/claimed count, the on-disk count, filter drops, Gatti exclusion,
     and the final row count — the failure signal (candidate count collapse) is
     documented here and in research/notes/frontier-collapse-alarm.md.

Also verifies TASKS.md item 1: research/CLAIMS.md was regenerated and
`cht-inverse-theorem` and `valid-extension-nonlocal` each appear exactly once
(matching the backtick-delimited claim id; plain-string counts reported too).
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # /workspace
RECOVERED = ROOT / "research" / "notes" / "frontier-recovered-2026-08-13.md"
FRONTIER = ROOT / "research" / "FRONTIER.md"
CLAIMS = ROOT / "research" / "CLAIMS.md"

# Share/bookmark endpoint patterns (operator-specified + similar).
URL_BLOCK_PATTERNS = [
    "intent/tweet",
    "sharer.php",
    "shareArticle",
    "/submit?url=",
    "BibtexHandler",
    "/import/?url=",
    "follow/publon",
    "/follow/",
]
# Host-level blocklist: the vendors whose buttons replaced the frontier in the
# 2026-08-13 collapse (and again in the second incident).
BLOCK_HOSTS = [
    "twitter.com",
    "x.com",
    "facebook.com",
    "linkedin.com",
    "reddit.com",
    "del.icio.us",
    "delicious.com",
    "bibsonomy.org",
    "mendeley.com",
    "publons.com",
    "addthis.com",
    "digg.com",
    "buffer.com",
    "pinterest.com/pin/create",
]

# Per directive (5): the Gatti preprints.org wrapper must not appear in the frontier.
EXCLUDED_URLS = {
    "https://www.preprints.org/manuscript/202003.0145",
    "http://www.preprints.org/manuscript/202003.0145",
    "www.preprints.org/manuscript/202003.0145",
}


def is_blocked(url: str) -> bool:
    low = url.lower()
    for pat in URL_BLOCK_PATTERNS:
        if pat.lower() in low:
            return True
    for host in BLOCK_HOSTS:
        if host in low:
            return True
    return False


def extract_rows(text: str):
    """Yield (raw_line, cited_by, source_url, rest) for every table data row."""
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        # Table rows have >= 4 cells: cited-by, source, called, why.
        if len(cells) < 4:
            continue
        try:
            cited = int(cells[0])
        except ValueError:
            continue  # header or separator row
        rows.append((line, cited, cells[1], cells[2:]))
    return rows


def main() -> int:
    rec_text = RECOVERED.read_text(encoding="utf-8")
    rows = extract_rows(rec_text)
    n_recovered = len(rows)

    # Claimed count in the recovered prologue ("These 42 rows are ...").
    m = re.search(r"These (\d+) rows are the last committed frontier", rec_text)
    claimed = int(m.group(1)) if m else None

    dropped = []      # rows removed by the share/bookmark filter
    excluded = []     # rows removed by the Gatti directive
    kept = []
    for line, cited, url, rest in rows:
        if is_blocked(url):
            dropped.append((line, url))
            continue
        if url in EXCLUDED_URLS:
            excluded.append((line, url))
            continue
        kept.append((line, cited, url, rest))

    # Header for the rebuilt frontier.
    header = f"""# Frontier — what this library's own sources cite

Derived from the citations inside every document this run has downloaded, and rewritten on each download. Nothing here has been judged: a row is a lead, not a recommendation.

Ranked by how many of the library's sources cite it, then by how closely the citing sentence matches the goal. A **cited by** count above one means independent sources agree it is the reference for the subject, which is worth more than any single search ranking. A ~~struck-through~~ row is already in the library — do not download it again.

**Filter rule (applied every write):** URLs matching any of these patterns are share/bookmark endpoints, never citations, and are dropped before writing: `intent/tweet`, `sharer.php`, `shareArticle`, `/submit?url=`, `BibtexHandler`, `/import/?url=`, `follow/publon`, `/follow/`, and the host-level blocklist (twitter, facebook, linkedin, reddit, delicious, bibsonomy, mendeley, publons, addthis, digg, buffer, pinterest pin/create). A single bad wrapper page replaced this file wholesale on 2026-08-13; the filter prevents a recurrence. The header says how many rows were dropped.

**Failure signal:** If the candidate count drops by more than 30%, the output is likely garbage. On 2026-08-13 it fell from 501 candidate leads to 15 — social-media buttons from a single archived wrapper page (the Gatti 2020 preprints.org wrapper). `research/notes/frontier-collapse-alarm.md` records the rule, and the next run must re-read this file after any multi-page download and check the count.

*Reseeded {n_recovered} rows from commit db36fc23 (operator recovery 2026-08-13, `research/notes/frontier-recovered-2026-08-13.md`). Rebuilt 2026 by `code/frontier_repair/rebuild_frontier.py`: recovered note claimed {claimed} rows; on-disk table held {n_recovered}; share-filter dropped {len(dropped)}; Gatti 2020 wrapper excluded per directive ({len(excluded)}); {len(kept)} rows kept. The 418 cited-once candidates referenced by the recovered note were not saved by the operator (lost with `config/.frontier.json`) and are not recoverable from the committed state.*

| Cited by | Source | Called | Why it was cited |
| --- | --- | --- | --- |
"""
    body = "\n".join(line for line, _cited, _url, _rest in kept)
    tail = f"""

_418 further candidates not shown by the recovered commit; they were cited once each and are not recoverable from the committed state._
"""
    FRONTIER.write_text(header + body + "\n" + tail, encoding="utf-8")

    # ---- TASKS.md item 1: CLAIMS.md dedup check ----
    claims_text = CLAIMS.read_text(encoding="utf-8") if CLAIMS.exists() else ""
    verdicts = {}
    for claim_id in ("cht-inverse-theorem", "valid-extension-nonlocal",
                     "valid-extension-backward-nonlocal-refuted"):
        backticked = claims_text.count(f"`{claim_id}`")
        plain = claims_text.count(claim_id)
        verdicts[claim_id] = (backticked, plain)

    print(f"recovered note exists:            {RECOVERED.exists()}")
    print(f"rows claimed in prologue:          {claimed}")
    print(f"rows on disk in table:             {n_recovered}")
    print(f"rows dropped by share filter:      {len(dropped)}")
    for line, url in dropped:
        print(f"    DROPPED {url}")
    print(f"rows excluded (Gatti wrapper):     {len(excluded)}")
    for line, url in excluded:
        print(f"    EXCLUDED {url}")
    print(f"rows kept in rebuilt FRONTIER.md:  {len(kept)}")
    print(f"FRONTIER.md written:               {FRONTIER} ({FRONTIER.stat().st_size} bytes)")
    print(f"CLAIMS.md exists:                  {CLAIMS.exists()}")
    for cid, (bt, pl) in verdicts.items():
        verdict = "OK once" if bt == 1 else ("FAIL" if bt == 0 else f"{bt}x DUPLICATE")
        print(f"  `{cid}`  backticked={bt}  plain={pl}  -> {verdict}")
    return 0


if __name__ == "__main__":
    sys.exit(main())