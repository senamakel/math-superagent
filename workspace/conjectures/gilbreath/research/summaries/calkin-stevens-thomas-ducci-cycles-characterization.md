# Calkin–Stevens–Thomas — A characterization for the length of cycles of the N-number Ducci game

**Full text:** `research/sources/calkin-stevens-thomas-ducci-cycles-characterization.full.md`
**Source URL:** https://www.fq.math.ca/Papers1/43-1/paper43-1-7.pdf
**Published:** Fibonacci Quarterly 43.1 (2005) 53–59.

The Ducci map on cyclic n-tuples, `D(x) = (|x1−x2|, |x2−x3|, …, |xn−x1|)`. Core reduction (due to Ehrlich; quoted here): every integer Ducci sequence eventually reaches a **simple vector** `k·(x1..xn)` with `xi ∈ {0,1}` and constant `k`. So the map's asymptotics reduce to the **linear** map over Z₂, `Dx = (x1+x2, x2+x3, …, xn+x1) mod 2 = (I + S_L)x`.

**Main results (exact statements):**
- **Theorem 2.1:** for `v ∈ Z₂ⁿ` with minimal annihilating polynomial `µv(λ) = λᵏ·µ̃v(λ)` (`µ̃v(0) ≠ 0`), the k-th iterate lies in a cycle whose length is `c = ord(µ̃v)` — the order of the non-nilpotent part of the minimal polynomial. This gives the complete cycle-length structure: all periods are orders of the divisors of the minimal polynomial of the map.
- **Characteristic polynomial / minimal polynomial of the map:** `µn(λ) = (1+λ)ⁿ + 1` over Z₂. The maximal cycle length for cyclic length n is the order of this polynomial.
- **Ehrlich's divisibility conditions re-proved:** for odd n with `c1 = 2^j − 1` (j = order of 2 mod n), the maximal period `c | c1`; and if `n | 2^m + 1` (with minimal such m), `c | c2 = n(2^m − 1)`, and `c2 | c1` (j = 2m then). Ehrlich's examples n = 37, 95, 101, 111 show c can be a proper common divisor.
- **Table 1:** exact cycle-length lists for n ≤ 40. E.g. n = 2,4,8,16,32 have single cycle of length 1 (zero vector only); n = 3: {1,3}; n = 5: {1,15}; n = 9: {1,3,63}; n = 17: {1,85,255}.
- Classical fact restated: **cyclic length n reaches the zero vector for all starts iff n is a power of 2** — the proof is `(I+S_L)^{2^r} = I + S_L^{2^r} = I + I = 0` over Z₂ since all inner binomial coefficients are even. For n ≠ 2^r every start converges to a (nonzero) cycle.

**What this establishes for this run:**
- The run's Rule-90 interior (`rule90-interior-xor`, halved {0,2} entries evolve by XOR = Pascal mod 2) is the **same linear map** this paper studies; the paper is an independent, primary, peer-reviewed source for the mod-2 linearization and for the exact cycle structure of the binary Ducci map — which is precisely what a *cyclic* truncation of a Gilbreath row would do.
- **Critical boundary for the approaches:** all of Calkin–Stevens–Thomas (and the classical Ciamberlini–Marengoni criterion) concerns **cyclic** n-tuples with wraparound `|xn − x1|`. The Gilbreath triangle has **no wraparound**: row k has one fewer entry than row k−1, and its right end carries no constraint. So the power-of-2 nilpotence theorem does **not** transfer to the half-infinite object; it bounds what a cyclic model can say. Any claim importing "Ducci ⇒ zero" into Gilbreath must first state how the missing wraparound is handled — Eppstein's anti-Gilbreath construction is exactly the demonstration that the half-infinite case behaves differently.
- The "eventually simple" reduction is the same statement as the run's observation that the tail of a row arrives in {0,d} form; it confirms the CHT obstruction framing (long {0,d}-blocks) at the level of single rows.

**Status:** sourced (peer-reviewed, Fibonacci Quarterly); statements quoted exactly; the transfer from cyclic to half-infinite is this run's own deduction, not in the paper.