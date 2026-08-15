# Pattern-finder scan of the existing computed record

Role: pattern-recognition on data this run already produced. Every claim below
is exact over the stated bounds; each is labelled conjecture (verified over the
computed range) versus proved (the recharge identity is a theorem per memory).
No new closed form was found — the sequence tools found no low-degree
polynomial and no small constant-coefficient linear recurrence for any of the
central sequences; OEIS confirmed the block profile is A000232−1 and the
shifted/minus-one form is uncatalogued.

## 1. Recharge identity and surplus monotonicity — exact over rows 1..1000

`b_m = b_1 + Σ_{events < m}(j+1) − (m−1)`, with the event set = the 60
(2,4)-events (**43 positive-jump + 17 zero-jump stalls**). Verified **0
failures** over rows 1..1000. Using only the positive-jump events it fails — the
stalls are essential (they contribute +1 = just the −(k−1) offset).

Surplus `S_m = b_m − b_1 + (m−1)` is **nondecreasing**, strictly increasing
**exactly** at the 60 events, by `j+1` each. `S_1000 = 1270603`;
`min_m (S_m − (m−2)) = 1`, i.e. the block never drops below 2 over the record
(never anywhere near 0). This is the proved recharge theorem restated with the
exact event set; the novel check is that the zero-jump stalls must be counted.

Anchor: `code/out/blocks_depth1000.json`; `research/notes/step_law_proved.md`.

## 2. Second-entry sequence — no closed form the tools can find

`s(k) = A_k(1)` (the whole conjecture reduces to s(k) ∈ {0,2}) is a 1000-bit
string, 520 zeros / 480 ones, 468 runs, max 0-run 8, max 1-run 11, mean run
2.14. The sequence tools find **no** constant-coefficient linear recurrence
(order ≤ 12) and **no** low-degree polynomial. It is catalogued as A089582.
Consistent with (but not proof of) a Bernoulli/ergodic bit string — there is no
extractable closed form here, which is why the run's structural direction is the
block-length / event-rate / ν₂-supply route rather than the exact second-entry
sequence.

Anchor: `code/out/sequence_dump.txt`, `code/out/blocks_depth1000.json`.

## 3. Block profile — equal to A000232 − 1 (catalogue cross-check)

The run's `b` array matches `(OEIS A000232(n) − 1)` exactly for rows 1..20
(checked directly against the catalogue terms). The minus-one form itself is
uncatalogued (OEIS lookup: no match) — already recorded in run memory; do not
re-search.

## 4. Giant landing blocks — geometric description

1e9 run, 15 genuine giants. Consecutive landing-block ratios:
`2.727, 3.915, 1.354, 2.940, 1.123, 1.363, 1.917, 1.197, 1.587, 1.422, 1.492,
4.951, 1.967, 2.174`, geometric-mean 1.760/event. Geometric fit beats linear
(R² 0.9439 vs 0.7830, per `directive24`). **Description, not a proof**; matches
the run's recorded sublinear log-log slope 0.388 (landing block vs block index).

## 5. Inter-giant gaps and the regeneration ratio bound

Inter-giant gaps (1e9, 15 genuine): `[22,8,4,26,2,14,2,14,4,4,12,15,13,64]`,
max 64. `gap_i/(j_i+1) ≤ 1.2644e-2` everywhere — the tightened regeneration
target (bound holds with 2+ orders slack). OEIS: no match for the gap sequence.

## 6. ν₂ supply — the live theoretical input (Route B)

Over grid n = 50..100000: `ν₂/n ∈ [0.400, 0.540]`; implied exponent
`min = 0.766` (n=50), rising essentially monotonically to `0.940` (n=1e5); the
margin `ν₂/n^0.525` is **monotonically increasing** from 2.56 to 118.8. So
`ν₂(n) > n^0.525` — Granville's demand — holds over **every** sample with a
large and growing margin. Also `ν₂ = n/2 + O(√(n log n))` (deviations ~100×
under the LIL band). This is the supply side of Route B; it still needs a
provable prime-gap-mod-4 frequency theorem (the chebyshev approach). All
numerical.

## 7. The single Lemma 5.4 hypothesis violation is a startup artifact

Hypothesis `g*_n ≤ 2·ν₂(n−1)+2`: exactly 1 violation in 99,999 (0.001%), and
re-deriving it with `lib.rightdiag` locates it at **n = 5**: the running max gap
is already 4 while the early diagonal {0,2}-suffix has ν₂ = 0. A tiny startup
effect, not asymptotic — the only violation over ~18,000 primes.

## 8. No 'energy stored during erosion'

`corr(jump_i, gap_following) = +0.335` (positive). Big jumps are **not** followed
by short gaps — refutes any "the block stores energy during erosion" intuition,
consistent with CONTEXT's observation that giants arrive 1–13 rows after the
previous event.

## 9. No OEIS match for the derived event sequences

Inter-event gaps `[1,2,4,1,1,2,2,1,4,3,1,3,...]` — no OEIS entry. Jumps, gaps,
and landing blocks have no constant-coefficient linear recurrence (order ≤ 10/12)
and no low-degree polynomial.

## Bottom line for the run

The recharge/S-monotonicity structure (with stalls counted) and the ν₂ > n^0.525
supply bound hold **exactly over the stated bounds** — each a conjecture for the
infinite process except the already-proved recharge identity. The most
derivable regularities are (a) the ν₂ supply bound as a theorem under a
prime-gap-mod-4 frequency claim (existing approach), and (b) geometric growth of
landing blocks as a conjecture (already recorded). No new closed form existed to
be looked up or found.
