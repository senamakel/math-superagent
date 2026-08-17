# Librarian pass — closed the Bouchard-named-but-absent gap (2026)

## Gap found

The run's durable memory (CONTEXT.md / Cognee) asserted facts about two 2025
Bouchard papers as if established, but neither was on disk — only
`2503.00277` (lattice formulation) was. Named-in-memory-but-absent is exactly
the failure this role exists to prevent.

- **Bouchard, "An averaging result for union-closed families of sets",
  arXiv:2509.12537** (2025-09-16) — *was absent*.
- **Bouchard, "An upper bound for union-closed family size",
  arXiv:2511.10608** (2025-11-13) — *was absent*.

Both confirmed to exist by live `exa_search` (arXiv listings + arXiv.gg author
page) before download. Neither re-fetches anything on disk.

## Now on disk

- `research/sources/bouchard-averaging-result-upto-n2-2509.full.md` (73 KB
  markdown body, source URL `https://arxiv.org/html/2509.12537` in first
  lines).
- `research/sources/bouchard-upper-bound-family-size-2511.full.md` (30 KB
  markdown body, source URL `https://arxiv.org/html/2511.10608`).

## What each establishes (digests replaced with summaries)

1. **Averaging result (2509.12537)** — new provable class + limits of averaging:
   - Thm 1.4: separating UC family with height h ≤ 3 has Avg ≥ n/2, so UC.
   - Thm 2.1/Cor 2.2: separating UC family with h = 4 ≤ n and |B| ≤ 2 (B a
     smallest irredundant subfamily of A_<n/2) has Avg ≥ n/2, so UC.
   - Thm 3.2: h = 4 is the **largest** averaging-reachable height — explicit
     separating UC families with h ≥ 5, |B| = 1, Avg < n/2.
   - Sharpens the library's `cms-averaged-frankl-wrong` limits-of-averaging
     thread with an explicit modern witness.
2. **Upper bound on family size (2511.10608)** — refines Reimer/Erdős line:
   - Thm 1: |A| ≤ Σ_{i=0}^ℓ C(n,i), equality iff all subsets of size ≥ n−ℓ.
   - Cor 2.1: some element in ≤ Σ_{i=0}^ℓ C(n-1,i) member sets (the "at most"
     dual frequency bound).
   - Thm 2: analytic binomial-sum bound with optimal p̂.

## Filed

- Full texts in `research/sources/`.
- Digests replaced by proper summaries in `research/summaries/` (both carry
  the source URL and falsifier).
- Verified findings in Cognee (`remember_memory`, source = the arXiv URL).

No new request opened; both papers are partial results, not record constants.
The record stays Yu 0.38234 published / Liu 0.38271 conditional preprint.
