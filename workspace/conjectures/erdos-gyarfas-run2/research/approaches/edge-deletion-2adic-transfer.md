# Approach — reverse-ear / chord-deletion recursion with 2-adic length transfer

```approach
idea: Recursive decomposition of a 2-connected minimal counterexample by reverse
      ear deletion. A 2-connected graph with δ ≥ 3 equals H + e (a chord e = ab)
      where H is 2-connected and δ(H) ≥ 2; the cycle lengths of G not in H are
      exactly {|P|+1 : P a simple a–b path in H}. The conjecture becomes an
      inductive, 2-adic statement about path lengths: G has a 2^k-cycle iff H has
      one, or H has an a–b path of length 2^k − 1.
mechanism: Whitney's open-ear decomposition (a graph is 2-connected iff it has an
      open ear decomposition, and every open ear added preserves 2-connectivity).
      Take any open ear decomposition P0,…,Pk of a 2-connected graph G; the LAST
      ear Pk has all its internal vertices of degree exactly 2 in G (they are
      introduced by Pk and touched by no later ear). Since δ(G) ≥ 3, Pk has NO
      internal vertices, so Pk is a single edge e = ab joining two vertices of
      H := G − e = P0 ∪ … ∪ P_{k−1}. Hence H is 2-connected (prefix of an open
      ear decomposition), and δ(H) ≥ 2 (only a,b lose a degree: 3 → 2). Cycle
      transfer: cycles through e are in bijection with simple a–b paths in H, each
      contributing length |P|+1, so C(G) = C(H) ∪ {|P|+1 : P an a–b path in H}.
      Since δ(H) ≥ 2 at a and b and H is 2-connected, Menger gives two
      internally-disjoint a–b paths of lengths p, q: G gains cycles of length
      p+1 and q+1, and H already has a cycle of length p+q. The three lengths
      satisfy p+q = (p+1)+(q+1)−2, a genuine 2-adic coupling (v2 of x+y−2 against
      v2(x), v2(y)). Iterating the deletion reaches a MINIMALLY 2-connected core
      M with δ(M) = 2 — this core is NOT in general a cycle (K_{2,3} is
      minimally 2-connected with δ=2); the recursion terminates at the well-known
      (but non-trivial) class of minimally 2-connected graphs.
status: adopted
first-step: (1) Formalise and machine-check the two lemmas the single step rests
      on — "every 2-connected δ≥3 graph has a chord e with G−e 2-connected and
      δ(G−e) ≥ 2", and "C(G) = C(G−e) ∪ {|P|+1 : P an a–b path in G−e}" — in
      code/lean/ (lean_prover + tool_builder). (2) Oracle scan of the committed
      n≤8 2-connected δ≥3 class (READ code/out/g_heart_verify_n8.out and
      code/out/g_heart_verify_n8.md, or run code/out/pattern_gheart_corrected_fast.py
      — NO ad-hoc regeneration of the class): for each graph find the chord e
      whose two internally-disjoint a–b paths give p+1 or q+1 a power of two;
      report the smallest graph where NO deletable chord does this. That graph is
      the induction's exact worst case and names what the next lemma must kill.
speculative: The single-step reduction is standard and provable (derived from
      Whitney's theorem, still to be Lean-checked); the *open content* is proving
      the length-closure {p+1, q+1, p+q} must hit a power of two when the final
      graph has δ ≥ 3. The recursion repackages the conjecture so the δ≥3 vs δ≥2
      boundary is the load-bearing object; it does not yet prove the closure.
precedent: CHECKED (research pass, current run). (1) The reverse-ear / chord-
      deletion view is classical — Whitney's open-ear decomposition (1932), and
      the fact that δ(G)≥3 forces the last open ear to be a single chord is
      exactly "G is 2-connected but NOT minimally 2-connected ⟹ some chord e
      has G−e 2-connected". No library or search source states the cycle-length
      transfer identity C(G) = C(G−e) ∪ {|P|+1 : P an a–b path in G−e} as a
      named tool; it is elementary (cycles through a chord correspond to a–b
      paths in G−e) and only implicit in the ear-based cycle-length literature
      (Ma–Yang 2020; Liu–Ma 2019; Lyngsie–Merker 2021), which all use ears to
      bound/realize ranges or residue classes, never to force a power of two.
      (2) The 2-adic conclusion from p+q=(p+1)+(q+1)−2 (v2(x+y−2) against
      v2(x),v2(y) forcing a 2-power among {p+1, q+1, p+q}): NO source found
      derives this. It is genuinely novel to the run — see "2-adic transfer is
      novel" below. (3) Termination fact "every minimally 2-connected graph has
      δ = 2" is a citable primary theorem: Dirac 1967 (J. Reine Angew. Math.
      228:204–216, doi:10.1515/crll.1967.228.204) and Plummer 1968 (Trans. AMS
      134:85–94, doi:10.1090/s0002-9947-1968-0228369-8); independently
      confirmed by Chartrand–Kaugars–Lick (Proc. AMS 1972).
      Nearest adjacent results that do NOT deliver the transfer, and why:
      Bondy–Vince (1998, ≤2 deg-<3 vertices ⟹ two cycles differing by 1 or 2)
      and Gao–Huo–Liu–Ma (2019, unified: δ≥k+1 gives long APs of x–y path
      lengths with difference 1 or 2) are the closest "couplings", but both
      produce CONSECUTIVE/AP lengths, never a prescribed power of two. This
      reproduces the run's standing obstruction (ROOT §1): interval/consecutive
      machinery cannot hit a 2-power. So the 2-power transfer at the single
      chord step is open content the literature does not cover.

## 2-adic transfer is novel (research check, current run)

Focused search (several angles: reverse ear / chord deletion cycle length
transfer; 2-adic valuation of p+q=(p+1)+(q+1)−2; power-of-two from two
internally-disjoint a–b path lengths; minimal counterexample chord/ear
recursion) found NO source deriving a power-of-two or 2-adic conclusion from
the chord-deletion coupling. The step "2-connected δ≥3 ⟹ last open ear is a
single chord ⟹ H = G−e with δ(H)≥2, and Menger gives two internally-disjoint
a–b paths with p+q a cycle of H while p+1, q+1 are cycles of G, satisfying
p+q=(p+1)+(q+1)−2" is the run's own repackaging. Nothing adjacent reaches the
2-power: the entire generic machinery (Liu–Ma, Gao–Huo–Liu–Ma, Bondy–Vince,
Lyngsie–Merker) produces ranges/residue classes/consecutive lengths. So the
run's open lemma — {p+1, q+1} contains a power of two for some deletable chord,
when G is a δ≥3 2-connected minimal counterexample — is not a known result and
appears to be the genuine new content. State plainly: if this transfer is ever
called "known", it is being conflated with the classical Whitney/Dirac ear
facts, which say nothing about lengths hitting a power of two.
```

