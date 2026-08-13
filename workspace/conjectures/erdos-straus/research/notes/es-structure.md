# Structure of the Erdős–Straus open classes: six residues mod 840, verification bounds, minimal counterexample, and why the six resist identity shapes

Question: exactly which residue classes mod 840 remain open for `4/n = 1/x+1/y+1/z`
with `x,y,z ∈ ℕ` (Erdős–Straus 1948), why the other 834 are settled, what the
current and older verification bounds are, what a minimal counterexample must
look like, and the precise obstruction that keeps the six open classes out of
reach of the standard identity families.

Convention: `n ≥ 2`; a *solution* is a triple of positive integers. `Type I`
means `n | x` and `gcd(n,y) = gcd(n,z) = 1`; `Type II` means `n | y, n | z` and
`gcd(n,x) = 1` (Elsholtz–Tao [ET13] §1). A primitive residue class `r mod q`
is `gcd(r,q) = 1`.

---

## (a) The six open classes, and why the other 834 are settled

**Exact statement (sourced).** Mordell (1967): the classical polynomial
identity families give a three-term expansion of `4/n` for every `n` except
possibly those congruent to one of

```
1, 121, 169, 289, 361, 529   (mod 840)
```

- **Wikipedia** (Erdős–Straus conjecture): "Polynomial identities listed by
  Mordell (1967) provide three-term Egyptian fractions for 4/n whenever n is
  one of: 2 mod 3, 3 mod 4, 2 or 3 mod 5, 3, 5, or 6 mod 7, or 5 mod 8.
  Combinations of Mordell's identities can be used to expand 4/n for all n
  except possibly those that are 1, 121, 169, 289, 361, or 529 mod 840. The
  smallest prime that these identities do not cover is 1009."
  https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Straus_conjecture
- **Erdős problems #242** (Bloom, citing Mordell [Mo69] *Diophantine
  Equations*, 1969, pp. 287–290): "Arguing via parametric solutions, Mordell
  [Mo69] proved it is true for all n except those congruent to one of
  {1,121,169,289,361,529} modulo 840."
  https://www.erdosproblems.com/242
- **Elsholtz–Tao** (arXiv 1107.1010, final version, §10): "It is well-known
  (see [39 = Mordell]) that any primitive residue class n = r mod 840 is
  solvable by polynomials unless r is a perfect square."
  https://arxiv.org/abs/1107.1010

**Why each of the other 834 of the 840 classes is settled (derived by hand
CRT; cross-checked against two published residue lists).** The five families
cover exactly the residues that satisfy at least one of:

| family | residue | identity (Type) |
| --- | --- | --- |
| mod 3 | `n ≡ 2` | `4/n = 1/n + 1/((n+1)/3) + 1/(n(n+1)/3)` (Type I) |
| mod 4 | `n ≡ 3` | corrected form, `x = (n+1)/4, y = n(n+1)/4 + 1, z = y(y−1)` (Type I) |
| mod 5 | `n ≡ 2, 3` | attested by Mordell/Wikipedia (polynomial form not in this run's sources) |
| mod 7 | `n ≡ 3, 5, 6` | attested by Mordell/Wikipedia |
| mod 8 | `n ≡ 5` | `4/n = 1/(2t) + 1/(t(8t−3)) + 1/(2t(8t−3))`, `n = 8t−3` (Type I) |

`lcm(3,4,5,7,8) = 840`, so the five families together impose a condition mod
840. Hand CRT (exact arithmetic; see the note below):

- To avoid `2 mod 3`, `3 mod 4`, `5 mod 8` and lie in a class containing
  primes (`gcd(r,840)=1`), one must have `r ≡ 1 (mod 24)`: the candidate
  `r ≡ 1 (mod 12)` classes mod 24 are `{1, 13}`, and `13 ≡ 5 (mod 8)` fires
  the mod-8 family, so `r ≡ 1 (mod 24)` is forced. (This is exactly Salez's
  "ℕ₀ = {n : n ≡ 1 mod 24}" reduction, [Sa14] §3.)
- Adding "avoid `2,3 mod 5`" for `r ≡ 1 mod 24`: `r = 1 + 24k ≡ 1 + 4k
  (mod 5) ∈ {1,4}` gives `k ≡ 0, 2 (mod 5)`, i.e. `r ≡ 1, 49 (mod 120)` —
  this is Salez's published `R₁ = {1, 49}` (mod 120), [Sa14] §4.1.
- Adding "avoid `3,5,6 mod 7`": `r = r₀ + 120j` with `r₀ ∈ {1,49}`,
  `j = 0..6`; since `120 ≡ 1 (mod 7)` and `49 ≡ 0 (mod 7)`, the surviving
  `r mod 7 ∈ {1,2,4}` give `r ∈ {1, 121, 361} ∪ {169, 289, 529}` —
  precisely Salez's published `R₂ = {1, 121, 169, 289, 361, 529}` (mod 840),
  [Sa14] §4.1 ("It was the choice made by Swett").

So a residue class mod 840 that avoids all five families **and** contains
primes is exactly one of the six; every other class either (i) fires one of
the five Type-I polynomial families, or (ii) has `gcd(r,840) > 1`, in which
case its members are composite or one of 2,3,5,7, handled by the trivial even
identity, the explicit small primes, and the prime/composite reduction (below).
That is the reason "834 of the 840" are settled.

**Both published lists agree with the hand CRT:** Wikipedia's six residues and
Salez's `R₂` are the same set. (Mechanical re-check script written but *not*
executed by this role: `code/es_structure/verify_es_structure.py`; its
output file `code/out/es_structure.verify.txt` does not exist yet.)

