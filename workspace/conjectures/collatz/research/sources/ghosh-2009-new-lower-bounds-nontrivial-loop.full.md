<!-- source: https://arxiv.org/html/0907.3086v4 | converted from HTML -->

New lower bounds for the size of a non-trivial loop in the Collatz 3x+1 and generalized px+q problem

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:0907.3086v4 [math.GM] 09 Aug 2009

# New lower bounds for the size of a non-trivial loop in the Collatz 3x+1 and generalized px+q problem

Roupam Ghosh

Date: 28 July 2009

Abstract

In the Collatz 3x+1 problem, there are 3 possibilities: Starting from any positive number, we either reach the trivial loop (1,4,2), end up in a non-trivial loop, or go until infinity. In this paper, we shall show that if a non-trivial loop with m m odd numbers exists, then its minimum odd number is bounded above by a function of m m. We shall also use that bound to calculate the least number of odd elements required for a non-trivial loop to exist. Also, the generalized bounds for the px+q problem are given.

Introduction to the Collatz problem

Consider the function,

 | f ⁡ ( x) = { x 2 if x is even 3 ​ x + 1 if x is odd f(x)=\begin{cases}\frac{x}{2}&\text{if $x$ is even}\\ 3x+1&\text{if $x$ is odd}\end{cases} |  |

The Collatz 3x+1 conjecture states that for every positive integer x x, there exists an integer d ( ≥ 0) d(\geq 0) corresponding to x x such that f ( d) ​ ( x) = 1 f^{(d)}(x)=1, where f ( d) ( x) = f ( f ( f ( … d f^{(d)}(x)=f(f(f(...d times... ( f ( f ( f ( x)))))))...(f(f(f(x)))))))
For example, the iterations of f f on a few numbers are given below:

(1) |  | 1 → 1 2 → 1 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 4 → 2 → 1 5 → 16 → 8 → 4 → 2 → 1 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 and so on… \begin{split}&1\rightarrow 1\\ &2\rightarrow 1\\ &3\rightarrow 10\rightarrow 5\rightarrow 16\rightarrow 8\rightarrow 4\rightarrow 2\rightarrow 1\\ &4\rightarrow 2\rightarrow 1\\ &5\rightarrow 16\rightarrow 8\rightarrow 4\rightarrow 2\rightarrow 1\\ &6\rightarrow 3\rightarrow 10\rightarrow 5\rightarrow 16\rightarrow 8\rightarrow 4\rightarrow 2\rightarrow 1\\ &\text{and so on...}\end{split} |  |

Considering only odd numbers

Now, let us consider only odd integers of the Collatz sequence and modify the function f f to a function T T defined on odd integers such that T ⁡ ( x) = ( 3 ​ x + 1) 2 k T(x)=\frac{(3x+1)}{2^{k}}, where k k is the highest power of two in which 2 k 2^{k} divides 3 ​ x + 1 3x+1.

For example, we have for x = 7 x=7:

(2) |  | T ( 7) = 11, T ( 2) ( 7) = 17, T ( 3) ( 7) = 13, T ( 4) ( 7) = 5, T ( 5) ( 7) = 1, T ( 6) ( 7) = 1, T ( 7) ( 7) = 1, … k 1 = 1, k 2 = 1, k 3 = 2, k 4 = 3, k 5 = 4, k 6 = 2, k 7 = 2, … \begin{split}T(7)=11,T^{(2)}(7)=17,T^{(3)}(7)=13,T^{(4)}(7)=5,T^{(5)}(7)=1,T^{(6)}(7)=1,T^{(7)}(7)=1,...\\ k_{1}=1,k_{2}=1,k_{3}=2,k_{4}=3,k_{5}=4,k_{6}=2,k_{7}=2,...\end{split} |  |

and so on, where k i k_{i} is the highest power of two which divides 3 ​ T ( i − 1) ​ ( x) + 1 3T^{(i-1)}(x)+1. The iterations of T T on a few odd numbers are given below:

(3) |  | 1 → 1 3 → 5 → 1 5 → 1 7 → 11 → 17 → 13 → 5 → 1 9 → 7 → 11 → 17 → 13 → 5 → 1 11 → 17 → 13 → 5 → 1 13 → 5 → 1 15 → 23 → 35 → 53 → 5 → 1 and so on… \begin{split}&1\rightarrow 1\\ &3\rightarrow 5\rightarrow 1\\ &5\rightarrow 1\\ &7\rightarrow 11\rightarrow 17\rightarrow 13\rightarrow 5\rightarrow 1\\ &9\rightarrow 7\rightarrow 11\rightarrow 17\rightarrow 13\rightarrow 5\rightarrow 1\\ &11\rightarrow 17\rightarrow 13\rightarrow 5\rightarrow 1\\ &13\rightarrow 5\rightarrow 1\\ &15\rightarrow 23\rightarrow 35\rightarrow 53\rightarrow 5\rightarrow 1\\ &\text{and so on...}\end{split} |  |

Some inequalities

Starting with any arbitrary odd integer a 1 a_{1}, let a r = T ( r) ​ ( a 1) a_{r}=T^{(r)}(a_{1}). Let us suppose a non-trivial loop exists and consists of m odd numbers. Let us consider 2 1 k, 2 2 k ​ …, 2 m k 2^{k}_{1},2^{k}_{2}...,2^{k}_{m} to be the highest powers of two which divide 3 ​ a 1 + 1, 3 ​ a 2 + 1, …, 3 ​ a m + 1, 3a_{1}+1,3a_{2}+1,...,3a_{m}+1, respectively.

And let us denote S r = k 1 + k 2 + … ​ k r S_{r}=k_{1}+k_{2}+...k_{r}. Then we shall have

(4) |  | a m + 1 = 3 m 2 S m ​ a 1 + c m 2 S m a_{m+1}=\frac{3^{m}}{2^{S_{m}}}a_{1}+\frac{c_{m}}{2^{S_{m}}} |  |

where c m = 3 m − 1 + 3 m − 2 ​ 2 S 1 + … + 3 2 ​ 2 S m − 3 + 3 1 ​ 2 S m − 2 + 2 S m − 1. c_{m}=3^{m-1}+3^{m-2}2^{S_{1}}+...+3^{2}2^{S_{m-3}}+3^{1}2^{S_{m-2}}+2^{S_{m-1}}.

Therefore, by definition,

(5) |  | 2 S r = 2 k 1 + k 2 + … + k r = ( 3 ​ a 1 + 1) a 2 ​ ( 3 ​ a 2 + 1) a 3 ​ … ​ ( 3 ​ a r + 1) a r + 1 = ( 3 + 1 a 1) ​ ( 3 + 1 a 2) ​ … ​ ( 3 + 1 a r) ​ a 1 a r + 1 \begin{split}2^{S_{r}}&=2^{k_{1}+k_{2}+...+k_{r}}\\ &=\frac{(3a_{1}+1)}{a_{2}}\frac{(3a_{2}+1)}{a_{3}}...\frac{(3a_{r}+1)}{a_{r+1}}\\ &=(3+\frac{1}{a_{1}})(3+\frac{1}{a_{2}})...(3+\frac{1}{a_{r}})\frac{a_{1}}{a_{r+1}}\\ \end{split} |  |

Then for a 1 = a m + 1 a_{1}=a_{m+1}, i.e., for a loop containing m m odd numbers, we shall have

(6) |  | 2 S m = ( 3 + 1 a 1) ​ ( 3 + 1 a 2) ​ … ​ ( 3 + 1 a m) 2^{S_{m}}=(3+\frac{1}{a_{1}})(3+\frac{1}{a_{2}})...(3+\frac{1}{a_{m}}) |  |

Let us consider a m ​ i ​ n a_{min} to be the minimum among a 1, a 2, …, a m a_{1},a_{2},...,a_{m}. Then we have

(7) |  | 3 m < 2 S m < ( 3 + 1 a m ​ i ​ n) m m ⁡ ( log 2 ⁡ 3) < S m < m ⁡ ( log 2 ⁡ 3) + m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) \begin{split}&3^{m}<2^{S_{m}}<(3+\frac{1}{a_{min}})^{m}\\ &m(\log_{2}3)<S_{m}<m(\log_{2}3)+m\log_{2}(1+\frac{1}{3a_{min}})\end{split} |  |

