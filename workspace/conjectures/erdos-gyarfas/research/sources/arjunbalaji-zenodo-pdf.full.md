<!-- source: https://zenodo.org/records/21190438/files/erdos-gyarfas-ieee.pdf?download=1 | converted from PDF -->

SUBMITTED TO IEEE ACCESS 1

Verifying the Erdős–Gyárfás Conjecture up to 31
Vertices with SAT Modulo Symmetries

Arjun Balaji

Abstract—Boolean satisfiability (SAT) solvers have resolved
a series of longstanding combinatorial problems, yet many
well-known conjectures have never been attacked with modern
automated-reasoning tools. We present the first SAT-based
attack on the Erdős–Gyárfás conjecture (1995), which asserts
that every graph of minimum degree at least 3 contains a
cycle whose length is a power of two. The conjecture is open;
prior computer search established that any general minimum-
degree-3 counterexample has at least 17 vertices (Royle and
Markström), and any cubic (3-regular) counterexample at least
30 (Markström, 2004). Using SAT Modulo Symmetries (SMS),
which performs complete isomorph-free graph generation inside
a CDCL solver, with the Glasgow subgraph solver as a complete
forbidden-subgraph propagator, we verify that every minimum-
degree-3 graph on at most 31 vertices contains a cycle of
length 4, 8, or 16, settling the entire range in which these are
the only admissible power-of-two cycle lengths. Consequently
any general minimum-degree-3 counterexample has at least 32
vertices, improving the two-decade-old general bound from 17
to 32 and the cubic bound from 30 to 32. Each order up to 31
is decided in at most about two hours on a single CPU core,
whereas a conventional CEGAR baseline stalls near order 20.
We corroborate the result with an exact ground-truth check
against nauty at n = 10, reproduction of the n ≤ 16 baseline,
agreement with the independent CEGAR solver for n ≤ 19,
and robustness across cardinality encodings and symmetry-
breaking methods, and we release the complete reproducible
pipeline.

Index Terms—Automated reasoning, Boolean satisfiability,
combinatorics, constraint propagation, Erdős–Gyárfás conjec-
ture, graph generation, symmetry breaking.

I. Introduction
S AT solvers have become a standard instrument for set-
tling hard combinatorial questions: celebrated exam-
ples include the Boolean Pythagorean triples problem [1],
Schur number five [2], and Keller’s conjecture [3], each
resolved by encoding the question into propositional logic
and letting a conflict-driven solver exhaust the search
space. A newer line of work, SAT Modulo Symmetries
(SMS) [15], [16], extends this instrument to graph exis-
tence questions: it augments a CDCL solver with an in-
search canonicity propagator so that the solver enumerates
exactly one representative per isomorphism class, making
exhaustive isomorph-free search feasible at orders far
beyond explicit enumeration. In this paper we apply SMS
to a well-known open conjecture of Erdős and Gyárfás that,
to our knowledge, has never been attacked with SAT-based
or constraint-programming methods.

A. Balaji is with Columbia University, New York, NY, USA (e-mail:
ab6136@columbia.edu). ORCID: 0009-0005-1790-0034.
 In 1995 Erdős and Gyárfás posed the following conjec-
ture (see Erdős [4]); Erdős offered $100 for a proof and
$50 for a counterexample [5].
Conjecture 1 (Erdős–Gyárfás): Every graph with mini-
mum degree at least 3 contains a simple cycle whose length
is a power of two.
The conjecture is open. It has been confirmed for
restricted classes, including K1,m-free graphs [9], planar
claw-free graphs [10], 3-connected cubic planar graphs [8],
and the Pt-free families P8 [11], P10 [12], and (with the aid
of a computer search assisting a structural proof) P13 [13].
These are theorems for infinite hereditary classes and do
not bound the order of a general counterexample. Carr [14]
recently showed that at least 4/7 of the vertices of any
minimal counterexample have degree exactly 3.
Computationally, two frontiers were known, and the
distinction is central to this paper. Write δ(G) for the
minimum degree of G.

• General (δ ≥ 3, arbitrary maximum degree): com-
puter searches of Royle and Markström are commonly
cited as establishing that any counterexample has at
least 17 vertices [20].

