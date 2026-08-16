# Verification of the 2/3 degree-fraction claim (jul059)

Source being verified: erdosproblems.com #64 forum comment by jul059,
26 Jul 2026, "Found by ChatGPT 5.6 Sol High, not verified."
Full text: [[erdosproblems-64-discussion.full]]
Concerns claim: `ce-2-3-degree-fraction`.

## The claim

In a minimal counterexample G to the Erdős–Gyárfás conjecture, with
V₃ = {d=3} and V≥₄ = {d≥4}:

    |V₃| ≥ 2|V≥₄| + 1,  hence  |V₃| > (2/3)|V(G)|.

This improves Carr's 4/7 bound in Theorem 0.1.

## What I verified, step by step (against held Carr full text)

Every line uses only facts whose full proofs are now held in
`research/sources/carr-predominantly-cubic-fulltext.html.full.md`:

1. **V≥₄ is independent** (Carr Cor 0.1(2)). So every edge incident with V≥₄
   joins V≥₄ to V₃. Hence e(V≥₄,V₃) = Σ_{v∈V≥₄} d(v) ≥ 4|V≥₄|.
   ✓

2. **Every vertex is adjacent to a degree-3 vertex** (Carr Cor 0.1(1)). Applying
   this to a vertex of V₃: it has degree 3 and must be adjacent to some V₃
   vertex, so it has at most **2** neighbours in V≥₄ (not 3). Hence
   e(V≥₄,V₃) ≤ 2|V₃|.
   ✓ THIS is the improvement: Carr's 4/7 proof used the looser ≤ 3|V₃|.

   Putting 1 and 2 together: 4|V≥₄| ≤ 2|V₃|, i.e. |V₃| ≥ 2|V≥₄|. ✓

3. **Exclude equality |V₃| = 2|V≥₄|.** At equality every inequality holds with
   equality: every v∈V≥₄ has d(v)=4 (since 4|V≥₄| = Σd ≥ 4|V≥₄|), and every
   v∈V₃ has exactly 2 V≥₄ neighbours (so degree-3 total gives 1 V₃ neighbour).
   Build H on V≥₄: replace each x∈V₃, with its two V≥₄ neighbours u_x,v_x, by
   the edge u_x v_x.
   - H is simple: two distinct V₃ vertices sharing the same two V≥₄ neighbours
     u,v would give a 4-cycle u–x–v–y–u in G, i.e. a 2²-cycle, contradiction.
   - Every H-vertex has degree 4 (each V≥₄ vertex has exactly 4 V₃ neighbours,
     each contributing exactly one incident edge of H).
   - |V(H)| = |V≥₄| < |V(G)|, so by minimality H contains a 2^k-cycle (k≥2).
   - Replacing each H-edge u v by the 2-edge path u–x–v (x the corresponding
     V₃ vertex) gives a cycle in G of length 2·2^k = 2^{k+1}, contradiction.
   Hence equality is impossible, and |V₃| ≥ 2|V≥₄| + 1. ✓

4. **|V₃| > 2/3|V(G)|**: |V₃| ≥ 2|V≥₄|+1 ⟹ 3|V₃| ≥ 2|V₃|+2|V≥₄|+2 >
   2(|V₃|+|V≥₄|) = 2|V(G)|, so |V₃| > (2/3)|V(G)|. ✓

## Assessment

The argument is **sound as a deduction from Carr's lemmas**. Every step rests
on a lemma whose full proof is now held, and the only genuinely new—and
correct—step is replacing Carr's 3|V₃| bound with 2|V₃| using Cor 0.1(1)
applied to the V₃ vertices themselves.

**Caveat**: this is my own verification of a forum post's reasoning, not a
peer-reviewed result, and the source explicitly says it is not verified /
machine-found. It is *proved-from-held-lemmas* here, but it has not survived
the oracle's counterexample search (the equality case H is itself a graph to
hunt). I record it as `verified-numerically/derived`, not `proved` in the
formal sense, until the Lean formalisation or an independent check lands.

## What would falsify it

- A minimal counterexample in which a V₃ vertex has all three neighbours in
  V≥₄ — impossible because Cor 0.1(1) is now proved (every vertex has a V₃
  neighbour). No such vertex can exist.
- A bug in the H-construction (e.g. H not simple, H not 4-regular, or the
  cycle-length doubling failing). I checked each: H simple, 4-regular, and
  each H-edge ↔ one 2-edge V₃-path, so cycle lengths double exactly.
- A 4-cycle produced by two V₃ vertices sharing a pair of V≥₄ neighbours would
  only matter if G were assumed not to already contain a 2-power cycle — but
  4 IS a 2-power and G contains none, so it's excluded. ✓

```claim
id: ce-2-3-degree-fraction
statement: In a minimal counterexample |V3| ≥ 2|V≥4| + 1, hence strictly more than 2/3 of vertices have degree exactly 3 (improving Carr's 4/7).
hypotheses: G a vertex- then edge-minimal counterexample to Erdos-Gyarfas; V3 = deg-3 vertices, V≥4 = deg-≥4 vertices; relies on Carr Cor 0.1(1),(2)
holds-here: yes (improves the live near-cubic thread ce-principality-carr)
status: derived (verified this cycle against held Carr full proof; still not formally/independently checked, source is a forum post)
bearing: if confirmed, tightens the minimal-counterexample degree spine; the 2/3 improvement is the correct new step (Cor 0.1(1) applied to V3 vertices)
anchor: research/sources/carr-predominantly-cubic-fulltext.html.full.md, research/summaries/erdosproblems-64-discussion.md
```
