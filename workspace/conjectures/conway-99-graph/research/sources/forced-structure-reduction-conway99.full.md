<!-- source: https://arxiv.org/html/2608.11211v1 | converted from HTML -->

A Forced-Structure Reduction and Verifiable Bounds for Conway’s 99-Graph

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY-NC-ND 4.0][2]

arXiv:2608.11211v1 [cs.AI] 13 Jul 2026

# A Forced-Structure Reduction and Verifiable Bounds for Conway’s 99-Graph

Aalok Thakkar
Vachani School of Advanced Computing
Ashoka University
Sonipat, India – 131029
thakkar@ashoka.edu.in

###### Abstract

Conway’s 99-graph problem asks whether a strongly regular graph with parameters srg ​ ( 99, 14, 1, 2) \mathrm{srg}(99,14,1,2) exists. We report a systematic, fully reproducible attack by an autonomous AI research agent, scored under the track’s partial-credit metric. Our verifiable contributions are: (1) an *exhaustive*proof that no circulant graph on ℤ / 99 \mathbb{Z}/99 satisfies more than 3366 / 4950 = 68.0 % 3366/4950=68.0\% of the constraints ( 33 33 of 49 49 difference-classes), with the same ceiling for the other abelian group of order 99 99; (2) a forced-structure reduction: λ = 1 \lambda=1 makes each neighbourhood a perfect matching and μ = 2 \mu=2 puts the outer vertices in bijection with non-matched neighbour-pairs, collapsing existence to a 12 12 -regular graph on 84 84 vertices, encoded for CP-SAT and *validated*by recovering the unique srg ​ ( 9, 4, 1, 2) \mathrm{srg}(9,4,1,2); (3) a validated prescribed-automorphism orbit-existence framework (fixed-point-free and single-fixed-point actions, checked on srg ​ ( 9, 4, 1, 2) \mathrm{srg}(9,4,1,2) and the Paley graph srg ​ ( 13, 6, 2, 3) \mathrm{srg}(13,6,2,3)), and (4) a best verified artifact at 69.43 % 69.43\%, with evidence that this is a robust frontier (fourteen distinct methods, none exceeding it) entangled with the open question, since any provable bound below 4950 4950 is a non-existence proof.

## 1 Introduction

A *strongly regular graph*srg ​ ( v, k, λ, μ) \mathrm{srg}(v,k,\lambda,\mu) is a k k -regular graph on v v vertices in which every adjacent pair has exactly λ \lambda common neighbours and every non-adjacent pair has exactly μ \mu. The parameter set ( 99, 14, 1, 2) (99,14,1,2) was identified by Biggs [3] and popularised by Conway, who offered a $1000 prize for a construction or a non-existence proof [18, 7]. The parameters pass every standard feasibility test (integral eigenvalues 14 ( 1), 3 ( 54), ( − 4) ( 44) 14^{(1)},3^{(54)},(-4)^{(44)}, the Krein conditions, the absolute bound [5, 4]), and it is known that such a graph cannot be vertex-transitive, which eliminates all standard algebraic constructions [6]. The problem is open.

Modern SAT, SMT, and CP-SAT solvers [8, 2, 14] have been applied across combinatorial and synthesis problems [9, 11, 15, 16, 17]; they are the main tools used below.

We attempt the conways-99-graph instance of the CAISc 2026 Verifiable Problems track [13]. The track scores a submitted 99 × 99 99\times 99 symmetric 0 / 1 0/1 matrix by the fraction of constraints satisfied: 99 99 degree constraints (row sums 14 14), one λ \lambda constraint per edge, and one μ \mu constraint per non-edge. As every unordered pair is an edge xor a non-edge, the denominator is fixed at 99 + ( 99 2) = 4950 99+\binom{99}{2}=4950, and a perfect score is a solution to the open problem. We attack the well-posed sub-question: *how high can the score be pushed, and what can be proved about it?*Per the track’s stated interest, we report how an AI agent navigated the problem. We are explicit that we neither construct the graph nor prove non-existence; our contributions are verifiable bounds, a validated reduction, a reusable framework, and the documented trajectory.

## 2 Problem, metric, and a non-obstruction

Let A A be the adjacency matrix and C = A 2 C=A^{2}, so C i ​ j C_{ij} counts common neighbours of i, j i,j. The strongly-regular conditions are equivalent to the single matrix identity A 2 + A − 12 ​ I = 2 ​ J A^{2}+A-12I=2J (with J J all-ones); the score counts how many of its 4950 4950 scalar instances hold.

