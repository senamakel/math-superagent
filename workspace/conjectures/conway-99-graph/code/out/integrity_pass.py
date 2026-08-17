"""Final integrity pass (directive 20 / steering): confirm every capture that a
`checked` claim or solution.md cites actually exists on disk, and flag any
artifact that is cited while being SUPERSEDED / retracted.

This is not new mathematics: it checks the run's record for a false 'checked'.
Files that a claim or route names but that never landed (an empty capture, a
superseded one passed off as live, a renamed/missing file) are where a wrong
'checked' would hide.

Usage: python code/out/integrity_pass.py
"""
import os
import re
import sys

ROOT = "/workspace"

# All files referenced by solution.md routes 1-11 (from reading §2).
solution_md_refs = [
    "code/out/g_reduce_control.captured.txt",
    "code/out/hexagon_identity_verified.captured.txt",
    "code/out/n3_order6_feasibility.captured.txt",
    "code/out/check_triangle_graph.captured.txt",
    "code/out/coclique_lift_clean_design.txt",
    "code/out/coclique_lift_cpsat.captured.txt",
    "code/out/n3_global_ledger.captured.txt",
    "code/out/incidence_prank_determinism.captured.txt",
    "code/out/verify_twograph_gate.captured.txt",
    "code/out/n3_vc_loop_closure_recheck.captured.txt",
    "code/out/n3_vc_gate.captured.txt",          # cited as SUPERSEDED -> allowed only as retraction
    "code/out/orbit_z3_enc_g99_plain_detached.captured.txt",
    "code/out/orbit_order3_final_boundary.captured.txt",
    "code/out/route11_boundary_final_verify.captured.txt",
]

# The checked-claim anchors, as recorded in the claims ledger:
# claim id -> files that claim names as its evidence/capture.
checked_claim_files = {
    "c3-controls-verified": ["research/notes/c3-triangle-graph-controls.md"],
    "c4": ["research/notes/established-claims.md"],
    "c5": ["research/notes/established-claims.md"],
    "coclique-alpha22-forces-22242-design": ["research/notes/n3-coclique-design-dead-end.md"],
    "coclique-bound-closed-form": ["code/out/coclique-bound-closed-form.md"],
    "divisor63-multiplicity-integrality": ["code/out/divisor63-characterization.md"],
    "fixed-set-lemma-fails-on-bvls": ["research/notes/fixed-set-lemma-fails-on-bvls.md"],
    "g-reduce-c-refuted-on-bvls": ["research/notes/g-reduce-c-refuted.md"],
    "incidence-2rank-not-parameter-determined-but-unprovable": ["research/threads/incidence-code.md"],
    "integrality-five-members": ["code/out/feasibility-candidates-corrected.md"],
    "keramatipour-paley9-pattern-holds-on-controls": ["research/summaries/keramatipour-sat-conway99-body.md"],
    "makhnev-condstar-gate-passed": ["code/out/n3-screening-claims.md"],
    "makhnev-lambda0-1331216-infeasible-integrality": ["research/notes/makhnev-lambda0-infeasible-integrality.md"],
    "n3-99-forced-at-least-3": ["code/out/n3-screening-claims.md"],
    "n3-cap-closed-form": ["research/notes/n3-cap-closed-form.md"],
    "n3-seed-locally-consistent-radius1": ["research/notes/n3-seed-locally-consistent-radius1.md"],
    "n3-zero-four-classical-lambda1-srgs": ["code/out/n3-four-graphs-finding.md"],
    "order6-n3-not-forced": ["code/out/n3-screening-claims.md"],
    "pentagon-count-closed-form-verified": ["code/out/pentagon-count-verified.md"],
}

problem = 0


def exists(path):
    full = os.path.join(ROOT, path)
    return os.path.isfile(full)


print("=" * 72)
print("1) solution.md route citations exist on disk")
print("=" * 72)
for ref in solution_md_refs:
    ok = exists(ref)
    if not ok:
        problem += 1
    print(("  OK  " if ok else " MISS ") + ref)

print()
print("=" * 72)
print("2) checked-claim anchor files exist on disk")
print("=" * 72)
for cid, files in checked_claim_files.items():
    for f in files:
        ok = exists(f)
        if not ok:
            problem += 1
        print(("  OK  " if ok else " MISS ") + f"({cid}) {f}")

print()
print("=" * 72)
print("3) every *.captured.txt referenced in a checked-claim note exists")
print("   (captures that a 'checked' claim rests on but that never landed)")
print("=" * 72)
# For each anchor note, extract any `.captured.txt` / `.txt` reference and check it.
seen = set()
for cid, files in checked_claim_files.items():
    for f in files:
        full = os.path.join(ROOT, f)
        if not os.path.isfile(full):
            continue
        try:
            text = open(full, encoding="utf-8").read()
        except Exception as e:
            print(f"  UNREADABLE ({cid}) {f}: {e}")
            problem += 1
            continue
        for m in re.finditer(r"(?:code/out/[\w./-]+\.(?:captured\.txt|txt|md)|research/out/[\w./-]+\.(?:captured\.txt|txt))", text):
            ref = m.group(0)
            if ref in seen:
                continue
            seen.add(ref)
            ok = exists(ref)
            if not ok:
                problem += 1
            print(("  OK  " if ok else " MISS ") + f"({cid}) {ref}")

print()
print("=" * 72)
print("4) no artfact cited by solution.md is a 0-byte / retracted file")
print("=" * 72)
for ref in solution_md_refs:
    full = os.path.join(ROOT, ref)
    if not os.path.isfile(full):
        continue
    size = os.path.getsize(full)
    flag = ""
    if size == 0:
        flag = "  <-- EMPTY (0 bytes): a capture that never landed"
        problem += 1
    # SUPERSEDED only allowed for the one file solution.md itself flags as retracted.
    if "vc_gate" not in ref:
        try:
            head = open(full, encoding="utf-8", errors="replace").read(2000)
            if "SUPERSEDED" in head or "NOT EVIDENCE" in head or "RETRACT" in head.upper():
                flag = f"  <-- HEADER MARKS SUPERSEDED/RETRACTED ({size}B)"
                problem += 1
        except Exception:
            pass
    print(f"  {size:>8}B {ref}{flag}")

print()
print("=" * 72)
print(f"INTEGRITY PASS RESULT: {problem} problems")
print("=" * 72)
sys.exit(1 if problem else 0)
