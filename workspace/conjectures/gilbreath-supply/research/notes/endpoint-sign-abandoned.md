# Endpoint-sign investigation abandoned — the eight attempts and the blocker

**Status: abandoned by directive 29.** A clean abandonment with the obstruction
named, as the run's record of why this line produced no captured result.

## What the question was

The endpoint-parity reduction writes the fold cell as a character product over
the runs of a digital down-set:

- **committed (skeleton) form** `(-1)^{T(n,d)} = (-1)^{#runs(d)} · ∏_R χ(r_{a_R}) χ(r_{b_R})`,
- **corrected form** `(-1)^{T(n,d)} = ∏_R χ(r_{a_R}) χ(r_{b_R})`.

The question was whether the `(-1)^{#runs(d)}` factor is real or spurious. Each
run of `↓d` telescopes independently: XOR over a run equals the endpoint
comparison `[r_a ≢ r_b]`, and `(-1)^{[x≠y]} = χ(x)χ(y)`; XOR carries signs
multiplicatively, so **there is no extra per-run sign**.

## What the eight attempts each tried

1. `committed_sign_d3.p` — TPTP d=3 encoding; axioms pin every boolean atom, `find_counterexample` returns "undecided".
2. `endpoint_sign.p` — TPTP n=5/d=3 instance; committed form vs corrected, undecided.
3. `endpoint_sign2.p` — TPTP fixed-instance `r1=r5=1`; encodes the contradiction as a `$true` conjecture, undecided.
4. `endpoint_sign3.p` — TPTP fixed-instance with `correct_plus`/`skeleton_plus` tie axioms, undecided.
5. `endpoint_sign_pure.p` — TPTP minimal d=3, `T <=> mismatch` axiom vs `T <=> ~mismatch` conjecture, undecided.
6. `endpoint_sign_spurious.p` / `endpoint_sign_spurious2.p` — TPTP tff forms fixing `r_a=1, r_b=3` (and the all-equal case), undecided.
7. `endpoint_sign_corrected_d3.p` / `endpoint_sign_test_corrected.p` / `endpoint_sign_d3.p` — TPTP positive-control encodings of the *corrected* identity, undecided.
8. `endpoint_sign_check.py` / `verify_endpoint_sign.py` — exhaustive Python checks of both forms against the literal fold oracle, the one instrument that can decide the question.

Plus nine near-identical wrappers/runners around those (`_run.py`, `_run2.py`,
`_run3.py`, `_run4.py`, `_run_grounding.py`, `run_amplify.py`, `run_endpoint.sh`,
`run_endpoint_sign.sh`, `run_refute_endpoint.sh`) that only re-invoked the same
two checkers.

## Why none produced a capture

The eight attempts split into two instruments, and **only the Python checks
decide the question**:

- **The TPTP encodings (attempts 1–7) are a wrong instrument by construction.**
  The d=3 instance has no free boolean left: `h` is defined from `r`, `T` is
  defined from `h`, and the run telescope pins `T ⇔ mismatch`. The committed
  form then asserts `T ⇔ ~mismatch`, i.e. the conjecture is contradicted by
  **every** assignment. A model-finder with no free atom to exhibit neither
  finds a model nor proves — it reports "undecided" on this finite boolean
  domain. That is not a near-miss; it is the tool's design boundary, and it
  cannot be removed by a ninth encoding.

- **The Python checks (attempt 8) do decide it** and were *not run to a capture*
  this cycle: `verify_endpoint_sign.py` and `endpoint_sign_check.py` were
  repeatedly re-written/re-wrapped rather than executed and captured, so no
  `code/out` file ever recorded their verdict. The verdict itself was already
  established and is on disk in prose
  (`research/notes/refuter_endpoint_sign.md`, §1): the committed form fails 449
  of 6868 (n,d) pairs at n=20..120 (and every odd d), the corrected form holds
  on all of them, with a decisive hand proof at d=3.

## The blocker, named

**There was no convention flip, no sign that drifted between formulations, and
no oracle disagreement.** The question was settled at d=3 by the hand proof and
on all 6868 pairs by the Python check: the `(-1)^{#runs}` factor is spurious.
The blocker was an instrument mismatch that the attempt count kept hiding — the
TPTP model-finder cannot refute a conjecture that is false for *every* input
because every atom is already pinned, and instead of accepting the hand+Python
verdict the line kept generating a fresh encoding of the same settled instance,
so a capture was never produced. The run's standing identity record is
`research/notes/refuter_endpoint_sign.md` (committed form false, corrected
identity holds).

## What survives

The settled result, not the scratch: the corrected identity
`(-1)^{T(n,d)} = ∏_R χ(r_{a_R})χ(r_{b_R})` (no `(-1)^{#runs}` factor) is true,
verified on 6868 (n,d) pairs n=20..120 with the committed form failing 449 of
them. The approach it fed, `dyadic-gap-character-correlation`, is separately
refuted on its own falsifier (no low-popcount stratum dominates S(n)), so the
sign correction does not revive it.

The single script needed to reproduce the blocker and the verdict is
`code/refute/endpoint_sign_check.py`: it checks both forms exhaustively over all
`{0,1}^12` strings and on the real prime residues, printing the committed-form
mismatches and the corrected-form pass. Directive 30 replaces the scratch deletion with a name-pattern rule: delete
every file whose name begins with an underscore or matches `*_probe.py`,
`*_run*.py`, `*_run*.sh`, or `*.p`, keeping `endpoint_sign_check.py`; count
before and after and report both numbers.

```claim
id: endpoint-sign-corrected-identity
statement: The character-product form of the endpoint parity is
  (-1)^{T(n,d)} = ∏_R χ(r_{a_R}) χ(r_{b_R}) with NO (-1)^{#runs(d)} prefactor.
  The committed form carrying the spurious (-1)^{#runs(d)} factor is false for
  every binary string at every odd d (hand proof at d=3: T = r0 XOR r4, so
  (-1)^T = χ(r0)χ(r4) while the committed form multiplies by (-1)^#runs = -1).
hypotheses: h any {0,1} string; boundary r_j = q_{j+1} mod 4 in {1,3}; T(n,d)
  the submask-XOR fold cell; each run of the digital downset telescopes and XOR
  carries signs multiplicatively (rests on g-run-telescope-verified). Checked
  range: all 6868 (n,d) pairs n=20..120 against the literal oracle t_direct,
  committed form failing 449 of them.
holds-here: yes — the telescoping argument is prime-independent; the checked
  range is the 6868 pairs n=20..120 (449 committed failures).
status: proved
bearing: the endpoint-sign character-sum carries no extra per-run sign; the
  approach it fed (dyadic-gap-character-correlation) is separately refuted on
  its own falsifier, so this correction does not revive it.
anchor: research/notes/refuter_endpoint_sign.md ; code/refute/endpoint_sign_check.py
```
