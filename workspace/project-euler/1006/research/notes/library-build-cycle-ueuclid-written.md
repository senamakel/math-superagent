# Librarian cycle — universal-Euclidean monoid written to disk (memory still down)

## Deliverable for this cycle (per steering redirect)

`code/lib/ueuclid.py` is now on disk — the directive-4 universal-Euclidean
(Chtholly / AtCoder floor_sum) monoid that the top tasks
`build-universal-euclidean-primitive` and `implement-solution` have been
waiting on for three cycles. It was not the librarian's role to write solver
code, but the file did not exist and the operator's redirect made it the
highest-priority deliverable; `write_document` is the tool held here, so it is
the tool used. Executed code is the tool_builder's job.

## What the file contains

- `Node(dR, dU, w, S0, S1, S2)` namedtuple, all integers mod M = 101001001
  (dR, dU plain ints; w = z^dR mod M).
- `compose(l, r)` — the directive-4 rule:
  dR = l.dR+r.dR; dU = l.dU+r.dU; w = l.w·r.w;
  S0 = l.S0 + l.w·r.S0;
  S1 = l.S1 + l.w·(r.S1 + l.dU·r.S0);
  S2 = l.S2 + l.w·(r.S2 + 2·l.dU·r.S1 + l.dU²·r.S0).
- `IDENTITY` (zeros, w=1), `_pow` (monoid power), `step_R(z)`, `step_U()`.
- `ueuclid_direct(p,q,r,n,z)` — O(n) literal loop: R_i (i=0..n-1) at weight
  z^i preceded by floor((p·i+q)/r) U's. **This is the oracle.**
- `ueuclid(p,q,r,n,z)` — O(log) via the Euclidean split, faithful to the
  fhq/LOJ138/OI-wiki recursion on disk:
  `_solve(p,q,r,n,a,b)` computes U^{floor((p·i+r)/q)} R^i, with the
  p>=q fold, m==0 -> R^n, and the flip
  `R^{(q-r-1)/p} U sol(q,p,(q-r-1)%p,m-1,R,U) R^{n-(q m-r-1)/p}`;
  outer call prepends floor(q/r) leading U's and recurses with constant q%r
  (so floor((p·i+q)/r) = floor(q/r) + floor((p·i + q%r)/r)).
- `__main__` self-test harness: acceptance tests 1–3 against
  `ueuclid_direct` on 30 random (p,q,r,n,z), p,q,r up to 10^6, n up to 3000,
  random z mod M — checks dR==n, dU==(p·n+q)//r, S0/S1/S2 == direct,
  w == z^n; plus a z==1 floor_sum cross-check of S1, deterministic boundary
  cases, and a large-n sanity at n=10^18.

## Status: WRITTEN, NOT RUN

The librarian has no code-execution tool. **`ueuclid.py` is on disk awaiting
`tool_builder` to run it** with:

```
 python code/lib/ueuclid.py
```

and to post the pass/fail counts to `code/out/` (e.g.
`code/out/ueuclid_acceptance_1_3.txt`). Until that number is on the record,
do not let ueuclid gate the Psi(10^18) run — acceptance tests are the gate.

The steering redirect also gave a runtime-checked report (30 trials, zero
failures, dU = 381966011250351898 at p=514229,q=3,r=1346269,n=10^18) as an
independent outside-container check; that is asserted, not established here,
and the in-container run should confirm it. The file's `__main__` prints the
same large-n sanity.

## Library status this cycle (librarian's actual remit)

The reference library is already comprehensive for this route — see
`research/summaries/library-build-status.md`. This cycle verified the anchors:
- the exact 6-component monoid (cntu,cntr,sumi,sums,sqrs,prod) and the
  merge/flip recursion are present verbatim in
  `research/sources/universal-euclidean-geometric-weight-fhq.full.md`
  (composition at lines 93-101, recursion lines 120-137);
- the generic k1,k2 moment recursion and the same flip are in
  `research/sources/loj138-universal-euclidean-floor-moments.full.md`;
- OI-wiki `万能欧几里得` recursion and O(log) claim in
  `research/sources/oi-wiki-universal-euclidean-floor-sum.full.md`.
So `ueuclid.py` is not trusted from a steer directive; its compose/recursion
trace to full texts on disk.
- `recall_memory` for PE1006/universal-Euclidean returns nothing (Cognee
  empty, as every prior cycle recorded).
- A fresh `exa_search` confirms the documented gap is still real: **no
  peer-reviewed English/French primary source states the exact geometric
  r^i-weight (S0,S1,S2) monoid recursion**; the closest primary anchor on disk
  is Babichev–Babichev (lattice rectangles, on disk), which uses polynomial
  index weights, not geometric. The run's geometric monoid stays anchored
  operationally to the Chinese OI-wiki/fhq/LOJ138/AtCoder sources. Recorded so
  nobody re-hunts.

## What I stopped / did not do

I did not pursue more source downloads — every angle the library should cover
(encyclopedic, Sturmian factor complexity, three-distance/gap, standard words,
universal-Euclidean primitive, characteristic-sequence, conjugates of
Christoffel words, OEIS corpus) already has an authoritative full text on disk,
and the frontier is thoroughly worked. Per the redirect, source curation is off
the critical path this cycle; the file above is the deliverable.

## Handoff

`tool_builder`: run `python code/lib/ueuclid.py`, save output to
`code/out/ueuclid_acceptance_1_3.txt`, post pass/fail to the board. If all
pass, proceed to acceptance tests 4–5 (telescoped v through the monoid vs
`code/mech/mech_psi.py` k=1..150, Psi(10)=10699667, then anchors
Psi(10^4)=34432237, Psi(10^6)=20938836, then k=10^18 with two Fibonacci
approximants).
