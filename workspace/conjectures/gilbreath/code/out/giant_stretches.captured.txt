# Giant generating stretches — 12 genuine (2,4)-events

Depth 147, W = 1,270,607 primes (sieve 2e7), exact integers, one worker.

Oracle: rows A_1..A_5 reproduce problem.md exactly. Sieve: 1270607 primes up to 2e7.

Cross-checks (a): block_profile == stored b for all 13 giant event rows (12 genuine + capped 161) and all 12 genuine landing rows; step law (2,4), chain 1-Lipschitz, landing bits in {0,1}, block maximality, and container == [1, b_{k+1}+1] verified for all 12.

--- Event k=34  b_k=865  b_{k+1}=2179  j=1314 (landing row 35) ---
(b) generating stretch h_k over [865, 2180], len 1316 = j+2
    rle values (value^count, in order): 1^1 2^4 1^1 0^1 1^2 0^1 1^1 0^2 1^1 0^1 1^4 0^2 1^1 0^3 1^3  ...(672 runs total)...  1^1 0^3 1^4 0^2 1^1 0^2 1^1 0^1 1^1 0^4
    distinct=3 min=0 max=2 dominant=0 (count 677, frac 0.5144)
    steps: level 644 (0.4897), up 335 (0.2548), down 336 (0.2555); net drift -1; level+up = 0.7445
(c) landing bits row 35 over [865, 2179], len 1315 = j+1
    rle 0/1: 1^1 0^3 1^3 0^1 1^3 0^1 1^3 0^3 1^1 0^1 1^2 0^2 1^1 0^2 1^4  ...(660 runs total)...  1^3 0^2 1^1 0^3 1^1 0^1 1^2 0^1 1^4 0^3
    #0=644 (0.4897)  #1=671 (0.5103)  longest 0-run 10, longest 1-run 13; head: 100011101110111000101100
(d) CONTROL row 34: 4062 maximal 1-Lipschitz stretches with >= 100 positions total
    top lengths: [2180, 1744, 1384, 1247, 1201, 1199, 1197, 1184, 1176, 1168, 1124, 1113] ...
    runner-up (longest stretch other than the container): [6032, 7775] len 1744
    container of generating stretch = [1, 2180] len 2180 = b_{k+1}+1 = 2180; rank by length among the 4062: 1 (ties: 0)

--- Event k=56  b_k=4203  b_{k+1}=5942  j=1739 (landing row 57) ---
(b) generating stretch h_k over [4203, 5943], len 1741 = j+2
    rle values (value^count, in order): 1^1 2^3 1^1 0^1 1^1 0^2 1^1 0^4 1^1 0^1 1^5 0^2 1^1 0^2 1^1  ...(867 runs total)...  0^4 1^1 0^2 1^1 0^1 1^1 0^4 1^1 0^2 1^1
    distinct=3 min=0 max=2 dominant=0 (count 895, frac 0.5141)
    steps: level 874 (0.5023), up 433 (0.2489), down 433 (0.2489); net drift +0; level+up = 0.7511
(c) landing bits row 57 over [4203, 5942], len 1740 = j+1
    rle 0/1: 1^1 0^2 1^4 0^1 1^2 0^3 1^3 0^4 1^1 0^1 1^2 0^1 1^3 0^1 1^2  ...(871 runs total)...  0^2 1^1 0^3 1^2 0^1 1^4 0^3 1^2 0^1 1^1
    #0=874 (0.5023)  #1=866 (0.4977)  longest 0-run 8, longest 1-run 9; head: 100111101100011100001011
(d) CONTROL row 56: 1216 maximal 1-Lipschitz stretches with >= 100 positions total
    top lengths: [12156, 7226, 6840, 5943, 5838, 5782, 5264, 4540, 4339, 4232, 4019, 4003] ...
    runner-up (longest stretch other than the container): [5949, 18104] len 12156
    container of generating stretch = [1, 5943] len 5943 = b_{k+1}+1 = 5943; rank by length among the 1216: 4 (ties: 0)

