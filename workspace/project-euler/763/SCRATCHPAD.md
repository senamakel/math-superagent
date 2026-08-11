# Scratchpad

Naive BFS oracle results (exact integers), /workspace/brute.py:

depth N | D(N) | states at previous depth | frontier time
1 | 1 | 1 | ~0
2 | 3 | 1 | ~0
3 | 9 | 3 | ~0
4 | 30 | 9 | ~0
5 | 99 | 30 | ~0
6 | 336 | 99 | ~0
7 | 1134 | 336 | ~0
8 | 3855 | 1134 | 0.01-0.02s
9 | 13086 | 3855 | 0.05-0.06s
10 | 44499 | 13086 | 0.22-0.28s
11 | 151263 | 44499 | 1.0-1.2s
12 | 514419 | 151263 | 4.7-8.7s
13 | 1749267 | 514419 | ~200s
