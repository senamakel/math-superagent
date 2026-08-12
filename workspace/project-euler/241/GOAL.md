# Goal

**Problem (PE 241).** For positive integer n, let sigma(n) be the sum of all
divisors of n (e.g. sigma(6)=1+2+3+6=12). Define the perfection quotient
p(n)=sigma(n)/n. Find the sum of all positive integers n ≤ 10^18 for which
p(n) has the form k + 1/2, where k is an integer.

Equivalently: n is "hemiperfect" (OEIS A159907): 2·sigma(n)/n is an odd
integer.

## Completion criteria (all observable)

- [ ] Reproduce the statement's worked example: sigma(6)=12, from
      /workspace/code/brute.py. Checked by running brute.py.
- [ ] Brute-force oracle finds, at N=10^6, exactly {2,24,4320,4680,26208}
      with their k values (matches A159907 prefix). Checked by running brute.py.
- [ ] DFS solver /workspace/code/hemiperfect_dfs.py agrees with the brute
      oracle at every bound brute can reach (at least 10^6; ideally 3e7).
      Checked by running both.
- [ ] DFS solver at LIMIT=10^18 produces the full set of 22 hemiperfects
      (per prior memory, awaiting run) and a total sum.
- [ ] Total sum independently confirmed from the OEIS A159907 b-file: sum of
      exactly the b-file terms ≤ 10^18. Must equal the DFS sum. (Second route.)
- [ ] /workspace/solution.md and /workspace/code/solution.py written and
      described; solution.md states the method, the governing result
      (multiplicativity of sigma(n)/n + forced denominator cancellation), and
      the verification commands.

## Verification commands
- Python /workspace/code/brute.py          (oracle at small bound)
- Python /workspace/code/hemiperfect_dfs.py  (full run at 10^18)
