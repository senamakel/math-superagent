# Librarian — novelty of Γ̂(1/2) = φ/2, scoped to the held library

Status: library-grounded narrowing of the `yugamma-half-collapse` external-novelty
gap. NOT a global literature-novelty search (which the standing operator
directive `stop-adding-sources` forbids); a statement, from the primary texts already
on disk, of what the three relevant authors do and do not state.

## What was checked

The `yugamma-half-collapse` thread and CONTEXT.md Gaps row record that whether
Yu / Cambie / Liu already state the exact collapsed certificate value
Γ̂(1/2) = φ/2 = (1+√5)/4 = 0.80901699… is UNKNOWN. This note reads the three
held primary texts at the exact places that could state it and records what each
says.

Primary texts on disk:
- `research/sources/yu-dimension-free-bounds-2023.full.md` — Yu, Entropy 25(5):767 (2023).
- `research/sources/cambie-better-bounds-entropy-2022.pdf.full.md` — Cambie, arXiv:2212.12500.
- `research/sources/liu-conditionally-iid-coupling-2023.full.md` — Liu, arXiv:2306.08824.

## Findings (each read directly in the source text)

1. **Yu** — Prop. 1 defines the two-atom relaxation `Γ̂(t)` and the objective
   `g(P_pq, α) = (1−α)E h(p+q−pq) + α E h(φ(1,p,q))`, with the coupling family
   `(1−β)Q_{a1,a2} + β Q_{b1,b2}` and `β = (t−a)/(b−a)`. The paper's record value
   is the t_max where Γ̂ crosses 1 (≈0.38234). Yu does **not** state any value of
   Γ̂(t) at t=1/2, nor the exact φ/2 collapse, nor the minimizer
   a=(3−√5)/2 at the collapse. The only 1/2 in the statement is the conjecture's
   target and the median cutoff in φ(1,p,q).

2. **Cambie** — solves Sawin's Question 2, weights (1−α)E H(p+q−pq) +
   α E H(max(p,r,min(p+r,1/2))). The 1/2 occurrences are the median/min cutoff
   `min(p+r,1/2)`. Cambie does **not** state a closed form Γ̂(1/2) or φ/2. His
   value is the t_max = 0.3823455334 ceiling, not a t=1/2 certificate.

3. **Liu** — the conditionally-IID coupling inequality (eq. 7), objective in
   (13). The 1/2 occurrences are again `min(S+R,1/2)`. Liu does **not** state a
   t=1/2 value or φ/2.

## Scoped conclusion

Within the held library's three primary entropy-era texts, **none states the
exact collapsed certificate value Γ̂(1/2) = φ/2** at the α=0 collapse (nor the
minimizer a=(3−√5)/2 at that end). So the run's φ/2 result is not a restatement
of a value these three authors printed.

This is NOT a proof of global novelty: it does not rule out a source outside the
library stating φ/2 (e.g. a later survey, a lecture note, or a section of these
papers the grep did not surface). It upgrades the closure only to
"absent from the three held primary treatments," which is the honest, scoped
statement. The `yugamma-half-collapse` thread's novelty row can now close with
this exact scope.

## What this does NOT do

- It does not re-run the prohibited record-freshness searches (operator
  directive 15 / `stop-adding-sources`): no new download, no arXiv query.
- It does not claim φ/2 is a new value — only that it is absent from the held
  texts.

## Claim block

```claim
id: phiover2-absent-from-held-entropy-texts
statement: The exact collapsed certificate value Gamma-hat(1/2) = phi/2 =
  (1+sqrt5)/4 = 0.80901699... is NOT stated in any of the three held primary
  entropy-era texts: Yu (Entropy 2023, Prop.1), Cambie (arXiv:2212.12500,
  eq.1 objective and t_max result), Liu (arXiv:2306.08824, eq.7/13). Each uses
  1/2 only as the conjecture's target or as a median/min cutoff inside
  phi(1,p,q) / min(p+r,1/2); none gives a closed-form certificate value at
  t=1/2 nor the alpha=0 minimizer a=(3-sqrt5)/2.
hypotheses: the three primary texts named above are the authoritative statements
  of the Yu/Sawin two-atom relaxation; "absence" = not found in the text as held.
holds-here: yes
status: asserted (library-grounded; scoped to the held texts, NOT global novelty)
bearing: closes the external-novelty row of thread yugamma-half-collapse with the
  exact scope "absent from the three held primary treatments". It does not prove
  global novelty; a source outside the library could still state phi/2.
anchor: research/notes/librarian-phiover2-novelty-scoped-2026.md; and the three
  source files it greps
answers: yugamma-half-collapse (partial: the "absent from held texts" half of the
  novelty question is now answered; the "absent from the whole literature" half
  is deliberately left open, per stop-adding-sources)
```

## Files
- This note: `research/notes/librarian-phiover2-novelty-scoped-2026.md`
- Sources read: `research/sources/yu-dimension-free-bounds-2023.full.md`,
  `research/sources/cambie-better-bounds-entropy-2022.pdf.full.md`,
  `research/sources/liu-conditionally-iid-coupling-2023.full.md`
