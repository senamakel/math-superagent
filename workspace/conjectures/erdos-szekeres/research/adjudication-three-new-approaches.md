# Adjudication of three proposed approaches (literature grounding)

Cycle: research specialist, taking the inventor's three candidates to the
literature. Each candidate's file under `research/approaches/` carries the full
verdict; this note is the short cross-candidate statement and the reason each
stands where it does. The three are genuinely different mechanisms (algebraic
grid-rank / spectral-association-scheme / stability-classification), none a
re-run of a closed one.

## 1. polynomial-rank-nullstellensatz — status: grounded-as-reformulation

**What it is / tools.** The mechanism is a real, standard algebraic method: Alon's
Combinatorial Nullstellensatz (Combin. Probab. Comput. 8 (1999) 7–29,
doi 10.1017/S0963548398003411); Alon–Füredi grid bound (European J. Combin. 14
(1993) 79–83); the modern per-variable-degree generalization (Bishnoi–Clark–
Potukuchi–Schmitt, Combin. Probab. Comput. 27 (2018),
doi 10.1017/S0963548317000566). The 4-point convexity criterion it wants to encode
is already the library claim `es35-four-criterion`, machine-checkable with
`lib/es_geom`.

**Precedent question answered.** No published application of the
Combinatorial-Nullstellensatz / Alon–Füredi method to the Erdős–Szekeres
convex-position upper bound ES(n) ≤ 2^{n-2}+1 exists. Checked against the
Morris–Soltan survey (BAMS 2000), Suk (JAMS 2016), the Mubayi–Suk induced-Ramsey
paper, and the CN literature: the run is not re-deriving a known result. The idea
is novel as a reformulation.

**Why not grounded-as-proof.** The load-bearing step is the run's own unproved
claim that an *arbitrary* no-convex-n-gon set indexes into {0,1}^{n-2}. That
injection is exactly what killed `boolean-lattice-injection-compression`
(Sperner cannot give 2^{n-2}) and the α-injectivity whose natural host
`etv-grid-simplex-compression` showed is C(2n-4,n-2) ≈ 4^n. The alignment check
on es_construct (nonzero set = 2^{n-2}) only verifies the *construction* saturates
an upper bound — which is the already-known lower bound — and does not produce an
injection for general sets. The inventor's own stated critical risk (natural host
recurs as a 4^n simplex) is real and unresolved by the literature. The cheap
first-step (n=5,6,7 on es_construct: does the nonzero set sit on a 2^{n-2} cube?)
is legitimate.

## 2. association-scheme-spectral — status: grounded-as-reformulation (weakest)

**Tools real, domain wrong.** Delsarte's association-scheme LP, Krawtchouk joint
diagonalization, and MacWilliams–Sloane coding theory are all real (Delsarte 1973;
MacWilliams–Sloane 1977; Delsarte-LP modern reconstructions IEEE T-IT 2024
doi 10.1109/TIT.2024.3476974; rank-metric eigenvalue bounds IEEE T-IT 2023
doi 10.1109/TIT.2023.3339808). But every one of them bounds the SIZE OF CODES at
a Hamming/rank *distance threshold*. Nothing applies to point-set convexity, and a
planar point set is not a code under a convexity relation (convexity is order-type
data, not a distance-threshold metric), so Delsarte's LP likely cannot even be
posed. The open precedent question is answered: no one has framed ES's 2^{n-2} as
a spectral/Delsarte threshold, but equally there is zero evidence the framing can
work.

## 3. stability-split-tight-decomposable — deductive route UNSOUND; structural claim worth testing

**The decisive adjudication.** The inventor's route "split-tight OR decomposable
⟹ ES(n) ≤ 2^{n-2}+1" is unsound at the split-tight branch, because a Baek–Balko
**split k-gon is not a convex k-gon**. From the held Baek–Balko text: a split
k-gon is an a-cap and u-cup sharing only the *rightmost* point (a+u=k+2); it gives
k points in convex position only if they *also* share the leftmost point. And that
strictness is exactly where the hardness lives (ROOT.md §5.1). Concretely:

- The split threshold theorem 2^{k-2}+1 already guarantees EVERY 2^{n-2}+1-point
  set contains a split n-gon — so split-tightness at that size is automatic for
  all sets and can never separate extremal from non-extremal.
- At the extremal size 2^{n-2} (where the dichotomy is stated), split-tightness is
  NOT guaranteed; indeed es_construct, the canonical 2^{n-2}-point tight witness,
  is split-FREE, not split-tight.
- The decomposable branch rests on Baek–Balko Thm 8, which is asserted-by-source
  in this library ("The proof of Theorem 8 is omitted" in the held SoCG version;
  deferred to JCTA 2026). So the only branch that genuinely gives convex position
  is itself unverified.
- Related literature: Balko–Kynčl–Langerman–Pilz (ENDM 2017,
  doi 10.1016/j.endm.2017.06.023) leave open "whether there is a (2,2)-Ramsey point
  set that is not decomposable" — the same stability gap.

**What survives.** The dichotomy as a novel TESTABLE STRUCTURAL claim — does every
no-convex-n-gon 2^{n-2}-set have a recursive deep-below decomposition (even if not
line-separated)? That is genuine GOAL-4 material (classify over Aichholzer order
types, n≤10, with the exact oracle). But it does NOT by itself resolve the upper
bound: the split-tight→convex step is already falsified.

## Net

Two of the three are novel reformulations whose tools are real but whose load-
bearing step is unproved and leans on the same injection/4^n-collapse that killed
prior counted routes; the third's deductive logic is unsound but leaves a genuine
classification sub-question. Do not treat any of the three as a proof route on the
current evidence. The cheap es_construct first-steps of (1) and (2) are worth
running as empirical controls; (3)'s enumeration is worth running as a structural
classification.
