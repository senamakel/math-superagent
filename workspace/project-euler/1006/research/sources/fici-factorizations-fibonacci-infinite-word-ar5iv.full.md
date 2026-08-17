<!-- source: https://ar5iv.labs.arxiv.org/html/1508.06754 | converted from HTML -->

[1508.06754] Factorizations of the Fibonacci Infinite Word

# Factorizations of the Fibonacci Infinite Word Thanks: Published on Journal of Integer Sequences, Vol. 18 (2015), Article 15.9.3.

Gabriele Fici Address: Dipartimento di Matematica e Informatica
Università di Palermo
Palermo
Italy Email address: [Gabriele.Fici@unipa.it][1]

###### Abstract.

The aim of this note is to survey the factorizations of the Fibonacci infinite word that make use of the Fibonacci words and other related words, and to show that all these factorizations can be easily derived in sequence starting from elementary properties of the Fibonacci numbers.

Keywords. Fibonacci word; Zeckendorf representation; Lyndon factorization; Lempel-Ziv factorization; Crochemore factorization.

## 1. Preliminaries

The well-known sequence of Fibonacci numbers (sequence A000045 in the On-Line Encyclopedia of Integer Sequences) is defined by F 1 = 1 F_{1}=1, F 2 = 1 F_{2}=1 and for every n > 2 n>2, F n = F n − 1 + F n − 2 F_{n}=F_{n-1}+F_{n-2}. The first few values of the sequence F n F_{n} are reported in Table 1 for reference.

n n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |

F n F_{n} | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 610 | 987 | 1597 | 2584 | 4181 | 6765 |

Table 1. The first few values of the sequence of Fibonacci numbers.

A basic property of Fibonacci numbers (that can be easily proved by induction) is that 1 1 plus the sum of the first n n Fibonacci numbers is equal to the ( n + 2) (n+2) -th Fibonacci number:

(1) |  | 1 + ∑ i = 1 n F i = F n + 2. 1+\sum_{i=1}^{n}F_{i}=F_{n+2}. |  |

We recall here a famous result, usually attributed to Zeckendorf [13], but published earlier by Lekkerkerker [8] and which, in fact, is a special case of an older and more general result due to Ostrowski [10]. It permits us to use Fibonacci numbers as a basis for representing integers:

###### Theorem 1.

Every positive integer can be expressed uniquely as the sum of one or more distinct non-consecutive Fibonacci numbers F n F_{n}, n > 1 n>1.

For example, 17 = 13 + 3 + 1 = F 7 + F 4 + F 2 17=13+3+1=F_{7}+F_{4}+F_{2}, and there is no other way to write 17 17 as the sum of non-consecutive Fibonacci numbers (assuming the convention that F 1 F_{1} is not used in the representation). Thus, one can represent natural numbers as strings of 0 0 - 1 1 bits, where the i i -th bit (from the right) encodes the presence/absence of the ( i + 1) (i+1) -th Fibonacci number in the representation given by Theorem 1. So for example the number 17 17 is represented by 100101 100101. We call this representation of natural numbers the *Zeckendorf representation*.

The first few natural numbers and their Zeckendorf representations are displayed in Table 2, where we padded to the left with 0 0 s in order to have strings of the same length. Note that with 6 6 bits one can represent the first 21 21 natural numbers. In fact, for every n > 0 n>0, there are exactly F n F_{n} integers whose leftmost 1 1 in the Zeckendorf representation is in position n n (starting from the right). From ( 1) (\ref{eq:Fib}), we derive that one needs n n bits to represent the first F n + 2 F_{n+2} natural numbers.

The strings of length n n forming the Zeckendorf representations of the first F n + 2 F_{n+2} natural numbers are precisely all the 0 0 - 1 1 strings of length n n not containing two consecutive 1 1 s. These strings are in lexicographic order if the natural numbers are in increasing order from 0 0 to F n + 2 − 1 F_{n+2}-1.

Zeck. | decimal  | Zeck. | decimal  | Zeck. | decimal  |

 |  |  |  |  |  |

000000 000000 | 0  | 010000 010000 | 8  | 100100 100100 | 16  |

000001 000001 | 1  | 010001 010001 | 9  | 100101 100101 | 17  |

000010 000010 | 2  | 010010 010010 | 10  | 101000 101000 | 18  |

000100 000100 | 3  | 010100 010100 | 11  | 101001 101001 | 19  |

000101 000101 | 4  | 010101 010101 | 12  | 101010 101010 | 20  |

001000 001000 | 5  | 100000 100000 | 13  |  |  |

001001 001001 | 6  | 100001 100001 | 14  |  |  |

001010 001010 | 7  | 100010 100010 | 15  |  |  |

Table 2. The Zeckendorf representations of the first few natural numbers coded with 6 bits.

Let us define f ⁡ ( n) f(n), for every n ≥ 0 n\geq 0, as the rightmost digit of the Zeckendorf representation of n n. For every n > 1 n>1 we define the *n n -th Fibonacci word*as the string

 | f n = f ( 0) f ( 1) ⋯ f ( F n − 1) f_{n}=f(0)f(1)\cdots f(F_{n}-1) |  |

of length | f n | = F n |f_{n}|=F_{n}. By convention, we set f 1 = 1. f_{1}=1. The first few Fibonacci words are shown in Table 3.

 | f 1 = 1 f 2 = 0 f 3 = 01 f 4 = 010 f 5 = 01001 f 6 = 01001010 f 7 = 0100101001001 f 8 = 010010100100101001010 f 9 = 0100101001001010010100100101001001 \begin{split}f_{1}&=1\\ f_{2}&=0\\ f_{3}&=01\\ f_{4}&=010\\ f_{5}&=01001\\ f_{6}&=01001010\\ f_{7}&=0100101001001\\ f_{8}&=010010100100101001010\\ f_{9}&=0100101001001010010100100101001001\\ \end{split} |  |