• Cubic (3-regular): Markström [6] verified all cubic
graphs on at most 29 vertices, so any cubic coun-
terexample has at least 30 vertices.
A targeted literature search (covering theses, OEIS, House
of Graphs, and the most recent surveys of SMS and of
computer-assisted graph theory [16], [17]) found no im-
provement of the general bound past 17 after 2004, and no
prior application of SAT, SMS, constraint programming,
or isomorph-free generation to Conjecture 1.
Contribution: We give the first SAT-based attack on
Conjecture 1, combining SMS with the Glasgow subgraph
solver [18] as a complete forbidden-subgraph propagator:
Theorem 1: Every graph with minimum degree at least
3 on at most 31 vertices contains a cycle of length 4, 8, or
16. Consequently, any minimum-degree-3 counterexample
to the Erdős–Gyárfás conjecture has at least 32 vertices.
This improves the general bound from 17 to 32, a +15-
vertex extension over a search space that, unlike the cubic
case, includes all non-regular graphs of minimum degree 3.
By Proposition 1 below, order 31 is exactly the last order
at which C4, C8, C16 are the only admissible power-of-two
cycle lengths, so Theorem 1 settles that entire regime; C32
first becomes possible at n = 32.
The two prior frontiers should not be conflated. Mark-
ström verified the cubic class up to order 29; the general
class had been verified only up to order 16. We verify the

SUBMITTED TO IEEE ACCESS 2

entire minimum-degree-3 class (a strictly larger family,
dominated by non-regular graphs) up to order 31, which
also covers all cubic graphs on 30 and 31 vertices, raising
the cubic bound from 30 to 32 as well. The genuinely new
content is thus the non-cubic minimum-degree-3 graphs
on 17 ≤ n ≤ 31 vertices together with the cubic graphs
on 30 ≤ n ≤ 31 vertices, and the methodology, which
had not previously been applied to this conjecture. Our
methodological ingredients, SMS and the Glasgow sub-
graph solver, have been applied to other graph-existence
questions (e.g., the 3-Decomposition Conjecture on cubic
graphs), but not to Conjecture 1.

II. Method
For fixed n we decide the following question with a
single SMS call: does there exist a graph G on n vertices
with δ(G) ≥ 3 that contains no cycle of length 4, 8, or 16?
The reduction to these three cycle lengths is justified by
the following observation.
Proposition 1: For 3 ≤ n ≤ 31, a graph on n vertices
contains a cycle whose length is a power of two if and only
if it contains C4, C8, or C16 as a (non-induced) subgraph.
Proof: A cycle of length ℓ is precisely a Cℓ subgraph,
and the powers of two that are valid cycle lengths (at least
3) and at most n ≤ 31 are exactly 4, 8, 16; the next one,
32, exceeds n.
By Proposition 1, if for every n ≤ 31 no minimum-
degree-3 graph on n vertices contains C4, C8, or C16,
then no minimum-degree-3 counterexample on at most
31 vertices exists. A minimum-degree-3 graph requires
n ≥ 4; for n ≤ 16 the conjecture is the established baseline,
which we reproduce (§IV), and the smallest orders hold
trivially (K4 contains C4). It therefore suﬀices to settle
17 ≤ n ≤ 31, which is the content of Theorem 1.

A. SAT Modulo Symmetries
Modern conflict-driven clause-learning (CDCL) solvers
can be extended with user propagators: external proce-
dures that inspect the solver’s partial assignment during
search and inject clauses, standardized by the IPASIR-UP
interface [7]. SMS builds on exactly this mechanism to
perform complete, isomorph-free generation of the graphs
satisfying given constraints: its modified CaDiCaL solver
carries an in-search canonicity (minimality) propagator
that prunes any partial adjacency matrix that cannot be
extended to the lexicographically minimal representative
of its isomorphism class [15]. This is the key to scaling:
symmetry is broken completely and during search, so the
solver considers essentially one graph per isomorphism
class rather than enumerating all labelings, and an UNSAT
outcome is a statement about all graphs of the given order,
not all labeled graphs.

