# Wen & Wen — Some Properties of the Singular Words of the Fibonacci Word (1994)

<!-- source: file research/sources/wen-wen-singular-words-fibonacci-word-1994.full.md (Theoret. Comput. Sci., likely 1994; no URL captured in file — verify before citing) | read 2026-08-19 -->

Full text: `research/sources/wen-wen-singular-words-fibonacci-word-1994.full.md`

## What it establishes

**Convention.** σ(a)=ab, σ(b)=a; F_n = σⁿ(a), so F_0=a, F_1=ab, F_{n+1}=F_nF_{n−1}; f_n = |F_n| = n-th Fibonacci number; F_∞ = lim σⁿ(a) = the Fibonacci word. This is the a↔b complement of PE1006's S_∞ (S has 0 where this has 1). C_k(w) = k-th conjugate, C(w) = full conjugacy class (all |w| conjugates distinct since F_n is primitive).

**The length-f_n factor set (Lemma 2 + surrounding).** For each n ≥ 1: Ω_{f_n} = C(F_n) ∪ {w_n}, i.e. the f_n-length factors of F_∞ are exactly the f_n conjugates of F_n **plus exactly one further word w_n = αF_nβ⁻¹** (where αβ is a suffix of F_n), called the **n-th singular word** w_n. w_n ∉ C(F_n) (different letter counts: L(w_n) = (f_{n−1}+1, f_{n−2}−1) if n odd, (f_{n−1}−1, f_{n−2}+1) if n even).

**Singular-word structure (Property 2, Theorem 1, Theorem 2).**
- w_n = w_{n−2}w_{n−3}w_{n−2} (n ≥ 1); w_{2n−1} = a·u·a, w_{2n} = b·v·b; w_n is a palindrome, primitive, not a product of two palindromes; w_n² ⊀ F_∞; no proper conjugate of w_n is a subword.
- Theorem 1: F_∞ = ∏_{j=−1}^∞ w_j (the whole word is the product of its singular words; w_{−2}=ε, w_{−1}=a, w_0=b).
- Theorem 2: F_∞ = (∏_{j=−1}^{n−1} w_j) w_{n,1} z_1 w_{n,2} z_2 … where z is the Fibonacci word over Σ_n = {w_{n+1}, w_{n−1}}; the adjacent singular words of one order are **positively separated** with gap d(w_{n,k}, w_{n,k+1}) ∈ {f_{n+1}, f_{n−1}} (Corollary 2).

**Theorem 3 (powers).** w_n² ⊀ F_∞; (C_k(F_n))² ≺ F_∞ for 0 ≤ k ≤ f_n−1; no u with f_{n−1} < |u| < f_n has u² ≺ F_∞; (C_k(F_n))³ ≺ F_∞ iff 0 ≤ k ≤ f_{n−1}−2; nothing has a 4th power.

**Theorem 5 (special words, Berstel's theorem reproved).** w ≺ F_∞ is a special word (wa, wb both factors) **iff w is a suffix of F_n** for some n ≥ 0. Proof gives the complete length-|u| factor census for f_k < |u| ≤ f_{k+1}: the factors split as s·w_n·t (|st| ≤ f_{n−1}), s·F_n·t, or s·t forms, yielding |Ω_{|u|}| = |u|+1.

**Theorem 6 (overlaps).** For f_n < |u| ≤ f_{n+1}, u ≠ w_{n+1}: u has an overlap iff w_n ⊀ u; the overlap is unique and u = v·v′·v with |v| = |u|−f_n. C_k(F_n) has overlap iff 0 ≤ k ≤ f_n−2.

## Why it matters for PE1006

- **Complete structural description of F_k at k = f_n:** the k+1 factors are the k conjugates of F_n plus the single singular word w_n. This is the finite-word mirror of the run's mechanical construction and of the Sivasankar–Rama rotation theorem (which is the same content in different language: prefixes of rotations of q_n = a conjugate of F_n, plus one more).
- The singular words are exactly the "odd one out" factors (e.g. at k=3, factors 001,010,100,101: 101 = the singular word; at k=10 the same structure holds) — identifying them gives the run a handle on the boundary correction terms in any window/rotation sum.
- Theorem 5's census |Ω_{|u|}| = |u|+1 with the three explicit factor forms is an independent, *finite-word* proof of the complexity count, and the three forms (with s,t suffix/prefix data) are exactly the boundary data a factor-sum evaluation must track.
- Theorem 3's powers and Theorem 6's overlaps bound what can repeat — relevant if any aggregation exploits periodicity.
- Convention caveat: F_∞ = a b a a b a b a a… is the **complement** of S_∞; val is decimal so the complement is NOT a symmetry of Ψ, but the *structural* statements (which strings, positions, powers) transfer under letter swap.

## What it does NOT establish

- No Ψ(k), no decimal weighting, no floor-sum evaluation, no O(log) method.

## Claims anchored here

Corroborates `governing-factor-complexity` (independent finite-word proof of k+1), `fibonacci-unique-special-factor-reverse` (Theorem 5: special words = suffixes of F_n, matching "right-special = reverse of prefix"), `sivasankar-rama-position-theorem` (the conjugate-plus-one structure). No new claim block needed for the run's critical path.
