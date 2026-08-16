# Ghosh char-0 break: eq (4.18) uses −n as a unit

Close-read + computational re-derivation of the exact step in the claimed Ghosh
proof (arXiv:2501.09272) that breaks in characteristic p. The result was
previously recorded only as prose in `research/threads/ghosh-char0-step.md` and
in a closed task's reason; it is now a claim so `search_claims` can find it.

```claim
id: ghosh-char0-break-4-18
statement: In the claimed Ghosh proof of CA (arXiv:2501.09272), the
  degree-lowering isomorphism eq (4.18) uses the leading coefficient −n of
  F(n,j_n,n) as a unit: F(n,j_n,n) has leading coefficient f(n,j_n,n), which
  equals 1 for j_n ≠ n and equals −n for j_n = n. The isomorphism (and the
  injectivity of ι_{1,*} in Prop 4.3 that it drives) therefore holds only
  when char(𝕂) does not divide n. Separately, Cor 3.9 / Thm 3.6 — the
  minimal-generator bound μ = n−1, the Abel–Gontcharoff / Brouwer-degree
  step the author flags as "works only over ℂ" — requires char ∉ 𝒫(n), a
  finite exceptional set. Hence the argument genuinely stops in char p at the
  step d = n with p | n: the unit −n is 0, (4.18) fails, and the induction
  cannot conclude. The char-p witnesses x^{p+1}−x^p (degree n = p+1) sit
  exactly at this boundary (the step d = p needs char∤p to fail).
hypotheses: the downward induction of Ghosh §4 as stated (Prop 4.3, eq (4.18),
  lines 503–606 of ghosh2025_proof_html.full.md); 𝕂 an arbitrary field
holds-here: yes — the char dependence is a named divisibility (char | n at
  eq (4.18); char ∈ 𝒫(n) at Cor 3.9/Thm 3.6), which is consistent with CA
  being false in char p and with the claimed proof being char-0-only. The
  proof does NOT prove the false char-p statement.
status: checked — 1313 exact checks over QQ and GF(p), p ∈ {2,3,5,7}, ALL
  PASSED (code/out/ghosh_break.captured.txt ends "TOTAL: 1313 checks, 0
  failed."). code/ghosh_charp/verify_break.py re-derived f(n,j,n) = 1 (j≠n)
  and = −n (j=n) independently, and confirmed −n = 0 in GF(p) exactly when
  p | n; Φ^#_{n,n}(e_1) = (x_1+…+x_{n−1}) − n·x_n verified for n=2,3,5,6,10.
evidence: checked (close-read of ghosh2025_proof_html.full.md §4, plus the
  computational re-derivation in code/ghosh_charp/verify_break.py)
bearing: Names the exact char-0-only step of the claimed proof, satisfying the
  char-p test GOAL.md demands: the argument is not characteristic-free and
  does not contravene the char-p counterexamples. Any future proof must use
  characteristic 0 in a way that dies at the same divisibility (char | n).
program: code/ghosh_charp/verify_break.py
capture: code/out/ghosh_break.captured.txt
anchor: research/threads/ghosh-char0-step.md; code/out/ghosh_break.captured.txt
falsifies: the claim that the Ghosh argument is characteristic-free, or that it
  would prove the (false) char-p statement
```
