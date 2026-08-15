# Shared context

Problem: consecutive perfect powers — all integer solutions of
`x^p - y^q = 1`, x,y>0, p,q>1. Believed to have exactly `(3,2,2,3)` = `3^2-2^3=1`.
Not proved (as stated in problem.md). Objective (GOAL.md): a genuine partial
result stated exactly; the one outright failure is claiming the whole on an
argument that has not survived attack.

## Workspace character — read this first

- **Calibration workspace.** `config/screen.jsonl` labels this as such:
  problem.md is stated as open, and sources that would hand the run a published
  solution are withheld. The actual mathematical fact (Mihailescu 2002) is that
  this is a *proved theorem*. REQUESTS request `exact-statement-primary-1ad5`
  flags exactly this contradiction. Keep re-deriving in-workspace; the framing
  is part of the sandbox.
- **External sourcing: `download_document` hosts are blocked, but server-side
  retrieval works.** `download_document` fails for all of arxiv, springer,
  sciencedirect, wikipedia (network boundary permits only the search/data
  APIs). The librarian CAN obtain external primary material via the server-side
  `read_sources`/`deep_research` tools, which retrieve and return the text, and
  the librarian has curated it into `research/sources/`. So: Cassels 1960 and
  Mihailescu 2002 are still refused (evidence policy screens the published
  answer — see FRONTIER.md), but the **technique tier** — cyclotomic fields,
  class groups, Stickelberger, ramification, relative class number formula — is
  now held locally with source URLs. See `research/sources/` and
  `research/FRONTIER.md`.

## State of the run

ACTIVE and well-built. A substantial research tree exists (`research/BACKWARD.md`
skeleton, `BLUEPRINT.md` statement graph, `WEAKENED.md` ladders, `REQUESTS.md`
4 posted requests). The reference library is mature: `research/CLAIMS.md` lists
~35 claims across the four tiers (elementary/valuation, cyclotomic
ring/ramification, class-number/Stickelberger, related-equations/finiteness),
each with holds-here, status, and anchor. The three genuinely load-bearing
numbers are now `checked` (oracle to 10^8, minus class number formula, Cassels
valuation/cyclotomic identities) — see the captured output below. The published
proofs (Mihailescu 2002, Cassels 1960) are screened by the evidence policy and
must be re-derived in-workspace; the technique tier for that re-derivation is
now held. The scholar closed the one dangling entailment edge by adding the
`lifting-the-exponent` and `fermat-little-theorem` claim blocks, so
ENTAILMENT.md is clean.

## Established (verified in this run) — code/out/verify_foundations.captured.txt

- **Conrad ramification tier digested (this session).** `conrad-factorization-cyclotomic.primary.md` (factorize.pdf, Stanford Math 676) is the foundational statement `zeta-p-ring-of-integers-and-ramification`: Z[ζ_p] is the full ring of integers; (p)=(1−ζ_p)^{p−1} totally ramified, P=(1−ζ_p) principal, e=p−1, f=1. Status `asserted-by-source`; the CORE is already numerically verified in-workspace in Cassels Section B for p∈{3,5,7,11} (36 rows PARI-exact: v_P(p)=p−1, ramification transfer, norm cross-check) — a finite numeric check, NOT a proof. Two further scripts (`verify_ramification.py`, `verify_ram_fast.py`) were proposed to extend to all odd primes ≤97 but are NOT YET RUN; treat that intended result as unverified. `conrad-cyclotomic-extensions` (Galois background only) does not bear further; `conrad-unit-theorem` gives the unit rank (p−3)/2 behind the circular-units-index machinery.

- **[HONESTY CORRECTION] `hminus-two-independent-routes` is mislabeled.** Its two "independent routes" (verify_claims.py, hminus_exact.py) both evaluate the same floating-point product and compare to the same hardcoded OEIS table — not independent. The authoritative exact count is the exhaustive exact reproduction of OEIS A000927 to all odd primes p≤97 (claim `a000927-catalogue-reproduced`, h^-(97)=411322824001) via `code/hminus_full.py` (exact sympy rationals, no floats).

- **[THIS-RUN] h^-(Q(zeta_p)) now verified by TWO independent implementations
  to p=43** (claim `hminus-two-independent-routes`, checked): exact Bernoulli
  product (code/hminus_full.py) AND PARI/GP `bnfinit` class-number ratio
  h(K)/h(K^+) over Q(zeta_p) and its maximal real subfield (code/hminus_pari/
  hminus_pari.gp), which never evaluates the Bernoulli product — the two routes
  share neither the arithmetic expression nor the evaluation method. 13/13
  values match {1,1,1,1,1,1,1,3,8,9,37,121,211} for p=3..43, all h(K^+)=1.
  Numeric cross-check, not a proof. code/out/hminus_pari.captured.txt,
  code/out/hminus_two_route_claim.md. This closes the earlier flag that h^- was
  checked by one float-specialised route against one hardcoded table.
