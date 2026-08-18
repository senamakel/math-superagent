# Scholar verification: universal-Euclidean monoid primitive (geometric second moment)

**Status**: VERIFIED against full texts this cycle. Cognee memory server is down
(health-check timeout, `remember_memory` refused), so this durable finding is
persisted here instead of in memory. Store to Cognee once the server recovers.

## Verified statements

Three independent full texts carry the same Euclidean recursion and monoid
model: fhq cnblogs 万能欧几里得 (`[[universal-euclidean-geometric-weight-fhq.full]]`),
LOJ138 mizu164 (`[[loj138-universal-euclidean-floor-moments.full]]`), and
OI-wiki universal Euclidean / Euclidean-like algorithm
(`[[oi-wiki-universal-euclidean-floor-sum.full]]`, `[[oi-wiki-euclidean-like-algorithm-en.full]]`).

### The Euclidean recursion (string form; U = horizontal/floor step, R = vertical/contribution step)

For y = ⌊(p·t+r)/q⌋, t = 0..n, the operation string has n R's with the i-th R
preceded by ⌊(p·i+r)/q⌋ U's. Let m = ⌊(p·n+r)/q⌋:

```
solve(p,q,r,n,U,R):
  if m == 0:            return R^n
  if p >= q:            return solve(p mod q, q, r, n, U, U^(p//q) * R)
  else:                 # flip / reciprocal
    return R^((q-r-1)//p) * U * solve(q, p, (q-r-1) mod p, m-1, R, U) * R^(n - (q*m-r-1)//p)
```

Each round is a Euclidean step (p,q) -> (q, p mod q): total O(log max{p,q})
merges, n never a loop bound. This is the go/no-go fact for k=10^18.

### The geometric second-moment monoid (directive-4 spec)

Node state (segment-relative, mod M): dR (R-count), dU (U/floor-delta count),
w = z^dR (geometric weight across the segment), S0 = Σ z^t, S1 = Σ z^t·y,
S2 = Σ z^t·y², with t the R index and y = floor value within the segment.

Compose left l then right r:

```
dR = l.dR + r.dR      dU = l.dU + r.dU        w  = l.w * r.w
S0 = l.S0 + l.w * r.S0
S1 = l.S1 + l.w * (r.S1 + l.dU * r.S0)
S2 = l.S2 + l.w * (r.S2 + 2*l.dU*r.S1 + l.dU^2*r.S0)
```

Identity: all zeros, w = 1. The dU shifts carry floor values across the
segment boundary — the sole place the primitive goes wrong; test it hard.

**Why these formulas are correct (checked against LOJ138's general rule).** The
LOJ138 source gives the binomial composition rule for a node carrying
(cnt1=cntU, cnt2=cntR, ans[a,b] = Σ (y+·)^a (x+·)^b):

    C.ans[a,b] = A.ans[a,b] + Σ_{i=0..a} Σ_{j=0..b} C(a,i) C(b,j)
                 * A.cnt1^i * A.cnt2^j * B.ans[a-i, b-j]

Applied with geometric weight z^t where t is the R index and moments of the
floor argument y only up to degree 2, this specialises exactly to the S0/S1/S2
compose rules above (the w_A = z^{dR_A} factor is the geometric analogue of the
binomial shifts A.cnt2^j). So directive-4's monoid is the verified case of a
documented general construction, not an ad-hoc steer.

### Cautions

- The fhq note's monoid is concrete over mod 998244353; re-implement over
  M = 101001001 with z = 10^{-1} mod M (valid: gcd(10,M)=1; M odd, not ≡0 mod 5).
- The monoid requires the carried quantities be linear-difference in the floor
  argument / powers up to 2. Ψ(k) is quadratic in floors — inside closure.
  Terms like x^{⌊·⌋} with floor in the *exponent* are outside; none arise here.
- Exact integer arithmetic throughout — no floating point (fhq's C++ `div`
  macro uses long double but the recursion is integer; the solver must not).

## What it lets the run do

Gives the O(log) primitive of directive 4 a source-verified correctness
statement, closing requests `citable-name-treatment-0c91`,
`citable-precise-statement-600d`, `citable-precise-statement-d2e7`. The solver
can implement the monoid from these formulas and validate against brute /
mech_psi without re-deriving a known algorithm.

## Claim block

```claim
id: monoid-composition-formulas-verified
statement: For the geometric second-moment floor-sum monoid over a Euclidean path (n R's, i-th R preceded by floor((p·i+r)/q) U's), composing segment l then r by dR=l.dR+r.dR, dU=l.dU+r.dU, w=l.w·r.w, S0=l.S0+l.w·r.S0, S1=l.S1+l.w·(r.S1+l.dU·r.S0), S2=l.S2+l.w·(r.S2+2·l.dU·r.S1+l.dU²·r.S0) is correct to a second moment of the floor argument with geometric weight z^t, and the Euclidean recursion solves it in O(log max{p,q}) merges with n never a loop bound.
hypotheses: y=floor((p·t+r)/q) integer floor; t the R index; w=z^dR with z a fixed ring element (here 10^-1 mod M); carried quantities linear-difference in y / powers ≤ 2
holds-here: yes
status: proved
bearing: this is the O(log) primitive for Psi(k) at k=10^18; implements directive-4's monoid with a source-verified (not ad-hoc) correctness statement
anchor: research/sources/universal-euclidean-geometric-weight-fhq.full.md
follows-from: governing-universal-euclidean
answers: citable-name-treatment-0c91, citable-precise-statement-600d, citable-precise-statement-d2e7
```

The S1/S2 composition is the geometric-weight specialisation of the LOJ138
binomial rule C.ans[a,b] = A.ans[a,b] + Σ C(a,i)C(b,j)·A.cnt1^i·A.cnt2^j·B.ans[a-i,b-j].
The S0 = l.S0 + l.w·r.S0 rule gives the plain (count, Σz^t) against a direct
loop.

## Note on memory

`remember_memory` refused: "memory server cannot index right now." Same
documented limitation as prior cycles. Durable records are on disk in this note
and the per-source digests; synced to Cognee when the server recovers.
