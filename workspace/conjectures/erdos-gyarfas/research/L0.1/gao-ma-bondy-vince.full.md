<!-- source: https://arxiv.org/pdf/1902.05701 | converted from PDF -->

arXiv:1902.05701v2  [math.CO]  23 Jul 2019
On a conjecture of Bondy and Vince

Jun Gao∗ Jie Ma†

School of Mathematical Sciences
University of Science and Technology of China
Hefei, Anhui 230026, China.

Abstract

Twenty years ago Bondy and Vince conjectured that for any nonnegative integer k,
except ﬁnitely many counterexamples, every graph with k vertices of degree less than
three contains two cycles whose lengths diﬀer by one or two. The case k ≤ 2 was proved
by Bondy and Vince, which resolved an earlier conjecture of Erd˝os et. al.. In this paper
we conﬁrm this conjecture for all k.

The study on cycles has been extensive in the literature and various problems on the

existence of cycles with speciﬁed lengths were investigated decades ago (e.g., Erd˝os [2, 3]).

One such question, proposed by Erd˝os et. al. (see the discussion in [1]), asked whether every
graph with minimum degree at least three contains two cycles whose lengths diﬀer by one

or two. This was answered aﬃrmatively by Bondy and Vince [1] in the following stronger
theorem: with the exception of K1 and K2, every graph having at most two vertices of

degree less than three contains two cycles of lengths diﬀering by one or two. They further

conjectured the following generalization. (All graphs referred here are simple.)

Conjecture. (Bondy and Vince [1]) Let k be any nonnegative integer. With ﬁnitely many

exceptions, every graph having at most k vertices of degree less than three has two cycles
whose lengths diﬀer by one or two.

The authors of [1] remarked that they can also prove for k = 3 (with twelve exceptions)
and the case k = 4, 5 likely can be solved using their analysis. We mention that the theorem

in [1] was generalized in another direction by Fan [4]. For related topics, results and open

problems, we refer interested readers to [6, 7, 8, 10, 11] and their references.

∗Email: gj0211@mail.ustc.edu.cn.
†Email: jiema@ustc.edu.cn. Research supported in part by NSFC grants 11501539 and 11622110 and
Anhui Initiative in Quantum Information Technologies grant AHY150200.

1

In this paper, we conﬁrm the above conjecture of Bondy and Vince by the following.

Theorem. Every graph, having at most k vertices of degree less than three and at least

5k2 vertices, contains two cycles whose lengths diﬀer by one or two.

This also can be viewed as a resilience type answer to the above question of Erd˝os et.

al.. Let G be an n-vertex graph with minimum degree at least three. Then one can derive
that by deleting any √
n/5 edges from G, the remaining graph still contains two cycles of

lengths diﬀering by one or two. Also by repeating the following procedure: ﬁrst apply this
theorem to ﬁnd a pair of two cycles of lengths diﬀering by one or two and then delete two

edges to destroy these two cycles, one can in fact ﬁnd Ω(
√n) such pairs of cycles in G.

For the proof, we will need a lemma of Bondy and Vince [1] (the proof of which uses an
argument based on Thomassen and Toft [9]). Let C be a cycle in a graph G. A bridge of

C is either a chord of C or a subgraph of G obtained from a component B in G − V (C) by

adding all edges between B and C. We call vertices of the bridge not in C internal.

Lemma. ([1]) Let G be a 2-connected graph, not a cycle, and let C be an induced cycle

in G some bridge B of which has as many internal vertices as possible. Then either B is
the only bridge of C, or else that B is a bridge containing exactly two vertices u, v in V (C)

and every other bridge of C is a path from u to v.

We are ready to present the proof of our result.

Proof of Theorem. Throughout this proof, let B(G) denote the set of all vertices with
degree at most two in a graph G, and we say a pair of cycles is good if their lengths diﬀer

by one or two. Let f (1) = f (2) = 3, f (3) = 14, f (4) = 56, f (5) = 116 and f (k) = 5k2 for

