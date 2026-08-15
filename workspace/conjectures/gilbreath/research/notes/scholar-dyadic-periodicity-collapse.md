# Scholar digest: dyadic-periodicity-collapse dichotomy vs the held library

Directive 58 live thread: why does the F2 transfer die exactly on dyadic-periodic
halved-gap bit strings, and is there an anti-dyadic property of the primes
restoring ν2 ≥ c·n? This note says what the *held library already establishes*
about that dichotomy, so the proof work is not spent re-deriving it. Library is
closed (39/46); nothing new was fetched.

## 1. The "power-of-2 period ⇒ collapse" half is already half-proved on disk

The mechanism the thread needs is already a proved claim:
`rule90-interior-xor` (status: proved) — every halved entry of a {0,2} block
is an XOR-fold of the row-1 halved-gap bits with the Pascal/Lucas kernel,
and at depth a power of 2 the kernel is all-1. `granville-lucas-kummer-
sierpinski` (asserted, held) supplies binom(2^j,·)≡1 mod 2. So:

> A periodic halved-gap bit string h with period 2^k makes every {0,2}-tail
> cell a fixed XOR-fold of windowed bits; the tail value-set, hence the
> {0,2}-suffix length and ν2, is O_k(1).

That is exactly the "power-of-2 period forces ν2 = O_k(1)" leg the thread asks
theorem_prover to prove. **It needs no new source** — it is rule90-interior-xor
+ Lucas + the transfer matrix. The proof task is to make the O_k(1) bound
explicit (the transfer matrix is an explicit linear map; see
`transfer-matrix-kernel-allones` for its structure).

## 2. What BCZ 2023.11776 actually establishes (and does not)

Bhat–Cobeli–Zaharescu 2023.11776 (held, proved in source) studies the
halved-{0,1} operator (|a−b| = a+b mod 2, the Pascal/rule-90 addition, their
Eq. (6)) and classifies *rows that repeat*:

- **Theorem 2**: a binary row is ultimately replicated identically in the next
  PG line iff its F2 generating function is φ(α)=P/(1+X+X^r) or
  P/(X^r(1+X)+1).
- **Theorem 5**: α is ultimately identical with Ψ(α) (a *fixed class under the
  quotient* Ψ̂) iff φ(α)=G(X)/(1−X^{2^d−1}).
- **Eq. (6)**: on F2 the operator acts as φ(Ψ(α))=((1+X)φ(α)−α0)/X,
  agreeing with this run's rule90-interior-xor.

**Do NOT over-read:** Theorem 5 classifies rows that are fixed under the
operator (repeat in the next line), which is a property of a *row within the
triangle*, not a statement that "an eventually periodic *input* collapses." A
periodic input row need not itself be a PG fixed class (BCZ's own example T =
(0,1,1,1,0,...) is periodic but NOT a fixed class — its triangle dies to zeros).
So BCZ Thm 5 is NOT the collapse mechanism for the dichotomy.

**The honest collapse mechanism is rule90-interior-xor.** Every {0,2}-tail
cell of the right diagonal is an XOR-fold of a finite window of the initial
halved-gap bits h over the Pascal/Lucas kernel. If h is periodic of period p,
the windowed XOR-folds take only finitely many values (the XOR-sums of the
period word and its shifts), so the tail values are bounded by the period word
— the {0,2}-suffix length and ν2 are O_p(1). This is proved (rule90-interior-xor
is status: proved) and it is the correct anchor for the collapse half. It is
**stronger and cleaner** than trying to use BCZ: periodic of ANY period p
(bounds folds by period, not only power-of-2), and it needs no fixed-point
machinery.

**Claim block**
```claim
id: rule90-periodic-window-collapse
statement: If the halved-gap bit string h is periodic with period p, then every
  {0,2}-tail cell of the right diagonal is an XOR-fold of a bounded window of h,
  taking only finitely many values (the XOR-sums of the period word and its
  shifts). Hence the {0,2}-suffix length and nu2 are O_p(1).
hypotheses: rule90-interior-xor (proved): tail cells are Pascal/Lucas XOR-folds
  of the row-1 halved-gap bits; h periodic of period p.
holds-here: no — FALSE as stated for any period with an odd factor (period 3
  gives nu2 = 2666 at n = 4000, measured), so the "any period p" form does not
  hold for the binary system it claims to describe.
status: refuted — the over-general form (ANY period p ⟹ nu2 = O_p(1)) is FALSE.
  The fold window [c, c+d] grows with depth d, so it is bounded only when the
  submask factorization d = D·2^k + s makes the inner XOR vanish, which fails
  for odd-factor periods. The correct restriction (period a POWER OF TWO) is
  the proved theorem `dyadic-collapse-proved` (research/notes/dyadic-collapse-proof.md).
closed-by: rule90-periodic-window-collapse-refuted
bearing: kept here as a refuted claim with its flaw recorded, so the dead
  over-generalisation is not re-derived (Directive 65: a refuted claim must
  stay, never be deleted). BCZ Thm 5 is NOT the mechanism — do not cite it for
  collapse; the power-of-2 collapse is rule90-interior-xor + Frobenius.
anchor: research/notes/rule90-interior.md, research/notes/scholar-dyadic-periodicity-collapse.md
answers: dyadic-periodicity-collapse
```

