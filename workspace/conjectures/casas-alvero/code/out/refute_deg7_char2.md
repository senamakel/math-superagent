# Refutation: CA in degree 7 over F_2 is FALSE (p=2 is a bad prime for n=7)

**Refuter finding, first n=7 refutation in the refute set.**

## Statement attacked

CA in degree 7 over F_2, Hasse-derivative formulation: a monic degree-7 f over
F_2 sharing a root with each Hasse derivative H_1..H_6 is a pure power.
This is the char-p version of the run's load-bearing bad-prime claims
(`G-bad-prime-extension`, `badprimes-*`): it is the concrete content of the
published degree-7 bad-prime list (Castryck et al. 2012 Thm 4: for d=7 the
smallest non-bad prime apart from 7 is 127, so every prime <127 except 7 — in
particular p=2 — is bad for degree 7). The n=6/n=7 bad-prime lists had
previously been taken only on source word (the J_T minors criterion is
infeasible at n=6, and the refute set reached degree 6 but never degree 7).

## Witness (derived by hand, confirmed by find_counterexample)

```
f(x) = x^7 + x^3  over F_2  =  x^3 (x+1)^4
```

Roots {0 (mult 3), 1 (mult 4)} → **not a pure power** (two distinct zeros).

Hasse derivatives over F_2 (H_i = Σ_j C(j,i) c_j x^{j−i}; c7=1, c3=1),
each sharing a root with f:

| i | H_i | mod 2 | common root |
|---|---|---|---|
| 1 | 7x^6 + 3x^2 | x^6 + x^2 | 0 |
| 2 | 21x^5 + 3x | x^5 + x | 0 |
| 3 | 35x^4 + 1 | x^4 + 1 | 1 |
| 4 | 35x^3 | x^3 | 0 |
| 5 | 21x^2 | x^2 | 0 |
| 6 | 7x | x | 0 |

Check on F_2 = {0,1}:
- f(0)=0, f(1)=1+1=0
- H_1: H_1(0)=0, H_1(1)=1+1=0 → shares root 0
- H_2: H_2(0)=0, H_2(1)=1+1=0 → shares root 0
- H_3: H_3(0)=1, H_3(1)=1+1=0 → shares root 1 (f(1)=0)
- H_4=x^3, H_5=x^2, H_6=x: all vanish at 0, which is a root of f

## Engine confirmation

`find_counterexample` on `code/refute/ca_deg7_char2.p` returns **refuted**
(SZS CounterSatisfiable), producing exactly the above model: f(0)=f(1)=0;
h1=h2=(0,0); h3=(1,0); h4=h5=h6=identity-value. Every hypothesis axiom
(f shares a root with each H_1..H_6) holds; the conclusion (pure power =
single zero at 0 or 1 only) fails because f has two distinct zeros.

## Alignment with the published lists

- Castryck et al. 2012 Thm 4: degree-7 bad primes are all primes <127 except
  7; so p=2 is bad for n=7. Consistent.
- Sufficient binomial criterion (Schaub–Spivakovsky Cor 8): p | C(7,1)−1 = 6,
  so 2 is certified bad for n=7. Consistent.
- This is an independent finite-model confirmation of a list the run had only
  on source word, at the smallest degree (7) the refute set had never
  exercised.

## What this is, and what it is not

This **refutes the char-p statement** (CA_7,2 in the Hasse formulation). It is
**not** a counterexample to CA in characteristic 0 — CA holds in char 0 for
all degrees, and this is exactly the positive-characteristic degeneration the
whole approach predicts breaks. It confirms the admissibility test: any
argument for CA in degree 7 must use characteristic 0 somewhere and must break
over F_2, and here the break is per-index Hasse degeneracy (none of H_1..H_6
vanishes identically here, yet the roots still don't collapse).

```claim
id: deg7-char2-refuted
statement: CA in degree 7 over F_2 is FALSE in the Hasse formulation:
  f = x^7 + x^3 = x^3(x+1)^4 over F_2 has two distinct roots {0,1}
  (0 mult 3, 1 mult 4), is NOT a pure power, yet shares a root with every
  Hasse derivative H_1 = x^6+x^2 (root 0), H_2 = x^5+x (root 0),
  H_3 = x^4+1 (root 1), H_4 = x^3, H_5 = x^2, H_6 = x (root 0). Hence p=2 is
  a bad prime for degree 7, confirming the 7-entry of the published degree-7
  bad-prime list (Castryck et al. 2012 Thm 4: all primes <127 except 7 are
  bad for d=7) and the binomial criterion (2 | C(7,1)-1 = 6). This is the
  first n=7 refutation in the refute set, an independent finite-model check
  of a degree-7 list the run previously held only on source word.
hypotheses: char 2; degree 7 (Hasse formulation)
holds-here: yes — confirms the published degree-7 bad-prime list at its
  smallest bad prime; consistent with the sufficient binomial criterion
status: checked (find_counterexample refuted code/refute/ca_deg7_char2.p;
  witness hand-verified against the oracle's Hasse-derivative definition)
anchor: code/refute/ca_deg7_char2.p
falsifies: nothing in char 0; it is the char-p degeneration the approach
  predicts. It does not settle whether the degree-7 list's 366-vs-661
  cross-source count discrepancy (de Frutos Marín vs Castryck) is resolved —
  it merely confirms p=2 is bad for n=7.
```
