# Durand & Rigo, "On Cobham's theorem" (EMS Handbook of Automata Theory, 2021)

**Source:** F. Durand, M. Rigo, "On Cobham's theorem", in *Handbook of
Automata Theory* (J.-É. Pin, ed.), EMS Press, 2021, chapter 26, pp. 897–921.
DOI 10.4171/automata-1/26. Full text obtained as the **author postprint**
(525 KB PDF) from the University of Liège repository ORBi:
https://orbi.uliege.be/bitstream/2268/39461/1/Chapter26.pdf
(permalink https://hdl.handle.net/2268/39461). The EMS publisher page
(`https://doi.org/10.4171/automata-1/26`) 404s on direct fetch, so the ORBi
record is the free-tier copy. Full text:
`[[durand-rigo-on-cobham-theorem-ems-2021.full]]`.

## What it establishes (precise statements, verified in full text)

- **Theorem 1.1 (Cobham's theorem):** for multiplicatively independent k, ℓ ≥ 2,
  a set X ⊆ N is both k- and ℓ-recognizable **iff** X is ultimately periodic.
- **Theorem 2.3 / Prop 2.4:** for a linear numeration basis U with dominant
  root β, rep_U(N) regular ⟺ β a Parry number — the bridge between linear
  numeration systems and substitutive/sofic dynamics.
- **Definition 2.3 (Pisot numeration system):** a linear numeration basis whose
  characteristic polynomial is the minimal polynomial of a Pisot number β;
  integer bases are the special case. **Example 2.1 (Fibonacci numeration)** is
  worked explicitly: U0 = 1, U1 = 2, U_{n+2} = U_{n+1}+U_n; representations are
  the language L = 1{0,01}* ∪ {ε}; the characteristic polynomial is the minimal
  polynomial of (1+√5)/2 — i.e. **the Fibonacci numeration system is a Pisot
  numeration system with β = φ**. Normalization is by finite automaton in such
  systems (so addition works digit-wise with carry removal).
- **Theorem 3.4 (Cobham, version 2):** x ∈ B^N both k-automatic and
  ℓ-automatic, k, ℓ multiplicatively independent ⟹ x ultimately periodic —
  the automatic-word form, which is the one directly about binary words.
- **Theorem 4.3 + Cor 4.4 (Presburger):** ⟨N, +, <, (≡_m)⟩ eliminates
  quantifiers, so any Presburger-definable set is ultimately periodic — the
  target of the Cobham–Semenov definability conclusion.
- **Theorem 4.7 (Cobham–Semenov theorem, higher dimension):** X ⊆ N^d is
  definable in both ⟨N,+,V_k⟩ and ⟨N,+,V_ℓ⟩ for multiplicatively independent
  k, ℓ **iff** definable in ⟨N,+⟩.
- Sections 5.x survey Cobham-type results for substitutive sets and the
  density/syndeticity/ultimate-periodicity consequences; §5.6.2 covers
  Bertrand bases.

## Hypotheses and whether they hold here

- The theorem statements are about automata recognizability in *bases* (integer
  or Pisot). PE1006's numerical set is the set of decimal values of length-k
  factors, read in **base 10**, while the positions are indexed by a
  **Fibonacci (φ-)numeration**. The two systems have multiplicatively
  independent bases (10 and φ), so by the Cobham–Frougny/Bès obstruction line,
  no finite automaton converts between them; the chapter's Theorem 2.3/
  Prop 2.4 and Example 2.1 are exactly the machinery that makes the Fibonacci
  system a Pisot system.

## What it must not be used for

- It does **not** say the universal-Euclidean floor-sum monoid is blocked: the
  monoid is exact integer arithmetic working entirely within one base (base-10
  digit weights with a slope given by Fibonacci ratios); it is not a finite
  automaton converting between φ- and 10-representations, so Cobham's theorem
  does not apply to it.

## Bearing on PE1006

- Fixes the **Pisot/Fibonacci numeration** terminology and the modern citable
  statement of Cobham's theorem (both base-set form Thm 1.1 and automatic-word
  form Thm 3.4), plus the higher-dimensional Cobham–Semenov form (Thm 4.7).
  This is the strongest modern survey tier for the run's claim
  `cobham-bes-frougny-multiplicatively-independent-conversion`, alongside the
  Bruyère et al. 1994 survey and Frougny 2002 (all held).
- Its §5 (substitutive sets, ultimate periodicity) is relevant background for
  the factor-position theorems the run uses (Sivasankar–Rama, Chuan–Ho).

## Paywalled companion noted (not obtained)

- A. Bès, "An extension of the Cobham–Semënov theorem", J. Symbolic Logic
  65(1) (2000) 201–211, DOI 10.2307/2586532 — the precise Pisot-vs-Pisot
  statement (θ, θ′ multiplicatively independent Pisot numbers, U, U′ their
  linear numeration systems: A ⊆ N^n both U- and U′-recognizable ⟹ A
  definable in ⟨N,+⟩). Cambridge Core and JSTOR both paywalled; statement
  recorded from the published abstract so the claim has a citable primary
  even without full text.