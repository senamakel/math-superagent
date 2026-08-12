<!-- source: https://en.wikipedia.org/wiki/Ballot_problem | converted from HTML -->

Bertrand's ballot theorem - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

(Redirected from [Ballot problem][1])

Election result probability theorem

In [combinatorics][2], **Bertrand's ballot problem**is the question: "In an [election][3] where candidate A receives *p*votes and candidate B receives *q*votes with *p*>*q*, what is the [probability][4] that A will be strictly ahead of B throughout the count under the assumption that votes are counted in a randomly picked order?" The answer is

p − q p + q. {\displaystyle {\frac {p-q}{p+q}}.}[image: {\displaystyle {\frac {p-q}{p+q}}.}]

The result was first published by [W. A. Whitworth][5] in 1878, but is named after [Joseph Louis François Bertrand][6] who rediscovered it in 1887. [1] [2] [3] [4] [5]

In Bertrand's original paper, he sketches a proof based on a general formula for the number of favourable sequences using a [recursion relation][7]. He remarks that it seems probable that such a simple result could be proved by a more direct method. Such a proof was given by [Désiré André][8], [6] based on the observation that the unfavourable sequences can be divided into two equally probable cases, one of which (the case where B receives the first vote) is easily computed; he proves the equality by an explicit [bijection][9]. A variation of his method is popularly known as **André's reflection method**, although André did not use any reflections. [7]

Bertrand's ballot theorem is related to the **cycle lemma**. They give similar formulas, but the cycle lemma considers [circular shifts][10] of a given ballot counting order rather than all permutations.

## Example

[[edit][11]]

Suppose there are 5 voters, of whom 3 vote for candidate *A*and 2 vote for candidate *B*(so *p*= 3 and *q*= 2). There are ten equally likely orders in which the votes could be counted:

- *AAABB*
- *AABAB*
- *ABAAB*
- *BAAAB*
- *AABBA*
- *ABABA*
- *BAABA*
- *ABBAA*
- *BABAA*
- *BBAAA*

For the order *AABAB*, the tally of the votes as the election progresses is:

Candidate | *A* | *A* | *B* | *A* | *B* |

*A* | 1 | 2 | 2 | 3 | 3 |

*B* | 0 | 0 | 1 | 1 | 2 |

For each column the tally for *A*is always larger than the tally for *B*, so *A*is always strictly ahead of *B*. For the order *AABBA*the tally of the votes as the election progresses is:

Candidate | *A* | *A* | *B* | *B* | *A* |

*A* | 1 | 2 | 2 | 2 | 3 |

*B* | 0 | 0 | 1 | 2 | 2 |

For this order, *B*is tied with *A*after the fourth vote, so *A*is not always strictly ahead of *B*. Of the 10 possible orders, *A*is always ahead of *B*only for *AAABB*and *AABAB*. So the probability that *A*will always be strictly ahead is

2 10 = 1 5, {\displaystyle {\frac {2}{10}}={\frac {1}{5}},}[image: {\displaystyle {\frac {2}{10}}={\frac {1}{5}},}]

and this is indeed equal to 3 − 2 3 + 2 {\displaystyle {\frac {3-2}{3+2}}}[image: {\displaystyle {\frac {3-2}{3+2}}}] as the theorem predicts.

## Equivalent problems

[[edit][12]]

### Favourable orders

[[edit][13]]

Rather than computing the probability that a random vote counting order has the desired property, one can instead compute the number of favourable counting orders, then divide by the total number of ways in which the votes could have been counted. (This is the method that was used by Bertrand.) The total number of ways is the [binomial coefficient][14] ( p + q p) {\displaystyle {\tbinom {p+q}{p}}}[image: {\displaystyle {\tbinom {p+q}{p}}}]; Bertrand's proof shows that the number of favourable orders in which to count the votes is ( p + q − 1 p − 1) − ( p + q − 1 p) {\displaystyle {\tbinom {p+q-1}{p-1}}-{\tbinom {p+q-1}{p}}}[image: {\displaystyle {\tbinom {p+q-1}{p-1}}-{\tbinom {p+q-1}{p}}}] (though he does not give this number explicitly). And indeed after division this gives p p + q − q p + q = p − q p + q {\displaystyle {\tfrac {p}{p+q}}-{\tfrac {q}{p+q}}={\tfrac {p-q}{p+q}}}[image: {\displaystyle {\tfrac {p}{p+q}}-{\tfrac {q}{p+q}}={\tfrac {p-q}{p+q}}}].

### Random walks

[[edit][15]]

