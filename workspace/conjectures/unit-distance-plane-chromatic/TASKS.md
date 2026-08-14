# Tasks

Order of work; work the earliest incomplete item.

Directive 2 closed phase 1. Gathering is over. Further sources are fetched only
against a gap named in `research/REQUESTS.md`, and only via `read_sources` /
`deep_research` (never `download_document` on arxiv.org, doi.org,
sciencedirect.com, or springer.com — the network boundary drops those hosts).

## 1. Extract the library already gathered (immediate)

The fenced claim blocks already exist in `research/CLAIMS.md`. What is missing
is CONTEXT.md's **Established** section, which is still the empty placeholder.

- [ ] scholar: write the beliefs from `research/CLAIMS.md` into CONTEXT.md's
      **Established** section, one line each, each with its evidence class
      (proved / computed-and-checked / sourced / conjectured) and what would
      falsify it.
- [ ] Record any closed direction under CONTEXT.md **Ruled out** with the
      obstruction that closed it.

## 2. Calibrate the oracle — run code/brute.py, capture the output

- [ ] Execute:
      `timeout 540 python3 code/brute.py 2>&1 | tee code/out/brute.captured.txt; echo EXIT_CODE=$?`
      so the raw output lands in `code/out/brute.captured.txt`.
- [ ] Confirm from that capture: 7 distinct points, all 11 edges certified unit
      in exact arithmetic, 4-colourable with witness, 3-colourable UNSAT,
      `CALIBRATION PASSED`, EXIT_CODE=0.
- [ ] Do not accept the existing `G-oracle-calibrated` claim as calibration:
      `code/out/commands.log` shows only a `timeout 120` run, and
      `code/out/oracle_calibration.md`'s "verbatim" edge list does not match
      `brute.py`'s print format. The calibration is accepted only from
      `brute.captured.txt`.

## 3. Only then measure anything new

- [ ] No new measurement with the oracle until step 2's capture file exists and
      is confirmed. Any new measurement gets its own captured output file in
      `code/out/`.

## 4. Loop

- [ ] Each attempt states one precise structural claim about a minimal
      counterexample, attacks it (hunt the counterexample as seriously as the
      proof), and establishes, refutes, or leaves it open with the gap named.
- [ ] sat_solver for finite SAT questions (UNSAT is a theorem), lean_prover for
      the statement and stabilised lemmas, symbolic_math for closed forms.
- [ ] Verify any result by a second, independent route.
