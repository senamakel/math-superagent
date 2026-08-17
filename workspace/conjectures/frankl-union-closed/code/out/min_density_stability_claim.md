# Min-density uniqueness claim: min-density UC families are the near-n-cube

```claim
id: min-density-uc-families-are-near-n-cube
statement: For n in {2,3,4,5}, every union-closed family F on [n] that attains
the minimum density 1/(2^{n-1}+1) is isomorphic to the near-n-cube
(2^[n-1] union {[n-1] union {n}}, |F|=2^{n-1}+1), whose sorted-descending
abundance profile is [(2^{n-2}+1) repeated n-1 times, 1]. The min-density class
is exactly ONE isomorphism class of size n (one choice of the distinct count-1
element), all other coordinates sitting at the plateau 2^{n-2}+1. n=5 is the
new step: the cascade over all 2771102 UC families on [5] gives equality class
profile (9,9,9,9,1) with 5 families, all isomorphic to the near-5-cube.
hypotheses: F a union-closed family on [n], genuinely on n (the near-n-cube is
extreme), attaining density 1/(2^{n-1}+1) = WORST(n) (equivalently total
member-set sizes minimal for its size, or min-density equal to the sourced
Das-Wu/Nagel extremal value).
holds-here: yes
status: verified-computational — uniqueness up to isomorphism PROVED for
n<=4 by the independent small capture (min_density_stability_small.captured.txt,
exhaustive enumeration through the oracle lib.uc, distinct min-density profile
== near-n-cube profile, all min-density families isomorphic to the near-n-cube),
and n=5 by the cascade in min_density_stability (min-present-count==1 BROAD
class vs EQUALITY class; the statement is about MIN-DENSITY, i.e. the EQUALITY
class, NOT the min-present-count==1 class).
bearing: DISTINGUISH the two notions. min-present-count==1 (some element with
count 1) only forces m <= 2^{n-1}+1; density equality 1/(2^{n-1}+1) additionally
forces m = 2^{n-1}+1. Non-near-cube families with min-present-count 1 and
m < 2^{n-1}+1 (e.g. n=4 counts (4,3,3,1), n=5 counts (6,5,4,3,1)) have density
1/m > 1/(2^{n-1}+1) and are NOT density-extremal. The uniqueness claim is about
the min-DENSITY class (the EQUALITY class), which has exactly ONE profile, not
about the broader min-count class (which has 27 profiles at n=4, 166 at n=5).
anchor: code/out/min_density_stability.captured.txt (promoted from .raw.txt),
code/out/min_density_stability_small.captured.txt, code/out/min_density_stability.py
```