B. Encoding
The minimum-degree constraint δ(G) ≥ 3 is encoded
as a cardinality constraint over the (n
2) edge variables
(the sequential-counter encoding produced by PySMS;
 TABLE I
SMS decision per order n: no minimum-degree-3 graph on n
vertices avoids C4, C8, C16. With the reproduced n ≤ 16 baseline
this proves Theorem 1.

n count time (s) n count time (s)

17 0 2.9 25 0 339.8
18 0 7.8 26 0 414.8
19 0 24.1 27 0 1000.3
20 0 27.8 28 0 1892.0
21 0 19.3 29 0 2342.8
22 0 101.1 30 0 6888.9
23 0 202.9 31 0 7351.4
24 0 148.3

see §IV for a totalizer cross-check). The constraint “no
C4, C8, or C16” is enforced by the Glasgow subgraph
solver [18] as a complete forbidden-subgraph propagator:
whenever a (partial) graph contains one of these cycles as
a (non-induced) subgraph, the propagator adds a clause
excluding it. Forbidding the short cycle C4 statically in
CNF is cheap, but C8 and C16 have Θ(n8) and Θ(n16)
potential occurrences, so a static encoding is infeasible; the
propagator is what makes the search tractable. A return
of “no graphs” certifies that no such graph exists.

C. Why not plain CEGAR-SAT
As a baseline we also implemented a self-contained
counterexample-guided (CEGAR) SAT solver in Python
(PySAT with CaDiCaL, a DFS power-of-two cycle de-
tector, and a static adjacent-transposition lexicographic
symmetry break). With only a partial symmetry break
it re-discovers each forbidden cycle in many isomorphic
copies: at n = 17 it accumulates roughly 85,000 refinement
clauses and the per-instance time grows by about a factor
of two per vertex, so it stalls at n = 19 (bound ≥ 20).
SMS decides the same n = 17 instance in 2.9 seconds
(Table I). Complete symmetry breaking is precisely what
removes this bottleneck; the two solvers agree wherever
both finish (n ≤ 19, §IV).

III. Results
Table I reports, for each n from 17 to 31, that SMS finds
no minimum-degree-3 graph avoiding all of C4, C8, C16
(solution count 0). All runs used a single CPU core;
Figure 1 shows the runtime trend.
Experimental setup: For each n we encode minimum
degree at least 3 as a cardinality constraint over the(n
2) edge variables and decide it with the SMS solver
run in enumeration mode, using the Glasgow subgraph
solver to forbid C4, C8, and C16. The runs used SMS at
commit 464f12f, built with the Glasgow Subgraph Solver
at commit abd331a and the SMS-bundled CaDiCaL,
compiled with g++ 12.2.0 on Debian 12 (Python 3.12)
cloud containers, one virtual CPU core per order, with a
per-order soft time budget enforced by the harness and
a hard container ceiling above it. Wall times in Table I
exclude container start-up. Each order is an independent,
stateless decision, so the ladder parallelizes trivially and

SUBMITTED TO IEEE ACCESS 3

17 19 21 23 25 27 29 31
100

102

104
 order nwalltime(s)
Fig. 1. Single-core wall time of the SMS decision at each order n (log
scale). Every point is UNSAT. Growth is roughly geometric, about
a factor of 1.5–2 per added vertex.

any order can be re-run in isolation. The exact solver
invocation, the pinned tool versions, and the build and
run scripts are available in the accompanying repository
(see Data Availability).

IV. Verification
A non-existence claim at n = 31 cannot be brute-
forced (exhaustive generation of minimum-degree-3 graphs
is infeasible beyond roughly n = 13), so we corroborate
Theorem 1 with several independent checks. No check
produced a contradiction.
1) Ground-truth anchor. At n = 10, forbidding only
C4, SMS returns exactly 5 graphs, matching the
independent count of the 5 C4-free minimum-
degree-3 graphs on 10 vertices obtained with nauty
(geng+labelg) [19].
2) Baseline reproduction. For n = 6, . . . , 16, forbidding
all of C4, C8, C16 yields 0, reproducing the published
baseline.
3) Independent second solver. Our CEGAR-SAT solver
and SMS both return UNSAT for n = 17, 18, 19
(different solvers, symmetry breaking, and cycle
handling).
4) Encoding robustness. Re-deciding with the totalizer
cardinality encoding (a structurally different CNF)
gives count 0 at n = 17, 20, 22, 25.
5) Symmetry-method robustness. Re-deciding with
SMS’s colex minimality ordering gives count 0 at
n = 17, 20; the (slower, experimental) colex variant
timed out at n = 22, 25 (inconclusive, not contradic-
tory).
6) Positive controls. Forbidding only C4 (a weaker
constraint) yields a graph at n = 17, 20, 25, 30,
confirming the pipeline returns a solution when one
exists.
The soundness of the result rests on SMS’s isomorph-
free generation, the completeness of the Glasgow subgraph
propagator, and the correctness of the min-degree encod-
ing; the checks above corroborate this composition exactly
at n = 10 and across n ≤ 16, as is standard for computer-
assisted enumeration. The natural further strengthening
is an end-to-end machine-checked certificate: smsg can
emit an LRAT proof for UNSAT instances, but a generic
 checker cannot validate it against the min-degree CNF
