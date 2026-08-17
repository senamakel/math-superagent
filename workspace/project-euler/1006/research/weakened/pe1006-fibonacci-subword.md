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
frontier in the scale difficulties: verify the moderate-k anchors in-container,
then build the O(log) Euclidean monoid, then hit 10^18.

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
stance: open
merge: the scripts exist (code/out/verify/check_phase4_anchors.py, check_directive6_anchors.py) but are not yet run; running them settles this rung. Once the anchors hold, turning the O(log) Euclidean monoid back on must reproduce exactly these values before anything is trusted at 10^18 — so this rung is the gate for R5.
```

```rung
id: R5-olog-monoid
statement: evaluate the same geometrically weighted second moment through the universal-Euclidean (Chtholly / AtCoder floor_sum) monoid — the (count, sum x^j, sum x^j·floor, sum x^j·floor^2) tuple over the arc representatives, dU shifts carrying floor values across segment boundaries, x = 10^-1 mod M — and match, in negligible time: Psi(10)≡10699667, Psi(k) vs mech_psi at k=1..150, and the verified R4 anchors 34432237 (k=10^4) and 20938836 (k=10^6).
off: k=10^18
stance: open
merge: this switches back on the O(log) floor-sum difficulty — the dU boundary shift is where a wrong implementation shows up. It is the scale-launched rung: the same sum evaluated without enumerating factors. The last move is to dial k up past every anchor to 10^18 with a Fibonacci approximant whose denominator exceeds 10^18 and confirm stability across two approximants — that is the goal itself, reached when the rung's method runs at the full size.
```
