# Matveev 2000 — explicit lower bound for a homogeneous rational linear form in logarithms of algebraic numbers (PRIMARY)

Source: E.M. Matveev, "An explicit lower bound for a homogeneous rational
linear form in logarithms of algebraic numbers", Izvestiya RAN Ser. Mat. 62:4
(1998) 81–136; English translation in Izvestiya: Mathematics 62:4 (1998)
723–772. Downloaded the **full English text** from mathnet.ru:
https://www.mathnet.ru/php/getFT.phtml?jrnid=im&paperid=190&what=fullteng&option_lang=eng
Stored at `research/sources/matveev-2000-homogeneous-linear-form.full.md`.
(Note: the same mathnet entry "paperid=190" is the 1998 volume 62 paper; the
follow-up "II" is Izv. Math. 64:6 (2000) 1217–1269 — the run's effective-bound
uses the 1998 theorem, which is the one practitioners cite as Matveev 2000.)

This is the **primary authority for the explicit constants** of the
linear-forms-in-logarithms lower bound that GOAL.md's "effective height bound
with a computed constant (Baker / linear forms in logarithms)" partial result
requires. The library already holds a worked application template
(`research/summaries/matveev-application-linear-forms.md`, Tiebekabe–Diouf
2021) which quoted a Theorem 2.9 (Matveev) without the full constants; this
primary now supplies the constants themselves.

## The theorem (homogeneous rational case, Kummer condition)

Linear form Λ = b1 ln α1 + ⋯ + bn ln αn, n ≥ 2, rational integers bj, bn ≠ 0,
Λ ≠ 0. K an algebraic number field of degree DK over Q embedded in C (κ = 1 if
K ⊆ R, else 2; D = DK/κ). α1,…,αn ∈ K* satisfy the **Kummer (strong
independence) condition** (1.5):

    [K(√α1,…,√αn) : K] = 2^n.

