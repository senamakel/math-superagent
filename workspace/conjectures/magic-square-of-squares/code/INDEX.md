# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `brute.py` | Naive oracle for the 3x3 magic square of squares: is_magic_square_of_squares verifier (failure_of diagnosis), grid_from_params, and a generator over the (c,u,v) parametrisation. Run against the statement's structural worked examples (parametrisation identity, centre-line AP structure, completeness) and small exhaustive scans (entries<=100, c=e^2 box). ALL TESTS PASSED, 6.9 s; exact output in code/out/oracle_output.txt. This is the ground truth every sieve/descent/structural lemma is measured against, and the pass criteria deliberately forbid treating repeated-entry grids (all-k^2, {1,25,49} family) as solutions. |
