<!-- source: https://research.ibm.com/haifa/ponderthis/challenges/April2004.html | converted from HTML -->

Ponder This Challenge - April 2004 - Labeling VCR cassettes using digit stickers - IBM Research

Ponder This Challenge:

This month's puzzle comes from Michael Brand.

My friend compulsively records television programs on his VCR. To this end, he has a very large stock of VCR cassettes. He has long given up on trying to label these cassettes with any meaningful names. Now he just numbers them. The numbers go from 1 up and are consecutive.

In order to label the cassettes, he uses the digit stickers that come with a bought cassette. Each cassette comes with one sticker for each digit.

So, for example, to label the first cassette, he uses just the sticker "1" and keeps the rest. To label the second, he uses just the sticker "2" and keeps the rest. To label the tenth, he uses two stickers, one "1" and one "0", and keeps the rest. To label the eleventh, he uses one "1" sticker from the stickers he just got, and one "1" sticker which he had in stock from the previous ten. And so on.

The question is, what is the number of the first cassette which he will no longer be able to label in this way (i.e., that will deplete his stock of stickers to the point that he will not be able to form the desired number)? Please give your answer for general B, as well as for B=10. Please supply a proof if posssible.

In order to make the question interesting (and avoid simple programmatic solutions), the solver should give a closed formula for the number as a function of B, where B is the base in which my friend counts (assume that the cassettes come with one sticker for each digit of the base used). So, for example, if my friend chooses to count in hexadecimal, this is because each cassette comes with 16 stickers, that are "0", "1", "2", ... , "F"). The closed formula need only work for B's that are even numbers, such as decimal, octal, hexadecimal and binary. I am not aware of the existence of a closed formula for the odd numbered bases.

As usual, preference is given to closed-form solutions (no recursion, no sums). Each proof is expected to be your own; it's no fair using a proof that you've seen elsewhere.

---

We will post the names of those who submit a correct, original solution! If you don't want your name posted then please include such a statement in your submission!

We invite visitors to our website to submit an elegant solution. Send your submission to the [ponder@il.ibm.com][1].

*If you have any problems you think we might enjoy, please send them in. All replies should be sent to:*[ponder@il.ibm.com][2]

## Solution

-

Click here to view the solution

**April 2004 Solution:**

The first thing to note is that the "1"s digit is always the one with the lowest stock. Therefore, it must be the digit that will run out first. All other digits are inconsequential. We will use the notation s(x) to denote the number of "1"s that are in stock after labelling the x'th cassette. s(x) can be negative to indicate a deficit in "1"s. We are interested in the lowest x for which s(x) is negative.

Note that the required x must have at least two "1"s, or else
s(x)≥s(x-1).

Second, note that the first unlabellable cassette must have a number of the form 1XYZ... . That is, its most significant digit must be "1". The reason for this is that if the string UVW (of any length) has no "1"s, then

s(UVW1XYZ...) - s(UVW0000...) = s(1XYZ...)

If "UVW1XYZ..." is the first unlabellable cassette, then s(UVW1XYZ...) must be smaller than s(UVW0000...), meaning that s(1XYZ...) is smaller than zero. Because "UVW1XYZ..." is larger than "1XYZ..." it can not be the required solution.

Third, notice that when x is of the form "1XYZ...", s(x) is monotonously decreasing (in a weak sense). For this reason, it is not necessary to inspect each X of that form, but only those x's of the form "1999..." (where "9" represents the "B-1" digit) in order to know in which block of numbers of the form 1XYZ... the x we are looking for is. In particular:

s(2*B^n-1) = (2*B^n-1) - B^n - n*2*B^(n-1) "where "^" denotes exponentiation."

The first term is the number of "1"s we got. The second is the number of "1"s used to label the most digit in the B^n position. The final term states that for each of the preceding n places, exactly 1/B of the digits used were "1"s.

Therefore:

s(2*B^n-1) = (2B-B-2n)*B^(n-1) - 1 = (B-2n)*B^(n-1) - 1

Clearly, the streak of numbers of the form "1XYZ..." in which the number we are looking for resides is the one between B^(B/2) and 2*B^(B/2)-1.

When reaching y=2*B^(B/2)-1 our stock is at s(y)=-1. So, all we need to do is to find the highest number that is smaller than y that has more than a single appearance of the digit "1". This will be the number in which s(x) becomes -1 from a non-negative value for the first time, and is therefore our solution.

This number is 2*B^(B/2)+1-B, which has "1" both in the most significant digit and in the least significant digit. For base ten, this value is 199991, which is significantly smaller than most people initially guess.

