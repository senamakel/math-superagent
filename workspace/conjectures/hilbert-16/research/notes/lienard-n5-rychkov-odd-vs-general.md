# Liénard degree-5: Rychkov vs the open general case — a distinction worth keeping

**Claim being refined:** `h16-lienard-n5-open` (unchecked) says the general
degree-5 classical Liénard case (whether > ⌊(5−1)/2⌋ = 2 limit cycles) was open
as of the 2017 Llibre–Zhang survey.

**What is actually held and confirmed this pass:**

1. Llibre–Zhang 2017 survey (postprint, held full):
   `research/sources/llibre-zhang-lienard-survey-postprint-2017.full.md`
   - Theorem 2: LdMP conjecture holds for n = 1,2,3,4; fails for n ≥ 6.
   - The survey's **Open problem** (line ~90): "What is the maximum number of
     limit cycles for the Liénard differential systems (1) when n ≥ 5?" — the
     *general* degree-5 case is left open.
   - It cites Rychkov [32] but only as a reference, not as resolving the general
     n=5 case.

2. **Rychkov 1975** (Differential Equations 11:390–391): proves the *odd-only*
   system ẋ = y − Σᵢ aᵢx^{2i+1}, ẏ = −x (degree-5 odd polynomial) has **at
   most 2 limit cycles**. This is a NARROWER class than the general degree-5
   Liénard system (which allows even as well as odd terms in F).
   - Confirmed by multiple independent search results this pass (Llibre–Valls
     2013; Giacomini–Neukirch 1998; Gasull–Giacomini–Grau 2018; Llibre–Zhang
     survey). Not yet held as a primary text.

**Resolution of the apparent contradiction:** There is none. Rychkov closes the
odd-polynomial degree-5 case (=2); the general degree-5 case, where LdMP
predicts ⌊(5−1)/2⌋=2, remains **open** as of Llibre–Zhang 2017. The library's
`h16-lienard-n5-open` claim is therefore NOT struck — but it should be
strengthened: it refers to the general (mixed-parity) degree-5 case, and the
odd-only degree-5 case is settled (=2, Rychkov 1975, second-hand).

**Evidence class:** sourced (Llibre–Zhang 2017 held full); Rychkov's own result
is asserted-by-source (1967/1975 Russian paper, no primary text held).

**Falsifier for the refinement:** a primary statement, or an authorative survey,
showing that the *general* degree-5 Liénard system has a settled maximum
different from "open", or a primary text of Rychkov that narrows or broadens
the exact class he treated.
