<!-- source: https://arxiv.org/html/1501.04067v1 | converted from HTML -->

Partition and sum is fast

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1501.04067v1 [math.HO] 14 Jan 2015

# Partition and sum is fast

Steve Butler Thanks: Department of Mathematics, Iowa State University, Ames, IA 50011, USA (butler@iastate.edu). Ron Graham Thanks: Department of Computer Science and Engineering, UC San Diego, La Jolla, CA 92093, USA (graham@ucsd.edu). Richard Stong Thanks: Center for Communications Research, La Jolla, CA 92121, USA (stong@ccrwest.org)

###### Abstract

We consider the following “partition and sum” operation on a natural number: Treating the number as a long string of digits insert several plus signs in between some of the digits and carry out the indicated sum. This results in a smaller number and repeated application can always reduce the number to a single digit. We show that surprisingly few iterations of this operation are needed to get down to a single digit.

## 1 Introduction

Consider the following operation, we call *partition and sum*, that can be performed on a natural number:

*Treating the number as a long string of digits insert plus signs, “ + {+} ”, in between some of the digits (as many or as few as desired) and then carry out the indicated sum to produce a new number.*

This operation can be done for a number in any base (where we use the same base for the entire process), if there is a possibility of confusion we will indicate which base a number is written in using subscript notation, i.e., 111 ( 2) 111_{(2)} is 7 7 in base 2 2. The operation in base 2 2 was originally suggested by Gregory Galperin (see [1]) who asked for a bound on how many steps it takes to get a number down to 1 1 (as long as one plus sign is inserted the number will decrease and so we always can get to 1 1).

We encourage the reader at this point to put the paper aside, write down some random binary numbers, and try to use the partition and sum operation to get to 1 1 in a few steps.

One approach that seems to work well (and that you might have tried) is to simply insert all possible plus signs, i.e., sum the digits. This takes a number n n and gets it to something on the order of at most log ⁡ n \log n. So then we only need to apply enough iterations so that when we iteratively apply the logarithm to n n, i.e., log ( log ( ⋯ ( log ( n)) ⋯)) \log(\log(\cdots(\log(n))\cdots)) the value is less than 1 1. This is known as log ∗ ⁡ ( n) \log^{*}(n) and grows *amazingly*slowly with n n, i.e., goes to infinity slower than just about any function we would expect to encounter. But it still goes to infinity.

While the simple sum the digits strategy gives a good bound, it is still *far*from the truth!

###### Theorem 1.

In base b = 2 b=2 we can take any natural number to a single digit in at most *two*applications of partition and sum. In base b ≥ 3 b\geq 3 we can take any natural number to a single digit in at most *three*applications of partition and sum.

## 2 Reducing in base 2 2

For the result in base 2 2 it suffices to show that in one application of partition and sum we can get to a power of two (i.e., 100 ​ … ​ 0 ( 2) 100\ldots 0_{(2)}). We do this by changing the way we think about the operation. Namely we start by inserting all possible plus signs between digits and then removing some of them to *merge*digits together forming a larger number and increasing the sum (so now we are doing “merging and sum”). We will make use of the following observation (here “ ∗ {*} ” indicates an unknown digit).

###### Observation.

Merging 1 + ∗ 1{+}{*} to 1 ∗ ( 2) 1{*}_{(2)} increases the sum by 1 1; merging 1 + 0 + ∗ 1{+}0{+}{*} to 10 ∗ ( 2) 10{*}_{(2)} increases the sum by 3 3; merging 1 + 1 + ∗ 1{+}1{+}{*} to 11 ∗ ( 2) 11{*}_{(2)} increases the sum by 4 4.

One important thing we will make use of when we merge *three*terms together is that we get significantly more value for our 1 1 ’s. In particular the total sum from the parts which were merged together in triples is at least 7 / 3 7/3 of the number of individual 1 1 ’s that were used (i.e., 1 + 1 + 1 1{+}1{+}{1} to 111 ( 2) 111_{(2)} changed that portion of the sum from 3 3 to 7 7 and the rest of the possibilities yield even better returns). So by forming many triples we can efficiently increase the sum; this forms the basis of our strategy.

