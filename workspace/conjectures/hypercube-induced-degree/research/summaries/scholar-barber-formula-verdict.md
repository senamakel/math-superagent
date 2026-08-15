# Scholar note — Barber balanced-independent-set formula: transcription is broken

Settling the contradiction the prior pass flagged but could not run: the source
file `research/sources/barber-balanced-independent-cube-2012.md` gives the odd-n
max-balanced-independent-set constant two incompatible ways (prose: no `/2`;
theorem text / claim block / summary: `/2`), and the even-n formula looks wrong
at small n.

## Hand oracle (small cases, per method rule 9) — NOT from a shell run

- **n=2 (even):** Q₂ = 4-cycle, every even vertex adjacent to both odds ⇒ no
  balanced independent set. True max = **0**. Even formula 2¹−2⁻¹·0 = 2 is **wrong**.
- **n=3 (odd):** every pair of even vertices jointly touches all four odds, so
  k=2 impossible; max balanced = {000,111} = **2**. odd v2 = 2²−(2¹·2)/2 = 2 ✓;
  odd v1 = 2²−2¹·2 = 0 ✗.
- **n=5 (odd):** an odd vertex non-adjacent to a fixed even vertex always exists
  (e.g. 00111 vs 00000), so true max ≥ **2**. v1 = 2⁴−2³·4 = −16 and
  v2 = 16−(8·4)/2 = 0 are both ≤ 0 ⇒ **both fail**.

So neither transcription is the correct formula: the even form fails at n=2, the
odd v2 form happens to hit 2 at n=3 but both odd forms collapse at n=5.

## Consequences

- The balanced-set constant is **not load-bearing** for f(n): it is the d=0
  (independent-set) line of f(n)'s structure, and f(n)'s +1 excess is untouched
  by it. The classification claim below is the part that matters and is sound.
- Do not cite either transcription of the balanced formula. If the exact value is
  ever needed, compute it (oracle below) or fetch Barber's paper (screen-held).
- The library's CLAIMS.md rows for
  `balanced-independent-set-max-smaller-than-parity` carry the broken formula and
  should be treated as **unverified** until a correct value is established.

## Claim block

```claim
id: barber-balanced-formula-transcription-broken
statement: Neither transcription of Barber's balanced-independent-set constant
  in the library is correct. True max balanced independent set of Q_n: n=2 → 0
  (even formula gives 2, wrong); n=3 → 2 (odd v2 gives 2, odd v1 gives 0); n=5 →
  ≥ 2 but both odd transcriptions give ≤ 0. Hence the even and odd forms as
  written fail at small n.
hypotheses: Q_n = {0,1}^n, balanced = equal # even and # odd vertices,
  independent, no inter-parity edges; n small (2,3,5).
holds-here: yes — this is the disputed transcription, checked by hand on the
  small cases; the exact general constant is not established here.
status: checked (n=2,3 by hand; n=5 lower bound by construction; exact values for
  4,5 left to the oracle)
bearing: the balanced-set line is NOT load-bearing for f(n) (it is the d=0 line;
  f(n)'s +1 excess is untouched). Treat the formula rows in CLAIMS.md as
  unverified; do not cite the constant.
contradicts: balanced-independent-set-max-smaller-than-parity (both ROWS carry a
  broken transcription), barber-balanced-formula-odd-half (that prior claim
  asserts the /2 odd form is correct for all odd n>=3, hand-checked only at n=3;
  n=5 refutes it — v2=0 there while a balanced set of size 2 provably exists,
  e.g. {00000, 00111})
anchor: research/sources/barber-balanced-independent-cube-2012.md
```

## Reconciliation with the prior `barber-balanced-formula-odd-half` claim

`code/out/verify_barber_balanced.note.md` reaches the same n=3 result (true
max 2, matching the /2 form) but over-generalises it into "v2 is the correct
constant for all odd n >= 3", confirmed by hand at n=3 only. That is the
over-broad step: v2 = 2^{n-1} - 2^{n-2}(n-1)/2 collapses to 0 at n=5 (16-16),
whereas a balanced independent set of size 2 provably exists (00000 even,
00111 odd, differ in 3 coords → not adjacent). So the /2 form is NOT the
correct general odd-n constant either; it merely happens to match at n=3.
Both library transcriptions are broken. A runner must brute-force n=4,5
(`code/out/check_barber_balanced.py`) to get true values; do not cite any
transcribed constant until the oracle output exists.

## Oracle for a runner (I have no shell)

There are two equivalent brute-force oracles; both must be run by a coder/
tool_builder (scholar has no shell). Values n=2→0 and n=3→2 are hand-derived
checks both should reproduce; n=4,5 are open until a run exists.
- `code/out/check_barber_balanced.py` — exhaustive over A ⊆ X_0 (m = 2^(n-1)),
  maximising 2·min(|A|, |X₁|−|N(A)|) = true max balanced independent set, n=2..5.
  Run: `sh code/out/run_barber_check.sh`.
- `code/out/verify_barber_balanced.py` — prior pass's brute force, n=2..4
  (enumerates even/odd k-subsets, checks independence). Do not re-read.
Not yet executed (no shell here). n=5 is beyond the prior oracle's range (which
stops at 4), so the transcription-breaking n=5 case is only covered by my new one.
