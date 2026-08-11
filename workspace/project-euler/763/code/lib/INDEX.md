# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `amoeba.py` | Reusable 3D PE763 routines shared by every oracle and data dump. Functions: `next_level_bits(level, W)` — one-step BFS over fixed-width int-bitmask configs, returns set of distinct one-division successors; `next_level_fs(level)` — same step over naive frozenset-of-tuples configs (exponential oracle, moved here from brute_extended.py/configs_n3_n4.py); `decode_bits`/`encode_bits` — int-bitmask <-> frozenset; `config_features`/`feature_record` — structural features (level histogram, bbox, max level M). Correctness established by brute oracles reproducing D(2)=3 and D(10)=44499. |
| `amoeba2d.py` | Reusable 2D amoeba (PE763 d=2) routines. CANONICAL shared copy of the A007902 auxiliary recurrence `G(k,m)` (memoized, returns 0 for k<1) and `a(n)` (offset 1, a(1)=1, a(n)=G(n,0)); plus int-bitmask encode/decode and next_level_bits2_compact (one BFS step, per-level compact grid width). G correctness established by reproducing OEIS A007902 a(1..33) exactly (incl. a(22)=13686805) and by matching the 2D BFS oracle code/amoeba2d/d2d.py on a(1..14); the BFS steps by frozenset oracle agreement for N=0..12 (code/amoeba/d2_check.py). |