Triple merging strategy: Given a number whose binary expansion has m m total 1 1 ’s where 2 k < m ≤ 2 k + 1 2^{k}<m\leq 2^{k+1}, insert plus signs between each pair of digits in the expansion and perform the following as long as the sum is ≤ 2 k + 1 \leq 2^{k+1}: Find the left-most 1 1 that has not yet been merged and merge it with its two successors.

Finally, use merges of the form 1 ∗ 1{*} with the remaining digits to make up the difference to get the sum to 2 k + 1 2^{k+1}.

We note this strategy will *fail*when m = 5 m=5. In this case if there is a 1 + 0 + ∗ 1{+}0{+}{*} anywhere then by merging the three terms together we get the sum to 8 8 and we are done. This leaves 111110 ( 2) 111110_{(2)} and 11111 ( 2) 11111_{(2)} which can be handled by 11 ( 2) + 11 ( 2) + 10 ( 2) 11_{(2)}{+}11_{(2)}{+}10_{(2)} and 1 ( 2) + 1111 ( 2) 1_{(2)}+1111_{(2)} respectively.

###### Proposition 1.

The triple merging strategy works when m ≠ 5 m\neq 5.

###### Proof.

If 7 3 ​ ( m − 5) + 5 > 2 k + 1 \frac{7}{3}(m-5)+5>2^{k+1} then this strategy must succeed. To see this, suppose that q q is the number of 1 1 ’s that have been merged into triples at some stage in the strategy. Then the total sum is at least 7 3 ​ q + ( m − q) \frac{7}{3}q+(m-q). We will stop just before we get above 2 k + 1 2^{k+1} and the inequality indicates that when we stop we have at least *six*1 1 ’s remaining (for otherwise our sum would be too large). The only reason we would stop though is if we ran out of 1 1 ’s (which we haven’t), or the next merging of triples would put us over 2 k + 1 2^{k+1}. Since merging triples increases the total by at most 4 4 this means that we are now at most 3 3 away. So using the remaining 1 1 ’s we can now form 1 ∗ 1{*} ’s to make up the difference and get the sum to 2 k + 1 2^{k+1}.

Simplifying we can conclude that the strategy works for m > 6 7 ​ 2 k + 20 7 m>\frac{6}{7}2^{k}+\frac{20}{7}. When we combine this with m ≥ 2 k + 1 m\geq 2^{k}+1, we can conclude that this holds for m ≥ 10 m\geq 10. On the other hand for m = 1, 2, 3, 4, 6, 7, 8 m=1,2,3,4,6,7,8 we could never form a triple and so the forming twins portion of the strategy kicks in and this will always succeed.

That leaves us with m = 9 m=9, and to finish this off we consider the possible triples that the strategy gives us before we have to move to forming twins.

Starting triples | Remaining 1 1 ’s | Remaining difference |

11 ∗ 11{*} | ≥ 6 \geq 6 | 3 3 |

11 ∗ 11{*} 10 ∗ 10{*} | ≥ 4 \geq 4 | 0 0 |

10 ∗ 10{*} 11 ∗ 11{*} | ≥ 4 \geq 4 | 0 0 |

10 ∗ 10{*} 10 ∗ 10{*} | ≥ 5 \geq 5 | 1 1 |

In each case the number of 1 1 ’s that remain can readily be used to make up the difference. This finishes the case for m = 9 m=9 and also the proof. ∎

## 3 Reducing in base ≥ 4 \geq 4

We start by showing that if n n is small then there is a simple strategy that works for partition and sum.

###### Lemma 1.

Let b ≥ 4 b\geq 4 be our base. Then any number n < 3 ​ b 2 − b − 1 n<3b^{2}-b-1 can be collapsed to a single digit in at most two steps.

###### Proof.

First we observe that for n = 1, 2, …, 2 ​ b − 2 n=1,2,\ldots,2b-2, we can apply the summing digits strategy to get to a single digit in one step. The first number for which the summing digits strategy fails to reach a single digit in two steps is 1 ​ ( b − 1) ​ ( b − 1) ( b) 1(b-1)(b-1)_{(b)}. However, for this number we can first do 1 ( b) + ( b − 1) ​ ( b − 1) ( b) = 100 ( b) 1_{(b)}+(b-1)(b-1)_{(b)}=100_{(b)} and then sum our digits as before.

