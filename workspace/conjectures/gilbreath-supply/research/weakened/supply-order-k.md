# SUPPLY — the correlation-order budget ladder

**This ladder owns GOAL.md priority 3: the budget.** It does not build the
functional, price it, or touch the primes — that axis is owned by
`supply-k-functional.md`, and this ladder hands off to it at the top.

Why a separate ladder: the second pass's central fact is that `Φ` provably sees
structure up to correlation order `K*(n) ≈ ⌈n/2⌉` (`research/REOPENED.md`), but
the budget is *measured to n=20 only*, with a flagged `n=5` mismatch
(`K*(5)=2`, not `⌈5/2⌉=3`). GOAL.md priority 3 makes "determine whether `K*`
really is `⌈n/2⌉` or merely close" an explicit target, and it is attackable
today — by exact computation at small `n` plus a structural argument that
defeats the `2^n` search. That is a weakened target: the full goal with the
functional, the pricing, the primes, and the certification all switched off.

**Definition of `C_K`** (pinned from the witness data): `C_K(h)` is the
empirical count vector of length-`(K+1)` consecutive blocks of the binary
string `h` — i.e. the `(K+1)`-gram counts, with `2^{K+1}` components. Two
strings are in the same `C_K`-fiber iff they have identical `(K+1)`-gram
counts. The witness checks this: a single `1` at any interior position of a
length-8 string has 2-grams `(00)×5, (01)×1, (10)×1, (11)×0`, so `C₁ = (5,1,1,0)`
independent of position. **`K*(n) := min{K ≥ 1 : S² is constant on every
C_K-fiber of F₂ⁿ}`** — the smallest correlation order at which the fold's
second moment factors through the `(K+1)`-gram statistics. Here
`S(n) = (n−2) − 2·ν₂(n)` is the signed fold excess (claim
`excess-is-negative-character-sum`), so `S²` and `ν₂` differ by a fixed affine
map and have identical fibers.

```ladder
goal: Determine K*(n) := min{K ≥ 1 : S² is constant on every C_K-fiber of F₂ⁿ} exactly for all n — the correlation-order budget of the SUPPLY fold, and the enabling fact for any K>1 functional (GOAL.md priority 3). This is the second-pass goal with the functional, the pricing, the primes, and the certification all switched off.
difficulties: functional-construction, arithmetic-price, primes-input, certification, exponential-search, n-finite-evidence
status: open
```

- `functional-construction` — building the actual separating functional `F`
  (deferred to `supply-k-functional.md`); the budget only needs `S²` and its
  fibers.
- `arithmetic-price` — pricing a functional below positive mod-4 switch density
  (deferred); the budget is pure combinatorics of `Φ_n`, no arithmetic.
- `primes-input` — the real prime gap-parity string (deferred); the budget is
  over all of `F₂ⁿ`.
- `certification` — turning the functional into `ν₂(n) ≥ c·n` (deferred).
- `exponential-search` — the naive check "does there exist a pair with equal
  `C_K` but different `S²`" enumerates pairs over `2^n` strings; cost grows
  with `2^n`, which is exactly the stated bound's way of defeating the naive
  method, and the obstruction the structural argument must beat.
- `n-finite-evidence` — even a correct table to `n = N` is finite evidence, not
  an all-`n` theorem; the closed form must be proved, not fitted.

```rung
id: R-k1-witness
statement: There exist n and distinct binary strings h, h' with identical C₁ (identical 2-gram counts) but different fold weight. Concretely at n=8: h=00000010 and h'=00000100 both have C₁=(5,1,1,0), yet ν₂(h)=3 and ν₂(h')=4 (S²=0 vs 4, S=0 vs −2). Hence S² is NOT a K=1 functional, and K*(8) ≥ 2.
off: functional-construction, arithmetic-price, primes-input, certification, exponential-search, n-finite-evidence
stance: settled
merge: Promote "one witness" to "the measured budget table". First move is R-kstar-measured-n20. Settled by collapse-witness-n8-kstar-ge-2.
```

```rung
id: R-kstar-measured-n20
statement: For n = 4..20 the measured value of K*(n) is n=4→2, n=5→2, n=6→3, n=7→4, n=8→4, n=9→5, n=10→5, n=11→6, n=12→6, n=13→7, n=14→7, n=15→8, n=16→8, n=17→9, n=18→9, n=19→10, n=20→10 — i.e. K*(n) = ⌈n/2⌉ for every n in 4..20 EXCEPT n=5, where K*(5)=2 ≠ ⌈5/2⌉=3. In particular the budget reaches ⌈n/2⌉ = 10 at n=20, far past the K=1 that the eight first-pass routes were confined to.
off: functional-construction, arithmetic-price, primes-input, certification, exponential-search
stance: settled
merge: This is imported-measured, not re-derived with the canonical oracle in this workspace, and the n=5 mismatch is flagged, not explained. Turn `exponential-search` back on: extend the table past n=20 by a structural (non-2^n-enumerating) argument that also explains the n=5 exception. First move is R-kstar-beat-exhaustion. Settled by kstar-n20-measured-table.
```

```rung
id: R-kstar-beat-exhaustion
statement: Extend the measured table of K*(n) past n=20 by a structural argument that does not enumerate pairs over all 2^n strings, and explain the n=5 exception (K*(5)=2, not ⌈5/2⌉=3). Concretely: for n up to some larger N (say 30), determine K*(n) from a formula in the submask-XOR / run-endpoint coordinates of the fold rather than from a 2^n pair search, and state which structural fact makes the n=5 value 2.
off: functional-construction, arithmetic-price, primes-input, certification
stance: open
merge: Turn `n-finite-evidence` back on: the extended table, even to n=30, is still finite. Convert the structural argument into a proof valid for all n — first move is R-kstar-closed-form. Expected bite: `exponential-search` — this is the rung where the naive 2^n pair search dies and the structural fact (which correlations C_K actually captures, which coordinate changes S² is invariant under) must take over. The n=5 exception is the natural first test of that structural fact.
```

```rung
id: R-kstar-closed-form
statement: It is PROVED for all n ≥ 2 that S² is constant on every C_K-fiber for K ≥ K*(n) and non-constant on some C_{K−1}-fiber for K ≤ K*(n), with K*(n) given exactly — if the answer is K*(n) = ⌈n/2⌉ for all n ≥ 4 except n=5 (where K*=2) and K*=1 for n≤3, state it with the exception proved; if not, state the correct closed form and its full exceptional set. No functional beyond S², no arithmetic, no primes, no certification.
off: functional-construction, arithmetic-price, primes-input, certification, exponential-search, n-finite-evidence
stance: open
merge: This is the terminal rung of this ladder: every budget difficulty is off. Turn `functional-construction` back on and hand off — the budget now says exactly how far past pairs a functional may reach, which is the input `supply-k-functional.md`'s R-k-functional needs to beat `k1-collapse`. First move: from the theorem's witness family, write the separating functional F in submask-XOR coordinates (claim `no-standalone-switch-sign-in-squared-excess` already shows S²'s off-diagonal terms are products of ≥2 switch signs, order ≥2). On exhaustion here, the next ladder's R-k-functional becomes attackable with the budget in hand.
```
