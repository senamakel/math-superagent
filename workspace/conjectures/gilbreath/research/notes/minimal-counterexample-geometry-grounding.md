# Grounding of `minimal-counterexample-geometry` — the SMT/unsatisfiability approach to Gilbreath

**Date:** this run. **Task:** check the proposed approach against the literature
and the run's own computed rows; set status `grounded` or `refuted`.

**Bottom line: the approach is refuted as a route to a proof.** The literature
and the run's own depth-1000 data contradict both premises of the proposed
method, and the method itself cannot do what its own partial-result fallback
claims. The refutation is on four independent grounds.

---

## 0. Restatement of the approach (what it actually claims)

The approach file claims:

1. (Premise A) The block lemma gives `b_{k+1} ≥ b_k − 1`, so reaching `b = 0`
   from `b = n` requires "n rows of pure erosion (b shrinks by 1 each row with
   no regeneration)".
2. (Premise B) During a pure erosion run of length `m`, the values at the
   shrinking block tip satisfy a "backward-difference recurrence"; starting
   from the hypothetical failure `A_{k+m}(1) = 4` at `b = 0` one can
   reverse-engineer the initial row's entries, and if those entries violate
   parity/gap structure the run is impossible.
3. (Method) Encode "there exists a 2-then-odds sequence with gaps ≤ g that
   produces m consecutive erosion rows" as SAT/SMT. UNSAT would prove the
   block can never reach 0, or even reach length 100.

**The literature does not support any of the three premises as stated, and the
run's own data refute their use.**

---

## 1. Has anyone attempted a constraint-satisfaction / reverse-engineering approach?

**Yes — and the field knows exactly what it buys.** Three independent literatures
converge on the same objects:

1. **Muney 2026 (arXiv:2606.23721) — the exact reverse-engineering theory.** The
   valid-extension set is computed by **backward preimage steps** on the right
   anti-diagonal: `Pe(T) = {e+t : t∈T} ∪ {e−t : t∈T, e≥t}`, applied from the
   final value `1` upward (Proposition 18, the "reverse-tree"). The valid
   distance set is a **fiber of a composition of folding maps** `FS(d) = 1`
   (iterated `x ↦ |x−e|`), and the exact membership criterion is an
   **order-sensitive analogue of Brown's subset-sum-completeness criterion** —
   a *global*, order-dependent condition on the whole prefix, with factorial
   weights reaching back to `s_1` (Alkan et al. 2023). There is **no bounded
   local constraint system**: Muney's own Corollary 3 gives only an absolute
   candidate bound `|k−s_n| ≤ A(S)+1`, and the set it bounds can have interior
   holes (first at length 5, `(2,3,5,9,15)`) and exponentially many components.
   **Consequence:** encoding "m consecutive erosion rows" as a bounded SMT
   instance is exactly the kind of *finite-window* approximation that Muney's
   theorem shows is *not* the real criterion — the satisfiability of a
   length-m prefix is a function of the entire prefix history, with weights
   that grow factorially. A finite SMT encoding would either be a
   re-statement of Muney's global criterion (whose check is as hard as the
   conjecture) or a strictly weaker bounded approximation whose UNSAT proves
   nothing about the primes.