Table 3. The first few Fibonacci words.

We also define the *Fibonacci infinite word*f f as the limit of f n f_{n} as n n goes to infinity. That is, f f is the infinite word whose n n -th letter is the “parity” of the Zeckendorf representation of n n:

 | f = f ( 0) f ( 1) f ( 2) f ( 3) ⋯ = 0100101001001010010 ⋯ f=f(0)f(1)f(2)f(3)\cdots=0100101001001010010\cdots |  |

In the Zeckendorf representation of an integer, when the n n -th digit from the right is a 1 1, the ( n − 1) (n-1) -th digit from the right is a 0 0. Hence, the rightmost n − 2 n-2 digits of the Zeckendorf representations of the natural numbers from F n + 1 F_{n+1} to F n + 2 − 1 F_{n+2}-1 are the same rightmost n − 2 n-2 digits of the Zeckendorf representations of the first F n F_{n} natural numbers. For example, the 2 2 rightmost digits of the Zeckendorf representations of 5 5, 6 6 and 7 7 are, respectively, 00 00, 01 01, 10 10, as well as the 2 2 rightmost digits of the Zeckendorf representations of the 0 0, 1 1 and 2 2. We deduce that for every n > 2 n>2, one has

(2) |  | f n = f n − 1 ​ f n − 2. f_{n}=f_{n-1}f_{n-2}. |  |

For more details on Fibonacci words the reader can see, for instance, [1].

Recall that a *factorization*of an infinite word w w is a sequence ( x n) n ≥ 1 (x_{n})_{n\geq 1} of finite words such that w w can be expressed as the concatenation of the elements of the sequence, i.e., w = ∏ n ≥ 1 x n w=\prod_{n\geq 1}x_{n}.

In general, exhibiting a factorization ( x n) n ≥ 1 (x_{n})_{n\geq 1} of an infinite word w w can be useful to better understand the combinatorics of w w, provided the sequence ( x n) n ≥ 1 (x_{n})_{n\geq 1} has non-trivial combinatorial properties—for example, all the words in the sequence are palindromes, squares, or prefixes of w w.

Another point of view consists in defining a factorization by some general rule that can be applied to any infinite word. The sequence ( x n) n ≥ 1 (x_{n})_{n\geq 1} is therefore determined by the particular instance of the infinite word w w (as is the case, for example, in the Lempel-Ziv factorization or in the Lyndon factorization, that we will see below). In this case, the word w w can have particular properties that make it a limit example for that particular factorization.

In next sections, we will show a number of factorizations of the Fibonacci infinite word that make use of the Fibonacci finite words and other related words. These factorizations have been introduced over the time in different papers, and we think it can be useful to collect them all together for reference. We also add some (at least to the best of our knowledge) novel factorizations. Moreover, we present these factorizations in an order that allows us to provide a short and elementary proof for each of them, despite the original proofs being sometimes more involved or more technical.

## 2. Fibonacci words and co-Fibonacci words

The first factorization of the Fibonacci infinite word we exhibit is the following.

###### Proposition 1.

The Fibonacci infinite word can be obtained by concatenating 0 0 and the Fibonacci words:

(3) |  | f \displaystyle f | = \displaystyle= | 0 ​ ∏ n ≥ 1 f n \displaystyle 0\prod_{n\geq 1}f_{n} |  |

 |  | = \displaystyle= | 0 ⋅ 1 ⋅ 0 ⋅ 01 ⋅ 010 ⋅ 01001 ⋅ 01001010 ⋅ ⋯ \displaystyle 0\cdot 1\cdot 0\cdot 01\cdot 010\cdot 01001\cdot 01001010\cdots |  |

###### Proof.

Since for every i ≥ 1 i\geq 1, | f i | = F i |f_{i}|=F_{i}, it is sufficient to prove that, for every n ≥ 1 n\geq 1, f n f_{n} occurs in f f starting at position 1 + ∑ i = 1 n − 1 F i = F n + 1 1+\sum_{i=1}^{n-1}F_{i}=F_{n+1}. From ( 2) (\ref{eq:rec}), we have f n + 2 = f n + 1 ​ f n f_{n+2}=f_{n+1}f_{n}, so that f n f_{n} has an occurrence in f f starting at position | f n + 1 | = F n + 1 |f_{n+1}|=F_{n+1}. ∎

Let us consider the sequence p n p_{n} of the palindromic prefixes of f f, also called *central words*. The first few values of the sequence p n p_{n} are displayed in Table 4, where ε \varepsilon denotes the empty word, i.e., the word of length 0 0.

 | p 3 = ε p 4 = 0 p 5 = 010 p 6 = 010010 p 7 = 01001010010 p 8 = 0100101001001010010 p 9 = 01001010010010100101001001010010 \begin{split}p_{3}&=\varepsilon\\ p_{4}&=0\\ p_{5}&=010\\ p_{6}&=010010\\ p_{7}&=01001010010\\ p_{8}&=0100101001001010010\\ p_{9}&=01001010010010100101001001010010\\ \end{split} |  |

Table 4. The first few central words.

As it is well-known, for every n ≥ 3 n\geq 3, p n p_{n} is obtained from f n f_{n} by removing the last two letters. More precisely, we have for every n ≥ 1 n\geq 1,

(4) |  | f 2 ​ n + 1 = p 2 ​ n + 1 ​ 01, f 2 ​ n + 2 = p 2 ​ n + 2 ​ 10. f_{2n+1}=p_{2n+1}01,\hskip 17.07164ptf_{2n+2}=p_{2n+2}10. |  |

The fundamental property of the central words is the following:

###### Lemma 1.

