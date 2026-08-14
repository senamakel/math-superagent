<!-- source: https://arxiv.org/html/2305.10357 | converted from HTML -->

Archive Labeling Sequences

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2305.10357v2 [math.HO] 16 Feb 2024

# Archive Labeling Sequences

Tanya Khovanova Gregory Marton

###### Abstract

What follows is the story of a family of integer sequences, which started life as a Google interview puzzle back in the previous century when VHS video tapes were in use.

## 1 Google’s Puzzle

Suppose you are buying VHS tapes and want to label them using the stickers that came in the package. You want to number the tapes consecutively starting from 1, and the stickers that come with each package are exactly one of each digit [0, … \dots, 9]. For your first tape, you use only the digit 1 and save all the other digit stickers for later tapes. The next time you will need a digit 1 will be for tape number 10. By this time, you will have several unused 1 stickers. What is the next tape number such that after labeling the tape with that number, you will not have any 1 stickers remaining?

## 2 Ones Counting Function

The puzzle appeared in Google Labs Aptitude Test [3] in the following formulation.

Consider a function f f which, for a given whole number x x, returns the number of ones required when writing out all numbers between 0 and x x inclusive. For example, f ⁡ ( 13) = 6 f(13)=6. Notice that f ⁡ ( 1) = 1 f(1)=1. What is the next largest x x such that f ⁡ ( x) = x f(x)=x?

One might notice that it is unclear that the two questions above are equivalent since the happy owner of the tapes might hypothetically run out of another sticker, say sticker 2 first, thus not reaching a point where all stickers 1 are used. Intuitively, we can expect that sticker 1 is the first to run out, and we will prove this shortly.

It is also unclear if any x x even exists such that f ⁡ ( x) = x f(x)=x. In teaching, we often ask students to find things that do not exist, expecting a proof of non-existence. While such problems may be considered evil, they are legitimate. At the time, Google’s unofficial motto was “Don’t be Evil”, and they weren’t: we will see that the answer does indeed exist.

But we digress. Our function f ⁡ ( x) f(x) is the number of 1 stickers needed to label all the tapes up to tape x x. When f ⁡ ( x) = x f(x)=x, then we have used all of the 1 stickers in labeling the first x x tapes. The function f ⁡ ( x) f(x) can be found in the Online Encyclopedia of Integer Sequences [5] as sequence [A094798][3].

In considering the other non-zero digits, let f d ​ ( x) f_{d}(x) count the number of d stickers needed to number the first x x tapes (and of course let f ⁡ ( x) f(x) henceforth be f 1 ​ ( x) f_{1}(x)). In the single and double-digit numbers, there are ten of each non-zero digit in the ones column and ten in the tens column, so 20 altogether. Early on, the tape number is ahead of the digit count. By the time we get to 20-digit numbers, though, there should be, on average, two of any single non-zero digit per number. 1 1 1 We’re looking at non-zero digits for now only because one would not use stickers for leading zeroes, unlike other leading digits, but we will return to zeroes shortly. Thus, the number of times that any digit is used should eventually catch up with the tape numbers.

Encouraged by assurance of reaching our goal somewhere, we might continue our estimate. In the up-to three-digit numbers, those less than 10 4 10^{4}, there are 300 of each non-zero digit; in the numbers below 10 5 10^{5}, there are 4000; then 50 000 below 10 6 10^{6}, and so on up to 10 10 10^{10}, where f d > 1 ​ ( x) f_{d>1}(x) and x x must (almost) meet. In particular, there are 10 000 000 000 counts for any non-zero digit in the numbers below 10 000 000 000. Hence, were the puzzle asking about any of the digits 2–9, then ten billion could have been an easy answer or, at least a limit on how far we need to search.

Sadly, there is a 1 in the decimal representation of ten billion (and a few zeroes), so we require 10 10 + 1 10^{10}+1 digits 1 to write the numbers [1, [1, …, 10 10],10^{10}]. Thus, f 1 ​ ( 10 10) ≠ 10 10 f_{1}(10^{10})\neq 10^{10}, so 10 10 10^{10} cannot be the answer to the original puzzle. Thus stymied, we wrote a program to find the solution to the original Google puzzle. And the answer turned out to be 199981, much smaller than we expected.

## 3 Counting Other Digits

We were so enjoying our stymie 2 2 2 Yes, we just nouned that verb. that we then wrote a program to solve the puzzle for any non-zero digit.

###### Definition 3.1.

We denote by a = ​ ( d) a_{=}(d) the smallest number x > 1 x>1 such that the decimal representation of d appears as a substring of the decimal representations of the numbers [1, [1, …, x],x] exactly x x times:

 | a = ​ ( d) = min ⁡ ( { x > 1: f d ​ ( x) = x }). a_{\bm{=}}(d)=\min(\{x>1:f_{d}(x)\bm{=}x\}). |  |

We already know that a = ​ ( 1) a_{=}(1) is 199 981. The sequence a = ​ ( d) a_{=}(d), which now has number [A163500][4], continues as follows:

 | 28 ​ 263 ​ 827, 371 ​ 599 ​ 983, 499 ​ 999 ​ 984, 10 ​ 000 ​ 000 ​ 000, 9 ​ 500 ​ 000 ​ 000, 9 ​ 465 ​ 000 ​ 000, 9 ​ 465 ​ 000 ​ 000, 10 ​ 000 ​ 000 ​ 000. \numprint{28263827},\ \numprint{371599983},\ \numprint{499999984},\ \numprint{10000000000},\\ \numprint{9500000000},\ \numprint{9465000000},\ \numprint{9465000000},\ \numprint{10000000000}. |  |

Did you expect this sequence to be increasing? You could have because smaller numbers tend to contain smaller digits than larger numbers. Then why is the sequence not increasing? As we failed to find a value for the digit 5 below ten billion, we noticed that it is fairly easy to imagine a scenario where you have one less than the number you need, and then the next value has more than you need for equality, and then you equalize again later. In response, we decided to look at a related sequence.

###### Definition 3.2.

Let

 | a > ​ ( d) = min ⁡ ( { x: f d ​ ( x) > x }). a_{\bm{>}}(d)=\min(\{x:f_{d}(x)\bm{>}x\}). |  |

The key difference is in using “more than” rather than “exactly”. Thus, we will also call our a = ​ ( d) a_{=}(d) sequence the “exactly” sequence and our a > ​ ( d) a_{>}(d) the “more than” sequence.

We later discovered that this related sequence was published at IBM’s famous puzzle website [“Ponder This” in April 2004][5] and was authored by Michael Brand [6]. This version is quite natural as it wonders when we first run out of the labels. Moreover, the 1 sticker plays a special role in this puzzle as it must be the digit that will run out first, as we see in the following table and shall prove theoretically in Proposition 8.1.

