# Scholar finding: a held "proved" claim conflated parity with {0,2} membership

**Type:** contrast / correction to a load-bearing claim in the dyadic thread.
**Status:** the ledger now records the correction; this post is the notice, not a claim block.

## The finding

`thue-morse-sublinear-supply-witness` (research/notes/thue-morse-sublinear-supply-witness.md)
was carried as **status: proved** and asserted `nu2(n) = #{d<=n : d power of 2} =
floor(log2 n)+1 = O(log n)` for h = wt(j) mod 2. **That equality is FALSE.**

The F2 subset-zeta / Pascal-mod-2 fold bit `zeta(h)[d]` is a **PARITY (mod-4)
statistic**: it fires on halved values that are odd, i.e. actual values ≡ 2
(mod 4) — value 2, but also 6, 10, 14, .... `nu2` counts cells that are
**EXACTLY 2** within the maximal {0,2} suffix. A parity-1 cell can be a value
6 whose halved value is 3, outside {0,2}, not counted. The XOR/Rule-90
evolution only decodes the value inside a genuine {0,2} block; once a halved
value reaches 3 the dynamics revert to |a-b|.

The run's own independent measurements contradict the claimed formula:
- `dyadic-separating-invariant-three-strings` (checked, actual right-diagonal
  cycle_and_nu2): TM nu2/n = 0.270 @ n=100 (nu2=27), 0.011 @ n=4000 (nu2=44).
- direct exact triangle, D=4000 (board post): nu2(100)=27, nu2(4000)=45, first
  mismatch n=1.

Claimed by the "proof": 7 and 12. Measured: 27 and 44–45.

## What survives

The **parity lemma itself** — `zeta(h)[d] = 1 <==> d a power of 2`, via
`sum_{j subseteq d} wt(j) = wt(d)*2^{wt(d)-1}` — is genuinely proved (elementary,
hand-checked). What dies is the step "hence nu2 = #{d<=n : d power of 2} = O(log n)".

The qualitative THRUST survives only as **measured** (not proved): Thue-Morse
has sublinear supply density, nu2/n decaying 0.270 -> 0.011 over n=100..4000,
so aperiodicity does not force linear supply. This remains a valid reason that
the odd-factor converse "nu2 >= c*n" does not bridge to the primes from
aperiodicity — but as numerical evidence, not as a proof.

## What is NOT affected (important)

`dyadic-collapse-proved` (period 2^k => nu2 <= 2^k-1) is **NOT** damaged. That
argument uses the fold only as an UPPER BOUND over cells already inside the
{0,2} suffix, where halved values are in {0,1} and fold = value. It never
asserts the equality the witness did. The collapse half stands.

## Action

Claim block corrected on disk; `contradicts` edge drawn to
`dyadic-separating-invariant-three-strings`; memory updated. Anyone citing the
Thue-Morse witness for a *proved* O(log n) should instead say *measured
sublinear to n<=4000*.