For every n ≥ 2 n\geq 2 one has

 | p 2 ​ n + 1 = p 2 ​ n − 1 ​ 01 ​ p 2 ​ n = p 2 ​ n ​ 10 ​ p 2 ​ n + 1, p 2 ​ n + 2 = p 2 ​ n ​ 10 ​ p 2 ​ n + 1 = p 2 ​ n + 1 ​ 01 ​ p 2 ​ n. p_{2n+1}=p_{2n-1}01p_{2n}=p_{2n}10p_{2n+1},\hskip 22.76219ptp_{2n+2}=p_{2n}10p_{2n+1}=p_{2n+1}01p_{2n}. |  |

###### Proof.

Follows immediately from ( 2) (\ref{eq:rec}) and ( 4) (\ref{central}). ∎

###### Remark 1.

It is easy to see from ( 2) (\ref{eq:rec}) that for every n ≥ 4 n\geq 4, one has f n = f n − 2 ​ f n − 3 ​ f n − 2 f_{n}=f_{n-2}f_{n-3}f_{n-2}. We have therefore from ( 3) (\ref{fibo}):

(5) |  | f \displaystyle f | = \displaystyle= | 01001 ​ ∏ n ≥ 2 f n ​ f n − 1 ​ f n \displaystyle 01001\prod_{n\geq 2}f_{n}f_{n-1}f_{n} |  |

 |  | = \displaystyle= | 01001 ⋅ ( 0 ⋅ 1 ⋅ 0) ​ ( 01 ⋅ 0 ⋅ 01) ​ ( 010 ⋅ 01 ⋅ 010) ​ ( 01001 ⋅ 010 ⋅ 01001) ​ ⋯ \displaystyle 01001\cdot(0\cdot 1\cdot 0)(01\cdot 0\cdot 01)(010\cdot 01\cdot 010)(01001\cdot 010\cdot 01001)\cdots |  |

Analogously, since 1 = f 3 1=f_{3}, we can write

(6) |  | f \displaystyle f | = \displaystyle= | 0100 ​ ∏ n ≥ 2 f n − 1 ​ f n ​ f n − 1 \displaystyle 0100\prod_{n\geq 2}f_{n-1}f_{n}f_{n-1} |  |

 |  | = \displaystyle= | 0100 ⋅ ( 1 ⋅ 0 ⋅ 1) ​ ( 0 ⋅ 01 ⋅ 0) ​ ( 01 ⋅ 010 ⋅ 01) ​ ( 010 ⋅ 01001 ⋅ 010) ​ ⋯ \displaystyle 0100\cdot(1\cdot 0\cdot 1)(0\cdot 01\cdot 0)(01\cdot 010\cdot 01)(010\cdot 01001\cdot 010)\cdots |  |

We now introduce a class of words that we call the co-Fibonacci words. Although this class has appeared previously in the literature [2], to the best of our knowledge no one has yet given a name to them.

The co-Fibonacci words f n ′ f^{\prime}_{n} are defined by complementing the last two letters in the Fibonacci words f n f_{n}, that is, f n ′ = p n ​ y ​ x f^{\prime}_{n}=p_{n}yx, where x x and y y are the letters such that f n = p n ​ x ​ y f_{n}=p_{n}xy. Equivalently, co-Fibonacci words can be defined by f n ′ = f n − 2 ​ f n − 1 f^{\prime}_{n}=f_{n-2}f_{n-1} for every n ≥ 3 n\geq 3. The first few co-Fibonacci words are displayed in Table 5.

 | f 3 ′ = 10 f 4 ′ = 001 f 5 ′ = 01010 f 6 ′ = 01001001 f 7 ′ = 0100101001010 f 8 ′ = 010010100100101001010 \begin{split}f^{\prime}_{3}&=10\\ f^{\prime}_{4}&=001\\ f^{\prime}_{5}&=01010\\ f^{\prime}_{6}&=01001001\\ f^{\prime}_{7}&=0100101001010\\ f^{\prime}_{8}&=010010100100101001010\\ \end{split} |  |

Table 5. The first few co-Fibonacci words.

The following lemma is a direct consequence of Lemma 1.

###### Lemma 2.

For every n ≥ 2 n\geq 2 one has

 | f 2 ​ n + 1 ′ = f 2 ​ n ​ f 2 ​ n − 1 ′, f 2 ​ n + 2 = f 2 ​ n ​ f 2 ​ n + 1 ′. f^{\prime}_{2n+1}=f_{2n}f^{\prime}_{2n-1},\hskip 22.76219ptf_{2n+2}=f_{2n}f^{\prime}_{2n+1}. |  |

###### Proposition 2.

The Fibonacci word can be obtained by concatenating 0 0 and the odd co-Fibonacci words:

(7) |  | f \displaystyle f | = \displaystyle= | 0 ​ ∏ n ≥ 1 f 2 ​ n + 1 ′ \displaystyle 0\prod_{n\geq 1}f^{\prime}_{2n+1} |  |

 |  | = \displaystyle= | 0 ⋅ 10 ⋅ 01010 ⋅ 0100101001010 ⋅ ⋯ \displaystyle 0\cdot 10\cdot 01010\cdot 0100101001010\cdots |  |

###### Proof.

Follows directly from ( 3) replacing f 2 ​ n − 1 ​ f 2 ​ n f_{2n-1}f_{2n} with f 2 ​ n + 1 ′ f^{\prime}_{2n+1}. ∎

Analogously, we have the following:

###### Proposition 3.

The Fibonacci word can be obtained by concatenating 01 01 and the even co-Fibonacci words:

(8) |  | f \displaystyle f | = \displaystyle= | 01 ​ ∏ n ≥ 1 f 2 ​ n + 2 ′ \displaystyle 01\prod_{n\geq 1}f^{\prime}_{2n+2} |  |

 |  | = \displaystyle= | 01 ⋅ 001 ⋅ 01001001 ⋅ 010010100100101001010 ⋅ ⋯ \displaystyle 01\cdot 001\cdot 01001001\cdot 010010100100101001010\cdots |  |