## 3. The "odd factor in the period ⇒ ν2 ≫ n" half is NOT in the library

The stage-1 dichotomy table (host-measured, Directive 58) says period 2,4,8
collapse (ν2 = O(1)) but periods 3,5,7, and critically period 6 = 2·3, grow
ν2 ~ c·n with c ∈ [0.53, 0.67]. No held source — BCZ, Chase/CHT, the Ducci
family, granville-lucas — explains **why an odd factor in the period forces
positive linear growth**. This is genuinely new and is the real open content of
the thread. Held material only settles the collapse side; the growth side is
up for theorem_prover / pattern_finder, and must NOT be claimed as sourced.

## 4. Contradiction to resolve before the dichotomy is load-bearing

The held claim `nu2-transfer-not-restored-by-nondegeneracy` (status: checked)
measured the **alternating-2/4** family — halved-gap bits h = [1,0] period 2 —
at **ν2 = 1** (both conventions), independently via two constructions, n =
200..5000. The stage-1 table lists **period 2 (h=01)** at **ν2 = 2** across
n = 200..1200. By complement-immateriality of the transfer matrix
(kernel = span(all-ones), `transfer-matrix-kernel-allones`), h=[1,0] and its
complement [0,1]=h+allones give the SAME transfer-matrix tail. So the two
figures (1 vs 2) should not both be right as stated.

Both are measured by the same λ-convention (maximal {0,2} suffix of the right
diagonal). The discrepancy is most plausibly a convention/off-by-one (terminal
element included vs excluded; or which gap indexes the periodic pattern starts
at — q1=2,q2=3 fixes a first gap of 2 outside the period, so "h=01" with the
first pattern bit applied to a different gap could legitimately shift which
columns reach the tail). **tool_builder (thread step 1) must reproduce both the
eight stage-1 rows and the period-2 value against the directive-55 alt-route
(ν2=1) and state which convention reconciles them.** The dichotomy's clean
power-of-2-collapse/odd-grows split does not stand on the two rows that
disagree until this is resolved. I cannot run code this cycle, so I assert this
as a discrepancy and recommend the resolution, not as a verdict.

## 5. What this does and does NOT give the primes

- **Gives:** a *structural* reason the collapse side is robust
  (rule90-interior-xor: a periodic halved-gap window gives an O_p(1) bounded
  tail). It explains why a *periodic* h collapses — a satisfying negative
  result. (BCZ Thm 5 is the fixed-point classification of repeating rows; it
  is NOT the collapse mechanism and must not be cited as such.)
- **Does NOT give:** any quantitative anti-dyadic input to G-supply. The primes
  are aperiodic (ν2/w ∈ [0.689,0.867], `g-supply-transfer-measured`), but the
  dichotomy "aperiodic ⇒ grow" is a *contrapositive of the collapse theorem*
  only for eventually-periodic, not for the primes being non-eventually-periodic
  in the quantitative sense ν2 ≥ c·n. The gap between "not eventually periodic"
  and "ν2 ≥ c·n" is exactly the honest remaining statement. **Aperiodicity
  alone does NOT close G-supply** — reaffirming the named-open status
  (`abgs-2011-s9-mod4-switch-limit-open`). The dichotomy is a structural
  clarification, not a supply proof.

## Sources read this cycle
- BCZ 2023.11776 quasi-periodicity (full text) — the fixed-point classification.
- rule90-interior.md, transfer-matrix-kernel.md, directive55 nu2 characterization
  (held claims) — the collapse mechanism and the contradiction.

## Stored
- remember_memory: dyadic-periodicity-vs-held-library (synthesis, complement
  prediction, contradiction flag, what is/isn't in the library).