2. **Eppstein 2011 — long erosion/no-regeneration runs are constructible.** The
   anti-Gilbreath construction works *backwards from the right edge*, choosing
   each new row's right side to keep entries small while creating a large gap;
   the escape condition is `gap > row-sum of the entire previous row` — another
   **global** quantity. Its conclusion for the 2-then-odds class: for **any**
   unbounded monotone `f(n) ≥ 2` there is a 2-then-odds sequence with gaps
   `≤ f(n)` whose right edge switches between 1 and non-1 **infinitely often**.
   In the run's block language this means: for any `m` and any concrete block
   length there **exists** a 2-then-odds, small-gap sequence whose leading
   `{0,2}` block erodes without regenerating for at least `m` rows — and
   simultaneously exists one that *does* regenerate. **Consequence:** the
   approach's target statement "no 2-then-odds sequence with gaps ≤ a bound g
   (however slowly the bound grows) can sustain m erosion rows for all m" is
   **false as a universal claim about the class**. The primes would have to be
   special beyond any property the approach's encoding of "2-then-odds + gaps"
   states. An UNSAT certificate for a *bounded g* provable instance would only
   re-derive that the primes' gaps happen to avoid the Eppstein escape — i.e.
   it would encode exactly the unproved "two-separated-set non-concentration"
   hypothesis of Chase–Hunter–Tao, not prove it. (CHT Theorem 1.3/1.6 formalize
   this: their hypotheses — sublinear growth + no 2-separated concentration —
   are *heuristic* for primes and precisely what is unproved.)

