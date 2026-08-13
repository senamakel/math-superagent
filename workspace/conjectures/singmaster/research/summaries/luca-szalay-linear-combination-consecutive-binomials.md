# Luca–Szalay, "Linear diophantine equation with three consecutive binomial coefficients" (2004)

Source: https://ami.uni-eszterhazy.hu/uploads/papers/finalpdf/AAPASM_31_from53to60.pdf
Acta Academiae Paedagogicae Agriensis, Sectio Mathematicae 31 (2004) 53–60.
Full text: `research/sources/luca-szalay-linear-combination-consecutive-binomials.full.md`.

## What it establishes

The paper classifies, for fixed integers A, B, C (A>0, C≠0, gcd(A,B,C)=1), when
the linear-diophantine equation in three consecutive binomial coefficients

```
A·C(n,k) + B·C(n,k+1) + C·C(n,k+2) = 0     (1 ≤ k < k+2 ≤ n−1)
```

has **infinitely many** integer solutions (n,k). The theorem:

- **(i) B = A+C, C<0**: all solutions lie on the straight line A(k+2)+C(n−k) = 0.
- **(ii) A=A0², B=−2A0C0, C=C0²** (coprime A0,C0): all solutions are
  k+2 = t(t+C0)/(A0(A0+C0)),  n−k = t(t−A0)/(C0(A0+C0)), t a positive integer
  in a congruence class mod A0C0(A0+C0) with t above a computable threshold.
- **(iii) B≠A+C, D=B²−4AC > 0 nonsquare**: all solutions come from
  finitely many binary recurrent sequences solving the Pell-type equation
  X²−DY² = E with X,Y,E explicit (X=(B²−4AC)(n−k)−A(B−2C), Y=2A(k+2)+B(n−k)−A,
  E=4A²C(A−B+C)).
- If D<0 or D a perfect square (with E≠0), there are only finitely many solutions.

Method: substitute x=k+2, y=n−k, complete the square to a conic and, in the
indefinite case, to a Pell equation. The proof is elementary (no heights).

## Bearing for this run

- **Attests Goetgheluck (Math. Comp. 67 (1998) 1727–1733) precisely.** The
  ratio-2 families `C(n,k)=2·C(a,b)` were previously an unattested REQUESTS row;
  the citations here fix the journal/page and describe the family solved via the
  Pell equation x²−3y²=−2.
- Illustrates the standard near-collision engine (substitute the middle column,
  complete the square, Pell) that appears in the run's k-column / consecutive-
  blocks threads — the same shape as Goetgheluck, Satoh, and the near-collision
  literature. The three-consecutive-coefficient equation is adjacent to the
  run's equal-products structure, not identical to it.
- Not load-bearing for the impossibility argument; corroboration + a missing
  citation fixed.

```claim
id: luca-szalay-three-consecutive-classification
statement: For fixed integers A>0, C≠0, gcd(A,B,C)=1, the equation
  A·C(n,k)+B·C(n,k+1)+C·C(n,k+2)=0 (1≤k<k+2≤n−1) has infinitely many integer
  solutions iff (i) B=A+C and C<0 (solutions on a line), or (ii) A=A0², B=−2A0C0,
  C=C0² (explicit quadratic family), or (iii) D=B²−4AC>0 nonsquare and the Pell
  equation X²−DY²=E has infinitely many solutions (binary recurrent sequences).
  Otherwise finitely many. Proof is elementary (conic/Pell completion).
hypotheses: A,B,C fixed integers, A>0, C≠0, gcd=1, 1≤k<k+2≤n−1.
holds-here: no — this is the three-consecutive-coefficient linear equation, not
  the run's equal-products two-variable equation C(x,k1)=C(y,k2); it is adjacent
  structure (near-collision engine), not a route to the conjecture.
status: asserted (source's theorem, elementary, not re-derived here).
bearing: corroboration of the near-collision method; fixes the Goetgheluck 1998
  citation (Math. Comp. 67, 1727–1733) and its Pell structure.
anchor: research/sources/luca-szalay-linear-combination-consecutive-binomials.full.md
```