--- Event k=64  b_k=5939  b_{k+1}=23265  j=17326 (landing row 65) ---
(b) generating stretch h_k over [5939, 23266], len 17328 = j+2
    rle values (value^count, in order): 1^1 2^1 1^1 0^1 1^2 0^4 1^1 0^2 1^1 0^1 1^1 0^3 1^1 0^1 1^3  ...(8419 runs total)...  0^3 1^1 0^2 1^1 0^2 1^2 0^2 1^1 0^1 1^1
    distinct=3 min=0 max=2 dominant=0 (count 8822, frac 0.5091)
    steps: level 8909 (0.5142), up 4209 (0.2429), down 4209 (0.2429); net drift +0; level+up = 0.7571
(c) landing bits row 65 over [5939, 23265], len 17327 = j+1
    rle 0/1: 1^4 0^1 1^1 0^3 1^2 0^1 1^4 0^2 1^3 0^2 1^1 0^1 1^2 0^4 1^1  ...(8645 runs total)...  0^2 1^2 0^1 1^2 0^1 1^1 0^1 1^1 0^1 1^3
    #0=8909 (0.5142)  #1=8418 (0.4858)  longest 0-run 13, longest 1-run 12; head: 111101000110111100111001
(d) CONTROL row 64: 700 maximal 1-Lipschitz stretches with >= 100 positions total
    top lengths: [23266, 13164, 9643, 8129, 8024, 7845, 7828, 7725, 7297, 7081, 6840, 6745] ...
    runner-up (longest stretch other than the container): [31545, 44708] len 13164
    container of generating stretch = [1, 23266] len 23266 = b_{k+1}+1 = 23266; rank by length among the 700: 1 (ties: 0)

--- Event k=68  b_k=23262  b_{k+1}=31499  j=8237 (landing row 69) ---
(b) generating stretch h_k over [23262, 31500], len 8239 = j+2
    rle values (value^count, in order): 1^1 2^4 1^3 0^2 1^2 0^2 1^1 0^1 1^2 0^1 1^2 0^3 1^2 0^1 1^1  ...(4171 runs total)...  0^2 1^1 0^2 1^1 0^2 1^4 0^3 1^1 0^4 1^2
    distinct=3 min=0 max=2 dominant=0 (count 4141, frac 0.5026)
    steps: level 4068 (0.4938), up 2085 (0.2531), down 2085 (0.2531); net drift +0; level+up = 0.7469
(c) landing bits row 69 over [23262, 31499], len 8238 = j+1
    rle 0/1: 1^1 0^3 1^1 0^2 1^1 0^1 1^1 0^1 1^1 0^1 1^3 0^1 1^2 0^1 1^1  ...(4236 runs total)...  1^2 0^1 1^1 0^3 1^1 0^2 1^2 0^3 1^1 0^1
    #0=4068 (0.4938)  #1=4170 (0.5062)  longest 0-run 11, longest 1-run 10; head: 100010010101011101101001
(d) CONTROL row 68: 523 maximal 1-Lipschitz stretches with >= 100 positions total
    top lengths: [31500, 14861, 14454, 14034, 13176, 12497, 9212, 9056, 8964, 8858, 8644, 8290] ...
    runner-up (longest stretch other than the container): [51885, 66745] len 14861
    container of generating stretch = [1, 31500] len 31500 = b_{k+1}+1 = 31500; rank by length among the 523: 1 (ties: 0)

--- Event k=94  b_k=31532  b_{k+1}=92620  j=61088 (landing row 95) ---
(b) generating stretch h_k over [31532, 92621], len 61090 = j+2
    rle values (value^count, in order): 1^1 2^2 3^1 2^1 1^1 0^2 1^1 0^1 1^1 0^2 1^1 0^3 1^4 0^3 1^4  ...(30378 runs total)...  1^2 0^4 1^3 0^2 1^7 0^4 1^1 0^1 1^2 2^2
    distinct=4 min=0 max=3 dominant=1 (count 30664, frac 0.5019)
    steps: level 30712 (0.5027), up 15189 (0.2486), down 15188 (0.2486); net drift +1; level+up = 0.7514