Starting at 1, Table 1 shows the first nine terms of the “exactly” and “more than” sequences.

d d | a = ​ ( d) a_{=}(d) | a > ​ ( d) a_{>}(d) |

1 | 199 981 | 199 991 |

2 | 28 263 827 | 28 263 828 |

3 | 371 599 983 | 371 599 993 |

4 | 499 999 984 | 499 999 994 |

5 | 10 000 000 000 | 5 555 555 555 |

6 | 9 500 000 000 | 6 666 666 666 |

7 | 9 465 000 000 | 7 777 777 777 |

8 | 9 465 000 000 | 8 888 888 888 |

9 | 10 000 000 000 | 9 999 999 999 |

Table 1: The first nine terms of a = ​ ( d) a_{=}(d) and a > ​ ( d) a_{>}(d).

Some of these rows are interesting in their own right. Notice that 199 991 is ten more than the previously found 199 981. For all the numbers in between, the initial equality holds ( ∀ i ∈ [199981, \forall i\in[199981, …, 199991],199991] we have i = f 1 ​ ( i) i=f_{1}(i)). Likewise, for d = 3 d=\boxed{3}, each of the numbers between 371 599 983 and 371 599 993 has exactly one three, so the increase in a number by one is the same as the increase in the count of threes. A similar situation holds for d = 4 d=\boxed{4}.

The sequence a > a_{>} can be found using the identifier [A164321][6] in the OEIS. Unsurprisingly, the values matching this relaxed second condition are more well-behaved than those with equality.

Did you notice that the second column is increasing? This might be surprising for the fans of the Champernowne constant. What’s the Champernowne constant? Imagine you placed an infinitude of labeled VHS tapes in order. The labels together will read as a concatenation of all positive integers, whose digits form the sequence A033307. Now we add a zero with a dot in front to get the constant:

 | 0.12345678910111213141516 ​ …. 0.12345678910111213141516\ldots. |  |

The constant is most famous for being a “normal” number in any base [1]. Here normal is a mathematical term referring to the distribution of digits. Normal means that all possible strings of digits of the same length have the same density. This means that every digit in base 10 appears with the same density. Despite this, our second column is increasing, demonstrating an unsurprising fact that smaller digits appear earlier than the bigger digits.

## 4 More “Exactly” Sequences

We want to introduce a few more related sequences, one per digit, where the letter E symbolizes exactness or equality.

###### Definition 4.1.

Let E d E_{d} be an increasing sequence of positive integers x x such that f d ​ ( x) = x f_{d}(x)=x.

The sequence E d E_{d} must be finite. After all, starting from 11-digit numbers, the supply of labels starts decreasing. We have to run out of labels. We can be more precise in claiming that the largest value in E d E_{d} is not more than d ​ 10 10 d10^{10}, which we prove in a more general setting in Proposition 9.1.