For any 14 14 -regular graph, ∑ i < j C i ​ j = ∑ v ( deg ⁡ v 2) = 99 ​ ( 14 2) = 9009 \sum_{i<j}C_{ij}=\sum_{v}\binom{\deg v}{2}=99\binom{14}{2}=9009, while the targets sum to 693 ⋅ 1 + 4158 ⋅ 2 = 9009 693\cdot 1+4158\cdot 2=9009: *exactly equal*. The feasible spectrum fixes ∑ i < j C i ​ j 2 = 17325 \sum_{i<j}C_{ij}^{2}=17325, again matched by the targets. Thus first and second moments give no contradiction, which is precisely why the problem resists easy arguments. A practical corollary, which shapes every search below, is that near degree 14 14 the λ \lambda - and μ \mu -satisfaction are *coupled*: one cannot cheaply maximise μ \mu alone, because the common-neighbour budget is tight, so a high partial score forces genuine near-strong-regularity.

## 3 An exhaustive bound for circulant graphs

A circulant on ℤ / 99 \mathbb{Z}/99 is given by a symmetric connection set S = − S S=-S with | S | = 14 |S|=14; it is automatically 14 14 -regular. By vertex-transitivity, all pairs in a difference-class { d, − d } \{d,-d\} behave identically, so the score is 99 + 99 ⋅ ( satisfied difference-classes) 99+99\cdot(\text{satisfied difference-classes}), over 49 49 classes, where class d d is satisfied iff ( d ∈ S d\in S and the cyclic autocorrelation λ ​ ( d) = | S ∩ ( S + d) | = 1 \lambda(d)=|S\cap(S+d)|=1) or ( d ∉ S d\notin S and λ ​ ( d) = 2 \lambda(d)=2). A perfect circulant would be a ( 99, 14, 1, 2) (99,14,1,2) partial difference set, known not to exist [12]; we compute the best partial one.

###### Proposition 1 (Exhaustive)

Over all ( 49 7) = 85, 900, 584 \binom{49}{7}=85{,}900{,}584 symmetric connection sets, the maximum number of satisfied difference-classes is 33 33; the best circulant scores 99 + 99 ⋅ 33 = 3366 / 4950 = 68.0 % 99+99\cdot 33=3366/4950=68.0\%.

We verified Proposition 1 by complete enumeration with batched FFT autocorrelation ( ≈ 100 \approx 100 s on a laptop). An optimal set is S = { ± 1, ± 2, ± 4, ± 15, ± 27, ± 36, ± 45 } S=\{\pm 1,\pm 2,\pm 4,\pm 15,\pm 27,\pm 36,\pm 45\}, with degree 99 / 99 99/99, λ \lambda 198 / 693 198/693, μ \mu 3069 / 4158 3069/4158; the algebra concentrates non-edge common-neighbour counts at 2 2 ( μ \mu at 73.8 % 73.8\%, versus ≈ 27 % \approx 27\% for a random regular graph). The non-cyclic abelian group of order 99 99, ℤ 3 × ℤ 3 × ℤ 11 \mathbb{Z}_{3}\times\mathbb{Z}_{3}\times\mathbb{Z}_{11}, attains the same 33 / 49 33/49.

## 4 A forced-structure reduction, validated on srg ​ ( 9, 4, 1, 2) \mathrm{srg}(9,4,1,2)

Most of any srg ​ ( v, k, 1, 2) \mathrm{srg}(v,k,1,2) is forced. Fix a vertex 0 with N ​ ( 0) = { 1, …, k } N(0)=\{1,\dots,k\}. Since λ = 1 \lambda=1, each neighbour shares exactly one common neighbour with 0, so the first subconstituent N ​ ( 0) N(0) is a perfect matching [5]; fix it (WLOG) as ( 1, 2), ( 3, 4), … (1,2),(3,4),\dots. Since μ = 2 \mu=2 on non-edges ( 0, outer) (0,\text{outer}), every outer vertex has exactly two neighbours in N ​ ( 0) N(0); and since μ = 2 \mu=2 on inner non-edges and λ = 1 \lambda=1 on inner edges, the outer vertices are in bijection with the non-matched pairs of N ​ ( 0) N(0). Hence the inner–outer adjacency is *entirely forced*: the outer vertex labelled { a, b } \{a,b\} is adjacent to exactly inner a a and b b.

