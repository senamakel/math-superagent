#!/usr/bin/env python3
"""
Independent second-route cross-check of the n=11 sharp-kernel census result.

The census (code/census_kernel.py, run for --maxn 11) tested every sharp-kernel
member C_N (N=8,9,10,11; 249 graphs total) for 4-colourability with the SAT
oracle (lib.satcolor, Cadical153) and recorded one witness per graph in
code/out/census_kernel_n11.captured_witnesses.json.

This script re-verifies each member's 4-colourability with a DIFFERENT
complete method: exhaustive DSATUR backtracking with symmetry breaking from
lib.coloring (chromatic_colorable). For every member it confirms
  (a) chromatic_colorable finds a proper 4-colouring (independent complete
      route), and
  (b) the recorded SAT witness independently checks via verify_coloring.

This is the same style of independent re-verification as
crosscheck_kernel_coloring.py (which covered N=8,9,10), extended to the
newly-enumerated n=11 members (228 graphs) and re-confirming the 21 older
members grew from the --maxn 11 enumeration.

Output: code/out/crosscheck_kernel_n11.captured.txt
"""
import json

from lib.coloring import chromatic_colorable, verify_coloring

WITNESS_JSON = "code/out/census_kernel_n11.captured_witnesses.json"
CAPTURE = "code/out/crosscheck_kernel_n11.captured.txt"


def main():
    with open(WITNESS_JSON) as f:
        data = json.load(f)   # {"n": {"idx": {"edges": [[i,j],...], "witness": [...]}}}

    total = 0
    agreed = 0
    problems = []
    lines = []

    def log(s):
        lines.append(s)
        print(s, flush=True)

    log("Independent cross-check of sharp-kernel census 4-colourability (N<=11),")
    log("via exhaustive DSATUR backtracking (lib.coloring.chromatic_colorable),")
    log("against the recorded SAT witnesses from lib.satcolor.")
    log("=" * 70)
    for n_str in sorted(data, key=int):
        n = int(n_str)
        for idx_str in sorted(data[n_str], key=int):
            entry = data[n_str][idx_str]
            edges = [tuple(e) for e in entry["edges"]]
            witness = entry["witness"]
            nv = max((max(a, b) for (a, b) in edges)) + 1
            total += 1

            ok, bt_witness = chromatic_colorable(nv, edges, 4)
            witness_ok = False
            try:
                verify_coloring(nv, edges, witness)
                witness_ok = True
            except AssertionError as exc:
                problems.append((n, idx_str, "witness check failed: %r" % exc))

            tag = "AGREE(4-colourable)" if (ok and witness_ok) else "MISMATCH"
            if ok and witness_ok:
                agreed += 1
            else:
                problems.append((n, idx_str, "ok=%s witness_ok=%s" % (ok, witness_ok)))
            log("n=%d idx=%s members=%d edges=%d bt4col=%s satWitnessChecks=%s -> %s"
                % (n, idx_str, nv, len(edges), ok, witness_ok, tag))

    log("=" * 70)
    log("TOTAL kernel members re-verified: %d" % total)
    log("Members both oracles agree 4-colourable: %d" % agreed)
    if problems:
        log("PROBLEMS: %d" % len(problems))
        for p in problems:
            log("  " + repr(p))
    else:
        log("No mismatches: SAT (Cadical153) and exhaustive backtracking")
        log("(lib.coloring) independently agree every kernel member up to n=11 is 4-colourable.")

    with open(CAPTURE, "w") as f:
        f.write("\n".join(lines) + "\n")
    log("(captured to %s)" % CAPTURE)


if __name__ == "__main__":
    main()
