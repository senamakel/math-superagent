Hand-verified facts for the candidate-precedent check. (No shell tool in this role;
each is exact arithmetic done by hand, recorded here so the run need not redo it.)

```claim
id: CAND2-RUN-VALUATION-VACUOUS
statement: For ANY integer m with ternary runs of 1s {(s_j,r_j)},
  m = sum_j 3^{s_j}(3^{r_j}-1)/2 hence 2m = sum_j (3^{s_j+r_j}-3^{s_j}); setting
  m=2^n makes v_2 of the RHS equal n+1 for every n, digit-free or not. The run/
  valuation identity is a tautology carrying no digit-{0,1} information.
hypotheses: none beyond the run-form identity (true for all integers).
holds-here: yes (the identity holds for all m; the absence of a digit hypothesis
  is exactly why it cannot be an invariant of the conjecture).
status: checked (exact hand arithmetic; see text).
bearing: kills candidate run-gap-signed-rep-zsigmondy by vacuity.
anchor: research/candidate-precedent-handcheck.md
```

```claim
id: CAND2-256-RUNS-MISCOMPUTED
statement: 2^8 = 256 = 100111_3 has runs {(0,3),(5,1)} (one run '111' at
  positions 0,1,2 and a single 1 at position 5), NOT {(0,2),(2,1),(5,1)}.
  The file's '8+18+486=512' chain splits a contiguous run and is miscomputed;
  the correct contribution is 3^0(3^3-1)/2 + 3^5(3^1-1)/2 = 256.
hypotheses: base-3 representation of 256.
holds-here: yes.
status: checked (exact hand arithmetic).
bearing: the motivating numerical example of the run-valued candidate is wrong;
  under the correct decomposition the valuation line collapses to the vacuous
  identity above.
anchor: research/candidate-precedent-handcheck.md
```

```claim
id: CAND3-CONVERGENT-DENOMINATOR-INSUFFICIENT
statement: Convergent denominators of log_3 2 include q=2 and q=8 (the two
  nontrivial witnesses) but also q=1,3,19,...; none of the non-{2,8} denominators
  is digit-2-free (2^1=2_3, 2^3=8=22_3, 2^19 has leading ternary digit 2).
  Hence 'n is a convergent denominator' is necessary for the witnesses but
  utterly insufficient -- infinitely many denominators fail.
hypotheses: alpha=log_3 2 ~ 0.63093, CF [0;1,1,1,2,2,...] (hand-computed partial
  quotients give denominators 1,1,2,3,8,19,...).
holds-here: yes.
status: checked (exact hand arithmetic on the first 6 convergents; the decision
  'n=2,8 must be special' would require excluding all other denominators, which
  this explicitly fails to do).
bearing: kills candidate beta-rotation-middle-digits-ostrowski -- the
  rotation/CF step only restates the problem and supplies no exclusion.
anchor: research/candidate-precedent-handcheck.md
```

```claim
id: CAND1-NONDEGENERATE-PROVED
statement: For every digit-2-free power 2^n = sum_{a in A}3^a, the S-unit
  equation 2^n - sum_{a in A}3^a = 0 (terms {2^n,-3^{a_1},...,-3^{a_k}} in the
  rank-2 group U_{2,3}) is non-degenerate: a vanishing proper sub-sum would
  force the complementary positive sum to vanish, impossible.
hypotheses: 2^n digit-2-free (all ternary digits in {0,1}); exponents a_j
  distinct nonnegative.
holds-here: yes, for all digit-free n including 0,2,8.
status: checked (exact hand argument, no computation needed).
bearing: the load-bearing structural fact on which the S-unit reformulation
  rests; correct.
anchor: research/candidate-precedent-handcheck.md
```

```claim
id: CAND1-UNIFORMITY-NO-PRECEDENT
statement: Evertse-Schlickewei-Schmidt (Ann. of Math 155, 2002) gives finiteness
  and a triply-exponential-in-k bound for the non-degenerate solutions of the
  level-k S-unit equation, but no uniformity in k; the uniformity statement is
  exactly the conjecture. The dual problem s_2(3^n) (sum of distinct powers of 2
  equal to a power of 3) was resolved unbounded by Baker-type linear-forms-in-log
  methods (Stewart 1980: > log n / log log n), not by a uniform S-unit / Subspace
  bound -- evidence that per-level S-unit finiteness does not transfer to
  uniformity in the support size.
hypotheses: ESS theorem hypotheses (fixed n = k+1 terms, rank-2 group, char 0
  field) hold at each fixed level; they are the level-finiteness step.
holds-here: the per-level theorem holds; the uniformity-in-k step does not follow
  and has no precedent found.
status: sourced (ESS bound) + the uniformity gap is the conjecture; dual history
  asserted-by-source (Stewart 1980).
bearing: S-unit reformulation is grounded as per-level; not grounded as a route
  to the full conjecture.
anchor: research/candidate-precedent-handcheck.md
```


