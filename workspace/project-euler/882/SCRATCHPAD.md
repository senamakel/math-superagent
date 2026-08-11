# Scratchpad

## Oracle run (tool_builder, TASK A)
Command: `timeout 120 python3 -u code/brute.py > code/out/brute_run.txt 2>&1`
Output (partial, killed at n=6 by 120s cap):
```
explicit-move check n=2: S(2) = 2
verify n=1: explicit S=1, memo S=1, match=True
verify n=2: explicit S=2, memo S=2, match=True
verify n=3: explicit S=8, memo S=8, match=True
S(1) = 1   states_memoized=3
S(2) = 2   states_memoized=21
S(3) = 8   states_memoized=184
S(4) = 9   states_memoized=3270
S(5) = 17  states_memoized=83052
```
- Worked examples: S(2)=2 MATCH, S(5)=17 MATCH.
- n=6 onward: real-game state space explodes (83052 states at n=5); n=10 (given
  64) is unreachable by the naive oracle, as the method policy anticipated.

## Counting surrogate (TASK B, separately-maintained, refuted per MEMORY.md)
`code/counting.py` reproduces none of the examples (all S=inf). Not the oracle;
the real-game brute is. Not my task; recorded for completeness.
