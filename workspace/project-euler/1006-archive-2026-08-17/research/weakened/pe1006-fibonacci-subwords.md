# PE1006 — Fibonacci subwords: ladder of weakened targets

Ψ(k) is the sum of squares of the k+1 distinct length-k factors of the infinite
Fibonacci word f (limit of 0, 01, 010, 01001, …), each factor read as a decimal
integer (leading zeros contribute nothing, so value = Σ_j bit_j·10^pos_j). The
decimal reading itself and the modulus M=101001001 are part of the definition and
present in every rung; they are conveniences (M has 9 digits, 10 is invertible mod
M since M ends in 1), not difficulties. The four difficulties below are the ones a
weakened version can actually switch off.

```ladder
goal: Ψ(10^18) mod 101001001, where Ψ(k) = sum over the k+1 distinct length-k factors of the Fibonacci word f of (decimal value)^2
difficulties: huge-k, factor-structure, irrational-slope, offset-summation
status: open
```

```rung
id: R-brute-small
statement: For k ≤ 40, compute Ψ(k) exactly by enumerating the distinct length-k substrings of the finite Fibonacci word S_n for n with |S_n| ≥ 2k+1 (e.g. n=12), reading each substring as a decimal integer (value = Σ_{j=0}^{k-1} b_j·10^{k-1-j}, leading zeros ignored), squaring, and summing. Reproduce the two given oracles: Ψ(3)=20302 and Ψ(10) ≡ 10699667 (mod 101001001).
off: huge-k, factor-structure, irrational-slope, offset-summation
stance: open
merge: Turn factor-structure back on. Replace substring enumeration of S_n by an explicit parametrization of the k+1 distinct length-k factors of f. Careful: the naive "windows f[i..i+k-1], i=0..k" is wrong — for k=3 it yields 010,100,001,010 (a duplicate and no 101). Establish the correct indexing (three-gap/Beatty special positions, or the k+1 Christoffel conjugates) and check it reproduces R1 for every k ≤ 40.
```

```rung
id: R-window-param
statement: Establish an explicit parametrization of the k+1 distinct length-k factors of f (three-gap/Beatty special positions, or the k+1 Christoffel conjugates), and for k up to ≈2000 compute Ψ(k) mod M by summing the square of the decimal value over exactly these k+1 words, generated from the recurrence f (substitution 0→01, 1→0) far enough (≈2k+2 bits). Verify equality with R1 at every k ≤ 40.
off: huge-k, irrational-slope, offset-summation
stance: open
merge: Turn irrational-slope back on. Re-express the bits by the floor form f(m)=⌊(m+2)α⌋−⌊(m+1)α⌋ with α=1/φ²=(3−√5)/2 (verified by hand for m=0..6: 0,1,0,0,1,0,1), computed exactly via Fibonacci arithmetic — no floats, and no naive √5 mod M. This is what makes the single-bit sums telescope.
```

```rung
id: R-floor-telescope
statement: For k up to ≈10^6 (where O(k²) modular arithmetic is still feasible), compute Ψ(k) mod M from the floor form f(m)=⌊(m+2)α⌋−⌊(m+1)α⌋ (α=1/φ²), by expanding the square: Ψ(k)=Σ_factors Σ_j f(pos+j)·10^{2j} + 2·Σ_factors Σ_{j<l} f(pos+j)·f(pos+l)·10^{j+l}. The single-bit part telescopes via floor differences (exact Fibonacci arithmetic); the pair part is computed by direct iteration over the k+1 indexed factors. Verify against R2 at every overlapping k.
off: huge-k, offset-summation
stance: open
merge: Turn offset-summation back on. The pair part is the weighted autocorrelation Σ_{d=1}^{k} Σ_{j=0}^{k-d} 10^{2j+d}·#(windows with f(pos+j)=f(pos+j+d)=1); it must be evaluated without iterating over d and j. Find the Fibonacci/Christoffel recurrence or matrix exponentiation (mod M) that collapses this double sum to poly-log k. This is the step expected to bite.
```

```rung
id: R-offset-closed
statement: For moderate k (up to ≈10^7, beyond what O(k²) can reach but checkable against R3 at k≈10^4–10^5), compute Ψ(k) mod M by the closed poly-log method for the weighted pair-correlation sum (offset-summation on), and verify it agrees with R3's direct computation wherever R3 still runs.
off: huge-k
stance: open
merge: Turn huge-k back on. The closed method must then run at k=10^18 with exact modular arithmetic; the only remaining work is pushing the poly-log method (matrix power / Fibonacci recurrence) to the full bound. That statement is the goal, R5.
```

```rung
id: R-full
statement: Ψ(10^18) mod 101001001 — the goal exactly as given.
off:
stance: open
merge: (none — this is the goal; settling R5 exhausts the ladder)
```

**Expected to bite:** `offset-summation`. The factor parametrization (R2) and the
floor/telescoping form (R3) are standard Sturmian-word theory, much of it already
in the library; the genuinely hard step is collapsing the weighted
pair-correlation double sum over all offsets and window positions to poly-log k.
