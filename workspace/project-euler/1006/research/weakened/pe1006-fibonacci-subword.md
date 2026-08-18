# PE1006 — Ψ(k): sum of squares of the decimal values of the Fibonacci subwords of length k

Notation (from `problem.md`): S_0=0, S_1=01, S_n = S_{n-1} S_{n-2}; a *Fibonacci
subword* is a contiguous substring of some S_n. For each length k there are
exactly k+1 Fibonacci subwords; interpreting each as a decimal number (leading
zeros ignored) and squaring gives values V_1..V_{k+1}, and
Ψ(k) = Σ V_i^2. Oracle: Ψ(3)=20302 (subwords 001,010,100,101 → values
1,10,100,101 → 1+100+10000+10201); Ψ(10) ≡ 10699667 (mod 101001001). Target:
Ψ(10^18) mod 101001001.

This ladder replaces an earlier draft whose rungs are all stale: it claimed no
brute oracle had been run and listed the factor-count and small-k rungs as the
open frontier. In fact the run has already climbed the structural ladder — the
brute oracle is verified, the k+1 Sturmian factor structure is claimed and
Lean-formalised, and the full second moment (leading zeros, squares, power-10
weights, mod M) is computed exactly to k=400 by `code/mech/mech_psi.py`
(== brute k=1..50). The rungs below mark those as `settled` and locate the real
frontier in the scale difficulties.

R4 is now **settled** (this pass): the asserted acceptance anchors
Psi(10^4)=34432237 and Psi(10^6)=20938836 have been recomputed in-container by
the independent window/residue route (claim `directive6-anchors-verified-incontainer`,
Evidence: checked, task `directive-6-anchors` done; counts 10001/1000001), and
`phase4-anchors-invalid` stands — the old collapse values 16242174/77578256 are
overruled. R4 was the gate for R5 and R5a; the gate is crossed.

R5a is new this pass: until now nothing on the ladder isolated the `square
second moment` difficulty. The run's own hazard record (directive 8) puts the
highest error risk at the interface between the power-10 digit weights and the
floor-sum monoid — the weight-index (z^0) off-by-one and the dU boundary shift —
and that interface is already live in the FIRST moment (S1 composition) before
any squaring. R5a is the version of R5 with the square switched off: same
monoid, same wiring, same boundary shift, but only the (count, sum x^j,
sum x^j·floor) tuple. Settling it pins the hazard on the easier object, and
turning the square back on is exactly R5.

Note on the primitive's apparent S1/S2 failure: the earlier reading that
`code/lib/ueuclid.py`'s compose had a dU boundary-shift bug
(`ueuclid-incontainer-fails-s1s2`) was a false alarm — the module is 1-indexed
and passes its own acceptance gate (`ueuclid-s1s2-false-alarm-refuted`,
Evidence: checked). The real remaining hazard is the *indexing convention* of
the reduction (which power of 10 the j-th digit carries), which is exactly what
R5a pins against `mech_psi` at small k. `record-ueuclid-main-incontainer`
(done) added the ue0 0-indexed wrapper for that.

```ladder
goal: compute Psi(10^18) mod 101001001, where Psi(k) is the sum of squares of the decimal values (leading zeros ignored) of the k+1 distinct Fibonacci subwords of length k
difficulties: k=10^18, self-similar factor set, leading zeros dropped, square second moment, power-10 weights mod M, O(log) Euclidean monoid primitive
status: open
```

```rung
id: R1-brute-oracle
statement: compute Psi(k) exactly for small k (1 <= k <= ~30) by exhaustive substring enumeration over a finite prefix of the Fibonacci word long enough to contain every length-k subword, keeping the full problem shape (decimal reading, leading zeros dropped, squares, power-10 weights mod M). Must reproduce Psi(3)=20302 and Psi(10) mod 101001001 = 10699667, and factor count exactly k+1.
off: k=10^18, O(log) Euclidean monoid primitive
establishes: verified by executing code/brute.py in-container — Psi(3)=20302, Psi(10) mod M = 10699667, factor count exactly k+1 for k=1..20 (both statement examples reproduced). Recorded in GOAL.md and code/out/brute_oracle_results.md.
stance: settled
merge: done — the brute oracle held; the difficulty the run then kept structural was identifying WHY there are k+1 factors and HOW to sum their squares without scanning S_n.
```

```rung
id: R2-factor-structure
statement: prove and verify (for small k) that the infinite Fibonacci word is Sturmian and has exactly k+1 distinct factors of length k, giving the structure that characterizes the objects Psi sums over. No decimal values, squares, or weights are involved.
off: k=10^18, leading zeros dropped, square second moment, power-10 weights mod M, O(log) Euclidean monoid primitive
establishes: claims fibonacci-sturmian-complexity / governing-factor-complexity / governing-sturmian (Morse–Hedlund minimal complexity p(s,n)=n+1 for Sturmian), each source-backed; brute-verified factor count k=1..20; Lean-formalised in code/lean/pe1006_psi_G1_sturmian_factor_structure and G1_factor_chain.
stance: settled
merge: done — the factor structure is a theorem of the run. Reintroduces the decimal reading of each factor, i.e. the place weights and the leading-zero issue.
```

