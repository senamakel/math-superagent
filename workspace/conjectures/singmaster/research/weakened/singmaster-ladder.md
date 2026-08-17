# Ladder — Singmaster's conjecture, weakened by switching off named difficulties

The full-strength target is `N(a) <= B` for an absolute `B`, all `a > 1`,
counted with both mirrors plus the trivial pair (`N(3003)=8`). Every rung
below is that same target with a declared subset of its difficulties switched
off. A weakened rung does **not** imply the goal; it is a smaller problem that
a forward attempt can settle, and its settled state is evidence about which
difficulty was carrying the weight.

```ladder
goal: N(a) = #{ (n,k) : C(n,k) = a } is bounded by an absolute constant B over all a > 1, counting both mirrors (n,k),(n,n-k) and the trivial pair C(a,1)=C(a,a-1), so N(3003)=8 and B >= 8
difficulties: uniform in a, unbounded columns/pairs, boundary regime, ineffective per-pair, infinite family
status: open
```

`uniform in a` — the bound must not grow with `a`; every classical result
(`O(log a)`, AEH, Kane) fails exactly here.
`unbounded columns/pairs` — a representative `(n,k)` can use any column up to
`k <= log2 a`, and two representatives can collide across any pair
`(k1,k2)`; there is no known finite class of colliding pairs to enumerate.
`boundary regime` — the small-`k` region `2 <= k <= exp((log n)^{2/3+eps})`
that MRSTT leaves open, where the multiplicity actually concentrates (every
known high-multiplicity witness sits here).
`ineffective per-pair` — Faltings/Siegel give finiteness of solutions of
`C(x,k1)=C(y,k2)` per fixed pair with no count computable in `(k1,k2)`.
`infinite family` — the Fibonacci-indexed identity `C(n+1,k+1)=C(n,k+2)`
produces infinitely many `a` with `N(a) >= 6`, so `B >= 6` and no argument
may imply a smaller bound.

---

## R1 — finite column budget

```rung
id: R-column-injectivity-bound
statement: For any fixed K >= 2 and any a > 1, the number of representatives (n,k) of a with 2 <= k <= K is at most K-1, uniformly in a. Proof: for each fixed k, C(n,k) is strictly increasing in n for n >= 2k (ratio C(n+1,k)/C(n,k) = (n+1)/(n+1-k) > 1), so a fixed column k contributes at most one n. 3003 achieves 3 columns {2,5,6} against the K=6 ceiling of 5.
off: unbounded columns/pairs, boundary regime, ineffective per-pair, infinite family
stance: settled
settled-by: G-column-injectivity in the boundary-finite-collisions skeleton (goals ledger) and the elementary ratio C(n+1,k)/C(n,k) = (n+1)/(n+1-k) > 1 for n >= 2k; this is the strict-monotonicity fact, no citation needed.
merge: To turn the column budget back on, stop capping all columns and control which columns can actually hit a given a — one needs the collision structure between columns, which is exactly the finite-pair classification that yields R3. This rung is the per-column injectivity fact the whole boundary skeleton rests on (G-column-injectivity is already in the library).
```

## R2 — a fixed small collision pair, effectively solved

```rung
id: R-fixed-solved-pair
statement: For a fixed small pair (k1,k2) (2 <= k1 < k2), the equation C(x,k1)=C(y,k2)=a has only finitely many solutions, and for the solved pairs the full finite list of a-values is known, so the number of a hit by this pair is independent of a. Explicitly complete for (2,3) Avanesov, (2,4)/(2,6)/(2,8)/(3,4)/(3,6)/(4,6)/(4,8) Stroeker-de Weger via elliptic logarithms, (2,5) BMSST hyperelliptic; genus closed form g(m,n)=((m-1)(n-1)+1-gcd(m,n))/2 is proved for all distinct m,n>=2 and genus>1 for every pair except {2,3},{2,4}.
off: unbounded columns/pairs, boundary regime, infinite family
stance: settled
settled-by: claims avanesov-1967-cx3-cy2-complete, sdw-elliptic-logarithms-eight-pairs, bmsst-hyperelliptic-effective-method, deweger-smallk-effective (per-pair complete solution lists) and genus-closed-form-derived-by-riemann-hurwitz (g(m,n) formula for all distinct m,n>=2, genus>1 except {2,3},{2,4}).
merge: To turn unbounded columns/pairs back on, replace "this pair" by "any pair": one needs to know, independent of Faltings' ineffectivity, which pairs can collide at all — the finite/witness classification of boundary-producing pairs that is R3. The per-pair effective results and the genus formula are the evidence here, but they give per-pair finiteness only and never a uniform count.
```

