# Scratchpad — pattern_finder findings (PE345)

## Root pattern data
The run's only numeric results are single-instance: 5x5 oracle = 3315 and
15x15 Matrix Sum = 13938 (`code/solution.py`; Hungarian, scipy). There is no
parameterized family of terms in the run's output.

## Sequence extracted from the data
To give the exact tools a genuine sequence, computed the Matrix Sum of each
leading principal kxk submatrix of the problem's 15x15 matrix, k=1..15
(`code/seq_extract.py`, same Hungarian solver, reproduced 13938 at k=15):

  7, 680, 1273, 2282, 3868, 4578, 5712, 7114, 7818, 8779, 9876, 11239, 12062,
  12928, 13938

## Tool results (EXACT over the 15 terms, conjectures, not proofs)
- analyze_sequence: differences never constant through 12 levels → not a
  low-degree polynomial.
- find_linear_recurrence (max order 6): NO constant-coefficient linear
  recurrence fits all 15 terms.
- oeis_lookup: NO match — sequence is uncatalogued.

## Verdict (re-confirmed independently by a second pattern pass)
I re-ran analyze_sequence and find_linear_recurrence directly on the 15 terms
(reproduced from code/seq_extract.py, which itself re-derives 13938) rather than
trusting the earlier note: no low-degree polynomial (differences never constant
through 12 levels), no CC linear recurrence through order 6, and oeis_lookup =>
no catalogued entry. Identical verdict: this sequence is a dead thread. It is offspring of arbitrary 1000-range matrix
rows; its increments track which elements the independent k-matching picks,
with no smooth law and no reason to follow one. Not exploitable, and it is
unrelated to the actual answer. Do NOT re-derive or re-search it.

## On the real answer
13938 is a single data point, not a sequence. It was produced by one Hungarian
compute plus 300 small random agreement checks (those validate the method, not
the specific 15x15 matching). Independent-route confirmation of 13938 is the
orchestrator's job; nothing here adds or subtracts from it.
