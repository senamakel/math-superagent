# Factor-balanced S-adic languages (Poirier–Steiner) — Morse–Hedlund balanced-blocks source

<!-- source: https://hal.science/hal-03869990v2/document | converted from PDF -->

**Digest replaced.** Léo Poirier & Wolfgang Steiner, "Factor-balanced S-adic languages",
Theoretical Computer Science 998 (2024) 114535, hal-03869990.

## What it establishes (relevant to PE1006)

The abstract and intro attribute to **Morse and Hedlund (1940)** the following fact,
which is exactly the classification the open request `precise-sourced-statement-c1ec` asks
for:

> each block of length `n` in a **Sturmian sequence of slope α** has `⌊nα⌋` or `⌈nα⌉`
> occurrences of the letter that has frequency `α` (equivalently the difference between the
> number of occurrences of a letter in blocks of the same length is at most 1 — the
> "letter-1-balanced" / balanced property).

Combined with the Sturmian factor-complexity fact (exactly `n+1` distinct length-`n`
factors), the balanced-blocks condition is a **necessary** restriction on the factors.
**It is NOT a bijection / enumeration:** the set of balanced binary words of length `n`
with `⌊nα⌋` or `⌈nα⌉` ones strictly contains the factor set and has more than `n+1`
elements (refuted by computation, `research/approaches/balanced-factors-claim-attack.md`:
k=3 gives 6 candidate words vs 4 factors; k=4 gives 10 vs 5). The factor set is
enumerated by the Perrin–Restivo consecutive-factor rule, not by the balanced-count
paraphrase.

For the Fibonacci word (slope `α = 1/φ² = (3−√5)/2`, the frequency of the letter `1`),
every length-`k` factor has `⌊k/φ²⌋` or `⌈k/φ²⌉` occurrences of `1` — necessary only.
Claim `PE1006-factors-one-count-necessary` (governing-theory note) is the surviving
correct statement.

The paper's own content (balance of S-adic substitution languages, factor-balance) is
beside the point for PE1006; the value is the faithfully quoted Morse–Hedlund balanced-
blocks statement that fills the request.

Full text: `research/sources/morse-hedlund-balanced-blocks-floor-alpha.full.md`.
