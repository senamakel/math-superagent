# Goal — first pass

Attack Hilbert's tenth problem over the rationals (`problem.md`): whether `Z` is
existentially definable in `Q`, and the quantifier-count frontier around it.
MRDP settles the integer case and is **not** the target; do not re-prove it.

## What this pass is for

### 1. Establish the status, from primary sources

Every item in `problem.md` is recalled and must be confirmed or struck with its
citation and exact hypothesis. Settle in particular:

- **The exact quantifier shape and count** of every published definition of `Z`
  in `Q`: Robinson's, Poonen's, Koenigsmann's, and anything since. Build a table
  of shape, count, and what each suffices for. This table is the run's target
  inventory.
- **The status of the rings-of-integers results** — what exactly was proved,
  for which rings, by which argument, and whether it is refereed. If the
  recalled 2024–25 resolution stands, say precisely what remains open.
- Mazur's conjecture: its exact statement, its status, and the precise
  implication linking it to H10.def.
- The decidability boundary by degree over `Q`: quadratics (Hasse–Minkowski),
  and exactly what is known for cubics.

Each goes in `research/CLAIMS.md` with its evidence class and its falsifier,
and a line under **Established** in `CONTEXT.md`.

### 2. Write the mathematics in Lean, from the first hour

- `code/lean/Lib/Statement.lean` states Diophantine definability over `Q`, the
  quantifier shapes as distinct definitions, and H10.def, ending in `sorry`.
  **Making the shapes distinct types is the point** — it is what makes test 1 of
  `problem.md` a structural control rather than a reminder.
- Hilbert symbols and local conditions can carry real Lean proofs for specific
  rationals. Do those; a verified local condition is a kernel-checked theorem.
- Cited results — MRDP, Poonen, Koenigsmann, the number-field theorems — are
  `axiom`s in `namespace Cited` with `/-- src: ... -/`, earning `conditional`.
- Report `#print axioms` and every `sorry`, every time.

### 3. Build the oracle

In `code/`, one canonical library over `Q`, verified against controls before
anything rests on it:

- **A formula evaluator**: given a definition of `Z` in `Q` written in an
  explicit syntax, evaluate its local conditions at a given rational and report
  whether the formula holds — so any published or new definition can be tested
  on an explicit set of rationals in seconds.
- **Hilbert symbols, quaternion algebra ramification, and local solvability**,
  exactly, at every place.
- **Guards, asserted on at entry, every run**: a published definition must
  accept `0, 1, −1, 2, −3` and reject `1/2, 2/3, −5/7`; Hilbert symbols must
  reproduce the standard tables; Hasse–Minkowski must decide a conic correctly
  against known examples. A library failing any of these may not be used.
- **A quantifier counter** operating on the formula's syntax, so a claimed
  count is computed and not asserted.
- Record where local computations stop being feasible and why.

### 4. Attack one precise claim

State it in Lean before spending the attempt on it. Candidates, none endorsed:

- A verified reproduction of Koenigsmann's universal definition, followed by an
  honest attempt to reduce its quantifier count — with any reduction verified
  on the test set before it is written up.
- A decidability result for a stated family of cubics over `Q`, with the
  algorithm and its ceiling.
- A precise statement of what a rank-one elliptic curve argument would need
  over `Q`, and why it is unavailable — the clearest thing that can be said
  about the obstruction.

## Rules

- **Every statement carries its quantifier shape.** No claim in this workspace
  is written without `∃`/`∀`/`∀∃` and a count attached.
- **One canonical oracle.** Everything that evaluates a formula or a local
  condition calls `code/lib`; nothing does it inline.
- **A numerical test is a filter, not a proof.** A formula passing the test set
  is a candidate; correctness is proved place by place.
- If an argument yields an existential definition of `Z` in `Q`, say
  immediately that it refutes Mazur's conjecture and treat that as evidence
  against the argument until every step has survived attack.
- Label every statement proved / verified-computationally / conjectured /
  asserted-by-source, and name the ceiling of every computation.
- **`problem.md` is written from memory and expects correction.**

## Out of scope

MRDP's proof, register machines and recursion theory beyond what is needed to
state the reduction, function-field analogues in positive characteristic, and
the full first-order theory of `Q` except as background to the quantifier-shape
distinction.