John Fletcher gives the following interesting treatment of the case of odd B:

Let c(b, n) be the number of occurrences of digit b, 0 <= b < B, among all the numerals n', 0 < n' <= n, expressed in radix B >= 2 without leading 0's.

Lemma: For all b and n, c(1, n) >= c(b, n).
Proof: There is a 1-to-1 mapping between the occurrences of any particular digit b != 1 and the occurrences of digit 1, with digit b in the bit position valued B^d, d >= 0, of numeral n' being paired with digit 1 in the same bit position of a lesser numeral, n' - (b-1)*B^d if b > 1 or n' - (B-1)*B^d if b = 0. So for every occurrence of digit b contributing to c(b, n) there is an occurrence of digit 1 contributing to c(1, n) -- QED. Let C(n) = c(1, n) and E(n) = C(n)-n, the desired integer N being the least such that E(N) > 0. Let Z = B-1, the largest digit.

Lemma: The leading (leftmost) digit of N must be 1.
Proof: Assume N to have a leading digit b > 1. Let M be the largest numeral less than N with a leading 1 (its digits being 1ZZ...Z), let m be the largest numeral with one fewer digits than N (ZZ...Z), and let m' be N with its leading digit removed; so E(N) = E(M) + (d-2)*E(m) + E(m'). Since M < N, m < N, and m' < N, it must be that E(M) <= 0, E(m) <= 0, E(m') <= 0, and consequently E(N) <= 0, a contradiction -- QED, reductio ad absurdum. So 1 followed by D >= 0 additional digits expresses N.

Let K = 2*B^D - 1 be the largest number expressed as 1 followed by D digits (1ZZ...Z); so C(K) = B^D + 2*D*B^(D-1) and E(K) = (2*D-B)*B^(D-1) + 1. Since E(k) is monotonically non-decreasing when N <= k <= K, it must be that E(K) >= E(N) > 0; so D is the least integer such that 2*D >= B. If B is even, then D = B/2 and E(K) = 1; so N is the largest integer not exceeding K expressed with at least two 1's, namely 2*B^(B/2) - B + 1 (1ZZ...Z1, where the Z's are B/2 - 1 in number) -- QED for even N.

If B is odd, then D = (B+1)/2 and E(K) = B^((B-1)/2) + 1, and there seems to be no simple expression for N. A C-language algorith given later, O(B) in the number of arithmetic and logical operations, implements a division-like procedure that finds N (for B either even or odd) -- QED: Using 012...89AB...YZ as digits, the N's for even B include binary 11, octal 17771, decimal 199991, and hexadecimal 1FFFFFFF1; for small odd B they are given in a table later.

When B is composite these show a tendency for some rightmost digits to have the form ...ZZZ1, just like all digits except the leftmost when B is even.

Counting digits from right to left starting with 0, let NN[d] = B-1-N[d] be the dth digit of NN, the "complement" of N. Assume that, except for d = D (the leftmost digit) and d = 0 (the rightmost digit), N[d] > 1, so that NN[d] < B-2. Then in the algorithm for N[d], L-1 always equals 0, inc always equals d, and only the last ("else") alternative applies for D > d > 0. A bit of algebra then shows that each successive NN[d] from left to right is obtained as the quotient when B*r is divided by d, where r is the remainder obtained from the division to obtain the preceding digit NN[d+1], the initial remainder for d = D being set to 1. (The full algorithm -- no assumptions -- for NN[d] when B is odd is as follows:

int complement (B, NN)
int B; /* radix (odd only) */
int NN[ ]; /* pointer to digits of complement */ {
int D; /* index (power of B) of leftmost digit */
int d; /* index of current digit */
int L; /* count of (B-2)'s among digits indexed >= d */
int r; /* count/(B to the d-1) of (B-2)'s still needed */
int inc; /* rate/(B to the d-1) of increase of (B-2)'s */

D = (B+1)/2;
NN[D] = B-2, r = 1, L = 1; /* find leftmost digit */
for (d = D-1; d > 0; d--) { /* from left to right, */
r *= B, inc = (L-1)*B + d; /* find further digits */
if (r < (B-2)*inc) /* digit < B-2 ? */
NN[d] = r/inc, r %= inc;
else if (r < (B-1)*inc+B) /* digit == B-2 ? */
NN[d] = B-2, r -= (B-2)*inc, L++;
else /* digit == B-1 */
NN[d] = B-1, r -= (B-1)*inc+B; }
inc = L-1; /* find rightmost digit */
if (r < (B-2)*inc) /* digit < B-2 ? */
NN[0] = r/inc;
else if (r < (B-1)*inc+1) /* digit == B-2 ? */
NN[0] = B-2;
else /* digit == B-1 */
NN[0] = B-1;
return D; } /* return digit count */ )

