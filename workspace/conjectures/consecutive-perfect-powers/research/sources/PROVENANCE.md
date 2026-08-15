# Library provenance and gaps

What the local reference library holds, where each source lives, what was
obtained and what could not be, and why.

## Available locally (research/sources/)

| File | Source | What it establishes | How obtained |
| --- | --- | --- | --- |
| `cassels-1960-II.md` | Cassels, *Math. Proc. Camb. Phil. Soc.* (1960), "On the equation ax − by = 1. II". DOI 10.1017/s0305004100034332 | Scope record: for `x^p − y^q = 1` with `p,q` odd, any solution has `p | y`, `q | x` — the `cassels-divisibility` / `G-Cassels` gap. | Server-side read of the paper's own abstract and reference list via `read_sources`. Full text not obtained (host blocked). |
| `crandall-dilcher-pomerance-wieferich-wilson.primary.md` | Crandall, Dilcher, Pomerance, "A search for Wieferich and Wilson primes", *Math. Comp.* 66 (1997), 433–450. URL https://doi.org/10.1090/s0025-5718-97-00791-6 | PRIMARY: base-a Wieferich definition `a^{p-1} ≡ 1 (mod p^2)` (base left, squared modulus right); base-2 only 1093 and 3511; search bound 4×10^12; the notation anchor for the double-Wieferich reconstruction. Claim `base-a-wieferich-definition-cdp`. | Server-side full-text readout via `read_sources` (AMS host refused for download). |
| `katz-wieferich-past-and-future.md` | Katz, "Wieferich past and future", *Contemp. Math.* 632 (2015). URL https://web.math.princeton.edu/~nmk/wieferich37.pdf and DOI 10.1090/conm/632/12632 | PRIMARY (survey): Wieferich's theorem 2^{p-1}≡1 (mod p^2) from FLT(I); the base-a Wieferich definition; Wieferich quotient/equidistribution conjecture. Second independent confirmation of the base-a definition. Claims `wieferich-primes-two-known-base2`, `wieferich-criterion-first-case-flt`. | Server-side full-text readout via `read_sources` (Princeton/AMS refused for download). |
| `cassels-1953.md` | Cassels, *Amer. J. Math.* **75** (1953), 159–162. DOI 10.2307/2372624 | Technique origin: divisibility structure of `a^x − b^y = 1`; ancestors of the `p|y, q|x` theorem. | Server-side readout via `read_sources`. Full text not obtained (JSTOR blocked). |
| `sinnott-1978-stickelberger-circular-units.md` | Sinnott, *Annals of Math.* **108** (1978). DOI 10.2307/1970932 | Minus-part index `[R-:S-] = h-` and circular-unit index `[E+:C+]` in a cyclotomic field — the class-group machinery named by the hard descent gap. | Server-side read of abstract via `read_sources`. Full text not obtained. |
| `ichimura-2006-class-number-formula-cyclotomic.md` | Ichimura, *Arch. Math.* **87** (2006), 539–545. DOI 10.1007/s00013-006-1867-7 | Stickelberger/class-number index in `Z[ζ_p]`, incl. `p ≡ 3 (mod 4)`, index-2 sub-case. | Server-side read of abstract. Full text not obtained. |
| `klazar-thue-theorem.primary.md` | Klazar, "Analytic and Combinatorial Number Theory II" (Charles Univ. Prague, 2010). Ch. 1 "Thue's theorem on Diophantine equations". URL https://kam.mff.cuni.cz/~klazar/ln_antcII.pdf | **Thue's finiteness theorem**: for an irreducible homogeneous P(x,y) of degree d ≥ 3, P(x,y)=m has finitely many integral solutions; proved from Thue's inequality |α − p/q| > c q^{−(d/2+ε)}. Also its exact scope limit: does NOT apply to x^p − y^q = 1 with varying exponents (a difference of monomials, not a fixed homogeneous P(x,y)=m) — so Thue alone cannot close the conjecture. Names the tool behind the run's fixed-(p,q) descents (Q(cuberoot 2) Thue equations) and its boundary. | Server-side readout via `read_sources` (host refused by download boundary). Claim `thue-finiteness-theorem`. |
| `columbia-ant-cyclotomic-and-class-numbers.primary.md` | Oh, "Algebraic Number Theory" (Columbia GU4043). URL https://www.math.columbia.edu/~gyujinoh/Spring2025/ANT.pdf | Canonical capture of this PDF: Z[ζ_p] ring of integers, h = h^+·h^-, minus part via odd characters/Bernoulli, Stickelberger annihilator, cyclotomic-units index. Claims `columbia-h-equals-hplus-tim-hminus`, `columbia-zetap-ring-of-integers-and-stickelberger`. (See also the pointer file `columbia-cyclotomic-class-groups.primary.md`, which duplicates this URL and must be removed on cleanup; it carries no claim.) | Server-side full-text readout via `read_sources`. |
| `milne-algebraic-number-theory.md` | Milne, "Algebraic Number Theory" (Univ. Michigan course notes). jmilne.org/math/CourseNotes/ANT210.pdf | Rings of integers, Dedekind domains, class group finiteness, unit theorem, cyclotomic extensions + FLT chapter: Z[ζ_p] ring of integers, ramification of p, ideal factorisation of (x+ζ^i y). | Server-side read of chapter outline/excerpt; full PDF not stored. |
| `nguyen-note-cyclotomic-integers.md` | Nguyen, "A Note on Cyclotomic Integers", Amer. Math. Monthly 2019; arXiv:1706.05390 | Self-contained proof Z[ζ_n] is the ring of integers; Φ_p(X) ≡ (X−1)^{p−1} mod p; (p)=(1−ζ_p)^{p−1}; product lemma ∏(1−u)=p. | Server-side read of PDF excerpt. |
| `conrad-factorization-cyclotomic.primary.md` | Keith Conrad, "Factorization in cyclotomic fields", Stanford Math 676 handout. URL https://math.stanford.edu/~conrad/676Page/handouts/factorize.pdf | PRIMARY: Z[ζ_n] the full ring of integers (monogenic, prime-power n); p ramifies totally in Q(ζ_{p^e}) as (p)=P^{e(p-1)}, P=(ζ_{p^e}-1) principal; for e=1, P=(1−ζ_p) the unique prime over p with e=p−1, f=1, (p)=(1−ζ_p)^{p−1}. The factorisation-machinery foundation the cyclotomic ideal approach rests on. | Server-side full-text readout via `read_sources` (Stanford host blocked for download_document). |
| `conrad-cyclotomic-extensions.about.md` | Keith Conrad, "Cyclotomic Extensions", Galois-theory notes. URL https://kconrad.math.uconn.edu/blurbs/galoistheory/cyclotomic.pdf | Entry-level Galois tier: Gal(Q(ζ_n)/Q)≅(Z/nZ)^×; Φ_n irreducible/monic, divides X^n−1; primitive roots conjugate. Not the ring-of-integers/ramification depth. | Server-side readout via `read_sources`. |
| `conrad-unit-theorem.about.md` | Keith Conrad, "The unit theorem", grad-num-theory notes. URL https://kconrad.math.uconn.edu/blurbs/gradnumthy/unittheorem.pdf | Dirichlet unit theorem: O^×≅W×Z^r; for Q(ζ_p), r=(p−3)/2. Minkowski bound → finite-set class-number control (class number 1/PID criterion). The unit-rank structure the circular-units-index-plus-part claim rests on; why small-p cyclotomic fields are PIDs. | Server-side readout via `read_sources`. |
| `keune-number-fields.md` | Keune, "Number Fields" lecture notes. DOI 10.54195/ipvu4488 | Z[ζ_m] is ring of integers, degree φ(m), discriminant formula, ramification of p. | Server-side read. |
| `washington-introduction-to-cyclotomic-fields.md` | Washington, "Introduction to Cyclotomic Fields", GTM 83 (2nd ed.) | Canonical reference: class numbers, cyclotomic units, Stickelberger, h± split, Main Conjecture. Metadata + ToC captured; full text not stored. | Book page + PDF catalogue reached server-side. |
| `schoof-real-cyclotomic-class-numbers.primary.md` | Schoof, "Class numbers of real cyclotomic fields of prime conductor", Math. Comp. 72 (2003), 913–937. DOI 10.1090/S0025-5718-02-01432-1. URL https://www.mat.uniroma2.it/~schoof/realcyc.pdf | PRIMARY full-text readout (server-side via read_sources): exact sequence 0→Cl+→Cl→Cl−→0, h=h+·h−, plus-min computable asymmetry, Jordan–Hölder factor computations for l<10000 (354 factors of order<80000, largest 1451; h̃+|h+). Technique, not the answer. | read_sources on freely-hosted PDF. download_document refused (host policy). |
| `hida-elementary-iwasawa-cyclotomic.primary.md` | Hida, "Elementary Iwasawa theory for cyclotomic fields", UCLA course notes. URL https://www.math.ucla.edu/~hida/207a.1.18w/Lec1.pdf | PRIMARY full-text readout: analytic class number formula (residue shape), Dirichlet/Kummer relative class number h−(Q(ζ_p))=2p∏(1/p)Σχ⁻¹(a)a, plus/minus idempotent decomposition, Stickelberger annihilator + Iwasawa p-cyclicity of Cl−, Kummer–Vandiver (verified to 163M primes). | read_sources on freely-hosted PDF. download_document refused. |
| `tijdeman-linear-forms-survey.md` | Tijdeman, "Linear forms in logarithms and exponential Diophantine equations" (HMJ survey 2020). DOI 10.46298/hrj.2020.6458 | Baker's bounds shape exp(−C(logA)^κ(logB)); the four-step Baker method; makes exponential Diophantine equations effectively finite. Technique, not the specific bound for x^p−y^q=1. | Server-side read of survey. |
| `zsigmondy-primitive-divisors-bhv.md` | Bilu–Hanrot–Voutier, "Existence of primitive divisors of Lucas and Lehmer numbers", INRIA RR-3792 (1999); Zsigmondy (1892). URL https://inria.hal.science/inria-00072867/file/RR-3792.pdf | Primitive prime divisor theorem (Zsigmondy; BHV classification of the finite exceptions); for odd prime p and x≥2, Φ_p(x)=(x^p−1)/(x−1)=U_p(x+1,x) has a primitive divisor r≡1 (mod p). The elementary engine of the Lucas-sequence approach, independent of the class group. | Full-text readout via `read_sources`. `download_document` refused (host policy). |
| `conrad-factorization-cyclotomic.primary.md` | Keith Conrad, "Factorization in cyclotomic fields" (Stanford Math 676 handout, factorize.pdf). URL https://math.stanford.edu/~conrad/676Page/handouts/factorize.pdf | PRIMARY full-text readout: Z[ζ_n] = O_{Q(ζ_n)} for n a prime power (equality holds in general, disc divisible exactly by the primes dividing n); for n=p^e, pZ[ζ_{p^e}] = P^{p^{e-1}(p-1)} with P=(ζ_{p^e}-1) principal, e=p^{e-1}(p-1), f=1; for p prime, (p)=(1−ζ_p)^{p-1}. Fills the previous summary-only gap on ring of integers + ramification. | `read_sources` on freely-hosted PDF; `download_document` refused (Stanford host blocked). |
| `conrad-cyclotomic-extensions.about.md` | Keith Conrad, "Cyclotomic Extensions" (Galois theory notes, cyclotomic.pdf). URL https://kconrad.math.uconn.edu/blurbs/galoistheory/cyclotomic.pdf | Entry-level: Gal(Q(ζ_n)/Q) ≅ (Z/nZ)^×; primitive roots of unity Galois-conjugate; Φ_n monic integral irreducible; Kronecker–Weber. Background tier. | `read_sources`. |
| `conrad-unit-theorem.about.md` | Keith Conrad, "The Unit Theorem" (gradnumthy/unittheorem.pdf). URL https://kconrad.math.uconn.edu/blurbs/gradnumthy/unittheorem.pdf | Dirichlet unit theorem O^× ≅ W × Z^{r_1+r_2-1}; for Q(ζ_p) rank (p-3)/2; Minkowski bound → class number from finite prime check. Structural basis of the cyclotomic-unit index [E+:C+]=h^+ machinery. | `read_sources`. |
| `elementary-factorisation-technique.md` | (method note) | The two exponent-2 cases' *technique*: coprime-factor in Z (x^2−y^q=1) and Gaussian-integer binomial in Z[i] (x^p−y^2=1). No published answers stored. | Written by librarian. |
| `p-adic-valuation-technique.md` | (method note) | LTE lemma; v_p(x^p−1)=1+v_p(x−1); the cyclotomic ideal-factorisation technique; norm identity N(1−ζ_p)=p. | Written by librarian. |
| `pillai-related-equations-stroeker-tijdeman-bennett.md` | Bennett, Canad. J. Math. 53 (2001); J. Number Theory (2003); Canad. Math. Bull. 52 (2009); Scott–Styer JNT 118 (2006); arXiv:1112.4547 | The related-equations tier (problem.md's final Lead, previously absent): Stroeker–Tijdeman `c_0(3,2)=13`; Bennett at-most-two / at-most-one and inequality results; the (3,2,1) prototype exception containing the known solution. | Server-side readout via read_sources; exact statements quoted in-document. |
| `mit-18.785-analytic-class-number-formula.primary.md` | MIT 18.785 "Number Theory I" (Fall 2015), Lecture 18 "The analytic class number formula". URL https://math.mit.edu/classes/18.785/2015fa/LectureNotes18.pdf | PRIMARY full-text: ζ_Q(ζ_m)(s) = ∏_χ L(s,χ) (Theorem 18.2), and the analytic class number formula ρ_K = 2^r(2π)^s R_K h_K/(w_K√|D_K|). The analytic scaffolding of the relative class number formula h^-(Q(ζ_p)). Claims `mit-zeta-factors-over-L-series`, `analytic-class-number-formula`. | read_sources on freely-hosted PDF (download blocked). |
| `evertse-linear-forms-logarithms.primary.md` | Evertse, "Diophantine Approximation" (Leiden), Ch. 5 "Linear forms in logarithms". URL https://pub.math.leidenuniv.nl/~evertsejh/dio19-5.pdf | PRIMARY full-text: Baker 1975 |Λ|>(eB)^(−C) (Thm 5.2) and multiplicative corollary |α_1^b1…α_m^bm−1|>(eB)^(−C0) (Cor 5.3); the mechanism producing the astronomically-large effective bound. Claims `baker-effective-lower-bound`, `effective-finite-but-not-computable`. | read_sources on freely-hosted PDF (download blocked). |
| `stewart-linear-forms-baker-wustholz.primary.md` | Stewart, "Linear forms in logarithms and Diophantine equations" (Waterloo). URL https://uwaterloo.ca/pure-mathematics/sites/default/files/uploads/documents/stewart.notes_1_0_0.pdf | PRIMARY full-text: Baker–Wüstholz 1993 explicit constant |Λ|>exp(−(16nd)^(2n+4)·∏log A_i·log B); the sharpest shape of the effective bound. Claims `baker-wustholz-explicit-constant`, `effective-method-sketched`. | read_sources on freely-hosted PDF (download blocked). |
| `kummer-ratio-relative-class-number.primary.md` | Kandhil, Languasco, Moree, Saad Eddin, Sedunova, "The Kummer ratio of the relative class number for prime cyclotomic fields", arXiv:2402.13829 (2024). URL https://arxiv.org/html/2402.13829 | PRIMARY: relative class number h_1(q)=h(q)/h^+(q) is the minus class number; Kummer's criterion q\|h(q) ⟺ q\|h_1(q); Maillet–Carlitz–Olson determinant det(M_q)=±q^((q-3)/2) h_1(q) — an independent exact-integer route to h^-(Q(ζ_p)); Carlitz/Metsänkylä/Feng bounds on h_1; FFT O(q log q) computation. Bounds any cross-prime minus-class-divisibility claim (request `exact-statement-mihailescu-bbf8`). Claims `kummer-q-divides-h-iff-q-divides-h1`, `maillet-determinant-equals-class-number`. Maillet check script `code/out/maillet_verify.py` written but NOT yet run (no execution tool here). | read_sources on arXiv HTML (host blocked for download_document). |
| `roitman-zsigmondy-primes.primary.md` | Roitman, "On Zsigmondy primes", Proc. Amer. Math. Soc. 125 (1997). URL https://doi.org/10.1090/s0002-9939-97-03981-6 | PRIMARY full-text: a Zsigmondy prime for (a,n) is a prime divisor of a^n−1 dividing no a^j−1 (0<j<n), equivalently ord_r(a)=n, hence n \| r−1 (r ≡ 1 (mod n), r ≥ n+1); large-Zsigmondy notion; Theorem 3 exception list. Anchors the congruence engine r ≡ 1 (mod p) for a primitive divisor of Φ_p(x), the adopted Lucas approach. Claims `roitman-zsigmondy-order-p-equals-1-mod-p`, `zsigmondy-exceptions-finite-list`. | read_sources on the AMS DOI (download blocked). |
| `kummer-ratio-maillet-handcheck.md` | (scholar hand-verification this session; no execution tool available) | Hand-corroboration of the Maillet determinant identity `det(M_q)=±q^((q-3)/2)h_1(q)` from arXiv:2402.13829 at q=3,5,7 (high-confidence hand arithmetic) and q=11 (lower-confidence 5×5). Evidence-class caveat: this is NOT machine-checked; the h_1>1 primes (q=23,29,31,37,41,43) remain untested until `code/out/maillet_verify.py` is run by a computing role. Claim `maillet-determinant-handchecked-3511` (asserted/hand-corroborated, not checked). | Hand arithmetic by scholar. |
| `voutier-primitive-divisors-III.primary.md` | Voutier, "Primitive divisors of Lucas and Lehmer sequences, III", Math. Proc. Camb. Phil. Soc. 123 (1998). URL https://doi.org/10.1017/s0305004197002223 | PRIMARY full-text: Theorem 1 — for all n > 30030 the n-th element of any Lucas/Lehmer sequence has a primitive divisor; the ω(n) split (ω=6 → n>30030, ω=5 → n>28980, ω=4 → n>26880, ω=3 → n>23040); conjecture threshold n>30. Anchors the existence half of the adopted primitive-divisor approach. Claims `voutier-primitive-divisor-universal-threshold`, `voutier-exception-bound-30030`. | read_sources on the Cambridge DOI (download blocked). |
| `katz-wieferich-past-and-future.md` | Katz, "Wieferich past and future", Topics in Finite Fields, Contemp. Math. 632 (2015). DOI 10.1090/conm/632/12632. Free reprint https://web.math.princeton.edu/~nmk/wieferich37.pdf | The FRONTIER's top-cited non-answer source (cited 3×). Fixes the definition of Wieferich primes/quotients, Wieferich/Mirimanoff/Vandiver FLT-first-case criteria, the base-2 record (only 1093, 3511 known < 6.7e15), and the equidistribution conjecture. Background to the double-Wieferich gap; **not** the double-Wieferich condition itself (that is cross-base and must be re-derived from Cassels). Claims `wieferich-primes-two-known-base2`, `wieferich-criterion-first-case-flt` (holds-here: no — FLT hypothesis). | read_sources on the free Princeton reprint (host blocked for download_document). |

## Superseded pointer files (kept on disk, carry no claim, do not read for content)

These two files are thin redirects left over from earlier librarian sessions.
Neither carries a claim block. Both point to a canonical file that holds the
real content; they exist only because a duplicate capture was started before the
canonical source was found. They are kept so a later reader does not re-derive a
capture of the same URL, but they are **not** the source of record. On a future
cleanup pass with file deletion, both should be removed and only the canonical
files kept:

- `columbia-cyclotomic-class-groups.primary.md` → canonical
  `columbia-ant-cyclotomic-and-class-numbers.primary.md` (same URL, same PDF).
- `katz-wieferich-past-future.primary.md` → canonical
  `katz-wieferich-past-and-future.md` (same Katz survey).

## Could not be obtained, and why — so nobody retries

- **Mihăilescu's proof of Catalan's conjecture (2002), and any survey or text
  stating/deriving the full classification.** The run's evidence policy screens
  material that would supply the published answer to `problem.md`. It is a
  deliberate, enforced boundary, not a network fault. **Do not retry.** The run
  must re-derive the closure steps itself, in-workspace, from the techniques
  the library supplies.
- **The double-Wieferich necessary condition and Inkeri's refinement** (REQUEST
  `exact-statement-citable-f890`): search for the exact statement is screened as
  answer-bearing. It is a necessary condition on a hypothetical solution (part
  of the run's owned re-derivation of Cassels's chain), so the library supplies
  the technique — Wieferich definition (Katz survey), Cassels valuation + LTE
  (`p-adic-valuation-technique.md`, `code/out/cassels_valuation.note.md`),
  cyclotomic-ring machinery (Conrad) — and the run derives the congruences
  itself. **Do not retry** a direct fetch of the condition.
