# Peters & Szekeres 2006, "Computer solution to the 17-point Erdős–Szekeres problem", ANZIAM J. 48, 151–164

Source: https://doi.org/10.1017/S144618110000300X
Full text: [[peters-szekeres - Computer solution to the 17-point ES problem - ANZIAM full.full]]

Settles ES(6)=17: every planar general-position set of 17 points contains a convex 6-subset.
This is the oracle model and the cost reference for any n=7 attack.

## The encoding

- Points ordered by increasing x-coordinate; every ordered triple $(i,j,k)$, $i<j<k$, gets a
  signature $\sigma(i,j,k)\in\{+,-\}$ = orientation (chirotope). $\Sigma_n$ = set of such
  signature functions on $[n]$ (2^C(n,3) of them); realizable ones form a small subset.
- **Cups/caps (Chung–Graham):** an ordered $\varepsilon$-chain $[a_0,\dots,a_i]$ has
  $\sigma(a_{\mu-2},a_{\mu-1},a_\mu)=\varepsilon$ for all $\mu$; $C_{+i}$ = $(i+1)$-cup, $C_{-i}$ =
  $(i+1)$-cap.
- **Convex k-subset:** union of a cup and a cap sharing both common endpoints $a_0=a$, $a_i=b$.
- **Geometric constraints (necessary for realizability):** for each 4-subset, writing the four
  triples $\sigma_1\dots\sigma_4$, convex quad iff $\sigma_1=\sigma_2,\ \sigma_3=\sigma_4$; concave
  quad iff $\sigma_1=-\sigma_4,\ \sigma_2=\sigma_3$. 8 of 16 signatures per quad are "geometric".
  $E^*_n$ = signatures satisfying these constraints on every 4-subset. (Necessary but NOT
  sufficient — Knuth's 9-point non-realisable example; so $(P^*)_{n,k}$ is stronger than the
  geometric $(P)_{n,k}$.)
- **9-point case (ES(5))**: 6-set convex iff its 10 triples satisfy one of 4 convex relations
  $R_1$–$R_4$ (504 relations over all 5-subsets). Search over 84-array with incremental
  assignment; finishes <1 sec on 1.5GHz.
- **17-point case (ES(6))**: 6-set convex iff its 20 triples satisfy one of **8** convex relations
  $R_1$–$R_8$ (totalling 8·C(17,6)=99,008 relations). $|\Omega^*|=892$ concave signatures
  compatible with the geometric constraints; assign to the 12 contiguous 6-subsets
  $U_i=[i,\dots,i+5]$ of $S_{17}$ (each pair shares 5 points = 10 triples). Extensions: the
  $U_{13}=[9,13,14,15,16,17]$ check, one-bit and two-bit checks. 446 independent assignments to
  $U_1$.
- **Cost:** ~3000 GHz-hours (1500 hours on ≤2 GHz machines); 446-way parallel; each single
  assignment took 1–20 hours. Three independent implementations (Szekeres, Peters, McKay) agree.

```claim
id: ps-es6
statement: ES(6) = 17: every 17-point planar set in general position contains 6 points in convex position, and 16 do not suffice.
hypotheses: planar, general position; signature functions satisfying the 8 geometric (4-subset) constraints
holds-here: yes
status: proved (computer-assisted, 3 independent implementations)
bearing: the oracle target ES(6)=17 and the exact verification bound the oracle must reproduce (criterion 3); the n=7 cost model (order of magnitude 3000+ GHz-hours per n).
anchor: research/sources/peters-szekeres - Computer solution to the 17-point ES problem - ANZIAM full.full.md
```

## What it does not settle

ES(7). Also $n_0(7)$ would be a far larger search; the 8-convexity-relation + contiguous-6-subset
framework is the natural staging for it, and is what the 33-point SAT works build on. Verified by
independent reimplementation, not by a proof certificate.
