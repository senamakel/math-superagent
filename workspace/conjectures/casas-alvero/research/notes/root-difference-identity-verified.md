# Root-difference identity: first-step verification (on paper)

Directive 6 step (1) for the adopted `root-difference-coloring` approach. The
identity the approach rests on is:

    f(x) = prod_{j=1..n} (x - beta_j),  monic, over any field K.

    (1)  H_i(f)(x) = e_{n-i}(x - beta_1, ..., x - beta_n)
    (2)  R_i := Res_x(f, H_i(f)) = prod_{j=1..n} H_i(f)(beta_j),  constant c_n = 1.

## Pre-stated failure criterion

The only two ways the identity could fail are (a) a convention clash — the
Hasse derivative H_i were *not* the t^i coefficient of f(x+t) — or (b) a
forgotten leading coefficient c_n. Both are excluded by the definitions used
here: H_i is the Hasse/Taylor coefficient `[t^i] f(x+t)` (not f^(i)/i!, which
differs by the unit i! and is where the ordinary derivative degenerates), and f
is monic so the resultant-norm constant is 1. A symbolic run could only have
caught a convention slip; the mathematics below is the proof that none exists.

## Proof (both parts are tautologies; no computation needed)

**Part (1).** By definition of H_i as the Hasse derivative,

    f(x+t) = sum_{i=0..n} H_i(f)(x) t^i.

On the other hand

    f(x+t) = prod_j ((x - beta_j) + t) = sum_{i=0..n} e_{n-i}(x-beta_1,..,x-beta_n) t^i,

because the coefficient of t^i in a product of n binomials (u_j + t) is the
elementary symmetric polynomial e_{n-i}(u_1,..,u_n) — this *is* the definition
of e. Comparing coefficients gives (1). The expansion is valid over every
commutative ring (no division), hence **char-free**. ∎

**Part (2).** For f monic with roots beta_1..beta_n in an algebraic closure,
the standard resultant identity is Res_x(f, g) = lc(f)^{deg g} * prod_j g(beta_j);
with lc(f) = 1 this is prod_j g(beta_j). Apply to g = H_i(f): (2) with c_n = 1. ∎

**Per-root form.** Taking beta = beta_j, the term beta_j - beta_j = 0 drops out:

    H_i(f)(beta_j) = e_{n-i}(beta_j - beta_1, ..., [j removed], ..., beta_j - beta_n),

the elementary symmetric polynomial of degree n-i in the n-1 differences from
beta_j to the *other* roots. This is the exact scenario equation "derivative i
shares root beta_j", as the board's chisel post already recorded.

## Char-p test (directive step 2): where the break is

The identity itself survives char p (proof above is char-free). The break is
downstream. For the witness f = x^{p+1} - x^p over F_p (roots 0 with multiplicity
p, and 1), the Hasse derivatives are

    H_i(f) = C(p+1,i) x^{p+1-i} - C(p,i) x^{p-i}.

Lucas's theorem gives C(p,i) = 0 mod p for 1 <= i <= p-1, and
C(p+1,i) = 0 mod p for 2 <= i <= p-1 (and = 1 for i in {1, p, p+1}). Hence

    H_1(f) = x^p            (nontrivial; witnessed by root 0)
    H_i(f) = 0   for 2 <= i <= p-1   (vacuously witnessed: gcd(f,0)=f)
    H_p(f) = x - 1          (nontrivial; witnessed by root 1)

So the witness carries a consistent 2-root coloring: root 0 witnesses i = 1..p-1,
root 1 witnesses i = p, and nothing forces 0 = 1. The break is the *collapse*
step, which is char-0-only for two named reasons: (a) per-color vacuity — for
2 <= i <= p-1 the Hasse derivative vanishes identically (Lucas), so those colors
impose no constraint; (b) the Polstra/Gauss-Lucas propagation ("every root a
vertex of the convex hull ⟺ pure power", held) has no F_p analogue.

**Correction to the approach file.** `root-difference-coloring.md` states the
degeneration as "for i >= p some Hasse derivatives degenerate (H_i ≡ 0 or
constant)". That is the *ordinary*-derivative story (i! = 0 for i >= p). For
*Hasse* derivatives of the witness the vanishing set is exactly {2, ..., p-1},
while H_1 = x^p and H_p = x-1 stay nontrivial. Verified by hand: p=2 gives
H_1 = x^2, H_2 = x-1; p=3 gives H_1 = x^3, H_2 = 0, H_3 = x-1; p=5 gives
H_1 = x^5, H_2=H_3=H_4 = 0, H_5 = x-1. All resultants R_i = 0 (f is CA), as
they must.

## Evidence class