Another related problem is to calculate the number of [random walks][16] on the [integers][17] that consist of *n*steps of unit length, beginning at the origin and ending at the point *m*, that never become negative. As *n*and *m*have the same parity and n ≥ m ≥ 0 {\displaystyle n\geq m\geq 0}[image: {\displaystyle n\geq m\geq 0}], this number is

( n n + m 2) − ( n n + m 2 + 1) = m + 1 n + m 2 + 1 ( n n + m 2). {\displaystyle {\binom {n}{\tfrac {n+m}{2}}}-{\binom {n}{{\tfrac {n+m}{2}}+1}}={\frac {m+1}{{\tfrac {n+m}{2}}+1}}{\binom {n}{\tfrac {n+m}{2}}}.}[image: {\displaystyle {\binom {n}{\tfrac {n+m}{2}}}-{\binom {n}{{\tfrac {n+m}{2}}+1}}={\frac {m+1}{{\tfrac {n+m}{2}}+1}}{\binom {n}{\tfrac {n+m}{2}}}.}]

When m = 0 {\displaystyle m=0}[image: {\displaystyle m=0}] and n {\displaystyle n}[image: {\displaystyle n}] is even, this gives the [Catalan number][18] 1 n 2 + 1 ( n n 2) {\displaystyle {\frac {1}{{\tfrac {n}{2}}+1}}{\binom {n}{\tfrac {n}{2}}}}[image: {\displaystyle {\frac {1}{{\tfrac {n}{2}}+1}}{\binom {n}{\tfrac {n}{2}}}}]. Thus the probability that a random walk is never negative and returns to origin at time n {\displaystyle n}[image: {\displaystyle n}] is 2 − n 1 n 2 + 1 ( n n 2) {\displaystyle 2^{-n}{\frac {1}{{\tfrac {n}{2}}+1}}{\binom {n}{\tfrac {n}{2}}}}[image: {\displaystyle 2^{-n}{\frac {1}{{\tfrac {n}{2}}+1}}{\binom {n}{\tfrac {n}{2}}}}]. By [Stirling's formula][19], when n → ∞ {\displaystyle n\to \infty }[image: {\displaystyle n\to \infty }], this probability is ∼ 2 2 π n − 3 / 2 {\displaystyle \sim 2{\sqrt {\frac {2}{\pi }}}n^{-3/2}}[image: {\displaystyle \sim 2{\sqrt {\frac {2}{\pi }}}n^{-3/2}}].

[Note that m, n {\displaystyle m,n}[image: {\displaystyle m,n}] have the same parity as follows: let P {\displaystyle P}[image: {\displaystyle P}] be the number of "positive" moves, i.e., to the right, and let N {\displaystyle N}[image: {\displaystyle N}] be the number of "negative" moves, i.e., to the left. Since P + N = n {\displaystyle P+N=n}[image: {\displaystyle P+N=n}] and P − N = m {\displaystyle P-N=m}[image: {\displaystyle P-N=m}], we have P = n + m 2 {\displaystyle P={\frac {n+m}{2}}}[image: {\displaystyle P={\frac {n+m}{2}}}] and N = n − m 2 {\displaystyle N={\frac {n-m}{2}}}[image: {\displaystyle N={\frac {n-m}{2}}}]. Since P {\displaystyle P}[image: {\displaystyle P}] and N {\displaystyle N}[image: {\displaystyle N}] are integers, m, n {\displaystyle m,n}[image: {\displaystyle m,n}] have the same parity]

## Proof by reflection

[[edit][20]]

For A to be strictly ahead of B throughout the counting of the votes, there can be no ties. Separate the counting sequences according to the first vote. Any sequence that begins with a vote for B must reach a tie at some point, because A eventually wins. For any sequence that begins with A and reaches a tie, reflect the votes up to the point of the first tie (so any A becomes a B, and vice versa) to obtain a sequence that begins with B. Hence every sequence that begins with A and reaches a tie is in one-to-one correspondence with a sequence that begins with B, and the probability that a sequence begins with B is q / ( p + q) {\displaystyle q/(p+q)}[image: {\displaystyle q/(p+q)}], so the probability that A always leads the vote is

= 1 − {\displaystyle =1-}[image: {\displaystyle =1-}] the probability of sequences that tie at some point = 1 − {\displaystyle =1-}[image: {\displaystyle =1-}] the probability of sequences that tie at some point and begin with A or B = 1 − 2 × ( {\displaystyle =1-2\times (}[image: {\displaystyle =1-2\times (}] the probability of sequences that tie at some point and begin with B ) {\displaystyle )}[image: {\displaystyle )}] = 1 − 2 × ( {\displaystyle =1-2\times (}[image: {\displaystyle =1-2\times (}] the probability that a sequence begins with B ) {\displaystyle )}[image: {\displaystyle )}] = 1 − 2 q p + q = p − q p + q {\displaystyle =1-2{\frac {q}{p+q}}={\frac {p-q}{p+q}}}[image: {\displaystyle =1-2{\frac {q}{p+q}}={\frac {p-q}{p+q}}}]

## Proof by induction

[[edit][21]]

Another method of proof is by [mathematical induction][22]:

- We loosen the condition q"}}'> q}"> p > q {\displaystyle p>q} q}"/> to p ≥ q {\displaystyle p\geq q}[image: {\displaystyle p\geq q}]. Clearly, the theorem is correct when p = q {\displaystyle p=q}[image: {\displaystyle p=q}], since in this case the first candidate will not be *strictly*ahead after all the votes have been counted (so the probability is 0).
- Clearly the theorem is true if *p*> 0 and *q*= 0 when the probability is 1, given that the first candidate receives all the votes; it is also true when *p*=*q*> 0 as we have just seen.
- Assume it is true both when *p*=*a*− 1 and *q*=*b*, and when *p*=*a*and *q*=*b*− 1, with *a*>*b*> 0. (We don't need to consider the case a = b {\displaystyle a=b}[image: {\displaystyle a=b}] here, since we have already disposed of it before.) Then considering the case with *p*=*a*and *q*=*b*, the last vote counted is either for the first candidate with probability *a*/(*a*+*b*), or for the second with probability *b*/(*a*+*b*). So the probability of the first being ahead throughout the count to the penultimate vote counted (and also after the final vote) is:

a ( a + b) ( a − 1) − b ( a + b − 1) + b ( a + b) a − ( b − 1) ( a + b − 1) = a − b a + b. {\displaystyle {a \over (a+b)}{(a-1)-b \over (a+b-1)}+{b \over (a+b)}{a-(b-1) \over (a+b-1)}={a-b \over a+b}.}[image: {\displaystyle {a \over (a+b)}{(a-1)-b \over (a+b-1)}+{b \over (a+b)}{a-(b-1) \over (a+b-1)}={a-b \over a+b}.}]

- And so it is true for all *p*and *q*with *p*>*q*> 0.

## Proof by the cycle lemma

[[edit][23]]

A simple proof is based on the cycle lemma of Dvoretzky and Motzkin. [8] Call a ballot sequence *dominating*if A is strictly ahead of B throughout the counting of the votes. The cycle lemma asserts that any sequence of p {\displaystyle p}[image: {\displaystyle p}] A's and q {\displaystyle q}[image: {\displaystyle q}] B's, where q"}}'> q}"> p > q {\displaystyle p>q} q}"/>, has precisely p − q {\displaystyle p-q}[image: {\displaystyle p-q}] dominating cyclic permutations. To see this, just arrange the given sequence of p + q {\displaystyle p+q}[image: {\displaystyle p+q}] A's and B's in a circle and repeatedly remove adjacent pairs AB until only p − q {\displaystyle p-q}[image: {\displaystyle p-q}] A's remain. Each of these A's was the start of a dominating [cyclic permutation][24] before anything was removed. So p − q {\displaystyle p-q}[image: {\displaystyle p-q}] out of the p + q {\displaystyle p+q}[image: {\displaystyle p+q}] cyclic permutations of any arrangement of p {\displaystyle p}[image: {\displaystyle p}] A votes and q {\displaystyle q}[image: {\displaystyle q}] B votes are dominating.

