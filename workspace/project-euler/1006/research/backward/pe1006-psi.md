# Proof skeleton: Ψ(10^18) mod 101001001

Decomposition of the goal of PE1006 into four lemmas that compose into the
answer. This is the committed, literature-backed reduction: the mechanical-word
/ geometrically-weighted floor-sum route (directives 2–4). The directive-9
contiguous-window route is NOT this skeleton — its one distinct contribution
(an O(log) sliding-window transfer-matrix collapse of a base-10 affine product)
was refuted in `research/approaches/pe1006-contiguous-window-cyclic-minus-prefix.md`
(it closes back onto the same floor-sum monoid). The set-identity half of
directive 9 survives only as a *verification* check on G1, not as a route.

G1, G2, G3 are discharged on the run's own executable verification (mech_psi ==
brute k=1..50, (A)==(B) telescoped identity k=1..400, Ψ(3)=20302,
Ψ(10)≡10699667). The genuinely open mathematical gap — the one this turn
sharpens — is G4: the outer sum of the second moment Σ_{m=0}^k v(x_m)^2 is over
k+1 ≈ 10^18 values, so it must collapse *alongside* the inner j-sum into an
O(log) monoid product. That is a reduction lemma that has **no claim behind it**
in this ledger, and it is the critical path.

```skeleton
detail: Skeleton at research/backward/pe1006-psi.md (rewritten this turn). The committed, literature-backed reduction is the mechanical-word / floor-sum chain (directives 2-4). The directive-9 contiguous-window route is NOT an independent O(log) method: pe1006-contiguous-window-cyclic-minus-prefix.md refutes its one distinct contribution (a base-10 sliding-window transfer-matrix collapse) as having no literature backing and closing back onto the floor-sum primitive; only its set-identity half survives as a verification check on G1. G1 (factor structure), G2 (mechanical representation), G3 (telescoped second moment) are discharged on the run's own executable verification; the ONE genuinely open mathematical gap is G4: the outer sum of the double sum Σ_{m=0}^k v(x_m)^2 is over k+1 ≈ 10^18 values and must collapse alongside the inner j-sum into an O(log) monoid product. No claim in the ledger states or proves that joint-index collapse — it is the reduction wiring, unexecuted. Status: live. First to close: G4 (steps 1-4 of the directive-10 order).
goal: compute Ψ(10^18) mod 101001001, where Ψ(k) is the sum of the squares of the k+1 distinct length-k Fibonacci subwords read as decimal numbers
implies: The four lemmas compose left-to-right and the chain of quantifiers closes with no free parameter. G1 fixes the index set: the k+1 distinct length-k Fibonacci subwords of S are exactly the k+1 length-k factors of the infinite Fibonacci word F (F is Sturmian of slope 1/φ², complexity k+1), so Ψ(k) = Σ over m = 0..k of the square of the m-th factor read as a decimal. G2 turns each factor into a value: the m-th factor is a mechanical word of the corrected slope a = F(n-2)/F(n) with digit digit_j(x_m) = floor(x_m + (j+1)a) − floor(x_m + ja), so the factor's decimal value is v(x_m) = Σ_{j=0}^{k-1} digit_j(x_m)·10^(k-1-j). G3 telescopes v: substituting the digit rule collapses the j-sum to v(x_m) = floor(x_m + ka) − 10^(k-1)·floor(x_m) + 9·Σ_{j=1}^{k-1} 10^(k-1-j)·floor(x_m + ja), so Ψ(k) = Σ_{m=0}^k v(x_m)^2 is the second moment of that geometrically weighted floor sum. G4 is the sharp gap: because the m-th representative x_m is itself the orbit point frac(−m·a) of the same rotation, m is another floor-sum index, so the DOUBLE sum Σ_{m=0}^k v(x_m)^2 collapses to an O(log) universal-Euclidean monoid product carrying (count, Σz^t, Σz^t·floor, Σz^t·floor²) mod M with z = 10^(−1) mod M — not O(k) outer steps each O(log) inner. Only G4 reaches k = 10^18; every earlier lemma supplies exactly the index set (G1), the term (G2), and the telescoped form (G3) that G4 consumes, and none of them leaves a free variable G4 has to bind.
killed-by: (nothing broken; the only structural lemma G1 still holds as open is the infinite-limit stabilisation, a formalisation nicety not on the numeric path. G4 is open in the sense that no claim in the ledger states or proves the double-sum collapse — the reduction wiring is unexecuted, not shown wrong.)
rests-on: fibonacci-sturmian-complexity, governing-sturmian, governing-factor-complexity, g1-factor-chain-nested, g1-oracle-length3, g2-mech-shell-exact-binary, mechanical-word-digit-rule, g3-telescoped-second-moment (mech_psi (B)), monoid-composition-formulas-verified, universal-euclidean-geometric-floor-sum, req-close-universal-euclidean, governing-universal-euclidean, ueuclid-s1s2-false-alarm-refuted
status: live
```

## The gaps

