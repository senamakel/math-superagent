# Oracle verification — this workspace's own reproduction

The Erdős ternary conjecture oracle, run in THIS workspace, captured at
`code/out/oracle_verify.captured.txt` (ALL PASS). This is the run's own
verification bound, kept separate from the literature's cited (not reproduced)
bounds Gupta n<4374, Vardi n≤2·3^20, Saye n≤2·3^45.

## What the capture establishes

- `digit_free(0)=digit_free(2)=digit_free(8)=True`; `digit_free(1)=digit_free(3)=
  digit_free(5)=False` (1=2_3, 3=22_3, 5=1012_3). Witness check PASSED.
- `sieve_count(k) == 2^(k-1)` for k=1..26, cross-checked against `direct_count`
  and `lift_count` for k≤11 (all agree). Counting obstruction CONFIRMED.
- `finite_check` over `[1,1000]` = {2,8}; exempt set size 2. So in this run's
  own verified range the only digit-2-free powers beyond 8 are exactly the
  two witnesses 2 and 8 (and 0).

This resolves the recalled `|A_k|=2^k` vs `2^(k-1)` contradiction in CONTEXT.md:
**`2^(k-1)` is right** (hand check k=1: A_1={0}, |A_1|=1=2^0; the k=1 row in the
table shows |A_1|=1). The value `2^k` was wrong.

```claim
id: ORACLE-VERIFIED-THIS-WORKSPACE
statement: In this workspace, the exact integer oracle verifies: digit_free
  on 0,2,8 = True and on 1,3,5 = False; sieve_count(k) == 2^(k-1) for
  k=1..26 with direct and lift counts agreeing for k<=11; and finite_check
  over [1,1000] = {2,8} (the only digit-2-free powers in that range beyond 0
  are 2^2 and 2^8). The counting obstruction |A_k|=2^(k-1) is therefore
  confirmed computationally in this workspace.
hypotheses: exact integer arithmetic (no floats); sieve works mod 3^k only,
  never materialising 2^n.
holds-here: yes.
status: checked (computed and cross-validated two ways -- direct_count and
  lift_count agree with sieve_count for k<=11; captured at
  code/out/oracle_verify.captured.txt).
bearing: upgrades SIEVE-EXACT-COUNT from 'asserted (recalled)' to 'checked in
  THIS workspace'. Confirms the modular sieve can never close by counting at
  any finite k. The run's own verified bound is k<=26 / [1,1000], NOT the
  literature's 2·3^45 — those stay sourced-but-not-reproduced.
anchor: code/out/oracle_verify.captured.txt
answers: code-oracle-verify-63ce
```

## Status

Verified numerically in workspace (k≤26, [1,1000]). Cross-validated by two
independent counting methods. Not a proof of the conjecture — it confirms the
counting obstruction, it does not overcome it.
