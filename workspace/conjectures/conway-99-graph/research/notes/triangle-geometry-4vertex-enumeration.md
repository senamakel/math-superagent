# The triangle-geometry angle: STS classification scale and the 4-vertex condition

Library note consolidating two gathered facts on the run's design-theoretic
attack surface. Neither is a new rule-out of 99; both bound *how* the
partial-Steiner-triple-system enumeration could ever be attempted.

## 1. STS block graphs meeting the 4-vertex condition → two SRG families

The triangle geometry of a putative srg(99,14,1,2) is a **partial Steiner
triple system** P on 99 points, 231 blocks (lines of size 3), 7 lines through
each point, whose block (collinearity) graph is G. The run's viable route is
structural: constrain P enough to classify or contradict, never enumerate.

Relevant primary fact. Behbahani–Lam–Östergård, "On triple systems and strongly
regular graphs" (J. Combin. Theory Ser. A 119 (2012) 1414–1426, DOI
10.1016/j.jcta.2012.03.013; also circulated as a Can. J. Math preprint) studies
which STS have block graphs satisfying the **4-vertex condition**. The abstract
states these fall into "two families of strongly regular graphs with the
4-vertex condition."

- Full text is paywalled (ScienceDirect/Springer). Obtained: abstract +
  surrounding citation context only. OpenAlex id W2919508139 (2012).
- EXACT classification now pinned by a source already in the library:
  Brouwer–Ihringer–Kantor, "Strongly regular graphs satisfying the 4-vertex
  condition" (arXiv 2107.00076, full text held), §3.4 "Block graphs of Steiner
  triple systems": Higman [14] found an STS(v) whose block graph satisfies the
  4-vertex condition is either a projective space PG(m,2) or has v ∈ {9,13,25};
  [25] rules out 13 and 25, leaving only the affine plane AG(2,3). All examples
  are rank 3. These are the block graphs G(B) (vertices = blocks of the STS),
  srg(v(v−1)/6, 3(v−3)/2, (v+3)/2, 9) — not the collinearity graphs. For PG(m,2)
  (v = 2^m−1) and AG(2,3) (v = 9), neither block-graph parameter set is the
  (99,14,1,2) spectrum, and no rank-3 graph can be srg(99,14,1,2) (which has
  |G| constrained tiny / would need Aut large enough for rank-3). This is
  exactly the content BLÖ's "two families" abstract gestures at; it concerns
  GENUINE STS block graphs.
- The run already holds the BvLS graph as the BvLS STS block graph at 243 and
  rook(3)=PG(2,3)"[partial] grid" at 9 — the two existing members of the family.

**Bearing on 99:** a partial STS whose block graph is srg(99,14,1,2) would, if
it were a *genuine* STS, be a candidate in Behbahani–Lam–Östergård's
classification — but the 99 triangle geometry is a *partial* STS (lines
through a point need not cover every pair), so the STS classification does not
directly decide it. It is a constraint to build on, and a reminder that a
Genuine-STS block graph over 99 would have to be one of the two classified
4-vertex families (neither of which has the (99,14,1,2) spectrum), whereas the
partial case escapes that classification.

## 2. The enumeration boundary for the triangle geometry is astronomically closed

Full Steiner triple system classification stops at order 19:
11,084,874,829 nonisomorphic STS(19) (Kaski–Östergård 2004). STS(21) is the
smallest open full-classification case; partial progress:
- STS(21) with sub-STS(7): 116,635,963,205,551 isomorphism classes
  (Heinlein–Östergård 2023, Glasnik Mat. 58(2), DOI 10.3336/gm.58.2.06).
- STS(21) with sub-STS(9): 12,661,527,336 (Kaski–Östergård–Popa classification).

A 99-point partial STS with 7 lines per point sits at a far smaller replication
but far larger structure count than any classification anyone has ever
completed. **Conclusion: the triangle-geometry route cannot be a blind
enumeration under any plausible symmetry reduction; it must be a structural
argument** (counting identity in induced C5/C6/K4−e; a forced/forbidden local
configuration; the n_3=0 pivot of Makhnev-1988/Reimbayev). This confirms the
"enumeration is the wrong method" caution from ROOT.md with a precise scale.

```claim
id: triangle-geometry-enumeration-closed
statement: The triangle geometry of a putative srg(99,14,1,2) is a partial
  Steiner triple system on 99 points, 231 blocks, replication 7. Any blind
  enumeration of such systems is astronomically beyond feasibility: even a
  full STS classification stops at order 19 (1.1e10 STS(19)) and STS(21) is
  the smallest open case (1.16e14 with sub-STS(7), Heinlein-Östergård 2023).
  So the design-theoretic route must be structural, not enumerative.
hypotheses: partial STS with the stated parameters is the triangle geometry.
holds-here: yes — bounds how the geometry can be attacked.
status: sourced (Kaski-Östergård 2004; Heinlein-Östergård 2023 summaries and
  primary abstract via read_sources). Not a rule-out of 99.
bearing: closes the "can the geometry be enumerated" sub-question with a
  concrete scale; directs phase-4 effort to structural counting identities.
anchor: research/summaries (Kaski-Östergård 2004; Heinlein-Östergård 2023),
  and this note.
```

```claim
id: sts-4vertex-two-families
statement: The Steiner triple systems whose block graphs satisfy the 4-vertex
  condition are exactly those from PG(m,2), the affine plane AG(2,3), and
  (ruled out) STS(13), STS(25) — i.e. Higman's classification with 13 and 25
  eliminated; all are rank-3 block graphs (Behbahani-Lam-Östergård 2012
  abstract "two families"; the precise list is Brouwer-Ihringer-Kantor §3.4).
  These are the *block* graphs (vertices = blocks of the STS, srg(v(v−1)/6,
  3(v−3)/2, (v+3)/2, 9)), NOT the collinearity graph. The 99 triangle geometry
  is a *partial* STS, so it escapes this STS classification; and no member of
  the classified STS block-graph list has the (99,14,1,2) collinearity
  spectrum. The partial case is not settled by this.
hypotheses: block graph is the collinearity graph of the (partial) STS.
holds-here: yes — a constraint on the geometry, not a rule-out.
status: sourced (BIK full text §3.4, held in library; BLÖ 2012 abstract).
bearing: the "two families" of BLÖ are now pinned exactly (PG(m,2) block
  graphs + AG(2,3)); the partial-STS 99 geometry escapes it, confirming the
  design-theoretic route must be partial-STS-specific, not genuine-STS.
anchor: research/sources/brouwer-ihringer-kantor-4vertex-condition.full.md
  §3.4 (lines 225-233); DOI 10.1016/j.jcta.2012.03.013 abstract.
```

## What would settle more
Full text of Behbahani–Lam–Östergård 2012 (paywalled): the exact two SRG
families and their spectra. If either family had spectrum 3^54,-4^44 this would
be a genuine-STS constraint near 99; the library does not yet know their
spectra, so it cannot claim a genuine-STS realization of 99 is or is not among
them. Recorded as a gap, not a result.
