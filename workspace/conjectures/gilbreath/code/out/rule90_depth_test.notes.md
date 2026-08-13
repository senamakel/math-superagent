# Rule-90 depth prediction vs block-length minima — exact numbers

data: D=1000, sieve_limit=20000000, num_primes=1270607, first_bad=None, oracle_agree_first_40=True
workers: 26 (of 28 CPUs)

local-min runs (p, q, b_k): [(1, 1, 2), (8, 8, 21), (12, 12, 96), (14, 14, 96), (22, 22, 288), (26, 26, 871), (34, 34, 865), (38, 38, 2176), (47, 50, 2762), (56, 56, 4203), (62, 64, 5939), (68, 68, 23262), (72, 72, 31496), (75, 76, 31525), (79, 80, 31525), (86, 86, 31530), (91, 91, 31533), (94, 94, 31532), (96, 96, 92619), (110, 110, 103960), (125, 125, 271617), (128, 128, 325089), (134, 134, 515907), (138, 138, 733567), (141, 143, 733574), (146, 146, 733575), (159, 159, 1094261), (1000, 1000, 1269606)]
runs: 28 total; 27 genuine — the row-1000 run is a finite-width artifact (from row 163 the block fills the sieve row and erodes one column per row; intruder is None there)

--- origin prev_min: depth = k - (first row of previous min run) ---
   k       b_k    ref     d  2^j  j dist tol1 tol0
   8        21      1     7    8  3    1    Y    N
  12        96      8     4    4  2    0    Y    Y
  14        96     12     2    2  1    0    Y    Y
  22       288     14     8    8  3    0    Y    Y
  26       871     22     4    4  2    0    Y    Y
  34       865     26     8    8  3    0    Y    Y
  38      2176     34     4    4  2    0    Y    Y
  47      2762     38     9    8  3    1    Y    N
  56      4203     47     9    8  3    1    Y    N
  62      5939     56     6    4  2    2    N    N
  68     23262     62     6    4  2    2    N    N
  72     31496     68     4    4  2    0    Y    Y
  75     31525     72     3    2  1    1    Y    N
  79     31525     75     4    4  2    0    Y    Y
  86     31530     79     7    8  3    1    Y    N
  91     31533     86     5    4  2    1    Y    N
  94     31532     91     3    2  1    1    Y    N
  96     92619     94     2    2  1    0    Y    Y
 110    103960     96    14   16  4    2    N    N
 125    271617    110    15   16  4    1    Y    N
 128    325089    125     3    2  1    1    Y    N
 134    515907    128     6    4  2    2    N    N
 138    733567    134     4    4  2    0    Y    Y
 141    733574    138     3    2  1    1    Y    N
 146    733575    141     5    4  2    1    Y    N
 159   1094261    146    13   16  4    3    N    N
1000   1269606    159   841 1024 10  183    N    N   (artif.)

--- origin last_minval: depth = k - (LAST row of previous min run) ---
   k       b_k    ref     d  2^j  j dist tol1 tol0
   8        21      1     7    8  3    1    Y    N
  12        96      8     4    4  2    0    Y    Y
  14        96     12     2    2  1    0    Y    Y
  22       288     14     8    8  3    0    Y    Y
  26       871     22     4    4  2    0    Y    Y
  34       865     26     8    8  3    0    Y    Y
  38      2176     34     4    4  2    0    Y    Y
  47      2762     38     9    8  3    1    Y    N
  56      4203     50     6    4  2    2    N    N
  62      5939     56     6    4  2    2    N    N
  68     23262     64     4    4  2    0    Y    Y
  72     31496     68     4    4  2    0    Y    Y
  75     31525     72     3    2  1    1    Y    N
  79     31525     76     3    2  1    1    Y    N
  86     31530     80     6    4  2    2    N    N
  91     31533     86     5    4  2    1    Y    N
  94     31532     91     3    2  1    1    Y    N
  96     92619     94     2    2  1    0    Y    Y
 110    103960     96    14   16  4    2    N    N
 125    271617    110    15   16  4    1    Y    N
 128    325089    125     3    2  1    1    Y    N
 134    515907    128     6    4  2    2    N    N
 138    733567    134     4    4  2    0    Y    Y
 141    733574    138     3    2  1    1    Y    N
 146    733575    143     3    2  1    1    Y    N
 159   1094261    146    13   16  4    3    N    N
