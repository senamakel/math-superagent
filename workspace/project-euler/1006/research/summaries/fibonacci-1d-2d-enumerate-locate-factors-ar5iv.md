# Sivasankar & Rama, "Fibonacci Sequences of 1D, 2D Words: Enumerating and Locating the Factors of the Fixed Points" (arXiv:2207.04304)

**Source:** https://ar5iv.labs.arxiv.org/html/2207.04304 (arXiv:2207.04304, full text converted from HTML). Authors: M. Sivasankar and R. Rama, Dept. of Mathematics, IIT Madras. 2022, 0 citations (new).

Replaces the structural digest. This is the **position/location theorem source** for the 1D Fibonacci word — the axis prior library-build cycles recorded as thin ("directive 9's contiguous-window claim is NOT stated verbatim in any held source"). This paper states it verbatim (both as a conjugate-prefix theorem, Lemma 2, and as a contiguous-window theorem, Proposition 1), so it is the primary anchor for the contiguous-window reformulation of Ψ(k).

## Convention note (READ FIRST)
The paper uses f_0 = a, f_1 = b, f_n = f_{n-1}f_{n-2} in Lemma 2 and f_0 = a, f_1 = ab, f_{n+1} = f_n f_{n-1} in §5 — the **rabbit-word / 1↔0 complement convention** (`f_∞ = abaababaabaab…`), the *complement* of PE1006's S limit `0100101001001…`. This does not change the *set* of length-k factors (factor sets are invariant under digit complement and under the reversal/rabbit convention), so the position theorems apply to PE1006's word with cautiously translated start positions. The run's slope is α = 1/φ² for PE1006's digit convention; the paper's slope is the complementary mechanical word. Check small-k against `mech_psi` before relying on the exact position indices numerically.

## Lemma 2 (Chuan–Ho position theorem, conjugate-prefix form; ref [10])
Let f_0 = a, f_1 = b, f_n = f_{n-1}f_{n-2}, F(n) = |f_n|, and define the "special conjugate"
  q_n = T^{F(n)-1}(f_n) if n even,  T^{F(n-1)-1}(f_n) if n odd,
where T is the left rotation (T(a_1…a_n) = a_2…a_n a_1) and T^{-1} the right rotation.
Then for each k with `1 ≤ k < F(n)`, the **k+1 prefixes of length k of T^0(q_n), T^{-1}(q_n), …, T^{-k}(q_n)** are the **k+1 distinct factors of f_∞ of length k**.
Example 2 (k=4): q_4 = babaa; the 5 length-4 prefixes of babaa, ababa, aabab, baaba, abaab are baba, abab, aaba, baab, abaa — the 5 distinct length-4 factors. This matches the conjugacy/rotation description of the k+1 factors at k = F(n)-1 (the F_n rotations of the standard word truncated to k letters, directive 1's domain).

## Proposition 1 (the CONTIGUOUS-WINDOW position theorem; ref [10])
Let `n ≥ 2` and `F(n) ≤ k < F(n+1)`. Then the **prefixes of length k of T^i(f_{n+1})**, for
  `i ∈ {0, 1, …, F(n)-1} ∪ {F(n+2)-k-1, F(n+2)-k, …, F(n+1)-1}`,
are the **k+1 distinct factors of f_∞ of length k**.
This is exactly the structure directive 9's contiguous-window reformulation needs: the k+1 distinct length-k factors are the contiguous windows (prefixes of rotations = contiguous length-k windows of the standard word f_{n+1} at the stated rotation indices), grouped as a "front block" of F(n) windows and a "tail block" of k - F(n) + 1 windows at positions F(n+2)-k-1 .. F(n+1)-1. This matches Sivasankar–Rama's Theorem 7 (already in the library) and gives the explicit window-range for the prefix-sum transfer-matrix route.

## §5 Occurrence (location) formula
With the rabbit convention f_0=a, f_1=ab, F(n)=|f_n|, and g_n = f_n minus its last two letters (truncated Fibonacci word), 𝒵_n = nonnegative integers with no Fibonacci numbers F(0)..F(n-1) in their Fibonacci (Zeckendorf) representation:
  occ(u) = occ(g_n) ⊞ first-occ(u) = 𝒵_{n-1} ⊞ first-occ(u)
where n is such that g_n is the shortest truncated Fibonacci word containing factor u, and ⊞ is set-wise addition of the shift first-occ(u). Example: occ(abab) = 𝒵_4 ⊞ 3 = {3, 11, 16, 24, 32, …}.
This gives the *exact* location sets of each length-k factor in terms of Zeckendorf representations — the same numeration axis as the run's Ostrowski/Zeckendorf knowledge (Fici, Hieronymi, richomme).

## Other content
The paper is largely about the **2D Fibonacci word** f_{∞,∞} (Fibonacci arrays): DAWG enumeration (Theorem 1, Corollary 1), enumeration by conjugation (Proposition 2 = the 2D analogue of Prop 1), FRAME-based location of 2D factors, and factor complexity/location of the fixed points of Fibonacci sequences of words (§6–7). The 1D results above are the load-bearing content for this run; the 2D machinery is adjacent and not needed for Ψ(k).

## Bearing on PE1006 / directive 9
- **Positive:** Prop 1 is the missing citable statement for the contiguous-window position claim: "the k+1 distinct length-k factors = the length-k windows at a prescribed finite set of rotation indices of f_{n+1} (F(n) ≤ k < F(n+1))." Together with the already-held Sivasankar–Rama Theorem 7 (arxiv:2204.13977) and the conjugate-Christoffel bridge (Bugeaud–Reutenauer), the library now anchors the finite/position side from a primary source, not just by the solver's own verification.
- **Caveat:** the paper's stated *conjugate-prefix* window indices are in the rabbit convention and post-rotation (T^i(f_{n+1})); directly mapping them onto PE1006's 0/1 characteristic convention + absolute prefix positions of q_n q_n (directive 9's `r = F_n-k-1 .. F_n-1`) still needs the small-k check against `mech_psi`, which the run already does as a solver task. This source **supplies the theorem**; it does **not** replace the verify-in-container step.
