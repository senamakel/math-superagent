# On 2-power unicyclic cubic graphs — full text summary

**Source:** S. Pirzada, M. A. Shah, E. T. Baskoro, *Electron. J. Graph Theory Appl.* 10(1) (2022) 337–344, doi:10.5614/ejgta.2022.10.1.24.
**Full text:** `research/sources/pirzada-2power-unicyclic-proof.full.md`
**URL:** https://ejgta.org/index.php/ejgta/article/download/1312/pdf_224

## What the paper genuinely establishes (construction)

The paper constructs an infinite family of **2-power unicyclic cubic graphs**: cubic graphs containing **exactly one** cycle whose length is a power of two, and no other.

- Definition: a *2-power unicyclic* graph contains a unique 2-power cycle (length 2^k).
- Theorem 2.1: for each i ≥ 1, there is a cubic graph **G_i** of order
  |G_i| = |G_{i-1}| + 2^{i+4}, |G_1| = 94, containing a cycle of length 2^{i+4} and
  **no** cycle of length 2^t for any t ≠ i+4 (i.e. all smaller powers 4,8,16,…,2^{i+3}
  are avoided).
- Concretely: G1 (n=94) has only C32 as a 2-power cycle; G2 (n=222) only C64;
  G3 (n=478) only C128, etc. The construction glues two copies of a gadget X_i via a
  bridge edge z1z1', so every 2-power cycle must lie within one half and its length
  is bounded by the half-order; a lower bound on the shortest cycle excludes all
  smaller powers, forcing exactly the single 2-power length. (The abstract omits
  the word "unique" but that is what is proved.)

These are genuine **near-counterexamples**: arbitrarily large cubic graphs whose
2-power cycle is a single prescribed length 2^k for arbitrarily large k, sitting
alongside Bensmail's construction (all 2-power cycles of length 4 only or 8 only).
They do **not** disprove the conjecture — every G_i still contains a 2-power cycle.

## The claim that is NOT established (flawed conclusion)

The final "Conclusion" asserts that no counterexample to the Erdős–Gyárfás
conjecture can exist, via a closing step that reads: "let us assume a cubic graph G
contains a cycle of length 2^k only … d(u,v) = 2^{k-1} − 1 … which negates the
above observation that each cubic graph … has one cycle of length 2^k. Accordingly,
there is no cubic graph in which we can develop a counter case."

This is **circular / a non-sequitur**. The "observation that each cubic graph has
a 2-power cycle" is exactly the conjecture being argued for; the step
d(u,v) < n/2 vs. Frank's 3-diameter bound does not, on its own, rule out a
cubic counterexample (Bensmail's and the constructed G_i show single or few
2-power cycles are possible). The paper proves the construction but **does not
prove the conjecture**. The abstract's phrasing "no counterexample exists" must
be treated as an over-claim, not an established result.

## Relevance to this run

- Fixed (from primary text) that arbitrarily large cubic graphs can have a **unique**
  2-power cycle of a prescribed single length 2^k. Any structural argument must be
  consistent with — and sit alongside — both this and Bensmail's construction.
- Caveat noted in `notes/library-holdings.md` remains: do **not** cite this paper as
  settling the conjecture; cite it only for the 2-power unicyclic construction.

```claim
id: pirzada-2power-unicyclic
statement: There is an infinite family of 2-power unicyclic cubic graphs: cubic graphs G_i with |G_1|=94, |G_i|=|G_{i-1}|+2^{i+4}, each containing a cycle of length 2^{i+4} and no cycle of length 2^t for any t != i+4. In particular G1 has only a 32-cycle as a 2-power cycle, G2 only a 64-cycle, G3 only a 128-cycle.
hypotheses: G_i cubic, order n=2s with a bridge splitting into halves so every cycle lies in one half; shortest cycle exceeds 2^{i+2}, bounding the only 2-power length to 2^{i+4}.
holds-here: yes (near-counterexample landscape; the G_i are consistent with Bensmail and do not disprove the conjecture, which they each satisfy).
status: proved
bearing: The paper's own Conclusion over-claims to rule out all counterexamples, but that step is circular and NOT established; cite only the construction. These graphs show single-2-power-length cubic graphs exist at arbitrarily large order (n=94,222,478,...).
anchor: research/summaries/pirzada-2power-unicyclic-proof.md
```

