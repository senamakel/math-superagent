# Status of the M=11 saturation question when this run was paused

Recorded by the operator before the container was stopped, because
`code/out/verify_s11_gap.captured.txt` had zero mentions in
`research/CLAIMS.md` and the previous two runs of this workspace both died with
unrecorded results in their captures.

## What the run produced

```
families covering t ≡ 3 or 4 (mod 11): 230
verified identities: 230/230

M -> s11 covered (all verified):
  M=17: [3,4]   M=23: [4]    M=26: [3]    M=29: [3,4]  M=31: [4]
  M=33: [3,4]   M=34: [3,4]  M=37: [3]    M=38: [3]    M=39: [3,4]  M=41: [3]
```

The 230 identities verify — that part is solid and consistent with every earlier
check, which has never found a bad family in this workspace.

## This does not close the saturation question, and must not be read as doing so

The operator re-ran `aggregate_subprogression.py`. It is **unchanged**:

```
M=11: covered 3, missing 8: [0, 1, 2, 3, 4, 6, 8, 9]
```

The reason is arithmetic, not a stale file. Every modulus in the table above —
17, 23, 26, 29, 31, 33, 34, 37, 38, 39, 41 — is coprime to 11 or has 11 dividing
it only in the cases 33. For a modulus `M` with `gcd(M,11) = 1`, a family
covering `t ≡ s (mod M)` meets **every** residue class mod 11 but covers only
`1/M` of each. So these families contribute a positive fraction of the mod-11
classes 3 and 4 and saturate neither.

Saturating a residue class mod 11 requires either a family at a modulus
divisible by 11 realising that class, or a finite union whose densities within
the class sum to 1 — and a union of classes at moduli coprime to 11 has density
strictly below 1 in the class for exactly the reason recorded in
`subprogression-coverage-positive-limit`: the uncovered density factors as a
product of strictly positive terms.

So the question posed to this run — *can any modulus be saturated* — is still
open, and `M = 11` is still the cheapest place to settle it.

```claim
id: s11-partial-coverage-does-not-saturate
statement: The 230 families in code/out/verify_s11_gap.captured.txt all verify
  as identities, 230/230, and their moduli are 17, 23, 26, 29, 31, 33, 34, 37,
  38, 39 and 41. They are described there as covering t congruent to 3 or 4 mod
  11, but for any modulus M with gcd(M,11)=1 a family covering t congruent to s
  mod M meets every residue class mod 11 while covering only 1/M of each, so
  these families saturate no mod-11 class. Re-running
  aggregate_subprogression.py confirms M=11 remains at 3 of 11 residues
  covered, missing 0,1,2,3,4,6,8,9, unchanged from the previous pass. The
  saturation question is therefore still open.
hypotheses: the families are exact identities in Z[k], established separately in
  subprogression-families-verified-and-coverage; coverage of a residue class is
  measured by density within that class
holds-here: yes. The identity count is the run's own verified output; the
  non-saturation is immediate from gcd(M,11)=1 and was confirmed by re-running
  the run's own aggregator
status: checked
bearing: prevents the 230-family result being read as progress on saturation,
  which it is not. Leaves M=11 as the cheapest open test of whether any modulus
  can be saturated, which by subprogression-coverage-positive-limit is the only
  way the identity-family method could ever close the class n congruent to 1 mod
  840. Recorded as the run was paused, so the next run resumes from it rather
  than re-deriving it
anchor: code/out/verify_s11_gap.captured.txt;
  code/out/aggregate_subprogression.captured.txt; code/out/s11_gap_status.md
source: operator-computation
```
