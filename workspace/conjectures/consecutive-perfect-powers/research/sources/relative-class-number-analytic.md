# The analytic class number formula and the minus part of the class group of Q(zeta_p)

## Source URLs

- Shokrollahi, M., "Relative class number of imaginary Abelian fields of prime
  conductor below 10000", Math. Comp. 68 (1999).
  https://doi.org/10.1090/s0025-5718-99-01139-4
- Schoof, R., "Class numbers of real cyclotomic fields of prime conductor", Math.
  Comp. 72 (2003), 913–937. https://doi.org/10.1090/S0025-5718-02-01432-1
  (full text read server-side from https://www.mat.uniroma2.it/~schoof/realcyc.pdf)
- Ichimura, H., "A class number formula for the p-cyclotomic field", Arch. Math.
  87 (2006), 539–545. https://doi.org/10.1007/s00013-006-1867-7
- Hida, H., course notes "Elementary Iwasawa theory for cyclotomic fields"
  (UCLA). https://www.math.ucla.edu/~hida/207a.1.18w/Lec1.pdf
- Hirabayashi, M., "A determinant formula for the relative class number of an
  imaginary abelian number field", Comm. Math. 22 (2014), 133–140.
  http://hdl.handle.net/10338.dmlcz/144126

These are the machine tier for the open content of the run's problem: the
obstruction to `x^p - y^q = 1` (p,q odd primes) is the class group of
`Q(zeta_p)`. This note records what the library establishes about that group and
its order. It supplies no bound and no proof for the challenge equation itself;
it is the toolkit the run's own derivation must use.

## Setup

Let `p` be an odd prime and `K = Q(zeta_p)` the `p`-th cyclotomic field, with
`K+ = Q(zeta_p + zeta_p^{-1})` its maximal real subfield. Let `G = Gal(K/Q)`.
Complex conjugation `c` acts on the class group `Cl(K)`; write
`Cl^+` and `Cl^-` for the `+1` and `-1` eigenspaces, and `h = #Cl(K)`,
`h^+ = #Cl(K+)`, `h^- = h/h^+` for their orders. The exact sequence

    0 -> Cl^+ -> Cl(K) -> Cl^- -> 0

holds (Schoof). `h^+` is the class number of the real subfield; `h^-` is the
"relative" or "minus" class number.

The library's key fact (Kummer's theorem, in this modern form) is that the minus
part is entirely computable, while the plus part is not:

- `h^-` is given by an explicit formula in terms of generalized Bernoulli
  numbers (below), and is easy to compute for large `p`.
- `h^+` is famously hard: it is not known for a single prime `p >= 71`
  (Schoof, abstract; Washington, cited therein).

## The relative class number formula (Shokrollahi; Washington Thm 4.17/Cor 4.13)

For `K` an imaginary subfield of `Q(zeta_p)` with maximal real subfield `K+`:

    h^-(K) = Q w \prod_{\chi \text{ odd}} (-1/2 B_{1,\chi})

where:

- `\chi` runs over the **odd** Dirichlet characters of `Gal(K/Q)`
  (i.e. `\chi(-1) = -1`);
- `B_{1,\chi}` are the first **generalized Bernoulli numbers** attached to
  `\chi`:
  - `B_{1,1} = -1/2` (trivial character),
  - `B_{1,\chi} = (1/p) \sum_{a=1}^{p} \chi(a) a` for `\chi != 1`, normalized so
    that `B_{1,\chi} = -L(0, chi)` for a primitive character;
- `w` is the number of roots of unity in `K`;
- `Q = [E : W E+]` (the unit index), where `E, E+` are the unit groups of `K, K+`
  and `W` the roots of unity in `K`.

Specialising to `K = Q(zeta_p)` (Shokrollahi eq. 2.1):

    h^-(Q(zeta_p)) = 2p \prod_{\chi \text{ odd mod } p} (-1/2 B_{1,\chi})
    h^-(Q(zeta_p)^(\pm)) = ... (imaginary subfields: `w = 2` unless `K = Q(zeta_p)`,
    where `w = 2p`).