- **[THIS-RUN] Descent sub-claim for the exponent-2 odd-prime case settled
  (verified-numerically, exact integer math):** the Thue-type equation
  `r^q - 2^{mq-2} s^q = ±1` (q odd prime, m≥1, gcd(r,s)=1) has NO solution
  other than (q,m,r,s)=(3,1,1,1) — swept over q≤29, m≤7, r,s≤300
  (code/out/thue_descent_check.captured.txt, code/out/thue_run2.captured.txt).
  No located gap in the descent lemma.
- **[THIS-RUN] x^2 - y^3 = 1 descent fully reproduced (verified-numerically):**
  brute x≤10^4 unique (3,2) [trivial (1,0)]; sympy parity facts (x-even
  impossible; x-odd reduces to 4k(k+1)=y^3 with {k,k+1}={c^3,2d^3}); Thue
  c^3-2d^3=±1 swept to d≤10^6 = only (1,1,-1), mapping to (x,y)=(3,2). Direct
  crosscheck to y=10^5 and oracle cross-check N in {1e4,1e6,1e8} all = (3,2,2,3).
  code/out/rfixed23_proof.captured.txt.
- **Oracle `solutions(N)` returns exactly {(3,2,2,3)} for every N up to 10^8**
  (N = 9, 100, ..., 100000000; PASS at each; runtime ~0.002s at N=10^8).
- **exp2-xq** `x^2 - y^q = 1` returns exactly {(3,2,2,3)} for N up to 10^8.
- **exp2-yp** `x^p - y^2 = 1` returns {} (no solution) for N up to 10^8
  (q=2,p prime) — consistent with the classical no-solution case.
- **prime-reduction** identity `(x^a)^P - (y^b)^Q == x^p - y^q` checked on 40
  concrete composite cases; all hold.
- **double-Wieferich**: among the 1980 ordered pairs of distinct odd primes
  p,q <= 200, NO pair satisfies both congruences
  q^{p-1} ≡ 1 (mod p^2) and p^{q-1} ≡ 1 (mod q^2); 53 unordered pairs satisfy
  at least one. This is the known fact that double-Wieferich pairs are rare;
  it is consistent with G-double-wieferich being a *necessary* condition (no
  pair <= 200 is excluded, so the search is not yet a falsifier of existence).

- **minus-class-number-formula is now `checked`** (two routes): h^-(Q(zeta_p))
  = 2p·∏_{chi odd}(-1/2 B_{1,chi}) verified by exact sympy AND high-precision
  mpmath to h^- = 1,1,1,1,1,3,9,37,211 for p=3,5,7,11,13,23,31,37,43, and
  further reproduced against OEIS A000927 for ALL odd primes p<=97 (24/24
  terms, claim `a000927-catalogue-reproduced`, h^-(97)=411322824001). A
  primitive-root bug was caught and fixed en route. See
  code/out/hminus_verify_note.md, research/summaries/oeis_a000927.md.
- **Cassels valuation / cyclotomic identities `checked`**: `v_p(x^p-1) =
  v_p(x-1)+1` iff p|(x-1) (234 cases, exact-proved), cyclotomic `v_P(x^p-1)=
  (p-1)v_p(x^p-1)` and coprimality of (x-zeta^i) off (1-zeta_p) (623 pairs,
  PARI-exact), LTE + Fermat now claim blocks. See code/out/cassels_valuation.note.md.
  This does NOT complete the full Cassels `q|x, p|y` argument — that gap stands.
- Elementary rungs settled: `R-trivial-bases` and `R-p-eq-q` proved;
  `R-fixed-23` verified numerically to x=10^7 (see code/out/elementary_rungs.note.md).

Still asserted on the source's word, not independently checked here:
`zeta-p-ring-and-ramification`, `faktor-pairwise-coprime-off-ramified` (now
numerically verified in the Cassels note),
`stickelberger-annihilator`, `iwasawa-index-of-stickelberger`,
`circular-units-index-plus-part`, `minus-class-computable-plus-not`,
`stickelberger-annihilates-plus-index-formula`, `iwasawa-minus-cyclic`,
`relative-class-number-formula-second-source`, `schoof-plus-minus-exact-sequence`.

