# Index — code/mech

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `mech_psi.py` | Psi(k) by the mechanical-word (Sturmian) construction in exact arithmetic, slope a = fib(n)/fib(n+2) -> 1/phi^2, k+1 arc-midpoint intercepts of {-m*a mod 1}. Computes Psi two independent ways — (A) arc midpoints directly, (B) left limits at cut points via the telescoped identity v(x)=floor(x+ka)-10^(k-1)floor(x)+9*sum 10^(k-1-l)floor(x+la) — and requires (A)==(B) in total and per-word multiset. Verified: equals brute.py string oracle k=1..50 (exact), recorded psi_exact.txt k=1..25 (exact), recorded psi_residues.txt k=1..400 (mod M), and is insensitive to the slope approximant q in {>k, >2k+1, >5k}. Full run captured in code/out/mech_psi.captured.txt. This gate proves the mechanical route sound at oracle scale; the O(log) evaluation of the same sum at k=10^18 is the remaining step (solution.py). |