The sole unknown is the outer–outer graph: ( k − 2) (k{-}2) -regular on M = ( k 2) − k / 2 M=\binom{k}{2}-k/2 vertices, constrained by label-derived λ / μ \lambda/\mu conditions. With inner vertices 0, …, k − 1 0,\dots,k{-}1 and matching m ​ ( 2 ​ i) = 2 ​ i + 1 m(2i)=2i{+}1, the outer vertices are the non-matched pairs. For outer u, v u,v with labels P u, P v P_{u},P_{v} and s = | P u ∩ P v | ∈ { 0, 1 } s=|P_{u}\cap P_{v}|\in\{0,1\}: if u ∼ v u\sim v then the number of common outer neighbours equals 1 − s 1-s, else 2 − s 2-s. For inner a a and outer u u: if a ∈ P u a\in P_{u}, exactly one outer neighbour of u u contains a a; if a ∉ P u a\notin P_{u}, then [m ​ ( a) ∈ P u] [m(a)\in P_{u}] plus the number of outer neighbours of u u containing a a equals 2 2. The symmetry generators are the k / 2 k/2 within-pair swaps and the k / 2 − 1 k/2-1 adjacent-pair transpositions; each induces a permutation of the outer vertices (hence of the edge variables), to which a lex-leader constraint is applied.

For ( 99, 14, 1, 2) (99,14,1,2) this is a 12 12 -regular graph on 84 84 vertices.

We encode the reduced problem for CP-SAT and add lex-leader symmetry breaking over the group B k / 2 B_{k/2} that relabels the k / 2 k/2 matching-pairs and swaps within them (order 2 7 ⋅ 7! = 645, 120 2^{7}\cdot 7!=645{,}120 for k = 14 k=14), via its 13 13 generators. The pipeline is *validated end-to-end*: it recovers the unique srg ​ ( 9, 4, 1, 2) \mathrm{srg}(9,4,1,2) in milliseconds, with and without symmetry breaking. The ( 99, 14, 1, 2) (99,14,1,2) model has 379, 987 379{,}987 Booleans and 761, 221 761{,}221 constraints; in our runs it neither returns a graph nor exhausts (the expected outcome for an open problem), so we release it as a validated, maximally-pruned framework.

## 5 Prescribed-automorphism search and a negative methods finding

The research frontier is the existence question under a prescribed automorphism. Cesarz and Woldar [6], building on the orbit-matrix method of Behbahani and Lam [1], prove that Aut \mathrm{Aut} of any such graph is severely constrained: orders 9 9 and 11 11 are *excluded*; if 2 ∣ | G | 2\mid|G| then | G | ∣ 6 |G|\mid 6; and if 7 ∣ | G | 7\mid|G| then G ≅ ℤ 7 G\cong\mathbb{Z}_{7}. Order 7 7 is thus constrained but *not*ruled out: whether a ℤ 7 \mathbb{Z}_{7} -symmetric srg ​ ( 99, 14, 1, 2) \mathrm{srg}(99,14,1,2) exists is itself open. Since the non-fixed vertices split into 7 7 -cycles, any order- 7 7 action fixes f ≡ 99 ≡ 1 ( mod 7) f\equiv 99\equiv 1\pmod{7} vertices; the minimal case has 14 14 orbits of size 7 7 and a single fixed point.

We built a clean orbit-model existence encoding for a prescribed automorphism of order p p. With B = 99 / p B=99/p orbits, an invariant graph is block-circulant (adjacency of ( i, a), ( j, b) (i,a),(j,b) depends only on ( i, j, b − a mod p) (i,j,b{-}a\bmod p)), and for every pair-class the strong-regularity collapses to common + adjacency = 2 \textit{common}+\textit{adjacency}=2, encoding λ = 1 \lambda{=}1 and μ = 2 \mu{=}2 at once. We support both the fixed-point-free case (semiregular p ∣ 99 p\mid 99) and the single-fixed-point case (the fixed vertex joins full orbits, forced by 14 = 2 ⋅ 7 14=2\cdot 7 to exactly two of them). The encoding is *validated end-to-end*: it reconstructs and re-verifies srg ​ ( 9, 4, 1, 2) \mathrm{srg}(9,4,1,2) (both a fixed-point-free ℤ 3 \mathbb{Z}_{3} and an order- 2 2 action with one fixed point) and the Paley graph srg ​ ( 13, 6, 2, 3) \mathrm{srg}(13,6,2,3) (order- 3 3, one fixed point).