(c) landing bits row 95 over [31532, 92620], len 61089 = j+1
    rle 0/1: 1^1 0^1 1^4 0^1 1^4 0^1 1^2 0^2 1^1 0^3 1^1 0^2 1^1 0^3 1^2  ...(30694 runs total)...  1^1 0^1 1^1 0^6 1^1 0^3 1^3 0^1 1^1 0^1
    #0=30712 (0.5027)  #1=30377 (0.4973)  longest 0-run 15, longest 1-run 17; head: 101111011110110010001001
(d) CONTROL row 94: 85 maximal 1-Lipschitz stretches with >= 100 positions total
    top lengths: [92621, 72143, 66917, 59994, 46990, 46304, 45179, 44691, 30187, 29664, 28890, 27033] ...
    runner-up (longest stretch other than the container): [798066, 870208] len 72143
    container of generating stretch = [1, 92621] len 92621 = b_{k+1}+1 = 92621; rank by length among the 85: 1 (ties: 0)

--- Event k=96  b_k=92619  b_{k+1}=103973  j=11354 (landing row 97) ---
(b) generating stretch h_k over [92619, 103974], len 11356 = j+2
    rle values (value^count, in order): 1^1 2^1 1^3 0^1 1^1 0^5 1^1 0^5 1^4 0^1 1^1 0^4 1^4 0^2 1^1  ...(5731 runs total)...  0^1 1^1 0^1 1^1 0^2 1^2 0^2 1^1 0^1 1^4
    distinct=3 min=0 max=2 dominant=0 (count 5694, frac 0.5014)
    steps: level 5625 (0.4954), up 2865 (0.2523), down 2865 (0.2523); net drift +0; level+up = 0.7477
(c) landing bits row 97 over [92619, 103973], len 11355 = j+1
    rle 0/1: 1^2 0^2 1^3 0^4 1^2 0^4 1^1 0^3 1^3 0^3 1^1 0^3 1^1 0^1 1^2  ...(5644 runs total)...  1^4 0^4 1^7 0^1 1^1 0^1 1^1 0^1 1^3 0^3
    #0=5625 (0.4954)  #1=5730 (0.5046)  longest 0-run 13, longest 1-run 12; head: 110011100001100001000111
(d) CONTROL row 96: 73 maximal 1-Lipschitz stretches with >= 100 positions total
    top lengths: [103974, 74892, 66921, 59996, 54477, 47653, 46988, 46318, 45177, 44689, 35064, 27777] ...
    runner-up (longest stretch other than the container): [795325, 870216] len 74892
    container of generating stretch = [1, 103974] len 103974 = b_{k+1}+1 = 103974; rank by length among the 73: 1 (ties: 0)

--- Event k=110  b_k=103960  b_{k+1}=141706  j=37746 (landing row 111) ---
(b) generating stretch h_k over [103960, 141707], len 37748 = j+2
    rle values (value^count, in order): 1^1 2^1 1^1 0^2 1^2 0^2 1^1 0^1 1^2 0^2 1^1 0^2 1^1 0^1 1^1  ...(18969 runs total)...  0^3 1^3 0^5 1^3 0^5 1^4 0^1 1^2 0^1 1^1
    distinct=3 min=0 max=2 dominant=1 (count 18974, frac 0.5026)
    steps: level 18779 (0.4975), up 9484 (0.2513), down 9484 (0.2513); net drift +0; level+up = 0.7487