Let h(αj) be the absolute logarithmic height, ln αj arbitrary fixed values of
the logarithms, ρ = rank_R{ln α1,…,ln αn}. Take Aj ≥ max{h(αj), |ln αj|/D,
1/(DC1)} (Theorem 2.2's choice (2.13)), Ω = A1⋯An, A1 ≤ ⋯ ≤ An,
B = max{ |bj|Aj/An : 1 ≤ j ≤ n } (2.14), and define C1, C2 by (2.4):

    C1 = (1 + e^{-2n}/148)(n ln 2 + 2)(1 + 1/n) C3,   C3 = n/ρ,
    C2 = 4(n + 1)(6 + 5/(n ln 2 + 2)) e^{2n} n^{1/2} C3,     [exact form per (2.4)]

with C′0 = ln(C2 D ω/(C1 An)) (2.15), ω = Ω. Then (Theorem 2.2, inequality
(2.16)):

    ln|Λ| > −112 · 2^n · C2 · C′0 · D² · ω · ln(2eB).

Theorem 2.1 gives the more precise but more technical version (2.12):
ln|Λ| > −91·2^n·C2·C0·D²·W0·ω, with C0, W0 satisfying explicit conditions
(2.6),(2.8),(2.9)–(2.11) — quotable from the full text if the run's bound needs
the sharper form.

Theorem 2.3: for K = Q with Aj ≥ h(αj), E = 1, C3 = n, the same bounds hold
with ϑ = 1; and for positive rational integers αj with Aj = ln αj the constant
ϑ improves to (1/2)(1 − 1/(n·e^{n+1})), strengthening the bound by a factor
~2^n.

The n-dependent factor in (2.16) satisfies (Remark after 2.16)

    112·2^n·C2·ϑ^n/(C1^n e^{−n})·(C3 exp(C3)Ee/(2ϑ))^ρ < 2^15 (ne/(2ρ))^ρ ρ(2e^{2ρ} ln 2)^n / n^{1/2}.

## What the run must know about hypotheses before applying

1. **Kummer condition (1.5) is required for these constants.** Without it the
   constant picks up an extra factor n^n and B must be the weaker (1.9)
   (Matveev §1, p. 725–726). Any application to a curve family must either
   verify (1.5) or quote the weaker bound. This is a verifiable algebraic
   condition: for the numbers α appearing in the linear form attached to
   C(x,k1)=C(y,k2), test whether adjoining √α1,…,√αn to K gives degree 2^n.
2. The heights are **absolute logarithmic heights h(α)_log**; other authors
   (incl. Tiebekabe–Diouf's Theorem 2.9) use exponential A_j, forcing ln A_j in
   place of A_j — the mathnet primary's Remark after (1.4) flags exactly this.
   When quoting the bound, state which convention.
3. ρ = rank of the span of {ln α1,…,ln αn} over the reals; κ = 1 (K real) or
   2; D = DK/κ. Kummer condition constrains which α's can be taken together.

## Bearing for the run

- This is the concrete engine for an effective per-pair bound: solutions of
  C(x,k1)=C(y,k2) with x,y large force a small (non-zero) linear form in
  logarithms; Matveev's (2.16) with the explicit C1,C2 turns "small" into an
  explicit upper bound on x,y — a computable number, not a citation. The
  constants are big but concrete; tool_builder can evaluate them for a chosen
  (k1,k2).
- It sharpens the run's "effective but astronomical" record: the
  "triple-exponential" description in CONTEXT.md is exactly the size of these
  Matveev-type bounds; the primary now lets the run state the shape of the
  bound instead of quoting the folklore.
- **It does not touch uniformity in k**: C1,C2,C′0,ω all grow with n (number
  of logarithms) and D and the heights, which for binomial curves grow with
  k1,k2. So Matveev + BST is effective per pair, non-uniform in the pair —
  the exact ineffectivity-vs-uniformity wall, now with the explicit constants
  on the effective side of the ledger.

```claim
id: matveev-2000-explicit-constants-primary
statement: Matveev (Izv. Math. 62 (1998) 723-772, homogeneous rational case,
  Kummer condition): for Lambda = b1 ln(alpha1) + ... + bn ln(alphan), n>=2,
  integers bj != 0 (bn != 0), Lambda != 0, D = DK/kappa, and
  Aj >= max{h(alpha_j), |ln alpha_j|/D, 1/(D C1)}, Omega = prod Aj,
  B = max{|bj| Aj/An}, with C1 = (1+e^{-2n}/148)(n ln 2 + 2)(1+1/n) C3,
  C3 = n/rho, C2 = 4(n+1)(6+5/(n ln 2+2)) e^{2n} sqrt(n) C3,
  C'_0 = ln(C2 D Omega/(C1 An)):  ln|Lambda| > -112 2^n C2 C'_0 D^2 Omega ln(2eB).
  Requires [K(sqrt(alpha1),...,sqrt(alphan)):K] = 2^n; without it the constant
  gains an extra n^n factor and B weakens to max|bj| (Matveev §1).
hypotheses: Kummer condition (1.5); h = absolute logarithmic height; B as (2.14);
  the constants are quotable from the held full text (Theorem 2.2, (2.4), (2.16)).
holds-here: yes as the engine for per-pair effective bounds on C(x,k1)=C(y,k2)
  solutions; the Kummer check and the height/degree bookkeeping are the gates
  the run must verify before quoting a number. It is per-pair and not uniform
  in (k1,k2) since C1,C2,D,Omega grow with n and the heights.
status: asserted-by-source (PRIMARY full text held at
  research/sources/matveev-2000-homogeneous-linear-form.full.md)
bearing: the explicit constants that turn "effective in principle" into a
  computable bound for a chosen (k1,k2); the uniformity wall remains, now
  quantified on the effective side.
anchor: research/summaries/matveev-2000-homogeneous-linear-form.md
```

## Relationship to the other Matveev sources in the library

- `research/sources/matveev-application-linear-forms.full.md` (Tiebekabe–Diouf
  2021): a worked pipeline (Matveev + Dujella–Pethő continued fractions) on a
  specific equation; its Theorem 2.9 is a transcription of this primary's
  bound. Use the primary for constants.
- The Bertin paper in the de Gruyter volume preview also cites Matveev for the
  small-logarithmic-height problem. Not needed further.