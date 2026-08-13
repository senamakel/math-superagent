# Saturation of modulus 11

Directive 7: M=11 is the smallest modulus and the cheapest test of whether the
Salez seven-equation generator can saturate any modulus at all. Either exhibit
families for the missing QNR-allowed residues, or prove an obstruction
forbidding them. Either answer is a result.

```thread
question: Can the Salez seven-equation generator produce polynomial identity
  families for the two QNR-allowed-but-unrealised residues s ∈ {3, 4} at
  modulus 11 (where s = (n−1)/840, n = 840·11·k + (840s+1))?
status: open
rests-on: subprogression-families-verified-and-coverage,
  subprogression-coverage-positive-limit,
  seven-equations-complete,
  coverage-figure-triangulated
blocked-by: none
next: (1) Run verify_current_coverage.py and capture output (directive 7
  priority 1). (2) Run search_subprogression.py targeting b yielding s=3 and
  s=4 at a=9240, with widened parameter bounds. (3) If search fails, prove
  obstruction: for a=9240 and b=840·3+1=2521 or b=840·4+1=3361, show the
  seven equations admit no solution with positive integer A,…,F.
```

## Schinzel analysis: only 2 residues are actually missing, not 8

`code/pattern_mining/schinzel_residue_gap.py` computed the Schinzel-legal
residues at each pure-prime modulus. For M=11:

- QNR-allowed (Schinzel-legal): s ∈ {3, 4, 5, 7, 10} (5 residues)
- Currently realised: s ∈ {5, 7, 10} (3 residues)
- **Gap: s ∈ {3, 4}** (2 residues — the only ones the generator could
  possibly reach)
- QR-blocked (Schinzel-forbidden): s ∈ {0, 1, 2, 6, 9} (b is a QR mod 11 when
  s takes these values, so no ℤ[k]-polynomial identity can exist)
- Non-unit (b divisible by 11): s = 8 (b=6721, gcd(b,9240)≠1, not primitive)

The gap is two residues, not eight. The other six are structurally forbidden
and their absence is not a failure of the generator — it is Schinzel's theorem
doing what it was proved to do.

## The obstruction approach

For s = 3 (b = 840·3+1 = 2521) and s = 4 (b = 840·4+1 = 3361):

1. **Search**: run `search_subprogression.py` targeting these b values directly
   with widened A,B,C,D,E,F parameter bounds.

2. **Obstruction proof (if search fails)**: For a=9240, examine each of the
   seven modular equations (14a–15d). Each equation fixes some subset of
   A,B,C,D,E,F as constants and expresses the others as functions of p =
   9240k+b. For b=2521 and b=3361, check whether any choice of the constant
   parameters yields positive-integer A,…,F for all k. This is a finite check
   over the parameter space — and if it returns empty, the obstruction is
   proved: **the Salez seven-equation generator cannot realise s=3 or s=4 at
   modulus 11**.

## Reference

- Schinzel Thm 1: `research/summaries/schinzel-three-unit-fractions.md`
- Salez seven equations: Proposition 3, Corollary 1 in
  `research/sources/salez-seven-modular-equations.full.md`
- Schinzel residue gap analysis: `code/pattern_mining/schinzel_residue_gap.py`
- Coverage triangulation: `code/out/coverage_triangulated.md`