## Proof by martingales

[[edit][25]]

Let n = p + q {\displaystyle n=p+q}[image: {\displaystyle n=p+q}]. Define the "backwards counting" [stochastic process][26]

X k = S n − k n − k; k = 0, 1,..., n − 1 {\displaystyle X_{k}={\frac {S_{n-k}}{n-k}};\quad k=0,1,...,n-1}[image: {\displaystyle X_{k}={\frac {S_{n-k}}{n-k}};\quad k=0,1,...,n-1}] where S n − k {\displaystyle S_{n-k}}[image: {\displaystyle S_{n-k}}] is the lead of candidate A over B, after n − k {\displaystyle n-k}[image: {\displaystyle n-k}] votes have come in.

Claim: X k {\displaystyle X_{k}}[image: {\displaystyle X_{k}}] is a [martingale][27] process.

Given X k {\displaystyle X_{k}}[image: {\displaystyle X_{k}}], we know that S n − k = ( n − k) X k {\displaystyle S_{n-k}=(n-k)X_{k}}[image: {\displaystyle S_{n-k}=(n-k)X_{k}}], so of the first n − k {\displaystyle n-k}[image: {\displaystyle n-k}] votes, X k + 1 2 ( n − k) {\displaystyle {\frac {X_{k}+1}{2}}(n-k)}[image: {\displaystyle {\frac {X_{k}+1}{2}}(n-k)}] were for candidate A, and − X k + 1 2 ( n − k) {\displaystyle {\frac {-X_{k}+1}{2}}(n-k)}[image: {\displaystyle {\frac {-X_{k}+1}{2}}(n-k)}] were for candidate B.

