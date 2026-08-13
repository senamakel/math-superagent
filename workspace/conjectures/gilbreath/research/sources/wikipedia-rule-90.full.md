<!-- source: https://en.wikipedia.org/wiki/Rule_90 | converted from HTML -->

Rule 90 - Wikipedia

Jump to content

[image: This is a good article. Click here for more information.] [1]

From Wikipedia, the free encyclopedia

Elementary cellular automaton

[2] Time-space diagram of Rule 90 with random initial conditions. Each row of pixels is a configuration of the automaton; time progresses vertically from top to bottom.

In the [mathematical][3] study of [cellular automata][4], **Rule 90**is an [elementary cellular automaton][5] based on the [exclusive or][6] function. It consists of a one-dimensional array of cells, each of which can hold either a 0 or a 1 value. In each time step all values are simultaneously replaced by the [XOR][6] of their two neighboring values. [1] Martin, Odlyzko & Wolfram (1984) call it "the simplest non-trivial cellular automaton", [2] and it is described extensively in [Stephen Wolfram][7] 's 2002 book *[A New Kind of Science][8]*. [3]

When started from a single live cell, Rule 90 has a time-space diagram in the form of a [Sierpiński triangle][9]. The behavior of any other configuration can be explained as a superposition of copies of this pattern, combined using the [exclusive or][6] function. Any configuration with only finitely many nonzero cells becomes a [replicator][10] that eventually fills the array with copies of itself. When Rule 90 is started from a [random][11] initial configuration, its configuration remains random at each time step. Its time-space diagram forms many triangular "windows" of different sizes, patterns that form when a consecutive row of cells becomes simultaneously zero and then cells with value 1 gradually move into this row from both ends.

Some of the earliest studies of Rule 90 were made in connection with an unsolved problem in [number theory][12], [Gilbreath's conjecture][13], on the differences of consecutive [prime numbers][14]. This rule is also connected to number theory in a different way, via [Gould's sequence][15]. This sequence counts the number of nonzero cells in each time step after starting Rule 90 with a single live cell. Its values are [powers of two][16], with exponents equal to the number of nonzero digits in the [binary representation][17] of the step number. Other applications of Rule 90 have included the design of [tapestries][18].