(c) landing bits row 111 over [103960, 141706], len 37747 = j+1
    rle 0/1: 1^3 0^1 1^1 0^1 1^1 0^1 1^3 0^1 1^1 0^1 1^2 0^1 1^5 0^3 1^2  ...(18823 runs total)...  0^4 1^1 0^2 1^1 0^4 1^1 0^3 1^2 0^1 1^2
    #0=18779 (0.4975)  #1=18968 (0.5025)  longest 0-run 18, longest 1-run 16; head: 111010101110101101111100
(d) CONTROL row 110: 31 maximal 1-Lipschitz stretches with >= 100 positions total
    top lengths: [187753, 141707, 129923, 108088, 79807, 76096, 59182, 53397, 51486, 40188, 39130, 30863] ...
    runner-up (longest stretch other than the container): [783716, 971468] len 187753
    container of generating stretch = [1, 141707] len 141707 = b_{k+1}+1 = 141707; rank by length among the 31: 2 (ties: 0)

--- Event k=112  b_k=141706  b_{k+1}=271629  j=129923 (landing row 113) ---
(b) generating stretch h_k over [141706, 271630], len 129925 = j+2
    rle values (value^count, in order): 1^1 2^2 1^1 0^1 1^2 0^1 1^1 0^1 1^1 0^4 1^2 0^1 1^2 0^1 1^4  ...(65013 runs total)...  0^1 1^1 0^1 1^3 0^1 1^1 0^1 1^3 0^5 1^2
    distinct=3 min=0 max=2 dominant=1 (count 65299, frac 0.5026)
    steps: level 64912 (0.4996), up 32506 (0.2502), down 32506 (0.2502); net drift +0; level+up = 0.7498
(c) landing bits row 113 over [141706, 271629], len 129924 = j+1
    rle 0/1: 1^1 0^1 1^3 0^1 1^5 0^3 1^1 0^1 1^2 0^1 1^2 0^3 1^1 0^1 1^4  ...(64870 runs total)...  1^3 0^1 1^4 0^2 1^4 0^2 1^1 0^4 1^1 0^1
    #0=64912 (0.4996)  #1=65012 (0.5004)  longest 0-run 16, longest 1-run 15; head: 101110111110001011011000
(d) CONTROL row 112: 26 maximal 1-Lipschitz stretches with >= 100 positions total
    top lengths: [271630, 187755, 108090, 79805, 76102, 63935, 59254, 53411, 50288, 40242, 30875, 28724] ...
    runner-up (longest stretch other than the container): [783712, 971466] len 187755
    container of generating stretch = [1, 271630] len 271630 = b_{k+1}+1 = 271630; rank by length among the 26: 1 (ties: 0)

--- Event k=126  b_k=271620  b_{k+1}=325090  j=53470 (landing row 127) ---
(b) generating stretch h_k over [271620, 325091], len 53472 = j+2
    rle values (value^count, in order): 1^1 2^1 1^1 0^1 1^1 2^2 1^3 0^1 1^2 0^1 1^1 0^3 1^2 0^3 1^1  ...(26737 runs total)...  0^1 1^1 0^1 1^1 0^4 1^2 0^3 1^1 0^1 1^2
    distinct=3 min=0 max=2 dominant=1 (count 26921, frac 0.5035)
    steps: level 26735 (0.5000), up 13368 (0.2500), down 13368 (0.2500); net drift +0; level+up = 0.7500
(c) landing bits row 127 over [271620, 325090], len 53471 = j+1
    rle 0/1: 1^5 0^1 1^1 0^2 1^2 0^1 1^3 0^2 1^1 0^1 1^1 0^2 1^2 0^3 1^1  ...(26810 runs total)...  1^3 0^2 1^11 0^3 1^1 0^1 1^1 0^2 1^3 0^1
    #0=26735 (0.5000)  #1=26736 (0.5000)  longest 0-run 15, longest 1-run 17; head: 111110100110111001010011
