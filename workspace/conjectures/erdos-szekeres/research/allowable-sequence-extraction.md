# Targeted extraction — allowable/circular sequences in the held library

Scope: what the held sources actually establish about Goodman–Pollack allowable (circular) sequences, k-sets in them, the "staircase of contiguous reversals" convexity characterization, and per-element depth statistics. This is the extraction behind the adopted approach `allowable-sequence-circular-representation`. Only allowable/circular-sequence content is recorded here.

## Summary of what is actually held

| Source | Held as | Circular-sequence content in the held text |
| --- | --- | --- |
| Goodman–Pollack 1980, "On the combinatorial classification of nondegenerate configurations in the plane" (JCTA 29:220–235, doi 10.1016/0097-3165(80)90011-4) | **NOT held** — only a bibliography entry in `goodman-pollack-sturmfels ... full.md` line 67 | — |
| Abello–Eğecioğlu–Kumar (DCG 14 (1995), doi 10.1007/bf02570710) | **NOT held** | — |
| Felsner–Weil 2001, "Sweeps, arrangements and signotopes" (DAM 109:257–284) | Full PDF (text-garbled single line) + summary | Sweeping Lemma, wiring diagrams, rank-3 signotopes ⟷ pseudoline arrangements; **no allowable-sequence definition, no k-sets, no convexity-in-circular-sequence statement, no reversal-depth** |
| Hoffmann–Merckx 2018 (arXiv:1801.05992) | arXiv abstract page only | Allowable-sequence realizability is ∃ℝ-complete (universality). No definitions, no convexity content |
| Dobbins–Holmsen–Hubard 2014 (arXiv:1305.2266, Mathematika 60:463–484) | arXiv abstract page only | Equivalence of convex-body and topological-affine-plane ES conjectures. **No allowable-sequence definition, no k-sets, no staircase characterization** |
| Morris–Soltan 2000 survey (BAMS 37:437–458) | Full text | **§5.5 Duality**: the *dual* ES problem (simple line arrangements + a point q, sub-arrangement whose q-cell is a convex n-gon); pseudoline version Nps(n); Goodman–Pollack conjecture Nps(n) ≤ 2^{n−2}+1. **No circular sequence of permutations, no k-sets, no reversal-depth** |
| Goaoc–Welzl 2020/2022 | Full text (ar5iv) | Uses "order type" (Goodman–Pollack terminology) only; **no k-sets, no allowable sequence** |

**The library holds no primary definition of the Goodman–Pollack allowable/circular sequence, no k-set characterization in it, and no staircase-of-reversals convexity statement.** The approach file's two load-bearing citations (GP80 for the representation and its convexity encoding; Abello–Eğecioğlu–Kumar for circular sequences as maximal chains in the weak Bruhat order with convexity via balanced tableaux) are both unheld. The staircase/convexity description appears in the approach file itself as its mechanism, attributed to that literature, but is **not sourced by anything on disk**.

## Question (2): the "staircase of contiguous reversals" claim — is it stated anywhere?

**No held source states it.** Exhaustive grep of `research/` and `code/` for `allowable`, `circular sequence`, `staircase`, `contiguous reversal`, `k-set` finds:
- The approach file `allowable-sequence-circular-representation.md` states it as its mechanism ("A subset in convex position has a well-known clean description here — its elements are swept by a rotating line as a contiguous staircase of reversals within one half-period"), attributing it to the GP80/Abello–Eğecioğlu–Kumar literature generally — none of which is held.
- `code/out/layer_profile_conjecture.md` and `code/out/staircase_probe.py` / `es61_staircase_probe.py` use the *word* staircase for the ES block arc placement, not for a circular-sequence characterization.
- Nothing else. So: **stated in the approach file as adopted mechanism; verified in no held source; the cited primary texts are not in the library.**

## Question (3): per-element depth/level statistic in the circular sequence of the ES construction