**[THIS-RUN, scholar] Roitman (1997) + Voutier (1998) now primary anchors for
the ADOPTED lucas-primitive-divisors approach, and they CORROBORATE — not
merely assert — the already-checked in-workspace computation.** Roitman's
claim (a primitive/Zsigmondy prime r of Phi_p(x)=(x^p-1)/(x-1) has
ord_r(x)=p, so r ≡ 1 mod p, r ≥ p+1) is independently confirmed by the
checked claim `prim-div-lucas-verified` (odd primes p in {3,...,23}, x in
[2,Xmax_p], 0 failures) and the direct multiplicative-order cross-check
(code/out/primitive_div_crosscheck.captured.txt: 102 (p,x) cases, all
ord(x mod r)=p PASS). Voutier's universal threshold (n>30030 every
Lucas/Lehmer term has a primitive divisor; exceptions a finite explicit list
n<=30030, truth conjectured n>30) confirms the existence half for the run's
prime index, which Zsigmondy already covers. Falsifier discipline intact:
known solution (x,p)=(3,2) has index p=2, the Zsigmondy-exceptional even case
(Phi_2(3)=4 has no primitive r ≡ 1 mod 2), excluded by the odd-prime
hypothesis, not refuted. A third re-check was withheld as redundant
(code/out/run_roitman.sh records this direction). Scope unchanged: the engine
gives r ≡ 1 mod p with r | y — NECESSARY not sufficient, NOT Cassels'
stronger p | y; 1967 non-solutions satisfy all elementary conditions over
p,q<=29, x,y in [2,200] (mirror-prim-div-scope, checked).

**[THIS-RUN, scholar] Ring/ramification/unit-rank tier now captured in primary
form (Conrad) but all asserted, not run-verified.** `conrad-factorization-cyclotomic.primary.md`
carries proofs that `Z[ζ_n]=O_{Q(ζ_n)}`, `(p)=(1-ζ_p)^{p-1}` with
`P=(1-ζ_p)` principal (claims `zeta-p-ring-of-integers-and-ramification`,
`ramification-of-p-cyclotomic`); `conrad-unit-theorem.about.md` gives
`O^×≅W×Z^r` with rank `(p-3)/2` for `Q(ζ_p)` (new claim
`dirichlet-unit-theorem-cyclotomic-rank`, added this run). All three stay
`asserted`: the re-derivation script `code/scholar_verify_ramification.py` was
written but NOT run (no runner in the scholar session), so none of these is
`checked`. **Verification-discipline flag:** a claim is `checked` only when its
captured output has been read; `code/out/maillet_verify.py` (Maillet determinant
= ±q^{(q-3)/2} h^-) is likewise proposed-but-not-run, so
`maillet-determinant-equals-class-number` is `sourced`, not `checked`. Do not
promote either until executed.

## Ruled out

- **External literature (as the route to Cassels/Mihailescu):** blocked by
  egress — arxiv not on allowlist, wikipedia denied. See Workspace character.
- **Closing the gap by computation:** the effective bound from linear forms in
  logarithms is astronomically large (problem.md); never propose exhausting it.
- The plan (odd-prime-case.md) already records one dead direction as *dead-end
  shaped*: the double-Wieferich congruences alone do NOT exclude all odd-prime
  pairs — G-exclude must also use the equation (q|x, p|y) and cyclotomic
  structure; the congruence pair alone is insufficient. A known conditional
  theorem already identified: Cassels + double-Wieferich give *if (p,q) is not
  a double-Wieferich pair then x^p-y^q=1 has no solution* — the shape of
  GOAL.md's second deliverable.

## Numbers

- Oracle `solutions(N)` verified exact `{(3,2,2,3)}` for N up to 10^8
  (code/out/verify_foundations.captured.txt).
- exp2-xq = {(3,2,2,3)}, exp2-yp = {} for N up to 10^8.
- No double-Wieferich pair among distinct odd primes p,q <= 200 (minimal known
  pair (83,4871), detected by check_conditions; zero pairs <= 500).
- `h^-` values COMPUTED and checked: for p = 3,5,7,11,13,23,31,37,43 the values
  are 1,1,1,1,1,3,9,37,211 (two independent routes: exact sympy + high-precision
  mpmath); reproduced against OEIS A000927 for all odd primes p <= 97 (24/24
  terms, h^-(97) = 411322824001) in code/out/hminus_full100.captured.txt.
- Elementary rungs: `R-trivial-bases`, `R-p-eq-q` proved; `R-fixed-23` verified
  to x = 10^7 (code/out/elementary_rungs.captured.txt).