We then attacked the genuinely open sub-cases. For the single-fixed-point ℤ 7 \mathbb{Z}_{7} model (the minimal admissible order- 7 7 action, where a construction would resolve existence and an infeasibility certificate would eliminate it), CP-SAT returns unknown even after a 48 48 -hour run on 14 14 cores, neither building the graph nor proving infeasibility; the fixed-point-free ℤ 3 \mathbb{Z}_{3} model ( 33 33 orbits) likewise returns unknown within 1800 1800 s. We record this as an honest negative methods finding: even on an open sub-case where a specialised orbit-matrix enumeration would terminate, off-the-shelf CP-SAT does not, in our hands, decide the instance, and its persistence across a 96 × 96\times longer budget points to a structural barrier in the general-purpose encoding rather than a mere time shortfall. This sharply delimits the general-purpose approach and motivates the specialised orbit-matrix + + eigenvalue-interlacing machinery.

## 6 Heuristic frontier, best artifact, and search trajectory

For general (asymmetric) graphs we built an O ​ ( deg) O(\deg) incremental engine that maintains A A, C = A 2 C=A^{2}, the squared error SE = ∑ i < j ( t i ​ j − C i ​ j) 2 \mathrm{SE}=\sum_{i<j}(t_{ij}-C_{ij})^{2} (target t i ​ j = 1 t_{ij}=1 if edge else 2 2; a fitness used in a prior evolutionary-algorithm attempt [10]), and the exact-match score, so an edge toggle updates all in ≈ O ​ ( 14) \approx O(14) time. Because exact-match is a flat objective (no gradient), local search stalls on it; we instead optimise the *blend*O ​ ( A) = real ​ ( A) − α ​ SE ​ ( A) O(A)=\text{real}(A)-\alpha\,\mathrm{SE}(A), which keeps the true objective primary while − α ​ SE -\alpha\mathrm{SE} supplies a descent direction across plateaus, inside an island-model evolutionary algorithm with degree-preserving crossover.

Table 1: Representative results across the fourteen configurations we ran (rows group related methods); the score converges to 68.0 68.0 – 69.43 % 69.43\%. The best verified artifact is 3437 / 4950 = 69.43 % 3437/4950=69.43\%.

Method | character | best score |

Exhaustive circulant ( ℤ / 99 \mathbb{Z}/99) | proven bound | 68.0% |

Cayley search ( ℤ 3 × ℤ 3 × ℤ 11 \mathbb{Z}_{3}{\times}\mathbb{Z}_{3}{\times}\mathbb{Z}_{11}) | search | 68.0% |

Block CP-SAT, ℤ / 11, ℤ / 9, ℤ / 3 \mathbb{Z}/11,\mathbb{Z}/9,\mathbb{Z}/3 | exact, symmetric | 68.0% |

Full MaxSAT ( 504, 504 504{,}504 vars) | exact | 68.0% |

Degree-preserving 2-opt SA | heuristic | ≈ 56 % \approx 56\% |

Tabu / ILS | heuristic | 69.3% |

Min-conflicts; blended SA + + island EA | heuristic | 69.43% |

Table 1 summarises the frontier; the best artifact has degree 69 / 99 69/99, λ \lambda 374 / 708 374/708, μ \mu 2994 / 4143 2994/4143. Every high-scoring solution sits near λ ≈ 53 %, μ ≈ 72 % \lambda\approx 53\%,\mu\approx 72\%, the circulant is a strict 2 2 -opt local maximum, and large-neighbourhood CP-SAT re-optimisation of 14 14 -vertex chunks yields only lateral moves. Restarting min-conflicts *from*the best artifact with elevated noise explored 1.57 × 10 6 1.57\times 10^{6} accepted moves without satisfying a single additional constraint. The frontier is a strict local optimum, not a tuning artifact. To our knowledge, no prior work reports a partial-credit score on the track’s constraint metric; the prior evolutionary attempt of Hutnyk [10] optimised squared error, not the constraint count.

#### Agent trajectory (reported per the track’s interest).