1000   1269606    159   841 1024 10  183    N    N   (artif.)

=== depth hit counts (genuine minima only, k < D: 26 depths; the first run has no reference) ===
  origin prev_min:  tol0: 10/26  tol1: 21/26  tol2: 25/26  tol4: 26/26
  origin last_minval:  tol0: 10/26  tol1: 20/26  tol2: 25/26  tol4: 26/26
  origin absolute:  tol0: 10/26  tol1: 20/26  tol2: 25/26  tol4: 26/26
  genuine depths prev_min:    [7, 4, 2, 8, 4, 8, 4, 9, 9, 6, 6, 4, 3, 4, 7, 5, 3, 2, 14, 15, 3, 6, 4, 3, 5, 13]
  genuine depths last_minval: [7, 4, 2, 8, 4, 8, 4, 9, 6, 6, 4, 4, 3, 3, 6, 5, 3, 2, 14, 15, 3, 6, 4, 3, 3, 13]
  comparability with the prior run: prev_min counts with the degenerate k=1 depth-0 entry appended (never a hit): tol0 10/27, tol1 21/27 — reproduces code/out/rule90_depth_test.captured.txt (10/27, 21/27) and rule90_depth_null.json (21/27)

=== baseline: uniform over the observed genuine depth range (fraction of integer values near a power of two) ===
  prev_min tol=0: baseline 3/14 (21%)  observed 10/26 (38%)
  prev_min tol=1: baseline 8/14 (57%)  observed 21/26 (81%)
  prev_min tol=2: baseline 11/14 (79%)  observed 25/26 (96%)
  prev_min tol=4: baseline 14/14 (100%)  observed 26/26 (100%)
  last_minval tol=0: baseline 3/14 (21%)  observed 10/26 (38%)
  last_minval tol=1: baseline 8/14 (57%)  observed 20/26 (77%)
  last_minval tol=2: baseline 11/14 (79%)  observed 25/26 (96%)
  last_minval tol=4: baseline 14/14 (100%)  observed 26/26 (100%)
  absolute tol=0: baseline 3/14 (21%)  observed 10/26 (38%)
  absolute tol=1: baseline 8/14 (57%)  observed 20/26 (77%)
  absolute tol=2: baseline 11/14 (79%)  observed 25/26 (96%)
  absolute tol=4: baseline 14/14 (100%)  observed 26/26 (100%)

=== expansion events: 43 positive jumps; mag min 1, median 34, max 360698; >=1000: 13
thresholds used: [1, 34, 1000]

--- events with mag >= 34 ---
   R      mag  d_pm  2^j  dst  t1  d_lm  2^j  dst  t1 d_abs  2^j  dst  t1
  10       34     2    2    0   Y     2    2    0   Y     9    8    1   Y
  11       39     3    2    1   Y     3    2    1   Y    10    8    2   N
  15       77     1    1    0   Y     1    1    0   Y    14   16    2   N
  20      115     6    4    2   N     6    4    2   N    19   16    3   N
  23      451     1    1    0   Y     1    1    0   Y    22   16    6   N
  24      134     2    2    0   Y     2    2    0   Y    23   16    7   N
  35     1314     1    1    0   Y     1    1    0   Y    34   32    2   N
  39      594     1    1    0   Y     1    1    0   Y    38   32    6   N
  51      603     4    4    0   Y     1    1    0   Y    50   64   14   N
  52      842     5    4    1   Y     2    2    0   Y    51   64   13   N
  57     1739     1    1    0   Y     1    1    0   Y    56   64    8   N
  65    17326     3    2    1   Y     1    1    0   Y    64   64    0   Y
  69     8237     1    1    0   Y     1    1    0   Y    68   64    4   N
  95    61088     1    1    0   Y     1    1    0   Y    94   64   30   N
  97    11354     1    1    0   Y     1    1    0   Y    96   64   32   N
 111    37746     1    1    0   Y     1    1    0   Y   110  128   18   N
 113   129923     3    2    1   Y     3    2    1   Y   112  128   16   N
 127    53470     2    2    0   Y     2    2    0   Y   126  128    2   N
 131   190810     3    2    1   Y     3    2    1   Y   130  128    2   N
 135   217657     1    1    0   Y     1    1    0   Y   134  128    6   N
 147   360698     1    1    0   Y     1    1    0   Y   146  128   18   N
 162   176181     3    2    1   Y     3    2    1   Y   161  128   33   N