###### Proof.

Follows directly from ( 3) replacing f 2 ​ n ​ f 2 ​ n + 1 f_{2n}f_{2n+1} with f 2 ​ n + 2 ′ f^{\prime}_{2n+2}. ∎

## 3. Singular words

Let us define the *left rotation*of a non-empty word w = w 1 w 2 ⋯ w n w=w_{1}w_{2}\cdots w_{n}, w i w_{i} letters, as the word w λ = w n w 1 ⋯ w n − 1 w^{\lambda}=w_{n}w_{1}\cdots w_{n-1}. Analogously, the *right rotation*of w w is defined as the word w ρ = w 2 ⋯ w n w 1 w^{\rho}=w_{2}\cdots w_{n}w_{1}.

The *singular words*f ^ n \hat{f}_{n} are defined by complementing the first letter in the left rotations of the Fibonacci words f n f_{n}. The first few singular words are displayed in Table 6. Note that for every n ≥ 1 n\geq 1, one has f ^ 2 ​ n + 1 = 0 ​ p 2 ​ n + 1 ​ 0 \hat{f}_{2n+1}=0p_{2n+1}0 and f ^ 2 ​ n + 2 = 1 ​ p 2 ​ n + 2 ​ 1 \hat{f}_{2n+2}=1p_{2n+2}1.

 | f ^ 1 = 0 f ^ 2 = 1 f ^ 3 = 00 f ^ 4 = 101 f ^ 5 = 00100 f ^ 6 = 10100101 \begin{split}\hat{f}_{1}&=0\\ \hat{f}_{2}&=1\\ \hat{f}_{3}&=00\\ \hat{f}_{4}&=101\\ \hat{f}_{5}&=00100\\ \hat{f}_{6}&=10100101\\ \end{split} |  |

Table 6. The first few singular words.

The singular words are palindromic factors of f f but do not appear as prefixes of f f (by the way, f f also contains other palindromic factors besides the central words p n p_{n} and the singular words f ^ n \hat{f}_{n}, e.g., 1001 1001 or 01010 01010, see [6] for more details). Their name comes from the fact that among the F n + 1 F_{n}+1 factors of f f of length F n F_{n}, there are F n F_{n} of them that can be obtained one from each other by iteratively applying left (or equivalently right) rotation and one, the singular word, whose left (or equivalently right) rotation is not a factor of f f.

Wen and Wen [12] proved that the Fibonacci infinite word can be obtained by concatenating the singular words:

###### Proposition 4.

The Fibonacci infinite word is the concatenation of the singular words:

(9) |  | f \displaystyle f | = \displaystyle= | ∏ n ≥ 1 f ^ n \displaystyle\prod_{n\geq 1}\hat{f}_{n} |  |

 |  | = \displaystyle= | 0 ⋅ 1 ⋅ 00 ⋅ 101 ⋅ 00100 ⋅ 10100101 ⋅ ⋯ \displaystyle 0\cdot 1\cdot 00\cdot 101\cdot 00100\cdot 10100101\cdots |  |

###### Proof.

Indeed, ( 9) follows directly from ( 3) and the definition of singular words, observing that the Fibonacci words end by letter 0 0 and 1 1 alternatingly. ∎

The factorization ( 9) is in fact the Lempel-Ziv factorization of f f. The Lempel-Ziv factorization is a factorization widely used in computer science for compressing strings [14]. The Lempel-Ziv factorization of a word w w is w = w 1 w 2 ⋯ w=w_{1}w_{2}\cdots where w 1 w_{1} is the first letter of w w and for every i ≥ 2 i\geq 2, w i w_{i} is the shortest prefix of w i w i + 1 ⋯ w_{i}w_{i+1}\cdots that occurs only once in the word w 1 w 2 ⋯ w i w_{1}w_{2}\cdots w_{i}. Roughly speaking, at each step one searches for the shortest factor that did not appear before.

###### Remark 2.

It is easy to see, using for example ( 2), ( 4) and the definition of singular words, that for every n ≥ 4 n\geq 4, f ^ n = f ^ n − 2 ​ f ^ n − 3 ​ f ^ n − 2 \hat{f}_{n}=\hat{f}_{n-2}\hat{f}_{n-3}\hat{f}_{n-2}. Therefore, from ( 9), we have

(10) |  | f \displaystyle f | = \displaystyle= | 0100 ​ ∏ n ≥ 2 f ^ n ​ f ^ n − 1 ​ f ^ n \displaystyle 0100\prod_{n\geq 2}\hat{f}_{n}\hat{f}_{n-1}\hat{f}_{n} |  |

 |  | = \displaystyle= | 0100 ⋅ ( 1 ⋅ 0 ⋅ 1) ​ ( 00 ⋅ 1 ⋅ 00) ​ ( 101 ⋅ 00 ⋅ 101) ​ ( 00100 ⋅ 101 ⋅ 00100) ​ ⋯ \displaystyle 0100\cdot(1\cdot 0\cdot 1)(00\cdot 1\cdot 00)(101\cdot 00\cdot 101)(00100\cdot 101\cdot 00100)\cdots |  |

Since 0 = f ^ 1 0=\hat{f}_{1}, we hence obtain

(11) |  | f \displaystyle f | = \displaystyle= | 010 ​ ∏ n ≥ 2 f ^ n − 1 ​ f ^ n ​ f ^ n − 1 \displaystyle 010\prod_{n\geq 2}\hat{f}_{n-1}\hat{f}_{n}\hat{f}_{n-1} |  |

 |  | = \displaystyle= | 010 ⋅ ( 0 ⋅ 1 ⋅ 0) ​ ( 1 ⋅ 00 ⋅ 1) ​ ( 00 ⋅ 101 ⋅ 00) ​ ( 101 ⋅ 00100 ⋅ 101) ​ ⋯ \displaystyle 010\cdot(0\cdot 1\cdot 0)(1\cdot 00\cdot 1)(00\cdot 101\cdot 00)(101\cdot 00100\cdot 101)\cdots |  |