Deriving the bound

Now, since S m S_{m} is a positive integer, if

 | [m ⁡ ( log 2 ⁡ 3) + m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n)] − [m ⁡ ( log 2 ⁡ 3)] = 0 [m(\log_{2}3)+m\log_{2}(1+\frac{1}{3a_{min}})]-[m(\log_{2}3)]=0 |  |

then no integer solution S m S_{m} exists (where [x] is the floor function), and this will imply that no loop exists with m-odd numbers. Here, { x } \{x\} denotes x − [x] x-[x], the fractional part of x x. Now, if the above condition is true then we have

 | m ⁡ ( log 2 ⁡ 3) + m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) − { m ⁡ ( log 2 ⁡ 3) + m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) } = m ⁡ ( log 2 ⁡ 3) − { m ⁡ ( log 2 ⁡ 3) } or m log 2 ( 1 + 1 3 ​ a m ​ i ​ n) = { m ( log 2 3) + m log 2 ( 1 + 1 3 ​ a m ​ i ​ n) } − { m ( log 2 3). } \begin{split}&m(\log_{2}3)+m\log_{2}(1+\frac{1}{3a_{min}})-\{m(\log_{2}3)+m\log_{2}(1+\frac{1}{3a_{min}})\}=m(\log_{2}3)-\{m(\log_{2}3)\}\\ &\text{or }m\log_{2}(1+\frac{1}{3a_{min}})=\{m(\log_{2}3)+m\log_{2}(1+\frac{1}{3a_{min}})\}-\{m(\log_{2}3).\}\end{split} |  |

