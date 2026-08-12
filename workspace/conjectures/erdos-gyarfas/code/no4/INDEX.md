# Index — code/no4

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `count_no4.py` | Driver for the NO4(n) exhaustive count via nauty-geng -f -d3 -c -u n; parses the >Z graphs-generated line, times with monotonic clock, runnable in background for n where the generator outlives the command timeout. Reproduces recorded terms 5,9,57,503,6059,91433,1655659 for n=10..16 before use; n=16 ~79 s. |
