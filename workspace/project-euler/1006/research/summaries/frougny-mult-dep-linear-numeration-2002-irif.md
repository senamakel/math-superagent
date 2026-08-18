# Frougny, "On multiplicatively dependent linear numeration systems, and periodic points" (2002)

**Source:** https://www.irif.fr/~cf/publications/lucas.pdf (Ch. Frougny, in
Actes / LIAFA). Full text: `[[frougny-mult-dep-linear-numeration-2002-irif.full]]`.

## What it establishes

**Set-up.** Two linear numeration systems whose characteristic polynomials are
the minimal polynomials of two Pisot numbers β, γ. The base question: when is
integer conversion between them computable by a finite automaton?

**Theorems (precise statements).**
- **Theorem 1:** If P is the minimal polynomial of a Pisot number of degree m,
  and U, V are two integer sequences with common characteristic polynomial P
  and different initial conditions, then conversion from a V-representation of
  a positive integer to the normal U-representation is computable by a finite
  automaton (single Pisot base, different initial vectors).
- **Theorem 2:** Let β and γ be multiplicatively dependent Pisot numbers, and
  U, V linear sequences with characteristic polynomial equal to the minimal
  polynomial of β resp. γ. Then conversion from the V-numeration system to the
  U-numeration system is computable by a finite automaton; **Corollary 1:** a
  set that is U-recognizable is then V-recognizable as well.
- The converse direction is the *Cobham–Frougny* restriction: two linear
  numeration systems over multiplicatively **independent** bases admit no such
  finite-automaton conversion.

**Application (second half).** For a Parry number β with beta-expansion
d_β(1) = t_1···t_N, defines v_n = trace(β^n) and the "periodic point count"
sequence r_n = v_n − p·[p | n]; shows r_n is exactly realised by the sofic
beta-shift and is linearly recurrent (Props 4–8).

## Hypotheses and whether they hold here

- β, γ Pisot with multiplicatively dependent/independent bases; sequences with
  common recurrence. This is the standard β-numeration setting.
- PE1006's two bases: **10 and φ = (1+√5)/2**. φ is a Pisot number; 10 = 10^1,
  φ is not a rational power of 10 (10^k = φ^m would force φ algebraic of small
  degree — impossible), so 10 and φ are **multiplicatively independent**.

## Bearing on PE1006 (important negative)

This is the **Cobham obstruction**, recorded as claim
`cobham-bes-frougny-multiplicatively-independent-conversion`: because 10 and φ
are multiplicatively independent, **no finite automaton converts between the
Fibonacci (φ-)numeration of positions and decimal digit weights** — i.e. the
"Zeckendorf digit-DP over a finite automaton in O(log k)" route
(`pe1006-zeckendorf-automatic-digit-dp`, approaches/) cannot be made
automaton-finite. The run's committed O(log) universal-Euclidean floor-sum
monoid is NOT an automaton conversion (it is exact integer arithmetic in one
base), so it does not fall to this obstruction. The claim is the reason that
particular approach candidate was recorded as refuted/infeasible at full size.

Verdict: **supplies the negative result** (why the digit-DP over a *finite*
automaton route fails); the O(log) monoid does not depend on conversion
automata at all.

```claim
id: cobham-bes-frougny-multiplicatively-independent-conversion
statement: Two linear numeration systems (over Pisot bases) are mutually
recognisable / convertible by finite automata only if their bases are
multiplicatively dependent. In particular, since 10 and phi = (1+sqrt5)/2 are
multiplicatively independent, no finite automaton converts between the
Fibonacci (phi-)numeration of positions and the decimal (base-10) digit
weights used to read a length-k window as a decimal number.
hypotheses: bases are Pisot; standard beta-numeration recognisability.
holds-here: yes — 10 and phi are multiplicatively independent.
status: sourced
bearing: rules out the finite-automaton Zeckendorf digit-DP route to Psi(k)
(approaches/pe1006-zeckendorf-automatic-digit-dp) at full size; the committed
universal-Euclidean monoid does exact integer arithmetic in one base and is
not affected.
anchor: research/sources/frougny-mult-dep-linear-numeration-2002-irif.full.md
(Theorem 2, Corollary 1 and the independence restriction stated in the intro)
answers: (the automaton-conversion question, negatively)
```