Sequences E d E_{d} are connected to our sequence a = ​ ( d) a_{=}(d):

 | a = ​ ( d) = { E d ​ ( 2) for ​ d = 1 E d ​ ( 1) otherwise. a_{=}(d)=\begin{cases}E_{d}(2)&\text{for }d=\boxed{1}\\ E_{d}(1)&\text{otherwise}\end{cases}. |  |

Recall, the special case for 1 is what made the puzzle interesting because E 1 ​ ( 1) = 1 E_{1}(1)=1. The sequences E d E_{d} are in the OEIS database, and we show their A-numbers and lengths in Table 2.

d d | OEIS ref. for E d E_{d} | Number of terms |

1 | [A014778][7] | 83 |

2 | [A101639][8] | 13 |

3 | [A101640][9] | 35 |

4 | [A101641][10] | 47 |

5 | [A130427][11] | 4 |

6 | [A130428][12] | 71 |

7 | [A130429][13] | 48 |

8 | [A130430][14] | 343 |

9 | [A130431][15] | 8 |

Table 2: The sequence numbers for E d E_{d} and their lengths.

The numbers of terms are their own sequence! It appears in the OEIS in disguise: sequence [A130432][16] is the last column of Table 2 plus 1, because the sequence author assumed that tapes would be numbered starting with 0. While that choice may have tempted the audience of this paper 3 3 3 If you numbered your VHS tapes starting at zero, please send a note, kindred spirit!, it would not have been common practice. However, if we did start at zero, and thus add 1 to the last column, we see a neat pattern: the result is divisible by d d. This hides an even more interesting fact: the actual values of E d E_{d} are periodic modulo 10 10 10^{10}, while being bounded by d ⋅ 10 10 d\cdot 10^{10}; the latter fact is proven in Proposition 9.1.

To explain periodicity, we observe that for 0 ≤ x < ( d − 1) ​ 10 10 0\leq x<(d-1)10^{10}, we have f d ​ ( x + 10 10) = f d ​ ( x) + 10 10 f_{d}(x+10^{10})=f_{d}(x)+10^{10}. It follows that the numbers x x and x + 10 10 x+10^{10}, are either both members of the sequence E ⁡ ( d) E(d) or both non-members. Thus the number of the solutions to the equation f d ​ ( x) = x f_{d}(x)=x in the range [0, [0, …, 10 10 − 1],10^{10}-1] is the same as in the range [r 10 10, [r10^{10}, …, ( r + 1) 10 10] − 1,(r+1)10^{10}]-1, when r < d r<d. Hence, we have d d ranges with the same number of solutions, which explains the divisibility of [A130432][16] ( d) (d) by d d.

When studying Table 1, you might notice that stickers 5 and 9 delay the start of the corresponding exact sequences until the latest possible value of x x of 10 000 000 000. Not surprisingly, in Table 2 the count for the number of terms for values 5 and 9 is much smaller than for other stickers. Due to the argument in the previous paragraph, all solutions of f d ​ ( x) = x f_{d}(x)=x for d d equaling 5 or 9 have to be of the form r ​ 10 10 r10^{10}, where r < d r<d. Thus, the last column of 2 has to be the smallest possible value of exactly d − 1 d-1.

Now that the upper bound is clear, we can find the largest values and treat them as another sequence, shown in Table 3.

d d | max ⁡ ( E ⁡ ( d)) \max(E(d)) |

1 | 1 111 111 110, |

2 | 10 535 000 000, |

3 | 20 500 000 000, |

4 | 30 500 000 000, |

5 | 40 000 000 000, |

6 | 59 628 399 995, |

7 | 69 971 736 170, |

8 | 79 998 399 997, |

9 | 80 000 000 000. |

Table 3: Largest values of x x, where f d ​ ( x) = x f_{d}(x)=x.

Let’s now dive deeper into the d = 0 d=0 case.

## 5 Counting Zeroes

In counting zeroes, let us recall that the puzzle specifies that the first VHS tape is labeled with the 1 sticker, not 0. Expanding on f f, we denote the function that calculates zeroes in numbers 1 through x x inclusive as f 0 ​ ( x) f_{0}(x). It is represented in the OEIS as sequence [A061217][17].

We calculated that the smallest number x x such that x x is less than or equal to the number of 0s in the decimal representations of [1, [1, …, x],x] is 100 ​ 559 ​ 404 ​ 366 \numprint{100559404366}, equivalently this number is a > ​ ( 0) a_{>}(0). But what is the corresponding number for the a = a_{=} sequence? It appears that no such number exists. To prove it, we need to start with a lemma.

###### Lemma 5.1.

For any integer x > 10 10 x>10^{10}, we have f 0 ​ ( x + 10 10) ≥ f 0 ​ ( x) + 10 10 f_{0}(x+10^{10})\geq f_{0}(x)+10^{10}.

###### Proof.

Indeed, numbers between x x and x + 10 10 x+10^{10} go through all possible combinations of the last ten digits. Hence, they contain at least 10 10 10^{10} zeroes. ∎

Now we are ready to prove our theorem.

###### Theorem 5.2.

The value a = ​ ( 0) a_{=}(0) is not well-defined.

###### Proof.

We calculated that f 0 ​ ( 100 ​ 559 ​ 404 ​ 366) = 100 ​ 559 ​ 404 ​ 367 f_{0}(\numprint{100559404366})=\numprint{100559404367}. Its predecessor then must be f 0 ​ ( 100 ​ 559 ​ 404 ​ 365) = 100 ​ 559 ​ 404 ​ 364 f_{0}(\numprint{100559404365})=\numprint{100559404364} with three fewer zeros. We verified that there were no equalities up to this point, and indeed up to a bigger number, but of course we couldn’t continue checking up to infinity.

So we need other arguments. Notice that number 100 ​ 559 ​ 404 ​ 366 \numprint{100559404366} has three zeroes. Hence, for some y y that are not much bigger than 100 ​ 559 ​ 404 ​ 367 \numprint{100559404367}, we will have that f 0 ​ ( y + 1) ≥ f 0 ​ ( y) + 3 f_{0}(y+1)\geq f_{0}(y)+3. For some time, the sequence f 0 f_{0} will be increasing in steps not less than three. We are getting away from the equality at high speed.

Were we dealing with random 12-digit numbers, then such numbers would have on average 11 / 10 11/10 zeroes. Hence, f 0 ​ ( x) f_{0}(x) grows faster than x x at this point. But this consideration is not a proof. To finish the proof of the theorem, we need to find a number y > 10 10 y>10^{10} such that f 0 ​ ( y) > y + 10 10 f_{0}(y)>y+10^{10} and check that there is no solution to f 0 ​ ( x) = x f_{0}(x)=x below y y. By Lemma 5.1, that number y y would guarantee that f 0 ​ ( x) f_{0}(x) will always be ahead of its index after y y.

Let us find such a number. We start with 100 559 404 366. The sequence f 0 ​ ( x) f_{0}(x) will continue to grow not slower than its index x x until the next number that doesn’t contain zeroes. Such a number is 111 111 111 111. We calculated that f 0 ​ ( 111 ​ 111 ​ 111 ​ 111) = 120 ​ 987 ​ 654 ​ 321 f_{0}(\numprint{111111111111})=\numprint{120987654321}. So the number of zeroes is way ahead of the number itself. As the sequence f 0 ​ ( x) f_{0}(x) is non-decreasing, we can’t have y y such that f 0 ​ ( y) = y f_{0}(y)=y until 120 987 654 321. This way, we can speed up the process, and we need a small number of iterations to get to such a number. We performed appropriate calculations, thus concluding the proof of the theorem. ∎

## 6 Greater or Equal

In addition to a = a_{=} and a > a_{>}, we counted the “greater or equal” sequence a ≥ ​ ( d) a_{\geq}(d), where d d again denotes the sticker in question. The great property of this latter sequence is that

 | a ≥ ​ ( d) = min ⁡ ( a = ​ ( d), a > ​ ( d)). a_{\geq}(d)=\min(a_{=}(d),a_{>}(d)). |  |

This sequence appears in the database as sequence [A164935][18]. How can we define such a sequence for multi-digit stickers? The idea is to ignore stickers and consider multi-digit strings; for which we give proper definitions in a later section.

One more caveat: we defined a = ​ ( 1) a_{=}(1) to be the smallest number greater than 1 satisfying the VHS property. This complicated condition was needed so that the sequence would include the solution of Google’s puzzle, 199 981, as the first term. But [A164935][18] ( 1) = 1 (1)=1 as it should be. This sequence is non-decreasing for the same reason the “more than” sequence is non-decreasing. We prove this in Proposition 8.1.

## 7 The Algorithms

So that you may easily check the facts we have described, we would like to share the [algorithms we used][19] [4]. In this section, we describe a more efficient way to find f d ​ ( x) f_{d}(x). We counted the digit d d separately in each decimal place it occurred. Suppose we want to count how many times the digit d d occurred in the k k -th place from the right in the set [1, [1, …, x],x]. It depends on which digit the number x x has in the k k -th place from the right. Suppose this digit is x k x_{k}. Consider the number y = ⌊ x / 10 k ⌋ ​ 10 k y=\lfloor x/10^{k}\rfloor 10^{k}. We chose y y because it is the largest number not exceeding x x with k k zeros at the end. In the range [1, [1, …, y − 1],y-1], if we pad smaller integers with zeros on the left, each digit appears in the k k -th place from the right the same number of times. Therefore, any digit d > 0 d>0 appears in this range y 10 = ⌊ x / 10 k ⌋ ​ 10 k − 1 \frac{y}{10}=\lfloor x/10^{k}\rfloor 10^{k-1} times.

Now, we need to calculate how often d d appears in the place of interest in the range [y, [y, …, x],x]. If x k < d x_{k}<d, then it doesn’t appear at all. If x k > d > 0 x_{k}>d>0 we need to add 10 k − 1 10^{k-1}. If x k = d > 0 x_{k}=d>0, we need to add the total count of our digit in the range, which is ( x mod 10 k − 1) + 1 (x\mod 10^{k-1})+1.

We need to consider the case of d = 0 d=0 separately, as we should not count leading zeros, nor zero itself, as the sequence starts at 1. If x k > d = 0 x_{k}>d=0, the count is ⌊ x / 10 k ⌋ ​ 10 k − 1 \lfloor x/10^{k}\rfloor 10^{k-1}, (the same as the x k < d x_{k}<d case for other digits), but if the k k -th digit is zero, we need to subtract the number of digits in the range [1, [1, …, y − 1],y-1] that have fewer than k k digits and add the number of digits in the range [y, [y, …, x],x] that have 0 in the k k -th place from the right. Thus the adjusment is − 10 k − 1 + ( x mod 10 k − 1) + 1 -10^{k-1}+(x\mod 10^{k-1})+1.

To summarize, we would like to express f d ​ ( x) f_{d}(x) as the sum of the contributions c d ​ ( x k) c_{d}(x_{k}) of the counts of the digit d d in the k k -the place from the right. This contribution depends on the value of x k x_{k}. Let Y Y be shorthand for ⌊ x / 10 k ⌋ ⋅ 10 k − 1 \lfloor x/10^{k}\rfloor\cdot 10^{k-1}, then:

 | c d ​ ( x k) = { Y when ​ d > 0 ​ and ​ x k < d Y + ( x mod 10 k − 1) + 1 when ​ d > 0 ​ and ​ x k = d Y + 10 k − 1 when ​ d > 0 ​ and ​ x k > d Y when ​ d = 0 ​ and ​ x k > d Y − 10 k − 1 + ( x mod 10 k − 1) + 1 when ​ d = 0 ​ and ​ x k = d. c_{d}(x_{k})=\begin{cases}Y&\text{when }d>0\text{ and }x_{k}<d\\ Y+(x\mod 10^{k-1})+1&\text{when }d>0\text{ and }x_{k}=d\\ Y+10^{k-1}&\text{when }d>0\text{ and }x_{k}>d\\ Y&\text{when }d=0\text{ and }x_{k}>d\\ Y-10^{k-1}+(x\mod 10^{k-1})+1&\text{when }d=0\text{ and }x_{k}=d\end{cases}. |  |

Summing over each k k -th place, we get

 | f d ​ ( x) = ∑ k c d ​ ( x k). f_{d}(x)=\sum_{k}{c_{d}(x_{k})}. |  | (1) |

We can now use this closed-form for f d ​ ( x) f_{d}(x) in much faster searches for a ≥ ​ ( d) a_{\geq}(d). To do so, we need the following lemma that allows us to skip a lot of numbers in our search.

###### Lemma 7.1.

Suppose we already know that a ≥ ​ ( d) > x a_{\geq}(d)>x. Suppose, in addition, we can show that f d ​ ( y) < x f_{d}(y)<x for some y > x y>x. Then a ≥ ​ ( d) > y a_{\geq}(d)>y.

###### Proof.

As f d f_{d} is non-decreasing and f d ​ ( y) < x f_{d}(y)<x, we know that the value of function f d f_{d} on any element in the range [x, [x, …, y],y] is not greater than x x. It follows that a ≥ ​ ( d) > y a_{\geq}(d)>y. ∎

We search the infinite space of possible values using a variation of unbounded binary search [2]. We call a range of numbers [x, [x, …, x + p],x+p] “safeleft” if we can guarantee that a ≥ ​ ( d) > x a_{\geq}(d)>x. We start with a safeleft range [2, … \dots, 3]. When d = 1 d=1, we can’t start with the range whose left side is 0, as we will get the answer 1, which we want to skip. It is easy to see that the base case holds for 2 in other words, f d ​ ( 2) < 2 f_{d}(2)<2 for any d d, as we only use one 1 and one 2 sticker up to tape number 2. Then we iterate to the next safeleft range as follows:

- •

If f d ​ ( x + p) < x f_{d}(x+p)<x, then a ≥ ​ ( d) a_{\geq}(d) is not in the range by Lemma 7.1, making any range starting with x + p x+p safeleft. The next range to search is [x + p, [x+p, …, x + 3 p],x+3p], where we move the start of the range to x + p x+p and increase the size of the range twice.

- •

If f d ​ ( x + p) ≥ x f_{d}(x+p)\geq x, then a ≥ ​ ( d) a_{\geq}(d) is not guaranteed to be outside of the range. The next range to search is [x, [x, …, x + p / 2],x+p/2], where we keep the start of the range and halve the size of the range.

- •

Suppose we reduced the range size to 1. Then if f d ​ ( x) < x f_{d}(x)<x and f d ​ ( x + 1) ≥ x + 1 f_{d}(x+1)\geq x+1, we have a ≥ ​ ( d) = x + 1 a_{\geq}(d)=x+1. If not, then any range starting with x + 1 x+1 is safe, and the new range is [x + 1, [x+1, …, x + 3],x+3].

After the value of a ≥ ​ ( d) a_{\geq}(d) is found, finding the value of a > ​ ( d) a_{>}(d) is easy for non-zero digits. One may need to check several next values. For zero it is not as easy, but see Section 5. When looking for the exact sequence a = ​ ( d) a_{=}(d), the answer is not always near a ≥ ​ ( d) a_{\geq}(d), but we can still search rapidly. If we already showed that a = ​ ( d) > x a_{=}(d)>x and if f d ​ ( x) > x f_{d}(x)>x, then a = ​ ( d) ≥ f d ​ ( x) a_{=}(d)\geq f_{d}(x). After all, if we saw no digits d d in the range [x, [x, …, f d ( x) − 1],f_{d}(x)-1] at all, x x would not catch up to f d ​ ( x) f_{d}(x) below f d ​ ( x) f_{d}(x).

## 8 Multiple Digits

There is no reason that we should be constrained to single digits. The formal statement of the problem provides a generalization, where we consider substrings of each of the numbers [1, [1, …, x],x] rather than digits in those numbers. We should note that we count every occurrence of a substring separately. Thus 11 will be counted twice as a substring of 1113 even though an actual sticker with “11” printed on it could be used in either position, but not in both positions simultaneously.

Now that we defined the “more than” sequence a > a_{>} for any positive integer, we can prove the statement we promised before, along with a corresponding statement about the a ≥ a_{\geq} sequence.

###### Proposition 8.1.

The “more than” sequence a > a_{>} and the “greater or equal” sequence a ≥ a_{\geq} are non-decreasing after the first terms a > ​ ( 1) a_{>}(1) and a ≥ ​ ( 1) a_{\geq}(1).

###### Proof.

For two strings i i and j j, if i < j i<j, then for every occurrence of j j in a number x x, we can get a smaller number with an occurrence of i i by replacing j j with i i. It follows that for 0 < i < j 0<i<j, and any x x,

 | f i ​ ( x) ≥ f j ​ ( x). f_{i}(x)\geq f_{j}(x). |  |

It follows that f i ​ ( a > ​ ( j)) ≥ f j ​ ( a > ​ ( j)) = a > ​ ( j) f_{i}(a_{>}(j))\geq f_{j}(a_{>}(j))=a_{>}(j), and f i ​ ( a ≥ ​ ( j)) ≥ f j ​ ( a ≥ ​ ( j)) = a ≥ ​ ( j) f_{i}(a_{\geq}(j))\geq f_{j}(a_{\geq}(j))=a_{\geq}(j) implying that a > ​ ( i) ≤ a > ​ ( j) a_{>}(i)\leq a_{>}(j) and a ≥ ​ ( i) ≤ a ≥ ​ ( j) a_{\geq}(i)\leq a_{\geq}(j). ∎

Inspired, we wrote an even fancier program to find values of the “more or equal” sequence a ≥ a_{\geq} for multi-digit numbers. As before, we start by calculating f d ​ ( x) f_{d}(x), where d d is an n n -digit number. As a warm-up, we have an exercise for the reader to check that for k ≥ n k\geq n

 | f d ​ ( 10 k − 1) = k ​ 10 k − n. f_{d}(10^{k}-1)=k10^{k-n}. |  |

To calculate f d ​ ( x) f_{d}(x), we count d d ’s contribution separately in each decimal place it occurred, parametrized by the placement of its last digit. Suppose we want to count how many times the n n -digit string d d occurred so that its last digit is in the k k -th place from the right in the range [1, [1, …, x],x]. It depends on which n n -digits the number x x has in the corresponding place. Suppose this n n -digit number is x k x_{k}. Consider the number y = ⌊ x / 10 k + 1 ⌋ ​ 10 k + 1 y=\lfloor x/10^{k+1}\rfloor 10^{k+1}. In the range [1, [1, …, y − 1],y-1], if we pad smaller integers with zeros on the left, each n n -digit number appears in the k k -th place from the right the same number of times. Therefore, d d appears in this range y 10 n = ⌊ x / 10 k + n − 1 ⌋ ​ 10 k − 1 \frac{y}{10^{n}}=\lfloor x/10^{k+n-1}\rfloor 10^{k-1} times.

Now, we need to calculate how often d d appears in the place of interest in the range [y, [y, …, x],x]. If x k < d x_{k}<d, then it doesn’t appear at all. If x k > d x_{k}>d we need to add 10 k − 1 10^{k-1}. If x k = d x_{k}=d, we need to add the total count of appearance d d in the given spot in the range [y, [y, …, x],x], which is ( x mod 10 k − 1) + 1 (x\mod 10^{k-1})+1.

To summarize, we would like to express f d ​ ( x) f_{d}(x) as the sum of the contributions c d ​ ( x k) c_{d}(x_{k}) of the counts of the n n -digit sticker d d in the k k -th place from the right. Here we assume that n > 1 n>1, and, consequently, d > 0 d>0, which makes the following formula simpler than the one for a single digit. This contribution depends on the value of x k x_{k}. Let Y Y be shorthand for ⌊ x / 10 k − n + 1 ⌋ ⋅ 10 k − 1 \lfloor x/10^{k-n+1}\rfloor\cdot 10^{k-1}, then:

 | c d ​ ( x k) = { Y when ​ x k < d Y + ( x mod 10 k − 1) + 1 when ​ x k = d Y + 10 k − 1 when ​ x k > d. c_{d}(x_{k})=\begin{cases}Y&\textrm{ when }x_{k}<d\\ Y+(x\mod 10^{k-1})+1&\textrm{ when }x_{k}=d\\ Y+10^{k-1}&\textrm{ when }x_{k}>d\end{cases}. |  |

After working out the case d = 0 d=0, we were not immediately sure that a = ​ ( d) a_{=}(d) is defined for every d > 0 d>0. However, it is.

###### Theorem 8.2.

The value a = ​ ( d) a_{=}(d) is well-defined for any d > 0 d>0.

###### Proof.

If d d is an n n -digit sticker that is not a power of 10, then f d ​ ( 10 k − 1) = f d ​ ( 10 k) f_{d}(10^{k}-1)=f_{d}(10^{k}). From the exercise above, it follows that f d ​ ( 10 k) = k ​ 10 k − n f_{d}(10^{k})=k10^{k-n}. Plugging in k = 10 n k=10^{n}, we get f d ​ ( 10 10 n) = 10 n ​ 10 10 n − n = 10 10 n f_{d}(10^{10^{n}})=10^{n}10^{10^{n}-n}=10^{10^{n}}. Thus, 10 10 n 10^{10^{n}} is always a solution for f d ​ ( x) = x f_{d}(x)=x. Therefore, for an n n -digit sticker d d that is not a power of 10, the function a = ​ ( d) a_{=}(d) is well-defined and a = ​ ( d) ≤ 10 10 n a_{=}(d)\leq 10^{10^{n}}.

Now we need to check the case when an n n -digit sticker d d is a power of 10, that is d = 10 n − 1 d=10^{n-1}. Consider x = 2 ⋅ 10 10 n − 6 + n x=2\cdot 10^{10^{n}-6+n}, then Y = 2 ⋅ 10 10 n − 6 Y=2\cdot 10^{10^{n}-6}. We count the contribution of the sticker d d, where the last digit is in the k k -th place from the right, where k k must be in the range [1, [1, …, 10 n − 4],10^{n}-4].

If k < 10 n − 4 k<10^{n}-4, then x k x_{k} is a string of 0s and d > x k d>x_{k}, and the contribution for this k k is Y = 2 ⋅ 10 10 n − 6 Y=2\cdot 10^{10^{n}-6}. If k = 10 n − 4 k=10^{n}-4, then x k x_{k} is a 2 followed by n − 1 n-1 zeros, so d < x k d<x_{k}, and the corresponding Y Y is 0, and the contribution for this k k is 10 k − 1 = 2 ⋅ 10 10 n − 6 + 10 10 n − 5 10^{k-1}=2\cdot 10^{10^{n}-6}+10^{10^{n}-5}. Summing up, we get

 | 2 ⋅ 10 10 n − 6 ​ ( 10 n − 5) + 10 10 n − 5 = 2 ⋅ 10 10 n − 6 + n, 2\cdot 10^{10^{n}-6}(10^{n}-5)+10^{10^{n}-5}=2\cdot 10^{10^{n}-6+n}, |  |

implying that f d ​ ( x) = x f_{d}(x)=x, which concludes the proof. ∎

Below is the smallest number x x for which the number of 10 s as substrings of the numbers in the range [1, [1, …, x],x] is more than or equal to x x. And by a lucky strike, the equality holds. The number has 93 digits and doesn’t fit on a line. Fortunately, the middle part of the number consists of a long run of nines, namely 88 of them. So we replaced some of the nines with dots without losing information. The number is:

 | a ≥ ( 10) = 109 ​ 999 ​ 999 ​ 999 ​ 999 ​ 999 ​ 999 ​ 999 ⋯ 999 ​ 999 ​ 999 ​ 999 ​ 999 ​ 999 ​ 999 ​ 810. a_{\geq}(\boxed{10})=\numprint{109999999999999999999999}\cdots\numprint{999999999999999999999810}. |  |

Now the reader can do an exercise and find the corresponding number for the “more than” sequence, a > ​ ( 10) a_{>}(\boxed{10}).

The value of a ≥ ​ ( 11) a_{\geq}(\boxed{11}) miraculously has 93 digits with a middle run of 88 nines:

 | a ≥ ( 11) = 119 ​ 999 ​ 999 ​ 999 ​ 999 ​ 999 ​ 999 ​ 999 ⋯ 999 ​ 999 ​ 999 ​ 999 ​ 999 ​ 999 ​ 999 ​ 811. a_{\geq}(\boxed{11})=\numprint{119999999999999999999999}\cdots\numprint{999999999999999999999811}. |  |

Note how strikingly similar it is to the tenth element of the sequence! Can you explain that similarity between a ≥ ​ ( 10) a_{\geq}(\boxed{10}) and a ≥ ​ ( 11) a_{\geq}(\boxed{11})?

Sadly, a ≥ ​ ( 12) a_{\geq}(\boxed{12}) is not so pretty, though it still has a middle run of 68 nines allowing us to display it on the line using dots. The total number of digits is 94:

 | a ≥ ( 12) = 1 ​ 296 ​ 624 ​ 070 ​ 230 ​ 872 ​ 986 ​ 615 ​ 199 ​ 999 ​ 999 ⋯ 999 ​ 999 ​ 999 ​ 999 ​ 812. a_{\geq}(\boxed{12})=\numprint{1296624070230872986615199999999}\cdots\numprint{999999999999812}. |  |

It appears that we are lucky again, that the a = a_{=} sequence is the same as the a ≥ a_{\geq} sequence for 11 and 12. Our luck runs out at 21.

We have calculated the values up to d d = 113 so far, but please feel free to contribute more compute!

The values for a = ​ ( 50) a_{=}(50) and a = ​ ( 99) a_{=}(99) are the same nice, round number: 10 101 10^{101}. Similarly, a = ​ ( 999) = 10 1002 a_{=}(999)=10^{1002}. It turns out that and a > ​ ( 99) = a = ​ ( 99) − 1 a_{>}(99)=a_{=}(99)-1 and a > ​ ( 999) = a = ​ ( 999) − 1 a_{>}(999)=a_{=}(999)-1, but there is no such pretty relationship for 50 or 500. There are, however, 6 two-digit values for which the difference is 100. There are also 8 two-digit values that share an a = a_{=} value of 9465 ⋅ 10 97 9465\cdot 10^{97}, reminiscent of the a = a_{=} values for 7 and 8: 9465 ⋅ 10 6 9465\cdot 10^{6}. And would you have guessed, there are corresponding three-digit values whose a = a_{=} values are 9465 ⋅ 10 998 9465\cdot 10^{998}! There are other tantalizing patterns; for details please see the code [4], and share what you find!

One would expect three-digit stickers to occur ten times less frequently than two-digit stickers, and indeed the corresponding values in this sequence that we’ve computed are in the neighborhood of a thousand digits. Each answer for a three-digit sticker has taken about an hour of compute to find, compared to a few seconds for two-digit numbers, so we haven’t checked them all.

Now that we defined our sequence for any sticker d d, we get some natural sequences. The first one is the sequence of stickers d d for which a > ​ ( d) = a ≥ ​ ( d) a_{>}(d)=a_{\geq}(d).:

 | 5, 6, 7, 8, 9, 21, 24, 29, 33, 39, 50, 52, 55, 56, 58, 59, 63, 66, 67, …. 5,\ 6,\ 7,\ 8,\ 9,\ 21,\ 24,\ 29,\ 33,\ 39,\ 50,\ 52,\ 55,\ 56,\ 58,\ 59,\ 63,\ 66,\ 67,\ \dots. |  |

Another lens on this sequence is those d for which a = ​ ( d) a_{=}(d) exists and a = ​ ( d) < a > ​ ( d) a_{=}(d)<a_{>}(d), which is almost the complement, except that 0 still does not appear:

 | 1, 2, 3, 4, 10, 11, …. 1,2,3,4,10,11,\dots. |  |

We can also extend Table 3, with the value for 10 being 5 352 172 560 followed by 90 zeroes, but the value for 11 is again not so pretty: values up to 94 are given in the supplementary materials [4].

Finally, we extend [A130432][16] to the multi-digit case. Starting with the value for the 10 sticker, these are:

 | 3167, 9043, 7485, 1305, 5299, 297, 4659, 1019, 37, 2019, 617, 621, …. 3167,\ 9043,\ 7485,\ 1305,\ 5299,\ 297,\ 4659,\ 1019,\ 37,\ 2019,\ 617,\ 621,\ \ldots. |  |

Sadly, this sequence has lost the divisibility property: [A130432][16] ( d) + 1 (d)+1 is guaranteed to be divisible by d d only for d < 10 d<10.

## 9 All Your Base

Of course the sticker sheets that came with VHS tapes had letters too. Interestingly, some sticker sheets (e.g., Figure 1) had letters A through F, that seemed to beg for hexadecimal numbering, though other sheets included the full alphabet. The algorithms generalize straightforwardly to any base, substituting base b b where we previously wrote 10 10.

[image: Refer to caption] Figure 1: One of the sticker sheets that came with early VHS tapes, with gratitude to an r/nostalgia user [7].

Let us add base b b as the second parameter of our functions. For example, we denote by f d ​ ( x, b) f_{d}(x,b) the number of times the sticker d d is used in the writing of numbers in the range [1, [1, …, x],x] in base b b. Similarly, we add the base to functions a a: a > ​ ( d, b) a_{>}(d,b), a = ​ ( d, b) a_{=}(d,b), and a ≥ ​ ( d, b) a_{\geq}(d,b), where we assume that sticker d d is also written in base b b.

The unary base, where b = 1 b=1, is a special case, as only stickers containing ones are relevant, and the function f d ​ ( x, 1) f_{d}(x,1) can be calculated explicitly. For example, f 1 ​ ( x, 1) = x ⁡ ( x + 1) 2 f_{1}(x,1)=\frac{x(x+1)}{2}. We leave it for the reader to investigate multi-digit cases in this base, and from now on, we will assume that b > 1 b>1.

Two sequences related to different bases are already in the database.

- •

Sequence [A092175][20] ( b) (b) represents our sequence a > ​ ( 1, b) a_{>}(1,b). Starting from base 1, the sequence a > ​ ( 1, b) a_{>}(1,b) progresses as follows:

 | 2, 3, 13, 29, 182, 427, 3931, 8185, 102 ​ 781, 199 ​ 991, 3 ​ 179 ​ 143, …. 2,\ 3,\ 13,\ 29,\ 182,\ 427,\ \numprint{3931},\ \numprint{8185},\ \numprint{102781},\ \numprint{199991},\ \numprint{3179143},\ \ldots. |  |

Comfortingly, [A092175][20] ( 10) = 199 ​ 991 (10)=\numprint{199991}, which we already knew from Table 1.

- •

Sequence [A165617][21] ( b) (b) counts the number of solutions to f 1 ​ ( x, b) = x f_{1}(x,b)=x. Sequence [A165617][21] starts from b = 2 b=2 as

 | 2, 4, 8, 4, 21, 5, 45, 49, 83, 10, 269, 11, 202, 412, 479, 15, …, 2,\ 4,\ 8,\ 4,\ 21,\ 5,\ 45,\ 49,\ 83,\ 10,\ 269,\ 11,\ 202,\ 412,\ 479,\ 15,\ \ldots, |  |

and, not surprisingly, the ninth term is 83, which we already knew from Table 2.

By the way, sequence [A165617][21] is easy to calculate, because the largest possible number such that f 1 ​ ( x, b) = x f_{1}(x,b)=x is known. This number is the concatenation of b − 1 b-1 ones followed by a single zero written in base b b, see the comment in sequence [A165617][21]. Expressed in base 10, these largest numbers are (starting from index 2):

 | 2, 12, 84, 780, 9330, 137 ​ 256, 2 ​ 396 ​ 744, 48 ​ 427 ​ 560, 1 ​ 111 ​ 111 ​ 110, …, 2,\ 12,\ 84,\ 780,\ \numprint{9330},\ \numprint{137256},\ \numprint{2396744},\ \numprint{48427560},\ \numprint{1111111110},\ \ldots, |  |

and they are in the database as sequence [A226238][22].

We promised to show that the solution to f d ​ ( x) = x f_{d}(x)=x for a one-digit nonzero sticker d in base 10 doesn’t exceed d ⋅ 10 10 d\cdot 10^{10}. We waited for this moment to do the proof for any base b b.

###### Proposition 9.1.

For any digit d > 0 d>0 in base b > d b>d the maximum possible value of a = ​ ( d, b) a_{=}(d,b) is b b b^{b} and all x x such that f d ​ ( x, b) = x f_{d}(x,b)=x must be ≤ d ⋅ b b \leq d\cdot b^{b}.

###### Proof.

Similar to base 10, we can calculate that f b ​ ( b b) = b b f_{b}(b^{b})=b^{b}, proving that a = ​ ( d, b) ≤ b b a_{=}(d,b)\leq b^{b}. If x = d ⋅ b b x=d\cdot b^{b}, then f d ​ ( x, b) = x + 1 f_{d}(x,b)=x+1. All numbers in the range [d ⋅ b b, [d\cdot b^{b}, …, ( d + 1) b b],(d+1)b^{b}] have d d for the first digit, implying that there are no solutions to f d ​ ( x, b) = x f_{d}(x,b)=x in this range. Then f d ​ ( ( d + 1) ​ b b) = ( d + 2) ​ b b f_{d}((d+1)b^{b})=(d+2)b^{b}. Converting Lemma 5.1 to base b b, we see that no solution can appear among the next b b b^{b} numbers, while the next b b b^{b} numbers use at least b b b^{b} digits d d. By repeating this ad infinitum, the conclusion follows. ∎

We can generalize Theorem 8.2 to any base b > 2 b>2.

###### Theorem 9.2.

The value a = ​ ( d, b) a_{=}(d,b) is well-defined for any b > 2 b>2 and any d > 0 d>0. For b = 2 b=2, it is well-defined when d > 0 d>0 is not a power of 2.

###### Proof.

By changing 10 to base b b in all the right places, the Theorem 8.2 can be adjusted for any b b and d d, except when b = 2 b=2, and d d is a power of b b. ∎

As you might have noticed, the theorem above excludes cases when b = 2 b=2 and d d is a power of 2. We ran our program for those cases, with findings shown in Table 4, and confirmed that indeed not all seem to exist. We have not proven an upper bound, but checked for 7 up to 1200 decimal digits, far larger than the solutions found for larger powers.

d d | { x: f d ​ ( x, 2) = x } \{x:f_{d}(x,2)=x\} | bits in a = ​ ( d, 2) a_{=}(d,2) |

2 | 10 | 21 | 5 |

4 | 100 | 610 | 10 |

8 | 1000 | 283 187 | 19 |

16 | 10 ​ 000 | 35 609 822 115 | 36 |

32 | 100 ​ 000 | 300 185 978 028 231 432 373 | 69 |

64 | 1 ​ 000 ​ 000 | unique value | 134 |

128 | 10 ​ 000 ​ 000 | not found! |

256 | 100 ​ 000 ​ 000 | unique value | 520 |

512 | 1 ​ 000 ​ 000 ​ 000 | unique value | 1033 |

1024 | 10 ​ 000 ​ 000 ​ 000 | 1023 consecutive values | 2058 |

Table 4: Solutions for f d ​ ( x, 2) = x f_{d}(x,2)=x for stickers d \boxed{d} being the binary stickers corresponding to powers of 2. Larger values are too long to show here.

We now turn our attention to d = 0 d=0. Many of the values a = ​ ( 0, b) a_{=}(0,b) are undefined. To be sure, we need to check to some upper bound, and it need not be tight, but how far do we need to check?

###### Proposition 9.3.

For digit 0 in base b > 1 b>1, the value of a = ​ ( 0, b) a_{=}(0,b), if it is well-defined, must be less than b b + 3 b^{b+3}.

###### Proof.

Similar to base 10, it is enough to find a number y > b b y>b^{b}, such that f 0 ​ ( y, b) > y + b b f_{0}(y,b)>y+b^{b}. We are then guaranteed that there are no solutions to f 0 ​ ( x, b) = x f_{0}(x,b)=x, for x > y x>y.

The number of zeros used in range [b p − 1, [b^{p-1}, …, b p − 1],b^{p}-1] is ( p − 1) ​ ( b − 1) ​ b p − 2 (p-1)(b-1)b^{p-2}. When p = b + 3 p=b+3, then the range contains ( b + 2) ​ ( b − 1) ​ b b + 1 = b b + 3 + ( b − 2) ​ b b + 1 ≥ b b + 3 + b b (b+2)(b-1)b^{b+1}=b^{b+3}+(b-2)b^{b+1}\geq b^{b+3}+b^{b} zeros, whenever b > 2 b>2.

If b = 2 b=2, then b b + 3 = 32 b^{b+3}=32. The number of zeros used in the range [1, [1, …, 32],32] is 54, which is greater than 32 + 4 32+4.

Thus, for b > 1 b>1, and y = b b + 3 y=b^{b+3}, we have f 0 ​ ( y, b) > y + b b f_{0}(y,b)>y+b^{b}, implying that a = ​ ( 0, b) < y a_{=}(0,b)<y. ∎

Those bases in which a = ​ ( 0, b) a_{=}(0,b) does not exist are now [A364972][23]:

 | 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 17, 18, 19, 20, … 3,4,5,6,7,8,9,10,12,14,15,17,18,19,20,\ldots |  |

The first few values of a = ​ ( 0, b) a_{=}(0,b) where it does exist are shown in Table 5.

base b b | a = ​ ( 0, b) a_{=}(0,b) |

2 | 8 |

11 | 3 152 738 985 031 |

13 | 3 950 024 143 546 664 |

16 | 295 764 262 988 176 583 799 |

24 | 32 038 681 563 209 056 709 427 351 442 469 835 |

26 | 160 182 333 966 853 031 081 693 091 544 779 177 187 |

28 | 928 688 890 453 756 699 447 122 559 347 771 300 777 482 |

29 | 74 508 769 042 363 852 559 476 397 161 338 769 391 145 562 |

31 | 529 428 987 529 739 460 369 842 168 744 635 422 842 585 510 266 |

Table 5: Values of the “exactly” sequence for the zero sticker in the first few bases where it exists.

## 10 Future research

We have stretched the notion of a sticker with the multi-digit case, because although our definition has nice mathematical properties it uses stickers that are counted as overlapping, and excludes multi-digit stickers that begin with a zero. These are of course both decisions that one can relax to explore fresh possibilities.

The common inclusion of letter stickers on these VHS sticker sheets invites not only generalization to other bases, but also generalization to, dare we say it, textual labels? But this is still a math paper, so let’s not get carried away: we can restrict ourselves by imagining textual labels that correspond to spelled-out versions of the numbers! Thus, for some English-like convention c c,

a = ​ ( `​ `​ o ​ ", c) a_{=}(``o",c) | = 2 =2 | “One”, “twO”), |

a = ​ ( `​ `​ e ​ ", c) a_{=}(``e",c) | = 3 =3 | (“onE”, “two”, “thrEE”) |

a > ​ ( `​ `​ j ​ ", c) a_{>}(``j",c) | undefined | “J” does not appear. |

Of course there are a jillion variations by language, locale, etc.

Throughout the paper we’ve noted phenomena that seemed interesting but bear further investigation. Examples include the many solutions to a = a_{=} in base 10 that begin with “9465”, what governs whether a = a_{=} is smaller or greater than a > a_{>}, what happens in unary base, whether the sequences are well-defined for all powers of 2 in base 2, and whether all of those have unique solutions. We encourage you to look at the tables in the supplementary materials, as there are many more patterns begging for attention.

One such pattern we see in the data, but have not proven anything about is that the number of digits in a = ​ ( b, b) a_{=}(b,b) equals b 2 + b + 3 b^{2}+b+3, for b > 2 b>2. The solutions, expressed in their respective bases in Table 6, all have a similar form for b > 2 b>2: the first digits are 1, then 0, then digits b − 1 b-1, finishing with b − 2 b-2, 1, 0.

base | length | a = ​ ( b, b) a_{=}(b,b) or equivalently, a = ​ ( 10, b) a_{=}(\boxed{10},b) |

2 | 5 | 10 ​ 101 2 \numprint{10101}_{2}, |

3 | 9 | 102 ​ 222 ​ 110 3 \numprint{102222110}_{3}, |

4 | 15 | 103 ​ 333 ​ 333 ​ 333 ​ 210 4 \numprint{103333333333210}_{4}, |

5 | 23 | 10 ​ 444 ​ 444 ​ 444 ​ 444 ​ 444 ​ 444 ​ 310 5 \numprint{10444444444444444444310}_{5}, |

6 | 33 | 105 ​ 555 ​ 555 ​ 555 ​ 555 ​ 555 ​ 555 ​ 555 ​ 555 ​ 555 ​ 410 6 \numprint{105555555555555555555555555555410}_{6}. |

Table 6: Lengths and values of a = ​ ( 10, b) a_{=}(\boxed{10},b) for the first few bases b b.

And of course the sequences we described in this paper can be extended, and there are many related sequences to be cataloged. We would love to hear tales from your explorations. Enjoy the sequence hunt!

## 11 Acknowledgments

We are grateful to Alexey Radul for his helpful suggestions. We are also thankful to the anonymous reviewers of the American Mathematical Monthly for encouraging us to dig deeper into the topic and providing helpful ideas and suggestions.

## References

- [1] David. H. Bailey and Richard E. Crandall, Random Generators and Normal Numbers. Exper. Math. 11, 527–546, 2002.
- [2] Jon L. Bentley and Andrew C. Yao. An Almost Optimal Algorithm for Unbounded Searching. *Information Processing Letters*, 3(3):144–147, 1976.
- [3] Google Labs Aptitude Test, Google, 2004.
- [4] Gregory Marton and Tanya Khovanova. Archive Labelling Sequences: Code. 2023. [https://colab.research.google.com/drive/1pGfgQWvJR1IAG3t4dNnrTnc07UvyV4xC][19]
- [5] OEIS Foundation Inc. (2023), The On-Line Encyclopedia of Integer Sequences, Published electronically at [https://oeis.org][24]
- [6] Ponder This, (2004), available at [https://research.ibm.com/haifa/ponderthis/challenges/April2004.html][5].
- [7] The stickers that came with blank VHS tapes. Posted by Reddit user u/morbidlyatease in r/nostalgia, used with permission. Posted March 24, 2022. [https://www.reddit.com/r/nostalgia/comments/tm21n4/the_stickers_that_came_with_blank_vhs_tapes/][25]


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: http://oeis.org/A094798
[4]: http://oeis.org/A163500
[5]: https://research.ibm.com/haifa/ponderthis/challenges/April2004.html
[6]: http://oeis.org/A164321
[7]: http://oeis.org/A014778
[8]: http://oeis.org/A101639
[9]: http://oeis.org/A101640
[10]: http://oeis.org/A101641
[11]: http://oeis.org/A130427
[12]: http://oeis.org/A130428
[13]: http://oeis.org/A130429
[14]: http://oeis.org/A130430
[15]: http://oeis.org/A130431
[16]: http://oeis.org/A130432
[17]: http://oeis.org/A061217
[18]: http://oeis.org/A164935
[19]: https://colab.research.google.com/drive/1pGfgQWvJR1IAG3t4dNnrTnc07UvyV4xC
[20]: http://oeis.org/A092175
[21]: http://oeis.org/A165617
[22]: http://oeis.org/A226238
[23]: http://oeis.org/A364972
[24]: https://oeis.org
[25]: https://www.reddit.com/r/nostalgia/comments/tm21n4/the_stickers_that_came_with_blank_vhs_tapes/
