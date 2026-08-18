```approach
idea: Attack the conjecture from the OPPOSITE direction — a certified
  LOWER BOUND via a fully machine-verifiable construction. Instead of proving
  finiteness (an upper bound), construct an explicit polynomial field carrying
  more small-amplitude limit cycles than the published count for its degree, and
  close the existence of each limit cycle with a trapping-region / return-map
  sign-change certificate that is re-stated as a kernel-checked Lean theorem via
  the run's own Lyapunov-quantity oracle.

  The representation change: limit-cycle EXISTENCE, which is otherwise a
  transcendental assertion, becomes the finite algebraic fact "this Lyapunov /
  Bautin coefficient takes these signs on this box" — a sign condition on
  explicit polynomials over Q, combined with the certified trapping region that
  upgrades "a relevant root exists" to "a limit cycle exists". This is the one
  direction where a certificate fully CONCLUDES rather than supports, and the
  run already has the Lyapunov machinery (code/bautin/lyapunov_quadratic.py,
  the verified focal values L4/L6/L8, the Bautin-trick ideal membership
  L_d∈⟨L4,L6,L8⟩ through degree 14).

mechanism: Why this problem's structure suits it. GOAL explicitly lists
  "a certified configuration beating a published lower bound in degree 3" and
  "a twelfth small-amplitude cycle at a cubic focus" as target results, and lists
  "improved lower bounds H(3)≥14, M(3)≥12" under genuinely-unknown. The 28-CPU
  box makes a sweep over coefficient ansätze cheap; the Lyapunov quantities are
  exact over Q; and the trapping-annulus certificate (interval-arithmetic return
  map with a sign change, per the oracle spec in GOAL) is the sole legitimate proof
  of existence. Test 2 is the relevant one here (the construction must beat H(3)≥13 /
  M(3)≥11, and will be checked against it); Test 1 is vacuously fine because we are
  only asserting existence, never a smooth-false finiteness. This is also the most
  likely to yield an actual *number* — a certified configuration with N cycles is
  a concrete, reproducible, publishable result.

  The honest scope: a lower bound is not a proof of H(3)<∞, but it is a genuine
  partial result in the direction the conjecture is OPEN (the exact maximum is
  unknown), it exercises the run's full certification pipeline end to end, and
  each limit cycle's existence is closed by a certificate Lean can re-verify —
  converting the "exact Lyapunov oracle" from a numerical search into a proof
  artefact.

first-step: Extend the existing Lyapunov-quantity oracle to the cubic focus
  (degree-3, so more coefficients and longer focal-value chains than the degree-2
  case already computed). On a box of coefficients, compute the first few focal
  values V₁,V₂,V₃... exactly over Q, and search (worker sweep) for coefficients
  where V₁=...=V_{k−1}=0, V_k≠0 with the right signs to force k small-amplitude
  cycles (a generalized Bautin argument: k·... cycles from k sign changes). Then,
  for the best candidate, run the certified limit-cycle counter — trapping annulus +
  interval-arithmetic return-map sign change — on each of the k cycles, capture to
  code/out/, and re-state the sign-change certificate as a Lean theorem (the
  decidable sign conditions on the explicit polynomials). First executed check:
  reproduce Bautin's M(2)=3 via the canonical quadratic oracle (already the
  literature boundary the run is told to reproduce before trusting anything past
  it), then push past it into degree 3.

precedent: [GROUNDED — both the certification method and the specific lower-bound
  targets are established in the literature; BUT the concrete "twelfth cycle at a
  cubic focus" target is ALREADY ACHIEVED (Torregrosa 2024, M(3)≥12, held full),
  so the honest new target must escalate.]
  Method precedent (rigorous/certified limit-cycle existence):
  - Immler & Tan, "The Poincaré–Bendixson theorem in Isabelle/HOL", CPP 2020,
    doi:10.1145/3372885.3373833 — formalised trapping region + Poincaré–Bendixson
    → constructive existence of a limit cycle, interval arithmetic over
    verified ODE reachability. This is the closest published formalization of
    exactly the certificate this approach wants (in Isabelle, not Lean).
  - Computer-assisted isolating annulus / Floquet-coordinate validation:
    "Experimentelle Mathematik in Beispielen" (Mitt. Dtsch. Math.-Ver. 5 (1997),
    doi:10.1515/dmvm-1997-0114) — interval arithmetic trapping annuli around a
    numerical cycle prove a hyperbolic limit cycle exists.
  - The run's own held oracle: Songling quadratic system with EXACTLY four limit
    cycles, proved rigorously by interval arithmetic (adaptive precision, P-map
    fixed points; claim h16-four-cycles-songling-galias-tucker, model oracle for
    this run's certifier).
  Lower-bound-target precedent:
  - M(3) = cyclicity of a cubic focus: best published is M(3) ≥ 12, Torregrosa
    "Cubic planar vector fields with high local cyclicity", São Paulo J. Math.
    Sci. 18 (2024), doi:10.1007/s40863-024-00486-9 (held full; claim
    h16-torregrosa-cubic-12-small-cycles-2024): twelve small-amplitude cycles via
    degenerate Hopf from two one-parameter cubic families, all Lyapunov
    computations exact polynomial arithmetic, exceptional parameter values by
    Sturm sequences. This supersedes the run's earlier M(3)≥11 (Żołądek) and
    makes "a twelfth cycle at a cubic focus" an EXISTING result, not a new one.
  - H(3) ≥ 13 (global): Li, Liu, Yang, "A cubic system with thirteen limit
    cycles", JDE 246 (2009) 3609–3619, doi:10.1016/j.jde.2009.01.038 (12 of them
    in a (5:1|1:5) two-nest configuration from a cubic Hamiltonian + 1
    surrounding; built by counting Abelian-integral zeros). Confirmed and
    extended by Yang–Han–Li–Yu, Int. J. Bifur. Chaos 20 (2010)
    doi:10.1142/s0218127410027209, and by Prohens–Torregrosa, Nonlinearity
    32 (2019) doi:10.1088/1361-6544/aae94d (H(4)≥28 via reversible centers).
  Consequence: a genuinely new certified configuration in degree 3 must beat
  M(3) ≥ 12 at a single cubic focus, or H(3) ≥ 13 globally (e.g. a 14th cycle,
  or a 13th in a configuration not already covered). The run's value-add over
  Torregrosa 2024 is NOT the number 12 — it is (a) a certified trapping-annulus
  + interval-return-map certificate (Torregrosa's verification is CAS exactness,
  not a topological certificate, and is not in Lean), and (b) the hunt for a
  configuration past 12. Both are open; (a) alone is a legitimate
  Lean-finishable deliverable (re-certify an existing published 12-cycle
  configuration with interval certificates, stated as kernel-checked sign
  conditions).
status: reserved
revive-when: the run has exercised the certification pipeline end-to-end (a
  trapping-annulus + interval-return-map + Lean sign-condition certificate closed
  on ONE configuration — the pipeline candidate 2's Wronskian/Sturm core will
  build, or a re-certification of a published small-amplitude configuration) AND
  either (a) a specific cubic-focus coefficient ansatz giving V₁=…=V_{k−1}=0,
  V_k≠0 for k≥13 is identified, or (b) the run decides re-certifying an existing
  published 12-cycle configuration with interval certificates + Lean-stated sign
  conditions is itself a deliverable. The concrete target M(3)≥12 is already
  achieved (Torregrosa 2024), so a genuinely new lower-bound result must beat
  M(3)≥12 at one cubic focus or H(3)≥13 globally; a search past those is not yet
  warranted before candidate 2's Lean-finished ABELIAN count demonstrates the
  pipeline can produce a kernel-checked sign-condition certificate at all.
```

_Line in a sentence: the certified-lower-bound method is established (Isabelle's
formalised Poincaré–Bendixson trapping-region existence; the run's own certified
Songling 4-cycle oracle), but the named target — a twelfth small-amplitude cycle
at a cubic focus — is already in the literature (Torregrosa 2024, M(3)≥12), so
the honest new work is either a certified Lean re-certification of an existing
configuration or a search past 12 (M(3)≥13 / H(3)≥14)._