--- Candidate 2: run decomposition of 256 ---
256 in base 3: 3^5=243, 3^4=81, 3^3=27, 3^2=9, 3^1=3, 3^0=1.
  256 - 243 = 13  -> place5=1
  13 < 81 (place4=0), 13 < 27 (place3=0)
  13 >= 9 (place2=1, rem 4), 4>=3 (place1=1, rem 1), 1 (place0=1)
  digits MSB->LSB: 1 0 0 1 1 1 = "100111".
  So positions 0,1,2 are ALL 1 -> ONE run of length 3 at s=0;
  position 5 is a length-1 run at s=5.  Runs = {(0,3),(5,1)}.

  The approach file's "runs {(0,2),(2,1),(5,1)}" is WRONG: it splits the
  contiguous block of three 1s at positions 0,1,2 into "11@0" and "1@2",
  which is not the base-3 digit string. Consequently its "8+18+486=512"
  chain is built on a miscomputed decomposition.

  Correct identity:
    3^0(3^3-1)/2 + 3^5(3^1-1)/2 = 13 + 243 = 256 = 2^8.
    2 * 256 = (3^3-3^0) + (3^6-3^5) = 26 + 486 = 512 = 2^9.  (v_2 = 9).

--- Candidate 2: the v_2 identity is vacuous ---
For ANY integer m with ternary runs of 1s {(s_j, r_j)}:
    m = sum_j 3^{s_j}(3^{r_j}-1)/2
  so 2m = sum_j (3^{s_j+r_j} - 3^{s_j}).
Set m = 2^n.  Then the RHS equals 2^{n+1} and v_2(RHS) = v_2(2^{n+1}) = n+1.
This holds IDENTICALLY for every n, digit-free or not: it is the definition of
2m in run form, not a constraint.  Therefore "v_2(LHS)=n+1 forces a 2-adic
cancellation tree" encodes nothing that distinguishes digit-{0,1} powers from
any other integer.  The only independence content would have to come from
Zsigmondy on run lengths r_j, which constrains lengths only and no digit
position, and is satisfied by infinitely many run multisets (e.g. any number
with a run of length 3 has the same, arbitrary, v_2 behaviour).  Refuted.

--- Candidate 3: convergent denominators of log_3 2 ---
alpha = log_3 2 = ln2/ln3 ~ 0.63092975357...
CF partial quotients (hand): floor(1/alpha)=1, then 1/0.6309...-1=0.5849...
  a = [0; 1,1,1,2,2,3,1,...]
  convergents (p/q):
    n=0: 0/1
    n=1: 1/1
    n=2: 1/2    (q=2)   <- n=2 IS a convergent denominator
    n=3: 2/3    (q=3)
    n=4: 5/8    (q=8)   <- n=8 IS a convergent denominator
    n=5: 12/19  (q=19)
  Denominators: 1,1,2,3,8,19,65,...   So BOTH nontrivial witnesses 2 and 8 are
  convergent denominators.  BUT the next denominators 1,3,19 are NOT digit-free
  (2^1=2_3 has a 2; 2^3=8=22_3; 2^19=524288 starts with ternary digit 2, since
    3^11=177147, 3^12=531441, and 524288/177147 = 2.96...).  So
  "n is a convergent denominator" is necessary-for-the-small-witnesses but
  utterly insufficient: infinitely many denominators fail.  The exclusion of
  all non-{2,8} denominators is the whole conjecture, and normality of log_3 2
  (which metric theory of rotations is about) is open and says nothing pointwise.

--- Candidate 1: non-degeneracy (re-verified) ---
Equation 2^n - sum_{a in A} 3^a = 0, terms {2^n, -3^{a_1},...,-3^{a_k}} in the
rank-2 group U_{2,3}={+/-2^u 3^v}.  A proper subsum vanishes iff:
  (i) a subcollection of the negative terms alone sums to 0: impossible (all
      -3^a are strictly negative), or
  (ii) 2^n - sum_{a in B} 3^a = 0 for a proper nonempty B subset A: then the
      complement sum sum_{a in A\B} 3^a = 0, impossible (all positive).
So the equation is NON-DEGENERATE for every digit-free power, incl. n=0,2,8.
Verified.  Evertse-Schlickewei-Schmidt (Ann. of Math 155, 2002) then gives
Finiteness of non-degenerate x=(2^n,-3^{a_j}) in U_{2,3}^(k+1) for each FIXED k,
with number of solutions <= exp((6(k+1))^{3(k+1)}(3)).  [schlickewei-1998-form]
But bound is triply-exponential in k and gives NO uniformity in k: it does NOT
bound n for large k, and whether finitely many n exist across ALL k is exactly
the conjecture.  The dual problem's resolution (s_2(3^n) unbounded; Stewart 1980,
log n / log log n lower bound) was obtained by Baker-type linear-forms-in-log
methods, NOT by a uniform S-unit/Subspace bound -- strong field evidence that
per-level S-unit finiteness does not yield the uniformity this conjecture needs.
