# Library acquisition cycle 2 — Williams 1976 primary anchor for the adopted approach

## What was added

| Path | What it is | Verdict |
| --- | --- | --- |
| `research/sources/williams-1976-supplement-biquadratic-reciprocity.full.md` | Williams, *On the supplement to the law of biquadratic reciprocity*, Proc. Amer. Math. Soc. 59 (1976) 19–22 (AMS PDF) | **PRIMARY** — the run previously held the supplementary law of biquadratic reciprocity only as `asserted` (Wikipedia / REU lecture notes). Now it is sourced and proved: the main law (11), the `i`-symbol (7)/(10), the `1+i`-supplement, and `(a/k)_4 = +1` for rational a,k, k odd |
| `research/summaries/williams-1976-supplement-biquadratic-reciprocity.md` | Proper digest (replaced the structural digest) | claim `williams1976-biquadratic-supplement-primary` written; anchor set |
| `code/verify_biquadratic_supplement.py` | Verification program (ready to run under `lib/` or directly) | checks `[i/π]`, `[1+i/π]`, `[-1/π]`, and derived `[2/π]=i^{-b/2}` against the definitional evaluation `α^{(Nπ−1)/4} mod π` on primary Gaussian primes |

## Why this particular source, and why now

The adopted open thread `research/threads/divisor-level-phi4p.md` and the
adopted approach `research/approaches/second-moment-character-mod16.md` both
rest on evaluating, in closed form, the quartic character `(2/(2^p+i))_4` over
the Gaussian factorization `2^{2p}+1 = (2^p+i)(2^p−i)`. The first-moment sum
`S_χ = Σ_{r|Φ_{4p}(2)}(2/r)_4` uses `[2/π]=i^{-b/2}`, and the `v2(r−1) ≥ 4`
(i.e. "not 3-Higgs") obstruction is exactly `[2/π]=+1 ⟺ r ≡ 1 (mod 16)`. All of
these were previously carried as **asserted** rows in `research/CLAIMS.md`
(`qr-supplementary-2`, `qr-char-def-and-primary`, `qr-main-law`). This primary
PDF upgrades the `1+i`-supplement and `i`-symbol components to **sourced**
(giving credibility to the compound `[2/π]` row). Fetch cost was one real
download (the author-hosted Carleton URL 404'd / refused; the AMS issue-59 URL
succeeded).

## Verification plan (execution is tool_builder/coder's)

`code/verify_biquadratic_supplement.py` computes the definitional quartic
character `α^{(Nπ−1)/4} mod π` for many primary Gaussian primes `π = a+bi`
(a odd, b even, a+b ≡ 1 mod 4) and compares it to the Williams closed forms.
Expected: all four symbols match. The property that converts this into the
mod-16 obstruction — `[2/π]=+1 ⟺ Nπ ≡ 1 (mod 16)` for primitive divisors of
`Φ_{4p}(2)` — was already verified computationally on all 71 such divisors
through p=61 (`code/out/heven_gauss_61.captured.txt`, check F2). So the primary
law + the existing computation together pin the non-3-Higgs discriminator.

## REQUESTS.md updates made

- Wall 1975 row marked RESOLVED (full text already held) — stale row removed.
- Wall-10^102 row marked RESOLVED (no such figure in the held primary; see
  `research/notes/wall-1975-bounds-and-102-claim.md`).
- New row added asking for primary verification of the supplementary biquadratic
  laws — marked RESOLVED by this cycle's Williams acquisition.
- Frei 1978 and Goto 2007 rows remain OPEN (blocked at captcha/paywall), with
  the blocked routes recorded so nobody retries the identical fetch.

## Library shape after this cycle

Encyclopedic tier, canonical head-theorem tier (Subbarao–Warren 1966, Wall
1975, Graham 1989, Wall 1987/1988), and the H_even/branch tier (Maciejewski
2026 full text) were already complete. This cycle closed the one remaining
*asserted-but-load-bearing* gap in the active analytic approach: the quartic
reciprocity supplementary law now has a primary, proved source instead of a
Wikipedia citation. The only primary-tier gaps left are Frei 1978 and Goto 2007,
both genuinely pay/robot-walled and not needed to advance the adopted divisor-
level thread (both concern the "is 3 | n forced?" question, a different listed
result from the branch this run is attacking).
