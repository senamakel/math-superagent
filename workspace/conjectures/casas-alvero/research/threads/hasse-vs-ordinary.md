```thread
question: Which derivative convention — ordinary formal derivative or Hasse derivative — do the published char-p bad-prime lists use, and which of the run's char-p results were computed under the wrong one?
status: dead
rests-on: charp-false, charp-witness-xpp1-xp, gvb-lift-and-bad-primes
blocked-by: none (all five plan steps are done)
next: closed — decision recorded in claim hasse-vs-ordinary-definitions; {2}/{3,5,7} reproduced under Hasse; char-p claims swept; Ghosh HD verification confirmed unaffected. See tasks record-hasse-ordinary-definitions, add-char0-hasse-agreement-guard, verify-badprimes-second-route, recheck-charp-claims-hasse, confirm-ghosh-hd-unaffected.
```

# Thread: ordinary vs Hasse derivatives in characteristic p

## Question
`code/out/badprimes_sn.captured.txt` ends ALL CHECKS FAILED, and two parts of
the run disagree about one fact. The ordinary-derivative S_n route computes
n=3 → [] (published {2}) and n=4 → {2,3,5,7} (published {3,5,7}); the ordinary
oracle in `code/lib/casas_alvero.py` flags x^3−x^2 over F_2 and x^4+x^2 over F_2
as counterexamples (so p=2 looks bad for n=4). The published lists disagree with
both. Which convention do the published lists use, and which of the run's
char-p results must be re-stated under it?

## The two definitions
- **Ordinary derivative** (sympy `Poly.diff`): f^(i) = d^i f / dx^i. In char p,
  i! = 0 in F_p for i ≥ p, so f^(i) can vanish identically; then gcd(f, 0) = f
  is non-constant and the hypothesis holds vacuously. This is the notion
  `is_ca` in `code/lib/casas_alvero.py` decides.
- **Hasse derivative**: H_i(f) = Σ_j C(j,i) c_j x^{j−i}, i.e. the coefficient of
  h^i in f(x+h). In char 0, f^(i) = i! · H_i(f); they agree up to a factorial
  unit. In char p the Hasse derivative stays non-degenerate where the ordinary
  one vanishes. This is the notion `is_ca_hasse` decides.

## What the held sources establish (the decision)
- **Castryck–Laterveer–Ounaïes 2012, Definition 1**
  (`research/sources/castryck2012_degree12_html.full.md` line 129): a CA
  polynomial is defined via "the j-th Hasse derivative" f_H^{(j)}, with the
  explicit note "it makes no difference in characteristic 0 or p > d−1, where
  f_H^{(j)} = (1/j!) f^{(j)}". The bad-prime lists — "p = 2 is the sole bad
  prime for degree d = 3" and "the bad primes for degree d = 4 are p = 3, 5, 7"
  (De Jong–Draisma) — follow immediately (line ~136) and are therefore **Hasse**
  lists.
- **Schaub–Spivakovsky 2023**
  (`research/sources/schaub_spivakovsky_bad-primes_2023.full.md` lines 50–53):
  H_i(f) is defined explicitly as the i-th Hasse derivative and CA is
  "gcd(f, H_i(f)) non-constant for every i".
- **Ghosh 2025** (`research/sources/ghosh2025_proof_html.full.md` lines 37–43):
  f_i is the Hasse–Schmidt derivative, and "over fields of characteristic 0 the
  two derivatives are related via f_i = f^{(i)}/i!".

**Decision: the published char-p bad-prime lists {2} (n=3) and {3,5,7} (n=4)
are Hasse-derivative lists.** Under Hasse, p=2 is good for n=4 (H_2(x^4+x^2)=1,
a nonzero constant, so gcd(f, H_2)=1) but remains bad for n=3.

## The internal contradiction this resolves
The ordinary oracle's enumeration (gcd) and the ordinary S_n route (radical
equality) disagree even with each other for n=3, p=2, because the ordinary
derivative f'' ≡ 0 there makes "shares a root with f''" vacuous, and the S_n
equation f''(r_2)=0 collapses to 0=0. Both ordinary artifacts are measuring a
*vacuity-prone* notion distinct from the literature's Hasse notion. The run
holds both conventions (`is_ca` and `is_ca_hasse` in `code/lib/casas_alvero.py`;
`sn_equations` and `hasse_sn_equations` in `code/lib/casasalvero.py`) and used
them in different places — that is the disagreement to close.

## Plan (directive 4)
1. Record the definitions and the sourced decision above as a claim
   (id `hasse-vs-ordinary-definitions`).
2. Keep `is_ca` and `is_ca_hasse` side by side (never replace); add a char-0
   agreement guard `is_ca(f,0) == is_ca_hasse(f,0)` to the oracle guard set.
3. Re-run `code/badprimes/verify_badprimes_sn.py` under Hasse (script already
   switched; capture is stale) and confirm {2} / {3,5,7}.
4. Sweep the char-p claims for ordinary-derivative vacuity — in particular the
   "f(X^p) ... all derivatives vanish" clause in `charp-witness-xpp1-xp`, and
   the refuter's TPTP encoding (ordinary, f''≡0) which must be re-stated with
   Hasse derivatives.
5. Confirm the Ghosh break verification (HD) is unaffected.

## References
- research/sources/castryck2012_degree12_html.full.md:129
- research/sources/schaub_spivakovsky_bad-primes_2023.full.md:50-53
- research/sources/ghosh2025_proof_html.full.md:37-43
- code/lib/casas_alvero.py (is_ca vs is_ca_hasse)
- code/out/badprimes_sn.captured.txt (stale ordinary capture)
