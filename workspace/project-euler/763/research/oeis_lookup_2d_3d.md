# OEIS lookups requested and resolved

## Request: 2D amoeba-analogue sequence — RESOLVED (OEIS A007902)

Terms checked (N=0..14): 1,1,2,4,9,20,46,105,243,561,1301,3014,6995,16227,37668.
Also the partial 1,2,4,9,20,46,105,243,561,1301.

Result: **this is OEIS A007902** ("Number of pebbling configurations with n
pebbles"), the classical chessboard-pebbling / pebble-spreading problem
(Kontsevich 1981; Khodulev 1982; Chung, Graham, Morrison & Odlyzko,
AMM 102 (1995) 113–123). Offset: this run's D_2D(N) = A007902(N+1),
verified on all 15 requested terms AND on the run's own extended BFS terms
D_2D(15..21) = 87426, 202961, 471150, 1093819, 2539348, 5895408, 13686805,
which equal A007902's terms 16..22.

- A-number: A007902, https://oeis.org/A007902
- No closed form; exact structural recurrence via auxiliary G(k,m)
  (recorded in research/amoeba2d_pebbling_a007902.md).
- Asymptotic: a(n) ~ c·d^n, d = 2.3216421994942297…, c = 0.12268707342148599…
  (Knessl; Kotesovec).

## Request: 3D sequence first 8 terms — RESOLVED (NOT in OEIS)

Terms checked: 1,1,3,9,30,99,336,1134. Also full 15 terms (per the prior note
research/amoeba_seq_oeis.md, and offset-1 11 terms).

Result: **no OEIS entry**. Direct queries (full 15 terms, offset-1 11 terms,
and now the 8-term partial 1,1,3,9,30,99,336,1134) all return "No results".
This is a permanent negative: the 3D D(N) has no A-number, so no catalogued
closed form exists; the structure must come from the problem itself.

Note: 1,2,4,9,20,46,105,243 (the 2D head) also appears as the head of the
directed-animal sequence A005773, but A005773's later terms diverge and it is
NOT this 2D amoeba sequence — the correct 2D identification is A007902.

Per run instruction, no Project Euler 763 solution/solver/forum thread was
consulted.
