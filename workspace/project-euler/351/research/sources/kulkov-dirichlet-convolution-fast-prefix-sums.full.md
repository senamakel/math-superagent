<!-- source: https://codeforces.com/blog/entry/117635 | converted from HTML -->

Dirichlet convolution. Part 1: Fast prefix sum computations - Codeforces

**

****

[image: Codeforces] [1]

[image: In English] [2][image: По-русски] [3]

[Enter][4] | [Register][5]

- [Home][1]
- [Top][6]
- [Catalog][7]
- [Contests][8]
- [Gym][9]
- [Problemset][10]
- [Groups][11]
- [Rating][12]
- [Edu][13]
- [API][14]
- [Calendar][15]
- [Help][16]

&rarr; Pay attention

Contest is running
[ICPC 2026 Online Challenge 1 powered by Huawei][17]
2 weeks
[Register now »][18]

&rarr; Top rated

# | User | Rating |

1 | [B enq][19] | 3857 |

2 | [j iangly][20] | 3812 |

3 | [V ivaciousAubergine][21] | 3647 |

4 | [m aroonrk][22] | 3536 |

5 | [t ourist][23] | 3530 |

6 | [K evin114514][24] | 3510 |

7 | [t urmax][25] | 3402 |

8 | [U m_nik][26] | 3389 |

9 | [R adewoosh][27] | 3367 |

10 | [h euristica][28] | 3322 |

[Countries][29] | [Cities][30] | [Organizations][31] | [View all &rarr;][12] |

&rarr; Top contributors

# | User | Contrib. |

1 | [Q ingyu][32] | 157 |

2 | [m aspy][33] | 149 |

3 | [U m_nik][26] | 145 |

4 | [adamant][34] | 138 |

5 | [m aroonrk][22] | 134 |

6 | [DNR][35] | 132 |

6 | [D ominater069][36] | 132 |

8 | [Proof_by_QED][37] | 130 |

9 | [BledDest][38] | 129 |

9 | [e rrorgorn][39] | 129 |

 | [View all &rarr;][40] |

&rarr; Find user

&rarr; Recent actions

-

[ICPCNews][41] &rarr; [ICPC Challenge powered by Huawei][42][image: New comment(s)]

-

[chromate00][43] &rarr; [Codeforces Round 1082 (Div. 1, Div. 2) Complete Editorial][44][image: New comment(s)]

-

[jay_jayjay][45] &rarr; [TeamsCode Summer 2026 Virtual Programming Contest][46][image: New comment(s)]

-

[kylychbek][47] &rarr; [IOI 2026 Team Standings][48][image: New comment(s)]

-

[DNR][35] &rarr; [ICPC World-Finals 2026 has been postponed][49][image: New comment(s)]

-

[BitByBit123][50] &rarr; [Suspicious CM yql0991666][51][image: New comment(s)]

-

[megahertz13][52] &rarr; [No author for upcoming Div. 2][53][image: New comment(s)]

-

[greateric][54] &rarr; [Why does my vector MLE?][55][image: New comment(s)]

-

[Errichto][56] &rarr; [Olympiad Classes by Harbour.Space][57][image: New comment(s)]

-

[ayushpandey_23][58] &rarr; [Unable to Submit Problems Due to Anti-Bot Verification on New Account][59][image: New comment(s)]

-

[zeyd1234][60] &rarr; [Is Codeforces Div. 2/3 turning into a pure ad-hoc math speedrun?][61][image: New comment(s)]

-

