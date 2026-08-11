> **Excerpt only — read this first.** The complete text is one level down at `research/L0.1/order_statistic_wikipedia_renyi_representation.full.md`; open that only when this file does not answer the question, because it is large. Replace this excerpt with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://en.wikipedia.org/wiki/Order_statistic | converted from HTML -->

Order statistic - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Kth smallest value in a statistical sample

 |

This article includes a list of [general references][1]**but lacks sufficient corresponding [inline citations][2]**. Please help [improve this article][3] by [introducing][4] more precise citations.*( December 2010)**( [Learn how and when to remove this message][5])*

 |

[6] [Probability density functions][7] of the order statistics for a sample of size *n*= 5 from an [exponential distribution][8] with unit scale parameter

In [statistics][9], the *k*th **order statistic**of a [statistical sample][10] is equal to its *k*th-smallest value. [1] Given a sample of size n {\displaystyle n}[image: {\displaystyle n}], the *k*th order statistic is denoted x ( k) {\displaystyle x_{(k)}}[image: {\displaystyle x_{(k)}}], with 1 ≤ k ≤ n {\displaystyle 1\leq k\leq n}[image: {\displaystyle 1\leq k\leq n}]. Together with [rank statistics][11], order statistics are among the most fundamental tools in [non-parametric statistics][12] and [inference][13].

Important special cases of the order statistics are the [minimum][14] and [maximum][15] value of a sample, and (with some qualifications discussed below) the [sample median][16] and other [sample quantiles][17].

When using [probability theory][18] to analyze order statistics of [random samples][19] from a [continuous distribution][20], the [cumulative distribution function][21] is used to reduce the analysis to the case of order statistics of the [uniform distribution][22].

## Notation and examples

[[edit][23]]

For example, suppose that four numbers are observed or recorded, resulting in a sample of size 4. If the sample values are

6, 9, 3, 7

the order statistics would be

x ( 1) = 3 x ( 2) = 6 x ( 3) = 7 x ( 4) = 9 {\displaystyle {\begin{aligned}x_{(1)}&=3\\x_{(2)}&=6\\x_{(3)}&=7\\x_{(4)}&=9\end{aligned}}}[image: {\displaystyle {\begin{aligned}x_{(1)}&=3\\x_{(2)}&=6\\x_{(3)}&=7\\x_{(4)}&=9\end{aligned}}}]

The **first order statistic**(or **smallest order statistic**) is always the [minimum][14] of the sample, that is,

X ( 1) = min { X 1, …, X n } {\displaystyle X_{(1)}=\min\{\,X_{1},\ldots ,X_{n}\,\}}[image: {\displaystyle X_{(1)}=\min\{\,X_{1},\ldots ,X_{n}\,\}}]

where, following a common convention, we use upper-case letters to refer to random variables, and lower-case letters (as above) to refer to their actual observed values.

Similarly, for a sample of size *n*, the *n*th order statistic (or **largest order statistic**) is the [maximum][15], that is,

X ( n) = max { X 1, …, X n }. {\displaystyle X_{(n)}=\max\{\,X_{1},\ldots ,X_{n}\,\}.}[image: {\displaystyle X_{(n)}=\max\{\,X_{1},\ldots ,X_{n}\,\}.}]

The [sample range][24] is the difference between the maximum and minimum. It is a function of the order statistics:

R a n g e { X 1, …, X n } = X ( n) − X ( 1). {\displaystyle {\rm {Range}}\{\,X_{1},\ldots ,X_{n}\,\}=X_{(n)}-X_{(1)}.}[image: {\displaystyle {\rm {Range}}\{\,X_{1},\ldots ,X_{n}\,\}=X_{(n)}-X_{(1)}.}]

A similar important statistic in [exploratory data analysis][25] that is simply related to the order statistics is the sample [interquartile range][26].

The sample median may or may not be an order statistic, since there is a single middle value only when the number *n*of observations is [odd][27]. More precisely, if *n*= 2*m*+1 for some integer *m*, then the sample median is X ( m + 1) {\displaystyle X_{(m+1)}}[image: {\displaystyle X_{(m+1)}}] and so is an order statistic. On the other hand, when *n*is [even][27], *n*= 2*m*and there are two middle values, X ( m) {\displaystyle X_{(m)}}[image: {\displaystyle X_{(m)}}] and X ( m + 1) {\displaystyle X_{(m+1)}}[image: {\displaystyle X_{(m+1)}}], and the sample median is some function of the two (usually the average) and hence not an order statistic. Similar remarks apply to all sample quantiles.


*[excerpt ends; 75082 characters not shown — see `research/L0.1/order_statistic_wikipedia_renyi_representation.full.md`]*