The factorization ( 11) is a sort of dual with Lucas numbers of the factorization in singular words ( 9). Indeed, the sequence of factor lengths in ( 9) is the sequence of Fibonacci numbers, while if in ( 11) one decomposes the first term as 01 ⋅ 0 01\cdot 0, then the sequence of factor lengths is the sequence of Lucas numbers (sequence A000032 in the On-Line Encyclopedia of Integer Sequences): 2,1,3,4,7,11, etc.

## 4. Christoffel words

The *lower Christoffel words*are defined by c n = 0 ​ p n ​ 1 c_{n}=0p_{n}1, for every n ≥ 3 n\geq 3. The lower Christoffel words are the Lyndon factors of f f, i.e., they are lexicographically smaller than any of their proper suffixes (with respect to the order induced by 0 < 1 0<1).

 | c 3 = 01 c 4 = 001 c 5 = 00101 c 6 = 00100101 c 7 = 0010010100101 c 8 = 001001010010010100101 \begin{split}c_{3}&=01\\ c_{4}&=001\\ c_{5}&=00101\\ c_{6}&=00100101\\ c_{7}&=0010010100101\\ c_{8}&=001001010010010100101\\ \end{split} |  |

Table 7. The first few lower Christoffel words.

If in the Euclidean plane one interprets each 0 0 by a horizontal unitary step and each 1 1 with a vertical unitary step, the lower Christoffel word c n c_{n} is the best grid approximation from below of the segment joining the point ( 0, 0) (0,0) to the point ( F n − 1, F n − 2) (F_{n-1},F_{n-2}) (see Figure 1).

[image: Refer to caption]

[image: Refer to caption]

Figure 1. The lower Christoffel word c 7 = 0010010100101 c_{7}=0010010100101 (left) and the upper Christoffel word c 7 ~ = 1010010100100 \widetilde{c_{7}}=1010010100100 (right) are the best grid approximations, respectively from above and from below, of the Euclidean segment joining the points ( 0, 0) (0,0) and ( 8, 5) = ( F 6, F 5) (8,5)=(F_{6},F_{5}).

Analogously, the *upper Christoffel words*are defined by c n ~ = 1 ​ p n ​ 0 \widetilde{c_{n}}=1p_{n}0, for every n ≥ 3 n\geq 3. Therefore, the upper Christoffel words are the reversals of the lower Christoffel words (we use the notation w ~ \widetilde{w} for the reversal, a.k.a. mirror image, of the word w w). The upper Christoffel words are the anti-Lyndon factors of f f, i.e., they are lexicographically greater than any of their proper suffixes (with respect to the order induced by 0 < 1 0<1). Moreover, c n ~ \widetilde{c_{n}} is the best grid approximation from above of the segment joining the point ( 0, 0) (0,0) to the point ( F n − 1, F n − 2) (F_{n-1},F_{n-2}).

###### Remark 3.

For every n ≥ 3 n\geq 3, c n = f n λ c_{n}=f^{\lambda}_{n} if n n is even, c n = f n λ ~ c_{n}=\widetilde{f^{\lambda}_{n}} if n n is odd. Therefore, c n ~ = f n λ ~ \widetilde{c_{n}}=\widetilde{f^{\lambda}_{n}} if n n is even, c n ~ = f n λ \widetilde{c_{n}}=f^{\lambda}_{n} if n n is odd.

 | c 3 ~ = 10 c 4 ~ = 100 c 5 ~ = 10100 c 6 ~ = 10100100 c 7 ~ = 1010010100100 c 8 ~ = 101001010010010100100 \begin{split}\widetilde{c_{3}}&=10\\ \widetilde{c_{4}}&=100\\ \widetilde{c_{5}}&=10100\\ \widetilde{c_{6}}&=10100100\\ \widetilde{c_{7}}&=1010010100100\\ \widetilde{c_{8}}&=101001010010010100100\\ \end{split} |  |

Table 8. The first few upper Christoffel words.

###### Lemma 3.

For every n ≥ 2 n\geq 2 one has

 | c 2 ​ n + 1 = c 2 ​ n ​ c 2 ​ n − 1, c 2 ​ n + 2 = c 2 ​ n ​ c 2 ​ n + 1, c_{2n+1}=c_{2n}c_{2n-1},\hskip 22.76219ptc_{2n+2}=c_{2n}c_{2n+1}, |  |

and therefore

 | c 2 ​ n + 1 ~ = c 2 ​ n − 1 ~ ​ c 2 ​ n ~, c 2 ​ n + 2 ~ = c 2 ​ n + 1 ~ ​ c 2 ​ n ~. \widetilde{c_{2n+1}}=\widetilde{c_{2n-1}}\widetilde{c_{2n}},\hskip 22.76219pt\widetilde{c_{2n+2}}=\widetilde{c_{2n+1}}\widetilde{c_{2n}}. |  |

###### Proof.

The first part follows from Lemma 2 by applying the right rotation to each side of the equalities. The second part follows from the first by applying the reversal. ∎

The following result states that every Christoffel word is the product of two singular words.

###### Lemma 4.

For every n ≥ 1 n\geq 1 one has

- •

c 2 ​ n + 1 = f ^ 2 ​ n − 1 ​ f ^ 2 ​ n c_{2n+1}=\hat{f}_{2n-1}\hat{f}_{2n}

- •

c 2 ​ n + 2 = f ^ 2 ​ n + 1 ​ f ^ 2 ​ n c_{2n+2}=\hat{f}_{2n+1}\hat{f}_{2n}