alone, because the forbidden-cycle clauses are added by the
propagator during search and are not RUP/RAT-derivable
from that CNF. A certificate via the certified-SMS proof-
logging machinery, in which the propagators justify their
own clauses, would put the result on the same footing as
the certified SAT resolutions of the Pythagorean triples
and Schur-number problems [1], [2]; we leave this as the
principal next step.
 V. Discussion

Two aspects of this study seem worth drawing out
for the automated-reasoning audience beyond the specific
bound.

A. The barrier was methodological, not computational

The general frontier for this conjecture stood at 16
vertices for roughly two decades. The entire ladder of
Table I, from n = 17 through n = 31, consumed under six
CPU core-hours in total on commodity cloud hardware,
i.e., a negligible computational budget by any modern
standard. What changed is not available computing power
but the search technology: explicit isomorph-free enu-
meration (of the geng type) hits a wall near n ≈ 13–
16 for this class because the number of isomorphism
classes explodes, while a naive SAT formulation without
complete symmetry breaking drowns in isomorphic copies
of the same forbidden substructures (§II). Complete in-
search symmetry breaking combined with a specialized
propagator for the global constraint is precisely what
removes the wall. We expect the same template, SMS
plus a forbidden-subgraph propagator, to apply directly to
other cycle-spectrum and forbidden-subgraph questions in
extremal graph theory, many of which have computational
frontiers of similar vintage.

B. Trusting a computational nonexistence claim

A claim of the form “no graph with these properties
exists on n ≤ 31 vertices” cannot be spot-checked against
examples, so the burden shifts to the pipeline. Our veri-
fication protocol (§IV) is designed around independence:
an exact agreement with nauty-based ground truth where
ground truth is computable, reproduction of the previously
published baseline, a second solver built from entirely
different components agreeing on the overlap region, ro-
bustness of the answer across two cardinality encodings
and two symmetry-breaking orders, and positive controls
confirming that the pipeline finds graphs when they exist.
None of these checks is individually conclusive; jointly
they leave the tool-chain-completeness assumption (§IV)
as the single point of trust, which is exactly the point
that a certified-SMS proof certificate would discharge. We
consider this protocol, rather than any single run, to be
the reusable contribution for practitioners applying SAT
to mathematical nonexistence questions.

SUBMITTED TO IEEE ACCESS 4

VI. Conclusion
We gave the first SAT-based attack on the Erdős–
Gyárfás conjecture. Casting the question as “does a
minimum-degree-3 graph with no C4, C8, or C16 exist?”
and discharging it with SAT Modulo Symmetries and the
Glasgow subgraph propagator, we verified the conjecture
for all minimum-degree-3 graphs on at most 31 vertices,
raising the general lower bound on a counterexample
from 17 to 32 and settling the entire regime in which
C4, C8, C16 are the only admissible power-of-two cycles.
The decisive ingredient is complete, in-search symmetry
breaking: a conventional CEGAR encoding stalls near
n = 20, whereas SMS decides each order up to 31 in
at most about two hours of single-core time.
The result does not prove the conjecture; it raises the
lower bound on the order of a hypothetical counterexam-
ple. Several directions remain. (i) Push the frontier. The
next order, n = 32, is the first at which a cycle of length
32 can occur, so extending the search requires adding
C32 to the forbidden set; the runtime trend (Figure 1)
suggests a few further orders are within reach with modest
parallelism. (ii) A machine-checked certificate, as discussed
in §IV. (iii) Exploit structure. Carr’s result that a minimal
counterexample is predominantly cubic [14] could be
added as a propagator to prune the search. (iv) Other
questions. The same SMS-plus-forbidden-subgraph tem-
plate applies directly to related cycle-spectrum problems.