(d) CONTROL row 126: 11 maximal 1-Lipschitz stretches with >= 100 positions total
    top lengths: [325091, 237871, 217648, 190036, 115307, 79824, 55949, 31562, 11430, 4729, 744]
    runner-up (longest stretch other than the container): [733588, 971458] len 237871
    container of generating stretch = [1, 325091] len 325091 = b_{k+1}+1 = 325091; rank by length among the 11: 1 (ties: 0)

--- Event k=130  b_k=325096  b_{k+1}=515906  j=190810 (landing row 131) ---
(b) generating stretch h_k over [325096, 515907], len 190812 = j+2
    rle values (value^count, in order): 1^1 2^1 1^2 0^2 1^1 0^1 1^1 0^3 1^1 0^4 1^1 0^3 1^2 0^2 1^1  ...(95232 runs total)...  1^1 0^2 1^1 0^1 1^1 0^2 1^2 0^3 1^4 0^1
    distinct=3 min=0 max=2 dominant=1 (count 95406, frac 0.5000)
    steps: level 95580 (0.5009), up 47615 (0.2495), down 47616 (0.2495); net drift -1; level+up = 0.7505
(c) landing bits row 131 over [325096, 515906], len 190811 = j+1
    rle 0/1: 1^2 0^1 1^1 0^1 1^4 0^2 1^2 0^3 1^2 0^2 1^1 0^1 1^1 0^1 1^2  ...(95129 runs total)...  0^1 1^4 0^1 1^1 0^1 1^1 0^2 1^1 0^3 1^1
    #0=95580 (0.5009)  #1=95231 (0.4991)  longest 0-run 17, longest 1-run 17; head: 110101111001100011001010
(d) CONTROL row 130: 8 maximal 1-Lipschitz stretches with >= 100 positions total
    top lengths: [515907, 249297, 217644, 115432, 79822, 55945, 31566, 4733]
    runner-up (longest stretch other than the container): [733588, 982884] len 249297
    container of generating stretch = [1, 515907] len 515907 = b_{k+1}+1 = 515907; rank by length among the 8: 1 (ties: 0)

--- Event k=134  b_k=515907  b_{k+1}=733564  j=217657 (landing row 135) ---
(b) generating stretch h_k over [515907, 733565], len 217659 = j+2
    rle values (value^count, in order): 1^1 2^2 1^1 0^3 1^1 0^2 1^7 0^1 1^1 0^1 1^1 0^1 1^1 0^1 1^4  ...(108998 runs total)...  1^4 0^3 1^2 0^1 1^4 0^1 1^1 0^1 1^2 0^1
    distinct=3 min=0 max=2 dominant=0 (count 108938, frac 0.5005)
    steps: level 108661 (0.4992), up 54498 (0.2504), down 54499 (0.2504); net drift -1; level+up = 0.7496
(c) landing bits row 135 over [515907, 733564], len 217658 = j+1
    rle 0/1: 1^1 0^1 1^2 0^2 1^2 0^1 1^1 0^6 1^8 0^3 1^3 0^2 1^7 0^6 1^1  ...(108491 runs total)...  0^3 1^1 0^2 1^1 0^1 1^2 0^3 1^4 0^1 1^1
    #0=108661 (0.4992)  #1=108997 (0.5008)  longest 0-run 20, longest 1-run 15; head: 101100110100000011111111
(d) CONTROL row 134: 6 maximal 1-Lipschitz stretches with >= 100 positions total
    top lengths: [733565, 249293, 120185, 79824, 55941, 31562]
    runner-up (longest stretch other than the container): [733588, 982880] len 249293
    container of generating stretch = [1, 733565] len 733565 = b_{k+1}+1 = 733565; rank by length among the 6: 1 (ties: 0)