So, with probability X k + 1 2 {\displaystyle {\frac {X_{k}+1}{2}}}[image: {\displaystyle {\frac {X_{k}+1}{2}}}], we have S n − k − 1 = S n − k − 1 {\displaystyle S_{n-k-1}=S_{n-k}-1}[image: {\displaystyle S_{n-k-1}=S_{n-k}-1}], and X k + 1 = n − k n − k − 1 X k − 1 n − k − 1 {\displaystyle X_{k+1}={\frac {n-k}{n-k-1}}X_{k}-{\frac {1}{n-k-1}}}[image: {\displaystyle X_{k+1}={\frac {n-k}{n-k-1}}X_{k}-{\frac {1}{n-k-1}}}]. Similarly for the other one. Then compute to find E [X k + 1 | X k] = X k {\displaystyle E[X_{k+1}|X_{k}]=X_{k}}[image: {\displaystyle E[X_{k+1}|X_{k}]=X_{k}}].

Define the [stopping time][28] T {\displaystyle T}[image: {\displaystyle T}] as either the minimum k {\displaystyle k}[image: {\displaystyle k}] such that X k = 0 {\displaystyle X_{k}=0}[image: {\displaystyle X_{k}=0}], or n − 1 {\displaystyle n-1}[image: {\displaystyle n-1}] if there's no such k {\displaystyle k}[image: {\displaystyle k}]. Then the probability that candidate A leads all the time is just E [X T] {\displaystyle E[X_{T}]}[image: {\displaystyle E[X_{T}]}], which by the [optional stopping theorem][29] is E [X T] = E [X 0] {\displaystyle E[X_{T}]=E[X_{0}]}[image: {\displaystyle E[X_{T}]=E[X_{0}]}]. Using the final lead as S n {\displaystyle S_{n}}[image: {\displaystyle S_{n}}], and the definition of X k {\displaystyle X_{k}}[image: {\displaystyle X_{k}}] at 0, E [X 0] = p − q p + q {\displaystyle E[X_{0}]={\frac {p-q}{p+q}}}[image: {\displaystyle E[X_{0}]={\frac {p-q}{p+q}}}].

## Bertrand's and André's proofs

[[edit][30]]

Bertrand expressed the solution as

2 m − μ μ {\displaystyle {\frac {2m-\mu }{\mu }}}[image: {\displaystyle {\frac {2m-\mu }{\mu }}}]

where μ = p + q {\displaystyle \mu =p+q}[image: {\displaystyle \mu =p+q}] is the total number of voters and m = p {\displaystyle m=p}[image: {\displaystyle m=p}] is the number of voters for the first candidate. He states that the result follows from the formula

P m + 1, μ + 1 = P m, μ + P m + 1, μ, {\displaystyle P_{m+1,\mu +1}=P_{m,\mu }+P_{m+1,\mu },}[image: {\displaystyle P_{m+1,\mu +1}=P_{m,\mu }+P_{m+1,\mu },}]

where P m, μ {\displaystyle P_{m,\mu }}[image: {\displaystyle P_{m,\mu }}] is the number of favourable sequences, but "it seems probable that such a simple result could be shown in a more direct way". Indeed, a more direct proof was soon produced by Désiré André. His approach is often mistakenly labelled "the reflection principle" by modern authors but in fact uses a permutation. He shows that the "unfavourable" sequences (those that reach an intermediate tie) consist of an equal number of sequences that begin with A as those that begin with B. Every sequence that begins with B is unfavourable, and there are ( p + q − 1 q − 1) {\displaystyle {\tbinom {p+q-1}{q-1}}}[image: {\displaystyle {\tbinom {p+q-1}{q-1}}}] such sequences with a B followed by an arbitrary sequence of (*q*-1) B's and *p*A's. Each unfavourable sequence that begins with A can be transformed to an arbitrary sequence of (*q*-1) B's and *p*A's by finding the first B that violates the rule (by causing the vote counts to tie) and deleting it, and interchanging the order of the remaining parts. To reverse the process, take any sequence of (*q*-1) B's and *p*A's and search from the end to find where the number of A's first exceeds the number of B's, and then interchange the order of the parts and place a B in between. For example, the unfavourable sequence AAB B ABAA corresponds uniquely to the arbitrary sequence ABAA AAB. From this, it follows that the number of favourable sequences of *p*A's and *q*B's is