The number 2 ​ ( b − 2) ​ ( b − 1) ( b) = 3 ​ b 2 − b − 1 2(b-2)(b-1)_{(b)}=3b^{2}-b-1 is the next time where the summing digits strategy fails, establishing the lemma. ∎

This lemma is tight; the number 2 ​ ( b − 2) ​ ( b − 1) ( b) 2(b-2)(b-1)_{(b)} takes three steps as is easy to check. In fact more is true.

###### Observation.

Let b ≥ 4 b\geq 4 be our base. Then 20 ​ … ​ 0 ​ ( b − 2) ​ ( b − 1) ( b) 20\ldots 0(b-2)(b-1)_{(b)} takes three steps for *any*number of zeroes. In particular, there are infinitely many numbers that take three steps.

To see this we first note that the process is always invariant modulo ( b − 1) (b-1) (this is the same principle which states that a number is divisible by 9 9 if and only if the sum of the digits is divisible by 9 9). So when we have taken this particular number to a single digit then we will end with 1 1. Now if it could be done in two steps we would have to be able to get it to a number of the form 10 ​ … ​ 0 ( b) 10\ldots 0_{(b)}, i.e., a power of b b. In particular the last digit after the first step would have to be zero. However, for a number of this form the last digit in merging would come from b − 1 b-1, ( b − 1) + ( b − 2) (b-1)+(b-2), ( b − 1) + 2 (b-1)+2 or ( b − 1) + ( b − 2) + 2 (b-1)+(b-2)+2 and none of these are 0 0 modulo b b when b ≥ 4 b\geq 4. (For b = 3 b=3 we can get a 0 0 in the last digit and so this number can be handled in two steps.)

Now we see that if the sum of digits is small then we can apply Lemma 1 after doing one step of summing the digits. We next show that if the sum of digits is large then we can take one step to get us to a number whose form can be finished in at most two more steps.

###### Lemma 2.

Let b ≥ 4 b\geq 4 be our base and let n n a number with the sum of its digits m ≥ b 2 m\geq b^{2}. Then in one step, n n can be collapsed to a number of the form c ​ 0 ​ … ​ 0 ​ d ​ e c0\ldots 0de where c ≤ 2 c\leq 2 and d ​ e ( b) ≤ b 2 − 2 ​ b de_{(b)}\leq b^{2}-2b.

###### Proof.

Let n = ( … ​ a 4 ​ a 3 ​ a 2 ​ a 1 ​ a 0) ( b) n=(\ldots a_{4}a_{3}a_{2}a_{1}a_{0})_{(b)} and let

 | A = max ⁡ { a 1 + a 3 + a 5 + ⋯, a 2 + a 4 + a 6 + ⋯ }. A=\max\{a_{1}+a_{3}+a_{5}+\cdots,a_{2}+a_{4}+a_{6}+\cdots\}. |  |

We do not use the last digit for A A and so we have A ≥ ( m − ( b − 1)) / 2 A\geq(m-(b-1))/2. We now consider what happens if we merge in pairs so that the leading digits in the pairs sum to A A (i.e., we pair so that all the digits are even or odd depending on which gave us A A). The sum total of this merging strategy will be

 | ( b − 1) ​ A + m ≥ ( b − 1) ​ ( m − b + 1) 2 + m = m ​ b + m − ( b − 1) 2 2 > m ​ b 2. (b-1)A+m\geq{(b-1)(m-b+1)\over 2}+m={mb+m-(b-1)^{2}\over 2}>{mb\over 2}. |  |

(The last step is by our assumption that m ≥ b 2 m\geq b^{2}.) If we now break these pairs one at a time, say from left to right, then the difference in the total would be at most ( b − 1) 2 (b-1)^{2} at each pair. Therefore we have a sequence of ways to partition which go from m m to ( b − 1) ​ A + m (b-1)A+m where the difference between two consecutive methods is at most ( b − 1) 2 (b-1)^{2}.