--- Event k=146  b_k=733575  b_{k+1}=1094273  j=360698 (landing row 147) ---
(b) generating stretch h_k over [733575, 1094274], len 360700 = j+2
    rle values (value^count, in order): 1^1 2^1 1^2 0^2 1^1 0^1 1^2 0^2 1^1 0^1 1^1 0^1 1^1 0^1 1^1  ...(180142 runs total)...  1^1 0^2 1^15 0^3 1^3 0^1 1^2 0^4 1^3 0^5
    distinct=3 min=0 max=2 dominant=0 (count 180930, frac 0.5016)
    steps: level 180558 (0.5006), up 90070 (0.2497), down 90071 (0.2497); net drift -1; level+up = 0.7503
(c) landing bits row 147 over [733575, 1094273], len 360699 = j+1
    rle 0/1: 1^2 0^1 1^1 0^1 1^3 0^1 1^1 0^1 1^12 0^3 1^4 0^1 1^2 0^3 1^2  ...(179846 runs total)...  1^1 0^2 1^2 0^1 1^1 0^3 1^1 0^2 1^1 0^4
    #0=180558 (0.5006)  #1=180141 (0.4994)  longest 0-run 15, longest 1-run 17; head: 110101110101111111111110
(d) CONTROL row 146: 3 maximal 1-Lipschitz stretches with >= 100 positions total
    top lengths: [1094274, 120189, 55961]
    runner-up (longest stretch other than the container): [1150272, 1270460] len 120189
    container of generating stretch = [1, 1094274] len 1094274 = b_{k+1}+1 = 1094274; rank by length among the 3: 1 (ties: 0)

## Summary across the 12 genuine giants

   k      b_k       j stretch dist  min    max  dom  domfrac   lvlf    drift   contLen rank #>=100    runner
  34      865    1314    1316    3    0      2    0   0.5144 0.4897       -1      2180    1   4062      1744
  56     4203    1739    1741    3    0      2    0   0.5141 0.5023       +0      5943    4   1216     12156
  64     5939   17326   17328    3    0      2    0   0.5091 0.5142       +0     23266    1    700     13164
  68    23262    8237    8239    3    0      2    0   0.5026 0.4938       +0     31500    1    523     14861
  94    31532   61088   61090    4    0      3    1   0.5019 0.5027       +1     92621    1     85     72143
  96    92619   11354   11356    3    0      2    0   0.5014 0.4954       +0    103974    1     73     74892
 110   103960   37746   37748    3    0      2    1   0.5026 0.4975       +0    141707    2     31    187753
 112   141706  129923  129925    3    0      2    1   0.5026 0.4996       +0    271630    1     26    187755
 126   271620   53470   53472    3    0      2    1   0.5035 0.5000       +0    325091    1     11    237871
 130   325096  190810  190812    3    0      2    1   0.5000 0.5009       -1    515907    1      8    249297
 134   515907  217657  217659    3    0      2    0   0.5005 0.4992       -1    733565    1      6    249293
 146   733575  360698  360700    3    0      2    0   0.5016 0.5006       -1   1094274    1      3    120189

Level-step fraction (plateau weight): min 0.4897, median 0.4998, max 0.5142.
Dominant (value, frac) per event: 0:0.514, 0:0.514, 0:0.509, 0:0.503, 1:0.502, 0:0.501, 1:0.503, 1:0.503, 1:0.503, 1:0.500, 0:0.500, 0:0.502
Dominant-value multiset: Counter({0: 7, 1: 5})
Net drift of the chain (h(b_{k+1}+1) - h(b_k)): [-1, 0, 0, 0, 1, 0, 0, 0, 0, -1, -1, -1]  (always nonnegative: False)
Total fresh (0, 2) entries generated by the 12 giants: 1091362; landing bits are 1 (chain climbing/falling) in 545317 = 0.4997 of them, 0 (level step) otherwise.
Container is the longest 1-Lipschitz stretch of its row in all 12: False.
Container == [1, b_{k+1}+1] in all 12 (start at block's first column, end at the chain break that defines the landing block end).

Cost: one worker; time 10.0 s wall; space O(W) ~ 220 MB peak (current row + 12 kept windows).