and therefore

- •

c 2 ​ n + 1 ~ = f ^ 2 ​ n ​ f ^ 2 ​ n − 1 \widetilde{c_{2n+1}}=\hat{f}_{2n}\hat{f}_{2n-1}

- •

c 2 ​ n + 2 ~ = f ^ 2 ​ n ​ f ^ 2 ​ n + 1 \widetilde{c_{2n+2}}=\hat{f}_{2n}\hat{f}_{2n+1}

###### Proof.

Follows directly from Lemma 1 and the definitions of Christoffel and singular words. ∎

Melançon [9] proved that the Fibonacci word is the concatenation of the odd lower Christoffel words:

###### Proposition 5.

The Fibonacci word is the concatenation of the odd lower Christoffel words:

(12) |  | f \displaystyle f | = \displaystyle= | ∏ n ≥ 1 c 2 ​ n + 1 \displaystyle\prod_{n\geq 1}c_{2n+1} |  |

 |  | = \displaystyle= | 01 ⋅ 00101 ⋅ 0010010100101 ⋅ ⋯ \displaystyle 01\cdot 00101\cdot 0010010100101\cdots |  |

###### Proof.

Follows directly from ( 9) and Lemma 4. ∎

Actually, Melançon proved that ( 12) is precisely the Lyndon factorization of f f. Recall that the Lyndon factorization of a word w w is w = ℓ 1 ℓ 2 ⋯ w=\ell_{1}\ell_{2}\cdots, where each ℓ i \ell_{i} is a Lyndon word and is lexicographically greater than or equal to ℓ i + 1 \ell_{i+1}. The uniqueness of such a factorization for finite words is a well-known theorem of Chen, Fox and Lyndon [4]. Siromoney et al. extended this factorization to infinite words [11].

Symmetrically, we have the following:

###### Proposition 6.

The Fibonacci word is the concatenation of 0 0 and the even upper Christoffel words:

(13) |  | f \displaystyle f | = \displaystyle= | 0 ​ ∏ n ≥ 2 c 2 ​ n ~ \displaystyle 0\prod_{n\geq 2}\widetilde{c_{2n}} |  |

 |  | = \displaystyle= | 0 ⋅ 100 ⋅ 10100100 ⋅ 101001010010010100100 ⋅ ⋯ \displaystyle 0\cdot 100\cdot 10100100\cdot 101001010010010100100\cdots |  |

###### Proof.

Follows directly from ( 9) and Lemma 4. ∎

In fact, it is easy to see that ( 13) is the Lyndon factorization of f f if one takes the order induced by 1 < 0 1<0.

We now present two other factorizations based on Christoffel words. To the best of our knowledge, these factorizations did not appear before in literature.

###### Proposition 7.

The Fibonacci word is the concatenation of 010 010 and the lower Christoffel words where each odd lower Christoffel word is squared:

(14) |  | f \displaystyle f | = \displaystyle= | 010 ​ ∏ n ≥ 1 c 2 ​ n + 1 2 ​ c 2 ​ n + 2 \displaystyle 010\prod_{n\geq 1}c_{2n+1}^{2}c_{2n+2} |  |

 |  | = \displaystyle= | 010 ⋅ ( 01 ⋅ 01 ⋅ 001) ​ ( 00101 ⋅ 00101 ⋅ 00100101) ​ ⋯ \displaystyle 010\cdot(01\cdot 01\cdot 001)(00101\cdot 00101\cdot 00100101)\cdots |  |

###### Proof.

Follows directly from ( 6) and Lemma 4. Indeed, by Lemma 4, we have

 | c 2 ​ n + 1 ​ c 2 ​ n + 1 ​ c 2 ​ n + 2 = f ^ 2 ​ n − 1 ​ f ^ 2 ​ n ⋅ f ^ 2 ​ n − 1 ​ f ^ 2 ​ n ⋅ f ^ 2 ​ n + 1 ​ f ^ 2 ​ n = ( f ^ 2 ​ n − 1 ​ f ^ 2 ​ n ​ f ^ 2 ​ n − 1) ​ ( f ^ 2 ​ n ​ f ^ 2 ​ n + 1 ​ f ^ 2 ​ n). c_{2n+1}c_{2n+1}c_{2n+2}=\hat{f}_{2n-1}\hat{f}_{2n}\cdot\hat{f}_{2n-1}\hat{f}_{2n}\cdot\hat{f}_{2n+1}\hat{f}_{2n}=(\hat{f}_{2n-1}\hat{f}_{2n}\hat{f}_{2n-1})(\hat{f}_{2n}\hat{f}_{2n+1}\hat{f}_{2n}). |  |

∎

Analogously, we have the following:

###### Proposition 8.

The Fibonacci word is the concatenation of 0100 0100 and the upper Christoffel words where each even upper Christoffel word is squared:

(15) |  | f \displaystyle f | = \displaystyle= | 0100 ​ ∏ n ≥ 1 c 2 ​ n + 1 ~ ​ c 2 ​ n + 2 ~ 2 \displaystyle 0100\prod_{n\geq 1}\widetilde{c_{2n+1}}\widetilde{c_{2n+2}}^{2} |  |

 |  | = \displaystyle= | 0100 ⋅ ( 10 ⋅ 100 ⋅ 100) ​ ( 10100 ⋅ 10100100 ⋅ 10100100) ​ ⋯ \displaystyle 0100\cdot(10\cdot 100\cdot 100)(10100\cdot 10100100\cdot 10100100)\cdots |  |

###### Proof.

