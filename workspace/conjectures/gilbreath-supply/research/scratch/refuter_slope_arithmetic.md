# Refuter slope arithmetic — exact column check

Per-doubling slope of log2(w) vs log2(n), from exact column
(w = [3,3,3,4,3,5,7,11,16,24,35,52,77] at n-doublings L=3..12 plus n=8..):

Doublings (n = 2^k, k=4..12; k=3 is n=8? no — n=8=2^3):
   n:    8    16   32   64   128  256  512  1024  2048  4096
   w:    3    3    5    7    11   16   24   35    52    77
   L=log2n: 3    4    5    6    7    8    9    10    11    12

slope[k] = log2(w_{k+1}/w_k), k = 3..11:
   3:  log2(3/3) = 0            (transient)
   4:  log2(5/3) = 0.7370
   5:  log2(7/5) = 0.4854
   6:  log2(11/7) = 0.6520
   7:  log2(16/11) = 0.5406
   8:  log2(24/16) = 0.5850
   9:  log2(35/24) = 0.5443
   10: log2(52/35) = 0.5713
   11: log2(77/52) = 0.5662

   last-3 mean (k=9,10,11) = (0.5443+0.5713+0.5662)/3 = 0.5606
   last-7 mean (k=5..11)  = (0.4854+0.6520+0.5406+0.5850+0.5443+0.5713+0.5662)/7
                          = 3.9448/7 = 0.5635

Theory (scholar_threshold_exact_mean.md): slope = 1/2 + 0.21/sqrt(L)
   L=9  : 0.5 + 0.21/3   = 0.570
   L=12 : 0.5 + 0.21/3.46 = 0.561
   observed last-3 mean 0.5606  -> matches theory to 0.000.

Candidate 0.7925 = log_4(3) = ln3/ln4: the observed slope 0.54-0.57 never
approaches 0.79. Refuted on existing data.

Conclusion: within the observable window the slope sits at 0.56-0.57 and the
run's own theory predicts it drifts to 1/2 as L->inf. "0.57 is a settled
constant" is a small-window fit; the honest closed form is 1/2 + subpolynomial.