The agent first encoded the problem for an SMT solver and stalled on the global connectivity/structure constraints; a corrective pivot to a CP-SAT solver gave order-of-magnitude speedups and unlocked the exhaustive circulant bound and the block models. Pushed for rigour, the agent then derived and validated the forced-structure reduction (Section 4), implemented the orbit-existence encoding, and, after a literature review establishing the open status and the automorphism results, re-scoped its claims to verifiable bounds and an explicit non-claim on existence. A final construction attempt prioritised the single most structurally-justified model (the open single-fixed-point ℤ 7 \mathbb{Z}_{7} orbit case) over undirected search, ran it to a 48 48 -hour budget, and reported its inconclusive ( unknown) outcome as such. The repeated theme was course-correction away from an over-optimistic framing toward certifiable statements.

## 7 Discussion and limitations

A score of 4950 4950*is*an srg ​ ( 99, 14, 1, 2) \mathrm{srg}(99,14,1,2); hence any provable upper bound below 4950 4950 would be a non-existence proof, and any method reaching 4950 4950 an existence proof. Crossing the partial-credit frontier toward the “high 90 90 s” is thus not a separate engineering target but is entangled with the open problem: a 95 % 95\% near-SRG is as structurally delicate to find as the graph. Limitations. We do not resolve existence; our 69.43 % 69.43\% artifact is a partial score, the ≈ 69 % \approx 69\% frontier is a search-landscape observation (not a proven global bound), and general-purpose CP-SAT did not decide the prescribed-automorphism sub-cases, including the genuinely open single-fixed-point ℤ 7 \mathbb{Z}_{7} case, which stayed unknown even after a 48 48 -hour, 14 14 -core run. The circulant bound (Prop. 1) and the reduction validation are the rigorous, reproducible results.

## 8 Conclusion

We contribute an exhaustive circulant ceiling ( 68.0 % 68.0\%), a validated forced-structure reduction to a 12 12 -regular graph on 84 84 vertices, a validated orbit-existence framework with an honest negative finding on the open single-fixed-point ℤ 7 \mathbb{Z}_{7} sub-case, a best verified artifact at 69.43 % 69.43\%, and a documented AI-agent trajectory, offered (as the track frames search work) as reusable infrastructure and structural pruning, with no claim on the open existence question.

## Acknowledgments and Disclosure of Funding

This work was supported by the Anusandhan National Research Foundation (ANRF), Government of India, under the Prime Minister Early Career Research Grant ANRF/ECRG/2025/001136/ENS.

## References

