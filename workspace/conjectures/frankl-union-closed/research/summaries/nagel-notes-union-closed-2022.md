# Nagel — Notes on the Union Closed Sets Conjecture

Source: https://arxiv.org/abs/2208.03803 (Nicolas Nagel, 2022; arXiv:2208.03803).

Full text: `research/sources/nagel-notes-union-closed-2022.full.md`

## What this establishes

The primary source of two structural directions the run cites elsewhere and previously held only by reference:

**1. The k-th most frequent element question (Section 2, Frequencies).** Does every union-closed family have a *second* (then k-th) most frequent element present in at least a half — or minimally some fixed fraction — of the sets? Nagel poses the question (Question 2.1 ff.) that generalises the Union Closed Sets Conjecture from "the most frequent element is in ≥ half" to a statement about all the ranking elements. This is precisely the question **Das–Wu (arXiv:2412.03862)** resolved: the k-th most frequent element is in at least `|F| / (2^k − 1 + 1)` sets (proportional to `(3−√5)/2` asymptotically), with equality exactly the near-k-cubes.

**2. Weakenings via interior operators / congruence relations (Section 3.1, Equivalent Structures).** Investigates structures equivalent to union-closed families — interior operators, congruence relations, up-sets, intersecting families — and obtains **weakenings** of the conjecture: `𝒯(F₁) ≤ #𝒯(F₂) ≤ … ≤ #𝒯(F_m)…` (a monotone sequence of transferred/derived family sizes). States theorems on these equivalent structures (Thm 3.1, 3.2, Cor 3.3, Lemma 3.5, Cor 3.6, Thm 3.7, 3.10, 3.11, 3.13, 3.14, 3.17) giving conditions under which families built from these equivalent structures satisfy the conjecture's conclusion.

## Why it matters to this run

- **Fixes the provenance of the "k-th most frequent element" thread**: the library's `daswu-*` claims and the `abundance-profile` thread rest on Nagel's Question as their base, and now the primary source for that question is on disk.
- The equivalence/weakening section is adjacent to the run's `bouchard-ucx-ladder` and `bouchard-ucn-minus1-to-ucn` claims (generalised complementary formulations). It offers possible structural reformulations in the interior-operator language that the approach ledgers have not yet mapped.

## Evidence class

- Statements: asserted-by-source (the paper is a 2022 preprint; by the library's own record its Question 2.1 is now *resolved* by Das–Wu 2412.03862).
- Theorems in Section 3.1 are stated with proofs in the source; not independently re-verified here.

## Falsifier / note

The k-th-frequency generalization (Question 2.1) is exactly what Das–Wu settle; if a source disputes the equality characterisation or the `(3−√5)/2` asymptotic, that would refine this note. The Section 3 equivalence claims are asserted-by-source unless a later note re-derives one.

```claim
id: nagel-kth-frequency-question
statement: (Nagel, Question 2.1) Does every union-closed family have a
  k-th most frequent element (k ≥ 2) in at least a fixed fraction of its sets —
  in particular is the second-most-frequent (then k-th) element in ≥ half?
  This generalises the Union Closed Sets Conjecture from "the most frequent
  element is abundant" to all ranks. Now RESOLVED by Das–Wu (arXiv:2412.03862):
  the k-th most frequent element is in ≥ |F|/(2^{k-1}+1) sets, equality exactly
  on near-k-cubes, asymptotic constant (3−√5)/2.
hypotheses: F union-closed, |∪F| ≥ k ≥ 2.
holds-here: yes — the question is the base of the run's daswu-nagel and
  abundance-profile claims; it is resolved, not open.
status: asserted-by-source (the question is Nagel's; its resolution is Das–Wu,
  separately filed).
bearing: fixes the provenance of the "k-th most frequent element" thread; the
  near-k-cube extremal equality ties the abundance-profile thread to the
  entropy constant (3−√5)/2.
anchor: research/sources/nagel-notes-union-closed-2022.full.md §2
```

```claim
id: nagel-interior-operator-equivalences
statement: Union-closed families admit equivalent descriptions via interior
  operators, congruence relations, up-sets and intersecting families; Nagel
  states structural theorems (Thm 3.1, 3.2, Cor 3.3, Lemma 3.5, Cor 3.6, Thm
  3.7, 3.10, 3.11, 3.13, 3.14, 3.17) giving conditions under which families in
  these equivalent languages satisfy the conjecture's conclusion, plus a
  monotone-transfer sequence 𝒯(F₁) ≤ #𝒯(F₂) ≤ … of derived family sizes.
hypotheses: the equivalent-structure definitions as in the paper §3.1;
  statements carry proofs in the source.
holds-here: yes — a reformulation. Adjacent to the run's bouchard-ucx-ladder
  and bouchard-ucn-minus1-to-ucn claims; not a bound, class or proof of UC.
status: asserted-by-source (proved in the paper, not re-derived here).
bearing: offers reformulations in interior-operator language the approach
  ledgers have not yet mapped; low-priority but available if a structural
  recasting is wanted.
anchor: research/sources/nagel-notes-union-closed-2022.full.md §3.1
```

Wikilink the full text: [[nagel-notes-union-closed-2022.full]]
