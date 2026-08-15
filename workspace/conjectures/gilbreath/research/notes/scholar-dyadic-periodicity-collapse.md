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

## 2. The broader "eventually periodic ⇒ collapse" half is the BCZ fixed-point theorem

Bhat–Cobeli–Zaharescu 2023.11776 (held, proved in source) is the right anchor
for periodicity — and it is strictly more general than the power-of-2 case:

- **Theorem 5**: a binary row α is *ultimately identical* with its Proth–
  Gilbreath image Ψ(α) (= the halved-{0,1} operator, since |a−b|=a+b mod 2)
  **iff** its F2 generating function is φ(α)=G(X)/(1−X^{2^d−1}) — i.e. **iff α
  is periodic** (period `2^d−1` appears; the closure is over the ≍
  ultimately-equal quotient).
- **Theorem 2**: the fixed points (rows replicated in the next line) have
  φ(α)=P/(1+X+X^r) or P/(X^r(1+X)+1).
- Eq. (6): on F2 the operator acts as φ(Ψ(α)) = ((1+X)φ(α)−α0)/X — the
  Pascal/rule-90 addition, agreeing with this run's rule90-interior-xor.

**Bearing on the dichotomy:** if the halved-gap bit string h is *eventually
periodic*, then by Theorem 5 the halved row is ultimately a fixed class under
the PG operator, so the entire halved triangle is eventually self-similar /
periodic in rows. A self-repeating triangle cannot build an unbounded {0,2}
suffix from bounded tails: the values recur, the {0,2}-suffix length and ν2 are
bounded. **This is the structural reason period collapses the transfer.** It
covers power-of-2 periods and every other period — a stronger statement than
the thread's power-of-2 leg.

**Claim block**
```claim
id: pg-theorem5-periodic-iff-fixed-class
statement: A binary row is ultimately identical with its Proth–Gilbreath image
  iff it is periodic (phi(alpha)=G(X)/(1-X^{2^d-1})). Hence an eventually
  periodic halved-gap bit string makes the halved triangle eventually
  row-repetitive, bounding the {0,2}-suffix length and nu2 by a constant of
  the period.
hypotheses: binary (halved) rows; PG operator = |a-b| = a+b mod 2; equivalence
  class = coinciding after finite prefix removal.
holds-here: yes — the halved {0,1} part of the prime triangle is exactly this
  binary system; not a GC statement by itself.
status: proved in source (BCZ Thm 5 + Thm 2 + Eq. (6)); the nu2-bounded
  consequence is this run's inference, asserted not yet checked.
bearing: halves of the Directive 58 dichotomy — "period ⇒ collapse" — are
  already in the library under BCZ Thm 5 + rule90-interior-xor; the
  anti-dyadic growth half is NOT (see §3).
anchor: research/sources/bhat-cobeli-zaharescu-quasi-periodicity-html.full.md
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

- **Gives:** a *structural* reason the collapse side is robust (BCZ Thm 5 +
  rule-90). It explains why a *periodic* h collapses — a satisfying negative
  result.
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
