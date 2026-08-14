# PE 351 — final pattern pass: every new subsequence and modulus is a dead end

Pattern finder's last sweep (this session), run over the exact 200000-term
prefixes stored in `code/out/seq_{A063985,H,Phi,phi,cototient}.txt`
(produced by `code/out/patterns.py`, exact totient sieve). All statements are
exact over the terms supplied and nothing here is a proof of a law; each is a
negative result closing a direction.

## Confirmed (already-known structure re-verified from disk, no new content)

- H(n) = 6·A063985(n) and A063985(n) = C(n+1,2) − Φ(n) hold over all
  200000 terms on disk (prior passes; not re-derived here).
- Mod-2 parity law on each half-index subsequence: A(2k) and A(2k+1) both
  satisfy A odd iff n mod 4 ∈ {1,2} over the full prefix — i.e. the known
  period-4 law restricted to each parity class; no new content.
- Telescoping identities (trivial, now checked over the whole prefix):
  A(n+2) − A(n) = c(n+1) + c(n+2) and A(2k+1) − A(2k−1) = c(2k) + c(2k+1),
  c = cototient; these are just the definition A(n) = Σ c(k).

## New checks, all negative (exact tools over the supplied terms)

1. Even/odd index subsequences A(2k), A(2k+1) (100000 terms each on disk):
   - `analyze_sequence` (80 terms): no polynomial fit within 12 difference
     levels; only the mod-2 period (the known law).
   - `find_linear_recurrence` (max order 12, 80 terms): no constant-
     coefficient linear recurrence fits either half.
2. A at primes p ≤ 200000 (17984 terms): no polynomial fit; no
   constant-coefficient linear recurrence of order ≤ 12 (40 terms);
   **not in OEIS** (24 terms).
3. A at triangular numbers T_k = k(k+1)/2 (631 terms): no polynomial fit;
   no recurrence order ≤ 12 (40 terms); **not in OEIS** (24 terms).
4. A at prime powers p² (29 terms) and p³ (15 terms) for odd primes: no
   polynomial fit (p²), no recurrence order ≤ 12 (p², 30 terms);
   **not in OEIS** (24 terms).
5. Period scans over the FULL prefix (n = 2..200000, exact):
   - A mod 6: no exact period ≤ 24.
   - H mod 36: no exact period ≤ 24.
   - H mod 60: no exact period ≤ 40.
   - A mod 3, A mod 5, H mod 5: no exact period ≤ 30.
   So the only exact residue periodicity is the mod-2 law (A mod 2 / H mod 12,
   period 4); it does not lift to any of 3, 5, 6, 36, 60.
6. Quadratic closed-form falsifier: F(n) = c·n² + a·n + b for A063985 with
   any rational c (in particular c = 1/2 − 3/π²) is FALSIFIED — the second
   differences take 34655 distinct values over n = 2..100001 (first 12:
   0, 1, −1, 3, −3, 3, −1, 3, −5, 7, −7, 7). First term that would falsify:
   the first index where d2 departs from a constant, i.e. n = 3 (d2(3)=1 ≠ 0).

## Where this leaves the problem

The sequence H carries no exploitable exact structure beyond what the run
already derived and used: H = 6·A063985 = 3n(n+1) − 6·Φ(n), the mod-12
period-4 residue law (A odd iff n mod 4 ∈ {1,2}), the jump identity
H(n) − H(n−1) = 6(n − φ(n)), and the catalogued evaluations
(A063985 = A063985, H = A216453, Φ = A002088). The final answer
H(10⁸) = 11762187201804552 stands on the verified Φ(10⁸) value; no further
sequence-level structure is needed or available.

Artifacts: `code/out/extract_parity_subs.py`, `code/out/final_structure_sweep.py`
(documented in `code/out/INDEX.md`).
