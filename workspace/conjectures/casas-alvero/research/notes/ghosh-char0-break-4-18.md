# Ghosh char-0 break: eq (4.18) and the Abel–Gontcharoff bound

The claimed Ghosh proof (arXiv:2501.09272) of Casas–Alvero must break in
characteristic p, since CA is false there (charp-false). A close read located
the step, and `code/ghosh_charp/verify_break.py` verified it computationally —
1313/1313 exact checks over QQ and GF(2,3,5,7); capture
`code/out/ghosh_break.captured.txt`. This note records the result as a claim so
`search_claims` can find it, which it could not while the finding lived only as
prose in `research/threads/ghosh-char0-step.md` and in a closed task's reason.

```claim
id: ghosh-char0-break-4-18
statement: In Ghosh's claimed proof of CA (arXiv:2501.09272), the downward
  induction's key injectivity lemma Prop 4.3 uses the leading coefficient of
  F(n,j_n,n) = Φ^#_{n,j_n}(HD^{n-1}_n(x_1,…,x_n)) as a unit in eq (4.18): the
  isomorphism R_n/(F(1,j_1,n),…,F(n,j_n,n)) ≅ R_{n-1}/(Δ_{1n},…,Δ_{n-1,n})
  holds only when char ∤ n, because f(n,j,n) = 1 for j ≠ n while
  f(n,n,n) = −n is the leading coefficient (so −n is a unit iff p ∤ n).
  Independently, Cor 3.9/Thm 3.6 — the Abel–Gontcharoff/Brouwer-degree
  minimal-generator bound μ(I_{n-1}(j_1,…,j_{n-1})) = n−1 — is available only
  for char p ∉ 𝒫(n), a finite exceptional set. Hence the proof genuinely
  stops in char p: at the induction step d = n with p | n the unit −n dies and
  injectivity of ι_{1,*} fails, and the char-p witnesses x^{p+1}−x^p
  (degree n = p+1) sit exactly at the boundary step d = p.
hypotheses: the downward-induction step d = n of Ghosh Prop 4.3, base field 𝕂,
  Hasse–Schmidt derivative convention of the source (HD^i_n(x_1…x_n) = e_{n−i})
holds-here: yes
status: checked
bearing: Names the exact char-0-only step the claimed proof relies on, so the
  proof does not contravene the char-p counterexamples (it does not prove the
  false char-p statement). Every future attempt must beat this named
  obstruction. Computationally verified: 1313/1313 exact checks confirm
  f(n,j,n)=1 (j≠n), f(n,n,n)=−n, the automorphism axioms of Φ^#, and the death
  of the unit −n exactly at p | n.
anchor: research/threads/ghosh-char0-step.md (Findings),
  code/out/ghosh_break.captured.txt, code/ghosh_charp/verify_break.py
```
