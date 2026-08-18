# Scholar digest — this cycle: ueuclid acceptance-gate API mismatch + position-theorem anchor

## What this cycle did

The library was already fully digested from prior cycles (every `research/sources/*.full.md`
has a statement-level note; all four research requests carry `answers:` in claim blocks).
This cycle audited the **current build gate** — the universal-Euclidean monoid that the
open task `build-universal-euclidean-primitive` / `implement-solution` have been blocked
on — and found a concrete, blocking inconsistency plus confirmed the status of the
load-bearing position claim.

## Finding 1 (blocking): the acceptance harness for ueuclid is stale / cannot import the module

`code/lib/ueuclid.py` exposes exactly: `M`, `Node` (NamedTuple dR,dU,w,S0,S1,S2),
`IDENTITY`, `compose`, `_pow`, `step_R`, `step_U`, `ueuclid_direct`, `ueuclid`,
`floor_sum_plain`. It is **self-consistent**: its `__main__` runs acceptance tests 1–3
(30 random (p,q,r,n,z) vs `ueuclid_direct`, S1 vs plain floor_sum at z=1, deterministic
boundary cases, and a large-n sanity at n=10^18), all against `ueuclid_direct`.

But **both** external harnesses in `code/out/` import names that DO NOT EXIST in the
current module:

- `code/out/test_ueuclid.py` line 18: `from lib.ueuclid import M, Node, identity, compose, chain, pow_node, ueuclid, ueuclid_direct` — `identity`, `chain`, `pow_node` absent → **ImportError**.
- `code/out/ueuclid_tests.py` line 15–16: imports `identity, make_atoms, pow_node, direct_node …` — all absent → **ImportError**.

The captured "20/20 ALL PASS" in `code/out/ueuclid_tests.captured.txt` was produced by
an **older module version** (that had `identity`/`make_atoms`/`pow_node`/`direct_node`/
`chain`), not by the current file. So the recorded pass is stale and does not correspond
to what is on disk now. **If tool_builder runs `python3 code/out/test_ueuclid.py` or
`code/out/ueuclid_tests.py`, the primitive will appear broken by an ImportError that says
nothing about its correctness.**

**Correct acceptance command** (self-consistent, no stale imports):
```
cd /workspace && python3 code/lib/ueuclid.py
```
This runs the module's own `__main__`. If it prints `ALL MONOID TESTS PASSED`, post that.
The stale harnesses should be either deleted or reconciled to the module's API
(`compose`, `_pow`, `step_R`, `step_U`, `ueuclid`, `ueuclid_direct`) by tool_builder /
whoever owns them, so a later run is not misled.

## Finding 2: the position theorem is the closest anchor, but does not verbatim establish Claim 1

Sivasankar & Rama (arXiv:2204.13977, §5) — the source the directive-9 route lists for
"where each length-k factor occurs":

- **Thm 7**: with F(n) ≤ k < F(n+1), the k+1 distinct length-k factors of the (rabbit)
  infinite Fibonacci word, in order of first occurrence, are
  z_j = f[j+1..j+k] for 0 ≤ j ≤ F(n)−1, else f[j+F(n+1)−k .. +k] for F(n) ≤ j ≤ k.
- Convention caveat: the paper's word is the fixed point of h(a)=b, h(b)=ba =
  the **rabbit word** = 0↔1 complement of the problem's S. So Thm 7's factors transfer
  only after complementing digits; the **count** (k+1) is invariant under the swap.
- Relationship to directive-9 **Claim 1** (k+1 distinct length-k factors = the k+1
  CONTIGUOUS windows at positions F_n−k−1..F_n−1 of q_n q_n): Thm 7 confirms the factor
  **set** and its first-occurrence order, but it is about the *infinite* word's
  first-occurrence positions, NOT the specific contiguous windows of the *doubled standard
  word* q_n q_n that Claim 1 asserts. So Thm 7 **supports** the set identity but does not
  verbatim state Claim 1's contiguous-window-position claim. **Claim 1 remains a
  solver-verification task** (against mech_psi/brute), exactly as the steer and the
  thread already say — this cycle re-confirms that honest limitation rather than papering
  over it with a near-miss citation.

## Claim block (reaches derived/CLAIMS.md)

```claim
id: sivasankar-rama-position-theorem
statement: For the rabbit-word convention f (fixed point of a->b, b->ba; the 1<->0 complement of PE1006's S), with F(n) <= k < F(n+1), the k+1 distinct length-k factors of f in order of first occurrence are z_j = f[j+1..j+k] for 0<=j<=F(n)-1, else f[j+F(n+1)-k .. +k] for F(n)<=j<=k (f[i..i+k] the length-k substring starting at i). The factor count k+1 is invariant under the digit complement, so it holds for the problem's word S as well; the explicit first-occurrence list of S's factors is the digit-wise complement of z_j.
hypotheses: F(n) <= k < F(n+1), Fibonacci word in the rabbit (complement) convention
holds-here: yes — the k+1 count transfers (matches brute oracle k=1..20 and the problem's "only k+1 subwords"); the explicit position list for S requires complementing digits
status: asserted
bearing: Supplies the citable position/first-occurrence structure behind directive-9 Claim 1's factor set; confirms the factors are contiguous-window positions but NOT the specific windows of the doubled standard word q_n q_n at F_n-k-1..F_n-1 that Claim 1 asserts (that remains solver-verified against mech_psi/brute)
anchor: research/sources/fibonacci-word-2d-factor-complexity-ar5iv.full.md (Theorem 7, Proposition 4, Section 5)
```

## Contradiction / consistency notes

- No new contradiction with recalled memory. The slope-conflict ledger
  (`steer-d2-literal-slope` vs `mechanical-word-digit-rule`) remains the standing one and
  is resolved in favour of the corrected slope F(n-2)/F(n) -> 1/phi^2, verified.
- The stale-harness issue is a *consistency* defect within the run's own code, not a
  source-to-source contradiction — but it is exactly the kind of thing that makes the
  primitive "look broken" and waste a cycle, so it is flagged first here.

## What is missing (still)

- The monoid has not been RUN in-container (no pass numbers from `python3 code/lib/ueuclid.py`
  are on the record; the captured 20/20 is stale). That single execution is the gate for
  tasks `build-universal-euclidean-primitive` / `implement-solution`.
- In-container verification of the directive-6 anchors 34432237 (k=10^4) / 20938836
  (k=10^6) before they gate the k=10^18 run.
- Lean formalisation of the Euclidean recursion — explicitly gated until the executable
  reproduces the anchors (not this cycle).
