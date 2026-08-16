# Scholar pass — Tao Higher Order Fourier Analysis verified, char-2 caveat filed

## What was added

The librarian added Tao, *Higher Order Fourier Analysis* (AMS GSM 142) as the
reference volume for GOAL priority 2's vocabulary. This pass:
1. Verified the digest's three central statements against the full text
   (Gowers norms / inverse conjecture Thm 1.5.3 at lines 4411–4520; classical
   vs non-classical polynomial, Cor 1.4.2 at 3560–3705; Weyl/vdC equidistribution).
2. Rewrote the digest (`research/summaries/tao_higher_order_fourier_analysis.md`)
   and added **two claim blocks**: `tao-inverse-conjecture-blind-iff-nilphase-orthogonal`
   and the genuinely new one, `tao-low-characteristic-nonclassical-polynomial-unavailable`.
3. Stored the durable finding in Cognee.

## What the new finding is

The digest originally read Tao as supporting the "order-K functional blind ⇔
orthogonal to K-th nilphases" inversion. Reading §1.4 closely shows this is a
**high-characteristic** statement: it is clean only for `char(F) > d`. SUPPLY's
fold is over **F₂**, the paradigm low-characteristic case, where non-classical
polynomials occur (the F₂ "quadratic" `P(0)=0, P(1)=1/4` is not a shifted
classical phase) and Tao explicitly restricts away from the regime, noting the
low-characteristic non-classical theory is partly not in the literature.

**Consequence (cautionary):** any claim that a K>1 functional of the F₂ fold is
controllable by an arithmetic input weaker than switch density must not silently
import the high-characteristic inverse theory. The control on the constants at
characteristic 2 is not provided by this source. This matches and strengthens
the existing negative findings — door 3 (Thue–Morse) is Gowers-uniform of all
orders (Konieczny), so finite-order correlation control of `h` cannot be the
weaker input regardless of characteristic caveats.

## Not helpful, and why

For the specific gap request `walsh-spectral-subset-b904` (a Walsh/subset-sum
lower bound on `wt(Φ_n h)`, or a finite-prefix/index-domain transfer for the
prime gap-parity string) Tao does not help: it is about the structure of
correlation, gives no `wt` lower bound, and does not touch the mod-4 switch side.

## Contradictions with recalled memory

None. Cognee recall returned 404 (no prior data), so the on-disk claim ledger is
authoritative; the new claims are consistent with it (the Gowers-uniformity
claims `konieczny-thuemorse-gowers-uniform-exponential` and
`bkm-automatic-structured-plus-gowers-uniform` corroborate the obstruction, and
the low-characteristic caveat adds to them rather than contradicting them).

## What the run still lacks

Unchanged: the single open statement is an unconditional second-moment /
submask-window Walsh bound on the prime gap-parity string (`E[S(n)²]=O(n)`,
request `walsh-spectral-subset-b904`). No source provides it; it is a theorem
gap, not a library gap.