**The six classes are exactly the square classes among the primitive classes
mod 840 (derived + sourced):** `121 = 11², 169 = 13², 289 = 17², 361 = 19²,
529 = 23², 1 = 1²`, with all of `1,11,13,17,19,23` coprime to 840. Conversely
any odd `s` coprime to 840 satisfies `s² ≡ 1 (mod 24)`, `s² ≡ 1 or 4
(mod 5)`, `s² ≡ 1,2,4 (mod 7)`, so `s² mod 840` is one of the six. Hence

```
{open classes mod 840} = {r mod 840 : r odd, gcd(r,840)=1, r a square mod 840}
```

This is the "unless r is a perfect square" clause in the Elsholtz–Tao §10
statement verbatim.

---

## (b) Verification bounds

| bound | who | when | how | source |
| --- | --- | --- | --- | --- |
| `10^14` | Allan Swett | 1999 | sieve, one modular equation, 150 hours | Salez abstract; Elsholtz–Tao Table 1; Wikipedia |
| `2×10^14` | Bello-Hernández, Benito, Fernández | 2012 | — | Elsholtz–Tao Table 1 |
| `10^17` | Serge E. Salez | 2014 | seven-modular-equation sieve (`ℕ₇`, moduli < 5000), C++ | arXiv:1406.6307 |
| `10^18` | Mihnea & Dumitru | 2025 | extends Salez's modular-filter method (filters to S₂₉, `G₈ = 25,878,772,920`, 2,101,514 residue classes, 140,000 prime filters), parallel | arXiv:2509.00128 |

- **Salez 10^17** (`https://arxiv.org/abs/1406.6307`): "In 1999 Allan Swett
  checked ... up to N = 10^14 with a sieve based on a single modular equation.
  After having proved the existence of a 'complete' set of seven modular
  equations (including three new ones), this paper offers an optimized sieve
  based on these equations." §4.2: every `n ∈ ℕ₇` (the six-class survivors
  `R₂` under `G₇ = 892,371,480`) below `10^17` that is **not a square** has a
  modular certificate; the 51,732,427 squares encountered were checked
  separately. So "verified up to 10^17" means: every n ≤ 10^17 has a
  three-term expansion.
- **10^18 (current, 2025)** (`https://arxiv.org/abs/2509.00128`): "We
  provide empirical evidence for the Erdős-Straus conjecture by improving
  computational bounds to 10^18 ... Build on Salez's modular filtering
  approach, extending filters to S₂₉ and obtaining a residue set R₈ modulo
  G₈ = 25,878,772,920 with 2,101,514 residue classes that must be checked."
  Recorded by the Erdős problems database: "This has been verified for all
  n ≤ 10^18 [MiDu25]" (`https://www.erdosproblems.com/242`).
