# Durable findings — PE1006 scholar digest (memory-server down)

Cognee memory server was down during this whole cycle (every `remember_memory`
failed the health check); durable findings are recorded here so the next run can
relaunch them. Each finding is source-backed and cross-checked; the numbers are
brute-oracle-verified in `code/out/`; the slope correction is hand-verified in
exact arithmetic and confirmable mechanically via `code/out/check_slope.py`.

## Cycle note — one genuine claim-block defect fixed; entailment tooling caveat

- **Fixed a malformed claim block.** `research/notes/three-distance-frequency-structure.md`
  carried claim `dir1-domain-autocorrelation` with the field written as
  `statement (steer, ...):` instead of `statement:`. The parser read it as
  having no `statement`, so the claim "claimed nothing" and was flagged by the
  claims ledger as a block that could not be read. Rewritten to a well-formed
  `statement: Directive 1's pair-correlation identity C(j,jp)=A(jp-j) holds
  ONLY at k=F_n-1 ...` (the A(d) clause now lives in the hypotheses field, where
  it belongs, so no duplication remains). It now parses and appears in
  derived/CLAIMS.md. `holds-here: unchecked` / `status: asserted` is correct —
  it is a steer-directive scope statement, recorded so the identity's domain is
  not forgotten, not a library-proved result.
- **Entailment tooling caveat (confirmed again).** The rendered `derived/ENTAILMENT.md`
  still reads "nothing to derive yet" despite `follows-from:` edges now on
  `mechanical-word-digit-rule`, `fibonacci-sturmian-complexity`, and
  `req-close-factor-complexity`. Same renderer gap as the `answers:` lines in
  the requests ledger — the edges are recorded on disk in the claim blocks
  (what CLAIMS.md consumes); the ENTAILMENT/REQUESTS *renderers* lag. Not a
  blocking gap; a `request_research` / note re-post may be needed to reflect
  closure in the rendered ledger.

## Finding 1 — the problem's word is the characteristic Sturmian word of slope 1/phi^2