So if there is an integer solution for S m S_{m}, we must have

 | m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) > { m ⁡ ( log 2 ⁡ 3) + m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) } − { m ⁡ ( log 2 ⁡ 3) }. m\log_{2}(1+\frac{1}{3a_{min}})>\{m(\log_{2}3)+m\log_{2}(1+\frac{1}{3a_{min}})\}-\{m(\log_{2}3)\}. |  |

This leaves us with only two possibilities, m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) > 1 m\log_{2}(1+\frac{1}{3a_{min}})>1 or m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) < 1 m\log_{2}(1+\frac{1}{3a_{min}})<1.

Bound for the case m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) > 1 m\log_{2}(1+\frac{1}{3a_{min}})>1:

 | m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) > 1 m\log_{2}(1+\frac{1}{3a_{min}})>1 |  |

Rearranging the terms of m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) > 1 m\log_{2}(1+\frac{1}{3a_{min}})>1, we get

 | a m ​ i ​ n < 1 3 ​ ( 2 1 m − 1) a_{min}<\frac{1}{3(2^{\frac{1}{m}}-1)} |  |

We shall define α ⁡ ( m) \alpha(m) to be 1 3 ​ ( 2 1 m − 1) \frac{1}{3(2^{\frac{1}{m}}-1)}.

Bound for the case m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) < 1 m\log_{2}(1+\frac{1}{3a_{min}})<1:

From above, if a solution for S m S_{m} exists then we have

 | m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) > { m ⁡ ( log 2 ⁡ 3) + m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) } − { m ⁡ ( log 2 ⁡ 3) } m\log_{2}(1+\frac{1}{3a_{min}})>\{m(\log_{2}3)+m\log_{2}(1+\frac{1}{3a_{min}})\}-\{m(\log_{2}3)\} |  |

