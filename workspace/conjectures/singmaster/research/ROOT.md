# ROOT — phase-1 library completion summary

What must be established before this phase ends, per the phase plan; each item is
answered and the library in `research/` now carries the primary sources.

## Structure of a minimal counterexample

A counterexample to Singmaster would be a value `a` with `N(a) > B` for some
candidate `B`, i.e. strictly more than the conjectured constant. The relevant
structural facts the library fixes:

- The only number with a known large multiplicity is **3003, with N(3003)=8**
  (counting both mirrors plus the trivial pair). Any uniform bound `B`, and any
  lemma implying one, must satisfy `B >= 8`; a proof of `B < 8` is refuted by 3003.
  In the half-triangle convention (`k<=n/2`) this is 4 occurrences.
- There is an **infinite family with N(a) >= 6** (Singmaster/Lind/Tovey Fibonacci
  family, first members 3003 and 61218182743304701891431482520), so `B >= 6`
  generically. N(3003)=8 is the only known multiplicity-8 value.
- Any proof must therefore be consistent with: for infinitely many `a`, `N(a)=6`
  is achieved *with the value inside the triangle*, not just on the boundary —
  the infinite "interior" family is real and optimal for MRSTT's bound of two
  interior solutions.

## Current verification bound

- Verified (primary source, Singmaster 1971 full text + witnesses.json + brute
  oracle): no `a <= 2^48` has N(a) >= 8 except 3003; the six N(a)=6 values
  <= 2^48 are 120, 210, 1540, 7140, 11628, 24310.
- Blokhuis–Brouwer–de Weger 2017 (INTEGERS 17 #A64, held): no unknown collisions
  for `n <= 10^6` or value `<= 10^60`.
- OEIS A003015 corroborates the first terms independently.

## Three restricted classes already settled (with hypotheses)

1. **MRSTT interior**: For `0<eps<1`, `t` large, at most 2 solutions to C(n,m)=t
   in `exp(log^{2/3+eps} n) <= m <= n/2` (at most 4 in the full interior). 
   Hypotheses: eps fixed, t large depending on eps. Leaves open the small-m regime
   `2 <= m <= log t / log_2^{3/2-eps} t`. (arXiv:2106.03335, held.)
2. **Small-(k,l) effective solutions**: `C(n,2)=C(m,3)` (Avanesov, Skolem);
   `C(n,2)=C(m,4)` (de Weger/Pintér, Gelfond–Baker); `C(n,3)=C(m,4)` (Mordell/de
   Weger, genus-3 curve, double cover of an elliptic curve); `C(n,2)=C(m,5)`
   (BMSST, hyperelliptic). Hypothesis: each specific pair (k,l), solved with
   explicit constants. (de Weger, Jenkins, MRSTT refs, held.)
3. **The infinite six-fold family (equality class)**: the equation
   `C(n+1,k+1)=C(n,k+2)` is completely solved — infinitely many solutions,
   `n=F_{2i+2}F_{2i+3}-1, k=F_{2i}F_{2i+3}-1`, giving N(a)>=6 infinitely often;
   this is the unique `a=b` case with infinitely many lattice points in Jenkins'
   curve family. (Singmaster FQ 1975, Lind, MRSTT Remark 1.4, Jenkins, held.)
   Plus the Wu/Stroeker-style bound: `C(x,2)=C(y,p)` finite for p prime (Kiss).

## The central obstruction, named

Finiteness is not a bound. For each fixed `(k1,k2)` the curve `C(x,k1)=C(y,k2)`
is finite (genus > 1 → Faltings; even genus 1 → Siegel), but **both are
ineffective** — no count computable in `(k1,k2)`. Singmaster needs uniformity over
all pairs. Jenkins proved finiteness for the `a != b` curves but could not seal
the `a = b` (golden-ratio) case which is exactly the infinite family. An effective
uniform bound needs general effective Siegel or an effective Schmidt subspace
theorem — out of reach. This is the recognized "finiteness is not a bound" trap;
the run must name it and must not claim a uniform bound from per-pair finiteness.

## Phase-1 exit test

Met: the minimal-counterexample structure (3003 / B>=8, infinite family B>=6),
the verification bound (2^48 primary + 10^6/10^60 Blokhuis), and three restricted
classes with hypotheses are stated and anchored to held primary sources. Further
gathering now happens only against a stated gap in research/REQUESTS.md or a lead
on research/FRONTIER.md the run's own thread demands.

Held sources (see research/sources/): Singmaster 1975 FQ (primary), Abbott–Erdős–Hanson
1974, Kane 2004 & 2007 (summaries), MRSTT 2021 full text, Jenkins 2014 full text,
de Weger 1997 full text, Blokhuis–Brouwer–de Weger 2017 full text, Bugeaud–Mignotte–
Siksek–Stoll–Tengely 2008, Hajdu–Papp–Tijdeman 2022 (Ramanujan J), Tao blog,
Wikipedia, OEIS A003015/A003016. Singmaster 1971 (AMM 78) NOT held — the downloaded
file is the Fermat's Library comments page (see `research/summaries/singmaster-1971.md`).
blog,
Wikipedia, OEIS A003015/A003016.