Every configuration of Rule 90 has exactly four predecessors, other configurations that form the given configuration after a single step. Therefore, in contrast to many other cellular automata such as [Conway's Game of Life][19], Rule 90 has no [Garden of Eden][20], a configuration with no predecessors. It provides an example of a cellular automaton that is [surjective][21] (each configuration has a predecessor) but not [injective][22] (it has sets of more than one configuration with the same successor). It follows from the [Garden of Eden theorem][23] that Rule 90 is locally injective (all configurations with the same successor vary at an infinite number of cells).

## Description

[[edit][24]]

### Rules

[[edit][25]]

[26] In Rule 90, each cell's value is computed as the exclusive or of the two neighboring values in the previous time step.

Rule 90 is an [elementary cellular automaton][5]. That means that it consists of a one-dimensional array of cells, each of which holds a single binary value, either 0 or 1. An assignment of values to all of the cells is called a *configuration*. The automaton is given an initial configuration, and then progresses through other configurations in a sequence of discrete time steps. At each step, all cells are updated simultaneously. A pre-specified rule determines the new value of each cell as a function of its previous value and of the values in its two neighboring cells. All cells obey the same rule, which may be given either as a formula or as a rule table that specifies the new value for each possible combination of neighboring values. [1]

In the case of Rule 90, each cell's new value is the [exclusive or][6] of the two neighboring values. Equivalently, the next state of this particular automaton is governed by the following rule table: [1]

current pattern | 111 | 110 | 101 | 100 | 011 | 010 | 001 | 000 |

new state for center cell | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |

### Naming

[[edit][27]]

The name of Rule 90 comes from [Stephen Wolfram][7] 's [binary-decimal notation][28] for one-dimensional cellular automaton rules. To calculate the notation for the rule, concatenate the new states in the rule table into a single [binary number][29], and convert the number into [decimal][30]: 01011010 2 = 90 10. [1] Rule 90 has also been called the **Sierpiński automaton**, due to the characteristic [Sierpiński triangle][9] shape it generates, [4] and the **Martin–Odlyzko–Wolfram cellular automaton**after the early research of Olivier Martin, [Andrew M. Odlyzko][31], and [Stephen Wolfram][7] ( 1984) on this automaton. [5]

## Properties

[[edit][32]]

### Additivity, superposition, and decomposition

[[edit][33]]

A configuration in Rule 90 can be partitioned into two subsets of cells that do not interact with each other. One of these two subsets consists of the cells in even positions at even time steps and the cells in odd positions in odd time steps. The other subset consists of the cells in even positions at odd time steps and the cells in odd positions at even time steps. Each of these two subsets can be viewed as a cellular automaton with only its half of the cells. [6] The rule for the automaton within each of these subsets is equivalent (except for a shift by half a cell per time step) to another [elementary cellular automaton][5], **Rule 102**, in which the new state of each cell is the exclusive or of its old state and its right neighbor. That is, the behavior of Rule 90 is essentially the same as the behavior of two interleaved copies of Rule 102. [7]

Rule 90 and Rule 102 are called *additive cellular automata*. This means that, if two initial states are combined by computing the exclusive or of each their states, then their subsequent configurations will be combined in the same way. More generally, one can partition any configuration of Rule 90 into two subsets with disjoint nonzero cells, evolve the two subsets separately, and compute each successive configuration of the original automaton as the exclusive or of the configurations on the same time steps of the two subsets. [2]

### Deterministic solution

[[edit][34]]

Rule 90 is deterministically solvable, meaning that one can express the state of a given cell after n {\displaystyle n}[image: {\displaystyle n}] iterations starting from initial configuration x ∈ { 0, 1 } Z {\displaystyle x\in \{0,1\}^{\mathbb {Z} }}[image: {\displaystyle x\in \{0,1\}^{\mathbb {Z} }}] by an explicit formula. Let [F n ( x)] j {\displaystyle [F^{n}(x)]_{j}}[image: {\displaystyle [F^{n}(x)]_{j}}] represent the state of cell j {\displaystyle j}[image: {\displaystyle j}] after n {\displaystyle n}[image: {\displaystyle n}] iterations or rule F {\displaystyle F}[image: {\displaystyle F}], which in our case is rule 90. Initial condition is represented by x {\displaystyle x}[image: {\displaystyle x}], so that x i {\displaystyle x_{i}}[image: {\displaystyle x_{i}}] is the state of cell i {\displaystyle i}[image: {\displaystyle i}] in the initial configuration, x i ∈ { 0, 1 } {\displaystyle x_{i}\in \{0,1\}}[image: {\displaystyle x_{i}\in \{0,1\}}]. For rule 90 one can show [8] [9] that

[F n ( x)] j = ∑ i = 0 n ( n i) x 2 i − n + j mod 2 {\displaystyle [F^{n}(x)]_{j}=\sum _{i=0}^{n}{\binom {n}{i}}x_{2\,i-n+j}\mod 2}[image: {\displaystyle [F^{n}(x)]_{j}=\sum _{i=0}^{n}{\binom {n}{i}}x_{2\,i-n+j}\mod 2}]

### Probabilistic solution

[[edit][35]]

Suppose that the initial configuration is a random bi-infinite binary string x ∈ { 0, 1 } Z {\displaystyle x\in \{0,1\}^{\mathbb {Z} }}[image: {\displaystyle x\in \{0,1\}^{\mathbb {Z} }}] drawn from the Bernoulli distribution, such that probability of x i = 1 {\displaystyle x_{i}=1}[image: {\displaystyle x_{i}=1}] is equal to p ∈ [0, 1] {\displaystyle p\in [0,1]}[image: {\displaystyle p\in [0,1]}] and the probability of x i = 0 {\displaystyle x_{i}=0}[image: {\displaystyle x_{i}=0}] is 1 − p {\displaystyle 1-p}[image: {\displaystyle 1-p}]. Then one can show [10] that after n {\displaystyle n}[image: {\displaystyle n}] iterations of rule 90, probabilities of occurrence of blocks 0, 00, 000 {\displaystyle 0,00,000}[image: {\displaystyle 0,00,000}], and 010 {\displaystyle 010}[image: {\displaystyle 010}], denoted by P n ( 0), P n ( 00), P n ( 000) {\displaystyle P_{n}(0),P_{n}(00),P_{n}(000)}[image: {\displaystyle P_{n}(0),P_{n}(00),P_{n}(000)}] and P n ( 010) {\displaystyle P_{n}(010)}[image: {\displaystyle P_{n}(010)}], are given by

P n ( 0) = 1 2 + 1 2 ( 1 − 2 p) G ( n), P n ( 00) = ( 1 2 + 1 2 ( 1 − 2 p) G ( n)) 2, P n ( 000) = ( 1 4 + 1 2 ( 1 − 2 p) G ( n) + 1 4 ( 1 − 2 p) G ( n + 1)) ( 1 2 + 1 2 ( 1 − 2 p) G ( n)), P n ( 010) = 1 8 + 1 8 ( 1 − 2 p) G ( n) + 1 8 ( 1 − 2 p) G ( n + 1) − 1 4 ( 1 − 2 p) 2 G ( n) − 1 8 ( 1 − 2 p) G ( n + 1) + G ( n). {\displaystyle {\begin{aligned}P_{n}(0)&={\frac {1}{2}}+{\frac {1}{2}}\,\left(1-2\,p\right)^{G\left(n\right)},\\P_{n}(00)&=\left({\frac {1}{2}}+{\frac {1}{2}}\,\left(1-2\,p\right)^{G\left(n\right)}\right)^{2},\\P_{n}(000)&=\left({\frac {1}{4}}+{\frac {1}{2}}\,\left(1-2\,p\right)^{G\left(n\right)}+{\frac {1}{4}}\,\left(1-2\,p\right)^{G\left(n+1\right)}\right)\left({\frac {1}{2}}+{\frac {1}{2}}\,\left(1-2\,p\right)^{G\left(n\right)}\right),\\P_{n}(010)&={\frac {1}{8}}+{\frac {1}{8}}\,\left(1-2\,p\right)^{G\left(n\right)}+{\frac {1}{8}}\,\left(1-2\,p\right)^{G\left(n+1\right)}-{\frac {1}{4}}\,\left(1-2\,p\right)^{2\,G\left(n\right)}\\&-{\frac {1}{8}}\,\left(1-2\,p\right)^{G\left(n+1\right)+G\left(n\right)}.\end{aligned}}}[image: {\displaystyle {\begin{aligned}P_{n}(0)&={\frac {1}{2}}+{\frac {1}{2}}\,\left(1-2\,p\right)^{G\left(n\right)},\\P_{n}(00)&=\left({\frac {1}{2}}+{\frac {1}{2}}\,\left(1-2\,p\right)^{G\left(n\right)}\right)^{2},\\P_{n}(000)&=\left({\frac {1}{4}}+{\frac {1}{2}}\,\left(1-2\,p\right)^{G\left(n\right)}+{\frac {1}{4}}\,\left(1-2\,p\right)^{G\left(n+1\right)}\right)\left({\frac {1}{2}}+{\frac {1}{2}}\,\left(1-2\,p\right)^{G\left(n\right)}\right),\\P_{n}(010)&={\frac {1}{8}}+{\frac {1}{8}}\,\left(1-2\,p\right)^{G\left(n\right)}+{\frac {1}{8}}\,\left(1-2\,p\right)^{G\left(n+1\right)}-{\frac {1}{4}}\,\left(1-2\,p\right)^{2\,G\left(n\right)}\\&-{\frac {1}{8}}\,\left(1-2\,p\right)^{G\left(n+1\right)+G\left(n\right)}.\end{aligned}}}]

where G ( n) {\displaystyle G(n)}[image: {\displaystyle G(n)}] is the [Gould's sequence][15],

G ( n) = ∑ k = 0 n ( ( n k) mod 2). {\displaystyle G(n)=\sum _{k=0}^{n}\left({n \choose k}\mod 2\right).}[image: {\displaystyle G(n)=\sum _{k=0}^{n}\left({n \choose k}\mod 2\right).}]

The remaining probabilities of blocks of length 1, 2 and 3 can be obtained using Kolmogorov consistency conditions, [11]

P ( 1) = 1 − P ( 0), P ( 01) = P ( 0) − P ( 00), P ( 10) = P ( 0) − P ( 00), P ( 11) = 1 − 2 P ( 0) + P ( 00), P ( 001) = P ( 00) − P ( 000), P ( 011) = P ( 0) − P ( 00) − P ( 010), P ( 100) = P ( 00) − P ( 000), P ( 101) = P ( 0) − 2 P ( 00) + P ( 000), P ( 110) = P ( 0) − P ( 00) − P ( 010), P ( 111) = 1 − 3 P ( 0) + 2 P ( 00) + P ( 010). {\displaystyle {\begin{aligned}P(1)&=1-P(0),\\P(01)&=P(0)-P(00),\\P(10)&=P(0)-P(00),\\P(11)&=1-2P(0)+P(00),\\P(001)&=P(00)-P(000),\\P(011)&=P(0)-P(00)-P(010),\\P(100)&=P(00)-P(000),\\P(101)&=P(0)-2P(00)+P(000),\\P(110)&=P(0)-P(00)-P(010),\\P(111)&=1-3P(0)+2P(00)+P(010).\end{aligned}}}[image: {\displaystyle {\begin{aligned}P(1)&=1-P(0),\\P(01)&=P(0)-P(00),\\P(10)&=P(0)-P(00),\\P(11)&=1-2P(0)+P(00),\\P(001)&=P(00)-P(000),\\P(011)&=P(0)-P(00)-P(010),\\P(100)&=P(00)-P(000),\\P(101)&=P(0)-2P(00)+P(000),\\P(110)&=P(0)-P(00)-P(010),\\P(111)&=1-3P(0)+2P(00)+P(010).\end{aligned}}}]

### Stunted trees and triangular clearings

[[edit][36]]

[37] A forest of stunted trees. This is a time-space diagram, but with time running upwards, not downwards. Interestingly, the fifth tree did not sprout in both directions despite being able to.

The Rule 90 automaton (in its equivalent form on one of the two independent subsets of alternating cells) was investigated in the early 1970s, in an attempt to gain additional insight into [Gilbreath's conjecture][13] on the differences of consecutive [prime numbers][38]. In the triangle of numbers generated from the primes by repeatedly applying the [forward difference operator][39], it appears that most values are either 0 or 2. In particular, Gilbreath's conjecture asserts that the leftmost values in each row of this triangle are all 0 or 2. When a contiguous subsequence of values in one row of the triangle are all 0 or 2, then Rule 90 can be used to determine the corresponding subsequence in the next row. Miller (1970) explained the rule by a metaphor of tree growth in a forest, entitling his paper on the subject "Periodic forests of stunted trees". In this metaphor, a tree begins growing at each position of the initial configuration whose value is 1, and this forest of trees then grows simultaneously, to a new height above the ground at each time step. Each nonzero cell at each time step represents a position that is occupied by a growing tree branch. At each successive time step, a branch can grow into one of the two cells above it to its left and right only when there is no other branch competing for the same cell. A forest of trees growing according to these rules has exactly the same behavior as Rule 90. [12]

From any initial configuration of Rule 90, one may form a [mathematical forest][40], a [directed acyclic graph][41] in which every [vertex][42] has at most one outgoing edge, whose trees are the same as the trees in Miller's metaphor. The forest has a vertex for each pair (*x*,*i*) such that cell *x*is nonzero at time *i*. The vertices at time 0 have no outgoing edges; each one forms the root of a tree in the forest. For each vertex (*x*,*i*) with *i*nonzero, its outgoing edge goes to (*x*± 1, *i*− 1), the unique nonzero neighbor of *x*in time step *i*− 1. Miller observed that these forests develop triangular "clearings", regions of the time-space diagram with no nonzero cells bounded by a flat bottom edge and diagonal sides. Such a clearing is formed when a consecutive sequence of cells becomes zero simultaneously in one time step, and then (in the tree metaphor) branches grow inwards, eventually re-covering the cells of the sequence. [12]

For random initial conditions, the boundaries between the trees formed in this way themselves shift in a seemingly random pattern, and trees frequently die out altogether. But by means of the theory of [shift registers][43] he and others were able to find initial conditions in which the trees all remain alive forever, the pattern of growth repeats periodically, and all of the clearings can be guaranteed to remain bounded in size. [12] [13] Miller used these repeating patterns to form the designs of [tapestries][18]. Some of Miller's tapestries depict physical trees; others visualize the Rule 90 automaton using abstract patterns of triangles. [12]

### Sierpiński triangle

[[edit][44]]

[45] [Sierpiński triangle][9] generated by Rule 90

The time-space diagram of Rule 90 is a plot in which the *i*th row records the configuration of the automaton at step *i*. When the initial state has a single nonzero cell, this diagram has the appearance of the [Sierpiński triangle][9], a [fractal][46] formed by combining [triangles][47] into larger triangles. Rules 18, 22, 26, 82, 146, 154, 210 and 218 also generate Sierpinski triangles from a single cell, however not all of these are created completely identically. One way to explain this structure uses the fact that, in Rule 90, each cell is the [exclusive or][6] of its two neighbors. Because this is equivalent to [modulo][48] -2 addition, this generates the modulo-2 version of [Pascal's triangle][49]. The diagram has a 1 wherever Pascal's triangle has an [odd number][50], and a 0 wherever Pascal's triangle has an [even number][51]. This is a discrete version of the Sierpiński triangle. [1] [14]

The number of live cells in each row of this pattern is a [power of two][16]. In the *i*th row, it equals ''k''</sup>"}},"i":0}}]}'>2*k*, where *k*is the number of nonzero digits in the [binary representation][29] of the number*i*. The sequence of these numbers of live cells,

1, 2, 2, 4, 2, 4, 4, 8, 2, 4, 4, 8, 4, 8, 8, 16, 2, 4, 4, 8, 4, 8, 8, 16, 4, 8, 8, 16, 8, 16, 16, 32, ... (sequence [A001316][52] in the [OEIS][53])

is known as [Gould's sequence][15]. The single live cell of the starting configuration is a [sawtooth pattern][54]. This means that in some time steps the numbers of live cells grow arbitrarily large while in others they return to only two live cells, infinitely often. The growth rate of this pattern has a characteristic growing [sawtooth wave][55] shape that can be used to recognize physical processes that behave similarly to Rule 90. [4]

The Sierpiński triangle also occurs in a more subtle way in the evolution of any configuration in Rule 90. At any time step *i*in the Rule's evolution, the state of any cell can be calculated as the exclusive or of a subset of the cells in the initial configuration. That subset has the same shape as the *i*th row of the Sierpiński triangle. [15]

### Replication

[[edit][56]]

In the Sierpiński triangle, for any integer *i*, the rows numbered by multiples of ''i''</sup>"}},"i":0}}]}'>2*i*have nonzero cells spaced at least ''i''</sup>"}},"i":0}}]}'>2*i*units apart. Therefore, because of the additive property of Rule 90, if an initial configuration consists of a finite pattern *P*of nonzero cells with width less than ''i''</sup>"}},"i":0}}]}'>2*i*, then in steps that are multiples of ''i''</sup>"}},"i":0}}]}'>2*i*, the configuration will consist of copies of *P*spaced at least ''i''</sup>"}},"i":0}}]}'>2*i*units from start to start. This spacing is wide enough to prevent the copies from interfering with each other. The number of copies is the same as the number of nonzero cells in the corresponding row of the Sierpiński triangle. Thus, in this rule, every pattern is a [replicator][10]: it generates multiple copies of itself that spread out across the configuration, eventually filling the whole array. Other rules including the [Von Neumann universal constructor][57], [Codd's cellular automaton][58], and [Langton's loops][59] also have replicators that work by carrying and copying a sequence of instructions for building themselves. In contrast, the replication in Rule 90 is trivial and automatic. [16]

### Predecessors and Gardens of Eden

[[edit][60]]

In Rule 90, on an infinite one-dimensional lattice, every configuration has exactly four predecessor configurations. This is because, in a predecessor, any two consecutive cells may have any combination of states, but once those two cells' states are chosen, there is only one consistent choice for the states of the remaining cells. Therefore, there is no [Garden of Eden][20] in Rule 90, a configuration with no predecessors. The Rule 90 configuration consisting of a single nonzero cell (with all other cells zero) has no predecessors that have finitely many nonzeros. However, this configuration is not a Garden of Eden because it does have predecessors with infinitely many nonzeros. [17]

The fact that every configuration has a predecessor may be summarized by saying that Rule 90 is [surjective][61]. The function that maps each configuration to its successor is, mathematically, a surjective function. Rule 90 is also not [injective][62]. In an injective rule, every two different configurations have different successors, but Rule 90 has pairs of configurations with the same successor. Rule 90 provides an example of a cellular automaton that is surjective but not injective. The [Garden of Eden theorem][20] of Moore and Myhill implies that every injective cellular automaton must be surjective, but this example shows that the converse is not true. [17] [18]

Because each configuration has only a bounded number of predecessors, the evolution of Rule 90 preserves the [entropy][63] of any configuration. In particular, if an infinite initial configuration is selected by choosing the state of each cell independently at random, with each of the two states being equally likely to be selected, then each subsequent configuration can be described by exactly the same probability distribution. [2]

## Emulation by other systems

[[edit][64]]

[65] The bowtie pasta replicator in HighLife, one-dimensional arrays of which can be used to emulate Rule 90

Many other cellular automata and other computational systems are capable of emulating the behavior of Rule 90. For instance, a configuration in rule 90 may be translated into a configuration into the different elementary cellular automaton Rule 22. The translation replaces each Rule 90 cell by three consecutive Rule 22 cells. These cells are all zero if the Rule 90 cell is itself zero. A nonzero Rule 90 cell is translated into a one followed by two zeros. With this transformation, every six steps of the Rule 22 automaton simulate a single step of the Rule 90 automaton. Similar direct simulations of Rule 90 are also possible for the elementary cellular automata Rule 45 and Rule 126, for certain [string rewriting systems][66] and [tag systems][67], and in some two-dimensional cellular automata including [Wireworld][68]. Rule 90 can also simulate itself in the same way. If each cell of a Rule 90 configuration is replaced by a pair of consecutive cells, the first containing the original cell's value and the second containing zero, then this doubled configuration has the same behavior as the original configuration at half the speed. [19]

Various other cellular automata are known to support replicators, patterns that make copies of themselves, and most share the same behavior as in the tree growth model for Rule 90. A new copy is placed to either side of the replicator pattern, as long as the space there is empty. However, if two replicators both attempt to copy themselves into the same position, then the space remains blank. In either case the replicators themselves vanish, leaving their copies to carry on the replication. A standard example of this behavior is the "bowtie pasta" pattern in the two-dimensional [HighLife][69] rule. This rule behaves in many ways like Conway's Game of Life, but such a small replicator does not exist in Life. Whenever an automaton supports replicators with the same growth pattern, one-dimensional arrays of replicators can be used to simulate Rule 90. [20] Rule 90 (on finite rows of cells) can also be simulated by the block [oscillators][70] of the two-dimensional [Life-like</span> cellular automaton"}]]}'>Life-like cellular automaton][71] B36/S125, also called "2x2", and the behavior of Rule 90 can be used to characterize the possible periods of these oscillators. [21]

