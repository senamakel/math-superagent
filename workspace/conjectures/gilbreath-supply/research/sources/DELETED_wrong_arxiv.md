# Overwrite note — arXiv ID collisions corrected

Two downloads initially resolved to the *wrong* papers because guessed arXiv IDs
pointed at unrelated preprints:

- `maynard_dense_clusters_primes_subsets.*` first fetched the astronomy paper
  "A ~12 kpc H i extension ... in CIG 340" (arXiv:**1405.2594**). Maynard's
  "Dense clusters of primes in subsets" is arXiv:**1405.2593**.
- `banks_freiberg_turnagebutterbaugh_consecutive_primes_tuples.*` first fetched
  the LHC paper "Contact Interactions Probe Effective Dark Matter Models at the
  LHC" (arXiv:**1303.3348**). BFTB's "Consecutive primes in tuples" is
  arXiv:**1311.7003**.

Both files were **overwritten in place** with the correct full texts (verified:
DENSE CLUSTERS OF PRIMES IN SUBSETS / CONSECUTIVE PRIMES IN TUPLES headers now
match, no astronomy or LHC content remains), and their digests replaced. The
wrong content never entered the claim ledger.

Lesson for later runs: an arXiv ID is a distinct identifier, not a guess; the
four leading digits changed here (2594 vs 2593, 3348 vs 7003). Verify the
fetched title against the intended paper before trusting a digest, and use
`exa_search` or a citation graph to confirm arXiv IDs rather than inferring them.
