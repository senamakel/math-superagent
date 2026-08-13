# Acquisition status for sought primary sources

These files were fetched but **did not yield the primary text**, so the open
research requests they relate to remain open. Recorded so nobody re-downloads
and re-compresses the same failure.

## Frei 1978, "Über unitar perfekte Zahlen" (Elem. Math. 33 (1978) 95–96)
- `[[frei-1978-unitar-perfekte-zahlen.full]]` and `frei-1978-heft4.md` /
  `frei-1978-kleine-mitteilungen.md`: the E-Periodica landing page and the two
  cntmng pages all resolve to **"Bestätigung erforderlich" (verification
  required)** — a paywall/captcha, no article text. The three summaries are
  shells, not the article.
- **Consequence:** the OEIS-recorded Frei result (a UPN not divisible by 3 has
  `2^m | n`, `m ≥ 144`, `ω ≥ 144`, `n > 10^440`) remains **unverified against
  primary text** — exactly the OPEN row `frei-1978-full-text` in
  `research/REQUESTS.md`. This is load-bearing for the "is 3 | n forced?"
  question and must not be treated as established here.

## Goto 2007, "Upper Bounds for UPNs and Unitary Harmonic Numbers" (RMJM 37 (2007) 1557–1576)
- `goto-2007-upper-bounds.md`: Project Euclid landing page only — title,
  DOI, "PURCHASE THIS CONTENT / $25". No abstract or body captured.
- **Consequence:** the OEIS-recorded bound `ω(m) = k ⇒ m < 2^(2^k)` (credited
  to Goto 2007) remains **unverified against primary text** — OPEN row
  `goto-2007-full-text`. Do not treat the `2^(2^k)` upper bound as
  load-bearing until confirmed.

## Both: what would settle them
- Frei: primary statement of the m≥144 / ω≥144 / n>10^440 bounds for
  3 ∤ n UPNs, or a counterexample UPN not divisible by 3 below those bounds.
- Goto: the exact statement and proof of `m < 2^(2^ω(m))` for unitary perfect
  m, or a counterexample.

Nothing to remember durably; the claims they would support are not established.
