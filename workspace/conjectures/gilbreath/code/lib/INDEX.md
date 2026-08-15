# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `PARALLEL.md` | _(undescribed)_ |
| `carry.py` | Two's-complement carry/borrow bridge for |a-b|: 3-state MSB comparator + 2-state LSB borrow-subtractor (a-b = a+~b+1), composed absdiff_transducer, borrow_chain, and Diaconis-Fulman add_carry_chain. Exhaustive-checked equal to |a-b| for all a,b<2^14 in code/carry/verify_transducer.py. |
| `gilbreath.py` | Exact integer iterated absolute-difference row generator (primes_up_to, rows_generator, block_profile, diff_block) reproducing the five worked rows of problem.md; oracle for the run. |
| `parallel.py` | _(undescribed)_ |
