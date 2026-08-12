<!-- source: https://www.erdosproblems.com/64 | converted from HTML by download_document -->

# Erdős Problem #64 — Power-of-two cycles

URL: https://www.erdosproblems.com/64
Owner's editorial state: **FALSIFIABLE** — Open, but could be disproved with a finite counterexample. Prize: **$1000**.

## Statement

> Does every finite graph with minimum degree at least 3 contain a cycle of length $2^k$ for some $k\geq 2$?

References tagged: [#64][Er93,p.343] [Er94b] [Er95,p.174] [Er96] [Er97b] [Er97c]. Tags: graph theory, cycles.

## Open-status note

> The open status of this problem reflects the current belief of the owner of this website. There may be literature on this problem that I am unaware of, which may partially or completely solve the stated problem. Please do your own literature search before expending significant effort on solving this problem. If you find any relevant literature not mentioned here, please add this in a comment.

- **No claimed proofs** (partial or complete) in the comments ("0 claimed proofs").
- 2 comments on the problem.

## Remarks

Conjectured by Erdős and Gyárfás, who believed the answer must be negative, and in fact for every $r$ there must be a graph of minimum degree at least $r$ without a cycle of length $2^k$ for any $k\geq 2$.

This was **solved in the affirmative if the minimum degree is larger than some absolute constant by Liu and Montgomery [LiMo20]** (therefore disproving the above stronger conjecture of Erdős and Gyárfás). Liu and Montgomery prove a much stronger result: if the average degree of $G$ is sufficiently large then there is some large integer $\ell$ such that for every even integer $m\in [(\log \ell)^8,\ell]$, $G$ contains a cycle of length $m$.

An infinite tree with minimum degree $3$ shows that the answer is **trivially false for infinite graphs**.

The conjecture has been confirmed for various families of graphs; see the comment by **Alfaiz** for a list.

This problem is **#69 in Extremal Graph Theory** in the graphs problem collection.

## Meta

- Formalised statement? **Yes** — [google-deepmind/formal-conjectures FormalConjectures/ErdosProblems/64.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/64.lean).
- Page last edited **10 April 2026**.
- Problem owner's recommended citation: "T. F. Bloom, Erdős Problem #64, https://www.erdosproblems.com/64, accessed 2026-08-12".
- Additional thanks: Alfaiz, Desmond Weisenberg, Yuval Wigderson.
- LaTeX source endpoint (https://www.erdosproblems.com/latex/64) returns the raw statement LaTeX only.

## Notes for this run

This is the canonical Erdős-problems.com entry for the Erdős–Gyárfás conjecture (the run's central open problem). It confirms: (a) still open as of the last edit (10 Apr 2026); (b) the modern prize is listed as $1000 (note: the older Royle/UCSD wording cites Erdős's original $100 proof / $50 counterexample — the two figures differ and are recorded separately); (c) the Liu–Montgomery [LiMo20] theorem resolves the *stronger* original belief that counterexamples exist for every min-degree r, by proving a power-of-two cycle (indeed all even lengths in a huge range) exists once average degree is large; (d) infinite min-degree-3 trees are (trivial) infinite counterexamples; (e) a Lean formalisation exists upstream (deepmind formal-conjectures #64).
