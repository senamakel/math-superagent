# exp2-a-even — machine verification of the even-x case of x^2 - y^q = 1

Program: `code/exp2_even_proof.py`. Output: `code/out/exp2_even_proof.captured.txt`.

## Lemma

```
x^2 - y^q = 1  with x,y > 0, x EVEN (x >= 2), q an ODD PRIME
=>  NO SOLUTION
```

## The three-step elementary proof, and how each step was machine-checked

All arithmetic exact integers; no floats, no logarithms, no `math.pow`.

**Step 1 — gcd.** `x` even ⇒ `x-1`, `x+1` odd, and `gcd(x-1,x+1) | 2`; since
both are odd the gcd is 1. Checked: (i) `gcd(x-1,x+1)=1` for every even
`x <= 2×10^6`; (ii) the stronger exact identity `gcd(x-1,x+1) == gcd(2,x-1)`
(= 1 since x-1 is odd) for every even `x <= 2×10^6`.

**Step 2 — factorisation into q-th powers.** `(x-1)(x+1) = y^q` with the two
factors coprime and positive, so each is a q-th power: `x-1 = a^q`,
`x+1 = b^q`, with `b > a >= 1`. Checked: wherever `x^2-1` is a q-th power for
even `x <= 200,000` and odd prime `q <= 37`, the integer q-th roots a, b exist
and satisfy `x-1=a^q`, `x+1=b^q` with `gcd=1` and `1<=a<b`. (There were 0 such
cases in that window — see the falsifier note below — so the structural
statement is verified as: whenever the situation occurs, the structure holds;
the sweep never presents a counterexample.)

**Step 3 — inequality.** `b^q - a^q = (x+1)-(x-1) = 2`, but
`b^q - a^q >= (a+1)^q - a^q >= 2^q - 1 >= 7 > 2` for `q >= 3`,
contradicting `= 2`. Checked: (a) the exact minimum of `b^q - a^q` over
`1 <= a < b <= 200` is attained at `(a,b)=(1,2)` and equals `2^q-1`, for each
odd prime q in {3,5,7,11,13,17,19,23,29,31}; (b) `(a+1)^q - a^q` is strictly
increasing in a over `[1,200]`; (c) `2^q - 1 >= 7 > 2`. Independently rechecked
at the larger window `a <= 5000` for q in {3,5,7}: still minimum `2^q-1` at
a=1, and monotone, hence `b^q-a^q >= 7 > 2` for all a>=1.

## Brute-force oracle (part c)

Over even `x in [2, 10^7]` and odd prime `q <= 30`, `x^2 - y^q = 1` has
**zero solutions**. Runtime 53.7 s, N (x bound) reached = 10^7, q bound 30.
Exact q-th-power detection of `x^2-1` via integer bisection; verified by a
positive control that genuine `b^q` are detected and `b^q+1` rejected, and
that the known solution's witness `3^2-1 = 8 = 2^3` is detected (so the
"zero found" verdict is meaningful, not an always-false detector).

## Falsifier discipline

- The lemma covers only **even x**. The known solution of the full
  `x^p-y^q=1` is `(3,2,2,3)`, whose x-exponent part in this case is
  `(x,y,q) = (3,2,3)` with **x = 3 odd** — it is excluded by hypothesis and
  is **not** claimed to be a solution or non-solution of this lemma. The
  program asserts `known_excluded = True` (x odd) and that the identity
  `3^2-1 == 2^3` holds (so the witness the oracle detects is exactly this one).
- The lemma is silent about odd x; nothing here excludes or includes the known
  solution. Good.
- Independent cross-check vs. the pre-existing two-route search
  (`code/out/exp2.md`): the only solution of `x^2-y^q=1` at N=1e7 in any base
  is `(3,2,3)`, and it has odd x; so the even-x sweep finding nothing is
  consistent. A separate re-implementation (different root routine) confirmed
  zero even-x solutions for `x <= 3×10^6`.

## What is proved versus checked

- **Proved by the elementary argument** (steps 1–3 above are a complete proof,
  and the `b^q-a^q >= 7 > 2` inequality is an exact arithmetic fact verified at
  the minimiser and by monotonicity): the lemma holds for **all** even `x` and
  **all** odd primes `q`.
- **Checked (numerical, finite box):** the gcd identity on `x<=2×10^6`; the
  factor-structure-on-occurrence over the small window; the zero-solution
  oracle over even `x<=10^7`, `q<=30`.

The structural factorization step (product of two coprime integers being a
q-th power forcing each factor to be a q-th power) is a standard elementary
fact; it is stated as a proof step here and its hypothesis (coprime factors)
is exactly the gcd=1 the program verified.

```claim
id: exp2-a-even
statement: x^2 - y^q = 1 with x,y > 0, x even (x >= 2), and q an odd prime,
  has NO solution.  Proof: x even => x-1, x+1 odd and coprime (gcd divides 2,
  both odd, so gcd = 1); their product is y^q, so with coprime factors each is
  a q-th power, x-1=a^q, x+1=b^q, b>a>=1; then b^q-a^q=(x+1)-(x-1)=2, but
  b^q-a^q >= (a+1)^q-a^q >= 2^q-1 >= 7 > 2 for q>=3, contradiction.
hypotheses: x,y > 0 integers, x even >= 2, q an odd prime >= 3.  The
  elementary inequality and gcd steps are exact for all such x,q; the finite
  oracle confirms zero even-x solutions on even x<=10^7, odd prime q<=30.
holds-here: TRUE — the lemma is about even x only; the known solution (3,2,3)
  has x=3 odd and is excluded by hypothesis, so nothing is contradicted or
  eliminated.  The gcd identity is verified for all even x<=2*10^6 and the
  b^q-a^q>=7>2 inequality verified at the exact minimiser (a,b)=(1,2) for q
  in {3,5,7,11,13,17,19,23,29,31} plus a=1..5000 monotonicity check.
status: proved-by-elementary-calculation (exact parts); the coprime-factor
  -> q-th-power structural step is a standard proof step, stated here; the
  zero-solution oracle is checked over even x<=10^7, q<=30.
bearing: discharges the open gap exp2-a-even of
  research/backward/exponent-2-in-full.md: the even-x branch of Lebesgue
  Case A (x^2-y^q=1).  The odd-x branch (exp2-a-odd-descent) remains, and
  together they give Case A.
anchor: code/out/exp2_even_proof.note.md
```

## Files

- `code/exp2_even_proof.py` — the verifying program.
- `code/out/exp2_even_proof.captured.txt` — the captured output.
- `code/out/exp2_even_proof.note.md` — this note.