3. **SAT-for-conjectures is a real and active methodology (MATHCHECK, Konev–
   Lisitsa EDC, Bright's surveys), and it has never been applied to Gilbreath —
   for a structurally good reason.** The successes (Erdős discrepancy,
   Boolean Pythagorean triples, Williamson matrices) all feature (a) a finite
   decision procedure for each candidate length, and (b) a *bounded* state /
   constraint description of the property. Gilbreath fails both: the property
   "row begins with 1" is a statement about an **unbounded** array, and the
   valid-extension/right-edge escape criteria are **global** (Muney, Alkan,
   Eppstein). Bounded model checking can explore a finite prefix, but the
   library finds **no published SAT/SMT attack on Gilbreath**, consistent with
   the community's assessment that the relevant constraints are not bounded
   locally.

**Searches run:** "Gilbreath conjecture SAT SMT constraint satisfaction
counterexample search"; "Gilbreath conjecture backward construction reverse
engineering sequence absolute differences triangle"; "absolute differences of
primes triangle block of zeros and twos regeneration erosion conjecture";
"Gilbreath conjecture 2, odd, gaps bounded counterexample construction";
"absolute difference triangle preimage inverse backward extension valid next
value criterion"; OEIS A036262 / A000232 / A089582 commentaries. The only
constraint-flavored material anywhere near Gilbreath is Muney (reverse tree),
Alkan (Gilbreath polynomials, factorial K-criterion), Eppstein (backward
construction), and the OEIS comment that a first term `>2` "jump" propagates
once formed — none of which supports a bounded local UNSAT.

---

## 2. Both premises are wrong as stated

### Premise B is contradicted by the run's own data

The approach's "key technical step" — the tip values during erosion satisfy a
'backward-difference recurrence' whose reverse-engineering finds a
contradiction for any 2-then-odds start — is empirically false *in the only
place it could be tested against the primes*:

- Depth-1000 rows (live regime k = 1..161): **101 erosion steps, and the tip /
  intruder trajectory is fully explained by a *one-row* rule**: during erosion,
  `y(k+1) = y(k) − 2` if the last block entry `x(k)=2`, else `y(k+1) = y(k)`.
  The intruder `y` is **monotone non-increasing** and reaches 4 and sticks;
  regeneration fires **exactly** when `(x,y) = (2,4)`. So the "constraints on
  the boundary values" are not a constraint *system* — they are a single-row
  drain rule with no backward coupling, and they are **satisfiable indefinitely**:
  `y` drains `14→4` in 13 rows and erosion runs of length 13 actually occur
  (k = 97..109, 113..124, 147..158). Every such run is *followed by
  regeneration at the same `(x,y)=(2,4)` point.*
- Consequently the approach's factual claim "starting from the eventual
  failure (A_{k+m}(1) = 4 at b = 0)" mis-states the dynamics: in 1000 rows of
  the actual prime data **the boundary never reaches `A_{k+m}(1) = 4` at `b=0`**
  — the block reaches the end of the row only by width-exhaustion of a finite
  record (k ≥ 162, intruder `None`), a record artifact. The genuine erosion
  runs always stop at `(2,4)`, i.e. *regeneration*, not at `b=0`.

### Premise A is arithmetic, not structural

`b_{k+1} ≥ b_k − 1` is true (verified), but "to reach b=0 from b=n requires n
rows of pure erosion" **does not follow**: the lemma lets `b` shrink by at
most 1 per row, but nothing says consecutive `−1`s must happen without
regeneration in between, and nothing couples a hypothetical long erosion run
to a *local* constraint contradicting parity/gap bounds. The block lemma (this
run's re-derivation, constant exactly 1) states precisely the *consumption*
half: a block of length n protects n+1 rows; the *regeneration* half — why the
boundary keeps re-entering `{0,2}` — is untouched and is exactly the
conjecture. The approach assumes the failure path can be characterized
locally; that is precisely what both the global-criterion literature (Muney,
Alkan) and the anti-Gilbreath construction (Eppstein) deny.

---

## 3. Are there known necessary conditions on tip values during erosion?

Yes, and they are *weaker* than the approach needs and *not* contradictory for
2-then-odds:

- **Established here (computed):** during erosion, `y` is even, `≥4`,
  non-increasing, and `y(k+1) = y(k) − 2·[x(k)=2]`. Regeneration occurs iff
  `(x,y) = (2,4)`. Zero failures over 998 transitions in depth-1000 data.
  These are the *only* known necessary conditions at the tip, and they are
  **satisfiable indefinitely** — real rows do it.
- **CHT Lemma 3.7(iii):** a `{0,d}`-valued block stays `{0,d}`-valued in all
  descendants; **Lemma 3.8** gives a parentage dichotomy. So "tip values"
  inside a two-valued region cannot force a decrease-in-magnitude by
  themselves — the *local* conditions cannot contradict erosion.
- **CHT Theorem 1.6:** the only obstructions to decay are long zero-blocks and
  long shallow `{0,d}`-blocks — i.e. the *global* (length/height) profile, not
  any pointwise tip condition.
- No source in the library states a *non-trivial necessary condition on the
  boundary values during erosion* that would make the proposed constraint
  system unsatisfiable. The only exact "tip" theory is Muney's reverse-tree /
  folding criterion, which is global and, by Eppstein, satisfiable in the
  2-then-odds class for arbitrary erosion lengths. **That is the finding: the
  tractable necessary conditions known are exactly the ones the approach's
  UNSAT would need to contradict, and they do not contradict.**

---

## 4. Why the proposed partial-result fallback cannot be a theorem either

The approach says: "even UNSAT for m up to some concrete number (say m = 100)
would be a genuine partial result: the block length can never drop below 100
in one erosion run given gap bound g."

- The run's data already show erosion runs of length 13 and a *mechanical*
  838-row run (k = 162..999) that is pure erosion with no intruder — so
  "long pure-erosion runs" exist and are not dynamically forbidden; only the
  *intruder-driven* ones are bounded (≤ 13 in this record).
- With a concrete *bounded* `g`, SAT can decide finite prefixes, but the
  result is a fact about the bounded-g finite prefix, **not** a theorem about
  the primes. To make it a theorem over all primes one must give a *bound
  valid for all primes* on the max erosion-run length or on `g` — and any such
  bound is either a restatement of a prime-specific non-concentration
  hypothesis (CHT: unproved, even heuristically only) or false in the
  2-then-odds class (Eppstein). A certified UNSAT with an explicit g would be
  a *computation*, and computing it for "all 2-then-odds sequences" is not
  finite: the class is infinite.

---

## 5. Verdict and why

**`refuted`.** Grounds, with sources:

| # | Ground | Source |
| --- | --- | --- |
| 1 | Exact valid-extension/reverse-engineering criterion is **global** (order-sensitive, factorial-weighted subset-sum analogue); no bounded local system exists. Alkan's `min K ≤ s_{m+1} ≤ max K` involves `s_1·(n−1)!+...`; Muney's reverse-tree is a fiber of composition of fold maps with subset-sum completeness criterion; candidate bound only `|k−s_n| ≤ A(S)+1`. | Alkan et al. 2023 (MDPI 11(18):4006); Muney 2026 arXiv:2606.23721 Prop. 2/12/18, Cor. 3 |
| 2 | For **any** unbounded monotone `f(n)≥2` there exist 2-then-odds sequences, gaps `≤f(n)`, whose right edge (block regime) leaves and re-enters the good state **infinitely often** — arbitrary erosion-run lengths are realizable in the class the approach encodes, however small `g`. | Eppstein 2011, https://11011110.github.io/blog/2011/02/20/anti-gilbreath-sequences.html |
| 3 | Premise B contradicted by the run's own rows: erosion is a **one-row drain rule** (`y→y−2` iff `x=2`), regeneration fires exactly at `(x,y)=(2,4)`, and real erosion runs of length 13 occur; no `A_{k+m}(1)=4 at b=0` trajectory exists in 1000 rows. The "constraint system" is satisfiable indefinitely in the data. | depth-1000 record: `code/out/blocks_depth1000.json`; analysis `research/notes/regeneration_data.md`; `code/out/erosion_dynamics.captured.txt` |
| 4 | SAT/SMT counters (MATHCHECK, EDC, Bright) have never been applied to Gilbreath; the framework's successes require finite/bounded state, which GC provably lacks on both sides (unbounded array; global extension criterion). No published SAT attack on GC found in any search. | MATHCHECK (IJCAI'16, Zulkoski/Ganesh/Czarnecki); Konev & Lisitsa 2014; Bright 2022 CACM; searches 1–6 §1 |
| 5 | The block lemma's protection is **linear** (n+1 rows per length-n block); the approach's "n rows of pure erosion to reach 0" is a *consumption* statement, and the regeneration half — the only obstacle to `b→0` — is exactly the unproved conjecture, reframed, not solved. | Odlyzko 1993 §2 p.374; this run's `research/notes/block_lemma.md` (proved, constant 1) |
| 6 | CHT: the only obstructions to decay are long zero-blocks and long shallow `{0,d}`-blocks (global length-height obstructions); `{0,d}` blocks propagate in all descendants; the prime-specific hypotheses (sublinear gaps + no 2-separated concentration) are unproved, and any "gap bound makes erosion impossible" claim in the 2-then-odds class is false by Eppstein. | CHT 2026 arXiv:2607.08712 Thm 1.6, Lemmas 3.7(iii), 3.8; Eppstein 2011 |

**The salvageable residue (worth keeping, not as a proof route):**
- The run's own exact characterization — regeneration fires iff the boundary
  pair is `(x,y) = (2,4)`, erosion = one-row drain — is a *computed fact worth
  keeping*; it is the correct precise statement of "tip conditions during
  erosion" and it is the right target for any future regeneration argument.
- Muney's reverse-tree is the correct *descriptive* tool for "which boundary
  values can produce which next-row entries", and it is global; any future
  approach must name a prime-specific input (not a 2-then-odds-only input)
  that makes the global criterion fail, which is the CHT non-concentration
  hypothesis and is unproved.

**What was searched, how far:** the full reference library (18 primary sources
on GC: Odlyzko, Killgrove–Ralston, CHT, Chase, Muney, Alkan, Eppstein, Li,
Colonna, Plouffe, Bhat–Cobeli–Zaharescu, Arias de Reyna, OEIS A036262/A000232/
A089582, Wikipedia/Arias de Reyna/Gilbreath surveys); 6 distinct live-web
searches incl. `category:"research paper"`; OEIS A036262 onward. No source
attempts a SAT/SMT Gilbreath encoding; no source proves a nontrivial local
necessary condition on erosion tip values; the class-level statement the
approach needs ("m erosion rows impossible from any 2-then-odds start with
small gaps") is *false* by Eppstein. Not found ≠ refuted for the *primes
specifically* — but the approach proves nothing about the primes that does
not already require the unproved CHT hypotheses.