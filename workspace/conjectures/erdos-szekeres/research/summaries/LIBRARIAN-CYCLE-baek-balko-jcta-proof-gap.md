# Librarian cycle — the one genuine open gap: the JCTA proof of Baek–Balko Theorem 8

## What this cycle verified (not a no-op pass)

The library was checked against the run's one stated missing-proof gap and found
complete **except** for the actual proof of the decomposable-sets theorem, which
no open-access copy carries.

## The gap, precisely

**Claim `baek-balko-decomposable` (load-bearing in the extreme-structure thread)
is stated on disk but its proof is not.** The held SoCG 2025 PDF
(`research/sources/baek-balko-ES-conjecture-revisited-SoCG2025.pdf.full.md`)
states Theorem 8 verbatim (lines 343–352):

> Let a, u, k be positive integers satisfying a, u ≤ k. Then, every decomposable
> set of more than Σ_{i=k-a+2}^{u} (k−2 choose i−2) points contains an a-cap, a
> u-cup, or k points in convex position.

…and then says, verbatim: **"The proof of Theorem 8 is omitted."** The split
lower-bound lemmas (Lemma 9, Lemma 12) are likewise "proof omitted" in the SoCG
version.

**The definition is on disk** (lines 439–443) — "A set P is decomposable if
either |P|=1 or if |P| ≥ 2 and P can be partitioned into two decomposable sets A
and B such that A is deep below B" — so the run CAN test decomposability of its
own es_construct sets with the exact orientation oracle even without the proof.

## What was searched and could not be obtained

- **JCTA 2026 journal version** (Baek & Balko, *The Erdős–Szekeres Conjecture
  Revisited*, J. Combin. Theory Ser. A, DOI 10.1016/j.jcta.2026.106195):
  paywalled; `read_sources` on the DOI returned only highlights/references, no
  full text or proof.
- **arXiv preprint**: no arXiv version of the joint Baek–Balko paper exists
  (searches constrained to arxiv.org return only the unrelated Baek 2022 ETV
  preprint). The SoCG LIPIcs version is the only open full text.
- **Author copy**: no open copy on Balko's or Baek's homepage surfaced in
  search.
- **Citation graph** of DOI 10.4230/LIPIcs.SoCG.2025.13: 0 connected works —
  OpenAlex record too new to carry connectivity; no new leads.
- **`find_similar_sources`** on the DROPS PDF returned only the SoCG entry and
  metadata/about pages (Ben-Gurion portal, Starfos, TA CR), none carrying the
  proof.

## Bottom line for the run

The decomposable theorem must be treated as **asserted-by-source (author-claimed,
proof not on disk)** until the JCTA 2026 full text is fetched. It must not be
used as a *proved* basis for a structural step. The run can, however:
- test whether its own es_construct extremal sets are decomposable (definition
  is on disk) — a genuinely useful computation;
- verify the theorem's instances computationally (S(a,u,k) bound for specific
  a,u,k) where feasible by brute force over small decomposable sets.

This gap was already recorded in Cognee durable memory; this note is the on-disk
anchor. It is the single genuinely-missing item on an otherwise complete library.

## Decision

The library is otherwise complete against the current state of the art. No other
angle is thin. Further librarian cycles should re-check for an open JCTA 2026
proof or author copy; absent that, NOTHING FURTHER to acquire.