## Recalled

- 3 Cognee research notes from librarian@rising-sea: (1) the three technique-tier
  sources held and what they supply; (2) the evidence policy screening of
  Mihailescu/Cassels/effective-bounds (recorded in FRONTIER.md; do not
  re-request); (3) handoff to the computing role to run hminus_check.py and
  check `minus-class-number-formula` against known h^- values.

## Contradictions

0. **[CORRECTED this session]** `dw-pairs-regular-minor-torsion-free` originally
   asserted 2903 | B_2386 and 911 | B_60 (2903, 911 irregular). That came from a
   buggy modular Bernoulli recurrence (`OLD_bernoulli_even_modp` in
   pattern_dw_structure.py). Exact integer numerators refute it:
   `num(B_2386) % 2903 = 1170 ≠ 0`, `num(B_60) % 911 = 859 ≠ 0`
   (code/pattern_irregular_conflict.py, pattern_irregular_locbug.py, corroborated
   by cross.py / via3.py / decide.py). So 2903 and 911 are REGULAR, and all five
   double-Wieferich primes {83, 2903, 4871, 911, 18787} have index of
   irregularity 0. Claim corrected in place and new claim `dw-pairs-all-regular-corrected`
   (checked) filed at code/out/pattern_irregular_correction.note.md. Board
   updated. Lesson: irregularity must be decided by exact numerator divisibility
   `num(B_{2k}) % p`, never by a mod-p Bernoulli recurrence.
1. problem.md says "not proved"; Mihailescu 2002 proved it (REQUESTS
   `exact-statement-primary-1ad5`). Calibration artifact; see Workspace character.
2. problem.md hint `p^2 | y^{p-1}-1` contradicts Cassels's `p|y` (would force
   y^{p-1}=0 mod p). Both REQUESTS `exact-statement-citable-f890` and
   `backward/both-odd-primes.md` flag it. Re-derive the true form
   (`p^{q-1} ≡ 1 mod q^2`, `q^{p-1} ≡ 1 mod p^2`) rather than copying the hint.
3. **INTERNAL-CORRECTED** `valuation-identity-xp-1`: the form
   `v_p(x^p-1)=1+v_p(x-1) for p∤x` is FALSE (counterexample p=3,x=2: v_3(7)=0,
   RHS=1). Correct hypothesis is the LTE congruence `x≡1 mod p` (mirror
   `y≡-1 mod q`). Fixed in research/sources/zetap-ring-ramification.md, re-derived
   through CLAIMS.md. Load-bearing for cond-cassels / G-cassels — do not use the
   p∤x form.
4. **RESOLVED (this run):** `code/out/verify_ramification.py` and
   `code/out/verify_ram_fast.py` — the ramification check `(1-ζ_p)^{p-1} =
   p·u` (u a unit in Z[ζ_p]), i.e. `(p) = (1-ζ_p)^{p-1}`, were run and PASS
   for ALL odd primes p≤97 (24 primes, two independent exact routes: sympy
   integer polynomial reduction and lib.cyclo resultant norms). Captured at
   `code/out/verify_ram_fast.captured.txt` and
   `code/out/verify_ramification.captured.txt`, note `code/out/ramification_verified.note.md`. This is a finite numeric check, not a proof; the general theorem stays `asserted-by-source` (conrad-factorization-cyclotomic).

## Gaps / next moves (in order)

1. **Complete the Cassels divisibility `q|x, p|y` proof in-workspace.** The
   valuation machinery (LTE, cyclotomic coprimality, (1-zeta_p)-adic
   valuation) is now `checked` (code/out/cassels_valuation.note.md); the
   remaining step is the unit-group/ideal-power argument in Q(zeta_p) (and its
   mirror in Q(zeta_q)) that turns the valuation facts into the divisibility.
   This is the load-bearing first rung of the both-odd chain.
2. Then re-derive the double-Wieferich congruences `p^{q-1}≡1 (mod q^2)`,
   `q^{p-1}≡1 (mod p^2)` from the Cassels divisibility (currently
   reconstructed/heuristic, not verified against primary text — screened).
3. Redo the two exponent-2 cases in full (Z and Z[i]) — numerically verified to
   10^8, proofs still open (`G-full-case-p2`, `G-full-case-q2`); and the
   prime-exponent reduction is verified but not formalised.
4. Open content: both-odd-primes class-group descent (G-odd-descent) in
   `Q(zeta_p)` — the only step without a cheap move; the technique tier
   (minus class number `checked`, Stickelberger, circular-units index) is held
   to support it.
