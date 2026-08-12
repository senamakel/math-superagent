> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/alexander-bishop-ghrist-capture-unbounded.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://www2.math.upenn.edu/~ghrist/preprints/convexcapture.pdf | converted from PDF -->

## What it claims

ABSTRACT. We introduce simple tools from geometric convexity to analyze capture-
type (or “Lion and Man”) pursuit problems in unbounded domains. The main result is
a necessary and sufﬁcient condition for eventual capture in equal-speed discrete-time
multi-pursuer capture games on convex Euclidean domains of arbitrary dimension and
shape. This condition is presented in terms of recession sets in unit tangent spheres.
The chief difﬁculties lie in utilizing the boundary of the domain as a constraint on the
evader’s escape route. We also show that these convex-geometric techniques provide
sufﬁcient criteria for pursuit problems in non-convex domains with a convex decom-
position.
 1. INTRODUCTION

Games of pursuit and evasion are among the oldest and most elegant problems in
game theory, osculating differential equations, control theory, differential geometry,
and graph theory. This paper focuses on global geometric features of capture-type
pursuit problems. The primary contribution is an introduction of tools from geometric
convexity which allow for results so general as to be…

1.1.…

## Statements it makes

Algorithm 1 P ′ = Radius(P, E′, O)

Lemma 7. For D ⊂ En convex, N 0 = R. Equivalently, x ∈ R if and only if H−x ⊃ N .

Lemma 8. For D ⊂ En convex, N lies in a closed hemisphere of Sn−1 if and only if D is
unbounded.

Theorem 9. The following are equivalent:

Proposition 10. The Boundedness Condition is a necessary condition for the existence of a
successful pursuit strategy.

Theorem 12. For any convex unbounded D, the pursuers win if (1) the Boundedness Condi-
tion holds and (2) [EPj] ∈ R for all j.

Lemma 15. Assume there is a single pursuer P , and that R ∪ U = Sn−1. Then the pursuer
wins following Radius if the Boundedness Condition holds.

Theorem 16. In the case of a single pursuer, if D contains a cone with central angle at least
π/4, then the Boundedness Condition guarantees capture via Radius.

Theorem 17. Discrete-time equal-speed capture on a convex domain D is achievable if and
only if the initial positions of the pursuers and evader satisfy the Boundedness Condition.

Lemma 18. If P t+1
j ̸= Et+1,
 |Ot
jP t
j |
2 + 1 < |Ot+1
j P t+1
j |
2.

Algorithm 2 (P ′, O′) = RotatingRadius(P, E′, O, D)

Lemma 19. cl Ct+1 ⊂ Ct for every t.

Corollary 20. Under the Boundedness Condition, if Qj ∈ (B0
j ∩ D), then the pursuers catch
the evader in time

Theorem 22. The Extended Boundedness Condition is sufﬁcient to ensure discrete-time equal-
speed capture on D.

*[digest of a 43701 character source; every section, statement, and proof in full at `research/sources/alexander-bishop-ghrist-capture-unbounded.full.md`]*