k ≥ 6 so that {f (k) − f (k − 1)} is strictly increasing and

f (k) ≥ f (k − 1) + 7k + f (3) holds for all k ≥ 4. (1)

We will prove by induction on k that every graph G with |B(G)| ≤ k and at least f (k)
vertices contains a good pair of cycles. The case k ≤ 2 follows by the aforementioned

theorem of Bondy and Vince [1], so we may assume that k ≥ 3 and the statement holds for
any integer ℓ < k.

We begin by showing some useful facts on graphs H with |B(H)| = k. For a subgraph

F of H, by H − F we denote the graph obtained from H by deleting all vertices of F .

Claim 1. Let H be a graph with |B(H)| = k, minimum degree δ(H) ≥ 2 and no good pair

of cycles. If k = 3 or k ≥ 4 and |V (H)| ≥ f (k − 1) + f (3), then H is 2-connected.

Proof. First we show that H is connected. Otherwise, there exist at least two components

of H. Let D1 be one of the components of H and let D2 = H − D1. Let j = |B(D1)|. So

2

|B(D2)| = k − j. Since δ(H) ≥ 2, we see |V (Di)| ≥ 3 for each i ∈ [2]. By the theorem of
Bondy and Vince, we may assume that 3 ≤ j ≤ k − 3. Since {f (k) − f (k − 1)} is strictly

increasing, |V (D1)| + |V (D2)| = |V (H)| ≥ f (k − 1) + f (3) ≥ f (j) + f (k − j). So either
|V (D1)| ≥ f (j) or |V (D2)| ≥ f (k − j). By induction, in either case we can ﬁnd a good pair

of cycles. This shows that H is connected.

Suppose that there exists a cut-vertex u in H. Let B1 be a component of H − {u} and
B2 = H − {u} − B1. For i ∈ [2], let bi = |B(H) ∩ Bi|. It is clear that k − 1 ≤ b1 + b2 ≤ k.

We also have bi ≥ 2. Indeed, otherwise say some bi ≤ 1, then Hi = H[Bi ∪ {u}] is a graph
with at least three vertices (since δ(H) ≥ 2) and at most two vertices of degree less than

three; by the theorem of Bondy and Vince, it contains a good pair of cycles (so does H), a

contradiction. This already proves for k = 3 (as it is impossible to have b1 + b2 ≥ 4). Now
we consider k ≥ 4. Since Hi contains no good pair of cycles and |B(Hi)| ≤ bi + 1 ≤ k − 1, by

induction we have f (b1 + 1) + f (b2 + 1) > |V (H1)| + |V (H2)| > |V (H)| ≥ f (k − 1) + f (3) =

max2≤s≤k/2{f (s + 1) + f (k − s + 1)}1, again a contradiction. This ﬁnishes the proof.

A cycle C in a graph H is called feasible if it is induced and H − C is connected.

Claim 2. Let H be a 2-connected graph with |B(H)| = k and no good pair of cycles. If

|V (H)| ≥ f (k − 1) + 1, then there exists a feasible cycle in H.

Proof. We see that H is not a cycle. Let C be an induced cycle in H such that some bridge

B of C has the maximum number of internal vertices. If B is the only bridge of C, then
C is feasible in H and we are home. Therefore, by Lemma we may assume that B is a

bridge containing exactly two vertices u, v ∈ V (C) and there exists another bridge P of C

which is a path from u to v. Let P = v0...vt with u = v0 and v = vt, where we have t ≥ 2,
dH (u) ≥ 4 and dH(v) ≥ 4. Let R = H − {v1}. Then |V (R)| ≥ f (k − 1) and |B(R)| ≤ k − 1.

By induction, R (and thereby H) has a good pair of cycles, a contradiction.

For F, F ′ ⊆ H, let NF (F ′) be the set of vertices in F adjacent to some vertex in F ′.