Follows directly from ( 5) and Lemma 4. Indeed, by Lemma 4, we have

 | c 2 ​ n + 1 ~ ​ c 2 ​ n + 2 ~ ​ c 2 ​ n + 2 ~ = f ^ 2 ​ n ​ f ^ 2 ​ n − 1 ⋅ f ^ 2 ​ n ​ f ^ 2 ​ n + 1 ⋅ f ^ 2 ​ n ​ f ^ 2 ​ n + 1 = ( f ^ 2 ​ n ​ f ^ 2 ​ n − 1 ​ f ^ 2 ​ n) ​ ( f ^ 2 ​ n + 1 ​ f ^ 2 ​ n ​ f ^ 2 ​ n + 1). \widetilde{c_{2n+1}}\widetilde{c_{2n+2}}\widetilde{c_{2n+2}}=\hat{f}_{2n}\hat{f}_{2n-1}\cdot\hat{f}_{2n}\hat{f}_{2n+1}\cdot\hat{f}_{2n}\hat{f}_{2n+1}=(\hat{f}_{2n}\hat{f}_{2n-1}\hat{f}_{2n})(\hat{f}_{2n+1}\hat{f}_{2n}\hat{f}_{2n+1}). |  |

∎

## 5. Reversals of Fibonacci words

One of the most known factorizations of the Fibonacci infinite word, and perhaps the most surprising, is the following.

###### Proposition 9.

The Fibonacci word can be obtained also by concatenating the reversals of the Fibonacci words:

(16) |  | f \displaystyle f | = \displaystyle= | ∏ n ≥ 2 f n ~ \displaystyle\prod_{n\geq 2}\widetilde{f_{n}} |  |

 |  | = \displaystyle= | 0 ⋅ 10 ⋅ 010 ⋅ 10010 ⋅ 01010010 ⋅ ⋯ \displaystyle 0\cdot 10\cdot 010\cdot 10010\cdot 01010010\cdots |  |

###### Proof.

It follows from the definitions that taking the right rotation of f n ~ \widetilde{f_{n}} and complementing the last letter produces the n n -th singular word f ^ n \hat{f}_{n}. Therefore, ( 16) follows directly from ( 9) observing that the reversals of the Fibonacci words start with 0 0 and 1 1 alternatingly. ∎

The factorization ( 16) is basically the Crochemore factorization of f f —the only difference is that the Crochemore factorization starts with 0 0, 1 1, 0 0 and then coincides with the one above (see [3]). Recall that the Crochemore factorization of w w is w = c 1 c 2 ⋯ w=c_{1}c_{2}\cdots where c 1 c_{1} is the first letter of w w and for every i > 1 i>1, c i c_{i} is either a fresh letter or the longest prefix of c i c i + 1 ⋯ c_{i}c_{i+1}\cdots occurring twice in f 1 f 2 ⋯ f i f_{1}f_{2}\cdots f_{i}. For example, the Crochemore factorization of the word w = 0101001 w=0101001 is 0 ⋅ 1 ⋅ 010 ⋅ 01 0\cdot 1\cdot 010\cdot 01, since 010 010 occurs twice in 01010 01010.

In 1995, de Luca [5] considered the following factorization:

###### Proposition 10.

The Fibonacci word can be obtained by concatenating the reversals of the even Fibonacci words.

(17) |  | f \displaystyle f | = \displaystyle= | ∏ n ≥ 2 f 2 ​ n ~ \displaystyle\prod_{n\geq 2}\widetilde{f_{2n}} |  |

 |  | = \displaystyle= | 010 ⋅ 01010010 ⋅ 010100101001001010010 ⋅ ⋯ \displaystyle 010\cdot 01010010\cdot 010100101001001010010\cdots |  |

###### Proof.

Applying the reversal to ( 2) (\ref{eq:rec}), we have that f n ~ = f n − 2 ~ ​ f n − 1 ~ \widetilde{f_{n}}=\widetilde{f_{n-2}}\widetilde{f_{n-1}}, for every n > 2 n>2. So ( 17) follows directly from ( 16) by replacing f 2 ​ n − 2 ~ ​ f 2 ​ n − 1 ~ \widetilde{f_{2n-2}}\widetilde{f_{2n-1}} with f 2 ​ n ~ \widetilde{f_{2n}}. ∎

In [5] de Luca proved that the factorization ( 17) has the following minimal property with respect to the lexicographical order: any non-trivial permutation of a finite number of the factors will produce an infinite word that is lexicographically greater than f f.

Concatenating the reversals of the odd Fibonacci words instead of even ones still produces the Fibonacci word, if one prepends a 0 0:

###### Proposition 11.

The Fibonacci word can be obtained by concatenating 0 0 and the reversals of the odd Fibonacci words:

(18) |  | f \displaystyle f | = \displaystyle= | 0 ​ ∏ n ≥ 2 f 2 ​ n + 1 ~ \displaystyle 0\prod_{n\geq 2}\widetilde{f_{2n+1}} |  |

 |  | = \displaystyle= | 0 ⋅ 10010 ⋅ 1001001010010 ⋅ ⋯ \displaystyle 0\cdot 10010\cdot 1001001010010\cdots |  |

###### Proof.

Follows directly from ( 16) by replacing f 2 ​ n − 1 ~ ​ f 2 ​ n ~ \widetilde{f_{2n-1}}\widetilde{f_{2n}} with f 2 ​ n + 1 ~ \widetilde{f_{2n+1}}. ∎

Recently [7], studying the so-called *open*and *closed*words, the following factorization has been proved:

###### Proposition 12.

The Fibonacci word can be obtained by concatenating 01 01 and the squares of the reversals of the Fibonacci words:

(19) |  | f \displaystyle f | = \displaystyle= | 01 ​ ∏ n ≥ 2 ( f n ~) 2 \displaystyle 01\prod_{n\geq 2}(\widetilde{f_{n}})^{2} |  |

 |  | = \displaystyle= | 01 ⋅ ( 0 ⋅ 0) ​ ( 10 ⋅ 10) ​ ( 010 ⋅ 010) ​ ( 10010 ⋅ 10010) ​ ⋯ \displaystyle 01\cdot(0\cdot 0)(10\cdot 10)(010\cdot 010)(10010\cdot 10010)\cdots |  |

