# Index — code/scholar

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `verify_malyshev_bound.py` | Exhaustive verification (s=1..14, all 2^s top rows) of Malyshev's sharp bound on #ones in a Boolean Pascal (rule-90) triangle: max_ones = ceil(s(s+1)/3), Fibonacci-mod-2 extremal. Written to upgrade the sourced claim malyshev-max-ones-boolean-pascal-bound to checked; NOT yet executed (no shell tool in scholar role) — operator must run `timeout 540 python3 code/scholar/verify_malyshev_bound.py` and capture to code/out/verify_malyshev_bound.captured.txt. |
