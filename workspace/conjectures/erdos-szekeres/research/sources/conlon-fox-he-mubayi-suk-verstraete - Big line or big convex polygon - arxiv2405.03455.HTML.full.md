<!-- source: https://arxiv.org/html/2405.03455v1 | converted from HTML -->

Big line or big convex polygon

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2405.03455v1 [math.CO] 06 May 2024

# Big line or big convex polygon

David Conlon Thanks: Department of Mathematics, California Institute of Technology, Pasadena, CA 91125. Email: dconlon@caltech.edu. Research supported by NSF Awards DMS-2054452 and DMS-2348859. Jacob Fox Thanks: Department of Mathematics, Stanford University, Stanford, CA 94305. Email: jacobfox@stanford.edu. Research supported by NSF Award DMS-2154129. Xiaoyu He Thanks: Department of Mathematics, Princeton University, Princeton, NJ 08544. Email: xiaoyuh@princeton.edu. Research supported by NSF Award DMS-2103154. Dhruv Mubayi Thanks: Department of Mathematics, Statistics and Computer Science, University of Illinois, Chicago, IL 60607. Email: mubayi@uic.edu. Research partially supported by NSF Awards DMS-1952767 and DMS-2153576. Andrew Suk Thanks: Department of Mathematics, University of California at San Diego, La Jolla, CA 92093. Email: asuk@ucsd.edu. Research supported by an NSF CAREER Award and by NSF Awards DMS-1952786 and DMS-2246847. Jacques Verstraëte Thanks: Department of Mathematics, University of California at San Diego, La Jolla, CA 92093. Email: jacques@ucsd.edu. Research supported by NSF Award DMS-1800332.

###### Abstract

Let E ​ S ℓ ​ ( n) ES_{\ell}(n) be the minimum N N such that every N N -element point set in the plane contains either ℓ \ell collinear members or n n points in convex position. We prove that there is a constant C > 0 C>0 such that, for each ℓ, n ≥ 3 \ell,n\geq 3,

 | ( 3 ​ ℓ − 1) ⋅ 2 n − 5 < E ​ S ℓ ​ ( n) < ℓ 2 ⋅ 2 n + C ​ n ​ log ⁡ n. (3\ell-1)\cdot 2^{n-5}<ES_{\ell}(n)<\ell^{2}\cdot 2^{n+C\sqrt{n\log n}}. |  |

A similar extension of the well-known Erdős–Szekeres cups-caps theorem is also proved.

## 1 Introduction

Given an n n -element point set P P in the plane, we say that P P is in *convex position*if P P is the vertex set of a convex n n -gon. We say that P P is in *general position*if no three members of P P are collinear. In 1935, addressing a problem raised by Klein, Erdős and Szekeres [4] proved that, for every integer n ≥ 3 n\geq 3, there is a minimal integer E ​ S ​ ( n) ES(n) such that any set of E ​ S ​ ( n) ES(n) points in the plane in general position contains n n members in convex position. Moreover, they showed that E ​ S ​ ( n) ≤ ( 2 ​ n − 4 n − 2) + 1 = 4 n + o ⁡ ( n) ES(n)\leq{2n-4\choose n-2}+1=4^{n+o(n)}. Many years later [5], they proved that E ​ S ​ ( n) ≥ 2 n − 2 + 1 ES(n)\geq 2^{n-2}+1, a bound that they had already conjectured to be tight in their earlier paper. It remained an open problem for several decades to improve the bound E ​ S ​ ( n) ≤ 4 n + o ⁡ ( n) ES(n)\leq 4^{n+o(n)} by any significant factor. This was finally accomplished by Suk [11], who proved that E ​ S ​ ( n) = 2 n + o ⁡ ( n) ES(n)=2^{n+o(n)}, coming close to matching Erdős and Szekeres’ lower bound and proving their conjecture. The best explicit bound for the o ⁡ ( n) o(n) term to date is due to Holmsen et al. [6], who optimized the argument in [11] and showed that E ​ S ​ ( n) ≤ 2 n + O ⁡ ( n ​ log ⁡ n) ES(n)\leq 2^{n+O(\sqrt{n\log n})}.

In this paper, we extend these results to arbitrary point sets in the plane. Let E ​ S ℓ ​ ( n) ES_{\ell}(n) be the minimum N N such that every N N -point set in the plane contains either ℓ \ell collinear points or n n points in convex position. Hence, E ​ S 3 ​ ( n) = E ​ S ​ ( n) ES_{3}(n)=ES(n). For ℓ ≥ 3 \ell\geq 3, we prove the following.

###### Theorem 1.1.

There exists C > 0 C>0 such that, for each ℓ, n ≥ 3 \ell,n\geq 3, E ​ S ℓ ​ ( n) ≤ ℓ 2 ⋅ 2 n + C ​ n ​ log ⁡ n ES_{\ell}(n)\leq\ell^{2}\cdot 2^{n+C\sqrt{n\log n}}.

The proof of Theorem 1.1 is based on both a new cups-caps theorem for arbitrary point sets in the plane and a new positive fraction Erdős–Szekeres theorem. In the case where n n is fixed and ℓ \ell tends to infinity, our cups-caps theorem implies that E ​ S ℓ ​ ( n) = O ⁡ ( ℓ) ES_{\ell}(n)=O(\ell), which is best possible up to constants. In turn, our lower bound for the cups-caps theorem implies the following lower bound for E ​ S ℓ ​ ( n) ES_{\ell}(n), which agrees with the Erdős–Szekeres lower bound in the ℓ = 3 \ell=3 case.

###### Theorem 1.2.

For each ℓ, n ≥ 3 \ell,n\geq 3, E ​ S ℓ ​ ( n) ≥ ( 3 ​ ℓ − 1) ⋅ 2 n − 5 + 1 ES_{\ell}(n)\geq(3\ell-1)\cdot 2^{n-5}+1.

It remains an interesting open problem to determine the correct dependence of E ​ S ℓ ​ ( n) ES_{\ell}(n) on ℓ \ell.

The paper is organized as follows. In the next section, we prove our cups-caps theorem for arbitrary point sets and Theorem 1.2. In Section 3, we establish a positive fraction Erdős–Szekeres theorem for arbitrary point sets. Finally, in Section 4, we prove Theorem 1.1. For the sake of clarity, we omit floor and ceiling signs whenever they are not crucial. We assume throughout that our point sets have distinct x x -coordinates, since we can slightly rotate the plane otherwise.

## 2 A cups-caps theorem for arbitrary point sets

Let X X be a k k -element point set in the plane with distinct x x -coordinates. We say that X X forms a *k k -cup*(*k k -cap*) if X X is in convex position and its convex hull is bounded above (below) by a single edge. The *length*of a k k -cup ( k k -cap) is k − 1 k-1. Write f ℓ ​ ( m, n) f_{\ell}(m,n) for the minimum N N such that every N N -point set in the plane contains either ℓ \ell collinear members, an m m -cup or an n n -cap. Erdős and Szekeres [4] proved that

 | f 3 ​ ( m, n) = ( m + n − 4 n − 2) + 1. f_{3}(m,n)={m+n-4\choose n-2}+1. |  | (1) |

For ℓ ≥ 3 \ell\geq 3, we prove the following.