( p + q q) − 2 ( p + q − 1 q − 1) = ( p + q q) p − q p + q {\displaystyle {\binom {p+q}{q}}-2{\binom {p+q-1}{q-1}}={\binom {p+q}{q}}{\frac {p-q}{p+q}}}[image: {\displaystyle {\binom {p+q}{q}}-2{\binom {p+q-1}{q-1}}={\binom {p+q}{q}}{\frac {p-q}{p+q}}}]

and thus the required probability is

p − q p + q {\displaystyle {\frac {p-q}{p+q}}}[image: {\displaystyle {\frac {p-q}{p+q}}}]

as expected.

## Variant: ties allowed

[[edit][31]]

The original problem is to find the probability that the first candidate is always strictly ahead in the vote count. One may instead consider the problem of finding the probability that the second candidate is never ahead (that is, with ties are allowed). In this case, the answer is

p + 1 − q p + 1. {\displaystyle {\frac {p+1-q}{p+1}}.}[image: {\displaystyle {\frac {p+1-q}{p+1}}.}]

The variant problem can be solved by the reflection method in a similar way to the original problem. The number of possible vote sequences is ( p + q q) {\displaystyle {\tbinom {p+q}{q}}}[image: {\displaystyle {\tbinom {p+q}{q}}}]. Call a sequence "bad" if the second candidate is ever ahead, and if the number of bad sequences can be enumerated then the number of "good" sequences can be found by subtraction and the probability can be computed.

Represent a voting sequence as a [North-East lattice path][32] on the Cartesian plane as follows:

- Start the path at (0, 0)
- Each time a vote for the first candidate is received move right 1 unit.
- Each time a vote for the second candidate is received move up 1 unit.

Each such path corresponds to a unique sequence of votes and will end at (*p*, *q*). A sequence is 'good' exactly when the corresponding path never goes above the diagonal line *y*=*x*; equivalently, a sequence is 'bad' exactly when the corresponding path touches the line *y*=*x*+ 1.

[33] 'Bad' path (blue) and its reflected path (red)

For each 'bad' path *P*, define a new path *P*′ by reflecting the part of *P*up to the first point it touches the line across it. *P*′ is a path from (−1, 1) to (*p*,*q*). The same operation applied again restores the original *P*. This produces a one-to-one correspondence between the 'bad' paths and the paths from (−1, 1) to (*p*,*q*). The number of these paths is ( p + q q − 1) {\displaystyle {\tbinom {p+q}{q-1}}}[image: {\displaystyle {\tbinom {p+q}{q-1}}}] and so that is the number of 'bad' sequences. This leaves the number of 'good' sequences as

( p + q q) − ( p + q q − 1) = ( p + q q) p + 1 − q p + 1. {\displaystyle {\binom {p+q}{q}}-{\binom {p+q}{q-1}}={\binom {p+q}{q}}{\frac {p+1-q}{p+1}}.}[image: {\displaystyle {\binom {p+q}{q}}-{\binom {p+q}{q-1}}={\binom {p+q}{q}}{\frac {p+1-q}{p+1}}.}]

Since there are ( p + q q) {\displaystyle {\tbinom {p+q}{q}}}[image: {\displaystyle {\tbinom {p+q}{q}}}] altogether, the probability of a sequence being good is p + 1 − q p + 1 {\displaystyle {\tfrac {p+1-q}{p+1}}}[image: {\displaystyle {\tfrac {p+1-q}{p+1}}}].

In fact, the solutions to the original problem and the variant problem are easily related. For candidate A to be strictly ahead throughout the vote count, they must receive the first vote and for the remaining votes (ignoring the first) they must be either strictly ahead or tied throughout the count. Hence the solution to the original problem is

p p + q p − 1 + 1 − q p − 1 + 1 = p − q p + q {\displaystyle {\frac {p}{p+q}}{\frac {p-1+1-q}{p-1+1}}={\frac {p-q}{p+q}}}[image: {\displaystyle {\frac {p}{p+q}}{\frac {p-1+1-q}{p-1+1}}={\frac {p-q}{p+q}}}]

as required.