**No held source defines one.** No source defines any per-element "depth" or "level" in a circular sequence at all (the phrase appears only in the approach file's mechanism and in `code/out/layer_profile_conjecture.md`'s Conjecture A, both this run's own writing). The ES construction's block structure |T_i| = C(n−2,i) is sourced (Morris–Soltan Thm 2.6; ES 1961 held), and `es-construct-block-tightness` verifies each block's cup+cap = n, but the *reversal-depth* statistic is a proposal of this run, not a sourced quantity.

## Question (1): exact definition of the GP allowable/circular sequence and of k-sets in it

**The exact definitions cannot be quoted from the library** — the primary texts are not held. What can be said from held sources and from the approach file's citation of GP80:

- **From the approach file (this run's own record, unverified):** a 2-periodic sequence of permutations of the n points in which consecutive permutations differ by reversing a set of increasing blocks, and over one full period every unordered pair is reversed exactly once; convexity questions are encoded by it; GP80 classifies n = 3, 4, 5 into 1, 2, 19 classes and refutes Perrin's claim that every allowable sequence is realizable (counterexample at n = 5). **None of this is in any held source text**; it is the approach file's citation of GP80's abstract/known content.
- **From Morris–Soltan §5.5 (held, verbatim):** the *dual* ES problem in terms of simple arrangements of lines — "The dual problem is then to determine the smallest integer N(n) so that every simple arrangement of N(n) lines together with a point q not on any line contains a sub-arrangement of n lines for which the cell containing q is a convex n-gon"; "Goodman and Pollack [37] conjectured that the inequality N(n) ≤ 2^{n−2} + 1 holds even if 'lines' in the dual Erdős–Szekeres problem are replaced by 'pseudolines'." This is the point-line duality ES problem (GP82 "A theorem of ordered duality"), distinct from the circular-sequence-of-permutations representation, and is the only *held* GP-adjacent material.
- **k-sets:** the library's only k-set content is `gsplit-enum-completeness-and-n7-zero` (this run's own checked claim: the rotating directed-line construction enumerates all N(N−1) distinct open half-plane sides / k-set sides) and a passing reference in Aichholzer et al. to Dey's planar k-set bounds. **No source defines k-sets inside the circular sequence** (i.e. as the elements appearing in a contiguous window of the sequence between two crossings).

## Claims written for the ledger

```claim
id: gp80-not-held-circular-sequence-unsourced
statement: The Goodman–Pollack 1980 paper (JCTA 29:220–235) that introduces the circular (allowable) sequence of permutations of a planar configuration, and the Abello–Eğecioğlu–Kumar 1995 paper (DCG 14) identifying circular sequences with maximal chains in the weak Bruhat order with convexity via balanced tableaux, are NOT in this library. The only held GP80 content is a bibliography entry in the Goodman–Pollack–Sturmfels full text. Consequently the exact definition of the GP allowable/circular sequence, of k-sets in it, and the convexity encoding attributed to GP80 in the approach file have no primary anchor on disk.
hypotheses: library contents as of this extraction (grep over research/ and code/).
holds-here: true — this is precisely the setting of the adopted approach's first step (write an allowable-sequence encoder from a point set), which needs the definition the library lacks.
status: catalogued (a term/file inventory, not a theorem).
bearing: the adopted approach's definition of the circular sequence must be reconstructed from a fetched primary source or from a standard secondary exposition before the encoder is written; the approach file's 'precedent' block overstates what the library sources.
anchor: research/sources/goodman-pollack-sturmfels - Upper bounds for configurations and polytopes in Rd.full.md (line 67); research/approaches/allowable-sequence-circular-representation.md
answers: gp80-primary-needed
```

```claim
id: hm-allowable-realizability-etr-complete
statement: Deciding whether a given allowable (circular) sequence is realizable by a planar point set is ∃ℝ-complete, even when the order type induced by the allowable sequence is realizable. Realization spaces of allowable sequences are universal (stably equivalent to arbitrary semi-algebraic sets).
hypotheses: allowable sequences in the Goodman–Pollack sense (the abstract relies on that standard notion without restating it); realizability by point sets in the plane.
holds-here: unchecked — the held file is only the arXiv abstract page; the term 'allowable sequence' is used without definition in the abstract, so the exact class of objects the theorem quantifies over is asserted rather than verified against GP80's definition.
status: asserted (source's own abstract; the ∃ℝ-completeness statement is the paper's main theorem, but this run holds no proof text and no definition section).
bearing: binds the allowable-sequence approach exactly as the order-type/chirotope trap binds the SAT arm: an upper bound proved over all abstract allowable sequences would be stronger than the ES conjecture and may be false; every candidate must be realized explicitly in exact coordinates before it counts.
anchor: research/sources/hoffmann-merckx-allowable-universality.full.md
contradicts: nothing held — corroborates the existing order-type realizability trap (realizability-etr-complete) by extending it to the finer allowable-sequence object.
```

```claim
id: dh-allowable-abstract-only
statement: The Dobbins–Holmsen–Hubard paper (arXiv:1305.2266; Mathematika 60 (2014) 463–484) is held only as its arXiv abstract page. The abstract establishes an equivalence between the Bisztriczky–Fejes Tóth conjecture on arrangements of planar convex bodies and a Goodman–Pollack conjecture on point sets in topological affine planes, with corollary upper bounds for convex-body ES problems; it contains no definition of the allowable sequence, no k-set characterization, and no convexity-in-circular-sequence statement.
hypotheses: none beyond the held abstract text.
holds-here: true — the approach file cites this paper for allowable-sequence convexity-type machinery, which the held text does not contain.
status: asserted (abstract-level claim; body not held).
bearing: removes this source as an anchor for any circular-sequence definition or convexity characterization; it remains an anchor only for the convex-body/topological-affine-plane equivalence.
anchor: research/sources/dobbins-holmsen-hubard-ES-noncrossing-1305.2266.full.md
```

```claim
id: staircase-convexity-unsourced
statement: No source held in this library states the characterization 'a subset of a point set is in convex position iff its elements appear in the allowable sequence as a contiguous staircase of reversals within one half-period'. The claim appears only in the adopted approach file as its mechanism, attributed to the unheld Goodman–Pollack 1980 / Abello–Eğecioğlu–Kumar 1995 literature. Its truth for realizable point sets is therefore unverified in this run, and it must be (a) sourced from the primary texts or a standard exposition, and (b) machine-checked against the exact convexity oracle (largest-convex-subset / cup-cap spectrum) before it is load-bearing.
hypotheses: allowable sequences over realizable planar point sets; the ES construction at n = 5,6,7 as the test bed.
holds-here: unchecked — no held source states it; the verification step is precisely the approach's first-step (allowable_encoder + oracle check).
status: asserted (this run's own proposal, unverified; not a sourced theorem).
bearing: this is the load-bearing structural fact of the adopted approach — without it the 'conjecture becomes a purely sequential statement' reformulation has no justification; until it is checked it must not be used to derive anything.
anchor: research/approaches/allowable-sequence-circular-representation.md
```

```claim
id: reversal-depth-unsourced
statement: No source held in this library defines a per-element depth/level/reversal statistic in the circular sequence of the ES construction, nor any depth profile whose level sizes are the binomial coefficients C(n−2,i). The identification 'block index T_i = reversal-depth i' is this run's own conjecture (stated in the approach file and in code/out/layer_profile_conjecture.md Conjecture A), motivated by the sourced facts that the ES blocks have sizes C(n−2,i) (Morris–Soltan Thm 2.6) and satisfy cup+cap = n per block (es-construct-block-tightness, checked). The depth statistic must be defined and machine-checked for realization-invariance (same order type, different coordinates → same depth) before it carries order-type structure.
hypotheses: the verified es_construct realization of the ES construction at n = 5,6,7; any definition of reversal depth must be checked across realizations of the same order type.
holds-here: true — this is the exact proposal the approach makes.
status: asserted (proposal; no source states it; not yet computed).
bearing: if depth = block index fails to be realization-invariant, the depth statistic is a placement artifact (like the onion layer profile the run already refuted) and the approach is refuted on arrival — the approach file's own critical falsifiability condition.
anchor: research/approaches/allowable-sequence-circular-representation.md; code/out/layer_profile_conjecture.md
```

```claim
id: ms-dual-esz-pseudoline-bound
statement: The Erdős–Szekeres problem has a point–line dual: N(n) is the least integer such that every simple arrangement of N(n) lines together with a point q not on any line contains a sub-arrangement of n lines for which the cell containing q is a convex n-gon; Goodman and Pollack conjectured N(n) ≤ 2^{n−2}+1 holds even when 'lines' are replaced by 'pseudolines' (Nps(n)), and the cups-caps arguments give Nps(n) ≤ C(2n−5, n−2)+2.
hypotheses: simple line/pseudoline arrangements; point q off all lines; general position.
holds-here: true — this is the dual formulation of the ES conjecture, quoted verbatim from the Morris–Soltan survey §5.5 (the survey is the run's held source; the primary citation is GP82 'A theorem of ordered duality').
status: asserted (survey statement; the Nps(n) ≤ C(2n−5,n−2)+2 bound is attributed by the survey to the cups-caps arguments of [32] and [80]).
bearing: the only GP-adjacent material actually held; provides the duality vocabulary but does not give a circular-sequence-of-permutations representation, and does not improve the exact point-set bound.
anchor: research/sources/morris-soltan - The Erdos-Szekeres problem on points in convex position - survey BAMS 2000.full.md (§5.5, lines 981–1006)
```

```claim
id: gsplit-k-set-sides-checked
statement: The count of distinct nonempty-proper open half-plane sides (k-set sides) of an N-point planar set in general position is exactly N(N−1), realized completely and with no spurious side by the rotating directed-line construction (ordered pairs (a,b) with the 4 inclusions of the two boundary points), validated exactly against a 2^N convex-hull-separation oracle at N = 8..16.
hypotheses: general position; the rotating-line (k-set) construction; exact integer determinants.
holds-here: yes — this is the k-set side of the circular sequence, the only k-set statement this run has verified.
status: checked (this run's computation, code/out/gsplit_enum_definitive.py; see also gsplit-enum-completeness-and-n7-zero).
bearing: the rotating directed line IS the sweep that generates the circular sequence of permutations; the N(N−1) sides are the half-period's reversals, so this checked claim is the computational backbone any allowable-sequence encoder will be validated against.
anchor: code/out/gsplit_enum_definitive_claim.md
```

## Bottom line for the approach

1. The representation's **definition** and the **staircase-convexity characterization** are unsourced on disk; both must be fetched (GP80; Abello–Eğecioğlu–Kumar; or a standard exposition such as the GP93 survey "Allowable sequences and order types in discrete and computational geometry") and/or machine-verified against the exact oracle before the approach's first step is trustworthy.
2. The **∃ℝ-completeness bind** is now sourced (Hoffmann–Merckx abstract): any abstract-allowable-sequence upper bound must be realized explicitly.
3. The **k-set side enumeration** (N(N−1) sides via the rotating directed line) is checked and provides the computational foundation.
4. **No depth/level statistic exists in the literature held**; the reversal-depth conjecture is the run's own, and its realization-invariance check is the approach's critical falsifier.

## Gap registered

The gap `gp80-primary-needed` — the primary GP80 definition and convexity characterization — could not be queued via `request_research` (the auto-filter repeatedly returned the same 8 unrelated claims and refused to queue). It is recorded here instead; the next fetch should target https://doi.org/10.1016/0097-3165(80)90011-4 or the GP93 survey (doi 10.1007/978-3-642-58043-7_6).