Now m m is in an interval of the form [b t, 2 ​ b t) [b^{t},2b^{t}) or [2 ​ b t, b t + 1) [2b^{t},b^{t+1}) for some t ≥ 2 t\geq 2. However we have that ( b − 1) ​ A + m > b ​ m / 2 (b-1)A+m>bm/2 cannot be in the same interval (here we use that b ≥ 4 b\geq 4). Therefore there will be some smallest merging strategy which will exceed the top of the given range containing m m. Let M M be the resulting total using this merging. Then we either have 2 ​ b t ≤ M < 2 ​ b t + ( b − 1) 2 2b^{t}\leq M<2b^{t}+(b-1)^{2} or b t + 1 ≤ M < b t + 1 + ( b − 1) 2 b^{t+1}\leq M<b^{t+1}+(b-1)^{2}, depending on which case we are in, which gives exactly the sort of base b b representation as given in the statement of the lemma. ∎

Now if the sum of digits m < b 2 m<b^{2} then sum the singletons and apply Lemma 1 to the result and we take at most three steps. On the other hand, if the sum of digits m ≥ b 2 m\geq b^{2} then by Lemma 2 in one step we will collapse to a number of the form c ​ 0 ​ … ​ 0 ​ d ​ e c0\ldots 0de with c ≤ 2 c\leq 2 and d ​ b + e ≤ b ⁡ ( b − 2) db+e\leq b(b-2). We have that d + e ≤ ( b − 3) + ( b − 1) = 2 ​ b − 4 d+e\leq(b-3)+(b-1)=2b-4, and so adding all the singletons gives a number of size at most 2 ​ b − 2 2b-2, which can be finished in one more step.

## 4 Reducing in base 3 3

We can adopt the same ideas as we have seen before by first showing when the number is small then at most two steps of partition and sum suffice. Then either the sum of the digits is small and so we first sum the digits and then apply a known two step technique *or*the sum of digits is large meaning we have many digits to work with and so we have a lot of flexibility in merging that allows us in one step to get to a number which can readily be done in at most two steps using the sum of digits strategy.

The details of this are not enlightening and so we omit them here and refer interested readers to [2] for details. But what makes base 3 3 interesting is that while there are numbers that require three steps, there are only eleven of them!

###### Theorem 2 (Butler-Graham-Stong [2]).

In base 3 3 any natural number can be collapsed to a single digit in at most two applications of partition and sum *except*for the following eleven:

 | 1781 = 2102222 ( 3) 41065 = 2002022221 ( 3) 3239 = 11102222 ( 3) 43981 = 2020022221 ( 3) 3887 = 12022222 ( 3) 98657 = 12000022222 ( 3) 11177 = 120022222 ( 3) 131461 = 20200022221 ( 3) 14821 = 202022221 ( 3) 393901 = 202000022221 ( 3) 33047 = 1200022222 ( 3) \begin{array}[]{r@{\,=\,}l@{\qquad\qquad\quad}r@{\,=\,}l}1781&2102222_{(3)}&41065&2002022221_{(3)}\\[3.0pt] 3239&11102222_{(3)}&43981&2020022221_{(3)}\\[3.0pt] 3887&12022222_{(3)}&98657&12000022222_{(3)}\\[3.0pt] 11177&120022222_{(3)}&131461&20200022221_{(3)}\\[3.0pt] 14821&202022221_{(3)}&393901&202000022221_{(3)}\\[3.0pt] 33047&1200022222_{(3)}\end{array} |  |

This was proved using a computer to exhaustively handle the case when the sum of digits is small and using theory to handle the case when the sum of digits is large. Finding a simpler, non-computer proof, for the base 3 3 case would be an interesting problem.

## References

- [1] Elwyn Berlekamp and Joe Buhler, Puzzles Column, *Emissary*, Fall 2011, 9.
- [2] Steve Butler, Ron Graham and Richard Stong, *Collapsing numbers in bases 2 2, 3 3, and beyond*, in the Proceedings of The Gathering for Gardner 10. Available online at [http://www.math.ucsd.edu/~ronspubs/][3].


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: http://www.math.ucsd.edu/~ronspubs/
