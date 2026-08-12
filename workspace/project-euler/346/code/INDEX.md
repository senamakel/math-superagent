# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `brute.py` | Naive oracle for Project Euler 346 (strong repunits): enumerates, for each n, every base 2<=b<=n and counts those in which n is a repunit; n is strong when the count >= 2. Includes the n=1 edge case (repunit of length 1 in every base). Reproduces the statement's examples exactly: 8 strong repunits below 50 and sum 15864 below 1000. Too slow for the 10^12 bound — oracle only. |