Claim 3. Let H be a 2-connected graph with |B(H)| = k and no good pair of cycles, whose
order is at least f (2) + 4 for k = 3 and at least f (k − 1) + f (3) + 2k for k ≥ 4. Let C be any

feasible cycle in H and let A = NC(H − C). Then C has length at most 2k and divisible by

four, whose vertices alternate between A and B(H) ∩ V (C).

Proof. Let C = u1u2...uru1. First we show that there is no pair ui, ui+⌊r/2⌋+1 ∈ A where
the subscript is modulo r. Otherwise, there exists a path P with endpoints ui, ui+⌊r/2⌋+1
and all internal vertices in H − C, which together with the two segments of C between

ui and ui+⌊r/2⌋+1 form a good pair of cycles in H. This also implies that |A| ≤ |C|/2.

1Here the equality follows from the fact that f (k) − f (k − 1) is increasing.

3

Now suppose that |A| < |C|/2. Since C is induced, we see that V (C) is partitioned into A
and B(H) ∩ V (C). Let H ′ be obtained from H by deleting B(H) ∩ V (C). Then |B(H ′)| ≤

k − |B(H) ∩ V (C)| + |A| ≤ k − 1 and, as |B(H) ∩ V (C)| ≤ k, we have |V (H ′)| ≥ |V (H)| − k ≥
f (k − 1). By induction, H ′ contains a good pair of cycles, a contradiction. So |A| =

|B(H) ∩ V (C)| = |C|/2 and C is an even cycle of length at most 2k. Let r = 2s.

Suppose there exist two consecutive vertices in C, say u1, u2, belonging to A. As noted
above there is no ui, ui+s+1 ∈ A for any i. So us, us+1, us+2, us+3 are not in A and the pair

ui, ui+s+1 for any 3 ≤ i ≤ s − 1 has at most one vertex in A, which together imply that
|A| ≤ s − 1, a contradiction. This shows that no two consecutive vertices of C can be in A

and thus the vertices of C alternate between A and B(H) ∩ V (C). Finally let us note that r

is divisible by four, as otherwise s is odd, so if ui ∈ A then ui+s+1 ∈ A, a contradiction.

Claim 4. Let H, C, A be from Claim 3. Let D = {v ∈ V (C)| dH (v) ≤ 3} and A′ =

B(H − D) \ B(H). Then |V (C)\D| ≤ 1, |A| = |A′| = |C|/2 with A ∩ A′ = V (C)\D, and
every vertex in A − V (C)\D is adjacent to a unique vertex in A′ − V (C)\D; moreover,

H − D is 2-connected with |B(H − D)| = |B(H)|.

Proof. Suppose that there are two vertices say uj, uj+t ∈ V (C)\D. So uj, uj+t ∈ A have

degree at least four in H, t ∈ [2, k] is even and we may assume that dH(uj+i) ≤ 3 for all

1 ≤ i ≤ t − 1. Let H ′ be obtained from H by deleting S = {uj+1, ..., uj+t−1}. By Claim 3
we have B(H ′) ≤ k − |S ∩ B(H)| + |S ∩ A| = k − 1 and |V (H ′)| ≥ |V (H)| − k ≥ f (k − 1), so

H ′ has a good pair of cycles. This contradiction proves that |V (C)\D| ≤ 1. Let |C| = 2s.
Consider H − D. We have that |V (H − D)| is at least f (2) for k = 3 (by Claim 3, |D| ≤

|C| = 4) and is at least f (k−1)+f (3) for k ≥ 4, and B(H −D) = (B(H)−B(H)∩V (C))∪A′.

So |B(H − D)| = k − s + |A′|. First we see |A′| ≥ s; as otherwise |B(H − D)| ≤ k − 1 and
by induction H − D has a good pair of cycles. If V (C)\D = ∅, then there are exactly

|A| = s edges between C and H − C, so the deletion of D = V (C) will result in at most s
new vertices of degree at most two, that is |A′| ≤ s. Therefore in this case, |A′| = s = |A|

and A ∪ A′ induces a matching of size s in H. Now suppose V (C)\D = {u}. There are