[Au_Bing][62] &rarr; [Avoid gratist's extension][63][image: New comment(s)]

-

[atcoder_official][64] &rarr; [AtCoder Beginner Contest 471 Announcement][65][image: New comment(s)]

-

[mariza_CY][66] &rarr; [JBOI 2026 teams][67][image: New comment(s)]

-

[mariza_CY][66] &rarr; [Balkan OI 2026 teams][68][image: New comment(s)]

-

[__rose][69] &rarr; [Codeforces Round 1054 (Div. 3) Editorial][70][image: New comment(s)]

-

[atcoder_official][64] &rarr; [AtCoder Regular Contest 227 Announcement][71][image: Text created or updated]

-

[m aroonrk][22] &rarr; [IOI 2026 Problem Discussion][72][image: New comment(s)]

-

[GomerDoGo][73] &rarr; [How to stop losing good blogs][74][image: New comment(s)]

-

[Top12][75] &rarr; [Rollback When?][76][image: Text created or updated]

-

[bihariforces][77] &rarr; [Maximize Subarray Length to Mode Frequency Ratio][78][image: New comment(s)]

-

[codersaky77][79] &rarr; [Game Theory Q1][80][image: New comment(s)]

-

[i_pranavmehta][81] &rarr; [ACD Ladders [A code daily ladders]][82][image: New comment(s)][image: Necropost]

-

[PavelKunyavskiy][83] &rarr; [IOI archive][84][image: New comment(s)][image: Necropost]

-

[SheTheRay][85] &rarr; [Algo][86][image: Text created or updated]

 | [Detailed &rarr;][87] |

- [adamant][34]
- [Blog][88]
- [Teams][89]
- [Submissions][90]
- [Groups][91]
- [Contests][92]
- [Problemsetting][93]

### [adamant's blog][88]

[Dirichlet convolution. Part 1: Fast prefix sum computations][94]

By [adamant][34], [history][95], 3 years ago, [image: In English]

Hi everyone!

Suppose that you need to compute some sum of a number-theoretic function that has something to do with divisors:

$$$\begin{gather} \sum\limits_{k=1}^n \varphi(k) = ? \\ \sum\limits_{k=1}^n \sum\limits_{d|k} d^2 = ?? \\ \sum\limits_{x=1}^n \sum\limits_{y=1}^x \gcd(x, y) = ?!? \end{gather}$$$

As it turns out, such and many similar sums can be computed with Dirichlet convolution in $$$O(n^{2/3})$$$, and in this article we will learn how.

Let $$$f(n)$$$ and $$$g(n)$$$ be two [arithmetic functions][96]. Let $$$F(n)$$$ and $$$G(n)$$$ be their prefix sums, that is

$$$\begin{matrix} F(n) = \sum\limits_{i=1}^n f(i), & G(n) = \sum\limits_{j=1}^n g(j). \end{matrix}$$$

We need to compute a prefix sum of the [Dirichlet convolution][97] $$$(f * g)(n)$$$. In this article, we will consider some general methods, and show how to do so in $$$O(n^{2/3})$$$ if we can compute prefix sums of $$$F(n)$$$ and $$$G(n)$$$ in all possible values of $$$\lfloor n/k \rfloor$$$ in this complexity.

- **Part 1: Fast prefix sum computation**
- **[Part 2: Dirichlet series and prime counting][98]**

[e cnerwala][99] previously [mentioned][100] that it is possible, but did not go into much detail. There is also a [blog][101] by [Nisiyama_Suzune][102], which covers prefix sums of Dirichlet inverses in $$$O(n^{2/3})$$$.

---

### Dirichlet convolution

Recall that the Dirichlet convolution of arithmetic functions $$$f(n)$$$ and $$$g(n)$$$ is defined as

$$$ \boxed{(f*g)(n) = \sum\limits_{d|n} f(d) g\left(\frac{n}{d}\right) = \sum\limits_{ij=n} f(i) g(j)} $$$

Dirichlet convolution is often of interest in the context of [multiplicative functions][103] (i.e., functions such that $$$f(a) f(b) = f(ab)$$$ for $$$\gcd(a,b)=1$$$), as the result can be proven to also be a multiplicative function. Moreover, quite often functions of interest can be expressed as a Dirichlet convolution. For example, the [divisor function][104]

$$$ \sigma_a(n) = \sum\limits_{d|n} d^a $$$

can be represented as a Dirichlet convolution of the constant function $$$f(n)=1$$$ and the power function $$$g(n)=n^a$$$. There are also other similar identities, for example, for the [Euler's totient function][105] $$$\varphi(n)$$$, one can notice that

$$$ \sum\limits_{d|n} \varphi(d) = n. $$$

This is due to the fact that $$$\varphi\left(\frac{n}{d}\right)$$$ is the number of integers $$$x$$$ such that $$$\gcd(x, \frac{n}{d})=1$$$, or, equivalently, $$$\gcd(x, n) = d$$$. This implies that $$$h(n)=n$$$ can be represented as the Dirichlet convolution of $$$f(n) = 1$$$ and $$$\varphi(n)$$$.

#### Hyperbola method

For now assume that we can compute any of $$$f$$$, $$$g$$$, $$$F$$$, $$$G$$$ in $$$O(1)$$$. We can rewrite the prefix sum of the Dirichlet convolution as

$$$ \sum\limits_{t \leq n} (f*g)(t) = \sum\limits_{t \leq n} \sum\limits_{d|t} f(d) g\left(\frac{t}{d}\right) = \sum\limits_{ij \leq n} f(i) g(j). $$$

In the expression above, at least one of $$$i$$$ and $$$j$$$ must be less than $$$\sqrt n$$$. This allows us to rewrite the expression as

$$$\begin{align} \sum\limits_{ij \leq n} f(i) g(j) &= \sum\limits_{i=1}^{\lfloor \sqrt n \rfloor} f(i) \sum\limits_{j=1}^{\lfloor n/i \rfloor} g(j) + \sum\limits_{j=1}^{\lfloor \sqrt n \rfloor} g(j) \sum\limits_{i=1}^{\lfloor n/j \rfloor} f(i) - \sum\limits_{i=1}^{\lfloor \sqrt n \rfloor} f(i) \sum\limits_{j=1}^{\lfloor \sqrt n \rfloor} g(j) \\&= \boxed{ \color{blue}{\sum\limits_{i=1}^{\lfloor \sqrt n\rfloor} f(i) G(\lfloor n/i \rfloor)} + \color{red}{ \sum\limits_{j=1}^{\lfloor \sqrt n\rfloor} g(j) F(\lfloor n/j \rfloor)} - \color{green}{F(\lfloor \sqrt n \rfloor)G(\lfloor \sqrt n \rfloor)} } \end{align}$$$

Thus, in this situation we can find a prefix sum of the Dirichlet convolution in $$$O(\sqrt n)$$$.

*Summation blocks in $$$ij \leq 15$$$
Points in the green block are double-counted and should be subtracted*

The representation of the prefix summation, as written above, is commonly known as the [Dirichlet hyperbola method][106]. Graphically, such summation splits lattice points below the $$$ij=n$$$ hyperbola into three parts (see the picture above). Besides exact computations, this method can also be used to get asymptotic estimations for summations like the one above.

**Exercise 1**: Solve **[Project Euler — #401 Sum of Squares of Divisors][107]**: Compute the prefix sum of $$$\sigma_2(n) = \sum\limits_{d|n} d^2$$$ up to $$$n = 10^{15}$$$.

#### Choosing a better splitting point

Now, what if computing $$$F(i)$$$ and $$$G(j)$$$ requires vastly unbalanced amount of effort?

**Example**: Let's say that we want to compute to compute

$$$ h(n) = \sum\limits_{a | n} \sum\limits_{b | a} b^2, $$$

the sum of squares of divisors of all divisors of $$$n$$$. It can be represented as a Dirichlet convolution of $$$f(n)=1$$$ and $$$g(n) = \sigma_2(n)$$$. For the first one, prefix sums can be computed in $$$O(1)$$$, and for the second one they can be computed in $$$O(\sqrt n)$$$, see excercise 1.

---

In this case, we can bound the sums by a point $$$(k,l)$$$ on the [rectilinear convex hull][108] of points under the hyperbola $$$kl=n$$$:

$$$ \boxed{\sum\limits_{ij \leq n} f(i) g(j) = \color{blue}{\sum\limits_{i=1}^{k} f(i) G(\lfloor n/i \rfloor)} + \color{red}{\sum\limits_{j=1}^{l} g(j) F(\lfloor n/j \rfloor)} - \color{green}{F(k)G(l)} } $$$

See the picture below for a graphical representation.

*For $$$n=15$$$, we can choose $$$k=2$$$ and $$$l=5$$$ instead of $$$k=l=3$$$*

Let's now assume that we can compute $$$F(n)$$$ in $$$n^\alpha$$$ and $$$G(n)$$$ in $$$n^\beta$$$ for $$$0 \leq \alpha, \beta \lt 1$$$. What is the optimal splitting pair $$$(k, l)$$$?

Note that for $$$(k, l)$$$ to be on the rectilinear convex hull of points below $$$kl=n$$$, it is necessary and sufficient to satisfy $$$kl \leq n$$$ and $$$(k+1)(l+1) \gt n$$$, so we may essentially assume that $$$kl \sim n$$$. What is the time complexity required to compute the full sum? It is

$$$ \sum\limits_{i=1}^k O\left(\frac{n^\beta}{i^\beta}\right) + \sum\limits_{j=1}^l O\left(\frac{n^\alpha}{j^\alpha}\right) = O\left(\frac{n^\beta}{k^{\beta-1}} + \frac{n^\alpha}{l^{\alpha-1}}\right) $$$

To minimize the total complexity, we should make the two summands equal. Substituting $$$l \sim n/k$$$, we get

$$$ n^{\beta} = n k^{\alpha + \beta - 2} \implies \boxed{k = n^{\frac{1-\beta}{2-\alpha-\beta}}} $$$

In particular, for $$$\alpha=0$$$ and $$$\beta=1/2$$$ we get $$$k=n^{1/3}$$$ and $$$l=n^{2/3}$$$, making for the total complexity $$$O(n^{2/3})$$$.

#### Adding precomputation

Okay now, but what if $$$\alpha$$$ and $$$\beta$$$ are roughly the same, and also reasonably huge? For example $$$\alpha = \beta = 1/2$$$ or even $$$\alpha = \beta = 2/3$$$.

Due to symmetry, it's still optimal to split in $$$k=l=\lfloor \sqrt n \rfloor$$$, so we can't make it better by choosing a better splitting point. What we can do, however, is to precompute prefix sums of $$$f(n)$$$ and $$$g(n)$$$ up to some point $$$\sqrt n \leq t \lt n$$$.

It's typically possible to do so with linear sieve (see [here][109] for details) in $$$O(t)$$$, after which the complexity for the full computation becomes

$$$ O(t) + \sum\limits_{i=1}^{n/t} O(\frac{n^\alpha}{i^\alpha}) + O(\sqrt n) = O\left(t + \frac{n^\alpha}{n^{\alpha-1}/t^{\alpha-1}} + \sqrt n\right) = O\left(t + nt^{\alpha-1} + \sqrt n\right). $$$

Optimizing for $$$t$$$ makes first $$$2$$$ summands equal, thus $$$t=n^{1/(2-\alpha)}$$$. This leads to $$$O(n^{2/3})$$$ for $$$\alpha=1/2$$$ or $$$O(n^{3/4})$$$ for $$$\alpha=2/3$$$.

#### Adding even more precomputation

The result above is still not quite satisfactory. We see that $$$n^{2/3}$$$ is a kind of magical bound, to which a lot of things reduce. Given that, it would be very nice to stick to it, that is to somehow guarantee that if we can compute prefix sums of $$$f(n)$$$ and $$$g(n)$$$ in $$$O(n^{2/3})$$$, then we also can compute prefix sums of $$$(f*g)(n)$$$ in $$$O(n^{2/3})$$$. Turns out that it is possible to do! We just need a bit stronger guarantees.

**Claim**: Let $$$f(n)$$$ and $$$g(n)$$$ be such that $$$F\left(\lfloor n/k\rfloor\right)$$$ and $$$G\left(\lfloor n/k\rfloor\right)$$$ are known for all possible arguments. Then we can compute prefix sum $$$H(n)$$$ of $$$h(n) = (f * g)(n)$$$ in $$$O(\sqrt n)$$$. Moreover, we can find $$$H(\lfloor n/k \rfloor)$$$ for all possible arguments in $$$O(n^{2/3})$$$.

**Note 1**: There might only be at most $$$2 \sqrt n$$$ distinct values of $$$\lfloor n/k \rfloor$$$, because either $$$k$$$ or $$$\lfloor n/k \rfloor$$$ must be smaller than $$$\sqrt n$$$.

**Note 2**: The result above allows us to repeatedly compute Dirichlet convolutions without blowing the complexity, as it will pin to $$$O(n^{2/3})$$$.

**Proof**: The result about $$$H(n)$$$ immediately follows from the hyperbola method.

Additionally, using the identities $$$\small \left\lfloor \frac{\lfloor n/a \rfloor}{b} \right\rfloor = \lfloor \frac{n}{ab}\rfloor$$$ and $$$\small \left\lfloor\sqrt{\left\lfloor \frac{n}{k} \right\rfloor} \right\rfloor = \left\lfloor\sqrt{\frac{n}{k}} \right\rfloor$$$, we can compute $$$H(\lfloor n/k \rfloor)$$$ with the hyperbola method as

$$$\boxed{ H(\lfloor n/k \rfloor) = \sum\limits_{i=1}^{\left\lfloor \sqrt{n/k}\right\rfloor} f(i) G\left(\left\lfloor \frac{n}{ki} \right\rfloor\right) + \sum\limits_{j=1}^{\left\lfloor \sqrt{n/k}\right\rfloor} g(j) F\left(\left\lfloor \frac{n}{kj} \right\rfloor\right) - F\left(\left\lfloor \sqrt{\frac{n}{k}}\right\rfloor\right)G\left(\left\lfloor \sqrt{\frac{n}{k}} \right\rfloor\right) }$$$

in $$$\small O\left(\sqrt{\frac{n}{k}}\right)$$$, as any individual summand is computed in $$$O(1)$$$ after pre-computation.

Note that $$$\lfloor \sqrt{t} \rfloor$$$ always lies in the corner of the rectilinear convex hull of points below $$$kl=t$$$. There are two cases two consider here:

1. The corner is "concave", that is $$$\lfloor \sqrt t \rfloor(\lfloor \sqrt t \rfloor+1) \leq t$$$. It means that $$$\lfloor \sqrt t \rfloor = \lfloor t/l \rfloor$$$ for $$$\small \lfloor \sqrt t \rfloor \lt l \leq \left\lfloor \frac{t}{\lfloor \sqrt t \rfloor} \right\rfloor$$$.
2. The corner is "convex", that is $$$\lfloor \sqrt t \rfloor(\lfloor \sqrt t \rfloor+1) \gt t$$$. It means that $$$\lfloor \sqrt t \rfloor = \lfloor t/l \rfloor$$$ for $$$\small \left\lfloor \frac{t}{\lfloor \sqrt t \rfloor+1} \right\rfloor \lt l \leq \lfloor \sqrt t \rfloor$$$.

**Note 3**: Graphically, on the picture above the corner $$$(3, 3)$$$ is "concave", and the corner $$$(3, 5)$$$ is "convex".

In either case, it means that $$$\lfloor \sqrt t \rfloor$$$ can always be represented as $$$\lfloor t/l \rfloor$$$ for some $$$l$$$. Applying this result to $$$\lfloor n/k \rfloor$$$ instead of $$$t$$$, we deduce that $$$\small \left\lfloor \sqrt{\frac{n}{k}} \right\rfloor$$$ can be represented as $$$\small \left\lfloor \frac{\lfloor n/k \rfloor}{l} \right\rfloor = \lfloor \frac{n}{kl}\rfloor$$$, thus the values of $$$F(n)$$$ and $$$G(n)$$$ in $$$\small \left\lfloor \sqrt{\frac{n}{k}} \right\rfloor$$$ must also be known, and do not contribute any extra burden to the computation time.

Thus, the overall complexity is the sum of $$$\small \sqrt{\frac{n}{k}}$$$ over all values of $$$\lfloor n/k\rfloor$$$, in which we compute it with the hyperbola method. Since we can pre-compute these values up to $$$n/k \sim n^{2/3}$$$ in $$$O(n^{2/3})$$$ with the linear sieve, we're only interested in values of $$$k$$$ up to $$$n^{1/3}$$$, which takes

$$$ \sum\limits_{k=1}^{\sqrt[3]{n}} \sqrt{\frac{n}{k}} \sim \int\limits_0^{\sqrt[3]{n}} \sqrt{\frac{n}{x}} dx = 2n^{2/3}, $$$

proving the overall complexity of $$$O(n^{2/3})$$$.

### Dirichlet inverse

**Example**: **[Library Judge — Sum of Totient Function][110]**. Find the sum of $$$\varphi(n)$$$ up to $$$n \leq 10^{10}$$$.

**Solution**: Explained below, see [submission][111] for implementation details.

The result above provides us with an efficient method of computing the prefix sums of the convolution of two sequences. However, it often happens that we can compute the prefix sums of the convolution $$$(f * g)(n)$$$, and of one of the functions $$$f(n)$$$, but not of the other.

For example, consider the prefix sums of the Euler's totient function $$$\varphi(n)$$$. We already know that the Dirichlet convolution of $$$\varphi(n)$$$ and $$$f(n) = 1$$$ is $$$h(n) = n$$$. We can easily compute prefix sums of $$$f(n)$$$ and $$$h(n)$$$. But computing them for $$$\varphi(n)$$$ is much more difficult.

What we can do here is consider the Dirichlet inverse of $$$f(n)=1$$$. Dirichlet inverse of a function $$$f(n)$$$ is the function $$$f^{-1}(n)$$$ such that $$$(f * f^{-1})(n)$$$ equates to the Dirichlet neutral function, which is defined as $$$1$$$ for $$$n=1$$$ and to $$$0$$$ otherwise. As follows from its name, Dirichlet convolution of any function with the Dirichlet neutral yields the initial function.

From [Möbius inversion formula][112], the inverse for it is known to be $$$\mu(n)$$$, the Möbius function, hence we can represent $$$\varphi(n)$$$ as

$$$ \varphi(n) = \sum\limits_{d|n} d \mu\left(\frac{n}{d}\right), $$$

that is as the Dirichlet convolution of $$$f(n)=n$$$ and $$$\mu(n)$$$. This reduces the task of finding prefix sums for $$$\varphi(n)$$$ to finding prefix sums of the Dirichlet convolution of $$$f(n) = n$$$ and $$$\mu(n)$$$. But how do we find the prefix sums of $$$\mu(n)$$$ (also known as the [Mertens function][113])?

**Claim**: Let $$$f(n)$$$ be such that we can find values of $$$F\left(\left\lfloor n/k\right\rfloor\right)$$$ for all possible arguments in $$$O(n^{2/3})$$$. Then we can also find the prefix sums for all possible arguments of the Dirichlet inverse $$$f^{-1}(n)$$$ in $$$O(n^{2/3})$$$.

**Proof**: Let $$$F^{-1}(n)$$$ be the prefix sum of $$$f^{-1}(n)$$$ up to $$$n$$$. The hyperbola formula allows us to compute $$$F^{-1}(n)$$$ in $$$O(\sqrt n)$$$, granted that we already know all values of $$$ F\left(\left\lfloor n/k\right\rfloor\right)$$$ and $$$ F^{-1}\left(\left\lfloor n/k\right\rfloor\right)$$$:

$$$ F^{-1}(n) = \frac{1}{f(1)} \left[1 + F(\lfloor \sqrt n \rfloor) F^{-1}(\lfloor \sqrt n \rfloor) - \sum\limits_{i=1}^{\lfloor \sqrt n \rfloor} f^{-1}(i) F(\lfloor n / i\rfloor) - \sum\limits_{i=2}^{\lfloor \sqrt n \rfloor} f(i) F^{-1}(\lfloor n / i\rfloor)\right] $$$

**Note**: For non-zero multiplicative functions, $$$f(1)=1$$$.

With this in mind, we can compute all values of $$$F^{-1}(n)$$$ up to $$$O(n^{2/3})$$$ with linear sieve, and then compute $$$ F^{-1}\left(\left\lfloor n/k\right\rfloor\right)$$$ one by one in the increasing order of arguments.

Each value is computed in $$$\small O\left(\sqrt{\frac{n}{k}}\right)$$$ starting with $$$k \approx \sqrt[3]{n}$$$ and going up to $$$k=1$$$. This gives the $$$O(n^{2/3})$$$ algorithm to find the Dirichlet inverse, and its analysis is essentially the same as with the algorithm for the Dirichlet convolution.

As a proof of concept, I have implemented the code to compute the sums of $$$\mu(n)$$$ and $$$\varphi(n)$$$ up to a given bound:

**code**

```
from sympy import sieve
import itertools
import math

n = 10**12
t = int(n**(2/3))

def floorrange(n):
    L = 1
    ans = []
    while L <= n:
        ans.append(L)
        L = n // (n // L) + 1
    return list(reversed(ans))

mu = [0] + list(sieve.mobiusrange(1, t))
mu_p = list(itertools.accumulate(mu))
M = dict()

M[0] = 0
for k in floorrange(n):
    nk = n//k
    if nk < len(mu_p):
        M[nk] = mu_p[nk]
    else:
        up = int(math.sqrt(nk))
        M[nk] = 1 + M[up] * up \
            - sum(M[nk // i] for i in range(2, up+1)) \
            - sum(mu[i] * (nk // i) for i in range(1, up+1))

phi = [0] + list(sieve.totientrange(1, t))
phi_p = list(itertools.accumulate(phi))
P = dict()
P[0] = 0

def f(n):
    return n
def sf(n):
    return n*(n+1)//2

for k in floorrange(n):
    nk = n//k
    if nk < len(phi_p):
        P[nk] = phi_p[nk]
    else:
        up = int(math.sqrt(nk))
        P[nk] = - M[up] * sf(up) \
            + sum(M[nk // i] * f(i) for i in range(1, up+1)) \
            + sum(mu[i] * sf(nk // i) for i in range(1, up+1))

print(M[n], P[n])
```

You can use $$$M(10^{12})=62366$$$ and $$$\Phi(10^{12})=303963550927059804025910$$$ to check your implementation.

**Exercise 2**: Solve **[Project Euler — #625 Gcd Sum][114]**: Compute $$$G(n) = \sum\limits_{j=1}^n \sum\limits_{i=1}^j \gcd(i, j)$$$ for $$$n=10^{11}$$$.

**Exercise 3**: Solve **[Project Euler — #351 Hexagonal Orchards][115]**.

### Further reading

- **[[Tutorial] Math note — linear sieve][109]**— how to compute prefix of multiplicative functions up to $$$n$$$ in $$$O(n)$$$ with linear sieve.
- **[[Tutorial] Math note — Möbius inversion][116]**— how to apply Möbius inversion to some number-theoretic problems.
- **[[Tutorial] Math note — Dirichlet convolution][101]**— another entry on Dirichlet convolution inversion in $$$O(n^{2/3})$$$.
- **[Summing Multiplicative Functions (Pt. 1)][117]**— more on computing prefix sums of multiplicative functions.

**UPD**: Turns out, it is also possible to compute prefix sums in $$$\lfloor n/k \rfloor$$$ for Dirichlet convolution and Dirichlet inverse in $$$O(n^{2/3})$$$ while only using $$$O(\sqrt n)$$$ memory, and without linear sieving:

**code**

```
import math
import itertools

# Returns a list of tuples (L, R, t)
# such that n//k = t <=> t in [L, R]
def floorrange(n):
    L = 1
    ans = []
    while L <= n:
        R = n // (n // L)
        ans.append((L, R, n//L))
        L = R + 1
    ans.append((n+1, n+1, 0))
    return list(reversed(ans))

def exec_on_blocks(func, n):
    rt_n = math.isqrt(n)
    floors = floorrange(n)
    num_ranges = len(floors)-1

    def to_ord(k):
        return k if k <= rt_n else len(floors) - n // k

    func([1, 1], [1, 1], [1, num_ranges])

    for k in range(2, len(floors)):
        z = len(floors) - k

        for x in itertools.count(2):
            y_lo_ord = max(to_ord(x), to_ord(z)) + 1
            y_hi_ord = to_ord(n//(x*z))
            if y_hi_ord < y_lo_ord:
                break
            func([x, x], [y_lo_ord, y_hi_ord], [k, k])
            func([y_lo_ord, y_hi_ord], [x, x], [k, k])

        func([1, 1], [k, k], [k, num_ranges])
        func([k, k], [1, 1], [k, num_ranges])

        x = k
        for y in range(2, k):
            z_lo_ord = to_ord(x*y)
            z_hi_ord = to_ord(n//x)
            if z_hi_ord < z_lo_ord:
                break
            func([x, x], [y, y], [z_lo_ord, z_hi_ord])
            func([y, y], [x, x], [z_lo_ord, z_hi_ord])

        z_lo_ord = to_ord(x**2)
        func([x, x], [x, x], [z_lo_ord, num_ranges])

def Dirichlet_mul(F, G, n):
    H = [0] * (len(F)+1)
    def propagate(x, y, z):
        t = (F[x[1]]-F[x[0]-1])*(G[y[1]]-G[y[0]-1])
        H[z[0]] += t
        H[z[1]+1] -= t
    exec_on_blocks(propagate, n)
    return list(itertools.accumulate(H))[:-1]

def Dirichlet_div(H, G, n):
    H = H.copy() + [0]
    H = [0] + [H[i]-H[i-1] for i in range(1, len(H))]
    F = [None] * len(G)
    F[0] = 0
    def propagate(x, y, z):
        if F[x[1]] is None:
            F[x[1]] = H[z[0]] // (G[y[1]] - G[y[0]-1]) + F[x[0]-1]

        t = (F[x[1]] - F[x[0]-1]) * (G[y[1]] - G[y[0]-1])
        H[z[0]] -= t
        H[z[1]+1] += t

    exec_on_blocks(propagate, n)
    return F
```

See the [comment below][118] for details.

[image: Tags] [tutorial][119], [dirichlet convolution][120]

- [image: Vote: I like it]
- +285
- [image: Vote: I do not like it]

- [image: Author] [34] [adamant][34]
- [image: Publication date] 3 years ago
- [image: Comments] [121] [20][121]

[image: Comments] Comments (20)

Write comment?

&raquo;

[ConnectedGraph][122]

 |

3 years ago, show (+ 1) #

 |

&raquo;

[122]

[ConnectedGraph][122]

 |

3 years ago, hide [#][123] |

&larr; Rev. 2 &rarr;

[image: Vote: I like it] -22[image: Vote: I do not like it]

Thanks for the blog

Also, please tell me that this is not a topic for under 3000 rated problems, because I really don't want to read all that any time in the future

&rarr; Reply

 |

-

&raquo;

&raquo;

[the_Incharge][124]

 |

3 years ago, show (+ 1) #

 |

&raquo;

&raquo;

[124]

[the_Incharge][124]

 |

3 years ago, hide [#][125] ^ |

[image: Vote: I like it] +93[image: Vote: I do not like it]

the "china" in your bio disagrees with you, look inside you , you already know all that.

&rarr; Reply

 |

  -

&raquo;

&raquo;

&raquo;

[ConnectedGraph][122]

 |

3 years ago, show #

 |

&raquo;

&raquo;

&raquo;

[122]

[ConnectedGraph][122]

 |

3 years ago, hide [#][126] ^ |

[image: Vote: I like it] +1[image: Vote: I do not like it]

LMAO

&rarr; Reply

 |

-

&raquo;

&raquo;

[tfg][127]

 |

3 years ago, show #

 |

&raquo;

&raquo;

[127]

[tfg][127]

 |

3 years ago, hide [#][128] ^ |

[image: Vote: I like it] +69[image: Vote: I do not like it]

"topics" over 3000 rating are 3000 rating just because people don't learn them.

&rarr; Reply

 |

&raquo;

[Psychotic_D][129]

 |

3 years ago, show #

 |

&raquo;

[129]

[Psychotic_D][129]

 |

3 years ago, hide [#][130] |

[image: Vote: I like it] +10[image: Vote: I do not like it]

Is there any CF problem based on this?

&rarr; Reply

 |

&raquo;

[nor][131]

 |

3 years ago, show (+ 1) #

 |

&raquo;

[131]

[nor][131]

 |

3 years ago, hide [#][132] |

[image: Vote: I like it] +65[image: Vote: I do not like it]

Thanks for the nice introductory blog! In my opinion, it could have been much more interesting for people who already know about the topics from the referred blogs if there was a treatment that focused on properties of Dirichlet series to explain the content of the blog.

Formal Dirichlet series over a ring form a ring under the Dirichlet convolution (for instance, when the ring is $$$\mathbb{R}$$$, it's easy to check that it is isomorphic to the ring of all formal power series in countably many variables due to unique factorization) — this is necessary to be able to do all the cool stuff mentioned in [this][100] comment.

Furthermore, Dirichlet series have Fourier-transform-esque properties, in the sense that [Dirichlet series inversion][133] resembles Fourier transforms. It is also interesting to note that L-functions are just Dirichlet series of Dirichlet characters, which are related to group characters used in [Fourier transforms on finite groups][134] — a concise resource on this can be found [here][135]. [This webpage][136] is a great resource on the connections between number theoretical topics like Dirichlet series and Fourier transforms, and anyone who likes FFT should go through some of these papers to truly appreciate the kind of theory that arises at the junction of these two seemingly different fields.

At the risk of going off a tangent, L-functions are also one of the most important objects of study for modern number theory, being closely related to elliptic curves and the Riemann hypothesis, to name a couple of famous applications — there is a lot of computational number theory that revolves around L-functions as primitives.

Here are a few resources for anyone who's interested:

- Wikipedia (with references) — probably the best resources for learning higher math
- [The Arithmetic Fourier Transform][137] — an alternative to FFT
- [Proof of Dirichlet's theorem on arithmetic progressions using L-functions][138]
- [Introduction to L-functions for graduate-level mathematicians][139]
- [Applications of L-functions to elliptic curves][140]

&rarr; Reply

 |

-

&raquo;

&raquo;

[adamant][34]

 |

3 years ago, show #

 |

&raquo;

&raquo;

[34]

[adamant][34]

 |

3 years ago, hide [#][141] ^ |

[image: Vote: I like it] +3[image: Vote: I do not like it]

Hey, thanks, I was actually planning to write about Dirichlet series initially, but I couldn't properly connect their nice theoretic framework with practical applications in programming yet. I plan to write another article about them as soon as I have enough understanding to cover this gap :)

&rarr; Reply

 |

&raquo;

[e cnerwala][99]

 |

3 years ago, show (+ 1) #

 |

&raquo;

[99]

[e cnerwala][99]

 |

3 years ago, hide [#][142] |

&larr; Rev. 2 &rarr;

[image: Vote: I like it] +40[image: Vote: I do not like it]

Actually, it's possible to do all of these operations in $$$O(n^{2/3})$$$ time but with only $$$O(n^{1/2})$$$ memory, without relying on the functions being multiplicative! The main idea is that we don't actually care about all values of the linear-time sieve (the memory-intensive part, which also relies on the function being multiplicative), we only care about them bucketed into distinct values of $$$\lfloor N/k \rfloor$$$.

Directly cutting out the sieve is a little tricky, so here's an alternative viewpoint which makes the algorithm a bit simpler. Consider trying to compute $$$H(\lfloor n / z \rfloor)$$$ for all $$$z$$$, where $$$h = f * g$$$. Then, note that $$$f(x) g(y)$$$ contributes to $$$H(\lfloor n / z \rfloor)$$$ iff $$$xyz \le n$$$. Now, we claim we can partition the space $$$xyz \le n$$$ into $$$O(n^{2/3})$$$ rectangular prisms (3D rectangles). (This is analogous to how we can partition $$$xy \le n$$$ into $$$O(n^{1/2})$$$ rectangles.)

The construction is pretty simple. WLOG, assume $$$x \le y \le z$$$ (this introduces a factor of $$$6$$$). Then, fix any $$$x \le y$$$ with $$$x y^2 \le n$$$. There are at most $$$O(n^{2/3})$$$ such pairs: for each $$$x \le n^{1/3}$$$, there are $$$\lfloor \sqrt{n/x} \rfloor$$$ pairs, and $$$\sum_{x=1}^{n^{1/3}} \lfloor \sqrt{n/x} \rfloor = O(n^{2/3})$$$ by integration. Then, simply take the rectangle $$$[x, x] \times [y, y] \times [y, \lfloor n / (xy) \rfloor]$$$.

Now that we've partitioned the space of $$$xyz \le n$$$ into $$$O(n^{2/3})$$$ rectangles (in fact, each rectangle is a $$$1 \times 1 \times k$$$ line in some dimension), we can easily perform the desired sum. For a rectangle $$$[x_1, x_2] \times [y_1, y_2] \times [z_1, z_2]$$$, we can use prefix sums to compute $$$\sum_{x=x_1}^{x_2} \sum_{y=y_1}^{y_2} f(x) g(y) = (F(x_2) - F(x_1 - 1))(G(y_2) - G(y_1 - 1))$$$, and we can implicitly add it to the interval $$$H(\lfloor n / z_2 \rfloor) \ldots H(\lfloor n / z_2 \rfloor)$$$ by storing $$$H$$$ in terms of its finite differences. (Note that all coordinates of the rectangles are of the form $$$\lfloor n / k \rfloor$$$ since they're either smaller than $$$\sqrt{n}$$$ or they're clearly of that form, so we only need the inputs of the form $$$F(\lfloor n / k \rfloor)$$$ and $$$G(\lfloor n / k \rfloor)$$$.) Adding the finite differences up in the end gives us the desired $$$H$$$.

Additionally, note that we're really just performing schoolbook long multiplication, but compressing some intervals when possible. We can also use this to perform schoolbook long division (e.g. Dirichlet inverse). The setup is that, we know $$$F$$$ and $$$H$$$, and we want to compute $$$G$$$ so that $$$F * G = H$$$. Let's initialize $$$G$$$ to be "unknown", and try to compute $$$F * G = H'$$$. Since the rectangles are easy to implicitly generate, we can compute $$$H'$$$ in "online order", meaning that we find $$$H'(k)$$$ before using $$$F(l)$$$ or $$$G(l)$$$ for $$$l \gt k$$$ (this is easy to work out, since the rectangles are just formed from fixing 2 coordinates). Then, at each step, we should just set $$$G(k)$$$ to make $$$H'(k) = H(k)$$$ (we can find the right value since we know it contributes exactly $$$F(1) G(k)$$$). Continuing to multiply gives us the full inverse we want. This also lets us compute functions like $$$\sqrt{F}$$$ and similar.

(Sorry, I meant to write a longer blog post describing all these algorithms, but haven't found the time. You can find my code for this stuff at [https://github.com/ecnerwala/cp-book/blob/master/src/dirichlet_series.hpp][143])

&rarr; Reply

 |

-

&raquo;

&raquo;

[adamant][34]

 |

3 years ago, show #

 |

&raquo;

&raquo;

[34]

[adamant][34]

 |

3 years ago, hide [#][144] ^ |

[image: Vote: I like it] +3[image: Vote: I do not like it]

Hey, that's very cool! In theory, at least. I'm trying to implement it and it doesn't seem very pleasant so far T_T

&rarr; Reply

 |

-

&raquo;

&raquo;

[h os.lyric][145]

 |

3 years ago, show (+ 1) #

 |

&raquo;

&raquo;

[145]

[h os.lyric][145]

 |

3 years ago, hide [#][146] ^ |

[image: Vote: I like it] +51[image: Vote: I do not like it]

As an additional note, this multiplication method can be modified to perform well in the case where $$$f$$$ and/or $$$g$$$ have some sparsity; skip 3D rectangles concerning $$$f(x) = 0$$$ or $$$g(y) = 0$$$. When $$$f$$$ and $$$g$$$ take values only on (say) $$$n^{1/6}$$$-rough numbers, I think it becomes $$$O(n^{2/3} \log(n)^{-1})$$$ time. When $$$f$$$ takes values only on powerful numbers, we can partition the space into $$$O(n^{1/2} \log(n))$$$ 3D rectangles (as far as I know this is less known than "powerful number sieve").

(Sorry, I meant to write a longer blog post describing all these algorithms, but have been too lazy to implement the division. Thanks for explaining how to think!)

&rarr; Reply

 |

  -

&raquo;

&raquo;

&raquo;

[adamant][34]

 |

3 years ago, show (+ 1) #

 |

&raquo;

&raquo;

&raquo;

[34]

[adamant][34]

 |

3 years ago, hide [#][147] ^ |

&larr; Rev. 6 &rarr;

[image: Vote: I like it] 0[image: Vote: I do not like it]

Hi, thanks for pointing that out! Could you please share more details on where the bound of $$$O(\sqrt n \log n)$$$ comes from? Also what would be the simplest way to construct such set of rectangles?

&rarr; Reply

 |

    -

&raquo;

&raquo;

&raquo;

&raquo;

[h os.lyric][145]

 |

3 years ago, show #

 |

&raquo;

&raquo;

&raquo;

&raquo;

[145]

[h os.lyric][145]

 |

3 years ago, hide [#][148] ^ |

[image: Vote: I like it] +10[image: Vote: I do not like it]

My idea is to use only the rectangles of the form $$$[x,x] \times [y,y] \times [y, N/(xy)]$$$ and $$$[x,x] \times [z,N/(xz)] \times [z,z]$$$, where we can assume that $$$x$$$ is powerful. We want to count $$$(x, y)$$$ such that $$$x y^2 \le N$$$ and $$$x$$$ is powerful. Using the representation $$$x = a^2 b^3$$$ ($$$b$$$: square-free), we have $$$\sum_{a\le N^{1/2}} \sum_b \mu(b)^2 (N/(a^2b^3))^{1/2} \sim N^{1/2} \log(N^{1/2}) \frac{\zeta(3/2)}{\zeta(3)}$$$.

&rarr; Reply

 |

-

&raquo;

&raquo;

[e cnerwala][99]

 |

3 years ago, show #

 |

&raquo;

&raquo;

[99]

[e cnerwala][99]

 |

3 years ago, hide [#][149] ^ |

[image: Vote: I like it] +23[image: Vote: I do not like it]

Another quick note: this construction gives the minimum number of rectangles. For any $$$x \le y \le z = \lfloor n / x / y \rfloor$$$, the point $$$(x, y, z)$$$ is "maximal" for $$$xyz \le n$$$, in that $$$n \lt xy(z+1) \le x(y+1) z \le (x+1) y z$$$. No two maximal points can be in the same rectangle, and each of our rectangles contains a maximal point, so we have an optimal partition.

&rarr; Reply

 |

-

&raquo;

&raquo;

[adamant][34]

 |

3 years ago, show #

 |

&raquo;

&raquo;

[34]

[adamant][34]

 |

3 years ago, hide [#][150] ^ |

&larr; Rev. 2 &rarr;

[image: Vote: I like it] 0[image: Vote: I do not like it]

After some further discussions with [e cnerwala][99], and a lot of help from him, we also have a self-contained Python implementation for multiplication and division in this algorithm:

**code**

```
import math
import itertools

# Returns a list of tuples (L, R, t)
# such that n//k = t <=> t in [L, R]
def floorrange(n):
    L = 1
    ans = []
    while L <= n:
        R = n // (n // L)
        ans.append((L, R, n//L))
        L = R + 1
    ans.append((n+1, n+1, 0))
    return list(reversed(ans))

def exec_on_blocks(func, n):
    rt_n = math.isqrt(n)
    floors = floorrange(n)
    num_ranges = len(floors)-1

    def to_ord(k):
        return k if k <= rt_n else len(floors) - n // k

    func([1, 1], [1, 1], [1, num_ranges])

    for k in range(2, len(floors)):
        z = len(floors) - k

        for x in itertools.count(2):
            y_lo_ord = max(to_ord(x), to_ord(z)) + 1
            y_hi_ord = to_ord(n//(x*z))
            if y_hi_ord < y_lo_ord:
                break
            func([x, x], [y_lo_ord, y_hi_ord], [k, k])
            func([y_lo_ord, y_hi_ord], [x, x], [k, k])

        func([1, 1], [k, k], [k, num_ranges])
        func([k, k], [1, 1], [k, num_ranges])

        x = k
        for y in range(2, k):
            z_lo_ord = to_ord(x*y)
            z_hi_ord = to_ord(n//x)
            if z_hi_ord < z_lo_ord:
                break
            func([x, x], [y, y], [z_lo_ord, z_hi_ord])
            func([y, y], [x, x], [z_lo_ord, z_hi_ord])

        z_lo_ord = to_ord(x**2)
        func([x, x], [x, x], [z_lo_ord, num_ranges])

def Dirichlet_mul(F, G, n):
    H = [0] * (len(F)+1)
    def propagate(x, y, z):
        t = (F[x[1]]-F[x[0]-1])*(G[y[1]]-G[y[0]-1])
        H[z[0]] += t
        H[z[1]+1] -= t
    exec_on_blocks(propagate, n)
    return list(itertools.accumulate(H))[:-1]

def Dirichlet_div(H, G, n):
    H = H.copy() + [0]
    H = [0] + [H[i]-H[i-1] for i in range(1, len(H))]
    F = [None] * len(G)
    F[0] = 0
    def propagate(x, y, z):
        if F[x[1]] is None:
            F[x[1]] = H[z[0]] // (G[y[1]] - G[y[0]-1]) + F[x[0]-1]

        t = (F[x[1]] - F[x[0]-1]) * (G[y[1]] - G[y[0]-1])
        H[z[0]] -= t
        H[z[1]+1] += t

    exec_on_blocks(propagate, n)
    return F
```

In the code above, the function `exec_on_blocks(func, n)`enumerates all $$$[x_0, x_1] \times [y_0, y_1] \times [z_0, z_1]$$$ blocks mentioned in his comment and passes them on to its argument function `func`.

This function `func`behaves simply for `Dirichlet_mul(F, G, n)`and `Dirichlet_div(H, G, n)`.

In the first case, it simply adds through finite differences

$$$ H(z_0 \dots z_1) \overset{+}{\leftarrow} [F(x_1) - F(x_0-1)] \cdot [G(y_1) - G(y_0-1)]. $$$

In the second case, it subtracts this value instead. Besides that, if $$$F(x_1)$$$ is unassigned at the moment, it assumes that $$$x_1 = z_0 = k$$$, such that $$$F(x)$$$ for $$$x \lt k$$$ are already known, and all the other blocks with $$$z_0 = k$$$ were already propagated. Therefore, $$$H(z_0)$$$ must become $$$0$$$ after subtraction, from which we can determine $$$F(x_1)$$$ as

$$$ F(x_1) = F(x_0 - 1) + \frac{H(z_0)}{G(y_1) - G(y_0-1)}. $$$

To maintain this, `exec_on_blocks`iterates over $$$k$$$, after which it

  1. Processes the blocks with $$$z_1 = z_2 = k$$$, (blocks that have $$$k$$$ as "output"),
  2. then the block with $$$x_1 = z_0 = k$$$, (during which $$$F(k)$$$ is determined),
  3. then the blocks with $$$x_0 = k$$$ or $$$y_0 = k$$$ (blocks that use $$$k$$$ as "input").

Note: The indices $$$x_i, y_i, z_i$$$ are actually from $$$0$$$ to $$$2 \sqrt n$$$, as they directly index distinct values of $$$\lfloor n/k \rfloor$$$.

&rarr; Reply

 |

-

&raquo;

&raquo;

[e cnerwala][99]

 |

3 years ago, show #

 |

&raquo;

&raquo;

[99]

[e cnerwala][99]

 |

3 years ago, hide [#][151] ^ |

[image: Vote: I like it] +10[image: Vote: I do not like it]

One more quick note: the $$$xyz \le N$$$ construction looks remarkably symmetric, and there's a good reason for this.

Fundamentally, why are we trying to compute all prefix sums $$$H(\lfloor N / z \rfloor)$$$? It's really because we want to be able to answer questions of the form "what is the $$$N$$$th prefix sum of $$$h * q$$$?" for an arbitrary function $$$Q$$$; $$$H$$$ is simply the coefficients for each $$$q(z)$$$. Substituting in $$$h = f * g$$$, we're trying to find the coefficient of each $$$q(z)$$$ in the $$$N$$$th prefix sum of $$$h * q = f * g * q$$$ (which equals $$$\sum_{xyz \le N} f(x) g(y) q(z)$$$).

Said differently, computing prefix sums of $$$h = f*g$$$ is the linear algebraic "transpose" of computing $$$\text{pref}(f*g*q)(N)$$$ with respect to $$$q$$$, so we can perform an algorithm to compute this prefix sum, but keep track of coefficients of $$$q$$$ instead of accumulating them (the more general form of this "transposition principle" is described [here][152]). This is why we should consider the coordinate scheme $$$H(\lfloor N / z \rfloor)$$$: $$$z$$$ is really the coordinate in $$$q$$$, and we're trying to "sum together" over $$$xyz \le N$$$.

&rarr; Reply

 |

&raquo;

[PinkieRabbit][153]

 |

3 years ago, show (+ 1) #

 |

&raquo;

[153]

[PinkieRabbit][153]

 |

3 years ago, hide [#][154] |

&larr; Rev. 16 &rarr;

[image: Vote: I like it] +58[image: Vote: I do not like it]

Last day an incredible breakthrough in this topic has been published by [z houkangyang][155]:

$$$ \text{Calculation of } H(\lfloor n/k \rfloor) \text{ can be done in } \mathcal O (n^{1/2} \operatorname{poly\,log} n) . $$$

**Brief**

The bottleneck for the current methods of Dirichlet convolution is contributing $$$F(x)$$$ and $$$G(y)$$$ to $$$H(n / z)$$$ for those $$$x, y, z \le \sqrt{n}$$$ and $$$x y \le n / z$$$, the remaining parts are studied and can be easily done in $$$\mathcal O (n^{1/2})$$$.

Solution: Take logarithms and use FFT. To deal with the floating points, we round them up to the closest integer. Now we analyze the error terms, a basic observation is, if we multiply the logarithms by $$$B$$$ before rounding up, the length of the FFT is also multiplied by $$$B$$$, but the error terms are divided by $$$B$$$. Surprisingly, the correction can be done in $$$\mathcal O (n / B \cdot \operatorname{poly\,log} n)$$$ (which is not discovered by anyone before) by simply enumerating $$$x$$$ and $$$y$$$ as factors of numbers in a range between $$$n \pm \mathcal O(n / B)$$$, because traditionally we need $$$x y z \le n$$$, in contrast, here an error occurs only when $$$\lvert x y z - n \rvert$$$ is small enough, and this can be bounded using the rate and the error term of $$$\sum_n d_3(n)$$$ ($$$d_k(n)$$$ is the $$$k$$$-fold divisor function), as Wikipedia [says][156] that $$$\sum_{i \le n} d_3(i) = n P_3(\ln n) + \mathcal O(n^{43 / 96 + \varepsilon})$$$ where $$$P_3$$$ is a polynomial of degree $$$2$$$. Balancing by the parameter $$$B$$$ gives the final result.

The algorithm takes $$$\mathcal O (n^{1/2} \operatorname{poly\,log} n)$$$ space, though, and the time constants are big. It’s theoretical meaning is much more greater. It’s very hard to believe that the bound of soft-$$$\mathcal O(n^{2 / 3})$$$ can actually be broken, after so many years of studies by CP experts in China (previous studies aimed to reduce the number of factors of logs in soft-$$$\mathcal O(n^{2 / 3})$$$, the best result might be approaching $$$-2$$$ logs). It’s very interesting that the method is not traditionally pure combinatorial, but contains a careful analysis in floating precisions, and uses a result from analytic number theory.

Check his [blog][157] (in Chinese) for details.

---

We later found [https://arxiv.org/abs/2212.09857][158]*Computing $$$\pi(N)$$$: An elementary approach in $$$\tilde{O}(\sqrt{N})$$$ time*(2022) by Dean Hirsch, Ido Kessler, and Uri Mendlovic. The paper uses a similar method and is one year prior to Zhou’s, check [https://x.com/negiizhao/status/1768007989984899152][159] and [https://github.com/yosupo06/library-checker-problems/issues/1118][160] for a further discussion.

&rarr; Reply

 |

-

&raquo;

&raquo;

[adamant][34]

 |

3 years ago, show #

 |

&raquo;

&raquo;

[34]

[adamant][34]

 |

3 years ago, hide [#][161] ^ |

&larr; Rev. 2 &rarr;

[image: Vote: I like it] +20[image: Vote: I do not like it]

Wow, that's very impressive! [z houkangyang][155] orz!

The story on how it's affected double precision also reminds me of the current best $$$\tilde O(\sqrt n)$$$ algorithm to compute the partition function $$$p(n)$$$ in a specific point $$$n$$$. Essentially, even if we just want to compute it modulo some number $$$m$$$, the best thing we can do is to evaluate [Rademacher formula][162] with enough precision to get the exact value as an integer, and then compute it modulo $$$m$$$.

I'm not sure I understand all of the details of the algorithm that you describe, but maybe I'll take a closer look later...

P.S. I wish these results were better exposed in English speaking resources T_T

&rarr; Reply

 |

-

&raquo;

&raquo;

[e cnerwala][99]

 |

3 years ago, show #

 |

&raquo;

&raquo;

[99]

[e cnerwala][99]

 |

3 years ago, hide [#][163] ^ |

[image: Vote: I like it] +10[image: Vote: I do not like it]

This is pretty cool. It looks like this uses analytical bounds to prove runtime, but is still combinatorial with respect to the coefficients, so it can work over an arbitrary ring, is that correct?

Also, do you know how it compares to analytical approaches like [this][164] paper? I thought they might be a little similar, using logs is kind of like writing the evaluation of the Dirichlet series in fixed-point in base $$$B$$$.

&rarr; Reply

 |

-

&raquo;

&raquo;

[kessido][165]

 |

23 months ago, show (+ 1) #

 |

&raquo;

&raquo;

[165]

[kessido][165]

 |

23 months ago, hide [#][166] ^ |

[image: Vote: I like it] +10[image: Vote: I do not like it]

This is suspiciously similar to the main idea in the paper I published with a couple of friends a year prior to this post (2022)...

Computing $$$\pi(N)$$$: An elementary approach in $$$\widetilde{O}(\sqrt{N})$$$ time.

We transform the Dirichlet convolution to a classical FFT convolution, and show how to compute many number-theoretic functions using it:

  -

The number of primes up to $$$N$$$ in time $$$\widetilde{O}(\sqrt{N})$$$.

  -

Mertens function (sum over the Möbius function) in time $$$O(\sqrt{N} \log N \sqrt{\log \log N})$$$.

  -

Sum of primes up to $$$N$$$ in time $$$\widetilde{O}(\sqrt{N})$$$.

  -

Number of primes $$$p \equiv r \ (\text{mod} \ m)$$$ up to $$$N$$$ in time $$$\widetilde{O}(\sqrt{N})$$$.

  -

Number of square-free numbers up to $$$N$$$ in time $$$\widetilde{O}(N^{1/3})$$$.

  -

Sum of Euler’s totient function up to $$$N$$$ in time $$$\widetilde{O}(\sqrt{N})$$$.

You can read it over here: [https://arxiv.org/abs/2212.09857][158]

And you can check our implementation here: [https://github.com/PrimeCounting/PrimeCounting][167]

&rarr; Reply

 |

  -

&raquo;

&raquo;

&raquo;

[PinkieRabbit][153]

 |

23 months ago, show #

 |

&raquo;

&raquo;

&raquo;

[153]

[PinkieRabbit][153]

 |

23 months ago, hide [#][168] ^ |

&larr; Rev. 2 &rarr;

[image: Vote: I like it] 0[image: Vote: I do not like it]

Very cool! Back then we are not aware of your independent discovering, but with months passed, some found your paper and confirmed that they are similar. Refer to [https://github.com/yosupo06/library-checker-problems/issues/1118][160] the Library Checker proposal, in which they acknowledged yours. The proposer [tweeted this][159] on Twitter, you may also refer.

I will edit the comment to acknowledge yours.

&rarr; Reply

 |

In English In Russian

&uarr;

---

---

&darr;

[Codeforces][169] (c) Copyright 2010-2026 Mike Mirzayanov

The only programming contests Web 2.0 platform

Server time: Aug/14/2026 19:31:08 (f1).

Desktop version, switch to [mobile version][170].

[Privacy Policy][171] | [Terms and Conditions][172]

Supported by

[image: TON] [173]

User lists

Name |


## Links

[1]: /
[2]: ?locale=en
[3]: ?locale=ru
[4]: /enter?back=%2Fblog%2Fentry%2F117635
[5]: /register
[6]: /top
[7]: /catalog
[8]: /contests
[9]: /gyms
[10]: /problemset
[11]: /groups
[12]: /ratings
[13]: /edu/courses
[14]: /apiHelp
[15]: /calendar
[16]: /help
[17]: /contest/2251/standings
[18]: /contestRegistration/2251
[19]: /profile/Benq
[20]: /profile/jiangly
[21]: /profile/VivaciousAubergine
[22]: /profile/maroonrk
[23]: /profile/tourist
[24]: /profile/Kevin114514
[25]: /profile/turmax
[26]: /profile/Um_nik
[27]: /profile/Radewoosh
[28]: /profile/heuristica
[29]: /ratings/countries
[30]: /ratings/cities
[31]: /ratings/organizations
[32]: /profile/Qingyu
[33]: /profile/maspy
[34]: /profile/adamant
[35]: /profile/DNR
[36]: /profile/Dominater069
[37]: /profile/Proof_by_QED
[38]: /profile/BledDest
[39]: /profile/errorgorn
[40]: /top-contributed
[41]: /profile/ICPCNews
[42]: /blog/entry/155646
[43]: /profile/chromate00
[44]: /blog/entry/151515
[45]: /profile/jay_jayjay
[46]: /blog/entry/155979
[47]: /profile/kylychbek
[48]: /blog/entry/155968
[49]: /blog/entry/155980
[50]: /profile/BitByBit123
[51]: /blog/entry/155862
[52]: /profile/megahertz13
[53]: /blog/entry/155981
[54]: /profile/greateric
[55]: /blog/entry/155945
[56]: /profile/Errichto
[57]: /blog/entry/155971
[58]: /profile/ayushpandey_23
[59]: /blog/entry/154242
[60]: /profile/zeyd1234
[61]: /blog/entry/155967
[62]: /profile/Au_Bing
[63]: /blog/entry/155993
[64]: /profile/atcoder_official
[65]: /blog/entry/155990
[66]: /profile/mariza_CY
[67]: /blog/entry/153536
[68]: /blog/entry/153535
[69]: /profile/__rose
[70]: /blog/entry/146793
[71]: /blog/entry/155991
[72]: /blog/entry/155911
[73]: /profile/GomerDoGo
[74]: /blog/entry/155946
[75]: /profile/Top12
[76]: /blog/entry/155807
[77]: /profile/bihariforces
[78]: /blog/entry/153395
[79]: /profile/codersaky77
[80]: /blog/entry/155976
[81]: /profile/i_pranavmehta
[82]: /blog/entry/117653
[83]: /profile/PavelKunyavskiy
[84]: /blog/entry/104593
[85]: /profile/SheTheRay
[86]: /blog/entry/155988
[87]: /recent-actions
[88]: /blog/adamant
[89]: /teams/with/adamant
[90]: /submissions/adamant
[91]: /groups/with/adamant
[92]: /contests/with/adamant
[93]: /contests/writer/adamant
[94]: /blog/entry/117635
[95]: /topic/118259/en25
[96]: https://en.wikipedia.org/wiki/Arithmetic_function
[97]: https://en.wikipedia.org/wiki/Dirichlet_convolution
[98]: https://codeforces.com/blog/entry/117783
[99]: /profile/ecnerwala
[100]: https://codeforces.com/blog/entry/91632#comment-802482
[101]: https://codeforces.com/blog/entry/54150
[102]: /profile/Nisiyama_Suzune
[103]: https://en.wikipedia.org/wiki/Multiplicative_function
[104]: https://en.wikipedia.org/wiki/Divisor_function
[105]: https://en.wikipedia.org/wiki/Euler%27s_totient_function
[106]: https://en.wikipedia.org/wiki/Dirichlet_hyperbola_method
[107]: https://projecteuler.net/problem=401
[108]: https://en.wikipedia.org/wiki/Orthogonal_convex_hull
[109]: https://codeforces.com/blog/entry/54090
[110]: https://judge.yosupo.jp/problem/sum_of_totient_function
[111]: https://judge.yosupo.jp/submission/147214
[112]: https://en.wikipedia.org/wiki/Möbius_inversion_formula
[113]: https://en.wikipedia.org/wiki/Mertens_function
[114]: https://projecteuler.net/problem=625
[115]: https://projecteuler.net/problem=351
[116]: https://codeforces.com/blog/entry/53925
[117]: https://gbroxey.github.io/blog/2023/04/30/mult-sum-1.html
[118]: https://codeforces.com/blog/entry/117635#comment-1041220
[119]: /search?query=tutorial
[120]: /search?query=dirichlet+convolution
[121]: /blog/entry/117635#comments
[122]: /profile/ConnectedGraph
[123]: #comment-1040821
[124]: /profile/the_Incharge
[125]: #comment-1040859
[126]: #comment-1040915
[127]: /profile/tfg
[128]: #comment-1040893
[129]: /profile/Psychotic_D
[130]: #comment-1040872
[131]: /profile/nor
[132]: #comment-1040985
[133]: https://en.wikipedia.org/wiki/Dirichlet_series_inversion
[134]: https://en.wikipedia.org/wiki/Fourier_transform_on_finite_groups
[135]: https://math.uchicago.edu/~may/REU2016/REUPapers/Monson.pdf
[136]: https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/NTfourier.htm
[137]: https://arxiv.org/pdf/2012.06963.pdf
[138]: https://math.nyu.edu/~goodman/teaching/NumberTheory/notes/DirichletTheorem.pdf
[139]: https://www.math.leidenuniv.nl/~pbruin/L-functions.pdf
[140]: https://www.math.columbia.edu/~phlee/CourseNotes/L-functions.pdf
[141]: #comment-1040993
[142]: #comment-1041002
[143]: https://github.com/ecnerwala/cp-book/blob/master/src/dirichlet_series.hpp
[144]: #comment-1041053
[145]: /profile/hos.lyric
[146]: #comment-1041067
[147]: #comment-1041996
[148]: #comment-1042129
[149]: #comment-1041071
[150]: #comment-1041220
[151]: #comment-1041315
[152]: https://specfun.inria.fr/bostan/publications/BoLeSc03.pdf
[153]: /profile/PinkieRabbit
[154]: #comment-1045987
[155]: /profile/zhoukangyang
[156]: https://en.wikipedia.org/wiki/Divisor_summatory_function
[157]: https://www.cnblogs.com/zkyJuruo/p/17544928.html
[158]: https://arxiv.org/pdf/2212.09857
[159]: https://x.com/negiizhao/status/1768007989984899152
[160]: https://github.com/yosupo06/library-checker-problems/issues/1118
[161]: #comment-1046037
[162]: https://en.wikipedia.org/wiki/Partition_function_%28number_theory%29#Approximation_formulas
[163]: #comment-1046418
[164]: https://www-users.cse.umn.edu/~odlyzko/doc/arch/analytic.pi.of.x.pdf
[165]: /profile/kessido
[166]: #comment-1198172
[167]: https://github.com/PrimeCounting/PrimeCounting
[168]: #comment-1198335
[169]: https://codeforces.com/
[170]: ?mobile=true
[171]: /privacy
[172]: /terms
[173]: https://ton.org/
