# Index — code/block_apex

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `check_constant_blocks.py` | Empirical probe for the block-apex-parity-forcing approach: exact sieve to 2e7 (1,270,607 primes), one row at a time; per row k=1..1000 records leading {0,2} block length b, second entry s, intruder y, whole-block constancy (const0/const2/mixed), terminal constant suffix length, and longest 0/2 runs. Correctness: reproduces the five witness rows of problem.md (hand-verified, smoke test), and its block lengths match the independent stored oracle code/out/blocks_depth1000.json 1000/1000. Result: live rows k=1..161 have whole-block constant blocks only at k=1 ([2,2], b=2); all k=2..161 blocks mixed; max live tail 7 (k=27); capture code/out/block_constancy.captured.txt, JSON code/out/block_constancy.json. |
| `front_sequence_oracle.py` | _(undescribed)_ |
| `run.sh` | _(undescribed)_ |
