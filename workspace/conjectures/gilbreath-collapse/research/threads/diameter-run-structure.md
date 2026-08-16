# Thread — diameter and run structure, not cardinality

Steer-1 reorients the collapse question: the census shows size is the wrong
statistic. At n=20 the occurring sets have |A| = 6..12 but diameter 10..18, up
to 8 runs, run_lengths mostly all-1s — small sets spread across nearly the whole
index range. Eight isolated singletons spanning diameter 14 is small and
maximally NON-local; it couples positions at opposite ends of the string. The
O(n) distance enumerator (problem.md item 4) weights by |A| and controls neither
diameter nor run count, so it does not imply short-range structure. The question
turns on the joint distribution of (|A|, diam A, #runs A).

```thread
question: Does S² factor through the short-range pair correlations of h? Decided
      by the joint distribution of (|A|, diam A, #runs A) over the index
      multiset {M_d △ M_{d'}} — diameter and run structure, not cardinality.
status: live
rests-on: pf-s2multiset-rigid (every nonempty set multiplicity exactly 2, n≤256);
      census code/out/multiset_census_n128.txt (n≤128, two-route verified by
      code/out/verify_census_bitset.txt); imported items 3,5 (size and run
      structure of M_d).
blocked-by: (none — census already reaches n=128; missing are the joint
      (|A|,diam,#runs) tabulation and the max-runs/max-diam growth curves)
next: tool_builder: joint (|A|, diam, #runs) distribution at every n reachable;
      report max-runs(n) and max-diam(n); decide the uniform bound R.
      sat_solver: witness from an isolated-singleton A (task witness-hunt-singletons).
```

## Dead: the cardinality reading

The heuristic "small |A| ⇒ short-range structure" (problem.md item 4's
interpretive sentence) is refuted by the census and is closed. Do not read the
growing max-span (n−1 at weight n−2, n=3..128) as a collapse refutation either:
long-span support is consistent with factoring through correlations (S² is a
square, (Σ χ_{M_d})²; the decision is C_K-fiber constancy, not support). It
kills the framing, not the statement.
