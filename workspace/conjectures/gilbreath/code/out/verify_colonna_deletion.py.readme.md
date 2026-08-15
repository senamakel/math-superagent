# NOT RUN — see the hand-verified note instead

This script was drafted to *machine*-verify the Colonna deletion counterexample,
but the scholar role does not hold a code-execution tool in this run, so it was
**never executed**. Do not treat any file under `code/out/` derived from it as a
check.

The claim it was meant to test is instead **hand-verified** in
`research/notes/colonna-deletion-verified.md` (status: checked), by exact
integer arithmetic on the nested absolute-difference triangle for deleting
primes 5, 7, 11:

- delete-11 (2,3,5,11,13,17,19): A_1=(1,2,6,2,4,2), A_2=(1,4,4,2,2) → A_2(1)=4,
  A_3(0)=3. Left edge fails at row 3.
- delete-5 (2,3,7,11,13,17,19), max gap 4: A_1(1)=4. Fails at row 1.
- delete-7 (2,3,5,11,13,17,19,23): A_2(1)=4, A_3(0)=3. Fails at row 3.

If a coder/symbolic role later wants the machine check, this file is the ready
script (sieve + exact difference-triangle oracle); it is offered as-is and
unrun.
