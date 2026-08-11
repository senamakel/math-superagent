# Index — tmp

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `dyadic6.py` | Computes the exact dyadic board value G(6)=sum k*g(k) under the Simplicity Rule using toolkits/simplest_dyadic.simplest_between, and the theoretical S_theory=ceil(G(6)) to compare against oracle S(6). |
| `probe6.py` | Probe version of the n=6 real-game run: prints periodic progress (state count, time) so we can measure how far RealSolver(6) gets before the 500s timeout. |
| `real6.py` | Driver that runs RealSolver(6) from fastbrute.py on the n=6 initial multiset and prints S(6) plus the memoized state count, with a strict timeout. Run as: timeout 500 python3 tmp/real6.py |