```rung
id: R3-mechanical-second-moment
statement: compute the full second moment Psi(k) with the real shape (self-similar factor set, leading zeros dropped, decimal reading, squares) for small-to-moderate k by the mechanical-word (Sturmian) construction, with two independent formulations of the sum agreeing and exact integer arithmetic — not yet at the astronomical scale, and not yet through an O(log) evaluation.
off: k=10^18, O(log) Euclidean monoid primitive
establishes: verified by executing code/mech/mech_psi.py in-container — arc-midpoints (A) and left-limits of the telescoped v (B) formulations agree; exact Fractions; slope-insensitive; == brute k=1..50, == recorded exact k=1..25, == recorded residues k=1..400 mod M, matches Psi(10)≡10699667. Captured in code/out/mech_psi.captured.txt.
stance: settled
merge: done — the full second moment with its real shape is a settled statement up to k=400. What remains is scaling the same sum to the boundary.
```

```rung
id: R4-moderate-scale-anchors
statement: compute the full second moment Psi(k) by the valid direct mechanical method at moderate k = 10^3, 10^4, 10^6 and confirm in-container the asserted acceptance anchors Psi(10^4) mod M = 34432237 (count 10001) and Psi(10^6) mod M = 20938836 (count 1000001); also confirm the phase4-anchors-invalid conclusion that the old collapse values 16242174 / 77578256 are wrong at these k. O(k^2) big-integer work is still feasible at these sizes.
off: k=10^18, O(log) Euclidean monoid primitive
establishes: verified in-container by the independent window/residue route (code/out/verify/window_residue_route.py + captured) — Psi(10^4)=34432237 (count 10001), Psi(10^6)=20938836 (count 1000001), Psi(3)=20302, Psi(10)=10699667, k=1..60 == brute.py. Found: single-modulus dedup is insufficient (k=10: factors 101001001 and 1010010010 both residue 0; k=10^6 single-count 995071 vs true 1000001) — the fix is two true sliding residues mod M and mod M2, which is what the route uses. Claim directive6-anchors-verified-incontainer (Evidence: checked). Old anchors 16242174/77578256 overruled (phase4-anchors-invalid).
stance: settled
merge: done — the anchors hold in-container and task directive-6-anchors is done; these are the exact acceptance numbers the O(log) monoid must reproduce before 10^18. Turning the O(log) Euclidean monoid back on must reproduce exactly 34432237 and 20938836 — and R5a is the rehearsal that pins the indexing at small k first.
```

```rung
id: R5a-olog-monoid-first-moment
statement: evaluate the FIRST moment Psi_1(k) = sum of the decimal values (leading zeros ignored) of the k+1 distinct length-k Fibonacci subwords — the goal's shape with the squaring removed — through the universal-Euclidean monoid carrying only (count, sum x^j, sum x^j·floor), x = 10^-1 mod M, fed by the arc-midpoint mechanical construction (formulation B of code/mech/mech_psi.py, same rational slope F(n-2)/F(n), same denominator threshold k=1..150 gate). Checks: S1-composed Psi_1(k) == mech_psi first-moment values at k=1..150 exactly; == brute first-moment at small k; the z=1 case collapses to plain AtCoder floor_sum; and the weight-index convention is pinned by comparing the monoid's per-digit power against the telescoped v identity at small k.
off: k=10^18, square second moment
stance: open
merge: the monoid's S1 composition (l.S1 + l.w·(r.S1 + l.dU·r.S0)) is where the digit-weight off-by-one and the dU boundary shift live (directive 8's hazard). The primitive on disk is 1-indexed and passes its own gate (ueuclid-s1s2-false-alarm-refuted); for the 0-indexed Psi wiring use the ue0 wrapper added in record-ueuclid-main-incontainer. Pinning the convention on the first moment against mech_psi settles the hardest part of the primitive on the easier object. Turning `square second moment` back on is R5: add the S2 composition with its 2·l.dU·r.S1 and l.dU^2·r.S0 terms (composition formulas already proved: claim monoid-composition-formulas-verified), and R5 must reproduce the R4 anchors 34432237 / 20938836 before any run at 10^18.
```

```rung
id: R5-olog-monoid
statement: evaluate the same geometrically weighted second moment through the universal-Euclidean (Chtholly / AtCoder floor_sum) monoid — the (count, sum x^j, sum x^j·floor, sum x^j·floor^2) tuple over the arc representatives, x = 10^-1 mod M — and match, in negligible time: Psi(10)≡10699667, Psi(k) vs mech_psi at k=1..150, and the verified R4 anchors 34432237 (k=10^4) and 20938836 (k=10^6). The last move of this rung is the goal itself: dial k to 10^18 with a Fibonacci approximant whose denominator exceeds 10^18 and confirm stability across two approximants.
off: k=10^18
stance: open
merge: this switches back on the O(log) floor-sum difficulty — the digit-weight convention and the S2 squared-floor term are where a wrong implementation shows up — on top of R5a's pinned S1. Once it reproduces the two anchors in negligible time, the only difficulty left is the k=10^18 scale itself, which the monoid absorbs by construction; the approximant-stability check (two independent Fibonacci denominators > 10^18) is what closes it.
```
