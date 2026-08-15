# Approach: Lucas sequences and the primitive-prime-divisor obstruction

```approach
idea: Recast x^p - y^q = 1 as a pair of Lucas-sequence divisibility statements
       and bring the full strength of the primitive-prime-divisor theorem
       (Zsigmondy's theorem; definitive form Bilu–Hanrot–Voutier for Lucas and
       Lehmer sequences) to bear on them.
mechanism: x^p - 1 = y^q  gives  y^q = (x-1) * Phi_p(x) where Phi_p(x) =
       (x^p-1)/(x-1). The factor Phi_p(x) is the p-th term of the Lucas sequence
       U_n(x+1, x) (companion / Lucas-sequence identity U_n(P,Q) = (a^n - b^n)/(a-b)
       with P = a+b = x+1, Q = ab = x, a = x, b = 1). Likewise y^q + 1 = x^p
       gives x^p = (y+1) * Phi_q(-y) for q odd, and Phi_q(-y) = (y^q+1)/(y+1)
       is the q-th term of the Lehmer/Lucas sequence U_q(y-1, -y) (a = y, b = -1).
       Zsigmondy/BHV then says: for all but an explicitly listed finite set of
       small (n, P, Q), the n-th term U_n has a *primitive* prime divisor — a
       prime r | U_n with r ∤ U_k for all k < n, and r ≡ 1 (mod n). Such a
       primitive divisor r of Phi_p(x) must divide y^q; so r | y, hence
       r^q | y^q = x^p - 1, and by r ≡ 1 (mod p) one forces p | r-1 | y^q - ...
       This is a *different* route to the double-Wieferich-type conditions and
       to congruence obstructions on x, y that the cyclotomic ideal-factorisation
       route derives by class-group arguments — here the same information comes
       from a purely elementary, fully-proved, effective theorem about the
       recurrence U_{n+1} = (x+1) U_n - x U_{n-1}.
status: adopted
precedent: Zsigmondy 1892 (Monatsh. Math. 3, 265-284); Roitman "On Zsigmondy primes" Proc. AMS 125 (1997) https://doi.org/10.1090/s0002-9939-97-03981-6 ; Schinzel "On primitive prime factors of a^n-b^n" Proc. Camb. Phil. Soc. https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/on-primitive-prime-factors-of-anbn/FF4F8CB4D5BEDD2854151670559F36C6 ; Bilu-Hanrot-Voutier "Existence of primitive divisors of Lucas and Lehmer numbers" J. reine angew. Math. 539 (2001), INRIA RR-3792 https://inria.hal.science/inria-00072867/file/RR-3792.pdf ; Voutier "Primitive divisors of Lucas and Lehmer sequences" (I-III), esp. III Proc. Camb. Phil. Soc. 123 (1998) https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/primitive-divisors-of-lucas-and-lehmer-sequences-iii/9E00EE0121300C7E0475721D86D8C530
killed-by: (none — grounded and adopted as a theorem; open question is only whether it buys a NEW condition, not whether the theorem applies)
research-note: The primitive-divisor machinery is fully proved and applies verbatim. For the cyclotomic factor Phi_p(x) = (x^p-1)/(x-1) = U_p(x+1,x), a primitive prime divisor r has ord of x mod r equal to p, so p | r-1 (Roitman Prop./Thm 3: a prime divisor of Phi_n(a) is a Zsigmondy prime iff its order mod the prime is n, hence r ≡ 1 (mod n)). Since y^q = (x-1)·Phi_p(x), r | Phi_p(x) with r ∤ (x-1) forces r | y. The exceptional cases where no primitive divisor exists are an explicit finite list (Voutier: for n > 30,030 every Lucas/Lehmer term has a primitive divisor; BHV: classification for small n); NONE of them can occur for odd prime p >= 3 with x >= 2 (the known solution sits at p=2, the exceptional index, excluded by the odd-prime hypothesis rather than by luck). CLAIM: for odd prime p and x >= 2, Phi_p(x) has a primitive prime divisor r ≡ 1 (mod p); left as a claim to verify symbolically and against the BHV exception list (status: proposed-claim).
first-step: A tool_builder can start today. (1) Symbolic verification (sympy,
       exact integers) of the two Lucas identities Phi_p(x) = U_p(x+1, x) and
       Phi_q(-y) = U_q(y-1, -y), plus the gcd lemma gcd(x-1, Phi_p(x)) =
       gcd(x-1, p), for p, q in {3,5,7,11} and small x, y. (2) Confirm the
       Zsigmondy primitive divisor in the non-exceptional range: for p in
       {3,5,7,11}, x >= 2, exhibit a prime r | Phi_p(x) with r ≡ 1 (mod p) and
       r ∤ (x-1); confirm r ≠ p (oracle calibration only — existence is
       Zsigmondy's theorem, proved, not enumerated). (3) Derive the elementary
       Cassels reformulation p | y ⇔ p | x-1 and q | x ⇔ q | y+1 from the gcd
       lemma, and calibrate at (3,2,2,3): 2 | 3-1 and 3 | 2+1 both hold.
       (4) Implement check_conditions(p,q,x,y) with these conditions and
       compare against the double-Wieferich conditions p^{q-1} ≡ 1 (mod q^2),
       q^{p-1} ≡ 1 (mod p^2), to decide whether the primitive-divisor route
       yields a condition beyond them.
```