###### Theorem 2.1.

There is an absolute constant c > 1 c>1 such that, for m, n, ℓ ≥ 3 m,n,\ell\geq 3,

 | f ℓ ​ ( m, n) ≤ c ⁡ ( min ⁡ { m − 1, n − 1 } + ℓ) ⋅ ( m + n − 4 n − 2). f_{\ell}(m,n)\leq c(\min\{m-1,n-1\}+\ell)\cdot{m+n-4\choose n-2}. |  |

The proof of this theorem is based on a connection between down-sets and ( 1) discovered by Moshkovitz and Shapira [8]. We will also need the following lemma due to Beck [1].

###### Lemma 2.2 (Theorem 1.2 in [1]).

There is an absolute constant ε > 0 \varepsilon>0 such that every t t -element point set in the plane contains either ε ​ t \varepsilon t collinear points or determines at least ε ​ ( t 2) \varepsilon\binom{t}{2} distinct lines.

###### Proof of Theorem 2.1.

Let ε > 0 \varepsilon>0 be the absolute constant from Lemma 2.2 and set c = 10 / ε c=10/\varepsilon. Let P P be an N N -element point set in the plane where N = c ⋅ ( min ⁡ { m − 1, n − 1 } + ℓ) ⋅ ( m + n − 4 n − 2) + 1. N=c\cdot(\min\{m-1,n-1\}+\ell)\cdot{m+n-4\choose n-2}+1. We may assume that P P does not contain ℓ \ell collinear members, since otherwise we would be done. Given points p, q ∈ P p,q\in P, we write p < q p<q if the x x -coordinate of p p is less than the x x -coordinate of q q. For the sake of contradiction, suppose P P contains neither an m m -cup nor an n n -cap. Hence, the longest cup in P P has length at most m − 2 m-2 and the longest cap in P P has length at most n − 2 n-2.

Let p, q ∈ P p,q\in P be such that p < q p<q. We label the pair p ​ q pq with the ordered pair ( x p ​ q, y p ​ q) (x_{pq},y_{pq}), where x p ​ q x_{pq} is the length of the longest cup ending at p ​ q pq and y p ​ q y_{pq} is the length of the longest cap ending at p ​ q pq. Let L ⁡ ( m − 2, n − 2) L(m-2,n-2) be the poset on [m − 2] × [n − 2] [m-2]\times[n-2] where ( x, y) ⪯ ( x ′, y ′) (x,y)\preceq(x^{\prime},y^{\prime}) iff x ≤ x ′ x\leq x^{\prime} and y ≤ y ′ y\leq y^{\prime}. For each q ∈ P q\in P, let S ( q) = { ( x p ​ q, y p ​ q): p ∈ P, p < q } S(q)=\{(x_{pq},y_{pq}):p\in P,\,p<q\}. Let D ( q) = { ( x, y) ∈ L ( m − 2, n − 2): ∃ ( x p ​ q, y p ​ q) ∈ S ( q), ( x, y) ⪯ ( x p ​ q, y p ​ q) } D(q)=\{(x,y)\in L(m-2,n-2):\exists(x_{pq},y_{pq})\in S(q),\,(x,y)\preceq(x_{pq},y_{pq})\} be the *down-set*in L ⁡ ( m − 2, n − 2) L(m-2,n-2) generated by S ⁡ ( q) S(q).

The number of down-sets in L ⁡ ( m − 2, n − 2) L(m-2,n-2) is ( m + n − 4 n − 2) {m+n-4\choose n-2} (see, e.g., [8, Observation 2.1]). Hence, by the pigeonhole principle, there are points q 1 < q 2 < ⋯ < q t q_{1}<q_{2}<\cdots<q_{t} in P P with t ≥ c ⋅ ( min ⁡ { m − 1, n − 1 } + ℓ) t\geq c\cdot(\min\{m-1,n-1\}+\ell) such that D ⁡ ( q i) = D ⁡ ( q j) D(q_{i})=D(q_{j}) for all i < j i<j. Set Q = { q 1, …, q t } Q=\{q_{1},\ldots,q_{t}\}. By Lemma 2.2, Q Q contains either ε ​ t \varepsilon t collinear members or determines at least ε ​ ( t 2) \varepsilon\binom{t}{2} distinct lines. In the former case, we have ε ​ t > ℓ \varepsilon t>\ell collinear points, which is a contradiction. Hence, Q Q determines at least ε ​ ( t 2) \varepsilon\binom{t}{2} distinct lines. By averaging, there is a point p ∈ Q p\in Q and a subset Q ′ ⊂ Q Q^{\prime}\subset Q of size at least ε ​ t / 2 > min ⁡ { m − 1, n − 1 } \varepsilon t/2>\min\{m-1,n-1\} such that p < q p<q for each q ∈ Q ′ q\in Q^{\prime} and there are | Q ′ | |Q^{\prime}| distinct lines between p p and Q ′ Q^{\prime}. Consider the labels on p ​ q pq for each q ∈ Q ′ q\in Q^{\prime}. Since the maximum size of an antichain in L ⁡ ( m − 2, n − 2) L(m-2,n-2) is min ⁡ { m − 1, n − 1 } \min\{m-1,n-1\}, by the pigeonhole principle, we obtain points p, q, q ′ p,q,q^{\prime} such that p < q < q ′ p<q<q^{\prime} and

1. 1.

D ⁡ ( p) = D ⁡ ( q) = D ⁡ ( q ′) D(p)=D(q)=D(q^{\prime}) and

2. 2.

( x p ​ q, y p ​ q) ⪯ ( x p ​ q ′, y p ​ q ′) (x_{pq},y_{pq})\preceq(x_{pq^{\prime}},y_{pq^{\prime}}) or ( x p ​ q, y p ​ q) ⪰ ( x p ​ q ′, y p ​ q ′). (x_{pq},y_{pq})\succeq(x_{pq^{\prime}},y_{pq^{\prime}}).

Let us assume by symmetry that ( x p ​ q, y p ​ q) ⪰ ( x p ​ q ′, y p ​ q ′) (x_{pq},y_{pq})\succeq(x_{pq^{\prime}},y_{pq^{\prime}}). Since D ⁡ ( p) = D ⁡ ( q) D(p)=D(q), there exists ( x, y) ∈ S ⁡ ( p) ⊂ D ⁡ ( p) (x,y)\in S(p)\subset D(p) such that ( x, y) ⪰ ( x p ​ q, y p ​ q) (x,y)\succeq(x_{pq},y_{pq}) and, by transitivity, ( x, y) ⪰ ( x p ​ q ′, y p ​ q ′) (x,y)\succeq(x_{pq^{\prime}},y_{pq^{\prime}}). By the definition of S ⁡ ( p) S(p), there exists p ′ < p p^{\prime}<p such that x = x p ′ ​ p x=x_{p^{\prime}p} and y = y p ′ ​ p y=y_{p^{\prime}p}. Since p, q, q ′ p,q,q^{\prime} are not collinear, one of p ′ ​ p ​ q, p ′ ​ p ​ q ′ p^{\prime}pq,p^{\prime}pq^{\prime} is not collinear. Without loss of generality, we can assume that p ′ ​ p ​ q p^{\prime}pq is not collinear, since the other case is symmetric. Then the triple p ′ ​ p ​ q p^{\prime}pq is either a cup or a cap. In the former case, the longest cup ending at p ′ ​ p p^{\prime}p with length x p ′ ​ p x_{p^{\prime}p} can be extended to end at p ​ q pq, which is a contradiction. If instead p ′ ​ p ​ q p^{\prime}pq is a cap, then the longest cap ending at p ′ ​ p p^{\prime}p with length y p ′ ​ p y_{p^{\prime}p} can be extended to end at p ​ q pq, again a contradiction. ∎