The PE1006 word S (S_n = S_{n-1}S_{n-2}, S_0=0, S_1=01) is the characteristic
Sturmian word c_alpha of slope alpha = 2/(3+sqrt5) = (3-sqrt5)/2 = 1/phi^2 ~
0.38197, phi = (1+sqrt5)/2.
Sources: Perrin-Restivo Example 2 ("The Fibonacci word is the characteristic
word of slope alpha = 2/(3+sqrt5)"), research/sources/perrin-restivo-note-sturmian-words.full.md;
Berstel DLT'95 ("Its slope is 1/tau^2"), research/sources/berstel-recent-results-sturmian-words-dlt95.full.md.
Factor complexity is exactly k+1 (Morse-Hedlund; Perrin-Restivo Thm 1), the
problem's "only k+1 different Fibonacci subwords of length k".

## Finding 2 — CRITICAL: directive 2's literal slope is the complement convention

Steering directive 2 says "slope a = F(n-1)/F(n)". Under every standard Fibonacci
convention F(n-1)/F(n) -> 1/phi ~ 0.618 = the density of the OTHER letter / the
rabbit (digit-complement) word. Exact arithmetic at k=3:
  - slope 34/89 = F(n-2)/F(n) -> 1/phi^2 reproduces {001,010,100,101} = the
    problem's factor set (Psi(3) = 20302);
  - slope 55/89 = F(n-1)/F(n) -> 1/phi gives {010,011,101,110}, Psi = 22522 != 20302.
The run MUST use F(n-2)/F(n) for the mechanical-word digit rule.
Claim ledger: `steer-d2-literal-slope` (holds-here: no) contradicts
`mechanical-word-digit-rule` (holds-here: yes) — flagged in derived/CLAIMS.md.

## Finding 3 — mechanical-word construction and Psi as second moment

With slope a and intercept rho = the k+1 arc-midpoints of the circle cut at
{frac(-m a) : m = 0..k}, digit_j(x) = floor(x + (j+1)a) - floor(x + j a),
v(x) = sum_j digit_j * 10^(k-1-j), telescoping:
  v(x) = floor(x + k a) - 10^(k-1) floor(x) + 9 * sum_{j=1}^{k-1} 10^(k-1-j) floor(x + j a).
Psi(k) = sum over the k+1 reps of v(x)^2 — a second moment of a geometric
(10^j)-weighted floor sum. Evaluated by the universal Euclidean algorithm
(monoid generalisation of AtCoder floor_sum, 万能欧几里得, fhq/OI-wiki/LOJ138)
in O(log) carrying (count, sum x^j, sum x^j floor, sum x^j floor^2) mod M with
x = 10^{-1} mod M. M = 101001001; gcd(10, M) = 1 so 10 is invertible.
STATUS: the slope construction itself is ALREADY VERIFIED in-container with
exact rational arithmetic for k = 1..100 (research/notes/mechanical-slope-correction.md,
programs /tmp/mech3.py..mech6.py, /tmp/bridge.py): the k+1 mechanical words at
slope F(n-2)/F(n) equal the brute length-k factor set exactly, count k+1. The
O(log) monoid evaluation is the remaining unverified piece.

## Finding 6 — minimal oracle prefix length Lmin(k) (verified)

Lmin(k) = k + NextFib(k) - 1, NextFib(k) = least Fibonacci number > k; verified
exactly k = 1..2583, 0 mismatches (research/notes/pattern-hunt-pe1006.md).
Consequences: brute word length >= 3k is always safe; 2k is not always enough;
a fresh run should not re-derive this. Also pattern-hunt notes establish
c1(k) = # length-k factors starting with '1' = 1 + floor(k/phi^2) (verified
k=1..400 and matches A189663), and that directive 1's lag-sum reduction does
NOT extend to general k (pair-correlation is position-dependent except at
k = F_m - 1) — so the mechanical-word (directive 2) route is the only
general-k handle.

## Finding 4 — brute-oracle numbers (verified, code/out/)

Psi(3) = 20302 (factors 001,010,100,101); Psi(10) mod 101001001 = 10699667;
factor counts = k+1 for k = 1..20, stable under word extension; word length
needed >= 2k is NOT always enough (k=15 needs 35); >= 3k is safe to k=30.
Psi(1..25) recorded in code/out/psi_exact.txt.

## Finding 5 — OEIS check

Psi(1..5) = 1, 101, 20302, 2042402, 204252402 has no OEIS match; A344953 is a
different (peripheral) sequence and does not help. OEIS A003849 factor corpus
(first 1652 subwords) independently matches the problem's length-3 set
(001,010,100,101) and confirms k+1 per length — an on-disk oracle for small k.

**Librarian re-check (this cycle):** the OEIS lookup was re-run with seven
oracle-verified terms
`1, 101, 20302, 2042402, 204252402, 30445654403, 3054587854503`
(Ψ(1)..Ψ(7), from code/out/brute_oracle_results.md) — still **no OEIS entry
matches**. The sequence of Ψ-values is not catalogued; do not run the lookup
again. Structure must come from Sturmian / universal-Euclidean theory, as
recorded.

## Open items for the solver

1. Implement the universal-Euclidean second-moment monoid; check vs brute on
   k=1..150 and Psi(10) mod M = 10699667; then run at k=10^18.
2. Second independent route: directive 1's autocorrelation form at k = F_n - 1
   (note: pattern-hunt shows the lag-sum does NOT generalise to arbitrary k —
   use it only as the k=F_n-1 cross-check).
3. Cleanup: `derived/CLAIMS.md` lists `fibonacci-word-sturmian-density-balance`
   and `req-close-*` as duplicates of the governing claims; keep or merge.
4. The slope check (code/out/check_slope.py) is superseded by the verified
   k=1..100 result — no need to re-run it.