Conversely, the tie case can be derived from the non-tie case. Note that the *number*of non-tie sequences with p+1 votes for A is equal to the number of tie sequences with p votes for A. The number of non-tie votes with p + 1 votes for A votes is p + 1 − q p + 1 + q ( p + 1 + q q) {\displaystyle {\tfrac {p+1-q}{p+1+q}}{\tbinom {p+1+q}{q}}}[image: {\displaystyle {\tfrac {p+1-q}{p+1+q}}{\tbinom {p+1+q}{q}}}], which by algebraic manipulation is p + 1 − q p + 1 ( p + q q) {\displaystyle {\tfrac {p+1-q}{p+1}}{\tbinom {p+q}{q}}}[image: {\displaystyle {\tfrac {p+1-q}{p+1}}{\tbinom {p+q}{q}}}], so the *fraction*of sequences with p votes for A votes is p + 1 − q p + 1 {\displaystyle {\tfrac {p+1-q}{p+1}}}[image: {\displaystyle {\tfrac {p+1-q}{p+1}}}].

## Notes

[[edit][34]]

1. ↑ Barton, D. E.; Mallows, C. L. (1965). ["Some Aspects of the Random Sequence"][35]. *Ann. Math. Statist*. **36**: 236– 260. [doi][36]: [10.1214/aoms/1177700286][35].
2. ↑ [Feller, William][37] (1968), *An Introduction to Probability Theory and its Applications, Volume I*(3rd ed.), Wiley, p. 69.
3. ↑ Whitworth, W. A. (1878). ["Arrangements of m things of one sort and n things of another sort under certain conditions of priority"][38]. *Messenger of Math*. **8**: 105– 114. Retrieved 25 May 2024.
4. ↑ Whitworth, W. A. (1886). "Chapter V". *Choice and Chance*(fourth ed.). Cambridge: Deighton, Bell and Co.
5. ↑ J. Bertrand, Solution d'un problème, Comptes Rendus de l'Académie des Sciences de Paris 105 (1887), 369.
6. ↑ D. André, Solution directe du problème résolu par M. Bertrand, Comptes Rendus de l’Académie des Sciences, Paris 105 (1887) 436–437.
7. ↑ Renault, Marc (2008). ["Lost (and found) in translation: André's actual method and its application to the generalized ballot problem"][39]. *Amer. Math. Monthly*. **115**(4): 358– 363. [doi][36]: [10.1080/00029890.2008.11920537][40]. [JSTOR][41] [27642480][39].
8. ↑ Dvoretzky, Aryeh; Motzkin, Theodore (1947), "A problem of arrangements", *Duke Mathematical Journal*, **14**(2): 305– 313, [doi][36]: [10.1215/s0012-7094-47-01423-3][42]

## References

[[edit][43]]

- [Ballot theorems, old and new][44], L. Addario-Berry, [B.A. Reed][45], 2007, in [Horizons of combinatorics][46], Editors Ervin Győri, G. Katona, Gyula O. H. Katona, [László Lovász][47], Springer, 2008, [ISBN][48] [978-3-540-77199-9][49]

## External links

[[edit][50]]

- [The Ballot Problem][51] (includes scans of the original French articles and English translations)
- Bernard Bru, [Les leçons de calcul des probabilités de Joseph Bertrand][52], history of the problem (in French)
- [Weisstein, Eric W.][53] ["Ballot Problem"][54]. *[MathWorld][55]*.

- [v][56]
- [t][57]
- [e][58]

[Probability][4] problems

 |

[Paradoxes][59] |

