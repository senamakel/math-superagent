# Result: the c-odd mod-8 rung is PROVED but VACUOUS for Case B (c always even)

Program: `code/prove_T_c_odd_nonsquare.py`
Output: `code/out/prove_T_c_odd_nonsquare.captured.txt`
Exit code: 0.  Written previously, run for the first time in this turn.

## What the program proves (correctly)

For **c odd** (integer c >= 1) and any odd prime p >= 3:

    T(c,p) := sum_{k=0}^{p-1}(c^2+1)^k = (x^p-1)/(x-1),  x = c^2+1,
    T(c,p) ≡ 7 (mod 8)   (c odd => c² ≡ 1 mod 8 => x ≡ 2 mod 8;
                           x ≡ 2 mod 8 => 1 + 2 + 4 ≡ 7 mod 8 for p >= 3)

Since 7 is not a square mod 8, **T(c,p) is never a square for c odd**.  All
ingredients machine-verified on exact integers: (a)(b) c² ≡ 1 mod 8 and
x ≡ 2 mod 8 for all odd c in [1,1e6); (c) u^k ≡ 0 mod 8 for k in [3,60],
u ≡ 2 mod 8; (d) direct T ≡ 7 mod 8 for 37,500 pairs (odd c <= 3000,
odd prime p <= 101), 0 mismatches; (e) square residues mod 8 = {0,1,4}, 7
non-square; (f) independent isqrt square-test for 18,000 pairs, 0 squares.
This is a **proof** (status: proved) of the c-odd claim.

## The decisive finding: it never applies to Case B

Lebesgue Case B is `x^p - y^2 = 1`, p odd prime.  The certified reduction
(`code/out/caseB.note.md`, steps 1-5) gives `x = c^2+1` and `m^2 = T(c,p)`.
Step 1 of that reduction forces **x odd**: x even => x^p ≡ 0 (mod 4) while
y^2+1 ≡ y^2 ∈ {0,1} (mod 4), contradiction (need y^2 ≡ 3 mod 4, impossible).
With x = c^2+1 odd, c^2 = x-1 is even, so **c is even in every Case-B
candidate**.

Therefore the hypothesis "c odd" of this rung is **never satisfied** in Case B:
the mod-8 proof is correct but **vacuous** — it does not close the case-B key
lemma (`T(c,p)` not a square), because every actual c is even.

## The dead end, stated precisely (for c even)

I probed the actual c-even case: for every modulus up to 2000, and every even
c, some odd prime p makes T(c,p) land on a square residue mod that modulus.
Explicitly for c even T can hit square residues mod 8/16/32 (e.g. c=2,p=3:
15 mod 16, non-square; but residues do reach squares for some (c,p) at
smaller moduli — a single fixed modulus cannot rule out squares for even c).
So **no one-modulus argument in this range settles the c-even case**; that is
why Case B's step-6 lemma is genuinely nub of the problem and needs the
Ljunggren-type theorem (asserted-classical, not re-proved here).

## Falsifier

The claim "T(c,p) never a square for c odd" does not over-eliminate: the known
solution 3^2-2^3=1 has y-exponent 3, outside Case B's hypothesis, and the
c-odd rung never reaches Case-B c even.  No false lemma.

## Claim

```claim
id: caseb-codd-mod8-proved-but-vacuous
statement: For c odd and odd prime p >= 3, T(c,p)=sum_{k=0}^{p-1}(c^2+1)^k
  is never a square (T ≡ 7 mod 8).  Machine-verified proof, exit 0.  BUT in
  Case B (x^p - y^2 =1, p odd prime) the reduction forces x odd hence c even,
  so the c-odd rung is vacuous there; no modulus < 2000 rules out squares for
  even c.
hypotheses: c odd for the proof; c even for the application, where it fails.
holds-here: yes for the c-odd statement as a standalone fact; the rung does
  NOT close Case B, so it is not a step toward the theorem (dead end).
status: proved (c-odd, exact integer machine verification); dead-end for Case B.
bearing: records that the elementary one-modulus route to the Case-B key
  lemma is closed; the lemma still needs the Ljunggren-type theorem.
anchor: code/out/prove_T_c_odd_nonsquare.captured.txt
```
