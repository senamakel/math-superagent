# Morgenstern, "3x3 Magic Square of Squares Properties", July 2015

[[morgenstern-properties-3x3-square-of-squares-2007]]

Elementary number theory results on the entries of a primitive 3×3 MSS, proved only with
modular arithmetic and quadratic residues. This is a **refereed-quality elementary sieve**
source, relevant because the run has already ruled out "pure modular sieves cannot prove
non-existence" — these results are congruences that mostly restrict *search*, they do not by
themselves eliminate the problem.

## Established statements

**AP background.** A three-square AP `A²≤C²≤B²` satisfies `A²+B²=2C²`; every AP is a scaled
primitive AP; a primitive AP `(2mn−m²+n², m²+n², 2mn+m²−n²)` with `m,n` coprime, one even
one odd. So the middle term `m²+n²` consists only of `1 mod 4` primes (Thm 2), and an outer
term `2r²−s²` only of `1,7 mod 8` primes (Thm 3).

**Primitive MSS restrictions (all proved, elementary):**
- Thm 4: in a primitive MSS all nine entries are **odd** (centre parity propagates through the
  four centre APs).
- Thm 5: central entry consists only of `1 mod 4` primes (must not carry a `3 mod 4` factor in
  its scaling).
- Thm 6: **no entry can have a `3 mod 8` prime factor**.
- Thm 7: no middle-side entry can have a `5 mod 8` prime factor.
- Thm 8/9: if a corner has a `3 mod 4` (resp. `5 mod 8`) factor, a couple of other entries do too.
- Thm 10: all entries are `1 mod 3`.

**Step-value restrictions (x,y,z formulation, `z=py`):** `p` can't be 0,1,2,3,4 (that would
force 5/6/7/9 squares in a 3-term AP, impossible), can't be a `4k+3` prime (Thm 18, by infinite
descent on Pythagorean triples), nor one less / one more than a `4k+3` prime (Thm 19, 20).

**Duplicate-entry classification (Thm 12).** In the x,y,z form, duplicated entries occur
exactly when `yz=0`. For a MSS (entries squares), there are 3 inequivalent duplication cases,
which force 5, 7, or 3 squares in AP; the `z=0` case gives the smallest non-trivial
{1,25,49}-family.

**Conjunction with Zimmermann–Loria:** all entries `1 mod 3` (Thm 10) plus all odd
(Thm 4) recovers Zimmermann–Loria's "entries ≡ 1 mod 24 and magic sum ≡ 3 mod 72".

## Implications for this run

- These are exact, proved congruence/parity restrictions. They **sharpen** the modular sieve
  but do not prove non-existence (Bremner's extension-field MSS satisfy the same entry
  congruences where defined). They are the correct sieve to run *against the witness set* —
  Bremner's 7-square witness must pass every one of Thm 4–10 (it does, being primitive? —
  check: centre 425 is `1 mod 4`, all entries odd). A sieve lemma that contradicts any of
  Thm 4–10 for a witness is false.
- The step-value theorem (p can't be 4k+3 prime or ±1) is a genuine structural constraint on
  the four centre-AP differences `u,v,u+v,u−v`, and is the elementary anchor for the
  run's four-AP obstruction.

```claim
id: primitive-mss-entry-congruences
statement: In a primitive 3x3 MSS all nine entries are odd and ≡1 mod 3; no entry has a 3 mod 8
  prime factor; no middle-side entry has a 5 mod 8 factor; central entry ≡1 mod 4 only; and the
  step ratio z=py excludes p ∈ {0,1,2,3,4} ∪ {4k+3 prime or ±1}.
hypotheses: primitive (gcd of all entries = 1); entries distinct squares
holds-here: yes (the run's target MSS is primitive after removing a common square factor)
status: proved
bearing: exact sieve restrictions for search; must be survived by every near-miss witness
anchor: research/sources/morgenstern-properties-3x3-square-of-squares-2007.full.md
```