```gap
id: G1-sturmian-factor-structure
lemma: The k+1 distinct Fibonacci subwords of length k are exactly the length-k factors of the infinite Fibonacci word F (limit of S_n), and that count is k+1 for every k ≥ 1 (F is Sturmian with complexity k+1). The finite chain FactorSet(S_n,k) is nested and stabilises, giving FibSubwords k = the length-k factor set of F.
status: open
discharged-by: the count k+1, Sturmian-ness and the nested chain are closed by fibonacci-sturmian-complexity, governing-sturmian, governing-factor-complexity, g1-factor-chain-nested, g1-oracle-length3. What remains open is only the infinite-limit stabilisation lemma (factor_limit_stabilises) as a closed Lean verdict — a formalisation nicety, explicitly not the critical path to the number, and numerically corroborated by mech_psi == brute on the factor set at every k tested.
next: finite oracle check k = 1..60 that the length-k factor set of S_n stabilises for n ≥ 3k+1 and equals FibSubwords k; then close factor_limit_stabilises to promote the count to a conditional verdict in Lean. A theorem_prover / oracle task; safe to defer behind G4.
```

```gap
id: G2-mechanical-word-representation
lemma: With the corrected slope a = F(n-2)/F(n) (|S_n| = F(n+2) indexing), the k+1 factors of F of length k, read as decimal numbers, are exactly the values v(x_m) where x_m is the midpoint of the m-th arc of the partition of the unit circle by {frac(−m·a) : m = 0..k} and digit_j(x) = floor(x + (j+1)a) − floor(x + ja). The literal slope F(n-1)/F(n) is refuted (steer-d2-literal-slope holds no).
status: discharged
discharged-by: mechanical-word-digit-rule (same-slope factor-set identity), g2-mech-shell-exact-binary (the exact/binary construction shell), and the in-container machine check mech_psi == brute at k = 1..50 on the string oracle (code/out/mech_psi.captured.txt) — the set {v(x_m)} equals the factor-set decimal values at every k tested.
```

```gap
id: G3-telescoped-second-moment
lemma: With v(x) = Σ_{j=0}^{k-1} digit_j(x)·10^(k-1-j) and the digit rule digit_j(x) = floor(x + (j+1)a) − floor(x + ja), the telescoping identity v(x) = floor(x + ka) − 10^(k-1)·floor(x) + 9·Σ_{j=1}^{k-1} 10^(k-1-j)·floor(x + ja) holds, so Ψ(k) = Σ_{m=0}^k v(x_m)^2 is the second moment of this geometrically weighted floor sum over m.
status: discharged
discharged-by: this is exactly formulation (B) of code/mech/mech_psi.py, whose captured record (code/out/mech_psi.captured.txt) shows (A)==(B) in total and per-word multiset at k = 1..400, reproducing Ψ(3) = 20302 and Ψ(10) ≡ 10699667 mod 101001001 against the brute oracle.
```

```gap
id: G4-universal-euclidean-floor-sum
lemma: Let x_m = mid of the m-th arc of the partition by {frac(−m·a) : m = 0..k} (equivalently an orbit point of the rotation by a), and let v be the G3 telescoped form. The double sum Ψ(k) = Σ_{m=0}^k v(x_m)^2 mod M is evaluable in O(log k) — NOT O(k) outer steps each O(log k) — by a universal-Euclidean monoid product carrying (count, Σz^t, Σz^t·floor, Σz^t·floor²) mod M with z = 10^(−1) mod M, because x_m itself runs with m as a floor-sum index, so the outer m-sum and inner j-sum merge into one jointly-indexed monoid product. The dU boundary shifts carry floor values across segment boundaries.
status: open
discharged-by: the primitive's own correctness is closed by monoid-composition-formulas-verified (proved), governing-universal-euclidean and universal-euclidean-geometric-floor-sum (asserted O(log) monoid), and the in-container module check ueuclid-s1s2-false-alarm-refuted (the 1-indexed recursion passes acceptance 1-3 30/30 + 6/6). What is open is the REDUCTION: no claim in this ledger states or proves that the telescoped double sum Σ_m v(x_m)^2 collapses to a fixed-size (O(log)-evaluable) monoid product, and the outer m-sum over 10^18 values is exactly what that lemma must absorb. The set-identity climbing-of-directive-9 gives no help here — its O(log) collapse was refuted.
next: the directive-10 order, each step RUN and captured — the executable evidence for exactly this collapse lemma: (1) wire the G3 telescoped v through code/lib/ueuclid.py with the joint (m,j) indexing so that Ψ(k) is a constant-size monoid product (acceptance step 4); (2) reproduce Ψ(k) k = 1..150 and Ψ(10) ≡ 10699667 through that wiring — THIS is the literal test of the reduction-indexing: it pinpoints the z^0 / power-of-10 assignment ("which power of 10 the j-th digit of the telescoped v carries"), the one place a reduction-merge passes every monoid-level test yet gives a wrong answer; (3) reproduce the two anchors Ψ(10^4) = 34432237 and Ψ(10^6) = 20938836 and capture them to code/out (the directive-10 hard gate that unblocks Lean); (4) run k = 10^18 under two Fibonacci approximants F(n) > 10^18 and confirm they agree; only the agreeing value is the answer. A tool_builder can start at step (2) today: the wiring script, the mech_psi oracle, and ueuclid are all on disk; failure of Ψ(k) at any small k pinpoints the indexing error directly.
```

## Why this, and what a bigger run would settle

G4 is the only gap whose closure produces the number, and its first move is a
runnable equality: wire the double sum through the monoid and require Ψ(k) ==
mech_psi at k = 1..150. That run settles, at every small k, the only genuinely
unproven identity in the whole reduction — the joint-index merge that lets an
O(k)-appearing double sum be an O(log) product. If it fails at some k it
pinpoints the indexing defect; if it passes and the anchors match, the
remaining step (two matching approximants at 10^18) is arithmetic, not
mathematics. G1's stabilisation is the only other open item and it is not the
critical path.