- [1] M. Behbahani, C. Lam. Strongly regular graphs with non-trivial automorphisms. *Discrete Math.*, 2011.
- [2] A. Biere, M. Heule, H. van Maaren, T. Walsh (eds.). *Handbook of Satisfiability*. IOS Press, 2nd ed., 2021.
- [3] N. L. Biggs. *Finite Groups of Automorphisms*. Cambridge Univ. Press, 1971.
- [4] A. E. Brouwer. Parameters of strongly regular graphs. Eindhoven Univ. of Technology.
- [5] A. E. Brouwer, A. M. Cohen, A. Neumaier. *Distance-Regular Graphs*. Springer, 1989.
- [6] P. G. Cesarz, A. J. Woldar. On the automorphism group of a putative Conway 99-graph. arXiv:2308.02978, 2023.
- [7] J. H. Conway. Five $1,000 problems (update 2017). OEIS A248380.
- [8] L. de Moura, N. Bjørner. Z3: An Efficient SMT Solver. In *TACAS 2008*, LNCS 4963, 337–340.
- [9] M. J. H. Heule, O. Kullmann, V. W. Marek. Solving and Verifying the Boolean Pythagorean Triples Problem via Cube-and-Conquer. In *SAT 2016*, LNCS 9710, 228–245.
- [10] C. Hutnyk. I’ve got 99 vertices but a solution to Conway’s problem ain’t one. Directed Reading Program, McGill University, 2019.
- [11] B. Konev, A. Lisitsa. A SAT Attack on the Erdős Discrepancy Conjecture. *Theoretical Computer Science*, 574:33–49, 2015.
- [12] S. L. Ma. A survey of partial difference sets. *Des. Codes Cryptogr.*, 1994.
- [13] Siddhartha Mahajan. Conway’s 99-Graph. Reviewed by Dr. Ankan Pal. CAISc 2026 Verifiable Problems Track, 2026. [https://caisc2026.github.io/verifiable-problems/?problem=conways-99-graph][3]
- [14] L. Perron, F. Didier. CP-SAT. Google OR-Tools. [https://developers.google.com/optimization/cp/cp_solver/][4], 2024.
- [15] A. Thakkar et al. Möbius: Synthesizing Relational Queries with Recursive and Invented Predicates. *Proc. ACM Program. Lang.*7 (OOPSLA), 2023.
- [16] A. Thakkar et al. Example-Guided Synthesis of Relational Queries. In *PLDI 2021*.
- [17] A. Thakkar et al. Modular Synthesis of Reactive Systems. In *SYNT 2020*.
- [18] Wikipedia contributors. Conway’s 99-graph problem. *Wikipedia*.

## Conference For AI Scientists 2026 - AI Involvement Checklist

### Research Stage Assessment

For items 1-4, give a score from the scale below that defines the role of AI in each part of the scientific process. The scores are as follows:

- •

[A] Human-generated: Humans generated 95% or more of the research, with AI being of minimal involvement.

- •

[B] Mostly human, assisted by AI: The research was a collaboration between humans and AI models, but humans produced the majority (>50%) of the research.

- •

[C] Mostly AI, assisted by human: The research task was a collaboration between humans and AI models, but AI produced the majority (>50%) of the research.

- •

[D] AI-generated: AI performed over 95% of the research. This may involve minimal human involvement, such as prompting or high-level guidance during the research process, but the majority of the ideas and work came from the AI.

For each research stage where AI was involved, i.e. where you selected [B] , [C] , or [D] , please also indicate the approximate level of iteration effort required using the provided iteration macros. Count substantive attempts, prompts, runs, agent trajectories, or course corrections; do not count minor wording edits.

- •

[Low] : approximately 1-10 substantive attempts.

- •

[Medium] : approximately 10-100 substantive attempts, with some failed attempts or course corrections.

- •

[High] : approximately 100+ substantive attempts, with substantial exploration, failures, or trial-and-error.

- •

[NA] : not applicable because AI involvement was [A] .

- •

[Unclear] : the authors cannot reasonably estimate.

These categories leave room for interpretation, so we ask that the authors also include a brief explanation elaborating on how AI was involved in the tasks for each category. Please keep your explanation to less than 150 words.

1. 1.

Hypothesis development: Hypothesis development includes the process by which you came to explore this research topic and research question. This can involve the background research performed by either researchers or by AI. This can also involve whether the idea was proposed by researchers or by AI.

Answer: [B]

Iteration Effort: [Medium]

Explanation: The problem instance and the strategic plan (the approaches, use of constraint solvers, considering the ℤ / 9 × ℤ / 11 \mathbb{Z}/9\times\mathbb{Z}/11 structure, and consult the literature) came from the author. The implementation and refinement of approaches (the circulant autocorrelation bound, the forced-structure reduction, the orbit-existence and blended-objective formulations) were generated by a frontier AI agent across iterations.

2. 2.

Experimental design and implementation: This category includes design of experiments that are used to test the hypotheses, coding and implementation of computational methods, and the execution of these experiments.

Answer: [C]

Iteration Effort: [Medium]

Explanation: The agent wrote the code (solver encodings, the reduction and its validation, and the fixed-point-free and single-fixed-point orbit-existence models).

3. 3.

Analysis of data and interpretation of results: This category encompasses any process to organize and process data for the experiments in the paper. It also includes interpretations of the results of the study.

Answer: [B]

Iteration Effort: [Low]

Explanation: The results were primarily analysed by the author, and the AI agent was only used for the final polish (to check if anything is missing).

4. 4.

Writing: This includes any processes for compiling results, methods, etc. into the final paper form. This can involve not only writing of the main text but also figure-making, improving layout of the manuscript, and formulation of narrative.

Answer: [C]

Iteration Effort: [Medium]

Explanation: The AI agent drafted the manuscript and tables. The author directed reviewing, revisions of framing, and scope.

### AI System Documentation

For items 5-6, provide a free-text description.

1. 5.

AI systems used: Describe all AI systems used in this research without naming specific products or models. Use system-level descriptors only (e.g., “a frontier large language model”, “a protein structure prediction system”, “a custom multi-agent framework built on open-source models”). Include relevant details such as system type, scale, and capabilities. Specific model and product names should only be included in the camera-ready version.

Description: Anthropic’s Claude, run as an autonomous research-and-coding agent via the Claude Code CLI with shell and tool access, invoking external constraint solvers (Google OR-Tools CP-SAT and Microsoft Z3) and standard scientific-Python libraries (NumPy, SciPy) for enumeration and verification.

2. 6.

Observed AI Limitations: What specific limitations and failure modes have you observed when using AI as a partner or lead author?

Description: (i) recurring tendency to over-claim or under-scope results, requiring repeated correction toward certifiable statements; (ii) inability of its general-purpose solver to decide the prescribed-automorphism instances (including the single-fixed-point ℤ 7 \mathbb{Z}_{7} sub-case).

## Conference For AI Scientists 2026 - Reproducibility and Responsibility Checklist

1. 1.

Claims

2.

Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope?

3.

Answer: [Yes]

4.

Justification: The abstract and introduction state exactly the verifiable contributions (exhaustive circulant bound, validated reduction, orbit framework with a negative finding, 69.43 % 69.43\% artifact) and explicitly disclaim any resolution of existence.

5.

Guidelines:

  - •

The answer NA means that the abstract and introduction do not include the claims made in the paper.

  - •

The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations. A No or NA answer to this question will not be perceived well by the reviewers.

  - •

The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings.

  - •

It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper.

6. 2.

Limitations

7.

Question: Does the paper discuss the limitations of the work performed by the authors?

8.

Answer: [Yes]

9.

Justification: A dedicated Discussion/Limitations section states that existence is unresolved, the 69 % 69\% frontier is empirical (not a proven global bound), and general-purpose CP-SAT did not certify the eliminations.

10.

Guidelines:

  - •

The answer NA means that the paper has no limitation while the answer No means that the paper has limitations, but those are not discussed in the paper.

  - •

The authors are encouraged to create a separate "Limitations" section in their paper.

  - •

The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e.g., independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally). The authors should reflect on how these assumptions might be violated in practice and what the implications would be.

  - •

The authors should reflect on the scope of the claims made, e.g., if the approach was only tested on a few datasets or with a few runs. In general, empirical results often depend on implicit assumptions, which should be articulated.

  - •

The authors should reflect on the factors that influence the performance of the approach. For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting.

  - •

The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size.

  - •

If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness.

  - •

While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper. Reviewers will be specifically instructed to not penalize honesty concerning limitations.

11. 3.

Theory assumptions and proofs

12.

Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof?

13.

Answer: [Yes]

14.

Justification: Proposition 1 is a computational claim proved by complete enumeration; the assumptions (symmetric | S | = 14 |S|=14 connection set on ℤ / 99 \mathbb{Z}/99; satisfaction criterion per difference-class) are stated in-place, and the enumerator and verifier are released with the paper. The forced-structure reduction of Section 4 states its assumptions ( λ = 1 \lambda=1, μ = 2 \mu=2) and derives the inner matching, inner–outer bijection, and outer-graph constraints in the text.

15.

Guidelines:

  - •

The answer NA means that the paper does not include theoretical results.

  - •

All the theorems, formulas, and proofs in the paper should be numbered and cross-referenced.

  - •

All assumptions should be clearly stated or referenced in the statement of any theorems.

  - •

The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition.

16. 4.

Experimental result reproducibility

17.

Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)?