--- events with mag >= 1000 ---
   R      mag  d_pm  2^j  dst  t1  d_lm  2^j  dst  t1 d_abs  2^j  dst  t1
  35     1314     1    1    0   Y     1    1    0   Y    34   32    2   N
  57     1739     1    1    0   Y     1    1    0   Y    56   64    8   N
  65    17326     3    2    1   Y     1    1    0   Y    64   64    0   Y
  69     8237     1    1    0   Y     1    1    0   Y    68   64    4   N
  95    61088     1    1    0   Y     1    1    0   Y    94   64   30   N
  97    11354     1    1    0   Y     1    1    0   Y    96   64   32   N
 111    37746     1    1    0   Y     1    1    0   Y   110  128   18   N
 113   129923     3    2    1   Y     3    2    1   Y   112  128   16   N
 127    53470     2    2    0   Y     2    2    0   Y   126  128    2   N
 131   190810     3    2    1   Y     3    2    1   Y   130  128    2   N
 135   217657     1    1    0   Y     1    1    0   Y   134  128    6   N
 147   360698     1    1    0   Y     1    1    0   Y   146  128   18   N
 162   176181     3    2    1   Y     3    2    1   Y   161  128   33   N

=== variant table (parallel across 26 workers) ===
     origin tol    thr  minH/tot   ev  evH   rate  evAbsH
   prev_min   0      1 10/   26   43   33    77%       6
   prev_min   0     34 10/   26   22   15    68%       1
   prev_min   0   1000 10/   26   13    9    69%       1
   prev_min   1      1 21/   26   43   42    98%       8
   prev_min   1     34 21/   26   22   21    95%       2
   prev_min   1   1000 21/   26   13   13   100%       1
   prev_min   2      1 25/   26   43   43   100%      13
   prev_min   2     34 25/   26   22   22   100%       7
   prev_min   2   1000 25/   26   13   13   100%       4
   prev_min   4      1 26/   26   43   43   100%      19
   prev_min   4     34 26/   26   22   22   100%       9
   prev_min   4   1000 26/   26   13   13   100%       5
last_minval   0      1 10/   26   43   36    84%       6
last_minval   0     34 10/   26   22   17    77%       1
last_minval   0   1000 10/   26   13   10    77%       1
last_minval   1      1 20/   26   43   42    98%       8
last_minval   1     34 20/   26   22   21    95%       2
last_minval   1   1000 20/   26   13   13   100%       1
last_minval   2      1 25/   26   43   43   100%      13
last_minval   2     34 25/   26   22   22   100%       7
last_minval   2   1000 25/   26   13   13   100%       4
last_minval   4      1 26/   26   43   43   100%      19
last_minval   4     34 26/   26   22   22   100%       9
last_minval   4   1000 26/   26   13   13   100%       5
   absolute   0      1 10/   26   43    6    14%       6
   absolute   0     34 10/   26   22    1     5%       1
   absolute   0   1000 10/   26   13    1     8%       1
   absolute   1      1 20/   26   43    8    19%       8
   absolute   1     34 20/   26   22    2     9%       2
   absolute   1   1000 20/   26   13    1     8%       1
   absolute   2      1 25/   26   43   13    30%      13
   absolute   2     34 25/   26   22    7    32%       7
   absolute   2   1000 25/   26   13    4    31%       4
   absolute   4      1 26/   26   43   19    44%      19
   absolute   4     34 26/   26   22    9    41%       9
   absolute   4   1000 26/   26   13    5    38%       5

=== cross-check: positive jumps vs the established regeneration criterion (edge==2 and intruder==4 at the pre-transition row) ===
  23/43 pre-rows satisfy it; 20 failures: [(3, 0, 4), (10, 0, 4), (11, 0, 4), (13, 0, 4), (15, 0, 4), (27, 0, 4), (35, 0, 4), (39, 0, 4), (51, 0, 4), (52, 0, 4), (77, 0, 4), (92, 0, 4), (97, 0, 4), (127, 0, 4), (132, 0, 4), (135, 0, 4), (137, 0, 4), (139, 0, 4), (144, 0, 4), (162, 0, 4)]