- **Full texts of all four papers above, and every other publisher-hosted
  paper.** The network boundary permits only the search and data APIs; direct
  fetching of publisher/preprint hosts fails regardless of the URL. Retrying
  mirrors fails the same way. For these the run relies on the server-side
  `read_sources` readouts already recorded, and must treat any full statement
  as to-be-re-derived, not as transcribed.
- **Lebesgue-style write-up of `x^p − y^2 = 1` and the effective Tijdeman
  bound**: both queries returned material screened as answer-bearing. The
  exponent-2 cases are elementary and will be re-derived in-workspace (Z and
  Z[i]); the effective bound is a "gathering" item whose exact size the run
  should aim to state from a re-derivation or a non-answer source.
- **Nagell–Ljunggren equation `(x^n−1)/(x−1)=y^q`**, the classical theorem that
  closes Case B (T(c,p) is never a square). Two searches for a primary survey
  were screened as answer-bearing (they would hand the run the closing lemma of
  `x^p−y^2=1`). The in-workspace Case B reduction does carry this lemma as
  verified-numerically (`caseb-lebesgue-reduction-certified`: T(c,p) not a
  square for c≤1e5, odd prime p≤251, 0 squares) and asserted-by-classical-
  theorem; it is NOT re-proved here. **Do not retry** the Nagell–Ljunggren
  fetch; it is the run's owned closing step to derive.

## Where the gaps point next (see REQUESTS.md)

The REQUESTS.md rows already capture the four exact gaps the library was aimed
at: `exact-closing-lemma-b571` (the closing step), `exact-statement-citable-f890`
(Cassels divisibility + double-Wieferich), `exact-statement-mihăilescu-bbf8`
(the descent in the minus class group), `exact-statement-primary-1ad5` (whether
the full goal is proved or open). This library gives those gaps their technique
foundation (Cassels divisibility, Stickelberger/minus-class machinery) but does
**not** supply their answers — the screener prevents it, by design. They remain
open and must be closed by the run's own derivation, with claims logged against
them.