Clearly, if the remainder r equals 0 for d = D', then it also equals zero for all succeeding d in the range D' > d > 0, with NN[d] = 0 (that is, N[d] = B-1); also NN[0] = B-2 (that is, N[0] = 1). Moreover, r surely equals 0 when d is a divisor of B, perhaps (depending on the value of the preceding r) also when d is a multiple of a proper divisor.

All this implies that, except in the following two cases, D' rightmost digits of N are of the form ...ZZZ1, where D' is a multiple of a proper divisor of B and is no less than the largest proper divisor: (1) If B is a prime, then the form does not appear because there are no proper divisors. (2) If NN[d] = B-2 (that is, N[d] = 1) happens to occur for some d equal to or greater than what would be D', then the assumptions are violated, and the form does not appear. These conclusions are illustrated by the following results for small B (where the digits are 012...89AB...YZab...yz):

 |  |  |  |

B | N | NN | D' |

3: | 111 | 111 | 1 |

5: | 1212 | 3232 |  |

7: | 14314 | 52352 |  |

9: | 165881 | 723007 | 3 |

11: | 18815A0 | 922950A |  |

13: | 1AA317A1 | B229B52B | 1 |

15: | 1CC5EEEE1 | D2290000D | 5 |

17: | 1EE86CB1D2 | F228A45F3E |  |

19: | 1GGAFF1C17E | H22833H6HB4 |  |

21: | 1IID1A1G8I28 | J227JAJ4C2IC |  |

23: | 1KKF5G7DH1HAB | L227H6F95L5CB |  |

25: | 1MMHB1CC1K8O0O | N227DNCCN4G0O0 |  |

27: | 1OOJG2QQQQQQQQ1 | P227AO00000000P | 9 |

29: | 1QQLL1DL40NPDGO3 | R2277RF7OS53FC4P |  |

31: | 1SSNPP96R1J7N0S4P | T22755LO3TBN7U2Q5 |  |

33: | 1UUPUDNWWWWWWWWWW1 | V2272J90000000000V | 11 |

35: | 1WWRYYYYYYYYYYYYYY1 | X22700000000000000X | 15 |

37: | 1YYU1F84J9G2GU3IZ4R8 | Z226ZLSWHRKYK6XI1W9S |  |

39: | 1aaW2FM8cccccccccccc1 | b226aNGU000000000000b | 13 |

41: | 1ccY4XAc1KaAI1EUBCFbNS | d226a7U2dK4UMdQATSP3HC |  |

43: | 1eea751JBD1WF9LLB8g1QdF | f226ZbfNVTfARXLLVY0fG3R |  |

45: | 1ggc9Jiiiiiiiiiiiiiiiii1 | h226ZP00000000000000000h | 18 |

47: | 1iieBYSX5eXPBY4VBXNIZ1fAZ | j226ZCIDf6DLZCgFZDNSBj5aB |  |

49: | 1kkgDmmmmmmmmmmmmmmmmmmmm1 | l226Z00000000000000000000l | 21 |

51: | 1mmiG9ZYjEoooooooooooooooo1 | n226YfFG5a0000000000000000n | 17 |

53: | 1ookILZFlKV6VfWUm5Bdbi1ham8h | p226YVHb5WLkLBKM4lfDF8p9G4i9 |  |

55: | 1qqmKXOsssssssssssssssssssss1 | r226YLU000000000000000000000r | 22 |

57: | 1ssoMj4sLdouuuuuuuuuuuuuuuuuu1 | t226YBq2ZH6000000000000000000t | 19 |

59: | 1uuqOuapG2l9GKlt1a2ScRirbBw2oGf | v226Y2M7guBngcB3vMuUKVE5Ll0u8gH |  |

61: | 1wwsR4fRwJNC9bEJ1aaFrMK1rQCTWCHp | x226XuJX2fbmpNkfxOOj7cex7YmVSmh9 |  |

Note that the indicated form appears only for composite B, with D' being no less than the largest proper divisor of B and having a common proper factor with B. That D' = 1 for B = 3 and for B = 13 reflects the fact that -- by "chance" -- N[0] happens to equal 1.) Also, the form does not appear for B = 21 or B = 25, because N[d] = 1 for d = 7 or d = 8, respectively, which equals or exceeds the minimum possible D', namely 7 or 5, respectively.

## Solvers

