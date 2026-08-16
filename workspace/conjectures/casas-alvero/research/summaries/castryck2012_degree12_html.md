# Castryck–Laterveer–Ounaïes, *Constraints on counterexamples to CA, and a verification in degree 12* (arXiv:1208.5404; Math. Comp. 83 (2014) 3017–3037)

Full text: [[castryck2012_degree12_html.full]]

The computational/theoretical cornerstone for this problem. Confirms CA in **degree 12** — the first degree not in the `p^k, 2p^k` families — and lays out the **scenario framework**, the **bad-primes theorem**, and the **variety-of-counterexamples** structure that the run's scheme-theoretic agenda is built on.

## The scenario / type framework (the run's key combinatorial object)

For a degree-d counterexample, `scen(f) = (s_1,…,s_{d−1})` minimizes (lexicographically) the number of distinct recycled roots used, with `s_1 = 0` (normalise a shared root of `f'` to 0) and `s_j ≤ max{s_i : i<j}+1`. `type(f) = max scen(f) = (#recycled roots used) − 1`. For d=12 there are 678570 scenarios total; restricted lists shrink them.

## The variety-of-counterexamples reformulation (most relevant to the run)

```claim
id: ca-variety-results
statement: CA for degree d is equivalent to V_k(d,t) = ∅ for ANY t∈{0,…,d−2}, where
  V_k(d,t) ⊂ weighted P is the projective variety cut out by the resultants
  I_k(d,t) = (Res_x(F, F_H^(j)) | j=2,…,d−1) for
  F = x^2 (x−P_1)…(x−P_t)(x^{d−2−t} + A_1 x^{d−3−t} + … + A_{d−2−t}).
  Each scenario s (type t) gives a subvariety V_k(s) cut out by (F_H^(j)(P_{s_j}))
  parametrising the CA-polynomials matching s; one needs V_k(s)=∅ for each scenario.
hypotheses: k algebraically closed, monic degree d, Hasse derivatives
holds-here: yes — this IS the affine scheme over Z the problem statement asks to study
status: proved (this is the paper's section 4, plus Theorem 5)
follows-from: resultant-reformulation
bearing: This is the exact object the run should attack: irreducible components,
  weighted dimensions, reduction mod p of V_k(s). The A-variables enter linearly,
  so they eliminate easily — the lower the type, the smaller the Gröbner system.
anchor: research/sources/castryck2012_degree12_html.full.md (§4)
falsifies: A held counterexample or a later source redoing degree 12 with a cheaper route.
```

## Bad primes (Theorem 3, 4 from [Graf-von-Bothmer] + this paper)

```claim
id: gvb-lift-and-bad-primes
statement: If no CA-polynomials of degree d exist over F_p-bar, then CA holds in
  degree d p^k for all k≥0 (char 0 and char p). p is "bad" for d iff CA fails in
  degree d char p. Bad primes: sole bad prime for d=3 is p=2; bad primes for d=4
  are {3,5,7} (de Jong–Draisma); d=5: 9 primes {2,3,7,11,131,193,599,3541,8009};
  d=6: 53 primes (Table 1); d=7: 366 primes (largest is 135 digits).
hypotheses: char p; bad-prime lists for d=5,6,7
holds-here: yes
status: asserted-by-source (lists are computed; the d≤5 lists independently checked by Chellali–Salinier)
follows-from: gvb-lift
bearing: The lazy lift CA_{d,p} ⇒ CA_{dp^k,0} is the engine of the settled families.
  It also gives the run a concrete finite filter: verify a small d and its bad
  primes, lift to all dp^k.
anchor: research/sources/castryck2012_degree12_html.full.md (Thm 3, Thm 4, §5)
falsifies: a held source contradicting any listed bad prime.
```

## Degree 12 settled

```claim
id: degree12-settled
statement: Conjecture 1 (CA) is true for d=12. Method: restrict to a small scenario
  list (five 5 scenarios of type 8), run the resultant/Gröbner algorithm in char
  p (=11) rather than char 0. Each of the 5 scenarios took ~3 weeks and ~90 GB RAM.
  The authors state pushing to d=20, the next open case, is "utopic" for this method.
hypotheses: char 0 for the conclusion; computation in F_11
holds-here: yes
status: asserted-by-source (computed, by the authors)
bearing: d=20 is the smallest open degree; direct-over-Q Gröbner is not the route to it.
anchor: research/sources/castryck2012_degree12_html.full.md (Thm 5, §5–6)
falsifies: a held source settling degree 20, or a cheaper independent d=12 verification.
```

## A char-p witness the oracle must pass

`f = x(x−1)^4(x−8)(x−18) ∈ F_23[x]` is a CA-polynomial (not a pure power) whose common-root sets with `f^(1),…,f^(6)` are `{1},{1,18},{1},{0},{18},{1}`; type(f)=2, scen(f)=(0,0,0,1,2,0). A concrete char-p negative control for the oracle.

## What it does NOT settle
Degree 20 (first non-`dp^k`-covered, it is `2^2·5` and 5 is not a good prime for the needed lift) is open. The "does not terminate" boundary: naive algorithm in degree 12 is completely out of reach; the whole art is scenario reduction + working in F_p.