## Why this and not the three refuted ones

The three killed candidates all *transferred the object away* and lost the
min-degree-3 guard (tree, cycle-space, edge-count). Research's sharpened fact is
that a minimal counterexample is **degree-3-closed downward but not pinned to
2n−2 edges** — the δ≥3 guard does work beyond degree-3-criticality. This
recursion keeps the δ≥3 condition front and centre: it is *exactly* the
condition that forces the last open ear to be a single edge, which is the only
place the "prescribed sparse length" target becomes an inductive path-length
transfer instead of a range/congruence statement. It is the run's committed
structural-graph-theory method, it is a change of representation (cycles →
chord-addition closure → path lengths with the coupling p+q = (p+1)+(q+1)−2),
and its first step is mechanical today.

## What would falsify the line (attack first — one already found and fixed)

- **Found while attacking (fixed in this file):** the first draft claimed the
  deletion iterates down to a cycle. That is false — K_{2,3} is 2-connected,
  δ=2, and has no edge whose deletion preserves both 2-connectivity and δ≥2, so
  the iteration terminates in the larger class of minimally 2-connected graphs.
  The single-step reduction (G = H+e, H 2-connected δ≥2) is what is actually
  load-bearing and is correct.
- A 2-connected δ≥3 graph in which, for *every* deletable chord e, both shortest
  disjoint a–b path lengths p+1 and q+1 are non-powers and C(H) has no 2-power —
  i.e. the oracle scan finds the induction's worst case at small n and it resists
  all further structure. This does not refute the recursion (a true restatement)
  but it locates precisely where the hard content lives.
- The two load-bearing lemmas failing to machine-check (would mean the reduction
  is wrong, not just incomplete).

## Open content (stated exactly)

Prove: if H is 2-connected with δ ≥ 2, a,b ∈ V(H), and p,q are the lengths of
two internally-disjoint a–b paths (so p+q is a cycle length in H), then for some
such pair one of {p+1, q+1} is a power of two — at least when H = G−e arises by
deleting a chord from a δ≥3 counterexample G. That single lemma, if true, closes
the 2-connected case (backward skeleton `G-heart`) by induction on chords, the
induction terminating at a minimally 2-connected core.
