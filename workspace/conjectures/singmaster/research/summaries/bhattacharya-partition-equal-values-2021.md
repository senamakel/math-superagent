# A. Bhattacharya, "Equal values of certain partition functions via Diophantine equations" (Research in Number Theory 7 (2021) #67)

Source: https://link.springer.com/article/10.1007/s40993-021-00293-7 (open access)
Full text: `research/sources/bhattacharya-partition-equal-values-2021.full.md`

## What it is

Open-access 2021 study of when partition functions P_A(n) (partitions of n with
parts in a finite set A) take equal values, P_A(x) = P_B(y). This is the
partition-function analogue of equal-values problems (and the paper's starting
point is a question of Benne de Weger about the equal-binomial-coefficients
literature). It appeared as a frontier target of this run's own library (the
earlier HPTV/Prouhet-Tarry-Escott thread cited the partition/Figurate family
papers). Filed for breadth of the equal-values subject.

## Results (from the abstract/entry)

- **Thm 2.1**: for A = {a1,a2} with gcd(a1,a2)=1 and any f ∈ Z[x] of positive
  degree and positive leading coefficient, P_A(x) = f(y) has infinitely many
  positive integer solutions.
- **Thm 3.1/3.2**: P_3(x) = P_4(y) has infinitely many solutions; P_3(x) =
  P_5(y) has only finitely many, fully characterized.
- **Thms 4.3-4.5**: for A = {1,2,a}, a≥3, y² = P_A(x) and P_A(x) = P_B(y)
  (B={1,2,b}, a≠b, mild conditions) have infinitely many positive solutions.

Method: explicit parametric families (partition functions are quasipolynomials
for finite A) reducing to curve/Diophantine analysis.

## Relevance

- It is the *opposite* direction from Singmaster: here equal values are made to
  occur *infinitely often* by construction, whereas Singmaster asks whether the
  binomial triangle has bounded multiplicity. The structural contrast — which
  combinatorial families admit infinite equal-value families and which do not —
  is exactly the (5,4,3)/(6,4,4)-exceptions structure in HPTV 2014 and the
  Bilu-Tichy exceptional pairs.
- Provides the modern survey-frame reference for "equal values of X via
  Diophantine equations" that the run's library cites.

## Claims

```claim
id: partition-equal-values-infinite-families
statement: Bhattacharya 2021 (Research in Number Theory 7 #67, open access):
  for A={a1,a2} with gcd(a1,a2)=1 and any f in Z[x] positive degree/leading
  coefficient, P_A(x)=f(y) has infinitely many positive integer solutions;
  P_3(x)=P_4(y) has infinitely many, P_3(x)=P_5(y) finitely many (all found);
  and for A={1,2,a}, y^2=P_A(x) and P_A(x)=P_B(y) have infinitely many
  positive solutions under mild conditions.
hypotheses: A finite; partition functions P_A quasipolynomial; conditions as
  stated.
holds-here: context only — partition functions, not binomial coefficients; the
  infinite-equal-values phenomenon is the structural contrast to Singmaster's
  bounded-multiplicity question.
status: asserted
bearing: breadth of the equal-values subject; illustrates which combinatorial
  families admit infinite equal-value families (contrast with the binomial
  triangle's known infinite families being few and classified).
anchor: research/sources/bhattacharya-partition-equal-values-2021.full.md
```