Data Availability
All source code, per-order data, the exact build scripts
with pinned tool versions, and the verification scripts are
openly available at https://github.com/ArjunBalaji
79/erdos- gyarfas- min- degree-3, enabling independent
reproduction of every value in Table I.

Acknowledgment
During this work the author used Anthropic’s Claude
(via the Claude Code interface) as a coding and research
assistant: principally to implement the SAT/SMS pipeline
and verification scripts and to execute the computational
experiments (§II and the accompanying repository), and
additionally to assist in preparing the manuscript and
searching the literature. The research questions, design
decisions, validation, and final text are the author’s, who
reviewed and edited all content and takes full responsibil-
ity for the content of this article. This work received no
external funding.
 References

[1] M. J. H. Heule, O. Kullmann, and V. W. Marek, “Solving and
verifying the Boolean Pythagorean triples problem via cube-and-
conquer,” in Proc. SAT 2016, LNCS 9710, 2016, pp. 228–245.
[2] M. J. H. Heule, “Schur number five,” in Proc. AAAI 2018, 2018,
pp. 6598–6606.
[3] J. Brakensiek, M. J. H. Heule, J. Mackey, and D. Narváez, “The
resolution of Keller’s conjecture,” in Proc. IJCAR 2020, LNCS
12166, 2020, pp. 48–65.
[4] P. Erdős, “Some old and new problems in various branches
of combinatorics,” Discrete Math., vol. 165/166, pp. 227–231,
1997.
 [5] Erdős Problems, “Power-of-two cycles.” [Online]. Available: ht
tps://www.erdosproblems.com/
[6] K. Markström, “Extremal graphs for some problems on cycles in
graphs,” Congressus Numerantium, vol. 171, pp. 177–188, 2004.
[7] K. Fazekas, A. Niemetz, M. Preiner, M. Kirchweger, S. Szeider,
and A. Biere, “IPASIR-UP: User propagators for CDCL,” in
Proc. SAT 2023, LIPIcs vol. 271, 2023.
[8] C. C. Heckman and R. Krakovski, “Erdős–Gyárfás conjecture
for cubic planar graphs,” Electron. J. Combin., vol. 20, no. 2,
#P7, 2013.
[9] S. E. Shauger, “Results on the Erdős–Gyárfás conjecture in
K1,m-free graphs,” Congressus Numerantium, vol. 134, 1998.
[10] D. Daniel and S. E. Shauger, “A result on the Erdős–
Gyárfás conjecture in planar graphs,” Congressus Numerantium,
vol. 153, 2001.
[11] Y. Gao and S. Shan, “Erdős–Gyárfás conjecture for P8-
free graphs,” Graphs Combin., vol. 38, no. 6, 2022, doi:
10.1007/s00373-022-02578-9.
[12] Z. Hu and C. Shen, “The Erdős–Gyárfás conjecture holds for
P10-free graphs,” Discrete Math., vol. 347, no. 9, 114175, 2024.
[13] A. S. Hegde, R. B. Sandeep, and P. Shashank, “Erdős–
Gyárfás conjecture on graphs without long induced paths,”
arXiv:2410.22842, 2024.
[14] A. Carr, “Every minimal counterexample to the Erdős–Gyárfás
conjecture is predominantly cubic,” arXiv:2605.22844, 2026,
preprint.
[15] M. Kirchweger and S. Szeider, “SAT Modulo Symmetries for
graph generation and enumeration,” ACM Trans. Comput.
Logic, vol. 25, no. 3, Art. 18, 2024, doi: 10.1145/3670405.
[16] S. Szeider, “SAT Modulo Symmetries: A survey,” CEUR Work-
shop Proceedings, vol. 4116, 2025.
[17] J. Jooken, “Computer-assisted graph theory,” arXiv:2508.20825,
2025.
[18] C. McCreesh, P. Prosser, and J. Trimble, “The Glasgow Sub-
graph Solver: Using constraint programming to tackle hard sub-
graph isomorphism problem variants,” in Graph Transformation
(ICGT 2020), LNCS 12150, 2020, pp. 316–324.
[19] B. D. McKay and A. Piperno, “Practical graph isomorphism,
II,” J. Symbolic Comput., vol. 60, pp. 94–112, 2014.
[20] Wikipedia, “Erdős–Gyárfás conjecture” (secondary source for
the commonly-cited general ≥ 17 bound).
