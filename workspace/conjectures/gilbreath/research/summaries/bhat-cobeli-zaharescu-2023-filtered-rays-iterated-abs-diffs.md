# Bhat–Cobeli–Zaharescu 2023 — "Filtered rays over iterated absolute differences on layers of integers"

**Source:** arXiv:2309.03922v2 (10 Dec 2024) [math.NT]; Chaos, Solitons & Fractals 178 (2024) 114315; doi 10.1016/j.chaos.2023.114315.
**Full text:** `research/sources/bhat-cobeli-zaharescu-filtered-rays-FULLPDF.full.md` [[bhat-cobeli-zaharescu-filtered-rays-FULLPDF.full]] — read THIS, not the `...-2023-...` file, which is only the arXiv abstract page.

## What the paper actually proves (checked against the full PDF)

Setup: u ∈ L (non-negative integer sequences) generates the P-G triangle (each row = absolute differences of the previous); Υ(u) = w = the left-edge sequence; Ψ = row-to-row operator. Mod 2, |a−b| = a+b, so the binary triangle is linear over F₂.

- **Theorem 2 (PROVED, main).** For binary u with generating function f ∈ F₂[[X]], the left-edge map is T(f)(X) = f(X/(1+X))·(1/(1+X)), and **T is an involution: T⁽²⁾ = id, hence Υ²(u) = u** — two left-edge iterations return the sequence. Finite analogue (Thm 3) mod X^N. (The old summary's "involution-like relationship" understated this: it is a genuine involution.)
- **Theorem 4.** Υ⁶(u) = u for every finite/infinite binary u (the helicoid has one layer). Conversely, Υ⁶(u) = u ⟹ u has at most one champion (a term exceeding all earlier terms); one champion is necessary, not sufficient.
- **Theorem 5.** For almost all binary u of length N (all but ≤ ε·2^N), every ray w₀..w_{⌊δN⌋} parallel to the left edge and its mirror rays have 0/1 proportion within [1/2−ε, 1/2+ε], δ = δε > 0. Proved via the involution + Stirling tail bounds.
- **Theorem 6.** For ANY sequence w of non-negative integers there is an increasing square-prime sequence whose P-G western edge has even-indexed entries = w. (A universal-realization result: left-edge shape is class-dependent, not a universal law.)
- **Conjecture 2 (their own, UNPROVED).** On every ray w_j of the prime triangle, ν_d(n) = n/2 ± c√n for d ∈ {0,2}. **Table 1 (computed, primes < 10⁶):** rays w₀..w₉, mod-4 counts, |#0 − #2| ≤ 431 of 78,496 per ray (≤ 0.55%) — strong numerical support for the balanced 0/2 density.

## Hypotheses held here?

Yes for Theorems 2–5 (binary sequences — the run's halved {0,2} interior is exactly the binary F₂ object). The prime-triangle 0/2 density is Conjecture 2, unproved, Table 1 evidence only.

## Bearing on this run

- **Corroborates Route B (Granville ν_2) independently.** BCZ Table 1 (primes < 10⁶, mod 4, rays parallel to the left edge) shows #0 ≈ #2 within 0.55% — the same balanced-0/2 density that Granville's Theorem 5.5 needs as ν₂(q_n−1) ~ n/2 on the right diagonal. ν₂ ~ n/2 is now two-source corroborated (this run's `nu2_granville_check`, BCZ Table 1), not a lone measurement.
- **New exact handle at the mod-2 level:** the F₂ involution Υ² = id is a structural identity for the halved left-edge map; any future mod-2 invariant must respect it.
- Theorem 6 is another anti-universality witness (cf. Eppstein, Colonna deletion): left-edge behaviour is class-dependent, so the primes' special structure (congruential gap constraints) is doing real work.
- Does NOT prove GC; does NOT bound the (2,4)-event rate. The run must not cite it for either.

```claim
id: bcz-2023-left-edge-stabilization
statement: For binary top rows the left-edge operator of the Proth–Gilbreath triangle is an F2 involution: T(f)(X) = f(X/(1+X))·(1/(1+X)) over F2[[X]] and T^2 = id (Thm 2); hence Υ^6(u) = u for all binary u, and Υ^6(u) = u implies u has at most one champion (Thm 4). Almost all binary u of length N have every ray's 0/1 proportion in [1/2−ε, 1/2+ε] (Thm 5). Any prescribed even-indexed western edge is realized by some square-prime sequence (Thm 6). The prime triangle's balanced 0/2 rays are Conjecture 2 (unproved), numerically supported by Table 1 (|#0−#2| ≤ 431 of 78,496 per ray, primes < 10^6).
hypotheses: u binary (Thms 2–5); square-primes (Thm 6); primes (Conj 2, Table 1).
holds-here: yes for the structural binary theorems (the halved {0,2} interior is the binary F2 object); the primes' density statement is conjectural.
status: proved in source (Thm 2, 4, 5; full PDF read this cycle); Table 1 computed by the source; the earlier "stabilizes to at most two values under slow growth" phrasing is the intro's expectation, not a theorem, and is downgraded.
bearing: (a) the F2 involution is the exact structure of the halved left-edge map — a new exact constraint for mod-2 invariants; (b) Table 1 independently corroborates Route B's ν_2 ~ n/2 supply side; (c) Thm 6 is an anti-universality witness for any deterministic general-class claim.
anchor: research/sources/bhat-cobeli-zaharescu-filtered-rays-FULLPDF.full.md
```