## R3 — boundary pair classification (the hard core)

```rung
id: R-boundary-pair-classification
statement: The set P of unordered pairs {k1,k2}, 2 <= k1 < k2, for which there is a boundary collision C(x,k1)=C(y,k2) with both (x,k1),(y,k2) in the left half (k1 <= x/2, k2 <= y/2) and k1,k2 < exp((log n)^{2/3+eps}) for an admissible eps, excluding the Fibonacci family {k,k+1}, is finite. Equivalently, every non-Fibonacci boundary collision involves columns bounded by a computable K_max.
off: ineffective per-pair, infinite family
stance: open
merge: This is G-nonfibonacci-pair-list, the single open gap in the run's boundary-finite-collisions skeleton. The forward move is the Bilu-Tichy/HPT exceptional classification applied under the MRSTT boundary condition: which (k1,k2) pairs have infinitely many integral solutions at all, intersected with the boundary inequality k < exp((log n)^{2/3+eps}). The Fibonacci family shows pairs genuinely collide at all scales, so it must be carved out explicitly, not assumed away — it is carried by the infinite-family difficulty kept off here.
```

## R4 — boundary multiplicity uniformly bounded

```rung
id: R-boundary-uniform-count
statement: There is an absolute constant C such that, for every a > 1 and every admissible eps in (0,1), the number of nontrivial left-half boundary representatives (n,k) with 2 <= k < exp((log n)^{2/3+eps}) and C(n,k)=a is at most C. Granting MRSTT's interior theorem (at most 2 interior left-half reps, effective and uniform), this yields N(a) <= 2C + 6 (plus the small-a Lane-Clark term below the effective threshold), i.e. Singmaster.
off: ineffective per-pair
stance: open
merge: The interior is handled by MRSTT (the one effective, uniform tool the run has), so this rung needs only R3 plus a bound on how many collisions from the finite pair list and from the Fibonacci family can land on one a. Turning ineffective per-pair back on (allowing R3's classification to be replaced by a non-constructive finiteness) is exactly R5 — which would not be Singmaster.
```

## R5 — the full conjecture

```rung
id: R-full-singmaster
statement: N(a) <= B for every a > 1 with both mirrors and the trivial pair counted.
off:
stance: open
merge: Climbing fully into the goal requires the boundary uniform count (R4) without the effective-tool assumption, i.e. a genuine uniform-in-a, uniform-in-(k1,k2) mechanism that the per-pair genus/Faltings/Siegel results provably cannot supply (effective-methods-wall). This is where the run expects to stop with a genuine partial result (R2, and possibly R3 as a conjecture/R4) rather than the conjecture.
```

---

## Where the weight is

The run has already banked R1 (column injectivity) and R2 (per-pair finiteness
plus the proved genus formula). The rung that first gets hard is **R3**,
because it sits at the interface between the bounded-column effective world
(R2) and the infinite-pair Faltings world: it asks for a *finite classification
of colliding pairs* that no per-pair theorem supplies and that Bilu-Tichy only
gives structurally (as exceptional families) once the boundary condition is
imposed. The difficulty I expect to actually bite is **`unbounded
columns/pairs`** — not uniformity in `a` and not ineffectivity alone, but the
absence of a finite list of pairs to enumerate, with the Fibonacci family
showing collisions at every scale. That rung is where a forward attempt should
be spent.
