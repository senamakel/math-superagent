# Weiß — Deducing the Three Gap Theorem from Rauzy–Veech Induction

Source: Christian Weiß, arXiv:1807.11273v3 (Feb 2019).
URL: https://arxiv.org/pdf/1807.11273
Full text: `research/sources/weiss-three-gap-rauzy-veeche.full.md`

## What it establishes

**Theorem 1 (Three Gap Theorem), with exact gap counts in Ostrowski form.**
Let z ∈ (0,1) irrational, continued fraction z = [a0; a1; a2; …], convergents
r_n = p_n/q_n. Let N ≥ 2 have (amended) Ostrowski representation
N = Σ_{j=0}^{m} b_j q_j with 0 ≤ b_j ≤ a_{j+1} and q_m + 1 ≤ N < q_{m+1} + q_m.
Define K_{2l−1} = {q_{2l−1}z}, K_{2l} = 1 − {q_{2l}z} if z < 1/2 (swapped if
z > 1/2). Then the finite sequence ({nz})_{n=1..N−1} has gaps of at most
three lengths

- L1 = K_{m−1} − b_m K_m,  L2 = K_m,  L3 = L1 + L2,

with counts

- N1 = N − b_m q_m − q_{m−1}  (length L1),
- N2 = N − q_m              (length L2),
- N3 = q_m − (N − b_m q_m − q_{m−1})  (length L3).

The proof reinterpretates the Kronecker sequence as the orbit of a circle
rotation (a two-interval exchange) and runs (accelerated) Rauzy–Veech
induction, which is equivalent to the continued-fraction algorithm; after m
steps [0,1) is partitioned into q_m long and q_{m−1} short intervals, and the
point set equals the Kronecker sequence as a set.

## What it implies for PE1006

This is the **explicit, count-carrying statement of the three-gap structure**
the adopted Ostrowski approach (`pe1006-ostrowski-sawtooth-closed-form`,
status adopted) cites as ingredient (i): the k+1 representatives
x_m = frac(−m·a) of the mechanical construction, a = F(n−2)/F(n) a rational
approximant of 1/φ², are exactly a Kronecker sequence, so the gap lengths and
their multiplicities N1, N2, N3 over m = 0..k are given by the continued
fraction / Ostrowski data of a. That turns any sum over m of a function of
the arc midpoints into a sum over the (at most three) gap classes with exact
counts — the structural reduction that makes an O(log k) second route to
Ψ(k) possible, independent of the universal-Euclidean monoid.

Combined with the on-disk van Ravenstein 1988 (three-gap, HAL),
Alessandri–Berthé 1998 (three-distance and words) and Sos 1958 (first proof,
cited therein), this closes the mechanical/Ostrowski alternative's source
requirements: the counts (Weiß/van Ravenstein), the word-side consequences
(Alessandri–Berthé), and the floor-sum primitive (fhq/OI-wiki/LOJ138/AtCoder)
are all in the library. Note Rockett–Szüsz (JNT, sums of fractional parts) is
still NOT on disk — cited in the approach for ingredient (ii); see requests.

## Caveats

- z irrational here; the run's a = F(n−2)/F(n) is rational. The gap structure
  for rational z is the periodic special case of the same continued-fraction
  mechanism (finite expansion); the rational case is covered by the same
  Rauzy–Veech partition argument with the expansion truncated at the last
  nonzero partial quotient. No source on disk states the rational case
  explicitly; the run's small-k oracle checks must cover it.
- The amended Ostrowski representation (b_j ≤ a_{j+1}, minimal m with
  q_m + 1 ≤ N < q_{m+1} + q_m) is the exact bookkeeping needed for k = 10^18.