exactly s − 1 edges between D and H − C, so the deletion of D will result in at most s − 1
new vertices of degree at most two in H − C, which, plus possibly u ∈ A′ (if and only if

dH (u) = 4), show that |A′| ≤ s. Therefore, again we have |A′| = s = |A|; in fact dH(u) = 4,

A ∩ A′ = {u} and A ∪ A′ − {u} induces a matching of size s − 1 in H.
The above analysis also demonstrates that every vertex in A′ has degree two in H − D

and thus δ(H − D) ≥ 2. By Claim 1, H − D is 2-connected. This ﬁnishes the proof.

Let G0 be a graph with |B(G0)| = k and at least f (k) vertices. Suppose for a contra-

diction that G0 has no good pair of cycles.
 4

We will deﬁne a sequence of subgraphs G0 ⊇ G1 ⊇ ... ⊇ Gm. First we show there exists
a 2-connected G1 ⊆ G0 with |B(G1)| = k and |V (G1)| ≥ f (k) − k. Let S be the set of

vertices of degree at most one in G0 and let G1 = G0 −S. Then |B(G1)| ≤ |B(G0)|−|S|+|S′|
where S′ denotes the set of vertices in G1 adjacent to S (so clearly |S′| ≤ |S|). We must

have |B(G1)| = k; otherwise, |B(G1)| ≤ k − 1 and |V (G1)| ≥ f (k) − k ≥ f (k − 1), implying a

good pair of cycles in G1 ⊆ G0. This shows that S ∪ S′ induces a matching of size |S| in G0
and every vertex in S′ is in B(G1)\B(G0). Therefore δ(G1) ≥ 2. As |V (G1)| ≥ f (k) − k ≥

f (k − 1) + f (3) for k ≥ 4, by Claim 1 we conclude that G1 is 2-connected.
Now suppose we have deﬁned Gi for some i ≥ 1. If Gi is 2-connected with |B(Gi)| = k

and of order at least f (2) + 4 for k = 3 and at least f (k − 1) + f (3) + 2k for k ≥ 4, then

• let Ci be a feasible cycle in Gi (by Claim 2), with the preference to be a four-cycle,

• let Ai = NCi(Gi − Ci), and further

• let Di = {v ∈ V (Ci)| dGi(v) ≤ 3}, Gi+1 = Gi − Di and A′
i = B(Gi+1) \ B(Gi).

Otherwise we terminate. Let G0 ⊇ G1 ⊇ ... ⊇ Gm be the sequence of subgraphs we obtain

as above. Then we can apply Claims 3 and 4 for Gi, Ci, Ai for each 1 ≤ i ≤ m − 1. In

particular, we see that Gi for all 1 ≤ i ≤ m is 2-connected with |B(Gi)| = k. So the reason
we terminate at Gm is because the order of Gm is at most f (2) + 3 for k = 3 and at most

f (k − 1) + f (3) + 2k − 1 for k ≥ 4. By (1), this implies that ∑m−1
i=1 |Di| = |V (G1)| − |V (Gm)|

is at least 5 for k = 3 and at least (f (k) − k) − (f (k − 1) + f (3) + 2k − 1) > 4k for k ≥ 4.
In what follows, we will investigate properties on the cycles C1, ..., Cm−1, which eventu-

ally will lead a contradiction to the above lower bound of ∑m−1
i=1 |Di|.
We ﬁrst show that if A′
i ̸⊆ B(Gi+1)∩V (Ci+1), then Ci+1 is a feasible cycle in Gi. Clearly

we have A′
i ∩ Ai+1 = ∅ (as any vertex in A′
i has degree two in Gi+1, while vertices in Ai+1
have degree at least three in Gi+1). Note that V (Ci+1) is partitioned into B(Gi+1)∩V (Ci+1)
and Ai+1. So A′
i ̸⊆ B(Gi+1) ∩ V (Ci+1) implies that A′
i intersects with Gi+1 − Ci+1. By