- **Older bounds** (Elsholtz–Tao Table 1, `research/sources/pomerance-erdos-straus.full.md`):
  Straus ≤ 1950 (5·10³), Bernstein 1962 (8·10³), Shapiro ≤ 1969 (2·10⁴),
  Obláth 1948/9 (106,128), Rosati 1954 (141,648), Yamamoto 1964 (10⁷),
  Jollensten 1976 (1.1·10⁷), Terzi 1971 (10⁸), Elsholtz–Roth 1994–96
  (10⁹, 10¹⁰, 1.6·10¹¹), Kotsireas 1999 (10¹⁰), Swett 1999 (10¹⁴),
  Bello-Hernández–Benito–Fernández 2012 (2·10¹⁴), Salez 2014 (10¹⁷).
  The Wikipedia article as cached in this run still prints 10^17 (draft of
  2025-06); the 10^18 bound supersedes it per the 2025 paper and the Erdős
  problems database.

**Evidence class:** sourced (abstracts + Table 1 + database entry). These are
empirical verification bounds, not theorems.

---

## (c) Structure of a minimal counterexample

**Composite reduction (sourced).** If `4/n = 1/x+1/y+1/z` then for any `m`,
`4/(mn) = 1/(mx)+1/(my)+1/(mz)` (Wikipedia; Elsholtz–Tao §1: "Since we
clearly have f(nm) ≥ f(n) for any n,m ∈ ℕ, we see that to prove the
Erdős-Straus conjecture it suffices to do so when n is equal to a prime p").
Contrapositive: any counterexample `mn` yields the smaller counterexample
`n`; hence a **minimal counterexample is prime**.

**Congruence structure (sourced + derived).** A minimal counterexample `p`
is an odd prime; `p = 2, 3, 5, 7` have explicit expansions, and the five
families and the greedy algorithm handle every other residue except the six
classes mod 840 (see (a); also Wikipedia: "the greedy algorithm finds a
solution in three or fewer terms whenever n is not 1 or 17 mod 24, and the
17 mod 24 case is covered by the 2 mod 3 relation, so the only values of n
for which these two methods do not find expansions in three or fewer terms
are those congruent to 1 mod 24"). Therefore a minimal counterexample must
satisfy

```
p prime,  p ≡ r (mod 840),  r ∈ {1, 121, 169, 289, 361, 529};
equivalently p ≡ 1 (mod 24), p ≡ 1 or 4 (mod 5), p ≡ 1, 2, or 4 (mod 7).
```

**Solution-type structure (sourced).** For an odd prime `p`, at least one of
`x,y,z` is divisible by `p` and not all three are (else RHS ≤ 3/p); hence
every solution is Type I or Type II and `f(p) = 3f_I(p) + 3f_II(p)`
(Elsholtz–Tao §1). Additionally (Elsholtz–Tao): the largest denominator of a
solution for prime `p` is always divisible by `p` (Remark 2.8, "this
observation also appears in [Elsholtz 2001]"); and for `m > 3`, `p` a prime
not dividing `m`, **no denominator is divisible by `p²`** (Proposition 2.10
in the journal PDF / 2.11 in the arXiv v6). So a minimal counterexample `p`
is a prime in one of the six classes at which `f_I(p) = f_II(p) = 0`, i.e.
there is no Type I solution `(abdp, acd, bcd)` and no Type II solution
`(abd, acdp, bcdp)` with `abcd` (resp. `abd`) coprime to `p` — the two
parameterisations of Elsholtz–Tao Propositions 2.1/2.5 (Mordell book form:
`4/p = 1/(abd) + 1/(acd) + 1/(bcdp)` and `4/p = 1/(abd) + 1/(acdp) +
1/(bcdp)`).

---

## (d) Why the six open classes resist the standard identity shapes

**Standard identity shapes.** The "standard shapes" are polynomial identities
that solve a primitive residue class `n ≡ r (mod q)` for all large `n` in the
class — the Mordell family list in (a), and their classification: Elsholtz–Tao
Proposition 1.9 shows that every Type-I-solvable / Type-II-solvable primitive
class is a subset of one of four / three families, each of the form
`{n ≡ −f mod 4ad}` with `f | 4a²d + 1`, `{n ≡ −1/e mod 4ab}` with
`e | a+b`, `{n ≡ −c/a mod f}`, etc. (arXiv:1107.1010 §10; Salez
[Sa14] Prop. 3 gives the equivalent complete set of 7 modular equations for
linear polynomials). Every primitive class solvable by polynomials is Type I
or Type II solvable (Elsholtz–Tao §10: for large `p`, a polynomial value
`P_i(p)` is divisible by `p` iff `P_i` has no constant term; one or two of
the three have no constant term, never all three).

**The obstruction (exact statement, sourced).**

1. **Schinzel's non-residue criterion** (Salez [Sa14] Proposition 2,
   "Schinzel's Theorem"): *Let `a > 0`, `(a,b) = 1`. If `4/(at+b)` is
   3-Egyptian (as a polynomial identity), then `b` is a quadratic non-residue
   modulo `a`.* Each covered class in the classical list is a
   quadratic-nonresidue class at its modulus: 2 non-residue mod 3, 3 mod 4,
   {2,3} mod 5, {3,5,6} mod 7, 5 mod 8. The six open `r` are quadratic
   residues **at every one of these moduli** (`r ≡ 1 mod 3`, `mod 4`, `mod 8`,
   `≡ 1,4 mod 5`, `≡ 1,2,4 mod 7`), so no linear-family identity can cover
   them — this is the residue-level reason the first-level families stop at
   `R₂ = {1,121,169,289,361,529}` (Salez §4.1, "the set of the residues [that
   pass through] ... It was the choice made by Swett").

2. **Vanishing of Type I/II at odd squares** (Elsholtz–Tao Proposition 1.6,
   "Vanishing", arXiv:1107.1010): *For any odd perfect square `n`,
   `f_I(n) = f_II(n) = 0`.* This "essentially dates back to Schinzel (see
   [Guy 1994, Mordell 1969, Schinzel 2000]) and Yamamoto (1965) and is an
   easy application of quadratic reciprocity"; the proof is in Elsholtz–Tao
   §4 (Type I case: `ne + 1 ≡ 0 mod q`, Jacobi symbol manipulation forces a
   contradiction; Type II is identical).

3. **The six classes contain infinitely many odd perfect squares (derived):
   ** for each `r = s² mod 840` with `s ∈ {1,11,13,17,19,23}`, the numbers
   `n = (s + 840k)²` are odd perfect squares and `n ≡ s² ≡ r (mod 840)`. So
   any polynomial identity solving the class `r mod 840` would produce a
   solution at infinitely many odd squares — and since the identity is Type I
   or Type II solvable, those solutions would be Type I or Type II, directly
   contradicting Proposition 1.6.

4. **Elsholtz–Tao state the conclusion** (§10): "any primitive residue class
   n = r mod 840 is solvable by polynomials unless r is a perfect square. On
   the other hand, it is also known ... that a primitive congruence class
   n = r mod q which is a perfect square, cannot be solved by polynomials
   (this also follows from Proposition 1.6)." And in the discussion of
   Prop. 1.6: showing `f_I(p)` or `f_II(p)` non-zero "can only use methods
   that must necessarily fail when p is replaced by an odd square such as p²,
   which already rules out many strategies (e.g. a finite set of covering
   congruence strategies, or the circle method)."

**Bottom line for (d):** the six classes resist the standard shapes *because*
they are exactly the square classes mod 840, and the standard shapes are
Type-I/Type-II polynomial identities, which by Schinzel's criterion require a
quadratic non-residue at the modulus, and by Prop. 1.6 must vanish at odd
squares — while each of the six classes contains infinitely many odd squares.
This is the obstruction any ansatz search must engage with, per
`research/REQUESTS.md` request `exact-statement-from-b7df`.

---

## Claims

```claim
id: mordell-six-open-classes-840
statement: 4/n = 1/x+1/y+1/z has a positive-integer solution for every n not congruent to one of 1, 121, 169, 289, 361, 529 modulo 840; these six residue classes are the only classes mod 840 not settled by the classical polynomial identity families (Mordell 1967).
hypotheses: n >= 2 integer; solution = three positive integers
holds-here: yes
status: sourced (Mordell 1967 pp. 287-290, cited by Wikipedia and erdosproblems.com #242; Elsholtz-Tao arXiv:1107.1010 sec.10: "any primitive residue class n = r mod 840 is solvable by polynomials unless r is a perfect square")
bearing: the six open classes are the target set; every ansatz identity must cover n ≡ r (mod 840) for some r in this set or it rediscovers known coverage
anchor: research/notes/es-structure.md (a), https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Straus_conjecture, https://www.erdosproblems.com/242, https://arxiv.org/abs/1107.1010
answers: exact-statement-from-b7df
```

```claim
id: six-classes-are-square-residues-840
statement: The six open classes are exactly {r mod 840 : r odd, gcd(r,840)=1, r a square mod 840} = {1², 11², 13², 17², 19², 23²} mod 840 = {1, 121, 169, 289, 361, 529}; equivalently the residues r with r ≡ 1 (mod 24), r ≡ 1 or 4 (mod 5), r ≡ 1, 2 or 4 (mod 7). Hand CRT of the five families' avoidance conditions reproduces Salez's published R1 = {1,49} mod 120 and R2 = {1,121,169,289,361,529} mod 840.
hypotheses: residue classes modulo 840 containing infinitely many primes (gcd(r,840)=1)
holds-here: yes
status: derived (hand CRT, exact arithmetic, cross-checked against Wikipedia's six-residue list and Salez arXiv:1406.6307 sec.4.1 tables R1, R2); mechanical script written but not executed this run (code/es_structure/verify_es_structure.py)
bearing: identifies the open set as the square classes; combined with Prop. 1.6 of Elsholtz-Tao this is the reason the six resist identity shapes
anchor: research/notes/es-structure.md (a), https://arxiv.org/abs/1406.6307
```

```claim
id: schinzel-nonresidue-criterion
statement: (Schinzel, as Proposition 2 of Salez) If 4/(at+b) is 3-Egyptian for a > 0, (a,b) = 1, then b is a quadratic non-residue modulo a. Every family in the classical mod-840 list covers a quadratic-nonresidue class at its modulus; the six open residues are quadratic residues modulo every divisor 3, 4, 5, 7, 8, so no linear-family identity can cover any of them.
hypotheses: polynomial identity (3-Egyptian) for the linear polynomial at+b; (a,b)=1
holds-here: yes
status: sourced (Salez arXiv:1406.6307 Proposition 2; the nonresidue list mod 3,4,5,7,8 is elementary and recorded in Wikipedia's Mordell-family table)
bearing: the residue-level reason the first-level families stop at R2, and part of why the six classes need a different shape
anchor: research/notes/es-structure.md (d), https://arxiv.org/abs/1406.6307
```

```claim
id: elt-prop16-vanishing-odd-squares
statement: For every odd perfect square n, the number of Type I solutions and the number of Type II solutions to 4/n = 1/x+1/y+1/z are both zero: f_I(n) = f_II(n) = 0 (Type I: n|x, gcd(n,y)=gcd(n,z)=1; Type II: n|y,z, gcd(n,x)=1). Proof by quadratic reciprocity (Section 4); observation dates back to Schinzel and Yamamoto.
hypotheses: n an odd perfect square, n = 1 mod 8
holds-here: yes
status: sourced with proof in source (Elsholtz-Tao arXiv:1107.1010 Proposition 1.6 and Section 4); numeric spot-check over odd squares n = 9..169 in a finite box x,y,z <= 6n is consistent but is NOT a proof (script not executed by this role)
bearing: the core obstruction: any standard (polynomial Type I/II) method that proves existence for primes must fail on odd squares, so a finite covering-system strategy is impossible (1 is a square mod every q)
anchor: research/notes/es-structure.md (d), https://arxiv.org/abs/1107.1010
```

```claim
id: six-classes-contain-odd-squares
statement: Each of the six open classes mod 840 contains infinitely many odd perfect squares: for r = s^2 mod 840 with s in {1,11,13,17,19,23}, n = (s + 840k)^2 is an odd perfect square congruent to r (mod 840). E.g. 841 = 29^2 in class 1, 121 = 11^2 in class 121, 169 = 13^2, 289 = 17^2, 361 = 19^2, 529 = 23^2.
hypotheses: k >= 0
holds-here: yes
status: derived (elementary; s^2 ≡ r and (s+840k)^2 ≡ s^2 mod 840), consistent with witnesses in code/out/witnesses.json
bearing: bridges (a) and (d): the six classes are non-solvable by polynomials precisely because they contain odd squares where Prop. 1.6 kills Type I/II
anchor: research/notes/es-structure.md (c,d)
```

```claim
id: minimal-counterexample-prime-in-six-classes
statement: A minimal counterexample to the Erdos-Straus conjecture, if one exists, is a prime p with p ≡ r (mod 840) for some r in {1,121,169,289,361,529}; equivalently p ≡ 1 (mod 24), p ≡ 1 or 4 (mod 5), p ≡ 1, 2 or 4 (mod 7). Any solution for such a prime is Type I or Type II (f(p) = 3f_I(p)+3f_II(p)); the largest denominator is divisible by p; and no denominator is divisible by p^2 (m = 4 > 3).
hypotheses: p prime; composite reduction f(nm) >= f(n)
holds-here: yes
status: sourced (composite reduction: Wikipedia, Elsholtz-Tao sec.1; congruence structure: Mordell/Wikipedia as in claim mordell-six-open-classes-840; Type I/II and largest-denominator: Elsholtz-Tao sec.1 and Remark 2.8; p^2-free denominators: Elsholtz-Tao Prop. 2.10/2.11)
bearing: defines the exact search target for oracle/falsification and for any new family: new identities must fire on primes in the six classes
anchor: research/notes/es-structure.md (c), https://arxiv.org/abs/1107.1010
```

```claim
id: verification-bounds
statement: The Erdos-Straus conjecture has been verified by exhaustive search for all n <= 10^14 (Swett 1999), 2*10^14 (Bello-Hernandez, Benito, Fernandez 2012), 10^17 (Salez 2014, seven-modular-equation sieve), and 10^18 (Mihnea & Dumitru 2025, extension of Salez's modular-filter method). Older checks: Oblath 106,128 (1948/9), Terzi 10^8 (1971), Kotsireas 10^10 (1999), per the Elsholtz-Tao Table 1.
hypotheses: none beyond the published computations being correct
holds-here: yes
status: sourced (Salez arXiv:1406.6307 abstract and sec.4; Elsholtz-Tao arXiv:1107.1010 Table 1; Mihnea-Dumitru arXiv:2509.00128; erdosproblems.com #242 "verified for all n <= 10^18 [MiDu25]"; Wikipedia as cached in this run still says 10^17)
bearing: any oracle or new-family verification only needs to target n beyond 10^18 if it wants to extend the numerical record; identities are the only way past the bound
anchor: research/notes/es-structure.md (b), https://arxiv.org/abs/1406.6307, https://arxiv.org/abs/2509.00128, https://www.erdosproblems.com/242
```

---

## Sources

**Used**

1. Elsholtz, C.; Tao, T. *Counting the number of solutions to the
   Erdős–Straus equation on unit fractions*. J. Austral. Math. Soc. 94 (2013)
   50–105. arXiv:1107.1010 (final v6). Full text in this run:
   `research/sources/pomerance-erdos-straus.full.md` (ar5iv HTML) and
   `research/sources/elsholtz-tao-counting.full.md` (journal PDF). Establishes
   Type I/II classification, Prop. 1.6 (vanishing at odd squares), Prop. 1.9
   (complete list of polynomial-solvable classes), Prop. 2.10/2.11 (no p² in a
   denominator for m > 3), Remark 2.8 (largest denominator divisible by p),
   Table 1 (verification history), §10 ("solvable by polynomials unless r is
   a perfect square").
2. Salez, S. E. *The Erdős–Straus conjecture: new modular equations and
   checking up to N = 10^17*. arXiv:1406.6307 (2014). Full text in this run:
   `research/sources/salez-seven-modular-equations.full.md`. Establishes
   Prop. 2 (Schinzel's non-residue theorem), Prop. 3 + Cor. 1 (complete set
   of 7 modular equations), §4.1 (`R₁ = {1,49}` mod 120, `R₂ =
   {1,121,169,289,361,529}` mod 840), §4.2–4.3 (certified non-squares below
   10^17; squares checked separately).
3. Wikipedia, *Erdős–Straus conjecture* (draft cached 2025). Full text:
   `research/sources/wikipedia-erdos-straus.full.md`. Establishes the Mordell
   family list, the six-residue open set, smallest uncovered prime 1009,
   greedy-algorithm residue analysis (1 mod 24), composite reduction,
   verification to 10^17.
4. Bloom, T. F., *Erdős Problem #242*. https://www.erdosproblems.com/242 .
   Full text: `research/sources/erdos-problems-242.full.md`. Establishes
   Mordell's six classes, Terzi's 198 classes mod 120120, Vaughan's bound,
   the 10^18 verification ([MiDu25]), the BlEl22 equivalent formulation.
5. Mihnea, S.; Dumitru, C. *Further verification and empirical evidence for
   the Erdős–Straus conjecture*. arXiv:2509.00128 (2025). Extends Salez's
   filter method to 10^18 (S₂₉, G₈ = 25,878,772,920, 2,101,514 residual
   classes).
6. Operator's earlier exact computation (this run), `code/out/verify_elementary_reductions.md`:
   the naive `n≡3 mod 4` identity is wrong (solves 3/n), the corrected form
   `x=(n+1)/4, y=n(n+1)/4+1, z=y(y−1)` is verified for n=4k+3, k=0..4999.
   Used in (a)'s table.
7. Elsholtz, C. *Sums of k unit fractions*. Trans. AMS 353 (2001) 3209–3227:
   cited by Elsholtz–Tao Remark 2.8 as the origin of the
   largest-denominator observation (context only).

**Rejected or not relied on**

- arXiv:2502.20935 (2025, "Partial resolution of the Erdős–Straus, Sierpiński
  ... conjectures using new analytical formulas"): claims a partial resolution
  via a conjectural perfect-square condition; the condition is itself a
  conjecture, and the paper's claims do not add a theorem about the open
  classes that either Wikipedia or Elsholtz–Tao already state more precisely.
  Rejected as a source for (a)–(d).
- J-STAGE / Suzuki 2025 (constructive algorithm, "92% success for massive
  integers"): empirical algorithmic claim without a proved covering; no
  structural statement about the six classes; rejected.
- Bright & Loughran (arXiv:1908.02526), no Brauer–Manin obstruction on
  Erdős–Straus surfaces: relevant background, present in this run's library
  (`research/sources/bright-loughran-brauer-manin.full.md`), but it does not
  bear on exactly which residue classes are open or why; not relied on here.
- Search-hit claims of a complete proof (e.g. news/blog items surfaced by
  search): none cite a peer-reviewed theorem; ignored.

## What would falsify the picture

A published or computable explicit type-I or type-II polynomial identity
covering any of `n ≡ 1, 121, 169, 289, 361, 529 (mod 840)` — i.e. a
polynomial `(P1(n), P2(n), P3(n))` with positive integer values on the class
and `4/n = 1/P1 + 1/P2 + 1/P3` — directly contradicts Elsholtz–Tao Prop. 1.6
(its square members would give Type I/II solutions at odd squares). This is
the falsifier recorded in `research/REQUESTS.md`
(`exact-statement-from-b7df`), now answered by this note. A *non*-standard
identity shape (not reducible to Type I/II polynomial families, e.g. identities
with denominators depending on a further parameter outside the Elsholtz–Tao
Prop. 1.9 families) is not excluded by anything above — that is the only
opening a new-family search has.

## Verification status of this note

The residue-level claims (a) and the square-class identification were
cross-checked **by hand CRT against Salez's published `R₁ = {1,49} (mod 120)`
and `R₂ = {1,121,169,289,361,529} (mod 840)`** (arXiv:1406.6307 §4.1) and
against Wikipedia's six-residue list; the two published lists and the hand CRT
agree. A mechanical re-check was written (`code/es_structure/verify_es_structure.py`)
but **not executed** in this role (no shell available), so its output file does
not exist; the claims whose status says "derived" rest on the hand CRT plus the
published cross-checks, and the claims whose status says "sourced" rest on the
primary sources cited. Nothing in this note is asserted on a run's computation
alone.