- [Bertrand's box paradox][60]
- [Boy or girl paradox][61]
- [Siegel's paradox][62]
- [Sleeping Beauty problem][63]
- [St. Petersburg paradox][64]
- [Two envelopes problem][65]

 |

Classical puzzles |

- [Balls into bins problem][66]
- [Banach's matchbox problem][67]
- [Birthday problem][68]
- [Monty Hall problem][69]
- [Three prisoners problem][70]
- [Urn problem][71]
- [Waldegrave problem][72]

 |

Sampling and estimation |

- [Coupon collector's problem][73]
- [German tank problem][74]
- [Newton–Pepys problem][75]

 |

Moment problems |

- [Hamburger moment problem][76]
- [Hausdorff moment problem][77]
- [Moment problem][78]
- [Stieltjes moment problem][79]
- [Trigonometric moment problem][80]

 |

Games and decision |

- [Bertrand's ballot theorem][81]
- [Gambler's ruin][82]
- [Littlewood–Offord problem][83]
- [Mabinogion sheep problem][84]
- [Pill puzzle][85]
- [Problem of points][86]
- [Secretary problem][87]
- [Sunrise problem][88]

 |

[Geometric probability][89] |

- [Bertrand's paradox][90]
- [Broken stick problem][91]
- [Buffon's needle problem][92]
- [Buffon's noodle][93]
- [Mean line segment length][94]
- [Sylvester's four point problem][95]
- [Wendel's theorem][96]

 |

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Bertrand%27s_ballot_theorem&oldid=1361316938][97] "

[Categories][98]:

- [Probability problems][99]
- [Enumerative combinatorics][100]
- [Theorems in combinatorics][101]
- [Theorems in probability theory][102]
- [Voting theory][103]

Hidden categories:

- [Articles with short description][104]
- [Short description is different from Wikidata][105]
- [Articles containing proofs][106]

Search

Bertrand's ballot theorem

9 languages Add topic


## Links

[1]: /w/index.php?title=Ballot_problem&amp;redirect=no
[2]: https://en.wikipedia.org/wiki/Combinatorics
[3]: https://en.wikipedia.org/wiki/Election
[4]: https://en.wikipedia.org/wiki/Probability
[5]: https://en.wikipedia.org/wiki/William_Allen_Whitworth
[6]: https://en.wikipedia.org/wiki/Joseph_Louis_François_Bertrand
[7]: https://en.wikipedia.org/wiki/Recursion_relation
[8]: https://en.wikipedia.org/wiki/Désiré_André
[9]: https://en.wikipedia.org/wiki/Bijection
[10]: https://en.wikipedia.org/wiki/Circular_shift
[11]: /w/index.php?title=Bertrand%27s_ballot_theorem&amp;action=edit&amp;section=1
[12]: /w/index.php?title=Bertrand%27s_ballot_theorem&amp;action=edit&amp;section=2
[13]: /w/index.php?title=Bertrand%27s_ballot_theorem&amp;action=edit&amp;section=3
[14]: https://en.wikipedia.org/wiki/Binomial_coefficient
[15]: /w/index.php?title=Bertrand%27s_ballot_theorem&amp;action=edit&amp;section=4
[16]: https://en.wikipedia.org/wiki/Random_walk
[17]: https://en.wikipedia.org/wiki/Integer
[18]: https://en.wikipedia.org/wiki/Catalan_number
[19]: https://en.wikipedia.org/wiki/Stirling's_approximation
[20]: /w/index.php?title=Bertrand%27s_ballot_theorem&amp;action=edit&amp;section=5
[21]: /w/index.php?title=Bertrand%27s_ballot_theorem&amp;action=edit&amp;section=6
[22]: https://en.wikipedia.org/wiki/Mathematical_induction
[23]: /w/index.php?title=Bertrand%27s_ballot_theorem&amp;action=edit&amp;section=7
[24]: https://en.wikipedia.org/wiki/Cyclic_permutation
[25]: /w/index.php?title=Bertrand%27s_ballot_theorem&amp;action=edit&amp;section=8
[26]: https://en.wikipedia.org/wiki/Stochastic_process
[27]: https://en.wikipedia.org/wiki/Martingale_(probability_theory)
[28]: https://en.wikipedia.org/wiki/Stopping_time
[29]: https://en.wikipedia.org/wiki/Optional_stopping_theorem
[30]: /w/index.php?title=Bertrand%27s_ballot_theorem&amp;action=edit&amp;section=9
[31]: /w/index.php?title=Bertrand%27s_ballot_theorem&amp;action=edit&amp;section=10
[32]: https://en.wikipedia.org/wiki/Lattice_path#North-East_lattice_paths
[33]: https://en.wikipedia.org/wiki/File:AndreReflection.svg
[34]: /w/index.php?title=Bertrand%27s_ballot_theorem&amp;action=edit&amp;section=11
[35]: https://doi.org/10.1214%2Faoms%2F1177700286
[36]: https://en.wikipedia.org/wiki/Doi_(identifier)
[37]: https://en.wikipedia.org/wiki/William_Feller
[38]: http://resolver.sub.uni-goettingen.de/purl?PPN599484047_0008
[39]: https://www.jstor.org/stable/27642480
[40]: https://doi.org/10.1080%2F00029890.2008.11920537
[41]: https://en.wikipedia.org/wiki/JSTOR_(identifier)
[42]: https://doi.org/10.1215%2Fs0012-7094-47-01423-3
[43]: /w/index.php?title=Bertrand%27s_ballot_theorem&amp;action=edit&amp;section=12
[44]: http://www.dms.umontreal.ca/~addario/papers/btsurvey.pdf
[45]: https://en.wikipedia.org/wiki/Bruce_Reed_(mathematician)
[46]: https://books.google.com/books?id=kIKW18ENfUMC
[47]: https://en.wikipedia.org/wiki/László_Lovász
[48]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[49]: https://en.wikipedia.org/wiki/Special:BookSources/978-3-540-77199-9
[50]: /w/index.php?title=Bertrand%27s_ballot_theorem&amp;action=edit&amp;section=13
[51]: http://webspace.ship.edu/msrenault/ballotproblem/
[52]: http://www.jehps.net/Decembre2006/Bru.pdf
[53]: https://en.wikipedia.org/wiki/Eric_W._Weisstein
[54]: https://mathworld.wolfram.com/BallotProblem.html
[55]: https://en.wikipedia.org/wiki/MathWorld
[56]: https://en.wikipedia.org/wiki/Template:Probability_problems
[57]: https://en.wikipedia.org/wiki/Template_talk:Probability_problems
[58]: https://en.wikipedia.org/wiki/Special:EditPage/Template:Probability_problems
[59]: https://en.wikipedia.org/wiki/Category:Probability_theory_paradoxes
[60]: https://en.wikipedia.org/wiki/Bertrand's_box_paradox
[61]: https://en.wikipedia.org/wiki/Boy_or_girl_paradox
[62]: https://en.wikipedia.org/wiki/Siegel's_paradox
[63]: https://en.wikipedia.org/wiki/Sleeping_Beauty_problem
[64]: https://en.wikipedia.org/wiki/St._Petersburg_paradox
[65]: https://en.wikipedia.org/wiki/Two_envelopes_problem
[66]: https://en.wikipedia.org/wiki/Balls_into_bins_problem
[67]: https://en.wikipedia.org/wiki/Banach's_matchbox_problem
[68]: https://en.wikipedia.org/wiki/Birthday_problem
[69]: https://en.wikipedia.org/wiki/Monty_Hall_problem
[70]: https://en.wikipedia.org/wiki/Three_prisoners_problem
[71]: https://en.wikipedia.org/wiki/Urn_problem
[72]: https://en.wikipedia.org/wiki/Waldegrave_problem
[73]: https://en.wikipedia.org/wiki/Coupon_collector's_problem
[74]: https://en.wikipedia.org/wiki/German_tank_problem
[75]: https://en.wikipedia.org/wiki/Newton–Pepys_problem
[76]: https://en.wikipedia.org/wiki/Hamburger_moment_problem
[77]: https://en.wikipedia.org/wiki/Hausdorff_moment_problem
[78]: https://en.wikipedia.org/wiki/Moment_problem
[79]: https://en.wikipedia.org/wiki/Stieltjes_moment_problem
[80]: https://en.wikipedia.org/wiki/Trigonometric_moment_problem
[81]: https://en.wikipedia.org/wiki/Bertrand's_ballot_theorem
[82]: https://en.wikipedia.org/wiki/Gambler's_ruin
[83]: https://en.wikipedia.org/wiki/Littlewood–Offord_problem
[84]: https://en.wikipedia.org/wiki/Mabinogion_sheep_problem
[85]: https://en.wikipedia.org/wiki/Pill_puzzle
[86]: https://en.wikipedia.org/wiki/Problem_of_points
[87]: https://en.wikipedia.org/wiki/Secretary_problem
[88]: https://en.wikipedia.org/wiki/Sunrise_problem
[89]: https://en.wikipedia.org/wiki/Geometric_probability
[90]: https://en.wikipedia.org/wiki/Bertrand_paradox_(probability)
[91]: https://en.wikipedia.org/wiki/Broken_stick_problem
[92]: https://en.wikipedia.org/wiki/Buffon's_needle_problem
[93]: https://en.wikipedia.org/wiki/Buffon's_noodle
[94]: https://en.wikipedia.org/wiki/Mean_line_segment_length
[95]: https://en.wikipedia.org/wiki/Sylvester's_four_point_problem
[96]: https://en.wikipedia.org/wiki/Wendel's_theorem
[97]: https://en.wikipedia.org/w/index.php?title=Bertrand%27s_ballot_theorem&amp;oldid=1361316938
[98]: /wiki/Help:Category
[99]: /wiki/Category:Probability_problems
[100]: /wiki/Category:Enumerative_combinatorics
[101]: /wiki/Category:Theorems_in_combinatorics
[102]: /wiki/Category:Theorems_in_probability_theory
[103]: /wiki/Category:Voting_theory
[104]: /wiki/Category:Articles_with_short_description
[105]: /wiki/Category:Short_description_is_different_from_Wikidata
[106]: /wiki/Category:Articles_containing_proofs