But, since m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) < 1 m\log_{2}(1+\frac{1}{3a_{min}})<1, { m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) } = m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) \{m\log_{2}(1+\frac{1}{3a_{min}})\}=m\log_{2}(1+\frac{1}{3a_{min}}).
Hence,

 | { m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) } > { m ⁡ ( log 2 ⁡ 3) + m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) } − { m ⁡ ( log 2 ⁡ 3) } \{m\log_{2}(1+\frac{1}{3a_{min}})\}>\{m(\log_{2}3)+m\log_{2}(1+\frac{1}{3a_{min}})\}-\{m(\log_{2}3)\} |  |

or

 | { m ⁡ ( log 2 ⁡ 3) } + { m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) } > { m ⁡ ( log 2 ⁡ 3) + m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) } \{m(\log_{2}3)\}+\{m\log_{2}(1+\frac{1}{3a_{min}})\}>\{m(\log_{2}3)+m\log_{2}(1+\frac{1}{3a_{min}})\} |  |

This is only possible if

 | { m ⁡ ( log 2 ⁡ 3) } + { m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) } > 1. \{m(\log_{2}3)\}+\{m\log_{2}(1+\frac{1}{3a_{min}})\}>1. |  |

Therefore, we have

 | m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) > 1 − { m ⁡ ( log 2 ⁡ 3) }. m\log_{2}(1+\frac{1}{3a_{min}})>1-\{m(\log_{2}3)\}. |  |

Rearranging the terms, we get

 | a m ​ i ​ n < 1 3 ​ ( 2 1 − { m ​ log 2 ​ 3 } m − 1). a_{min}<\frac{1}{3(2^{\frac{1-\{m\log_{2}3\}}{m}}-1)}. |  |

We shall define β ⁡ ( m) \beta(m) to be 1 3 ​ ( 2 1 − { m ​ log 2 ​ 3 } m − 1) \frac{1}{3(2^{\frac{1-\{m\log_{2}3\}}{m}}-1)}.

Some new definitions:

We shall divide the possible non-trivial loops of a Collatz sequence into two classes: We call loops satisfying the equation

 | m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) > 1 m\log_{2}(1+\frac{1}{3a_{min}})>1 |  |

α \alpha -loops and loops satisfying the equation

 | m ​ log 2 ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) < 1 m\log_{2}(1+\frac{1}{3a_{min}})<1 |  |

β \beta -loops.
Note that for α \alpha -loops we have a m ​ i ​ n < α ⁡ ( m) a_{min}<\alpha(m) and for β \beta -loops we have a m ​ i ​ n < β ⁡ ( m) a_{min}<\beta(m).

Computing the least number of odd numbers a loop must have

The Collatz algorithm has been tested and found to always reach 1 1 for all numbers ≤ 19 × 2 58 \leq 19\times 2^{58} (Oliveira e Silva 2008).
For α \alpha -loops, we have

 | a m ​ i ​ n < 1 3 ​ ( 2 1 m − 1) a_{min}<\frac{1}{3(2^{\frac{1}{m}}-1)} |  |

i.e.,

 | m > log ⁡ ( 2) log ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) m>\frac{\log(2)}{\log(1+\frac{1}{3a_{min}})} |  |

Putting a m ​ i ​ n = 19 × 2 58 − 1 a_{min}=19\times 2^{58}-1, we get m > 11387806137299329586 m>11387806137299329586.

Hence, if an α \alpha -loop exists we must have at least 11,387,806,137,299, 329, 586 11,387,806,137,299,329,586 odd numbers in that loop.

For β \beta -loops we have

 | m 1 − { m ​ log 2 ​ 3 } > log ⁡ ( 2) log ⁡ ( 1 + 1 3 ​ a m ​ i ​ n) \frac{m}{1-\{m\log_{2}3\}}>\frac{\log(2)}{\log(1+\frac{1}{3a_{{min}}})} |  |

