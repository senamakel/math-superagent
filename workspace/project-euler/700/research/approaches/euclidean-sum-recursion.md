# Approach: Direct Euclidean recursion for the total sum S(M,A), no coin enumeration

```approach
idea: Treat the sum of all Eulercoins as a function S(M,A) of the pair
       (M,A) alone, and derive a single Euclidean ("division-transform")
       recursion S(M,A) = (closed-form contribution of the first run) +
       S(reduced pair), so the answer falls out of an O(log M) exact-integer
       recursion that never materialises the 102 coins.
mechanism: The record-low *values* obey c_{k+2} = ceil(c_k/c_{k+1})·c_{k+1}
       − c_k = c_{k+1} − (c_k mod c_{k+1}) (a centred / least-absolute-
       remainder Euclidean descent). When the quotient is 2 — i.e.
       c_{k+1} ≥ c_k/2 — the recurrence is c_{k+2} = 2c_{k+1} − c_k, so a run
       of quotient-2 steps is exactly an arithmetic progression with constant
       difference, and a quotient ≥ 3 is exactly the jump that starts the next
       run (this is the source of the observed 17 maximal arithmetic runs).
       Hence the total sum telescopes run-by-run: each run contributes a closed
       arithmetic-series term, and the transition to the next run is a single
       Euclidean step on the pair (c_k, c_{k+1}). Writing everything in terms
       of the original pair (M, A) gives a self-similar recursion for S itself
       — the same shape as the floor_sum Euclidean recursion, but for the sum
       of record lows directly, which is a different representation from both
       the index recurrence (which enumerates coins) and the floor_sum
       window-sum route (which still needs the coin indices up front).
status: grounded (as a tractable stated-recursion reformulation), with an
       important qualification about independence — see killed-by in Notes.
precedent: The mechanism is realised on two named, standard objects already in
       this run's library:
       (a) floor_sum — the Euclidean recursion f(n,m,a,b)=f(y,a,m,z),
       y=floor((an+b)/m), validated at full size and claimed
       eu700-floor-sum-tool (research/summaries/floor-sum-editorial.md, AtCoder
       Library editorial). This is exactly the "division-transform"
       self-similarity the candidate describes.
       (b) the centred/least-absolute-remainder Euclidean descent with run
       telescoping — this is precisely the record-low recurrence
       eu700-record-low-recurrence in value form c_{k+2}=c_{k+1}-(c_k mod
       c_{k+1}), and the AP-run decomposition is the *checked* result of
       research/approaches/pe700-ap-runs.md (17 runs; V recomputed from the
       decomposition). So the run-by-run collapse is known-good.
       (c) The Dedekind-sawtooth circle of ideas is real: Dedekind sums
       s(a,b) have Euclidean-algorithm/continued-fraction closed forms and
       reciprocity (Hall–Huxley, Acta Arith 63 (1993), doi 10.4064/aa-63-1-79-90;
       Girstmair, Int. J. Number Th. 13 (2017), doi 10.1142/s1793042117500889;
       Minelli–Sourmelidis–Technau, arXiv 2301.00441). But the candidate's sum
       (of record lows) is NOT a Dedekind sum — it is the much sparser
       record-low subsequence, so this circle supplies vocabulary, not the
       recursion.
first-step: From c_{k+2} = c_{k+1} − (c_k mod c_{k+1}) and the run
       decomposition (quotient-2 ⟺ arithmetic run), write down S(m,a) and its
       base case explicitly, then check S against the brute oracle on the
       small pairs (7,17), (3,23), (5,13) and against the real pair's first
       coins.
```

## Notes

- GROUNDED as a reformulation, with an independence qualification (killed-by on
  novelty, not on correctness): the "division-transform" self-similarity is a
  real, named, O(log m) mechanism — it is exactly floor_sum (AtCoder Library),
  claimed eu700-floor-sum-tool and already validated at full size by this run.
  And the run-by-run telescoping over quotient-2 steps is the *checked* AP-run
  decomposition of pe700-ap-runs.md (17 runs, recomputes V). So the recursion
  S(m,a) = first-run-term + S(reduced pair) is a legitimate, O(log M) route to
  the exact sum without materialising all 102 coins, and the mechanism is
  nothing invented.
- Independence caveat (why it is not a *second independent derivation*): any
  values-only S recursion is the value-form expression of the same Euclidean
  quotient descent that the record-low index recurrence (eu700-record-low-
  recurrence) performs, just as the run's "Route A" value-descent re-derived V
  without index bookkeeping yet shares the descent structure (see
  eu700-floor-sum-tool caveat). So it is a distinct code path but not a
  mathematically distinct derivation. A genuinely independent route remains
  the brute forward prefix-min scan (reachable only to n=7e6) plus full
  small-modulus scans.
- The Dedekind-sum circle is vocabulary only: the sum of *record lows* is not a
  Dedekind/floor-power sum (those sum over the whole residue orbit, not the
  sparse record-low subsequence), so no off-the-shelf Dedekind-closed-form
  applies. Keep it as conceptual context, not as the recursion.
