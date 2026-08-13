The search is CLOSED before you start. `research/notes/why-the-search-is-closed.md`
records why, with the program beside it under a name that says so. Wall cleared
past `10^102` in 1975 and nothing this container can run reaches a region that
was not cleared then. Reproducing it is the one guaranteed waste available here.

Start by getting the paper. arXiv:2605.20475, Maciejewski, *Bounded-box
reductions in the Subbarao–Warren problem for unitary perfect numbers*, May 2026.
This workspace holds its **abstract only**. The definition of a *3-Higgs* prime,
the construction of the odd dependency graph, the five impostor kernels, and the
three filters are all in the full text and are all load-bearing — every one of
them appears in `problem.md` as a name with no definition behind it. Fetch the
HTML or PDF full text, not the arXiv landing page: a landing page is about six
kilobytes with no occurrence of "theorem" or "lemma" in it, and this repository
has filed abstracts as proved results before. Confirm you have the real text by
finding the definition of 3-Higgs in it before anything else.

Then attack the branch the paper leaves open, which is the only place a result
is available. It is

```
H_even = { even m : every prime divisor of 2^m + 1 is 3-Higgs }
```

with only counting bounds proved — `|H_even ∩ [2,40000]| ≤ 201` and
`|H_even ∩ [2,50000]| ≤ 272`. Finiteness of `H_even` closes the Subbarao–Warren
reduction. The paper names the analytic target: a divisor-level problem for the
cyclotomic values `Φ_{4p}(2)`. That is a concrete question about prime divisors
of `2^m + 1` and it is where a Zsigmondy or cyclotomic argument has room, so it
is where to spend the run.

Three things are already proved here and none of them counts again. Every
unitary perfect number is even; the 2-adic budget identity
`Σ_i v2(p_i^{e_i} + 1) = a + 1` is exact; and its corollary
`ω(odd part) ≤ a + 1`, with equality exactly when every odd component is
`1 mod 4`. All three are in `research/notes/parity-and-2-adic-budget.md`, all
three are proved, and all three are checked against the five known numbers. The
useful direction is the one they do not give: a **lower** bound on `a` in terms
of `ω`, or the impossibility of a residue class of `a`. The identity bounds `ω`
above by `a+1` and says nothing that stops `a` growing.

Graham (1989) settled squarefree odd part — the answer is exactly `6`, `60`,
`87360`. So a sixth example has a repeated odd prime power. The two such kernels
that actually occur are `3^2` in `90` and `5^4` in the fifth example, and the
paper's enumeration says any admissible source kernel is one of those two or one
of five impostors. **This is the sharpest edge of the witness set.** An argument
that rules out repeated odd prime powers kills `90` and the fifth number and is
therefore false; run every candidate lemma against all five before recording it
as anything but `asserted`.

On compute: it is for checking structure, never for finding `n`. Factoring
`2^m + 1` over a stated range of `m`, computing `Φ_{4p}(2)` and its divisors,
reproducing a table from the paper to check it, testing a proposed lemma against
the witness set — all legitimate. Enumerating `n` and testing `σ*(n) = 2n` in any
form is not. Factoring `2^m + 1` is the real cost centre and gets hard fast, so
bound every run as
`timeout 540 python3 <prog> 2>&1 | tee code/out/<name>.captured.txt; echo EXIT_CODE=$?`,
say what range was covered and what was left unfactored, and split `m` across
workers — the box has 28 CPUs and the container has no CPU quota. A partial
factorisation with its bound stated is a result. An unbounded run that gets
killed is not.

Two cautions this problem has earned. Rarity is not finiteness: a density-zero
or `o(x)` statement about unitary perfect numbers is almost certainly known and
does not touch the question, so say which one you have. And the product identity
`Π (1 + 1/p^a) = 2` is exact and elementary, which invites an elementary attack;
every such attack tried so far reduces to a search, so before pursuing one, state
what it does that a search does not.