Claim 4, we see that any vertex in A′
i is adjacent to Di, so Gi+1 − Ci+1 is adjacent to Di.

Therefore, Gi − Ci+1 is connected and thus Ci+1 is feasible in Gi.
We now assert that there exists some t such that |C1| = ... = |Ct| = 4 and |Ci| ≥ 8 for

each t + 1 ≤ i ≤ m − 1. By Claim 3 each |Ci| is divisible by four, so it suﬃces to prove that
if |Ci| ≥ 8, then |Ci+1| ≥ 8. Suppose this is not true. Then |Ci+1| = 4 < |Ci|, implying that

|A′
i| = |Ci|/2 > |Ci+1|/2 = |B(Gi+1) ∩ V (Ci+1)|. So Ci+1 is a feasible cycle (of length four)

in Gi. But this contradicts our preference for choosing Ci in Gi, ﬁnishing the proof.
Next we claim that for each 1 ≤ i ≤ t−1, Ci+1 is feasible in Gi. We have |Ci| = |Ci+1| =

4. So |A′
i| = 2 = |B(Gi+1) ∩ V (Ci+1)|. If A′
i = B(Gi+1) ∩ V (Ci+1), then this will give two

possible conﬁgurations between Ci and Ci+1 and in each case we can ﬁnd a good pair of

5

cycles easily (of lengths 4 and 5, or 4 and 6). So we may assume A′
i ̸= B(Gi+1) ∩ V (Ci+1).
Therefore, Ci+1 is a feasible cycle in Gi.

We also claim that for each i ≥ t + 1, Ci+1 is feasible in Gi. Let Ci = u0u1...us−1u0
where s ≥ 8. So |Ai| = |A′
i| ≥ 4. By Claims 3 and 4, we may assume that u0, u2, u4 ∈

Ai −V (Ci)\Di and x, y, z ∈ A′
i −V (Ci)\Di with u0x, u2y, u4z ∈ E(Gi). We may also assume

that x, y, z ∈ A′
i ⊆ B(Gi+1) ∩ V (Ci+1) (as otherwise, Ci+1 is feasible in Gi). Let P denote
one of the two segments of Ci+1 between x and y with |E(P )| ≥ |Ci+1|/2. Clearly |E(P )| ≥ 4

is even. If |E(P )| ≡ 2 mod 4, then C ′ = P ∪ xu0u1u2y forms a cycle in Gi whose length
is 2 mod 4 and thus is at least 10. Then there exist two vertices a, b ∈ V (P ) ∩ Ai+1 which

divide the cycle C ′ into two segments of lengths diﬀering by two. Also there exists a path

with endpoints a, b and all internal vertices in Gi+1 − Ci+1, which is internally disjoint from
C ′. Putting the above together, we ﬁnd a good pair of cycles in Gi. So |E(P )| ≡ 0 mod 4.

Similarly any segment of Ci+1 between y and z has length 0 mod 4. Therefore any segment

(say Q) of Ci+1 between x and z has length 0 mod 4 as well. Then Q ∪ xu0u1u2u3u4z forms
a cycle of length 2 mod 4. If |E(Q)| = 4, then Ci and (Ci − {u1, u2, u3}) ∪ u0x ∪ Q ∪ zu4
form a good pair of cycles (whose lengths diﬀer by two). So |E(Q)| ≥ 8. Again there exist
two vertices a, b ∈ V (Q) ∩ Ai+1 dividing the cycle Q ∪ xu0u1u2u3u4z into two segments of

lengths diﬀering by two. By similar arguments as above this enables us to ﬁnd a good pair

of cycles in Gi, proving the claim.
Finally we are completing the proof using the above two claims. We point out that for

each 1 ≤ i ≤ t − 1, Ci+1 and Ci play the same role in Gi. Repeatedly applying this, one

can conclude that in fact all four-cycles C1, C2, ..., Ct are feasible in G1. By Claims 3 and
4, each V (Ci)\Ai = B(G1) ∩ V (Ci) provides |Ci|/2 ≥ |Di|/2 distinct vertices in B(G1). So