18.

Answer: [Yes]

19.

Justification: The circulant enumeration (search space, autocorrelation criterion, running time), the reduced CP-SAT model ( 379, 987 379{,}987 Booleans, 761, 221 761{,}221 constraints, symmetry-breaking generators for B k / 2 B_{k/2}), the orbit-existence encoding, the blended objective ( O ​ ( A) = real ​ ( A) − α ​ SE ​ ( A) O(A)=\text{real}(A)-\alpha\,\mathrm{SE}(A)), and the compute budgets are all specified in the main text; source and the 69.43 % 69.43\% artifact are released as supplementary material.

20.

Guidelines:

  - •

The answer NA means that the paper does not include experiments.

  - •

If the paper includes experiments, a No answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important.

  - •

If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable.

  - •

We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility. In the case of closed-source models, it may be that access to the model is limited in some way (e.g., to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results.

21. 5.

Open access to data and code

22.

Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material?

23.

Answer: [Yes]

24.

Justification: The enumerator, reduction solver, orbit-existence encoding, search framework, verifier, and the artifact are released as supplementary material with run instructions.

25.

Guidelines:

  - •

The answer NA means that paper does not include experiments requiring code.

  - •

While we encourage the release of code and data, we understand that this might not be possible, so “No” is an acceptable answer. Papers cannot be rejected simply for not including code, unless this is central to the contribution (e.g., for a new open-source benchmark).

  - •

At submission time, to preserve anonymity, the authors should release anonymized versions (if applicable).

  - •

Please include anonymized code and data files (if applicable) as supplementary materials where relevant. The instructions should contain the exact command and environment needed to run to reproduce the results.

26. 6.

Experimental setting/details

27.

Question: Does the paper specify all the training and test details (e.g., data splits, hyperparameters, how they were chosen, type of optimizer, etc.) necessary to understand the results?

28.

Answer: [Yes]

29.

Justification: Encodings, objective (blend weight α \alpha), solver worker counts, and time budgets are described in the relevant sections.

30.

Guidelines:

  - •

The answer NA means that the paper does not include experiments.

  - •

The experimental setting should be presented in the core of the paper to a level of detail that is necessary to appreciate the results and make sense of them.

  - •

The full details can be provided either with the code, in appendix, or as supplemental material.

31. 7.

Experiment statistical significance

32.

Question: Does the paper report error bars suitably and correctly defined or other appropriate information about the statistical significance of the experiments?

33.

Answer: [NA]

34.

Justification: The headline results are deterministic (exhaustive enumeration; exact reduction). Heuristic outcomes are reported as best-found, for which error bars are not the appropriate summary.

35.

Guidelines:

  - •

The answer NA means that the paper does not include experiments.

  - •

The authors should answer "Yes" if the results are accompanied by error bars, confidence intervals, or statistical significance tests, at least for the experiments that support the main claims of the paper.

  - •

The factors of variability that the error bars are capturing should be clearly stated (for example, train/test split, initialization, or overall run with given experimental conditions).

36. 8.

Experiments compute resources

37.

Question: For each experiment, does the paper provide sufficient information on the computer resources (type of compute workers, memory, time of execution) needed to reproduce the experiments?

38.

Answer: [Yes]

39.

Justification: All experiments ran on a single 14 14 -core laptop CPU; the exhaustive circulant enumeration takes ≈ 100 \approx 100 s, the prescribed-automorphism orbit searches were run for 1800 1800 s (the open single-fixed-point ℤ 7 \mathbb{Z}_{7} case additionally to a 48 48 -hour budget), and other solver runs take minutes to a few hours, as stated.

40.

Guidelines:

  - •

The answer NA means that the paper does not include experiments.

  - •

The paper should indicate the type of compute workers CPU or GPU, internal cluster, or cloud provider, including relevant memory and storage.

  - •

The paper should provide the amount of compute required for each of the individual experimental runs as well as estimate the total compute.

41. 9.

Research Ethics

42.

Question: Does the research conducted in the paper conform with the [NeurIPS Code of Ethics][5], except where CAISc’s AI authorship policies apply?

43.

Answer: [Yes]

44.

Justification: The work is pure combinatorial mathematics with no human-subjects, data-privacy, or dual-use concerns; AI involvement is documented per CAISc policy.

45.

Guidelines:

  - •

All submissions should adhere to the [NeurIPS Code of Ethics][5], except where CAISc’s AI authorship policies apply.

  - •

The answer NA means that the authors have not reviewed the NeurIPS Code of Ethics.

  - •

If the authors answer No, they should explain the special circumstances that require a deviation from the Code of Ethics.

46. 10.

Broader impacts

47.

Question: Does the paper discuss both potential positive societal impacts and negative societal impacts of the work performed?

48.

Answer: [NA]

49.

Justification: The work concerns the existence of a specific combinatorial object; we identify no material positive or negative societal impact beyond contributing reusable search methodology.

50.

Guidelines:

  - •

The answer NA means that there is no societal impact of the work performed.

  - •

If the authors answer NA or No, they should explain why their work has no societal impact or why the paper does not address societal impact.

  - •

Examples of negative societal impacts include potential malicious or unintended uses (e.g., disinformation, generating fake profiles, surveillance), fairness considerations, privacy considerations, and security considerations.

  - •

If there are negative societal impacts, the authors could also discuss possible mitigation strategies.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: https://caisc2026.github.io/verifiable-problems/?problem=conways-99-graph
[4]: https://developers.google.com/optimization/cp/cp_solver/
[5]: https://neurips.cc/Conferences/2026/MainTrackHandbook
