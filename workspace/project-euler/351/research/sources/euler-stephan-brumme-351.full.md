<!-- source: https://euler.stephan-brumme.com/351/ | converted from HTML -->

My C++ solution for Project Euler 351: Hexagonal orchards -->

*e*[Home][1] | [Why?][2] | [Toolbox][3] | [Techniques][4] | [Inside][5] | [Performance][6] | [Progress][7] | [News][8]

[<< problem 349 - Langton's ant][9] | [10] | [Prime generating integers - problem 357 >>][11] |

# Problem 351: Hexagonal orchards

(see [projecteuler.net/problem=351][10])

A hexagonal orchard of order n is a triangular lattice made up of points within a regular hexagon with side n.
The following is an example of a hexagonal orchard of order 5:

[image: orchard]

Highlighted in green are the points which are hidden from the center by a point closer to it.
It can be seen that for a hexagonal orchard of order 5, 30 points are hidden from the center.

Let H(n) be the number of points hidden from the center in a hexagonal orchard of order n.

H(5) = 30. H(10) = 138. H(1 000) = 1177848.

Find H(100 000 000).

# My Algorithm

All six "triangles" of such a hexagon can be treated equal. I count only the points of the upper-right triangle and multiply the result by 6.
The point in the centre doesn't belong to any triangle and is never hidden.

All points can be thought of as fractions: the points on the right side of centre is 1/1.
The next ring (actually: part of a ring, I'm only looking at one six-th of it) is 1/2 and 2/2, then 1/3, 2/3, 3/3, followed by 1/4, 2/4, 3/4 and 4/4.
Finally the outer-most ring consists of 1/5, 2/5, 3/5, 4/5 and 5/5 for a total of 15 points.
The total number is equivalent to the triangular number T(n) = n(n+1)/2 (with T(5) = 15, see [en.wikipedia.org/wiki/Triangular_number][12])

The hidden points are 2/2, 3/3, 2/4, 4/4 and 5/5. Those are exactly the fractions that are not proper fractions:
both numerator and denominator share a common factor such that gcd(n,d) > 1.
The `bruteForce()`algorithm checks the gcd() of all fractions. It finds H(1000) within less than 0.04 seconds but becomes very slow for larger values (I assume it's O(n^2 log n)).

However, I've seen similar problems before: counting how often a certain number if coprime to other numbers can be done with Euler's totient function (see [en.wikipedia.org/wiki/Euler's_totient_function][13]).
The guys at Project Euler seem to really like this function because of its namesake ...

Anyway, the number of visible points in a (partial) ring i is phi(i). Then the number of hidden points in that (partial) ring i is i - phi(i).
The number of hidden points in a full ring is therefore 6 * (i - phi(i)).
The solution for an orchard of order n is
(1) sum_{i=1..n} 6 * (i - phi(i))
(2) 6 * sum_{i=1..n} (i - phi(i))
(3) 6 * (sum_{i=1..n} i - sum_{i=1..n} phi(i))
(4) 6 * (n(n+1)/2 - sum_{i=1..n} phi(i))

All I need is an efficient way to compute phi(i) for all i <= 10^8; that's the totient summary function (see [mathworld.wolfram.com/TotientSummatoryFunction.html][14]).
If I compute all phi(x) at once with a sieve then I need more than 400 MByte RAM which is more than the inofficial limit of Project Euler
(see `sumPhi()`, it takes about 3.5 seconds to finish).

So I rewrote that sieve to work in a segmented way (see `sumPhiSliced()`): compute phi(x) for 0 < x < 10^6, then 10^6 <= x < 2 * 10^6, and so on.
The memory consumption shrinks down to just 30 MByte and the program actually becomes a bit faster because of better cache locality (3.1 seconds, minus 0.4 seconds).
Admittedly, the code isn't that nice to look at: I added my prime sieve from my [toolbox][15] and it takes quite some code to properly handle all edge cases.

# Interactive test

You can submit your own input to my program and it will be instantly processed at my server:

This is equivalent to
`echo 1000 | ./351`

Output:

(please click 'Go !')

*Note:*the original problem's input `100000000`cannot be entered
because just copying results is a soft skill reserved for idiots.

*(this interactive test is still under development, computations will be aborted after one second)*

# My code

… was written in C++11 and can be compiled with G++, Clang++, Visual C++. You can [download][16] it, too. Or just jump to my [GitHub repository][17].

```

#include <iostream> |

#include <vector> |

  |

// ---------- gcd() can be found in my [toolbox][15], as well as my fast prime sieve ----------
 |

  |

// greatest common divisor
 |

template <typename T> |

T gcd(T a, T b) |

{ |

  while (a != 0) |

  { |

    T c = a; |

    a = b % a; |

    b = c; |

  } |

  return b; |

} |

  |

// odd prime numbers are marked as "true" in a bitvector
 |

std::vector<bool> sieve; |

  |

// return true, if x is a prime number
 |

bool isPrime(unsigned int x) |

{ |

  // handle even numbers |

  if ((x & 1) == 0) |

    return x == 2; |

  |

  // lookup for odd numbers |

  return sieve[x >> 1]; |

} |

  |

// find all prime numbers from 2 to size
 |

void fillSieve(unsigned int size) |

{ |

  // store only odd numbers |

  const unsigned int half = (size >> 1) + 1; |

  |

  // allocate memory |

  sieve.resize(half, true); |

  // 1 is not a prime number |

  sieve[0] = false; |

  |

  // process all relevant prime factors |

  for (unsigned int i = 1; 2*i*i < half; i++) |

    // do we have a prime factor ? |

    if (sieve[i]) |

    { |

      // mark all its multiples as false |

      unsigned int current = 3*i+1; |

      while (current < half) |

      { |

        sieve[current] = false; |

        current += 2*i+1; |

      } |

    } |

} |

  |

// ---------- problem-specific code ----------
 |

  |

// count all fractions i/j where i is coprime to j
 |

unsigned long long bruteForce(unsigned int limit) |

{ |

  unsigned long long hidden = 0; |

  for (unsigned int i = 1; i <= limit; i++) |

    for (unsigned int j = 1; j <= i; j++) |

      if (gcd(i, j) != 1) |

        hidden++; |

  return hidden; |

} |

  |

// needs almost half a GByte RAM
 |

unsigned long long sumPhi(unsigned int limit) |

{ |

  // similar to http://www.geeksforgeeks.org/eulers-totient-function-for-all-numbers-smaller-than-or-equal-to-n/ |

  // alternatives can be found here: https://codegolf.stackexchange.com/questions/26739/super-speedy-totient-function |

  |

  // the sum |

  unsigned long long result = 1; // phi(1) = 1 |

  |

  // allocate enough memory, fill with 1,2,3,4,... |

  std::vector<unsigned int> phi(limit + 1); |

  for (unsigned int i = 0; i < phi.size(); i++) |

    phi[i] = i; |

  |

  // look for prime numbers |

  for (unsigned int i = 2; i <= limit; i++) |

  { |

    result += phi[i]; |

  |

    // composite number, already computed phi(i) |

    if (phi[i] != i) |

      continue; |

  |

    // phi(prime) = prime - 1 |

    phi[i]--; // was initially phi[i] = prime |

    result--; |

  |

    // adjust all multiples |

    for (auto j = 2 * i; j <= limit; j += i) |

      phi[j] = (phi[j] / i) * (i - 1); |

  } |

  |

  return result; |

} |

  |

// adjustable memory consumption
 |

unsigned long long sumPhiSliced(unsigned int limit, unsigned int segmentSize = 1000000) |

{ |

  // the sum |

  unsigned long long result = 1; // phi(1) = 1 |

  |

  // find all primes |

  fillSieve(limit); |

  // store them |

  std::vector<unsigned int> primes = { 2 }; |

  primes.reserve(limit * 6 / 100); // about 6 million primes < 10^8 |

  for (unsigned int i = 3; i <= limit; i += 2) |

    if (isPrime(i)) |

      primes.push_back(i); |

  // release memory |

  sieve.clear(); |

  sieve.shrink_to_fit(); |

  |

  // allocate memory for a single segment |

  std::vector<unsigned int> phi(segmentSize); |

  |

  // start with phi(2) |

  for (unsigned int from = 2; from <= limit; from += segmentSize) |

  { |

    auto to = from + segmentSize; |

    if (to > limit) |

      to = limit + 1; |

    // actual size is always identical to segmentSize except for the last slice |

    auto size = to - from; |

  |

    // fill with from, from+1, from+2, ... |

    for (unsigned int i = 0; i < size; i++) |

      phi[i] = from + i; |

  |

    // process all multiples of all primes in the current segments |

    for (unsigned int p = 0; p < primes.size(); p++) |

    { |

      auto current = primes[p]; |

  |

      // find smallest multiple in current slice |

      auto minJ = 2 * current; |

      if (minJ < from) |

      { |

        minJ = (from / current) * current; |

        if (minJ < from) |

          minJ += current; |

      } |

  |

      // adjust all multiples |

      for (auto j = minJ; j < to; j += current) |

      { |

        auto index = j - from; |

        phi[index] = (phi[index] / current) * (current - 1); |

      } |

  |

      // don't forget about the primes |

      if (current >= from && current < to) |

        phi[current - from]--; |

    } |

  |

    // add all phi of the current slice |

    for (unsigned int i = 0; i < size; i++) |

      result += phi[i]; |

  } |

  |

  return result; |

} |

  |

int main() |

{ |

  unsigned int limit = 100000000; // 10^8 |

  std::cin >> limit; |

  |

  // slow brute-force |

  //unsigned long long result = bruteForce(limit); |

  |

  // fast algorithm |

  auto triangle = (unsigned long long)limit * (limit + 1) / 2; |

  |

#define SLICED |

#ifdef  SLICED |

  auto result = triangle - sumPhiSliced(limit); |

#else |

  auto result = triangle - sumPhi(limit); |

#endif |

  |

  // the previous code analyzed only one sixth of the hexagon |

  result *= 6; |

  |

  std::cout << result << std::endl; |

  return 0; |

} |

```

This solution contains 35 empty lines, 42 comments and 6 preprocessor commands.

# Benchmark

The correct solution to the original Project Euler problem was found in 3.1 seconds on an Intel&reg; Core&trade; i7-2600K CPU @ 3.40GHz.
Peak memory usage was about 31 MByte.

(compiled for x86_64 / Linux, GCC flags: `-O3 -march=native -fno-exceptions -fno-rtti -std=gnu++11 -DORIGINAL`)

See [here][18] for a comparison of all solutions.

**Note:**interactive tests run on a weaker (=slower) computer. Some interactive tests are compiled without `-DORIGINAL`.

# Changelog

September 26, 2017 submitted solution
September 26, 2017 added comments

# Difficulty

25% Project Euler ranks this problem at **25%**(out of 100%).

# Similar problems at Project Euler

Problem 214: [Totient Chains][19]

*Note:*I'm not even close to solving all problems at Project Euler. Chances are that similar problems do exist and I just haven't looked at them.

# See also

OEIS Sequence A216453: [www.oeis.org/A216453][20]

# Links

[projecteuler.net/thread=351][21] - **the**best forum on the subject (*note:*you have to submit the correct solution first)

Code in various languages:

C++ [github.com/Meng-Gen/ProjectEuler/blob/master/351.cc][22] (written by Meng-Gen Tsai)
C++ [github.com/roosephu/project-euler/blob/master/351.cpp][23] (written by Yuping Luo)
C [github.com/LaurentMazare/ProjectEuler/blob/master/e351.c][24] (written by Laurent Mazare)
Java [github.com/thrap/project-euler/blob/master/src/Java/Problem351.java][25] (written by Magnus Solheim Thrap)

Those links are just an unordered selection of source code I found with a semi-automatic search script on Google/Bing/GitHub/whatever.
You will probably stumble upon better solutions when searching on your own.
Maybe not all linked resources produce the correct result and/or exceed time/memory limits.

# Heatmap

*Please click on a problem's number to open my solution to that problem:*

green |  | solutions solve the original Project Euler problem and have a perfect score of 100% at Hackerrank, too |

yellow |  | solutions score less than 100% at Hackerrank (but still solve the original problem easily) |

gray |  | problems are already solved but I haven't published my solution yet |

blue |  | solutions are relevant for Project Euler only: there wasn't a Hackerrank version of it (at the time I solved it) or it differed too much |

orange |  | problems are solved but exceed the time limit of one minute or the memory limit of 256 MByte |

red |  | problems are **not**solved yet but I wrote a simulation to approximate the result or verified at least the given example - usually I sketched a few ideas, too |

black |  | problems are solved but access to the solution is blocked for a few days until the next problem is published |

[new] |  | the flashing problem is the one I solved most recently |

I stopped working on [Project Euler][26] problems around the time they released 617.

[1][27] | [2][28] | [3][29] | [4][30] | [5][31] | [6][32] | [7][33] | [8][34] | [9][35] | [10][36] | [11][37] | [12][38] | [13][39] | [14][40] | [15][41] | [16][42] | [17][43] | [18][44] | [19][45] | [20][46] | [21][47] | [22][48] | [23][49] | [24][50] | [25][51] |

[26][52] | [27][53] | [28][54] | [29][55] | [30][56] | [31][57] | [32][58] | [33][59] | [34][60] | [35][61] | [36][62] | [37][63] | [38][64] | [39][65] | [40][66] | [41][67] | [42][68] | [43][69] | [44][70] | [45][71] | [46][72] | [47][73] | [48][74] | [49][75] | [50][76] |

[51][77] | [52][78] | [53][79] | [54][80] | [55][81] | [56][82] | [57][83] | [58][84] | [59][85] | [60][86] | [61][87] | [62][88] | [63][89] | [64][90] | [65][91] | [66][92] | [67][93] | [68][94] | [69][95] | [70][96] | [71][97] | [72][98] | [73][99] | [74][100] | [75][101] |

[76][102] | [77][103] | [78][104] | [79][105] | [80][106] | [81][107] | [82][108] | [83][109] | [84][110] | [85][111] | [86][112] | [87][113] | [88][114] | [89][115] | [90][116] | [91][117] | [92][118] | [93][119] | [94][120] | [95][121] | [96][122] | [97][123] | [98][124] | [99][125] | [100][126] |

[101][127] | [102][128] | [103][129] | [104][130] | [105][131] | [106][132] | [107][133] | [108][134] | [109][135] | [110][136] | [111][137] | [112][138] | [113][139] | [114][140] | [115][141] | [116][142] | [117][143] | [118][144] | [119][145] | [120][146] | [121][147] | [122][148] | [123][149] | [124][150] | [125][151] |

[126][152] | [127][153] | [128][154] | [129][155] | [130][156] | [131][157] | [132][158] | [133][159] | [134][160] | [135][161] | [136][162] | [137][163] | [138][164] | [139][165] | 140 | [141][166] | [142][167] | 143 | [144][168] | [145][169] | [146][170] | [147][171] | [148][172] | [149][173] | [150][174] |

[151][175] | [152][176] | 153 | [154][177] | [155][178] | [156][179] | 157 | [158][180] | [159][181] | [160][182] | [161][183] | [162][184] | [163][185] | [164][186] | [165][187] | [166][188] | 167 | [168][189] | [169][190] | [170][191] | [171][192] | [172][193] | [173][194] | [174][195] | 175 |

176 | 177 | [178][196] | [179][197] | 180 | [181][198] | [182][199] | [183][200] | 184 | [185][201] | [186][202] | [187][203] | [188][204] | [189][205] | [190][206] | [191][207] | 192 | [193][208] | 194 | 195 | [196][209] | [197][210] | 198 | [199][211] | [200][212] |

[201][213] | 202 | [203][214] | [204][215] | [205][216] | [206][217] | [207][218] | [208][219] | [209][220] | 210 | [211][221] | 212 | [213][222] | [214][223] | [215][224] | [216][225] | 217 | [218][226] | [219][227] | 220 | 221 | [222][228] | 223 | 224 | [225][229] |

[226][230] | [227][231] | 228 | [229][232] | [230][233] | [231][234] | [232][235] | 233 | [234][236] | [235][237] | 236 | [237][238] | 238 | [239][239] | [240][240] | 241 | 242 | [243][241] | [244][242] | 245 | 246 | [247][243] | [248][244] | [249][245] | [250][246] |

251 | 252 | 253 | 254 | 255 | 256 | 257 | 258 | [259][247] | [260][248] | 261 | 262 | 263 | 264 | [265][249] | [266][250] | [267][251] | [268][252] | 269 | 270 | 271 | 272 | [273][253] | [274][254] | 275 |

276 | [277][255] | [278][256] | [279][257] | [280][258] | 281 | 282 | 283 | [284][259] | 285 | [286][260] | [287][261] | [288][262] | 289 | [290][263] | [291][264] | 292 | [293][265] | 294 | 295 | 296 | [297][266] | 298 | 299 | [300][267] |

[301][268] | 302 | [303][269] | [304][270] | 305 | [306][271] | [307][272] | [308][273] | [309][274] | [310][275] | 311 | 312 | [313][276] | 314 | [315][277] | 316 | [317][278] | 318 | 319 | 320 | [321][279] | 322 | [323][280] | [324][281] | 325 |

326 | [327][282] | 328 | [329][283] | 330 | 331 | 332 | [333][284] | 334 | 335 | [336][285] | 337 | 338 | 339 | 340 | [341][286] | 342 | [343][287] | 344 | [345][288] | [346][289] | [347][290] | [348][291] | [349][9] | 350 |

351 | 352 | 353 | 354 | 355 | 356 | [357][11] | [358][292] | [359][293] | 360 | 361 | 362 | [363][294] | 364 | 365 | 366 | 367 | 368 | 369 | 370 | [371][295] | 372 | 373 | 374 | [375][296] |

376 | 377 | 378 | 379 | 380 | [381][297] | 382 | 383 | 384 | 385 | [386][298] | [387][299] | 388 | 389 | 390 | 391 | 392 | [393][300] | 394 | 395 | 396 | 397 | 398 | 399 | 400 |

[401][301] | 402 | 403 | 404 | 405 | 406 | [407][302] | 408 | 409 | 410 | [411][303] | [412][304] | 413 | 414 | 415 | 416 | 417 | [418][305] | 419 | 420 | 421 | 422 | 423 | 424 | [425][306] |

426 | 427 | 428 | [429][307] | 430 | 431 | 432 | 433 | 434 | 435 | [436][308] | 437 | 438 | 439 | 440 | 441 | 442 | 443 | 444 | 445 | 446 | 447 | 448 | 449 | 450 |

451 | 452 | 453 | 454 | [455][309] | 456 | 457 | [458][310] | 459 | 460 | [461][311] | 462 | 463 | 464 | 465 | 466 | 467 | 468 | 469 | 470 | 471 | 472 | [473][312] | 474 | 475 |

476 | 477 | 478 | 479 | 480 | 481 | 482 | 483 | 484 | [485][313] | 486 | 487 | 488 | 489 | 490 | [491][314] | 492 | [493][315] | 494 | 495 | 496 | 497 | 498 | 499 | [500][316] |

[501][317] | 502 | 503 | [504][318] | 505 | 506 | 507 | 508 | 509 | [510][319] | 511 | 512 | 513 | 514 | 515 | [516][320] | 517 | [518][321] | 519 | 520 | 521 | 522 | [523][322] | 524 | 525 |

526 | 527 | 528 | 529 | 530 | 531 | 532 | 533 | 534 | 535 | 536 | 537 | 538 | [539][323] | 540 | 541 | 542 | 543 | 544 | 545 | 546 | 547 | 548 | [549][324] | 550 |

551 | 552 | 553 | 554 | 555 | 556 | 557 | 558 | 559 | 560 | 561 | 562 | [563][325] | 564 | [565][326] | 566 | 567 | 568 | 569 | 570 | [571][327] | 572 | 573 | 574 | 575 |

576 | [577][328] | 578 | 579 | 580 | [581][329] | 582 | 583 | 584 | 585 | 586 | [587][330] | 588 | 589 | 590 | 591 | 592 | 593 | 594 | 595 | 596 | 597 | 598 | 599 | 600 |

[601][331] | 602 | 603 | 604 | 605 | 606 | [607][332] | 608 | 609 | [610][333] | [611][334] | [612][335] | [613][336] | 614 | [615][337] | 616 | 617 | 618 | 619 | 620 | 621 | 622 | 623 | 624 | 625 |

626 | 627 | 628 | 629 | 630 | 631 | 632 | 633 | 634 | 635 | 636 | 637 | 638 | 639 | 640 | 641 | 642 | 643 | 644 | 645 | 646 | 647 | 648 | 649 | 650 |

651 | 652 | 653 | 654 | 655 | 656 | 657 | 658 | 659 | 660 | 661 | 662 | 663 | 664 | 665 | 666 | 667 | 668 | 669 | 670 | 671 | 672 | 673 | 674 | 675 |

676 | 677 | 678 | 679 | 680 | 681 | 682 | 683 | 684 | 685 | 686 | 687 | 688 | 689 | 690 | 691 | 692 | 693 | 694 | 695 | 696 | 697 | 698 | 699 | 700 |

701 | 702 | 703 | 704 | 705 | 706 | 707 | 708 | 709 | 710 | 711 | 712 | 713 | 714 | 715 | 716 | 717 | 718 | 719 | 720 | 721 | 722 | 723 | 724 | 725 |

726 | 727 | 728 | 729 | 730 | 731 | 732 | 733 | 734 | 735 | 736 | 737 | 738 | 739 | 740 | 741 | 742 | 743 | 744 | 745 | 746 | 747 | 748 | 749 | 750 |

751 | 752 | 753 | 754 | 755 | 756 | 757 | 758 | 759 | 760 | 761 | 762 | 763 | 764 | 765 | 766 | 767 | 768 | 769 | 770 | 771 | 772 | 773 | 774 | 775 |

776 | 777 | 778 | 779 | 780 | 781 | 782 | 783 | 784 | 785 | 786 | 787 | 788 | 789 | 790 | 791 | 792 | 793 | 794 | 795 | 796 | 797 | 798 | 799 | 800 |

801 | 802 | 803 | 804 | 805 | 806 | 807 | 808 | 809 | 810 | 811 | 812 | 813 | 814 | 815 | 816 | 817 | 818 | 819 | 820 | 821 | 822 | 823 | 824 | 825 |

826 | 827 | 828 | 829 | 830 | 831 | 832 | 833 | 834 | 835 | 836 | 837 | 838 | 839 | 840 | 841 | 842 | 843 | 844 | 845 | 846 | 847 | 848 | 849 | 850 |

851 | 852 | 853 | 854 | 855 | 856 | 857 | 858 | 859 | 860 | 861 | 862 |

The 310 solved problems (that's level 12) had an average difficulty of 32.6&percnt; at Project Euler and
I scored 13526 points (out of 15700 possible points, top rank was 17 out of &approx;60000 in August 2017) at Hackerrank's [Project Euler+][338].

My username at Project Euler is **stephanbrumme**while it's [stbrumme][339] at Hackerrank.

Look at my [progress][7] and [performance][6] pages to get more details.

# Copyright

I hope you enjoy my code and learn something - or give me feedback how I can improve my solutions.
All of my solutions can be used for any purpose and I am in no way liable for any damages caused.
You can even remove my name and claim it's yours. But then you shall burn in hell.

The problems and most of the problems' images were created by [Project Euler][26].
Thanks for all their endless effort !!!

[<< problem 349 - Langton's ant][9] | [10] | [Prime generating integers - problem 357 >>][11] |

more about me can be found on my [homepage][340], especially in my [coding blog][341].
some names mentioned on this site may be trademarks of their respective owners.
thanks to the [KaTeX team][342] for their great typesetting library !


## Links

[1]: /
[2]: /why/
[3]: /toolbox/
[4]: /techniques/
[5]: /inside/
[6]: /performance/
[7]: /progress/
[8]: /news/
[9]: /349/
[10]: https://projecteuler.net/problem=351
[11]: /357/
[12]: https://en.wikipedia.org/wiki/Triangular_number
[13]: https://en.wikipedia.org/wiki/Euler%27s_totient_function
[14]: http://mathworld.wolfram.com/TotientSummatoryFunction.html
[15]: ../toolbox/
[16]: 351.cpp
[17]: https://github.com/stbrumme/euler/blob/master/euler-0351.cpp
[18]: ../performance/
[19]: ../214/
[20]: http://www.oeis.org/A216453
[21]: https://projecteuler.net/thread=351
[22]: https://github.com/Meng-Gen/ProjectEuler/blob/master/351.cc
[23]: https://github.com/roosephu/project-euler/blob/master/351.cpp
[24]: https://github.com/LaurentMazare/ProjectEuler/blob/master/e351.c
[25]: https://github.com/thrap/project-euler/blob/master/src/Java/Problem351.java
[26]: https://projecteuler.net
[27]: /1/
[28]: /2/
[29]: /3/
[30]: /4/
[31]: /5/
[32]: /6/
[33]: /7/
[34]: /8/
[35]: /9/
[36]: /10/
[37]: /11/
[38]: /12/
[39]: /13/
[40]: /14/
[41]: /15/
[42]: /16/
[43]: /17/
[44]: /18/
[45]: /19/
[46]: /20/
[47]: /21/
[48]: /22/
[49]: /23/
[50]: /24/
[51]: /25/
[52]: /26/
[53]: /27/
[54]: /28/
[55]: /29/
[56]: /30/
[57]: /31/
[58]: /32/
[59]: /33/
[60]: /34/
[61]: /35/
[62]: /36/
[63]: /37/
[64]: /38/
[65]: /39/
[66]: /40/
[67]: /41/
[68]: /42/
[69]: /43/
[70]: /44/
[71]: /45/
[72]: /46/
[73]: /47/
[74]: /48/
[75]: /49/
[76]: /50/
[77]: /51/
[78]: /52/
[79]: /53/
[80]: /54/
[81]: /55/
[82]: /56/
[83]: /57/
[84]: /58/
[85]: /59/
[86]: /60/
[87]: /61/
[88]: /62/
[89]: /63/
[90]: /64/
[91]: /65/
[92]: /66/
[93]: /67/
[94]: /68/
[95]: /69/
[96]: /70/
[97]: /71/
[98]: /72/
[99]: /73/
[100]: /74/
[101]: /75/
[102]: /76/
[103]: /77/
[104]: /78/
[105]: /79/
[106]: /80/
[107]: /81/
[108]: /82/
[109]: /83/
[110]: /84/
[111]: /85/
[112]: /86/
[113]: /87/
[114]: /88/
[115]: /89/
[116]: /90/
[117]: /91/
[118]: /92/
[119]: /93/
[120]: /94/
[121]: /95/
[122]: /96/
[123]: /97/
[124]: /98/
[125]: /99/
[126]: /100/
[127]: /101/
[128]: /102/
[129]: /103/
[130]: /104/
[131]: /105/
[132]: /106/
[133]: /107/
[134]: /108/
[135]: /109/
[136]: /110/
[137]: /111/
[138]: /112/
[139]: /113/
[140]: /114/
[141]: /115/
[142]: /116/
[143]: /117/
[144]: /118/
[145]: /119/
[146]: /120/
[147]: /121/
[148]: /122/
[149]: /123/
[150]: /124/
[151]: /125/
[152]: /126/
[153]: /127/
[154]: /128/
[155]: /129/
[156]: /130/
[157]: /131/
[158]: /132/
[159]: /133/
[160]: /134/
[161]: /135/
[162]: /136/
[163]: /137/
[164]: /138/
[165]: /139/
[166]: /141/
[167]: /142/
[168]: /144/
[169]: /145/
[170]: /146/
[171]: /147/
[172]: /148/
[173]: /149/
[174]: /150/
[175]: /151/
[176]: /152/
[177]: /154/
[178]: /155/
[179]: /156/
[180]: /158/
[181]: /159/
[182]: /160/
[183]: /161/
[184]: /162/
[185]: /163/
[186]: /164/
[187]: /165/
[188]: /166/
[189]: /168/
[190]: /169/
[191]: /170/
[192]: /171/
[193]: /172/
[194]: /173/
[195]: /174/
[196]: /178/
[197]: /179/
[198]: /181/
[199]: /182/
[200]: /183/
[201]: /185/
[202]: /186/
[203]: /187/
[204]: /188/
[205]: /189/
[206]: /190/
[207]: /191/
[208]: /193/
[209]: /196/
[210]: /197/
[211]: /199/
[212]: /200/
[213]: /201/
[214]: /203/
[215]: /204/
[216]: /205/
[217]: /206/
[218]: /207/
[219]: /208/
[220]: /209/
[221]: /211/
[222]: /213/
[223]: /214/
[224]: /215/
[225]: /216/
[226]: /218/
[227]: /219/
[228]: /222/
[229]: /225/
[230]: /226/
[231]: /227/
[232]: /229/
[233]: /230/
[234]: /231/
[235]: /232/
[236]: /234/
[237]: /235/
[238]: /237/
[239]: /239/
[240]: /240/
[241]: /243/
[242]: /244/
[243]: /247/
[244]: /248/
[245]: /249/
[246]: /250/
[247]: /259/
[248]: /260/
[249]: /265/
[250]: /266/
[251]: /267/
[252]: /268/
[253]: /273/
[254]: /274/
[255]: /277/
[256]: /278/
[257]: /279/
[258]: /280/
[259]: /284/
[260]: /286/
[261]: /287/
[262]: /288/
[263]: /290/
[264]: /291/
[265]: /293/
[266]: /297/
[267]: /300/
[268]: /301/
[269]: /303/
[270]: /304/
[271]: /306/
[272]: /307/
[273]: /308/
[274]: /309/
[275]: /310/
[276]: /313/
[277]: /315/
[278]: /317/
[279]: /321/
[280]: /323/
[281]: /324/
[282]: /327/
[283]: /329/
[284]: /333/
[285]: /336/
[286]: /341/
[287]: /343/
[288]: /345/
[289]: /346/
[290]: /347/
[291]: /348/
[292]: /358/
[293]: /359/
[294]: /363/
[295]: /371/
[296]: /375/
[297]: /381/
[298]: /386/
[299]: /387/
[300]: /393/
[301]: /401/
[302]: /407/
[303]: /411/
[304]: /412/
[305]: /418/
[306]: /425/
[307]: /429/
[308]: /436/
[309]: /455/
[310]: /458/
[311]: /461/
[312]: /473/
[313]: /485/
[314]: /491/
[315]: /493/
[316]: /500/
[317]: /501/
[318]: /504/
[319]: /510/
[320]: /516/
[321]: /518/
[322]: /523/
[323]: /539/
[324]: /549/
[325]: /563/
[326]: /565/
[327]: /571/
[328]: /577/
[329]: /581/
[330]: /587/
[331]: /601/
[332]: /607/
[333]: /610/
[334]: /611/
[335]: /612/
[336]: /613/
[337]: /615/
[338]: https://www.hackerrank.com/contests/projecteuler/challenges
[339]: https://www.hackerrank.com/stbrumme
[340]: https://stephan-brumme.com
[341]: https://create.stephan-brumme.com
[342]: https://khan.github.io/KaTeX/
