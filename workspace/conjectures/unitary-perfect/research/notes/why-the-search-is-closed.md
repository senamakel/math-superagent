# The structural search is closed. Do not reopen it.

The product form `Π_{p^a || n} (1 + 1/p^a) = 2` makes a backtracking search look
tractable, and it is genuinely much better than enumerating `n`. The operator
built it, ran it, and is recording it here **as a closed route** so that this
run does not spend itself rediscovering that it does not reach.

`code/structural_search_CLOSED.py` is the program. The name is the instruction.

## Why it looks tractable

Search sets of prime powers `q_i = p_i^{e_i}` with distinct primes and
`Π (q_i + 1)/q_i = 2`. Track the remaining target `R = A/B` in lowest terms.
Since `B` divides `Π q_i`, **every prime dividing `B` must still be used**. So
whenever `B > 1` the *choice of prime is forced* and only the exponent branches.
Free choice of prime happens only at the rare states where `R` is an integer.
That is a real and strong prune, and it is why the tree looks thin.

## Why it does not reach

It recovers exactly the five known unitary perfect numbers within any bound this
container can run, and nothing else. That is not evidence of anything: **Wall
searched past `10^102` in 1975.** The bound reachable here is smaller by scores
of orders of magnitude, so:

- a negative result from it restates 1975 and is not new;
- a positive result from it is not available, because the region it covers was
  cleared fifty years ago.

The forced-prime prune does not change this. It changes the constant, not the
reach. A search whose covered region is a strict subset of a region already
cleared produces no information at any bound, and "further than before" is not a
property this instrument can have.

The implementation also has a canonical-ordering defect — it emits each solution
several times, once per order in which the free-choice states can produce it
(13 emissions for the 5 solutions at `P = 20`). It is **not worth fixing**.
Fixing it would make a useless instrument tidy.

## What to take from it instead

The denominator rule is the part worth keeping, and it is a statement, not a
program: *if the remaining target is `A/B` then every prime dividing `B` divides
`n`*. Used forwards on a hypothetical sixth example, that is a divisibility
constraint linking the seed `2^a + 1` to the odd components — which is exactly
the "odd dependency graph" that arXiv:2605.20475 builds its reduction on. Read
the paper and use the constraint structurally. Do not run it.

```claim
id: structural-search-cannot-reach
statement: The backtracking search over the product form
  prod (q_i+1)/q_i = 2, with q_i prime powers of distinct primes and the
  denominator rule forcing the next prime whenever the remaining target is not
  an integer, recovers exactly the five known unitary perfect numbers within
  any bound reachable in this container and produces no information at any such
  bound, because Wall (1975) already searched past 10^102. A negative result
  from it restates 1975; a positive result is unavailable since its covered
  region is a strict subset of a region cleared fifty years ago.
hypotheses: the container's compute budget, which is far below 10^102 for this
  enumeration; Wall's search bound as reported in the literature
holds-here: yes for this workspace's instrument. The claim is about reach, not
  about correctness of the search - the program is correct up to a
  canonical-ordering defect that emits each solution several times, which is
  not fixed because the instrument is closed
status: checked
bearing: closes the search route before the run spends itself on it, which is
  the degenerate move this problem offers. Keeps the useful half: the
  denominator rule as a divisibility constraint - if the remaining target is
  A/B then every prime dividing B divides n - which is the structural content
  that the odd dependency graph of arXiv:2605.20475 is built from, to be used
  forwards on a hypothetical sixth example rather than executed
anchor: code/structural_search_CLOSED.py;
  research/notes/why-the-search-is-closed.md
source: operator-computation
```