For a primitive odd character `chi` mod `p`, `B_{1,\chi} = (1/p)\sum a chi(a)`,
and `-L(0,chi) = B_{1,\chi}`.

**Equivalent product form** (Schoof's statement, used for computation): as a
product over the odd primitive characters `chi` mod `p`,

    h^- = \prod_{\chi \text{ odd}} |B_{1,\chi}| / p

(i.e. `p`-normalised), which is the value of `\prod L(0,\chi)` up to the root
count. The exact normalisation to use in `code/` must be pinned to one stated
source; the two displayed forms differ by the `2p`/`w`/`Q` factors. **Note for
the oracle**: use Shokrollahi's eq. (2.1) verbatim, `h^- = 2p \prod (-1/2 B_{1,\chi})`
for `K = Q(zeta_p)` (with `Q = 1` and `w = 2p` in that case), otherwise
`h^- = 2 \prod (-1/2 B_{1,\chi})` for `K = Q(zeta_p)^(\pm)` with `w = 2`.

`p` is **regular** (Kummer) iff `p` divides none of the numerators of
`B_2, B_4, ..., B_{p-3}` (ordinary Bernoulli numerators), equivalently iff
`p \nmid h^-`. The irregular pairs `(p, 2k)` with `p | B_{2k}` numerator are
exactly the primes for which `Cl^-` has nontrivial `p`-part.

## Stickelberger's theorem (Hida notes, Thm 5.2; Ichimura; Sinnott)

`G = Gal(Q(zeta_p)/Q) = (Z/pZ)^\times` via `sigma_a(zeta_p) = zeta_p^a`. The
Stickelberger element is

    theta = (1/p) \sum_{a=1}^{p-1} a sigma_a^{-1}  (in Q[G]).

The ideal `I0 = { beta in Z[G] : beta theta in Z[G] }` and the Stickelberger
ideal `s = I0 * theta = Z[G] theta cap Z[G]`. Theorem (Stickelberger): **`s`
annihilates `Cl(K)`** — for every fractional ideal `A` and every
`beta in I0`, the ideal `A^{beta theta}` is principal.

Iwasawa's index formula: `[Z[G]^- : s^-] = h^-`, the relative class number.
(Ichimura restates this and, for `p ≡ 3 mod 4` and a subgroup `H` of index 2,
proves `[Z[H] : s_H] = h^- / h(Q(sqrt(-p)))`.) Sinnott (Ann. Math. 1978)
computed `[R^- : S^-]` and `[E+ : C+]` (circular units index) in terms of
`h, h^+, h^-`.

## Why this is the machine tier for the run's problem

The open content is: both exponents odd primes, `Z[zeta_p]` factorisation, the
obstruction is the class group. The library entries here give, one and all, the
**computable** side of that obstruction:

- the order `h^-` via Bernoulli numbers (exact integer arithmetic),
- the generators/indices of the Stickelberger ideal (the annihilator),
- the unit index / circular units relations (Sinnott).

The **plus** side (`h^+`) is the part nobody can compute past `p = 67`, which is
why the run's own proof must not assume control of it. This asymmetry — minus
computed, plus not — is the first structural fact the run should state and use.

## Claims

```claim
id: minus-class-number-formula-statement
statement: >
  For K = Q(zeta_p), p odd prime, the relative (minus) class number is
  h^-(K) = 2p * prod_{chi odd mod p} (-1/2 B_{1,chi}), with
  B_{1,chi} = (1/p) sum_{a=1}^{p} chi(a) a for chi non-trivial, B_{1,1} = -1/2.
  For a proper imaginary subfield K of Q(zeta_p), h^-(K) = 2 * prod_{chi odd} (-1/2 B_{1,chi})
  and w = 2. In all cases Q = 1 for K = Q(zeta_p).
hypotheses: p an odd prime; K an imaginary subfield of Q(zeta_p).
holds-here: >
  yes — every hypothetical second solution has p an odd prime, and the minus class
  group of Q(zeta_p) is exactly the part of the class group computable; the formula
  is essential to assigning h^- values to the exponent pairs in check_conditions.
status: sourced (Shokrollahi eq. 2.1; Washington Thm 4.17 / Cor 4.13, cited therein).
  The same formula is verified independently — see the checked claim
  'minus-class-number-formula' (code/out/hminus_verify_note.md).
anchor: research/sources/relative-class-number-analytic.md
follows-from: minus-class-number-formula
bearing: gives the exact integer value of h^-(Q(zeta_p)) for arbitrary odd prime p, the obstruction's computable half.
```

```claim
id: minus-class-computable-plus-not
statement: >
  h^- of Q(zeta_p) is given by an explicit Bernoulli-number product and is easy to
  compute for very large odd primes p; h^+ of Q(zeta_p) is not known for any single
  prime p >= 71.
hypotheses: p an odd prime.
holds-here: yes — states the computable/vs-hard split of the obstruction.
status: sourced (Schoof abstract: "h^+ ... not known for a single prime l >= 71"; Kummer/Shokrollahi for h^- computation to p < 10000).
anchor: research/sources/relative-class-number-analytic.md
bearing: any run-proof that needs the plus part must not assume it computed; this bounds what a computational check can establish.
```

```claim
id: stickelberger-annihilates-plus-index-formula
statement: >
  The Stickelberger ideal s = Z[G]theta cap Z[G] annihilates the class group of
  Q(zeta_p), and [Z[G]^- : s^-] = h^-.
hypotheses: p an odd prime, G = Gal(Q(zeta_p)/Q), theta the Stickelberger element.
holds-here: yes — the class-group obstruction is exactly what these annihilators control.
status: sourced (Stickelberger's theorem via Hida Lec1 Thm 5.2; Iwasawa's index formula via Ichimura 2006).
anchor: research/sources/relative-class-number-analytic.md
bearing: the tool that turns the ideal relation forced by x^p - y^q = 1 into an element relation whenever the relevant prime is in the minus part; the run's descent would run through it.
```

Verified-by: multiple independent sources agree on the formula's shape:
Shokrollahi (explicit eq. 2.1 with Q, w), Schoof (product over odd chi of
|B_{1,chi}|/p), Hida (Stickelberger annihilator + Iwasawa index), Ichimura
(index formula). The three formula shapes are mutually consistent up to the
stated normalisation factors (2p, w, Q).

```claim
id: minus-class-normalisation-checked
statement: >
  The normalisation h^-(Q(zeta_p)) = 2p * prod_{chi odd mod p} (-1/2 B_{1,chi})
  (Q=1, w=2p for K=Q(zeta_p)) is pinned correctly: exact hand computation
  following Shokrollahi eq. 2.1 gives h^-=1 for p=3 and h^-=1 for p=5, matching
  the known catalogued values. For p=3: B1=-1/3, (-1/2)B1=1/6, 2p*1/6=1.
  For p=5: odd chars k=1,3 give (-1/2)B1 = 3/10 +- i/10, product = 1/10,
  2p*1/10 = 1. So the 2p factor (with Q=1, w=2p) is not off by a factor; the
  earlier "other normalisation" risk is resolved for at least p=3,5.
hypotheses: p an odd prime; chi over odd Dirichlet characters mod p;
  B_{1,chi}=(1/p) sum_{a=1}^{p} chi(a) a.
holds-here: yes — this is the order of the minus class group of Q(zeta_p),
  the obstruction for check_conditions(p,q).
status: checked (exact symbolic arithmetic by hand, p in {3,5}; the remaining
  values 7,11,13,23,31,37,43 must come from the scaffold run, not recalled).
anchor: research/sources/relative-class-number-analytic.md
bearing: confirms the minus-class number formula's normalisation, so
  check_conditions(p,q) can compute h^- directly; the formula is load-bearing
  for assigning h^- to exponent pairs.
```
