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

ACTIVE. A substantial research tree exists (`research/BACKWARD.md` skeleton,
`BLUEPRINT.md` statement graph, `WEAKENED.md` ladders, `REQUESTS.md` 4 posted
requests). The reference library is being built: `research/CLAIMS.md` now lists
8 claims, all `asserted` (one, `minus-class-number-formula`, `unchecked`), from
the technique-tier sources in `research/sources/`. Coder has already run the
oracle and the double-Wieferich search — see the captured output below. The
published proofs (Mihailescu, Cassels) are screened by the evidence policy and
must be re-derived in-workspace; the technique tier for that re-derivation is
now held.

## Established (verified in this run) — code/out/verify_foundations.captured.txt

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

Not yet verified: the relative class number formula `minus-class-number-formula`
(the scaffold exists in code/out/hminus_check.py; needs execution), and every
claim under `research/sources/` is `asserted` on the source's word, not checked.

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
- No double-Wieferich pair among distinct odd primes p,q <= 200.
- `h^-` values NOT yet computed in-workspace; `minus-class-number-formula` is
  `unchecked` (code/out/hminus_check.py scaffold awaits execution).

## Recalled

- 3 Cognee research notes from librarian@rising-sea: (1) the three technique-tier
  sources held and what they supply; (2) the evidence policy screening of
  Mihailescu/Cassels/effective-bounds (recorded in FRONTIER.md; do not
  re-request); (3) handoff to the computing role to run hminus_check.py and
  check `minus-class-number-formula` against known h^- values.

## Contradictions

1. problem.md says "not proved"; Mihailescu 2002 proved it (REQUESTS
   `exact-statement-primary-1ad5`). Calibration artifact; see Workspace character.
2. problem.md hint `p^2 | y^{p-1}-1` contradicts Cassels's `p|y` (would force
   y^{p-1}=0 mod p). Both REQUESTS `exact-statement-citable-f890` and
   `backward/both-odd-primes.md` flag it. Re-derive the true form
   (`p^{q-1} ≡ 1 mod q^2`, `q^{p-1} ≡ 1 mod p^2`) rather than copying the hint.

## Gaps / next moves (in order)

1. **Run `code/out/hminus_check.py`** (computing role) and mark
   `minus-class-number-formula` checked if it reproduces 1,1,1,1,1,3,9,37 for
   p=3..37. This is the only unchecked claim and the most load-bearing number
   for check_conditions.
2. **Close `R-trivial-bases`** (x,y >= 2: x=1→y^q=0 excluded, y=1→x^p=2
   impossible) — current weakest rung in `research/WEAKENED.md`, one line.
3. Redo the two exponent-2 cases (Z and Z[i]) and the prime-exponent reduction
   in-workspace — the foundation everything is calibrated against.
4. Re-derive Cassels (p|y, q|x) by in-workspace valuation computation using the
   held machinery (valuation identity, coprime ideals off (1-zeta_p)); then the
   double-Wieferich conditions. Cannot be fetched — evidence policy screens the
   published proof.
5. Open content: both-odd-primes class-group descent (G-exclude / G-odd-descent)
   in `Q(zeta_p)` — the only step without a cheap move; the technique tier
   (Stickelberger, minus class number, circular units index) is now held to
   support it.