Given below is PARI/GP code I used for calculating the value of m m for β \beta -loops.

```

lhs(x) = ( x / (1 - frac( x*log(3.0)/log(2.0) ) ) );
rhs(x) = ( log(2)/log(1 + 1/(3*x) ) );
{
       a = rhs( 19 * ( 2^58) - 1 );
       m = 2;
       while(1,
                if( lhs(m) > a,
                         print(m," is our desired result ");
                         quit;
                         ,
                         print(m, " has been checked...");
                );ΨΨ
       m++;
       );
}

```

The value for β \beta -loop is 6,586,818,670 6,586,818,670.
That is, at least 6,586,818,670 6,586,818,670 odd numbers are required to form a β \beta -loop, which is much larger than the current largest known lower bound for the length of a nontrivial cycle (Sinisalo, 2003).

Bounds for the generalized px+q problem

Consider the function,

 | f ⁡ ( x) = { x 2 if x is even p ​ x + q if ​ x ​ is odd. Here ​ p ​ and ​ q ​ are both positive odd numbers f(x)=\begin{cases}\frac{x}{2}&\text{if $x$ is even}\\ px+q&\text{if }x\text{ is odd. Here }p\text{ and }q\text{ are both positive odd numbers }\end{cases} |  |

Then we shall have

 | α ⁡ ( m) = q p ⁡ ( 2 1 m − 1) \alpha(m)=\frac{q}{p(2^{\frac{1}{m}}-1)} |  |

 | β ⁡ ( m) = q p ⁡ ( 2 1 − { m ​ log 2 ​ p } m − 1) \beta(m)=\frac{q}{p(2^{\frac{1-\{m\log_{2}p\}}{m}}-1)} |  |

We denote this fact by introducing this new notation,

 | α m ​ ( p, q) = q p ⁡ ( 2 1 m − 1) \alpha_{m}(p,q)=\frac{q}{p(2^{\frac{1}{m}}-1)} |  |

 | β m ​ ( p, q) = q p ⁡ ( 2 1 − { m ​ log 2 ​ p } m − 1) \beta_{m}(p,q)=\frac{q}{p(2^{\frac{1-\{m\log_{2}p\}}{m}}-1)} |  |

For example, in our case of 3 ​ x + 1 3x+1, we have

 | α m ​ ( 3, 1) = 1 3 ​ ( 2 1 m − 1) \alpha_{m}(3,1)=\frac{1}{3(2^{\frac{1}{m}}-1)} |  |

Acknowledgements
I thank Craig Alan Feinstein for giving me feedback on various important steps, providing me useful insights, and also amongst other things, for being a good friend. Also, my thanks goes to Eric Farin for helping me by running the program on his computer. I thank my mom, sister, and dad for making my life wonderful.

References

1. (1)

Weisstein, Eric W. ”Collatz Problem.” From MathWorld–A Wolfram Web Resource. http://mathworld.wolfram.com/CollatzProblem.html

2. (2)

Toms Oliveira e Silva, http://www.ieeta.pt/~tos/3x+1.html

3. (3)

Shalom Eliahou (1993), ”The 3x+1 Problem, New Lower Bounds on a Nontrivial Cycle Lenghts”, Discrete Math 118

4. (4)

Busido Chisale (1994), ”Cycles in Collatz Sequences” Publ. Math. Debrecen 45

5. (5)

Lorentz Halbeisen and Norbert Hungerbuhler (1997), ”Optimal Bounds for the Length of Rationnal Collatz Cycles”, Acta Arithmetica 78

6. (6)

Matti Sinisalo (2003), ”On the Minimal Cycle Length of the Collatz Sequences”, Univ of Oulu, Finland

7. (7)

The PARI Group - PARI/GP version 2.3.4, http://pari.math.u-bordeaux.fr/


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
