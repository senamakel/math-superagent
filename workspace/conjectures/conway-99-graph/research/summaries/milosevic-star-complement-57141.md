# Milošević, "An example of using star complements in classifying strongly regular graphs" (Filomat 22:2, 2008, 53–57)

<!-- source: https://www1.pmf.ni.ac.rs/pmf/publikacije/filomat/2008/22-2-2008/f22-2-5.pdf -->
<!-- full text: research/sources/milosevic-star-complement-57141.full.md -->

Reproves, by the **star-complement technique**, that there is no srg(57,14,1,4)
([Wilbrink–Brouwer 1983]). It is a λ=1, **k=14** nonexistence, and its local
structure is the *same as the 99-graph's*.

## The structural fact that makes it a close 99 analogue

For srg(57,14,1,4) with λ=1, the **closed neighbourhood N[u] induces the
windmill W₁₄** — 7 triangles sharing the central vertex u. Equivalently the
neighbourhood N(u) is a **perfect matching 7K₂**: the same local structure and
the same valency k=14 as the Conway 99-graph. Only μ differs (4 vs 2). So the
forced local extension around a fixed vertex is *identical* to 99's until the
second-subconstituent edges are decided. This is a closer structural analogue
than srg(85,14,3,2) (which the run currently files as the template): here λ=1
matches, only the μ-branch differs.

## The method (computer-assisted)

Spectrum of srg(57,14,1,4) is [14, 2³⁸, −5¹⁸]. Eigenvalue ξ=2 has multiplicity
m=38, so a star complement has 57−38 = **19 vertices**.
1. Fix u and an exterior vertex v; H = N[u] ∪ {v} is a 16-vertex graph not
   having 2 as an eigenvalue (Lemma 3: any induced subgraph without ξ extends
   to a star complement of ξ).
2. Extend H by 3 vertices "in all possible ways" preserving the srg common-
   neighbour conditions (λ=1: adjacent pairs ≤1 common neighbour; μ=4:
   nonadjacent ≤4), giving **3720 non-isomorphic** 19-vertex candidate star
   complements.
3. For each, build the compatibility graph Comp(C,ξ) (vertices b with
   ⟨b,b⟩=ξ; b′~b″ iff ⟨b′,b″⟩∈{−1,0}); a needed srg corresponds to a clique
   of size 38 = |X| = order 57 − 19. Largest clique found is 31; none reaches
   38 → no srg. Cliquer was used; results are computer-assisted.

## Reconstruction / compatibility theorems (usable general machinery)

- **Reconstruction Theorem**: X star set for ξ iff ξ is not an eigenvalue of C
  = G−X and ξI−A_X = Bᵀ(ξI−C)⁻¹B, so (ξ, B, C) determine G.
- Corollary: for columns b_u of B, ⟨b_u,b_u⟩=ξ and ⟨b_u,b_v⟩∈{−1,0}; ⟨b,b⟩=−1
  → edge, ⟨b,b⟩=0 → nonedge, under the inner product (ξI−C)⁻¹.
- **Lemma 3**: an induced subgraph H without eigenvalue ξ extends to a star
  complement for ξ. Active: any forced local configuration gives the seed.

## Implication for (99,14,1,2)

The 99-graph, if it existed, would have the **same windmill/7K₂ closed
neighbourhood and k=14**, so the star-complement attack opens the same way. Its
spectrum 3⁵⁴,−4⁴⁴ has eigenvalue −4 with m=44 → star complement order
99−44 = 55 (or ξ=3, m=54 → complement 45). A (57,14,1,4)-style attack would:
fix the windmill + one exterior vertex as the seed, enumerate candidate star
complements of order 55 (or 45), and check whether any clique of the required
size reconstructs a 99-graph. The 3720/38 numbers for the (57,14,1,4) case show
the scale that succeeded at k=14, μ=4; whether it transfers to μ=2 is open but
the local seed is literally identical.

## Status / caution
- Peer-reviewed (Filomat 2008); the enumeration is **computer-assisted**
  (Cliquer, not reproduced here). The windmill claim follows directly from
  λ=1 (N(u) induced is a perfect matching), holding identically for 99.
- Does not itself decide 99; it is a method template + the same-local-structure
  observation.

```claim
id: milosevic-starcomplement-5714-template
statement: srg(57,14,1,4) does not exist; the proof uses star complements for
  eigenvalue 2 (multiplicity 38): a 16-vertex seed N[u]∪{v} (closed
  neighbourhood a windmill W14) is extended to 3720 non-isomorphic 19-vertex
  star complements, none of whose compatibility graphs has a 38-clique. The
  closed neighbourhood being a windmill = neighbourhood a perfect matching
  7K2 is forced by lambda=1 and is identical for srg(99,14,1,2).
hypotheses: srg(57,14,1,4); star-complement reconstruction machinery (Cvetkovic-
  Rowlinson-Simic); lambda=1 forcing N(u)=7K2.
holds-here: yes for the local-structure part (identical to 99's windmill/7K2
  and k=14); the full nonexistence is for mu=4, which 99 does not have, so it
  is a template, not a transfer.
status: asserted-by-source (peer-reviewed; computer-assisted enumeration,
  not reproduced here; the 7K2/windmill fact is elementary from lambda=1).
bearing: a closer k=14, lambda=1 analogue than srg(85,14,3,2); supplies the
  star-complement reconstruction machinery and the same local seed (windmill)
  for a possible 99 attack, at star-complement order 55 (or 45).
anchor: research/sources/milosevic-star-complement-57141.full.md
contradicts: none; complements the library's existing (85,14,3,2) template claim
```

[[milosevic-star-complement-57141.full]]
