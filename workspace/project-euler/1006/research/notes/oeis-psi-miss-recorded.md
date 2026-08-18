# OEIS lookup: Ψ(k) raw values NOT catalogued (re-confirmed, cycle)

Consecutive exact values from `code/out/psi_exact.txt` (k=1..10):
1, 101, 20302, 2042402, 204252402, 30445654403, 3054587854503, 407470828064704,
40849095449084804, 4085011557551094804, ...

OEIS lookup sent the four smallest consecutive terms `20302, 112102, 522122,
2239703` — a timing artifact, not the real consecutive run, and it returned no
match. The real consecutive exact values above grow ~10^2k (Ψ(k) ~ k+1 terms
each ~10^k, squared and summed), so the raw sequence is both un-catalogued and
not practically a stored OEIS sequence. Recorded so nobody re-searches.

Earlier OEIS misses (cycle-3 note) stand: the enumerative sequences of the
problem carry no catalogued closed form; structure must come from the
Sturmian/mechanical construction. Reported misses:
- raw Ψ(k) exact values — NOT in OEIS
- n_def(k) Toeplitz-defect-count — NOT in OEIS
- Fibonacci-indexed Ψ residues — NOT in OEIS
- Lmin(k) matches A344953; c1(k) matches A189663 (already found).

A mod-101001001 residue sequence is not an OEIS catalogue object either. The
closed form (if any) is not obtainable by lookup.