t∑

i=1 |Di| ≤
 t∑

i=1 2|B(G1) ∩ V (Ci)| ≤ 2|B(G1)| ≤ 2k.

Similarly, Ct+1, Ct+2, ..., Cm−1 are feasible in Gt+1 and using this fact, we can derive that

m−1∑

i=t+1 |Di| ≤
 m−1∑

i=t+1 2|B(Gt+1) ∩ V (Ci)| ≤ 2|B(Gt+1)| ≤ 2k.

Putting the above together, we have ∑m−1
i=1 |Di| ≤ 4k, but we have seen that ∑m−1
i=1 |Di| > 4k
for k ≥ 4. This contradiction ﬁnishes the proof for the case k ≥ 4. For k = 3, by Claim 3,

all feasible cycles must be of length four, so t = m−1. And we obtained that ∑t
i=1 |Di| ≥ 5.

This tells that there are at least two four-cycles C1, C2, each providing two vertices in B(G1).
But it is impossible as 3 = |B(G1)| ≥ 4. The proof now is completed.

We didn’t make lots of eﬀorts to optimise the constant in the proof as we tend to believe
that the quadratic bound O(k2) can be further improved (perhaps, to a linear term O(k)).

6

To conclude this paper we would like to mention a conjecture of [7], which seems to be
a natural generalization for the question of Erd˝os et. al. and has implications (if true) for

other related problems: For any nonnegative integer k, every graph with minimum degree
at least k + 1 contains k cycles C1, ..., Ck with |Ci+1| = |Ci| + d for d ∈ {1, 2}.

Acknowledgement. We would like to thank the referees for their careful reading and
helpful suggestions.

Note added in proof. After this paper was submitted for publication, a proof to the

problem mentioned in the last paragraph was announced in [5].

References

[1] J. A. Bondy and A. Vince, Cycles in a graph whose lengths diﬀer by one or two, J.
Graph Theory 27 (1998), 11–15.

[2] P. Erd˝os, Some of my recent problems in combinatorial number theory, geometry and
combinatorics, in Graph Theory, Combinatorics and Algorithms, Vol. 1, Proc. Seventh

Quadrennial International Conference on the Theory and Applications of Graphs (Y.
Alavi and A. Schwenk, Eds.), pp. 335–349, Wiley, New York, 1995.

[3] P. Erd˝os, Some old and new problems in various branches of combinatorics, in Graphs
and Combinatorics (Marseille, 1995). Discrete Math. 165/166 (1997), 227–231.

[4] G. Fan, Distribution of cycle lengths in graphs, J. Combin. Theory Ser. B 84 (2002),
187–202.

[5] J. Gao, Q. Huo, C. Liu and J. Ma, A uniﬁed proof of conjectures on cycle lengths in
graphs, arXiv:1904.08126.

[6] R. H¨aggkvist and A. Scott, Arithmetic progressions of cycles, Technical Report No.
16 (1998), Matematiska Institutionen, Ume˚aUniversitet.

[7] C. Liu and J. Ma, Cycle lengths and minimum degree of graphs, J. Combin. Theory
Ser. B 128 (2018), 66–95.

[8] B. Sudakov and J. Verstra¨ete, Cycle lengths in sparse graphs, Combinatorica 28
(2008), 357–372.

[9] C. Thomassen and B. Toft, Non-separating induced cycles in graphs, J. Combin.
Theory Ser. B 31 (1981), 199–224.
 7

[10] J. Verstra¨ete, On arithmetic progressions of cycle lengths in graphs, Combin. Probab.
Comput. 9 (2000), 369–373.

[11] J. Verstra¨ete, Extremal problems for cycles in graphs, In Recent Trends in Combina-

torics, A. Beveridge et al. (eds.), The IMA Volumes in Mathematics and its Applica-

tions 159, 83–116, Springer, New York, 2016.

8
