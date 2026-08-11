# Thread: lift the 2D G(k,m) pebbling recurrence to 3D

```thread
question: Can the 3D D(N) = folded-polyominoid reachable-position count be
computed to N=10000 via a 3D analogue of the 2D CGMO G(k,m) recurrence,
rather than exact BFS (which caps at N=14, cgroup 2 GiB)?
status: open — direction identified; no 3D recurrence yet written
rests-on: n3-folded-polyominoid-voidance, d2-positions-are-polyominoid-voidance
blocked-by: the precise 3D structural recurrence is not in any source
(Eriksson names folded polyominoids but gives no closed form/recurrence for
them; Zhen-Knessl and CGMO are 2D-only). Need to derive the 3D transfer
procedure from voidance-set / level-histogram structure.
next: use data/level_N.txt (level histograms, max level M, bbox for N=2..12)
to identify how D(N) decomposes by top-level/highest-pebble structure —
the 2D G(k,m) works because configuring level-m structure reduces k and m;
find the 3D analogue (a 3-label folded-polyominoid DP).
```

Context: PE763 3D amoeba = Eriksson/Vaderlind n=3 pebbling, no cell played
twice (Prop 24), so positions = voidance sets = folded polyominoids (Thm 9).
The 2D count A007902 has an exact 3-index-ish recurrence G(k,m); the 3D D(N)
(1,1,3,9,30,99,336,...,5949063) needs its own 3D transfer. The run's BFS
oracle is capped at D(14); a closed-form/recurrence is the only route to
N=10000.
