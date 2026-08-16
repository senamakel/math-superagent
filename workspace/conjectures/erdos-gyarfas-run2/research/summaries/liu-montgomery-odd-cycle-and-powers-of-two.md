# Liu & Montgomery 2020 — huge average degree forces all even lengths in a long interval

Source: arXiv:2010.15802 "A solution to Erdős and Hajnal's odd cycle
problem" (Hong Liu, Richard Montgomery). Full text held as landing page /
abstract only; [[liu-montgomery-odd-cycle-and-powers-of-two.full]].

## Erdős–Gyárfás content (part of a broader paper)

Erdős's 1984 strengthening (the belief that *some absolute minimum-degree d*
suffices, i.e. his and Gyárfás's negative belief that for every r there is a
δ ≥ r graph with no 2-power cycle) is **disproved**: an *average degree*
condition is sufficient. Specifically (Bloom's digest of the result):

> if the average degree of G is sufficiently large then there is some large
> integer ℓ such that for every even integer m ∈ [(log ℓ)^8, ℓ], G contains a
> cycle of length m.

Since 2^k is even and lies in that interval for appropriate ℓ, this forces a
2-power cycle. Methods apply to a wide range of sequences, not just powers of
two. (Also solves Erdős–Hajnal's odd-cycle problem: sum of reciprocals of odd
cycle lengths ≥ (1/2 - o(1)) log χ(G).)

## What it implies here

Two readings of the same fact:
1. **The negative belief is dead:** Erdős–Gyárfás are *wrong* that arbitrarily
   high minimum degree fails; there is an absolute degree threshold forcing a
   2-power cycle. So the extremal structure is not "higher degree helps make
   counterexamples," which redirects the structural attack.
2. **The threshold is still gigantic and not the target:** the result needs
   average degree ≫ 3. At δ ≥ 3 the interval force m ∈ [(log ℓ)^8, ℓ] is
   completely unavailable. So this is the *same* obstruction as
   Sudakov–Verstraëte from the other side: it confirms the conjecture is a
   *sparse, uniform-degree* statement that neither average-degree theorem can
   reach. That is precisely the gap — and it is the gap this run must attack
   structurally, not by degree growth.

```claim
id: lm-large-avgdeg-forces-2power
statement: There is an absolute constant such that every graph of sufficiently large average degree has, for some large ℓ, cycles of every even length m ∈ [(log ℓ)^8, ℓ], hence a cycle of length a power of two.
hypotheses: average degree sufficiently large (absolute constant)
holds-here: no — at δ ≥ 3 the average-degree hypothesis fails
status: proved (in source)
bearing: disproves Erdős–Gyárfás's own negative belief; but does not reach δ ≥ 3
anchor: research/sources/liu-montgomery-odd-cycle-and-powers-of-two.full.md
answers: whether-large-min-degree-suffices (no—the tool is average degree)
```

```claim
id: lm-odd-cycle-reciprocals
statement: If G has chromatic number k then Σ_{ℓ ∈ C_odd(G)} 1/ℓ ≥ (1/2 - o_k(1)) log k; asymptotically optimal. Solves Erdős–Hajnal's odd cycle problem.
hypotheses: chromatic number k
holds-here: no (not the E–G frame)
status: proved
bearing: context only
anchor: research/sources/liu-montgomery-odd-cycle-and-powers-of-two.full.md
```
