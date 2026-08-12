# research — what this establishes

Batches of originals in `L0.<n>/`; folds in `L1.<n>/`, `L2.<n>/`. Claims below
are wikilinked to their notes; `INDEX.md` is the file table.

## Counting object of 3D D(N): folded polyominoids (sourced)

PE763's amoeba is exactly Eriksson/Vaderlind's **n=3 pebbling game**. In n≥3
**no cell is ever played twice** (Prop 24), so reachable positions ⇄ voidance
sets ⇄ **folded polyominoids** coincide bijectively (Theorem 9)
[[L2.0/pebbling_ejc_survey]]. So D(N) is a **folded-polyominoid reachable-
position count**, not a random directed-animal count. Primary source: Eriksson,
"Pebblings", EJC 2 (1995) #R7, verified against its full text
([[L0.0/pebbling_ejc_survey.full]]). Full structural characterization in
[[pebbling_structure_3d_ladder]] (holds-here=yes for claims
`n3-folded-polyominoid-voidance`, `d2-positions-are-polyominoid-voidance`).
Eriksson gives no closed form for folded polyominoids (Fig.3 is a small-N
table), so the numeric D(10000) still needs the run's own DP.

## The 2D relative is fully characterised — the template to lift

The 2D amoeba = A007902 **pebbling configurations**
[[amoeba2d_pebbling_a007902]], governed by the exact **two-index G(k,m)
recurrence** (CGMO eqs 2.1–2.3; no one-index closed form) + asymptotics
~0.122687·2.321642^n [[L2.0/pebbling_knessl_pdf]], [[L1.0/oeis_a007902]].
2D is hard because of **crossings** (cells played twice); that machinery drops
out in 3D (Prop 24). The G(k,m) recurrence is the template for the open 3D
lift — thread [[threads/lift_gkm_to_3d]]. CGMO lemmas/Theorem 1 in
[[L2.0/cgmo_opening_dijkstra]].

## The OEIS/lookup route is closed

- **3D D(N) has no OEIS entry** — direct and offset-1 queries both "No results"
  (`dN-not-in-oeis`, `dN-offset-also-not-in-oeis`), so no catalogued closed
  form exists. Sealed batch [[L2.0/L1.0]]; [[amoeba_seq_oeis]],
  [[oeis_lookup_2d_3d]].
- **No Motzkin/Fibonacci family fits** — A001006, A005207, A086246, A168049 all
  diverge from D(N)=1,1,3,9,30,99,336,... at n=2 (proved by term comparison;
  claims `dN-not-motzkin`, `dN-not-fibonacci-f2n1`, `dN-not-a086246`,
  `dN-not-a168049`). D(N)'s ~×3.4/division growth rules out these base-2.3–2.6
  constant-recurrence families.
- 2D reachable count ≠ directed-animal count (A005773) although heads agree;
  the true 2D object is A007902.

## Run's own level-structure yield

The **max-level column** Q_2(N) = R(N,N-2)/3^(N-5) = (N-5)(N+2)/2, confirmed
exactly on N=6..14 against A055999 [[L1.0/oeis_a055999]]. Q_3,Q_4,Q_5 columns
have no catalogued match. Conjecture past N=14; needs structural justification.

## Sources of evidence
Every theorem is sourced with a URL in the named note; none invented. The three
primary-source digests (Eriksson, CGMO, Zhen–Knessl) are verified against their
full texts (each `L2.0/<x>` ⇄ `L0.0/<x>.full`), with column checks re-derived
by hand. Deliberately NOT consulted: any PE763 solution/forum thread.
