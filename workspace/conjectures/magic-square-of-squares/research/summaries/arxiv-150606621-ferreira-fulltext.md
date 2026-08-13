# Ferreira's claimed proof of non-existence (arXiv:1506.06621) is invalid

Source: Jailton C. Ferreira, "On the 3×3 magic square constructed with nine
distinct square numbers," arXiv:1506.06621v2 (2015, math.GM). Abstract page:
`research/sources/arxiv-150606621-threexthree-magic-square-nonexistence-proof.full.md`;
full 4-page proof: `research/sources/arxiv-150606621-ferreira-fulltext.full.md`.

## What the paper claims

A short 4-page "proof" that **no** 3×3 magic square of nine distinct squares
exists. It works by parametrising the 3×3 magic square as
`(a,b,c;d,ε,f;g,h,i)` with centre ε, shows ε = x/3, and (eqs. 21–28) writes
each entry as ε ± Δᵢ with Δ₁≠0, Δ₂≠0, Δ₁≠Δ₂ required for distinctness. It then
setups up the main diagonal `n² + m² = 2e²` (eq. 44, with `a=n²`, `i=m²`,
`ε=e²`) and the middle column `(m−z)² + (n+w)² = 2e²` (eq. 45, with `c=(n+w)²`,
`g=(m−z)²`). Subtracting gives (46):
`(m−z)² + (n+w)² − (m²+n²) = 0`.
Solving (46) for z:
`z = m ± √(m²−2nw−w²)`; the paper keeps `z2 = m − √(m²−2nw−w²)`.
It then claims substituting z2 into (46) yields (47)
`n²−2nw−w²−(n+w)² = 0`, whose solutions force `w=0` or `w=−2n`, contradicting
Δ₁≠Δ₂ and positivity. Hence "no magic square with nine distinct squares."

## Where the proof fails (exact, reproducible)

**The step (46) → (47) is not a consequence of the substitution.** Substituting
`z = z2 = m − √(m²−2nw−w²)` into (46):

`(m−z2)² = (√(m²−2nw−w²))² = m²−2nw−w²`, so (46) becomes
`(m²−2nw−w²) + (n+w)² − m² − n²`
`= m²−2nw−w² + n²+2nw+w² − m² − n² = 0`.

That is the **identity 0 = 0**. It carries no information — and necessarily so:
z2 was defined as a *root of (46)*, so substituting it into (46) must vanish
trivially. The paper's equation (47) `n²−2nw−w²−(n+w)²` does **not** equal the
result of the substitution; it differs by the m²±n² cancellation having been
written incorrectly. In fact (47) simplifies to `−2w(2n+w)`, which is not
identically zero and is not implied by anything.

**Concrete countercheck to the claimed implication.** Take m=5, n=3, w=1
(so 2e²=m²+n²=34, e²=17; irrelevant whether e is an integer — the algebra of the
implication is what is being tested). z2 = 5 − √18. Then
(46): `(√18)² + (3+1)² − (25+9) = 18+16−34 = 0` ✓ (46 holds)
(47): `n²−2nw−w²−(n+w)² = 9−6−1−16 = −14 ≠ 0` ✗ (47 does **not** hold).
So the implication "(46) holds ⇒ (47) holds" is false.

**Diagnosis.** The error is the classic one of a fake descent: construct an
equation from the two AP conditions, solve it for a variable, substitute that
root back into the *same* equation (getting a tautology), then substitute a
*hand-written* different equation in its place and solve that to reach the
desired contradiction. No constraint on w is actually derived.

**Consequences.** The paper does **not** establish non-existence. It should not
be cited as a proof. This is consistent with the run's established fact that
genuine MSS exist over extension fields (`extension-field-mss-exist`) — a blank
structural argument that also killed those would be false — and with the fact
that the problem remains open. The paper is a data point in the long list of
failed elementary proofs, and the *reason it fails* (substituting a root into
its own defining equation and calling the tautology a constraint) is worth
recording so nobody re-proposes it.

## Claim block

```claim
id: ferreira-15060621-proof-invalid
statement: Ferreira (arXiv:1506.06621) does not prove non-existence of a 3x3
  magic square of distinct squares; the proof is invalid at the (46)->(47) step.
hypotheses: none needed; the refutation is pure algebra on the paper's own
  equations (44)-(49).
holds-here: yes (the claim under inspection is "no MSS exists", which this
  refutation does not establish either way)
status: checked (algebra verified by hand and by construction: substituting
  z2=m-sqrt(m^2-2nw-w^2) into (46) yields the tautology 0=0, not (47); witness
  m=5,n=3,w=1 satisfies (46) but not (47))
bearing: removes a citation-as-proof; reinforces that non-existence remains
  open; the specific failure (root-substitution tautology) is a known dead end
  not to be re-proposed.
anchor: research/summaries/arxiv-150606621-ferreira-fulltext.md
```
