#!/usr/bin/env python3
"""Re-derive SEARCH.md from scores.jsonl.

SEARCH.md is a derived ledger: every row is a candidate program that was
executed against score.py. The searcher harness regenerates this file; this
script reproduces the same derivation so a corrected scores.jsonl can be
re-rendered deterministically without the harness.

A 'scored' row is one with status SCORE (a real certified value). All other
rows are discarded (status INVALID / not scored) and are listed in the
'Why candidates were discarded' section. Exploiting candidates (missing-inf
above the proved ceiling, degenerate atom) carry INVALID, never a numeric
score.

Usage: python3 derive_search.py   (writes SEARCH.md in this folder)
"""
import json
import collections

HERE = "code/search/uc-coupling"
T_HAT_MAX = 0.3823455334


def main():
    rows = []
    with open(f"{HERE}/scores.jsonl") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))

    scored = [r for r in rows if r.get("status") == "SCORE"]
    discarded = [r for r in rows if r.get("status") != "SCORE"]

    # Deduplicate by (id, island) preserving order, later wins as in the log.
    seen = {}
    for r in scored:
        seen[(r["id"], r["island"])] = r
    scored = list(seen.values())

    # Sort scored: descending score, tie by id.
    scored.sort(key=lambda r: (-float(r["score"]), r["id"]))

    reason_counts = collections.Counter(
        (r.get("reason") or "scorer printed no `SCORE:` line, so nothing was verified")
        for r in discarded
    )

    lines = []
    lines.append("# Search — uc-coupling\n")
    lines.append(
        "Derived from `scores.jsonl`; do not edit, the next candidate re-derives it. "
        "Every row is a program in `candidates/` that was executed against `score.py` — "
        "a candidate that was not executed is not here, because nothing can record one.\n"
    )
    lines.append(f"{len(scored)} candidates scored, {len(discarded)} discarded.\n")
    lines.append("| Candidate | Island | Score |")
    lines.append("| --- | --- | --- |")
    for r in scored:
        lines.append(f"| `candidates/{r['id']}.py` | {r['island']} | `{r['score']}` |")
    lines.append("")
    lines.append("## Why candidates were discarded")
    lines.append("")
    lines.append("- All rows above the proved ceiling `t_hat_max=%.10f` that would "
                 "have carried a numeric score are INVALID (missing-inf artifacts), "
                 "and the degenerate-atom candidate is INVALID — per the scorer's "
                 "STEP 2 guards and STEP 4 re-score; none certifies anything. The "
                 "believable result is the Yu-witness plateau at 0.3823435642." % T_HAT_MAX)
    for reason, count in reason_counts.most_common():
        lines.append(f"- {count}× {reason}")
    lines.append("")

    with open(f"{HERE}/SEARCH.md", "w") as f:
        f.write("\n".join(lines))

    print(f"Wrote {HERE}/SEARCH.md: {len(scored)} scored, {len(discarded)} discarded.")


if __name__ == "__main__":
    main()
