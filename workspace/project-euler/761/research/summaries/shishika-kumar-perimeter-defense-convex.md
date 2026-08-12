> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/shishika-kumar-perimeter-defense-convex.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/1909.03989 | converted from PDF -->

## What it claims

This paper studies a variant of multi-player reach-avoid game played between intruders and defenders. The intruder team
tries to score by sending as many intruders as possible to the target area, while the defender team tries to minimize this score
by intercepting them. Speciﬁcally, we consider the case where the defenders are constrained to move on the perimeter of the
target area. Since it is challenging to directly solve the multi-player game due to the high dimensionality of the joint state
space, we leverage the solutions to smaller scale problems. First, we solve the one vs. one game, for which existing works
either rely on numerical approaches or make simplifying assumptions (e.g., circular perimeter, or equal speed). This paper
accommodates target areas with any arbitrary convex shapes and provides analytical solution which lends itself to a useful
geometric interpretation. We also provide a detailed discussion on the optimality of the derived strategies. Secondly, we solve
the two vs. one game to introduce a cooperative pincer maneuver, where a pair of defenders team up to…

## Statements it makes

Lemma 1 If the initial conﬁguration is such that xA ∈
RA(sD) (i.e., V > 0), then regardless of the defender

Lemma 1 only gives a suﬃcient condition for the intruder
to win. To prove that it is also a necessary condition,
we show that the defender wins if the game starts in a
conﬁguration xA /∈ RA(sD).

Lemma 2 When xA(t0) ∈ Γaﬀ(sD(t0)), then for any
intruder control strategy, the defender can maintain the
condition xA(t) ∈ Γaﬀ(sD(t)) for all t > t0 using the
following control:

Lemma 3 Let RD(sD) denote the complement of
RA(sD). If the initial condition is xA ∈ RD(sD), i.e.,
xA /∈ RA(sD), then regardless of the intruder strategy,
the defender wins the game of kind using ω∗
D in (18):
i.e., the defender either captures the intruder or prevents
it from scoring indeﬁnitely.

Theorem 1 The zero level set of V (sD, xA) deﬁned in
(14) gives the barrier of the game of kind.

Algorithm 2 Determining region (1 vs. 1)
1: Input: sD, xA, γ, and ν
2: Compute sL and sR using Alg. 1
3: J ∗
L ← JL(sL; sD, xA) using (2)
4: J ∗
R ← JR(sR; sD, xA) using (9)
5: if any of the conditions in (14) is true then
6: is in Left ← T rue
7: else
8: is in Left ← F alse
9: end if
10: Return: is in Left

Algorithm 3 Intruder control (1 vs. 1)
1: Input: sD, xA, γ, and ν
2: Compute sL and sR using Alg. 1
3: Determine the region (i.e., is in left) using Alg. 2
4: if is in left = T rue then
5: u∗
A ← ν ˆxA/L
6: else
7: u∗
A ← ν ˆxA/R
8: end if
9: Return: u
∗
A

Algorithm 4 Defender control (1 vs. 1)
1: Input: sD, xA, γ, and ν
2: Determine the region (i.e., is in left) using Alg. 2
3: if is in left = T rue then
4: ω∗
D ← 1
5: else
6: ω∗
D ← −1
7: end if
8: Return: ω∗
D
 3.3 Optimality of the Strategies

Theorem 2 If the initial conﬁguration satisﬁes xA ∈
RA(sD), and if the players use P1 in (21) as the objective
function, then u
∗
A in (16) and ω∗
D in (18) form an equi-
librium, and the value of the game is V (sD, xA) in (14):

Theorem 3 If the initial conﬁguration is xA /∈ RA(sD),
and if the players use P2 in (24) as the objective function,
then u
∗
A in (16) and ω∗
D in (18) form equilibrium strate-
gies, and the value of the game is V (sD, xA) in (14):

Theorem 4 (from [39]) For a circular perimeter, the
optimal strategies are

Lemma 4 If the initial conﬁguration satisﬁes xA(t0) ∈
RC(sDi(t0), sDj (t0)), then regardless of the defender’s
strategy, the intruder wins the game of kind using u
∗
A
deﬁned in (35).

Lemma 5 If the initial conﬁguration satisﬁes xA ∈
Rpair(sDi, sDj ), and if the defender pair uses a pin-
cer movement, [ωDi, ωDj ] = [1, −1], then either
xA ∈ RD(sDi) or xA ∈ RD(sDj ) occurs before the in-
truder reaches the perimeter: i.e., the defender pair wins.

Theorem 5 The zero level set of Vij deﬁned in (37)
gives the barrier of the game of kind played between two
defenders and one intruder.

Theorem 6 If the initial conﬁguration is xA ∈
RC(sDi, sDj ), and if the…

Alg…


*[further statements in the full text]*

*[digest of a 140124 character source; every section, statement, and proof in full at `research/sources/shishika-kumar-perimeter-defense-convex.full.md`]*
