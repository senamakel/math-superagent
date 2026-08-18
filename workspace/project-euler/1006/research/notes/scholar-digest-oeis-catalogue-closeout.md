# Scholar digest — OEIS catalogue + template close-out

This cycle the scholar closed the last undigested files in
`research/summaries/`: the surviving "Digest only" / "Filed by an OEIS
lookup, not read" templates. The substantive reference library (Sturmian
factor-complexity, mechanical-word slope 1/φ², universal-Euclidean monoid,
position theorems, standard-word/PER/Farey) was already fully digested in
prior cycles and is not re-reviewed here.

## What was digested this cycle

1. **Coven & Nitecki (arXiv:math/0611322)** — historical. Only content that
   bears on PE1006 is the reproduced Morse–Hedlund 1940 definition of
   Sturmian trajectories (the balance condition). It does NOT state the
   factor-complexity p(k)=k+1 theorem; that stays anchored to
   Perrin–Restivo/Berstel/Lothaire. **Marginal help**; kept as a citation of
   record, adds no theorem.
2. **de Luca 1997 docslib duplicate** — the substantive note is already at
   `deluca-sturmian-words-structure-arithmetics-1997.md`; this docslib-named
   sibling is a duplicate of the same source and carries no extra body text.
   **Already covered.**
3. **OEIS catalogue (12 files)** — proper verdicts now written:
   - **Load-bearing matches** (verified in-container in earlier pattern-hunt
     cycles): A001950/A090909 (V(R_k) run starts), A076662/A282162 (run-start
     gaps), A019587 (S1 jump d_j, with a Shallit O(log) Zeckendorf
     evaluation), A189663 (c1), A344953 (Lmin). These are *identifications* of
     the run's own verified sequences, not new theorems.
   - **Do not help:** A047931, A268317, A276575, A330064, A188036, A344953.
   - **Trap:** A330064 (Beatty cosh x) near-matches A001950 but is NOT the
     upper Wythoff sequence — flagged so it never substitutes for it.
   - The Ψ(k) sequence itself and its residues are NOT catalogued (no linear
     recurrence), so no OEIS lookup should be re-run.

## Durable findings stored to Cognee

- A330064 is a substitution trap for A001950 (stored).
- A019587 = S1-jump d_j with an O(log) Zeckendorf evaluation (stored).
- The OEIS catalogue is closed; the structural match list and the do-not-help
  list (stored).

## State of the run

All 41 sources in `research/sources/` now have statement-level notes in
`research/summaries/` and verdicts in place. The remaining open items are
execution, not digestion: run `code/lib/ueuclid.py`'s own `__main__`
(record-ueuclid-main-incontainer), then acceptance 4–5, then k=10^18 under
two approximants (task `implement-solution`, currently open). The Lean work
is hard-gated behind the captured anchors.

## Contradictions

None new with recalled memory. The standing contradictions remain:
`steer-d2-literal-slope` (holds-here: no) vs `mechanical-word-digit-rule`,
and `phase4-anchors-invalid` vs the old acceptance anchors — both already
filed and resolved in the prior cycles' ledger.