In the other direction, we prove the following.

###### Theorem 2.3.

 | f ℓ ​ ( m, n) > ℓ − 1 2 ​ ( m + n − 4 n − 2) − ℓ − 3 2 ​ ( m + n − 6 n − 3). f_{\ell}(m,n)>\frac{\ell-1}{2}\binom{m+n-4}{n-2}-\frac{\ell-3}{2}\binom{m+n-6}{n-3}. |  |

###### Proof.

Set

 | h ℓ ​ ( m, n):= ℓ − 1 2 ​ ( m + n − 4 n − 2) − ℓ − 3 2 ​ ( m + n − 6 n − 3). h_{\ell}(m,n):=\frac{\ell-1}{2}\binom{m+n-4}{n-2}-\frac{\ell-3}{2}\binom{m+n-6}{n-3}. |  |

In what follows, we will recursively construct planar point sets X ℓ, m, n X_{\ell,m,n} with | X ℓ, m, n | ≥ h ℓ ​ ( m, n) |X_{\ell,m,n}|\geq h_{\ell}(m,n) that contain neither ℓ \ell collinear points, m m -cups nor n n -caps. For ℓ, m ≥ 3 \ell,m\geq 3, we construct X ℓ, m, 3 X_{\ell,m,3} by taking the lower half of a regular m m -gon and, on ⌊ ( m − 1) / 2 ⌋ \lfloor(m-1)/2\rfloor of these segments, placing ℓ − 1 \ell-1 collinear points in the interior of the segment. If m − 1 m-1 is odd, then add another point on a segment by itself (adding more than one point to this segment would create an m m -cup). Hence, we have no ℓ \ell collinear points, no m m -cup and no 3 3 -cap. Moreover,

 | | X ℓ, m, 3 | = { ( ℓ − 1) ​ m − 1 2 if m − 1 is even ( ℓ − 1) ​ m − 2 2 + 1 if m − 1 is odd. |X_{\ell,m,3}|=\left\{\begin{array}[]{ll}(\ell-1)\frac{m-1}{2}&\textnormal{if $m-1$ is even}\\ \\ (\ell-1)\frac{m-2}{2}+1&\textnormal{if $m-1$ is odd.}\end{array}\right. |  |

Hence, for all m ≥ 3 m\geq 3,

 | | X ℓ, m, 3 | ≥ ℓ − 1 2 ​ ( m − 1) − ℓ − 3 2 = h ℓ ​ ( m, 3), |X_{\ell,m,3}|\geq\frac{\ell-1}{2}(m-1)-\frac{\ell-3}{2}=h_{\ell}(m,3), |  |

as desired. We construct X ℓ, 3, n X_{\ell,3,n} similarly such that

 | | X ℓ, 3, n | ≥ ℓ − 1 2 ​ ( n − 1) − ℓ − 3 2 = h ℓ ​ ( 3, n). |X_{\ell,3,n}|\geq\frac{\ell-1}{2}(n-1)-\frac{\ell-3}{2}=h_{\ell}(3,n). |  |

For the recursive step, assume that we have constructed X ℓ, m ′, n ′ X_{\ell,m^{\prime},n^{\prime}} for all m ′ < m m^{\prime}<m or n ′ < n n^{\prime}<n. We construct X ℓ, m, n X_{\ell,m,n} as follows. Take a very flat copy of X ℓ, m − 1, n X_{\ell,m-1,n} and a very flat copy of X ℓ, m, n − 1 X_{\ell,m,n-1} such that X ℓ, m, n − 1 X_{\ell,m,n-1} is very high and far to the right of X ℓ, m − 1, n X_{\ell,m-1,n}, the line spanned by any two points in X ℓ, m − 1, n X_{\ell,m-1,n} lies below X ℓ, m, n − 1 X_{\ell,m,n-1} and the line spanned by any two points in X ℓ, m, n − 1 X_{\ell,m,n-1} lies above X ℓ, m − 1, n X_{\ell,m-1,n}. See Figure 1.

X ℓ, m − 1, n X_{\ell,m-1,n} X ℓ, m, n − 1 X_{\ell,m,n-1} Figure 1: Construction for X ℓ, m, n X_{\ell,m,n} from X ℓ, m, n − 1 X_{\ell,m,n-1} and X ℓ, m, n − 1 X_{\ell,m,n-1}.

Hence, the resulting set does not contain ℓ \ell collinear points and neither an m m -cup nor an n n -cap. Finally,

 | | X ℓ, m, n | \displaystyle|X_{\ell,m,n}| | ≥ \displaystyle\geq | | X ℓ, m − 1, n | + | X ℓ, m, n − 1 | \displaystyle|X_{\ell,m-1,n}|+|X_{\ell,m,n-1}| |  |

 |  | ≥ \displaystyle\geq | h ℓ ​ ( m − 1, n) + h ℓ ​ ( m, n − 1) \displaystyle h_{\ell}(m-1,n)+h_{\ell}(m,n-1) |  |

 |  | ≥ \displaystyle\geq | ℓ − 1 2 ​ ( m + n − 5 n − 2) − ℓ − 3 2 ​ ( m + n − 7 n − 3) + ℓ − 1 2 ​ ( m + n − 5 n − 3) − ℓ − 3 2 ​ ( m + n − 7 n − 4) \displaystyle\frac{\ell-1}{2}\binom{m+n-5}{n-2}-\frac{\ell-3}{2}\binom{m+n-7}{n-3}+\frac{\ell-1}{2}\binom{m+n-5}{n-3}-\frac{\ell-3}{2}\binom{m+n-7}{n-4} |  |

 |  | = \displaystyle= | ℓ − 1 2 ​ ( m + n − 4 n − 2) − ℓ − 3 2 ​ ( m + n − 6 n − 3), \displaystyle\frac{\ell-1}{2}\binom{m+n-4}{n-2}-\frac{\ell-3}{2}\binom{m+n-6}{n-3}, |  |

as required. ∎

### 2.1 Proof of Theorem 1.2

We now use Theorem 2.3 to prove Theorem 1.2, the statement that E ​ S ℓ ​ ( n) ≤ ℓ 2 ⋅ 2 n + C ​ n ​ log ⁡ n ES_{\ell}(n)\leq\ell^{2}\cdot 2^{n+C\sqrt{n\log n}} for all ℓ, n ≥ 3 \ell,n\geq 3.

###### Proof of Theorem 1.2.

Let X ℓ, m, n X_{\ell,m,n} be the point set from the proof of Theorem 2.3 with no ℓ \ell collinear points, no m m -cup and no n n -cap, recalling that

 | | X ℓ, m, n | ≥ h ℓ ​ ( m, n) = ℓ − 1 2 ​ ( m + n − 4 n − 2) − ℓ − 3 2 ​ ( m + n − 6 n − 3). |X_{\ell,m,n}|\geq h_{\ell}(m,n)=\frac{\ell-1}{2}\binom{m+n-4}{n-2}-\frac{\ell-3}{2}\binom{m+n-6}{n-3}. |  |

Let S S be a unit circle in the plane centered at the origin and consider the arc α \alpha along S S from ( 0, 1) (0,1) to ( 1, 0) (1,0). Place a very small flat copy of X ℓ, n, 3 X_{\ell,n,3} near ( 0, 1) (0,1) and a very small flat copy of X ℓ, 3, n X_{\ell,3,n} near ( 1, 0) (1,0). Then evenly spread out very small flat copies of X ℓ, n − 2, 4, X ℓ, n − 3, 5, …, X ℓ, n − 2 − i, 4 + i, …, X ℓ, 4, n − 2 X_{\ell,n-2,4},X_{\ell,n-3,5},\ldots,X_{\ell,n-2-i,4+i},\ldots,X_{\ell,4,n-2} along α \alpha from top to bottom, between X ℓ, n, 3 X_{\ell,n,3} and X ℓ, 3, n X_{\ell,3,n}. We make each copy flat enough that the line generated by any two points in X ℓ, n − 2 − i, 4 + i X_{\ell,n-2-i,4+i} lies below X ℓ, n − 2 − j, 4 + j X_{\ell,n-2-j,4+j} for j < i j<i and lies above X ℓ, n − 2 − j, 4 + j X_{\ell,n-2-j,4+j} for j > i j>i. See Figure 2. Let P P be the final point set. Then

 | | P | \displaystyle|P| | ≥ \displaystyle\geq | ℓ − 1 2 ​ ( ( n − 1 1) + ( ∑ i = 0 n − 6 ( n − 2 2 + i)) + ( n − 1 n − 2)) − ℓ − 1 3 ​ ( ( n − 3 0) + ( ∑ i = 0 n − 6 ( n − 4 1 + i)) + ( n − 3 n − 3)) \displaystyle\frac{\ell-1}{2}\left(\binom{n-1}{1}+\left(\sum\limits_{i=0}^{n-6}\binom{n-2}{2+i}\right)+\binom{n-1}{n-2}\right)-\frac{\ell-1}{3}\left(\binom{n-3}{0}+\left(\sum\limits_{i=0}^{n-6}\binom{n-4}{1+i}\right)+\binom{n-3}{n-3}\right) |  |

 |  | = \displaystyle= | ℓ − 1 2 ​ ∑ i = 0 n − 2 ( n − 2 i) − ℓ − 3 2 ​ ∑ i = 0 n − 4 ( n − 4 i) \displaystyle\frac{\ell-1}{2}\sum\limits_{i=0}^{n-2}\binom{n-2}{i}-\frac{\ell-3}{2}\sum\limits_{i=0}^{n-4}\binom{n-4}{i} |  |

 |  | = \displaystyle= | ℓ − 1 2 ​ 2 n − 2 − ℓ − 3 2 ​ 2 n − 4 \displaystyle\frac{\ell-1}{2}2^{n-2}-\frac{\ell-3}{2}2^{n-4} |  |

 |  | = \displaystyle= | ( 3 ​ ℓ − 1) ​ 2 n − 5. \displaystyle(3\ell-1)2^{n-5}. |  |

[image: Refer to caption] Figure 2: The lower bound construction for E ​ S ℓ ​ ( n) ES_{\ell}(n).

Now suppose that K ⊂ P K\subset P is a subset in convex position. If K ⊂ X ℓ, n − 2 − i, 4 + i K\subset X_{\ell,n-2-i,4+i} for some i ≥ 0 i\geq 0, then | K | < n |K|<n. If K ⊂ X ℓ, n, 3 K\subset X_{\ell,n,3}, then | K | < n |K|<n by the structure of X ℓ, n, 3 X_{\ell,n,3}. A similar argument holds if K ⊂ X ℓ, 3, n K\subset X_{\ell,3,n}.

Suppose then that K K has a non-empty intersection with at least two of the parts. Let i i be the minimum integer such that K ∩ X ℓ, n − 2 − i, 4 + i ≠ ∅ K\cap X_{\ell,n-2-i,4+i}\neq\emptyset and j j be the maximum integer such that K ∩ X ℓ, n − 2 − j, 4 + j ≠ ∅ K\cap X_{\ell,n-2-j,4+j}\neq\emptyset. Assume that 0 ≤ i ≤ j ≤ n − 6 0\leq i\leq j\leq n-6, that is, that K K omits both the highest and lowest sets in our construction. By the flatness condition, for all i < s < j i<s<j, we have K ∩ X ℓ, n − 2 − s, 4 + s ≤ 1 K\cap X_{\ell,n-2-s,4+s}\leq 1. Hence,

 | | K | ≤ ( 4 + i − 1) + ( j − i − 1) + ( n − 2 − j − 1) = n − 1. |K|\leq(4+i-1)+(j-i-1)+(n-2-j-1)=n-1. |  |

Suppose now that | K ∩ X ℓ, n, 3 | ≠ ∅ |K\cap X_{\ell,n,3}|\neq\emptyset and the largest j j such that K ∩ X ℓ, n − 2 − j, 4 + j ≠ ∅ K\cap X_{\ell,n-2-j,4+j}\neq\emptyset satisfies 0 ≤ j ≤ n − 6 0\leq j\leq n-6 (or that no such j j exists) and | K ∩ X ℓ, 3, n | = ∅ |K\cap X_{\ell,3,n}|=\emptyset. If | K ∩ X ℓ, n, 3 | ≥ 3 |K\cap X_{\ell,n,3}|\geq 3, then K ∩ X ℓ, n, 3 K\cap X_{\ell,n,3} is a cup, which means that K ⊂ X ℓ, n, 3 K\subset X_{\ell,n,3} and hence | K | ≤ n − 1 |K|\leq n-1. Otherwise, | K ∩ X ℓ, n, 3 | ≤ 2 |K\cap X_{\ell,n,3}|\leq 2 and | K | ≤ 2 + ( n − 3 − j) + j = n − 1 |K|\leq 2+(n-3-j)+j=n-1. A similar argument applies if | K ∩ X ℓ, 3, n | ≠ ∅ |K\cap X_{\ell,3,n}|\neq\emptyset. Finally, if | K ∩ X ℓ, n, 3 | ≠ ∅ |K\cap X_{\ell,n,3}|\neq\emptyset and | K ∩ X ℓ, 3, n | ≠ ∅ |K\cap X_{\ell,3,n}|\neq\emptyset, then | K | ≤ 2 + ( n − 5) + 2 = n − 1 |K|\leq 2+(n-5)+2=n-1. Hence, E ​ S ℓ ​ ( n) ≥ ( 3 ​ ℓ − 1) ​ 2 n − 5 + 1 ES_{\ell}(n)\geq(3\ell-1)2^{n-5}+1, as required. ∎

## 3 A positive fraction cups-caps theorem for arbitrary point sets

In this subsection, we establish a positive fraction cups-caps theorem for arbitrary point sets. Given a k k -cap ( k k -cup) X = { x 1, …, x k } X=\{x_{1},\ldots,x_{k}\}, where the points appear in order from left to right, we define the *support of*X X to be the collection of open regions 𝒞 = { T 1, …, T k } \mathcal{C}=\{T_{1},\ldots,T_{k}\}, where T i T_{i} is the region outside of conv ​ ( X) \mbox{\rm conv}(X) bounded by the segment x i ​ x i + 1 ¯ \overline{x_{i}x_{i+1}} and by the lines x i − 1 ​ x i x_{i-1}x_{i}, x i + 1 ​ x i + 2 x_{i+1}x_{i+2} (where x k + 1 = x 1 x_{k+1}=x_{1}, x k + 2 = x 2 x_{k+2}=x_{2}, etc.). See Figure 3.

x 1 x_{1} T 1 T_{1} x 2 x_{2} x 3 x_{3} T 2 T_{2} T 3 T_{3} x 4 x_{4} T 4 T_{4} x 5 x_{5} T 5 T_{5} conv ​ ( X) \mbox{\rm conv}(X)

Figure 3: Regions T i T_{i} in the support of X X.

###### Theorem 3.1.

There is a constant c 1 c_{1} such that the following holds. Let P P be an N N -point planar set with no ℓ \ell points on a line and N > c 1 ​ ℓ ⋅ 2 32 ​ k N>c_{1}\ell\cdot 2^{32k}. Then there is a k k -element subset X ⊂ P X\subset P that is either a k k -cup or a k k -cap such that, for the regions T 1, …, T k − 1 T_{1},\ldots,T_{k-1} from the support of X X, the point sets P i = P ∩ T i P_{i}=P\cap T_{i} satisfy | P i | ≥ N / 2 32 ​ k |P_{i}|\geq N/2^{32k}. In particular, every ( k − 1) (k-1) -tuple obtained by selecting one point from each P i P_{i}, i = 1, …, k − 1 i=1,\ldots,k-1, is in convex position.

Let us remark that a positive-fraction cups-caps theorem for point sets in general position was first proved by Pach and Solymosi [9] and can be found more explicitly in [10]. Its proof is a simple supersaturation argument using ( 1). Unfortunately, this approach for point sets with no ℓ \ell collinear members gives a rather poor dependency on ℓ \ell. Instead, we will make use of simplicial partitions together with the probabilistic method. First, we need some simple definitions. A *cell*Δ ⊂ ℝ 2 \Delta\subset\mathbb{R}^{2} is a 1 or 2-dimensional simplex. Given a cell Δ ⊂ ℝ 2 \Delta\subset\mathbb{R}^{2}, we say that a line L L*crosses*Δ \Delta if L L intersects, but does not contain, Δ \Delta.

###### Lemma 3.2 ( [7, 2]).

Let P P be a set of N N points in the plane. Then, for any integer r > 0 r>0, there are disjoint subsets P 1, …, P r P_{1},\ldots,P_{r} of P P and disjoint cells Δ 1, …, Δ r \Delta_{1},\ldots,\Delta_{r} in ℝ 2 \mathbb{R}^{2}, with P i ⊂ Δ i P_{i}\subset\Delta_{i}, such that | P i | ≥ N / ( 8 ​ r) |P_{i}|\geq N/(8r) and every line in the plane crosses at most O ⁡ ( r) O(\sqrt{r}) cells Δ i \Delta_{i}.

Let us remark that in the original version of simplicial partitions due to Matousek [7], the cells Δ i \Delta_{i} may not necessarily be disjoint. However, in a newer version due to Chan [2], disjointness can also be guaranteed.

###### Proof of Theorem 3.1.

Let c 1 > c 2 c_{1}>c_{2} be large constants that will be determined later. Set r = c 2 ​ 2 16 ​ k r=c_{2}2^{16k}. Then we apply Lemma 3.2 with parameter r r to obtain subsets P 1, …, P r ⊂ P P_{1},\ldots,P_{r}\subset P and pairwise disjoint cells Δ 1, …, Δ r ⊂ ℝ 2 \Delta_{1},\ldots,\Delta_{r}\subset\mathbb{R}^{2} such that | P i | ≥ N / ( 8 ​ r) |P_{i}|\geq N/(8r) and P i ⊂ Δ i P_{i}\subset\Delta_{i}. Moreover, every line in the plane crosses at most O ⁡ ( r) O(\sqrt{r}) cells Δ i \Delta_{i}. Since

 | | P i | ≥ N 8 ​ r ≥ c 1 ​ ℓ ​ 2 32 ​ k 8 ​ c 2 ​ 2 16 ​ k > ℓ, |P_{i}|\geq\frac{N}{8r}\geq\frac{c_{1}\ell 2^{32k}}{8c_{2}2^{16k}}>\ell, |  |

no line contains a cell Δ i \Delta_{i}. We call a triple ( P i, P j, P s) (P_{i},P_{j},P_{s}) of parts *bad*if there is a line intersecting all three cells Δ i, Δ j \Delta_{i},\Delta_{j} and Δ s \Delta_{s}. Otherwise, we call the triple ( P i, P j, P s) (P_{i},P_{j},P_{s})*good*.

If there are three disjoint cells Δ i, Δ j, Δ s \Delta_{i},\Delta_{j},\Delta_{s} and a line L L that intersects all three, then we can translate and rotate L L so that L L is tangent to two of the cells and intersects the third. Hence, for every bad triple ( P i, P j, P s) (P_{i},P_{j},P_{s}), there is a line L L tangent to two of the cells, say Δ i \Delta_{i} and Δ j \Delta_{j}, such that L L intersect Δ s \Delta_{s}. For every pair { i, j } \{i,j\}, there are at most 4 tangent lines for Δ i \Delta_{i} and Δ j \Delta_{j} and, by our application of Lemma 3.2, there are at most O ⁡ ( r) O(\sqrt{r}) parts Δ s \Delta_{s} that intersect any of these 4 lines. Hence, the number of bad triples ( P i, P j, P s) (P_{i},P_{j},P_{s}) is at most O ⁡ ( r 2 ​ r) = c ′ ​ r 5 / 2 O(r^{2}\sqrt{r})=c^{\prime}r^{5/2}, where c ′ c^{\prime} is an absolute constant.

We pick each part P i P_{i} with probability p = 1 / ( 4 ​ c ′ ​ r 3 / 4) p=1/(\sqrt{4c^{\prime}}r^{3/4}). Then the expected number of parts chosen is p ​ r pr and the expected number of bad triples among them is at most

 | p 3 ​ c ′ ​ r 5 / 2 ≤ p ​ r / 4. p^{3}c^{\prime}r^{5/2}\leq pr/4. |  |

Hence, by the Chernoff bound, we can select at least 3 ​ p ​ r / 4 = Ω ⁡ ( r 1 / 4) 3pr/4=\Omega(r^{1/4}) parts P i P_{i} such that the number of bad triples among them is at most p ​ r / 2 pr/2. By deleting one part from each bad triple, we obtain p ​ r / 4 pr/4 parts P i P_{i} such that every triple among them is good. For simplicity, let P 1, …, P t P_{1},\ldots,P_{t} be the remaining parts, where t = p ​ r / 4 = Ω ⁡ ( r 1 / 4). t=pr/4=\Omega(r^{1/4}). By sweeping a vertical line from left to right, we can greedily pick subsets P i ′ ⊂ P i P^{\prime}_{i}\subset P_{i}, 1 ≤ i ≤ t 1\leq i\leq t, such that no vertical line intersects any two of the convex sets C i = conv ​ ( P i ′) C_{i}=\mbox{\rm conv}(P^{\prime}_{i}) and

 | | P i ′ | ≥ | P i | / t > Ω ⁡ ( N / r 5 / 4). |P^{\prime}_{i}|\geq|P_{i}|/t>\Omega(N/r^{5/4}). |  |

Without loss of generality, we can assume that the subsets P 1 ′, …, P t ′ P^{\prime}_{1},\ldots,P^{\prime}_{t} appear from left to right. That is, the x x -coordinate of each point in P i ′ P^{\prime}_{i} is less than the x x -coordinate of each point in P j ′ P^{\prime}_{j} for i < j i<j. Let Q Q be the t t -element point set obtained by selecting one point from each of the remaining P i ′ P^{\prime}_{i}. Then Q Q is in general position. By setting c 2 c_{2} sufficiently large, we have | Q | = t = p ​ r / 4 ≥ 4 2 ​ k |Q|=t=pr/4\geq 4^{2k}. By the Erdős–Szekeres cups-caps theorem ( 1), there is either a ( 2 ​ k) (2k) -cup or a ( 2 ​ k) (2k) -cap X ⊂ Q X\subset Q. We will assume that X X is a ( 2 ​ k) (2k) -cap, since a symmetric argument works otherwise. Let X = { x 1, …, x 2 ​ k } X=\{x_{1},\ldots,x_{2k}\} be the points of X X ordered from left to right and let us now assume that P i ′ P_{i}^{\prime} is the part that corresponds to the point x i ∈ X x_{i}\in X.

###### Observation 3.3.

If q 1 ∈ P 1 ′, …, q 2 ​ k ∈ P 2 ​ k ′ q_{1}\in P^{\prime}_{1},\ldots,q_{2k}\in P^{\prime}_{2k}, then q 1, …, q 2 ​ k q_{1},\ldots,q_{2k} forms a ( 2 ​ k) (2k) -cap.

###### Proof.

It suffices to show that every triple in { q 1, …, q 2 ​ k } \{q_{1},\ldots,q_{2k}\} forms a cap. For the sake of contradiction, suppose ( q i, q j, q s) (q_{i},q_{j},q_{s}) is a cup. Since ( x i, x j, x s) (x_{i},x_{j},x_{s}) is a cap, this implies that the convex sets conv ​ ( P i ′), conv ​ ( P j ′), conv ​ ( P s ′) \mbox{\rm conv}(P^{\prime}_{i}),\mbox{\rm conv}(P^{\prime}_{j}),\mbox{\rm conv}(P^{\prime}_{s}) can be pierced by a line, a contradiction. ∎

Set X ′ = { x 1, x 3, …, x 2 ​ k − 1 } X^{\prime}=\{x_{1},x_{3},\ldots,x_{2k-1}\}. Let T 1, …, T k T_{1},\ldots,T_{k} be the support of X ′ X^{\prime}. Then the k k parts P 2 ′, P 4 ′, …, P 2 ​ k ′ P^{\prime}_{2},P^{\prime}_{4},\ldots,P^{\prime}_{2k} must lie in T 1, …, T k T_{1},\ldots,T_{k}, respectively. Moreover, by setting c 1 c_{1} sufficiently large, each such part P 2 ​ i ′ P^{\prime}_{2i} satisfies

 | | P 2 ​ i ′ | ≥ Ω ⁡ ( N r 5 / 4) ≥ N 2 32 ​ k, |P^{\prime}_{2i}|\geq\Omega\left(\frac{N}{r^{5/4}}\right)\geq\frac{N}{2^{32k}}, |  |

as required. ∎

## 4 Big line or big convex polygon – Proof of Theorem 1.1

For the proof of Theorem 1.1, we will need the following more general version of Theorem 2.1. Let K K be a convex set in the plane. Then we say that the point set P P*avoids*K K if the line generated by any two points in P P is disjoint from K K. We say that K K and P P are ​ s ​ e ​ p ​ a ​ r ​ a ​ t ​ e ​ d \emph{separated} if there is a line that separates K K and conv ​ ( P) \mbox{\rm conv}(P). Suppose now that K K is a convex set in the plane, P P is a finite point set that avoids K K and K K and P P are separated. Then, given a subset X ⊂ P X\subset P, we say that X X is an *inner-cap*with respect to K K if, for each point x ∈ X x\in X, there is a line that separates x x from ( X ∖ { x }) ∪ K (X\setminus\{x\})\cup K. Similarly, we say that X ⊂ P X\subset P is an *outer-cup*with respect to K K if, for each point x ∈ X x\in X, there is a line that separates x ∪ K x\cup K from X ∖ { x } X\setminus\{x\}.

###### Theorem 4.1.

There is an absolute constant c > 0 c>0 such that the following holds. Let K K be a convex set in the plane and let P P be a finite point set in the plane that avoids K K. If K K and P P are separated and

 | | P | ≥ c ⁡ ( min ⁡ { m − 1, n − 1 } + ℓ) ⋅ ( m + n − 4 n − 2), |P|\geq c(\min\{m-1,n-1\}+\ell)\cdot{m+n-4\choose n-2}, |  |

then P P contains either ℓ \ell collinear points, an outer-cup with respect to K K of size m m or an inner-cap with respect to K K of size n n.

###### Proof.

Let | P | = N |P|=N. Without loss of generality, we can assume that the line L L which separates K K and P P is horizontal, that K K lies below L L and that P P lies above L L. By considering conv ​ ( K ∪ p) \mbox{\rm conv}(K\cup p) for each p ∈ P p\in P, we can radially order the elements in P = { p 1, …, p N } P=\{p_{1},\ldots,p_{N}\} with respect to K K in clockwise order, from left to right.

Notice that every triple in P P is either an inner-cap with respect to K K or an outer-cup with respect to K K. Moreover, for i < j < s < t i<j<s<t, if { p i, p j, p s } \{p_{i},p_{j},p_{s}\} and { p j, p s, p t } \{p_{j},p_{s},p_{t}\} are both inner-caps with respect to K K (outer-cups with respect to K K), then every triple in { p i, p j, p s, p t } \{p_{i},p_{j},p_{s},p_{t}\} is an inner-cap with respect to K K (outer-cup with respect to K K). Thus, by following the proof of Theorem 2.1 almost verbatim, the statement follows. ∎

We are now ready to prove Theorem 1.1.

###### Proof of Theorem 1.1.

Let P P be an N N -element planar point set in the plane, where N = ℓ 2 ⋅ 2 n + C ​ n ​ log ⁡ n N=\ell^{2}\cdot 2^{n+C\sqrt{n\log n}} with C C a sufficiently large absolute constant. We can assume that no two points in P P have the same x x -coordinate. Moreover, we can assume that there are no ℓ \ell collinear members in P P, since otherwise we would be done.

For the sake of contradiction, suppose P P does not contain n n points in convex position. Set k = 2 ​ ⌈ n ​ log ⁡ n ⌉ k=2\lceil\sqrt{n\log n}\rceil. We apply Theorem 3.1 to P P with parameter k + 3 k+3, obtaining a subset X = { x 1, …, x k + 3 } ⊂ P X=\{x_{1},\ldots,x_{k+3}\}\subset P such that X X is either a cup or a cap, where we assume that the points of X X appear in order from left to right. Moreover, the regions T 1, …, T k + 2 T_{1},\ldots,T_{k+2} in the support of X X satisfy

 | | T i ∩ P | ≥ N 2 32 ​ ( k + 3). |T_{i}\cap P|\geq\frac{N}{2^{32(k+3)}}. |  |

Set P i ⊂ T i ∩ P P_{i}\subset T_{i}\cap P to be the set of points of P P in the interior of T i T_{i}, for i = 1, …, k + 2 i=1,\ldots,k+2. Hence,

 | | P i | ≥ N 2 32 ​ ( k + 3) − 3 ​ ℓ ≥ N 2 40 ​ k. |P_{i}|\geq\frac{N}{2^{32(k+3)}}-3\ell\geq\frac{N}{2^{40k}}. |  |

We will now assume that X X is a cap, since a symmetric argument works in the other case.

Consider the subset P i ⊂ P P_{i}\subset P and the region T i T_{i} for some fixed i ∈ { 2, …, k + 1 } i\in\{2,\ldots,k+1\}. Let B i B_{i} be the segment x i − 1 ​ x i + 2 ¯ \overline{x_{i-1}x_{i+2}}. The point set P i P_{i} naturally comes with a partial order ≺ i \prec_{i}, where p ≺ i q p\prec_{i}q if p ≠ q p\neq q and p ∈ conv ​ ( B i ∪ q) p\in\mbox{\rm conv}(B_{i}\cup q). Note that p ≺ i q p\prec_{i}q if p p lies on the boundary of conv ​ ( B i ∪ q). \mbox{\rm conv}(B_{i}\cup q). Following Holmsen et al. [6], for each P i P_{i}, let

1. 1.

h i h_{i} be the size of the longest antichain with respect to ≺ i, \prec_{i},

2. 2.

v i v_{i} be the size of the longest chain with respect to ≺ i \prec_{i},

3. 3.

a i a_{i} be the size of the largest inner-cap with respect to x i + 1 x_{i+1} that is also a chain with respect to ≺ i \prec_{i},

4. 4.

b i b_{i} be the size of the largest inner-cap with respect to x i x_{i} that is also a chain with respect to ≺ i \prec_{i},

5. 5.

w i w_{i} be the size of the largest inner-cap with respect to B i B_{i} that is also an antichain with respect to ≺ i \prec_{i} and

6. 6.

z i z_{i} be the size of the largest outer-cup with respect to B i B_{i} that is also an antichain with respect to ≺ i \prec_{i}.

By Dilworth’s theorem [3], we have v i ​ h i ≥ | P i | v_{i}h_{i}\geq|P_{i}|. We also clearly have z i < n z_{i}<n. We now make the following observations.

###### Observation 4.2.

 | w 2 + w 4 + ⋯ + w k < n w_{2}+w_{4}+\cdots+w_{k}<n |  |

and

 | w 3 + w 5 + ⋯ + w k + 1 < n. w_{3}+w_{5}+\cdots+w_{k+1}<n. |  |

###### Proof.

Recall that k = 2 ​ ⌈ n ​ log ⁡ n ⌉ k=2\lceil\sqrt{n\log n}\rceil is even. Let us consider the sets P 2, P 4, …, P k P_{2},P_{4},\ldots,P_{k}. Suppose we have subsets S 2 ⊂ P 2, S 4 ⊂ P 4, …, S k ⊂ P k S_{2}\subset P_{2},S_{4}\subset P_{4},\ldots,S_{k}\subset P_{k} such that S i S_{i} is an antichain with respect to ≺ i \prec_{i}, an inner-cap with respect to B i B_{i} and satisfies | S i | = w i |S_{i}|=w_{i}. Then we claim that S = S 2 ∪ S 4 ∪ ⋯ ∪ S k S=S_{2}\cup S_{4}\cup\cdots\cup S_{k} is a cap and, therefore, in convex position. Let p ∈ S i p\in S_{i}. Then there is a line L L through p p that has the property that all of the other points in S i S_{i} lie below L L and L L does not intersect B i B_{i}. Since L L does not intersect B i B_{i}, all of the points in S ∖ { p } S\setminus\{p\} must lie below L L. But then, we must have that

 | w 2 + w 4 + ⋯ + w k = | S | < n, w_{2}+w_{4}+\cdots+w_{k}=|S|<n, |  |

as required. A similar argument works for the parts P 3, P 5, …, P k + 1 P_{3},P_{5},\ldots,P_{k+1} to prove the second inequality. ∎

By Observation 4.2, we have

 | w 2 + w 3 + ⋯ + w k + 1 < 2 ​ n. w_{2}+w_{3}+\cdots+w_{k+1}<2n. |  |

Let P i ′ ⊂ P i P^{\prime}_{i}\subset P_{i} be a chain with respect to ≺ i \prec_{i}. Clearly P i ′ P^{\prime}_{i} avoids x i x_{i} and x i + 1 x_{i+1}. Moreover, if P i ′ P^{\prime}_{i} contains an outer-cup with respect to x i x_{i}, then it must be an inner-cap with respect to x i + 1 x_{i+1}. Therefore, if | P i ′ | > f ℓ ​ ( m, n) |P^{\prime}_{i}|>f_{\ell}(m,n), then, by Theorem 4.1 applied to the convex set K = { x i } K=\{x_{i}\}, the set P i ′ P^{\prime}_{i} contains either an outer-cup with respect to x i x_{i} of size m m, which is an inner-cap with respect to x i + 1 x_{i+1} of size m m, or an inner-cap with respect to x i x_{i} of size n n. See Figure 4.

[image: Refer to caption] Figure 4: Four points in P i ′ P^{\prime}_{i} that form an outer-cup with respect to x i x_{i}, which is an inner-cap with respect to x i + 1 x_{i+1}.

###### Observation 4.3.

If there are subsets Y i − 1 ⊂ P i − 1 Y_{i-1}\subset P_{i-1} and Y i ⊂ P i Y_{i}\subset P_{i} such that Y i − 1 Y_{i-1} is a chain with respect to ≺ i − 1 \prec_{i-1} and an inner-cap with respect to x i x_{i} and Y i Y_{i} is a chain with respect to ≺ i \prec_{i} and an inner-cap with respect to x i x_{i}, then Y i − 1 ∪ Y i Y_{i-1}\cup Y_{i} is in convex position.

###### Proof.

It suffices to show that every four points in Y i − 1 ∪ Y i Y_{i-1}\cup Y_{i} are in convex position. If all four points lie in Y i Y_{i}, then they are in convex position. Likewise, if they all lie in Y i − 1 Y_{i-1}, they are again in convex position. Suppose we take two points p 1, p 2 ∈ Y i − 1 p_{1},p_{2}\in Y_{i-1} and two points p 3, p 4 ∈ Y i p_{3},p_{4}\in Y_{i}. Since Y i − 1 Y_{i-1} and Y i Y_{i} are both chains with respect to ≺ i − 1 \prec_{i-1} and ≺ i \prec_{i} respectively, the line spanned by p 1, p 2 p_{1},p_{2} does not intersect the region T i T_{i} and the line spanned by p 3, p 4 p_{3},p_{4} does not intersect the region T i − 1 T_{i-1}. Hence, p 1, p 2, p 3, p 4 p_{1},p_{2},p_{3},p_{4} are in convex position. Now suppose we have p 1, p 2, p 3 ∈ Y i − 1 p_{1},p_{2},p_{3}\in Y_{i-1} and p 4 ∈ Y i p_{4}\in Y_{i}. Since the three lines L 1, L 2, L 3 L_{1},L_{2},L_{3} spanned by p 1, p 2, p 3 p_{1},p_{2},p_{3} all intersect the segment B i − 1 B_{i-1}, both x i x_{i} and p 4 p_{4} lie in the same region in the arrangement of L 1 ∪ L 2 ∪ L 3 L_{1}\cup L_{2}\cup L_{3}. Therefore, p 1, p 2, p 3, p 4 p_{1},p_{2},p_{3},p_{4} are in convex position. The same argument works for the case where p 1 ∈ Y i − 1 p_{1}\in Y_{i-1} and p 2, p 3, p 4 ∈ Y i p_{2},p_{3},p_{4}\in Y_{i}. See Figure 5. ∎

[image: Refer to caption] Figure 5: An inner-cap of size 3 with respect to x i x_{i} in P i − 1 ′ P^{\prime}_{i-1} and an inner-cap of size 4 in P i ′ P^{\prime}_{i} with respect to x i x_{i}, which gives 7 points in convex position.

By Observation 4.3, we have a i + b i + 1 < n a_{i}+b_{i+1}<n for all i i. By applying Theorem 4.1 with K = { x i } K=\{x_{i}\}, we have v i ≤ f ℓ ​ ( a i + 1, b i + 1) < c ⁡ ( ℓ + n) ​ ( a i + b i − 2 a i − 1) v_{i}\leq f_{\ell}(a_{i}+1,b_{i}+1)<c(\ell+n){a_{i}+b_{i}-2\choose a_{i}-1}. Likewise, by applying Theorem 4.1 with K = B i K=B_{i}, we have h i ≤ f ℓ ​ ( w i + 1, z i + 1) < c ⁡ ( ℓ + n) ​ ( w i + z i − 2 w i − 1) h_{i}\leq f_{\ell}(w_{i}+1,z_{i}+1)<c(\ell+n){w_{i}+z_{i}-2\choose w_{i}-1}. Putting everything together, we obtain

 | N k 2 40 ​ k 2 \displaystyle\frac{N^{k}}{2^{40k^{2}}} | ≤ \displaystyle\leq | ∏ i = 2 k + 1 | P i | \displaystyle\prod\limits_{i=2}^{k+1}|P_{i}| |  |

 |  | ≤ \displaystyle\leq | ∏ i = 2 k + 1 v i ​ h i \displaystyle\prod\limits_{i=2}^{k+1}v_{i}h_{i} |  |

 |  | ≤ \displaystyle\leq | ∏ i = 2 k + 1 c 2 ​ ( ℓ + n) 2 ​ ( a i + b i − 2 a i − 1) ​ ( w i + z i − 2 w i − 1) \displaystyle\prod\limits_{i=2}^{k+1}c^{2}(\ell+n)^{2}\binom{a_{i}+b_{i}-2}{a_{i}-1}\binom{w_{i}+z_{i}-2}{w_{i}-1} |  |

 |  | < \displaystyle< | ∏ i = 2 k + 1 c 2 ​ ( ℓ + n) 2 ​ 2 a i + b i ​ ( 2 ​ n) w i \displaystyle\prod\limits_{i=2}^{k+1}c^{2}(\ell+n)^{2}2^{a_{i}+b_{i}}(2n)^{w_{i}} |  |

 |  | < \displaystyle< | ( c 2 ​ ( ℓ + n)) 2 ​ k ​ 2 ( k + 1) ​ n + 2 ​ n ​ log ⁡ ( 2 ​ n), \displaystyle(c^{2}(\ell+n))^{2k}2^{(k+1)n+2n\log(2n)}, |  |

where c c is the absolute constant from Theorem 4.1. Therefore, we have

 | N < c 2 ​ ( ℓ + n) 2 ​ 2 n + 3 ​ ( n / k) ​ log ⁡ ( 2 ​ n) + 40 ​ k. N<c^{2}(\ell+n)^{2}2^{n+3(n/k)\log(2n)+40k}. |  |

Since k = 2 ​ ⌈ n ​ log ⁡ n ⌉ k=2\lceil\sqrt{n\log n}\rceil, this gives us

 | N < ℓ 2 ⋅ 2 n + O ⁡ ( n ​ log ⁡ n). N<\ell^{2}\cdot 2^{n+O(\sqrt{n\log n})}. |  |

Since | P | = N = ℓ 2 ⋅ 2 n + C ​ n ​ log ⁡ n |P|=N=\ell^{2}\cdot 2^{n+C\sqrt{n\log n}}, by setting C C sufficiently large, we have a contradiction.∎

Acknowledgements. This research was initiated during a visit to the American Institute of Mathematics under their SQuaREs program.

## References

- [1] J. Beck, On the lattice property of the plane and some problems of Dirac, Motzkin and Erdős in combinatorial geometry, Combinatorica 3 (1983), 281–297.
- [2] T. M. Chan, Optimal partition trees, Discrete Comput. Geom. 47 (2012), 661–690.
- [3] R. P. Dilworth, A decomposition theorem for partially ordered sets, Ann. of Math. 51 (1950), 161–166.
- [4] P. Erdős and G. Szekeres, A combinatorial problem in geometry, Compos. Math. 2 (1935), 463–470
- [5] P. Erdős and G. Szekeres, On some extremum problems in elementary geometry, Ann. Univ. Sci. Budapest. Eötvös Sect. Math. 3-4 (1960/1961), 53–62.
- [6] A. Holmsen, H. N. Mojarrad, J. Pach and G. Tardos, Two extensions of the Erdős–Szekeres problem, J. Eur. Math. Soc. 22 (2020), 3981–3995
- [7] J. Matoušek, Efficient partition trees, *Discrete Comput. Geom.*8 (1992), 315–334.
- [8] G. Moshkovitz and A. Shapira, Ramsey theory, integer partitions and a new proof of the Erdős–Szekeres theorem, Adv. Math. 262 (2012), 1107–1129.
- [9] J. Pach and J. Solymosi, Canonical theorems for convex sets, Discrete Comput. Geom. 19 (1998), 427–435.
- [10] A. Pór and P. Valtr, The partitioned version of the Erdős–Szekeres theorem, Discrete Comput. Geom. 28 (2002), 625–637.
- [11] A. Suk, On the Erdős–Szekeres convex polygon problem, J. Amer. Math. Soc. 30 (2017), 1047–1053.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
