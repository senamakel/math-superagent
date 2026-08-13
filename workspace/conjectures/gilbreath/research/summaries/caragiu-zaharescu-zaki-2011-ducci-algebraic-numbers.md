# Caragiu, Zaharescu, Zaki, "On Ducci Sequences with Algebraic Numbers", Fibonacci Quarterly 49.1 (2011) 34–40

Source: https://www.fq.math.ca/Papers1/49-1/CaragiuZaharescuZaki.pdf (full
text at `research/sources/caragiu-zaharescu-zaki-2011-ducci-algebraic-numbers.full.md`).

## What it establishes

Studies the iterated-absolute-difference map on a **periodic** sequence;
§1 explicitly notes that the map `a′ₖ = |aₖ − aₖ₊₁|` on the infinite periodic
sequence is "the same map which appears in the well-known conjecture of
Gilbreath", and that periodicity is what makes the long-run behaviour
understandable there even though Gilbreath's conjecture is open.

- **Lemma 2.1**: the map is 2-Lipschitz: `‖D(X) − D(Y)‖ ≤ 2‖X − Y‖`
  (Euclidean), and no λ < 1 works (not a contraction).
- **Maximum component is non-increasing** (proof of Thm 1.1: all components
  of `Dⁿ(X)` lie in `[0, M]` for `M = max D(X)`), converging to a limit `M₀`;
  every element of the limit set has components in `{0, M₀}` (Brown–Merzel).
- **Theorem 1.1 (the main result)**: for `X` with real-algebraic components,
  the iterates converge to their (unique, finite) limiting cycle and the
  convergence is *at most* exponentially fast: either the cycle is reached in
  finitely many steps, or `‖D^{j+mL}(X) − V_j‖ ≥ C₁ e^{−C₂ m}` for all m.
  Explicit `C₂ = (log 2)([K:ℚ]−1)L` from the proof; with M₀ algebraic and
  Roth's theorem `C₂ = (log 2)(2+ε)L`.
- The proof machinery: iterates are integer-coefficient linear combinations
  of the initial components with coefficients bounded by `2ⁿ`; clearing
  denominators into a number field and using `|N_{K/ℚ}(nonzero algebraic
  integer)| ≥ 1` gives the separation bound.

## Relation to this run

- The **same operator** as Gilbreath's on an infinite periodic sequence — the
  nearest tractable relative of the half-infinite case in the literature, and
  one this run had not previously sourced the treatment of. The exponential
  convergence dichotomy (finite reach vs. `C₁e^{−C₂m}` lower bound) is a
  structural statement about the iteration that has no known analog for the
  half-infinite, non-periodic Gilbreath triangle.
- The 2-Lipschitz and max-non-increase facts hold in the half-infinite case
  verbatim (the run proves max non-increase locally in `ducci-potential`);
  the algebraic-separation lower bound does *not* transfer (no cycle, no
  periodicity, no K to work in).
- Useful negative control: any proposed "uniform fast convergence to {0,2}"
  for a general class must fail on algebraic periodic inputs — the theorem
  forbids faster-than-exponential decay there.

```claim
id: czz2011-ducci-2-lipschitz
statement: The difference map D on d-tuples with a′_k=|a_k−a_{k+1}| (and a′_d=|a_d−a_1|) is 2-Lipschitz in the Euclidean norm and is not a contraction; iterates have non-increasing maximum M and every limit-cycle element has components in {0, M0}.
hypotheses: finite d-tuples of real numbers, cyclic closure.
holds-here: yes, and the max-non-increase half transfers to the half-infinite Gilbreath rows (run's own proof of |a−b| ≤ max(a,b)); the 2-Lipschitz bound likewise transfers entrywise
status: proved (in source); primary source landed
bearing: Lyapunov/contraction facts for the approach ducci-potential-max-decrease; matches the run's own max Lyapunov function
anchor: research/sources/caragiu-zaharescu-zaki-2011-ducci-algebraic-numbers.full.md
answers: what-lipschitz-and-max-facts-hold-for-the-difference-map
```

```claim
id: czz2011-infinite-periodic-ducci-is-gilbreath-operator
statement: On an infinite periodic sequence, the map a′_k=|a_k−a_{k+1}| is exactly the operator of Gilbreath's conjecture; in the periodic setting (Brown–Merzel) iterates converge to a single finite cycle, and for algebraic initial data the convergence is at most exponentially fast (finite reach or ‖diff‖ ≥ C1 e^{−C2 m}).
hypotheses: periodic sequence of real algebraic numbers; map without the wrap-around entry (a′_k=|a_k−a_{k+1}| for all k).
holds-here: the operator identity holds; the periodicity/algebraicity hypotheses do not (prime gap sequence is neither periodic nor algebraic-separated in the needed sense)
status: proved (in source); primary source landed
bearing: names the nearest solvable relative of the half-infinite Gilbreath triangle and gives a structural dichotomy (finite reach vs exponential lower bound) — a useful control on what general-class theorems may assert
anchor: research/sources/caragiu-zaharescu-zaki-2011-ducci-algebraic-numbers.full.md
answers: is-there-a-tractable-relative-of-the-gilbreath-iteration
```

## What could not be obtained

Taylor & Francis blocks the published version (403); the FQ archive PDF is
the canonical free copy and was used. The paper's own references include
Brown–Merzel 2003 (limiting behavior) and the p-adic Ducci game note
(Caragiu–Baxter 2007) — neither in the library; the p-adic note is a
possible source for the run's `p-adic-valuation-carry-dynamics` approach.