## See also

[[edit][72]]

- Other elementary cellular automata: [Rule 30][73], [Rule 110][74], and [Rule 184][75]

## References

[[edit][76]]

1. 1 2 3 4 5 [Wolfram, Stephen][7] (1983), ["Statistical mechanics of cellular automata"][77], *Reviews of Modern Physics*, **55**(3): 601– 644, [Bibcode][78]: [1983RvMP...55..601W][79], [doi][80]: [10.1103/RevModPhys.55.601][81], archived from [the original][82] on 2013-09-21, retrieved 2011-02-07.
2. 1 2 3 Martin, Olivier; [Odlyzko, Andrew M.][31]; [Wolfram, Stephen][7] (1984), ["Algebraic properties of cellular automata"][83], *Communications in Mathematical Physics*, **93**(2): 219– 258, [Bibcode][78]: [1984CMaPh..93..219M][84], [doi][80]: [10.1007/BF01223745][85], [S2CID][86] [6900060][87], archived from [the original][88] on 2012-09-10, retrieved 2011-02-07.
3. ↑ [Wolfram, Stephen][7] (2002), **[A New Kind of Science][89], Wolfram Media. The book's index lists over 50 distinct subtopics for Rule 90.
4. 1 2 &nbsp;''α''</sup> spectra"},"journal":{"wt":"Physical Review E"},"volume":{"wt":"70"},"year":{"wt":"2004"},"issue":{"wt":"3"},"article-number":{"wt":"032101"},"doi":{"wt":"10.1103/PhysRevE.70.032101"},"pmid":{"wt":"15524560"},"arxiv":{"wt":"cond-mat/0308277"},"bibcode":{"wt":"2004PhRvE..70c2101C"},"s2cid":{"wt":"39929111"}},"i":0}}]}'/> Claussen, Jens Christian; Nagler, Jan; Schuster, Heinz Georg (2004), "Sierpinski signal generates 1/*f**α*spectra", *Physical Review E*, **70**(3) 032101, [arXiv][90]: [cond-mat/0308277][91], [Bibcode][78]: [2004PhRvE..70c2101C][92], [doi][80]: [10.1103/PhysRevE.70.032101][93], [PMID][94] [15524560][95], [S2CID][86] [39929111][96].
5. ↑ Misiurewicz, Michał; Stevens, John G.; [Thomas, Diana M.][97] (2006), "Iterations of linear maps over finite fields", *Linear Algebra and Its Applications*, **413**(1): 218– 234, [doi][80]: [10.1016/j.laa.2005.09.002][98].
6. ↑ [McIntosh, Harold V.][99] (1993), **[Ancestors: Commentaries on "The Global Dynamics of Cellular Automata" by Andrew Wuensche and Mike Lesser (Addison-Wesley, 1992)][100] (PDF), Instituto de Ciencias, Universidad Autónoma de Puebla.
7. ↑ Kawaharada, Akane (2014), "Ulam's cellular automaton and Rule 150", *Hokkaido Mathematical Journal*, **43**(3): 361– 383, [doi][80]: [10.14492/hokmj/1416837570][101], [MR][102] [3282639][103]: "Except for trivial CAs the other four linear elementary CAs, Rule 60, Rule 90, Rule 102 and Rule 150, are either essentially equivalent to Rule 90 or Rule 150."
8. ↑ Fukś, Henryk (2023), *Solvable Cellular Automata: Methods and Applications*, [Springer][104], [doi][80]: [10.1007/978-3-031-38700-5][105], [ISBN][106] [978-3-031-38699-2][107]: See sec. 3.2
9. ↑ Fukś, Henryk (2025). ["List of deterministic solution formulae for elementary CA"][108].
10. ↑ See sec. 8.6 of Fukś (2023).
11. ↑ See sec. 7.6 of Fukś (2023).
12. 1 2 3 4 [Miller, J. C. P.][109] (1970), "Periodic forests of stunted trees", *Philosophical Transactions of the Royal Society of London*, Series A, Mathematical and Physical Sciences, **266**(1172): 63– 111, [Bibcode][78]: [1970RSPTA.266...63M][110], [doi][80]: [10.1098/rsta.1970.0003][111], [JSTOR][112] [73779][113], [S2CID][86] [123330469][114].
13. ↑ ApSimon, H. G. (1970), "Periodic forests whose largest clearings are of size 3", *Philosophical Transactions of the Royal Society of London*, Series A, Mathematical and Physical Sciences, **266**(1172): 113– 121, [Bibcode][78]: [1970RSPTA.266..113A][115], [doi][80]: [10.1098/rsta.1970.0004][116], [JSTOR][112] [73780][117], [S2CID][86] [121067116][118]; ApSimon, H. G. (1970), "Periodic forests whose largest clearings are of size *n*≥ 4", *Philosophical Transactions of the Royal Society of London*, Series A, Mathematical and Physical Sciences, **266**(1538): 399– 404, [Bibcode][78]: [1970RSPSA.319..399A][119], [doi][80]: [10.1098/rspa.1970.0185][120], [JSTOR][112] [73780][117], [S2CID][86] [119435085][121]. A similar analysis of periodic configurations in Rule 90 also appears in Wolfram (2002), p. 954.
14. ↑ Wolfram (2002), pp. 25–26, 270–271, 870.
15. ↑ Kar, B. K.; Gupta, A.; Chaudhuri, P. Pal (1993), "On explicit expressions in additive cellular automata theory", *Information Sciences*, **72**( 1– 2): 83– 103, [doi][80]: [10.1016/0020-0255(93)90030-P][122].
16. ↑ Waksman, Abraham (1969), "A model of replication", *[Journal of the ACM][123]*, **16**(1): 178– 188, [doi][80]: [10.1145/321495.321509][124], [S2CID][86] [14547972][125]; Amoroso, Serafino; Cooper, Gerald (1971), "Tessellation structures for reproduction of arbitrary patterns", *Journal of Computer and System Sciences*, **5**(5): 455– 464, [doi][80]: [10.1016/S0022-0000(71)80009-0][126]. Wolfram (1983) (Fig.33 and surrounding text) also mentions the same property, and as well as citing Waksman, Amoroso, and Cooper he credits its observation to unpublished work by [Edward Fredkin][127] in 1981.
17. 1 2 Skyum, Sven (1975), "Confusion in the Garden of Eden", *[Proceedings of the American Mathematical Society][128]*, **50**(1): 332– 336, [doi][80]: [10.1090/S0002-9939-1975-0386350-1][129]
18. ↑ Sutner, Klaus (1991), ["De Bruijn Graphs and Linear Cellular Automata"][130] (PDF), *Complex Systems*, **5**: 19– 30. Wolfram (2002), pp. 959–960. Martin, Odlyzko & Wolfram (1984) provide a similar analysis of the predecessors of the same rule for finite sets of cells with periodic boundary conditions.
19. ↑ Wolfram (2002), pp. 269–270, 666–667, 701–702, 1117.
20. ↑ Griffeath, David (1996), "Recipe for the week of July 1–7: Replicating Skeeters", **[The Primordial Soup Kitchen][131].
21. ↑ Johnston, Nathaniel (2010), "The B36/S125 "2x2" Life-like cellular automaton", in [Adamatzky, Andrew][132] (ed.), *Game of Life Cellular Automata*, Springer-Verlag, pp. 99– 114, [arXiv][90]: [1203.1644][133], [Bibcode][78]: [2010golc.book...99J][134], [doi][80]: [10.1007/978-1-84996-217-9_7][135], [S2CID][86] [41344677][136].

## External links

[[edit][137]]

- [Weisstein, Eric W.][138], ["Rule 90"][139], *[MathWorld][140]*
- [Rule 90 in Wolfram's atlas of cellular automata][141]

- [v][142]
- [t][143]
- [e][144]

[Conway's Game of Life][19] and related [cellular automata][4]

 |

Structures |

- [Breeder][145]
- [Garden of Eden][20]
- [Glider][146]
- [Gun][147]
- [Methuselah][148]
- [Oscillator][70]
- [Puffer train][149]
- [Rake][150]
- [Reflector][151]
- [Replicator][10]
- [Sawtooth][54]
- [Spacefiller][152]
- [Spaceship][153]
- [Spark][154]
- [Still life][155]

 |

[Life variants][71] |

- [Day and Night][156]
- [Highlife][69]
- [Lenia][157]
- [Life without Death][158]
- [Seeds][159]

 |

Concepts |

- [Moore neighborhood][160]
- [Speed of light][161]
- [Von Neumann neighborhood][162]

 |

Implementations |

- [Golly][163]
- *[Life Genesis][164]*
- *[Video Life][165]*
- *[Anonymous;Code][166]*

 |

Key people |

- [John Conway][167]
- [Martin Gardner][168]
- [Bill Gosper][169]
- [Richard Guy][170]

 |

Websites |

- [LifeWiki][171]

 |

Popular culture |

- *[Bloom][172]*
- *[Wake][173]*

 |

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Rule_90&oldid=1336595066][174] "

[Categories][175]:

- [Cellular automaton rules][176]
- [Wolfram code][177]

Hidden categories:

- [Articles with short description][178]
- [Short description is different from Wikidata][179]
- [Good articles][180]

Search

Rule 90

4 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/Wikipedia:Good_articles*
[2]: https://en.wikipedia.org/wiki/File:R090_rand_0.png
[3]: https://en.wikipedia.org/wiki/Mathematics
[4]: https://en.wikipedia.org/wiki/Cellular_automaton
[5]: https://en.wikipedia.org/wiki/Elementary_cellular_automaton
[6]: https://en.wikipedia.org/wiki/Exclusive_or
[7]: https://en.wikipedia.org/wiki/Stephen_Wolfram
[8]: https://en.wikipedia.org/wiki/A_New_Kind_of_Science
[9]: https://en.wikipedia.org/wiki/Sierpiński_triangle
[10]: https://en.wikipedia.org/wiki/Replicator_(cellular_automaton)
[11]: https://en.wikipedia.org/wiki/Random
[12]: https://en.wikipedia.org/wiki/Number_theory
[13]: https://en.wikipedia.org/wiki/Gilbreath's_conjecture
[14]: https://en.wikipedia.org/wiki/Prime_numbers
[15]: https://en.wikipedia.org/wiki/Gould's_sequence
[16]: https://en.wikipedia.org/wiki/Power_of_two
[17]: https://en.wikipedia.org/wiki/Binary_representation
[18]: https://en.wikipedia.org/wiki/Tapestry
[19]: https://en.wikipedia.org/wiki/Conway's_Game_of_Life
[20]: https://en.wikipedia.org/wiki/Garden_of_Eden_(cellular_automaton)
[21]: https://en.wikipedia.org/wiki/Surjective
[22]: https://en.wikipedia.org/wiki/Injective
[23]: https://en.wikipedia.org/wiki/Garden_of_Eden_theorem
[24]: /w/index.php?title=Rule_90&amp;action=edit&amp;section=1
[25]: /w/index.php?title=Rule_90&amp;action=edit&amp;section=2
[26]: https://en.wikipedia.org/wiki/File:Rule_90_gate_array.svg
[27]: /w/index.php?title=Rule_90&amp;action=edit&amp;section=3
[28]: https://en.wikipedia.org/wiki/Wolfram_code
[29]: https://en.wikipedia.org/wiki/Binary_number
[30]: https://en.wikipedia.org/wiki/Decimal
[31]: https://en.wikipedia.org/wiki/Andrew_Odlyzko
[32]: /w/index.php?title=Rule_90&amp;action=edit&amp;section=4
[33]: /w/index.php?title=Rule_90&amp;action=edit&amp;section=5
[34]: /w/index.php?title=Rule_90&amp;action=edit&amp;section=6
[35]: /w/index.php?title=Rule_90&amp;action=edit&amp;section=7
[36]: /w/index.php?title=Rule_90&amp;action=edit&amp;section=8
[37]: https://en.wikipedia.org/wiki/File:Rule_90_trees.svg
[38]: https://en.wikipedia.org/wiki/Prime_number
[39]: https://en.wikipedia.org/wiki/Forward_difference_operator
[40]: https://en.wikipedia.org/wiki/Tree_(graph_theory)
[41]: https://en.wikipedia.org/wiki/Directed_acyclic_graph
[42]: https://en.wikipedia.org/wiki/Vertex_(graph_theory)
[43]: https://en.wikipedia.org/wiki/Shift_register
[44]: /w/index.php?title=Rule_90&amp;action=edit&amp;section=9
[45]: https://en.wikipedia.org/wiki/File:R090_pulse_wide.png
[46]: https://en.wikipedia.org/wiki/Fractal
[47]: https://en.wikipedia.org/wiki/Triangle
[48]: https://en.wikipedia.org/wiki/Modular_arithmetic
[49]: https://en.wikipedia.org/wiki/Pascal's_triangle
[50]: https://en.wikipedia.org/wiki/Odd_number
[51]: https://en.wikipedia.org/wiki/Even_number
[52]: //oeis.org/A001316
[53]: https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences
[54]: https://en.wikipedia.org/wiki/Sawtooth_(cellular_automaton)
[55]: https://en.wikipedia.org/wiki/Sawtooth_wave
[56]: /w/index.php?title=Rule_90&amp;action=edit&amp;section=10
[57]: https://en.wikipedia.org/wiki/Von_Neumann_universal_constructor
[58]: https://en.wikipedia.org/wiki/Codd's_cellular_automaton
[59]: https://en.wikipedia.org/wiki/Langton's_loops
[60]: /w/index.php?title=Rule_90&amp;action=edit&amp;section=11
[61]: https://en.wikipedia.org/wiki/Surjective_function
[62]: https://en.wikipedia.org/wiki/Injective_function
[63]: https://en.wikipedia.org/wiki/Entropy
[64]: /w/index.php?title=Rule_90&amp;action=edit&amp;section=12
[65]: https://en.wikipedia.org/wiki/File:Highlife_replicator.png
[66]: https://en.wikipedia.org/wiki/String_rewriting_system
[67]: https://en.wikipedia.org/wiki/Tag_system
[68]: https://en.wikipedia.org/wiki/Wireworld
[69]: https://en.wikipedia.org/wiki/Highlife_(cellular_automaton)
[70]: https://en.wikipedia.org/wiki/Oscillator_(cellular_automaton)
[71]: https://en.wikipedia.org/wiki/Life-like_cellular_automaton
[72]: /w/index.php?title=Rule_90&amp;action=edit&amp;section=13
[73]: https://en.wikipedia.org/wiki/Rule_30
[74]: https://en.wikipedia.org/wiki/Rule_110
[75]: https://en.wikipedia.org/wiki/Rule_184
[76]: /w/index.php?title=Rule_90&amp;action=edit&amp;section=14
[77]: https://web.archive.org/web/20130921060232/http://www.stephenwolfram.com/publications/articles/ca/83-statistical/
[78]: https://en.wikipedia.org/wiki/Bibcode_(identifier)
[79]: https://ui.adsabs.harvard.edu/abs/1983RvMP...55..601W
[80]: https://en.wikipedia.org/wiki/Doi_(identifier)
[81]: https://doi.org/10.1103%2FRevModPhys.55.601
[82]: http://www.stephenwolfram.com/publications/articles/ca/83-statistical/
[83]: https://web.archive.org/web/20120910140310/http://www.stephenwolfram.com/publications/articles/ca/84-properties/
[84]: https://ui.adsabs.harvard.edu/abs/1984CMaPh..93..219M
[85]: https://doi.org/10.1007%2FBF01223745
[86]: https://en.wikipedia.org/wiki/S2CID_(identifier)
[87]: https://api.semanticscholar.org/CorpusID:6900060
[88]: http://www.stephenwolfram.com/publications/articles/ca/84-properties/
[89]: https://www.wolframscience.com/nks/
[90]: https://en.wikipedia.org/wiki/ArXiv_(identifier)
[91]: https://arxiv.org/abs/cond-mat/0308277
[92]: https://ui.adsabs.harvard.edu/abs/2004PhRvE..70c2101C
[93]: https://doi.org/10.1103%2FPhysRevE.70.032101
[94]: https://en.wikipedia.org/wiki/PMID_(identifier)
[95]: https://pubmed.ncbi.nlm.nih.gov/15524560
[96]: https://api.semanticscholar.org/CorpusID:39929111
[97]: https://en.wikipedia.org/wiki/Diana_Thomas_(mathematician)
[98]: https://doi.org/10.1016%2Fj.laa.2005.09.002
[99]: https://en.wikipedia.org/wiki/Harold_V._McIntosh
[100]: http://delta.cs.cinvestav.mx/~mcintosh/comun/wandl/global.pdf
[101]: https://doi.org/10.14492%2Fhokmj%2F1416837570
[102]: https://en.wikipedia.org/wiki/MR_(identifier)
[103]: https://mathscinet.ams.org/mathscinet-getitem?mr=3282639
[104]: https://en.wikipedia.org/wiki/Springer_Publishing
[105]: https://doi.org/10.1007%2F978-3-031-38700-5
[106]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[107]: https://en.wikipedia.org/wiki/Special:BookSources/978-3-031-38699-2
[108]: https://lie.ac.brocku.ca/~hfuks/solvableca.html
[109]: https://en.wikipedia.org/wiki/J._C._P._Miller
[110]: https://ui.adsabs.harvard.edu/abs/1970RSPTA.266...63M
[111]: https://doi.org/10.1098%2Frsta.1970.0003
[112]: https://en.wikipedia.org/wiki/JSTOR_(identifier)
[113]: https://www.jstor.org/stable/73779
[114]: https://api.semanticscholar.org/CorpusID:123330469
[115]: https://ui.adsabs.harvard.edu/abs/1970RSPTA.266..113A
[116]: https://doi.org/10.1098%2Frsta.1970.0004
[117]: https://www.jstor.org/stable/73780
[118]: https://api.semanticscholar.org/CorpusID:121067116
[119]: https://ui.adsabs.harvard.edu/abs/1970RSPSA.319..399A
[120]: https://doi.org/10.1098%2Frspa.1970.0185
[121]: https://api.semanticscholar.org/CorpusID:119435085
[122]: https://doi.org/10.1016%2F0020-0255%2893%2990030-P
[123]: https://en.wikipedia.org/wiki/Journal_of_the_ACM
[124]: https://doi.org/10.1145%2F321495.321509
[125]: https://api.semanticscholar.org/CorpusID:14547972
[126]: https://doi.org/10.1016%2FS0022-0000%2871%2980009-0
[127]: https://en.wikipedia.org/wiki/Edward_Fredkin
[128]: https://en.wikipedia.org/wiki/Proceedings_of_the_American_Mathematical_Society
[129]: https://doi.org/10.1090%2FS0002-9939-1975-0386350-1
[130]: https://www.complex-systems.com/pdf/05-1-3.pdf
[131]: http://psoup.math.wisc.edu/archive/recipe75.html
[132]: https://en.wikipedia.org/wiki/Andrew_Adamatzky
[133]: https://arxiv.org/abs/1203.1644
[134]: https://ui.adsabs.harvard.edu/abs/2010golc.book...99J
[135]: https://doi.org/10.1007%2F978-1-84996-217-9_7
[136]: https://api.semanticscholar.org/CorpusID:41344677
[137]: /w/index.php?title=Rule_90&amp;action=edit&amp;section=15
[138]: https://en.wikipedia.org/wiki/Eric_W._Weisstein
[139]: https://mathworld.wolfram.com/Rule90.html
[140]: https://en.wikipedia.org/wiki/MathWorld
[141]: https://atlas.wolfram.com/01/01/90/
[142]: https://en.wikipedia.org/wiki/Template:Conway's_Game_of_Life
[143]: https://en.wikipedia.org/wiki/Template_talk:Conway's_Game_of_Life
[144]: https://en.wikipedia.org/wiki/Special:EditPage/Template:Conway's_Game_of_Life
[145]: https://en.wikipedia.org/wiki/Breeder_(cellular_automaton)
[146]: https://en.wikipedia.org/wiki/Glider_(Conway's_Game_of_Life)
[147]: https://en.wikipedia.org/wiki/Gun_(cellular_automaton)
[148]: https://en.wikipedia.org/wiki/Methuselah_(cellular_automaton)
[149]: https://en.wikipedia.org/wiki/Puffer_train
[150]: https://en.wikipedia.org/wiki/Rake_(cellular_automaton)
[151]: https://en.wikipedia.org/wiki/Reflector_(cellular_automaton)
[152]: https://en.wikipedia.org/wiki/Spacefiller
[153]: https://en.wikipedia.org/wiki/Spaceship_(cellular_automaton)
[154]: https://en.wikipedia.org/wiki/Spark_(cellular_automaton)
[155]: https://en.wikipedia.org/wiki/Still_life_(cellular_automaton)
[156]: https://en.wikipedia.org/wiki/Day_and_Night_(cellular_automaton)
[157]: https://en.wikipedia.org/wiki/Lenia
[158]: https://en.wikipedia.org/wiki/Life_without_Death
[159]: https://en.wikipedia.org/wiki/Seeds_(cellular_automaton)
[160]: https://en.wikipedia.org/wiki/Moore_neighborhood
[161]: https://en.wikipedia.org/wiki/Speed_of_light_(cellular_automaton)
[162]: https://en.wikipedia.org/wiki/Von_Neumann_neighborhood
[163]: https://en.wikipedia.org/wiki/Golly_(program)
[164]: https://en.wikipedia.org/wiki/Life_Genesis
[165]: https://en.wikipedia.org/wiki/Video_Life
[166]: https://en.wikipedia.org/wiki/Anonymous;Code
[167]: https://en.wikipedia.org/wiki/John_Horton_Conway
[168]: https://en.wikipedia.org/wiki/Martin_Gardner
[169]: https://en.wikipedia.org/wiki/Bill_Gosper
[170]: https://en.wikipedia.org/wiki/Richard_K._Guy
[171]: https://en.wikipedia.org/wiki/LifeWiki
[172]: https://en.wikipedia.org/wiki/Bloom_(novel)
[173]: https://en.wikipedia.org/wiki/Wake_(Sawyer_novel)
[174]: https://en.wikipedia.org/w/index.php?title=Rule_90&amp;oldid=1336595066
[175]: /wiki/Help:Category
[176]: /wiki/Category:Cellular_automaton_rules
[177]: /wiki/Category:Wolfram_code
[178]: /wiki/Category:Articles_with_short_description
[179]: /wiki/Category:Short_description_is_different_from_Wikidata
[180]: /wiki/Category:Good_articles