- **Satish Vedantam**(4.1.2004 @10:14:43 AM EDT)
- **Luke Pebody**(4.1.2004 @02:11:16 PM EDT)
- **Eugene Vasilchenko**(4.1.2004 @02:50:43 PM EDT)
- **Daniel Wood**(4.1.2004 @05:22:50 PM EDT)
- **Graeme McRae**(4.1.2004 @08:02:29 PM EDT)
- **Coserea Gheorghe**(4.1.2004 @08:24:32 PM EDT)
- **John Lister**(4.1.2004 @08:31:34 PM EDT)
- **Dan Dima**(4.1.2004 @11:57:11 PM EDT)
- **M.Venkata Ramayya**(4.2.2004 @04:31:35 AM EDT)
- **Amod Kulkarni**(4.2.2004 @04:31:35 AM EDT)
- **Anand**(4.2.2004 @07:18:23 AM EDT)
- **Trevor Graffa**(4.2.2004 @04:30:46 AM EDT)
- **Stephane Peysson**(4.2.2004 @08:49:18 AM EDT)
- **Roberto Tauraso**(4.2.2004 @09:42:37 AM EDT)
- **John Tromp**(4.2.2004 @12:18:00 PM EDT)
- **Narayanan Rajamani**(4.2.2004 @01:48:26 PM EDT)
- **Sean Owen**(4.2.2004 @03:29:34 PM EDT)
- **Dave Blackston**(4.2.2004 @03:48:31 PM EDT)
- **Gyozo Nagy**(4.2.2004 @05:23:00 PM EDT)
- **Brian Bitto**(4.2.2004 @05:51:25 PM EDT)
- **Hongli Xu**(4.2.2004 @09:05:52 PM EDT)
- **Amit Chattopadhyay**(4.3.2004 @03:47:16 AM EDT)
- **Daidi**(4.3.2004 @07:10:21 AM EDT)
- **Al Zimmermann**(4.3.2004 @03:14:57 PM EDT)
- **L.J. Zigerell Jr.**(4.3.2004 @03:43:35 PM EDT)
- **ILan Algor**(4.4.2004 @11:51:41 AM EDT)
- **Frank Mullin**(4.4.2004 @12:18:54 PM EDT)
- **Rock Verser**(4.5.2004 @08:10:27 AM EDT)
- **Clive Tong**(4.5.2004 @10:47:20 AM EDT)
- **Peter Mattsson**(4.5.2004 @11:12:00 AM EDT)
- **K**(4.5.2004 @11:34:03 AM EDT)
- **alyana Chakravarthy**(4.5.2004 @11:34:03 AM EDT)
- **Kenned**(4.6.2004 @01:14:57 AM EDT)
- **y**(4.6.2004 @01:14:57 AM EDT)
- **Luca Dalla Valle**(4.6.2004 @06:44:17 AM EDT)
- **Daragó László**(4.7.2004 @04:29:35 AM EDT)
- **Vardhan**(4.7.2004 @08:52:01 AM EDT)
- **Ross Millikan**(4.7.2004 @02:11:11 PM EDT)
- **Anneke Van Steirteghem**(4.7.2004 @04:31:53 PM EDT)
- **Arun Mandayam Krishnakumar**(4.8.2004 @03:42:34 AM EDT)
- **Joe BGI SF**(4.8.2004 @10:56:38 AM EDT)
- **Fendel**(4.8.2004 @10:56:38 AM EDT)
- **Joe Vanore**(4.8.2004 @05:46:06 PM EDT)
- **Vishal Mamania**(4.9.2004 @02:53:01 PM EDT)
- **Tim Deegan**(4.9.2004 @03:59:55 PM EDT)
- **David Friedman**(4.9.2004 @04:11:37 PM EDT)
- **Vinko Marinkovic**(4.10.2004 @01:36:17 AM EDT)
- **Nikhil Sahasrabudhe**(4.10.2004 @03:59:42 AM EDT)
- **Claudio Baiocchi**(4.11.2004 @01:04:29 PM EDT)
- **John Fletcher**(4.11.2004 @07:27:57 PM EDT)
- **Vineet Batra**(4.12.2004 @06:47:18 AM EDT)
- **Andre Rzym**(4.12.2004 @01:07:36 PM EDT)
- **Sriram Sankaranarayanan**(4.12.2004 @08:41:58 PM EDT)
- **Vincent Vermaut**(4.13.2004 @08:38:18 AM EDT)
- **K**(4.14.2004 @08:28:41 AM EDT)
- **rishna Chaitanya**(4.14.2004 @08:28:41 AM EDT)
- **IQSTAR**(4.14.2004 @01:58:02 PM EDT)
- **Karl D'Souza & Cristian Ianculescu**(4.14.2004 @02:39:23 PM EDT)
- **Paul Botham**(4.14.2004 @03:53:00 PM EDT)
- **John David**(4.14.2004 @10:56:50 PM EDT)
- **Vessey**(4.14.2004 @10:56:50 PM EDT)
- **Mohit Srivastava**(4.15.2004 @08:08:19 AM EDT)
- **Bob**(4.16.2004 @06:45:00 AM EDT)
- **Stewart**(4.16.2004 @06:45:00 AM EDT)
- **David P Woodruff**(4.16.2004 @08:28:22 PM EDT)
- (4.16.2004 @08:28:22 PM EDT)
- **Emile Joubert**(4.18.2004 @03:46:16 PM EDT)
- (4.18.2004 @03:46:16 PM EDT)
- **Michael Swart**(4.19.2004 @11:52:40 AM EDT)
- (4.19.2004 @11:52:40 AM EDT)
- **Shmuel Spiegel**(4.19.2004 @11:26:54 PM EDT)
- (4.19.2004 @11:26:54 PM EDT)
- **Mayank M**(4.20.2004 @01:04:18 PM EDT)
- **Kabra**(4.20.2004 @01:04:18 PM EDT)
- **A**(4.21.2004 @07:26:28 AM EDT)
- **nanda Raidu**(4.21.2004 @07:26:28 AM EDT)
- (4.21.2004 @07:26:28 AM EDT)
- **Derek Kisman**(4.21.2004 @02:50:27 PM EDT)
- **Hagen von Eitzen**(4.22.2004 @05:00:56 AM EDT)
- **Siva Dirisala**(4.23.2004 @06:50:32 PM EDT)
- (4.23.2004 @06:50:32 PM EDT)
- **Nagachandra Sekhar Grandhi**(4.25.2004 @09:19:45 AM EDT)
- (4.25.2004 @09:19:45 AM EDT)
- **Srinivaasan**(4.25.2004 @10:49:33 PM EDT)
- **Markandan**(4.25.2004 @10:49:33 PM EDT)
- (4.25.2004 @10:49:33 PM EDT)
- **Daniel Chong Jyh Tar**(4.26.2004 @12:32:57 AM EDT)
- (4.26.2004 @12:32:57 AM EDT)
- **Wolfgang Kais**(4.26.2004 @10:07:44 AM EDT)
- **Mihai Cioc**(4.26.2004 @03:33:03 PM EDT)
- (4.26.2004 @03:33:03 PM EDT)
- **Raj Mohan**(4.27.2004 @08:41:15 PM EDT)
- **Kumar**(4.29.2004 @05:05:16 AM EDT)
- **R. Nandakumar**(4.29.2004 @07:35:39 AM EDT)
- **Frans Buijsen**(4.29.2004 @07:44:10 AM EDT)
- (4.29.2004 @07:44:10 AM EDT)
- **Mark Abramson**(4.29.2004 @02:28:35 PM EDT)
- (4.29.2004 @02:28:35 PM EDT)
- **Chris Shannon**(4.30.2004 @07:19:50 PM EDT)
- **Ervan Darnell**(4.30.2004 @10:53:06 PM EDT)
- **Peter Huggins**(5.01.2004 @01:45:41 PM EDT)
- **Praveen Jagadishprasad**(5.02.2004 @09:24:32 PM EDT)

## Related posts

-

### [Ponder This Challenge - August 2026 - The Wheel of Buttons][3]

Puzzle

Gadi Aleksandrowicz

31 Jul 2026

  -

Ponder This

-

### [Ponder This Challenge - July 2026 - Return of the Superheroes][4]

Puzzle

Gadi Aleksandrowicz

01 Jul 2026

  -

Ponder This

-

### [Ponder This Challenge - June 2026 - The Superhero Team Movies][5]

Puzzle

Gadi Aleksandrowicz

01 Jun 2026

  -

Ponder This

-

### [Ponder This Challenge - May 2026 - The Powers of a Binary Matrix][6]

Puzzle

Gadi Aleksandrowicz

01 May 2026

  -

Ponder This


## Links

[1]: mailto:ponder@il.ibm.com?subject=ANSWER%3A%20April%202004%20Ponder%20This
[2]: mailto:ponder@il.ibm.com?Subject=PUZZLE%20SUGGESTION%3A&amp;Body=Please%20include%20the%20answer%20with%20your%20submission.
[3]: /blog/ponder-this-august-2026
[4]: /blog/ponder-this-july-2026
[5]: /blog/ponder-this-june-2026
[6]: /blog/ponder-this-may-2026
