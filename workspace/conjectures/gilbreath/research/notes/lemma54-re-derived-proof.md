# Granville Lemma 5.4 — RE-DERIVED and PROVED (even domain)

## Status

`id: lemma54-re-derived-proof`
`status: proved` (this run, exact-integer machine verification + clean parity argument)
`holds-here: yes`
`bearing:` Route B (Granville nu_2) primary; this is the lemma the ν_2 reduction
depends on. Previously the published proof did NOT establish it — the δ=0 case
("unless delta_{k-1}(q_n)=0... success is guaranteed") was discarded without
argument, and it occurs on 100% of real columns (50% of block entries).
This re-derivation handles δ=0 as a normal closure case and proves the lemma
for the even domain, which is exactly the prime case.

## The abstract theorem (proved)

Let `eps = (eps_1..eps_L) in {0,2}^L` be the maximal `{0,2}` suffix ("0-2 cycle")
of the previous right diagonal `delta(q_{n-1})`; `nu_2 = #{k : eps_k = 2}`.
The new diagonal orbit is `delta_0 = v`, `delta_k = |delta_{k-1} - eps_k|`.

> **Theorem (even domain).** If `v` is even and `v <= 2*nu_2 + 2`, then the
> orbit lands in `{0,2}` by step `L` (i.e. `delta_L in {0,2}`) and stays in
> `{0,2}` forever.

**Proof (parity-preserving descent).** The three local transition rules are
exact (verified by |a−b| over all relevant pairs):
- `eps_k = 0` ⟹ `delta_k = delta_{k-1}` (pass-through);
- `eps_k = 2`, `delta_{k-1} >= 2` ⟹ `delta_k = delta_{k-1} - 2` (descent by 2);
- `eps_k = 2`, `delta_{k-1} = 0` ⟹ `delta_k = 2` (bounce into {0,2};
  this is Granville's discarded "exception", here a normal closure case).

Since `eps_k in {0,2}` is even and `v` is even, induction gives every
`delta_k` even: `|even - even| = even`. Hence `delta_k` never equals 1; it is
always an even integer. While `delta_{k-1} >= 2`, the value either stays (ε=0)
or drops by exactly 2 (ε=2); it can never go below 0 to-be-bounced because
bounce happens when δ=0 (δ=0, ε=2 ⟹ 2, back in {0,2}). After consuming the
`nu_2` twos, `delta = v - 2*nu_2` (each 2 contributed −2), which is even and
`<= 2` because `v <= 2*nu_2+2`. An even integer `<= 2` is in `{0,2}`.
Finally `{0,2}` is absorbing under `|x - eps|`, `eps in {0,2}`:
`|0-0|=0, |0-2|=2, |2-0|=2, |2-2|=0`. ∎
A short counting form: `nu_2 >= (v - 2)/2` 2s suffice to bring an even `v`
down to `{0,2}`; the hypothesis states exactly that.

## Brute-force verification (exact integers, no floats)

- Case rules (1): all three PASS over all relevant pairs (δ=2..200004).
- Potential theorem over even v, L=1..10, all 2^L strings, v in 0..2L+4:
  24,572 (ε,v) pairs, **0 hypothesis violations, 0 closure violations — PASS**.
- Budget tightness (3): all-2s pattern, `v=2ν_2+2 → δ_L=2` (in {0,2}),
  `v=2ν_2+4 → δ_L=4` (out). **Exactly tight** for every L=1..10.
- Real primes (4): 281 diagonals (n=20..300, sieve 5e5, oracle reproduces the
  five worked rows), **281/281 satisfy `v_n <= 2*nu_2(q_{n-1})+2`**, zero
  landing-value mismatches, zero delta-dynamics mismatches, zero GC-terminal
  failures.

## Located boundary in Granville's statement

As stated over **all integers**, the lemma is **false**:
- `v = 1, eps = (2)`: `delta_1 = |1-2| = 1`, stuck at 1 ∉ {0,2}.
- reason: `|odd - even| = odd`, so an odd v stays odd forever and can never
  land in the even set {0,2}. (The published text operates on even integers;
  this is the precise reason that restriction is load-bearing.)

**Real primes are safe:** right-diagonal entries at positions ≥ 1 are all even
(parity wave: 2 is the only even prime, shape (odd, even, even, ...) is
preserved), so every real `v_n = delta_{tau_n}(q_n)` at position `n - tau_n >= 1`
is even. The proof applies unchanged to the prime case.

```claim
id: lemma54-re-derived-proof
statement: Granville Lemma 5.4 is PROVED on the even domain. Let eps in {0,2}^L be the maximal {0,2} suffix (0-2 cycle) of the previous right diagonal, nu_2 = # of 2s, and let the new diagonal orbit be delta_0 = v, delta_k = |delta_{k-1} - eps_k|. If v is even and v <= 2*nu_2 + 2 then delta_L in {0,2} and the orbit stays in {0,2} forever. Proof: parity keeps even delta even so it never hits 1; each eps_k=2 with delta>=2 reduces delta by exactly 2 (delta=0 -> 2 bounce stays in {0,2}); after nu_2 twos delta = v - 2*nu_2 <= 2 even, hence in {0,2}; {0,2} is absorbing. The delta=0 case, which Granville's published proof discards and which occurs on 100% of real columns (50% of block entries), is here handled as a normal closure case, not discarded. Budget 2*nu_2+2 is exactly tight (v=2nu_2+2 -> 2, v=2nu_2+4 -> 4, all L=1..16). As stated over ALL integers the lemma is FALSE: odd v stays odd forever (|odd-even| = odd; v=1, eps=[2] -> delta=1), a located parity boundary in Granville's statement; real prime right-diagonals are always even so the prime case is safe.
hypotheses: eps in {0,2}^L; v even; exact integer arithmetic; brute force L=1..16 (2621432 even-domain pairs, 0 violations) and separate run L=1..10 (24572 pairs, 0 violations); failing-side contrapositive non-vacuous on 30 synthetic failing columns; real primes n=20..300 all 281 diagonals satisfy v_n <= 2*nu_2(q_{n-1})+2, 0 failures
holds-here: yes (real prime diagonals are even-valued)
status: proved
bearing: Route B (Granville nu_2). Closes the demand->success leg of the nu_2 reduction (the lemma that bridges budget to success now has a valid proof for the prime domain). The supply side nu_2 > n^beta, beta > 0.525 remains the entire open content, as before.
anchor: code/gap_analysis/lemma54_verify.py, code/out/lemma54_verify.captured.txt, code/out/lemma54_failing_sisters.captured.txt, code/out/lemma54_descent_check.captured.txt
answers: lemma54-discarded-case-is-universal (the discarded-case gap is repaired here)
```

## Why this advances the run

The Route B chain (CONTEXT.md Gaps):
GC ⇔ A_k(1) ∈ {0,2} (proved) ⇔ Σ(j_i+1) ≥ k−2 (proved recharge), and Granville
Theorem 5.5 reduces it to `ν_2 > n^β, β > 0.525`. The **demand** side
`g*_n = O(n^{0.525+ε})` is proved unconditionally (BHP, claim
`bhp-demand-corollary-g-star`). The lemma that bridges budget to success —
Lemma 5.4 — had no valid proof in the ledger; it **now has one** (even-domain,
parity argument, machine-brute-forced + validated on 281 real diagonals).
The **supply** side (`ν_2 > n^β`) remains the entire open content, exactly as
before: this closes the demand→success leg, not the supply leg.

Anchor: `code/gap_analysis/lemma54_verify.py`,
`code/out/lemma54_verify.captured.txt` (EXIT_CODE=0, EXIT_STATUS=0).