## What this buys

The standard route converts `x^p - 1 = y^q` into an ideal relation in
`Z[zeta_p]` and then gets stuck on the class group (the *ideal → element* lift).
The Lucas-sequence route never leaves `Z`. The cyclotomic polynomial
`Phi_p(x)` is literally a Lucas-sequence term, so every prime factor of `Phi_p(x)`
is governed by Zsigmondy's theorem, and the primitive divisors carry a
congruence `r ≡ 1 (mod p)` for free. That congruence is exactly the engine that
produces the "p^2 | ..." / Wieferich-style divisibility conditions — but it is
obtained here from a theorem that is proved, effective, and elementary (a
recurrence), with no class-number hypothesis anywhere.

## The known solution and where it sits

At `3^2 - 2^3 = 1` the two factorisations are:
- `x = 3, p = 2`: `x^p - 1 = 8 = y^q` with `y = 2, q = 3`. Here `p = 2` is
  even, so `Phi_2(x) = x + 1 = 4`, and the Lucas-sequence index is `p = 2` —
  the Zsigmondy exceptional index. The approach must not assume `p` is odd, and
  the exception list of Zsigmondy/BHV has to be checked case by case, with
  `(x, p) = (3, 2)` sitting inside it. This is the falsification oracle: any
  lemma that says "Phi_p(x) has a primitive prime divisor with r ≡ 1 (mod p)
  for all p > 1" is *false* at `p = 2`, because `Phi_2(3) = 4` has only the
  prime 2, and 2 ≢ 1 (mod 2). The honest statement is: **for odd prime p and
  x ≥ 2, Phi_p(x) has a primitive prime divisor r ≡ 1 (mod p), with the finite
  known exceptions** — and `(3,2)` is excluded by the oddness hypothesis, not
  by luck.

## Why it beats the standard alternative here

- The class-group route needs `h^+` (unknown for p ≥ 71) or Stickelberger /
  circular-unit indices; the Lucas route needs only the recurrence and BHV.
- BHV's theorem is *classification-complete*: the exceptional (n, P, Q) triples
  with no primitive prime divisor are an explicit finite list (Bilu–Hanrot–
  Voutier 2001). So "no primitive divisor" is not a black-box open condition —
  it is a checkable finite list.
- The output is a *new necessary condition on x, y, p, q* that can be run
  through `check_conditions`, which is exactly the deliverable ranked third in
  GOAL.md.

## What could kill it

1. Zsigmondy's exceptional list may turn out to cover exactly the (x, p) values
   a hypothetical solution needs, leaving no contradiction — the route would
   then produce conditions but no exclusion (still a partial result).
2. The primitive divisor `r` divides `y`, but controlling `r^q | x^p - 1`
   may give only the already-known Wieferich conditions, not anything new.
3. The Lucas identities could be stated with the wrong P, Q (e.g. swapping
   `x+1`/`x` or sign of Q), which is why the first step is a symbolic check.

## Adopted refinement (synthesis of the grounded route with research findings)

Research grounded the primitive-divisor engine and refuted the other two
candidates on evidence. The decision is to adopt this route, and the synthesis
sharpens it as follows.

The primitive-divisor engine is exactly the *elementary half* of the known
structure of Catalan's equation, and the literature (Roitman, BHV/Voutier)
supplies the one theorem it needs, fully proved and with a complete finite
exception list. Its honest limit is now named precisely: everything it produces
lives in Z and needs no class-group input; what it cannot do is the
ideal-to-element lift in `Z[zeta_p]`, which is where the class group of
`Q(zeta_p)` enters. So this route is the elementary reduction *up to* the
double-Wieferich conditions, and its deliverable (GOAL.md rank 4, "divisibility
conditions re-derived with proofs") is reachable and is exactly what it buys.

Two concrete reformulations it produces, both to be proved in-workspace and
machine-verified:

- `gcd(x-1, Phi_p(x)) = gcd(x-1, p)`, so the two factors of
  `x^p - 1 = (x-1) Phi_p(x)` are coprime except possibly for `p`.
- Consequently `p | y ⇔ p | x-1` and `q | x ⇔ q | y+1`: Cassels'
  `p | y`, `q | x` in purely elementary form. The equivalence is elementary in
  *both* directions given the gcd lemma (`p | x-1 ⇒ p | y` needs no Cassels;
  the reverse is the gcd argument), but it does **not** by itself establish
  `p | y` — it transfers Cassels' content to the more elementary-looking
  `p | x-1`. Status: derived here; standard; needs the sympy check in first-step
  (3) before it is believed. The known solution satisfies it: `2 | 3-1` and
  `3 | 2+1`.

The corrected object from the refuted Jacobian candidate (Catalan curve
`y^q = x^p - 1`, Jacobian with CM by `Q(zeta_p, zeta_q)`, a quotient of the
Fermat Jacobian) is kept live as a *per-instance* tool (a thread), not as a
proof route: Chabauty applies iff `rank(J(Q)) < g`, and that rank bound is the
same class-group obstruction this route avoids. No step of the adopted route
depends on it.

## Cost

Symbolic verification is seconds. The BHV exceptional-list enumeration is a
finite search over an explicit published list (dozens of entries), so it is
bounded and independent of the problem's astronomical bound — this is an
evaluation of a classification, not an enumeration of the answer space.
