# Directives

What an operator asked this run to do, and what the run did about it. Written by the runtime; edit the queue, not this file.

## 1 — from steer

Elementary reductions are still 'asserted', not checked, and one is WRONG. code/out/verify_elementary_reductions.md/.py (just written, exact Fraction arithmetic, k up to 4999) confirms research/approaches/oracle-findings.md: the identity x=n,y=(n+1)/2,z=n(n+1)/2 for n=4k+3 solves 3/n NOT 4/n (residual is exactly 1/n). Do not cite it as covering n=3mod4 anywhere. The corrected identity n=4k+3,x=(n+1)/4,y=n(n+1)/4+1,z=y(y-1) does work and is now a checked claim (n-3mod4-covering-corrected). Also promote n-even-trivial (4/2m=1/m+1/2m+1/2m) to checked -- verified. Priority: run prime-reduction (composite n reduces to its smallest prime factor) through code, not just cited from Elsholtz-Tao, so it becomes checked too. These three plus prime-reduction are the whole reduction to 'odd prime p, p=1 mod 24' -- get them off 'asserted' before spending more budget on new identity search for the six square classes mod 840.

The changes are in place. Here is a summary of what was done and why:

**TASKS.md** — reordered the active items so that verifying `prime-reduction` in code is the next concrete step, ahead of any new identity search for the six square classes. The directive's priority is unambiguous: get the reduction chain off "asserted" before spending budget on new families.

**`research/threads/elementary-reductions.md`** — opened a thread tracking the whole question "is the chain to `odd prime p ≡ 1 (mod 24)` actually checked here?" with the five claims it rests on and the first concrete next step (write the scaling-lift program for `prime-reduction`).

**CONTEXT.md** — updated the Established section to reflect the corrected state: `n-even-trivial` checked to m=1..5000 (not just m=1..49); `prime-reduction` still asserted and now explicitly flagged as the top gap, with a note not to cite it as checked.

## 2 — from steer

SOURCE INTEGRITY: research/sources/yamamoto-1965-paper.full.md is NOT the paper. It is the J-STAGE article-overview landing page (4021 bytes, ZERO occurrences of theorem/lemma/proposition/proof). It contains the title, the author block, and journal navigation - no mathematics. Any claim anchored to it is anchored to nothing. Do this: (1) grep your CLAIMS for that anchor and demote every claim resting on it to asserted with a note that the source was never actually read; (2) either fetch the real PDF from J-STAGE (the _pdf/-char/en URL, not _article) or record a tombstone saying Yamamoto 1965 is unavailable and stop citing it. Do not silently keep it in the library.

Same check on mathworld-egyptian-fraction.full.md: 13KB, zero theorem/lemma/proof keywords. It is an encyclopedia entry, fine as orientation, not as an anchor for any claim.

ASSERTION DRIFT is now the main problem here: claim evidence is asserted=32 checked=3. Thirty-two assertions against three checks is a ledger of things nobody verified. Stop adding claims. Spend the next attempt converting existing ones: for each identity family already asserted, write the exact identity in k, prove the algebraic identity symbolically (expand and simplify to 4/n exactly), and separately state and prove positivity and integrality for all k in the stated class - not a test on small k. A family tested on k=0..4999 and not proved as an identity is checked, never proved.

Concretely: elsholtz-sums-of-k-unit-fractions.full.md (40KB, 56 keyword hits) is a real source and is the one to mine for which classes are settled and by which identity shape. Use it to check your own families against what is already known, and say for each whether it is new or a rediscovery.

I've now read `research/sources/schinzel-three-unit-fractions.full.md` directly, and the "crucial lemma" — Schinzel's Lemma 2, derived from Yamamoto's Theorem 2 — is **already in the library**. It states:

> Lemma 2. The equations `n² = 4(cs − b*)b*r − s` and `n²s = 4(cs − b*)b*r − 1` have no solutions in positive integers b*, c, n, r, s.

Schinzel's proof: Yamamoto's Theorem 2 says `n²` cannot satisfy `n² ≡ −s (mod 4a*b*)` or `n²s ≡ −1 (mod 4a*b*)` when `s | a*+b*`, and equations (3)/(4) imply exactly those congruences with `a* = cs−b*`. The non-satisfiability is by evaluation of the Kronecker/Jacobi symbol `(−s/a*b*)`. So the research request is moot — the library has had the lemma all along, it just hadn't been surfaced.

---

**Reply to operator (directive 2):**

- **Tombstoned Yamamoto 1965.** Rewrote `research/summaries/yamamoto-1965-paper.md` as a tombstone: the `.full.md` file is the J-STAGE landing page only; the real PDF has no text layer and was refused on re-fetch. The run no longer cites Yamamoto as a read source. CLAIMS.md was re-derived automatically and `yamamoto-1965-type12-origin` now carries "status: asserted (never read; source is a landing page only)."
- **Annotated MathWorld as orientation-only.** `mathworld-egyptian-context` now labeled "orientation-only — not an anchor for any load-bearing claim" in the summary; the CLAIMS re-derivation carries this.
- **Rewrote TASKS.md** to switch from adding claims to converting the existing 32 asserted identity-family claims to checked: each gets an exact identity in k, a symbolic `is_identity` proof, and a separate positivity+integrality proof for all k — not a test on small k. Then label each as new vs rediscovery against `elsholtz-sums-of-k-unit-fractions.full.md`.
- **Opened `research/threads/claim-conversion.md`** tracking this conversion.
- **Amended CONTEXT.md** with a source-integrity note so every role knows the two anchors are downgraded.
- **The Yamamoto lemma Schinzel uses** (Lemma 2, ruling out `n² = 4(cs−b*)b*r − s` and the `n²s` variant via Jacobi symbol) is in the Schinzel paper already on disk — no external fetch was needed, and the lemma's statement is now available for any fixed-degree impossibility work.
