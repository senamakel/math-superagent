<!-- source: https://www.stat.uchicago.edu/~yibi/teaching/stat317/2021/Lectures/Lecture9.pdf | converted from PDF -->

STAT253/317 Lecture 9

Yibi Huang

Chapter 5 Poisson Processes

Lecture 9 - 1

5.2 Exponential Distribution

Let X be of exponential distribution with rate λ: X ∼ Exp(λ).
▶ Density: fX (x) = λe−λx for x ≥ 0
▶ CDF: FX (x) = 1 − e−λx for x ≥ 0
▶ E(X ) = 1/λ, Var (X ) = 1/λ2

▶ If X1, . . . , Xn are i.i.d Exp(λ), then
Sn = X1 + · · · + Xn ∼ Gamma(n, λ), with density

fSn (x) = λe−λt (λt)n−1

(n − 1)!

Lecture 9 - 2

The Exponential Distribution is Memoryless (⋆ ⋆ ⋆ ⋆ ⋆)

P(X > t + s|X > t) = P(X > s)

Proof.
 P(X > t + s|X > t) = P(X > t + s and X > t)
P(X > t)

= P(X > t + s)
P(X > t)

= e−λ(t+s)

e−λt = e−λs = P(X > s)

Implication. If the lifetime of batteries has an Exponential
distribution, then a used battery is as good as a new one, as long
as it’s not dead!
 Lecture 9 - 3

Another Important Property of the Exponential

If X1, . . . , Xn are independent, Xi , ∼ Exp(λi ) for i = 1, . . . , n then

(i) min(X1, . . . , Xn) ∼ Exp(λ1 + · · · + λn), and

(ii) P
(Xj = min(X1, . . . , Xn)
) = λj
λ1 + · · · + λn
Proof of (i)

P(min(X1, . . . , Xn) > t) = P(X1 > t, . . . , Xn > t)

= P(X1 > t) . . . P(Xn > t) = e−λ1t · · · e−λnt

= e−(λ1+···+λn)t.
 Lecture 9 - 4

Proof of (ii)
 P
(Xj = min(X1, . . . , Xn)
)

= P(Xj < Xi for i = 1, . . . , n, i ̸= j)

= ∫ ∞

0 P(Xj < Xi for i ̸= j|Xj = t)λj e−λj tdt

= ∫ ∞

0 P(t < Xi for i ̸= j)λj e−λj tdt

= ∫ ∞

0 λj e−λj t ∏

i̸=j P(Xi > t)dt

= ∫ ∞

0 λj e−λj t ∏

i̸=j e−λi tdt

= λj
 ∫ ∞

0 e−(λ1+···+λn)tdt

= λj
λ1 + · · · + λn Lecture 9 - 5

Example 5.8: Post Oﬃce

▶ A post oﬃce has two clerks.
▶ Service times for clerk i ∼ Exp(λi ), i = 1, 2
▶ When you arrive, both clerks are busy but no one else waiting.
You will enter service when either clerk becomes free.
▶ Find E[T ], where T = the amount of time you spend in the
post oﬃce.

Solution. Let Ri = remaining service time of the customer with
clerk i, i = 1, 2.
▶ Note Ri ’s are indep. ∼ Exp(λi ), i = 1, 2 by the memoryless
property
▶ Observe T = min(R1, R2) + S where S is your service time
▶ Using the property of exponential distributions,

min(R1, R2) ∼ Exp(λ1+λ2) ⇒ E[min(R1, R2)] = 1
λ1 + λ2

Lecture 9 - 6

Example 5.8: Post Oﬃce (Cont’d)

As for your service time S, observe that

S ∼
 {
Exp(λ1) if R1 < R2
Exp(λ2) if R2 < R1 ⇒ E[S|R1 < R2] = 1/λ1
E[S|R2 < R1] = 1/λ2

Recall that P(R1 < R2) = λ1/(λ1 + λ2) So

E[S] = E[S|R1 < R2]P(R1 < R2) + E[S|R2 < R1]P(R2 < R1)

= 1
λ1 × λ1
λ1 + λ2 + 1
λ2 × λ2
λ1 + λ2 = 2
λ1 + λ2

Hence the expected amount of time you spend in the post oﬃce is

E[T ] = E[min(R1, R2)] + E[S]

= 1
λ1 + λ2 + 2
λ1 + λ2 = 3
λ1 + λ2 .

Lecture 9 - 7

5.3.1. Counting Processes

A counting process {N(t)} is a cumulative count of number of
events happened up to time t.

Deﬁnition.
A stochastic processes {N(t), t ≥ 0} is a counting process
satisfying

(i) N(t) = 0, 1, . . . (integer valued),

(ii) If s < t, then N(s) ≤ N(t).

(iii) For s < t, N(t) − N(s) = number of events that occur in the
interval (s, t].
 Lecture 9 - 8

Deﬁnition.
A process {X (t), t ≥ 0} is said to have stationary increments if for
any t > s, the distribution of X (t) − X (s) depends on s and t only
through the diﬀerence t − s, for all s < t.
That is, X (t + a) − X (s + a) has the same distribution as
X (t) − X (s) for any constant a.

Deﬁnition.
A process {X (t), t ≥ 0} is said to have independent increments if
for any s1 < t1 ≤ s2 < t2 ≤ . . . ≤ sk < tk , the random variable
X (t1) − X (s1), X (t2) − X (s2), . . . , X (tk ) − X (sk ) are independent,
i.e. the numbers of events that occur in disjoint time intervals are
independent.

Example. Simple random walk {Xn, n ≥ 0} is a process with
independent and stationary increment, since Xn = ∑n
k=0 ξk where
ξk ’s are i.i.d with P(ξk = 1) = p and P(ξk = −1) = 1 − p.

Lecture 9 - 9

Deﬁnition 5.1 of Poisson Processes

A Poisson process with rate λ > 0 {N(t), t ≥ 0} is a counting
process satisfying

(i) N(0) = 0,

(ii) For s < t, N(t) − N(s) is independent of N(s) (independent
increment)

(iii) For s < t, N(t) − N(s) ∼ Poi(λ(t − s)), i.e.,

P(N(t) − N(s) = k) = e−λ(t−s) (λ(t − s))k

k!

Remark: In (iii), the distribution of N(t) − N(s) depends on t − s
only, not s, which implies N(t) has stationary increment.

Lecture 9 - 10

Deﬁnition 5.3 of Poisson Processes
The counting process {N(t), t ≥ 0} is said to be a Poisson process
having rate λ, λ > 0, if
(i) N(0) = 0.
(ii) The process has stationary and independent increments.
(iii) P(N(h) = 1) = λh + o(h).
(iv) P(N(h) ≥ 2) = o(h).

Theorem 5.1 Deﬁnitions 5.1 and 5.3 are equivalent.
[Proof of Deﬁnitions 5.1 ⇒ Deﬁnition 5.3]
From Deﬁnitions 5.1, N(h) ∼ Poi(h). Thus

P(N(h) = 1) = λhe−λh = λh + o(h)

P(N(h) ≥ 2) = 1 − P(N(h) = 0) − P(N(h) = 1)

= 1 − e−λh − λhe−λh = o(h)

Proof of Deﬁnitions 5.3 ⇒ Deﬁnition 5.1:
See p.299-300 in textbook (p.315 in 10ed)
Lecture 9 - 11
