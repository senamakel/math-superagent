# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. So what is here is what the run knows without going to look, and
what is missing is what each agent rediscovers separately.

It has a token budget (`MATH_AGENT_CONTEXT_TOKENS`, 10,000 default). The file is
re-sent on every model call in every role that reads it, so length here is a
bill the whole run pays many times over. Link the file that still holds any
detail compressed away. Durable findings belong in Cognee. A statement nobody
can trace to a source is worth less than no statement.

## Established

Every claim marked with its evidence class; all anchors are in this workspace.

- **(proved) No odd unitary perfect number.** Every UP `n = 2^a·m`, `a ≥ 1`.
  Proof is three lines (v2 argument) in `research/notes/parity-and-2-adic-budget.md`.
  Subbarao–Warren 1966.
- **(proved, checked against all five) 2-adic budget identity**:
  `Σ_i v2(p_i^{e_i}+1) = a + 1`, exactly, for `n = 2^a Π p_i^{e_i}` UP with `p_i`
  odd distinct. Corollary `ω(odd part) ≤ a + 1`, with equality iff every odd
  component `≡ 1 (mod 4)`. This is the elementary form of the paper's
  "2-adic budget overshoot" filter. It bounds `ω` *above*; the open useful
  direction is a **lower** bound on `a` in terms of `ω`, or impossibility of a
  residue class of `a`. `research/notes/parity-and-2-adic-budget.md`.
- **(computed/checked) Witness set = the five known numbers**, verified by the
  exact-integer oracle `σ*(n) == 2n` with negative controls (12, 28 false):
  `6, 60, 90, 87360, 146361946186458562560000` (last = `2^18·3·5^4·7·11·13·19·37·79·109·157·313`).
  `code/out/known_five_verified.captured.txt`.
- **(computed) All five are divisible by 3.** Whether a sixth must be is open.
  **Sharpest edge of the witness set:** the two non-squarefree kernels are
  `3^2` (in 90) and `5^4` (in the fifth). Any lemma killing repeated odd prime
  powers kills two of the five and is **false** — run every candidate lemma
  against all five before recording it as anything but `asserted`.
- **(sourced) Graham 1989:** unitary perfect numbers with squarefree odd part
  are exactly `6, 60, 87360`. So any sixth example has a **repeated odd prime
  power**.
- **(asserted by abstract only — NOT verified, needs full text)** Maciejewski
  arXiv:2605.20475: any admissible *source kernel* of the odd dependency graph
  is one of `3^2`, `5^4`, or one of **five additional "impostor" kernels**, all
  eliminated for seed classes `1 ≤ a ≤ 10000` by a three-filter certificate
  (Zsigmondy exponent obstructions, inherited non-3-Higgs witnesses, 2-adic
  budget overshoot). It does not prove finiteness. Do not treat the impostor
  kernels or the filters as established until the full text is fetched and the
  claim checked.

## Ruled out

- **The structural backtracking search is CLOSED.** The product form
  `Π (q_i+1)/q_i = 2` with the denominator rule forcing the next prime whenever
  the remaining target is not an integer recovers exactly the five known numbers
  within any bound this container reaches and produces no information at any
  such bound — Wall (1975) cleared past `10^102`. Do not rerun it. The one thing
  worth keeping is the denominator rule as a **divisibility constraint** (if the
  remaining target is `A/B`, every prime dividing `B` divides `n`) — the
  structural content the odd dependency graph is built from; use it forwards, do
  not execute it. `research/notes/why-the-search-is-closed.md`,
  `code/structural_search_CLOSED.py`.
- **Rarity is not finiteness.** A density-zero / `o(x)` / `O(x^ε)` statement
  about UP numbers is almost certainly already known and does not touch the
  question. Say which one you have.

## Numbers

- Oracle: `σ*(n) = Π_{p^a||n}(p^a+1)`, exact integers; `n` UP iff `σ*(n) == 2n`.
  Verified by hand on 6 and on non-UP controls.
- Witness table (a, ω(odd), Σv2, a+1): 6→(1,1,2,2); 60→(2,2,3,3); 90→(1,2,2,2,
  equality); 87360→(6,4,7,7); fifth→(18,11,19,19). Identity exact in all five;
  equality in `ω ≤ a+1` holds only for 90.
- Paper's open branch (abstract): `|H_even ∩ [2,40000]| ≤ 201`,
  `|H_even ∩ [2,50000]| ≤ 272`, where `H_even = { even m : every prime divisor
  of 2^m+1 is 3-Higgs }`. Analytic target named in the paper: a divisor-level
  problem for the cyclotomic values `Φ_{4p}(2)`.

## Recalled

Durable Cognee memory holds **nothing** on this problem yet — `recall_memory`
and `relate_memory` for "unitary perfect number / Subbarao / H_even / 3-Higgs"
both returned empty. Do not re-call expecting prior-run findings. The established
content above is this run's own, from its notes and oracle.

## Contradictions

None identified yet.

## Gaps

- **Full text of arXiv:2605.20475 not fetched — workspace holds abstract only.**
  Needed, all load-bearing and none guessable: the definition of a **3-Higgs**
  prime; the construction of the odd dependency graph; the five impostor
  kernels; the three filters; and the exact divisor-level problem for `Φ_{4p}(2)`
  that the paper names as the analytic target for closing the `H_even` branch.
  Confirm the real text is held by finding the 3-Higgs definition before
  anything else. This is the only place a result is available.
- Open structural question: is `3 | n` forced for a sixth example? (all five have
  it; open.) Both directions are a result.