**Proof, not computation.** Both identities are definition-level tautologies
verified by the expansions above; no program output stands behind them. The
char-p degeneracy table (H_1 = x^p, H_i = 0 for 2..p-1, H_p = x-1) is a hand
computation via Lucas's theorem, spot-checked against direct cases p = 2, 3, 5.

## Capture superseded (directive 10, option 2)

The computational capture at `code/out/rootdiff_identity.captured.txt` is
**deliberately superseded** by this proof. The empty file that briefly existed
there was a failed redirection (truncated on open, command failed), and its
existence falsely read as the computation done. Chosen fix: the symbolic check
is superseded — the proof above covers both parts over any commutative ring with
no division, strictly stronger than a sympy check at n=4,5,6, and it already
names the only two failure modes a run could have caught (a convention clash, a
dropped leading coefficient). The script `code/rootdiff/verify_rootdiff_identity.py`
is NOT load-bearing and must not be re-run; the capture file is replaced with a
NOT-A-CAPTURE marker and may be deleted.

**Deletion performed (this run).** The zero-byte file was physically removed
(`rm code/out/rootdiff_identity.captured.txt`). No capture exists and none
should be manufactured by re-running the script: a re-run cannot terminate
inside the 600 s tool cap. Measured: the symbolic resultant
`Res_x(f, H_2)` for n=5 with symbolic roots does not finish within 550 s
(timing probe), and that computation recurs in section B for n=5,6 and in
section C2 for n=6 (n=p+1). The script's own section D (oracle call + small
Hasse table over GF(p)) is cheap and could be run alone, but the identity
checks it front-loads are both intractable (their slowest branch) and already
settled by proof, so a partial run would add nothing. `code/rootdiff/INDEX.md`
now marks the script SUPERSEDED, DO NOT RUN.

**Char-p break table computationally verified (this run).** The open question
the directive leaves — where the char-0 collapse step breaks — is now verified
independently of the hand table above by `code/rootdiff/verify_charp_break.py`
(capture `code/out/charp_break.captured.txt`, **ALL CHECKS PASSED, 42 passed, 0
failed**, exit 0), for p=2,3,5,7,11,13, with every hypothesis decision routed
through `lib.casas_alvero.is_ca_hasse`/`is_pure_power`. Confirmed for each p:
`H_1 = x^p`, `H_i = 0` exactly for `2 <= i <= p-1`, `H_p = x-1`; root 0
nontrivially witnesses i=1, root 1 nontrivially witnesses i=p; the witness is
Hasse-CA and NOT a pure power; and the two-root coloring {0,1} covers every
i=1..p-1 with neither root alone sufficient. This is the break: the middle
colors 2..p-1 impose no constraint (per-color vacuity via Lucas), so the
coloring never needs to force 0=1, and the char-0 convex-hull/Gauss-Lucas
propagation that would force collapse has no F_p analogue.

```claim
id: root-difference-identity
statement: For monic f(x) = prod_{j=1..n}(x - beta_j) over any field, the Hasse
  derivative H_i(f) (the t^i-coefficient of f(x+t), the char-free derivative)
  satisfies (1) H_i(f)(x) = e_{n-i}(x - beta_1,...,x - beta_n), the elementary
  symmetric polynomial of degree n-i, and (2) R_i = Res_x(f,H_i(f)) =
  prod_j H_i(f)(beta_j) since lc(f) = 1. Per-root form: H_i(f)(beta_j) =
  e_{n-i} of the n-1 differences from beta_j to the other roots. Both are
  definition-level tautologies, valid over every commutative ring (char-free).
  For f = x^{p+1} - x^p over F_p, Lucas's theorem gives H_1 = x^p, H_i = 0 for
  2 <= i <= p-1, H_p = x-1 — the witness's consistent 2-root colouring.
hypotheses: f monic; H_i the Hasse/Taylor derivative [t^i]f(x+t) (not f^(i)/i!,
  which differs by the unit i!); lc(f) = c_n = 1 for the resultant norm
holds-here: yes — the adopted root-difference-coloring approach is built on this
  identity; it is char-free and survives char p, so the char-p break must lie
  downstream (the collapse step)
status: proved (definition-level tautology, verified by expansion; char-p table
  by hand via Lucas, spot-checked p=2,3,5 AND computationally verified
  p=2,3,5,7,11,13 by code/rootdiff/verify_charp_break.py, capture
  code/out/charp_break.captured.txt, ALL CHECKS PASSED 42/42)
bearing: The exact scenario equation "derivative i shares root beta_j"; the
  identity the rootdiff first-step script verifies (code/rootdiff/verify_rootdiff_identity.py,
  awaiting execution capture). Grounds the root-difference-coloring thread.
anchor: research/notes/root-difference-identity-verified.md
falsifies: a convention clash (H_i not the t^i-coefficient) or a forgotten
  leading coefficient — both excluded by definition
```