###### Proof.

Recalling that for every n ≥ 3 n\geq 3, one has f n ~ = f n − 2 ~ ​ f n − 1 ~ \widetilde{f_{n}}=\widetilde{f_{n-2}}\widetilde{f_{n-1}}, we have, from ( 16), that f = f 2 ~ f 3 ~ f 4 ~ ⋯ = 0 ⋅ f 1 ~ f 2 ~ f 2 ~ f 3 ~ ⋯ = 01 ⋅ ( f 2 ~ f 2 ~) ( f 3 ~ f 3 ~) ⋯ = 01 ∏ n ≥ 2 ( f n ~) 2 f=\widetilde{f_{2}}\widetilde{f_{3}}\widetilde{f_{4}}\cdots=0\cdot\widetilde{f_{1}}\widetilde{f_{2}}\widetilde{f_{2}}\widetilde{f_{3}}\cdots=01\cdot(\widetilde{f_{2}}\widetilde{f_{2}})(\widetilde{f_{3}}\widetilde{f_{3}})\cdots=01\prod_{n\geq 2}(\widetilde{f_{n}})^{2}. ∎

## 6. Generalization to standard Sturmian words

The Fibonacci word is the most prominent example of a *standard Sturmian word*. Let α \alpha be an irrational number such that 0 < α < 1 0<\alpha<1, and let [0; d 1 + 1, d 2, d 3, …] \left[0;d_{1}+1,d_{2},d_{3},\ldots\right] be the continued fraction expansion of α \alpha. The sequence of words defined by s 1 = 1 s_{1}=1, s 2 = 0 s_{2}=0 and s n = s n − 1 d n − 2 ​ s n − 2 s_{n}=s_{n-1}^{d_{n-2}}s_{n-2} for n ≥ 3 n\geq 3, converges to the infinite word w α w_{\alpha}, called the standard Sturmian word of slope α \alpha. The sequence of words s n s_{n} is called the standard sequence of w α w_{\alpha}. The Fibonacci word is the standard Sturmian word of slope α = ( 3 − 5) / 2 \alpha=(3-\sqrt{5})/2 and its standard sequence is the sequence of Fibonacci finite words, since one has d i = 1 d_{i}=1 for every i ≥ 1 i\geq 1.

Most of the factorizations we described in this note can be generalized to any standard Sturmian word. However, the proofs become more technical and less easy to present.

## References

- [1] J. Berstel, Fibonacci words, a survey. In G. Rozenberg and A. Salomaa, editors, The Book of L, Springer-Verlang, 1985, pp. 11–25.
- [2] J. Berstel, On the index of Sturmian words. In Juhani Karhumäki, Hermann Maurer, Gheorghe Pǎun, and Grzegorz Rozenberg, editors, Jewels are Forever, Springer, 1999, pp. 287–294.
- [3] J. Berstel and A. Savelli, Crochemore factorization of Sturmian and other infinite words, In Mathematical Foundations of Computer Science, Vol. 4162 of Lecture Notes in Computer Science, Springer, 2006, pp. 157–166.
- [4] K. T. Chen, R. H. Fox, and R. C. Lyndon, Free differential calculus, IV — the quotient groups of the lower central series, Ann. Math. 68 (1958), 81–95.
- [5] A. de Luca, A division property of the Fibonacci word, Inform. Process. Letters 54 (1995), 307–312.
- [6] A. de Luca and A. De Luca, Combinatorial properties of Sturmian palindromes, Internat. J. Found. Comput. Sci. 17 (2006), 557–573.
- [7] A. De Luca and G. Fici, Open and closed prefixes of Sturmian words, In Proceedings of the 9th International Conference on Words, Vol. 8079 of Lecture Notes in Computer Science, Springer, 2013, pp. 132–142.
- [8] C. G. Lekkerkerker, Voorstelling van natuurlijke getallen door een som van Fibonacci, Simon Stevin 29 (1951–52), 190–195.
- [9] G. Melançon, Lyndon words and singular factors of Sturmian words, Theoret. Comput. Sci. 218 (1999), 41–59.
- [10] A. Ostrowski, Bemerkungen zur theorie der diophantischen approximationen, Abh. Math. Sem. Hamburg 1 (1922), 250–251. Reprinted in Collected Mathematical Papers, Vol. 3, pp. 57–80.
- [11] R. Siromoney, L. Matthew, V. R. Dare, and K. G. Subramanian, Infinite Lyndon words, Inform. Process. Letters 50 (1994), 101–104.
- [12] Z.-X. Wen and Z.-Y. Wen, Some properties of the singular words of the Fibonacci word, European J. Combin. 15 (1994), 587–598.
- [13] É. Zeckendorf, Représentation des nombres naturels par une somme de nombres de Fibonacci ou de nombres de Lucas, Bull. Soc. Roy. Sci. Liège 41 (1972), 179–182.
- [14] J. Ziv and A. Lempel, A universal algorithm for sequential data compression, IEEE Trans. Inf. Theor. 23 (3) (1977), 337–343.

[◄][2][image: ar5iv homepage] [3]
[Feeling lucky?][4] [5]
[Conversion report][6]
[Report an issue][7]
[View original on arXiv][8] [►][9]


## Links

[1]: mailto:Gabriele.Fici@unipa.it
[2]: /html/1508.06753
[3]: /
[4]: /feeling_lucky
[5]: /land_of_honey_and_milk
[6]: /log/1508.06754
[7]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1508.06754
[8]: https://arxiv.org/pdf/1508.06754
[9]: /html/1508.06755
