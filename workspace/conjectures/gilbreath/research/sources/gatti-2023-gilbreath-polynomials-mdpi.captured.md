# Gatti 2023, "Gilbreath Equation, Gilbreath Polynomials, and Upper and Lower Bounds for Gilbreath Conjecture"

Source URL: https://www.mdpi.com/2227-7390/11/18/4006
Journal: Mathematics (MDPI) 11(18):4006, 2023-09-21. Author: Riccardo Gatti.

**How obtained:** the direct PDF and page downloads return HTTP 403 (publisher
bot-guard, recorded in REQUESTS.md). The page text was captured via the library
`read_sources` route on 2026, which renders the article page. This file is the
captured page text, recording the concrete definitions and the exact derivation
of Equation (6). No full PDF has been obtained.

## The structure of Gilbreath sequences (Definitions 1–5)

A finite integer sequence S = (s_1, ..., s_n) is a *Gilbreath sequence of length
n*, S ∈ G_n, iff s_1 has one parity and s_2..s_n the opposite parity, and

    min K(s_1,...,s_m) ≤ s_{m+1} ≤ max K(s_1,...,s_m)   for all m in 1..n

where (from the held 2020 preprint machinery, which this paper restates)

    max K_S = s_1·(n−1)! + s_2·(n−2)! + ... + s_n·0! + 1
    min K_S = 2·s_n − max K_S

The paper defines the m-th *Gilbreath polynomial* P_m via, for the ordered
sequence of the first m primes,

    u_n = 2^{m+n−1} + P_m(n),   P_m(n) = a_{m,0} + a_{m,1} n + ... + a_{m,k} n^k

with coefficients a(m,j) tabulated (Table 2) and recorded in OEIS A347924
(numerators of coefficients by row m, column n) and A347925 (denominators).

## The main claim: Equation (6)

Applying the K-criterion to the prime sequence P = (p_1,p_2,...) = (2,3,...):
P ∈ G_2, and the left inequality min K(p_1..p_{n−1}) ≤ p_n "is trivial and
holds for all prime numbers". Hence

    p_n ≤ max K(p_1,...,p_{n−1})  ⟹  GC_n

and since, by the definition of the Gilbreath polynomial P_{n−1},

    max K(p_1,...,p_{n−1}) = 2^{n−1} + P_{n−1}(1)

the paper's Theorem 1 states

    p_n − 2^{n−1} ≤ P_{n−1}(1)  ⟹  GC_n          (Equation 6)

## The paper's own concession

"The left side of (6) ... consists of a Gilbreath polynomial conjecture whose
solution implies GC. Unfortunately, **bounds for p_n are not good enough to
prove (7)**; however, this opens the way for a new approach to the GC."

## Run's assessment (librarian 2026, after capturing the page text)

This closes the REQUESTS.md open item ("the 2023 claim remains unverified" —
the one Gilbreath-claim source the library could not read). The captured text
confirms:

1. **The claim is real and verbatim:** GC is implied by `p_n − 2^{n−1} ≤ P_{n−1}(1)`.
2. **It is the same claim already refuted in the 2020 preprint form.** The
   implication reduces to `p_n ≤ max K(p_1..p_{n−1})`, which is exactly Gatti's
   Theorem 4 from the 2020 preprint — and the run has already located the proof
   of Theorem 4 as **invalid** (`gatti-2020-theorem4-proof-invalid`: the
   right-inequality step assumes its own conclusion `p_n ≤ max K`, subtracting
   2p_{n−1} from both sides, and derives only a trivial `min K ≤ α` via
   Bertrand). The MDPI paper is the same single-author preprint→MDPI pipeline
   (v1 2020-03-08 on Preprints.org → MDPI *Mathematics* 11:4006, 2023) and
   restates the same inequality without supplying the order-theoretic step that
   would make `p_n ≤ max K` follow from fewer/weaker hypotheses.
3. **The paper itself concedes it does not prove the bound** ("bounds for p_n
   are not good enough"). So even on its own terms, Equation (6) is a
   sufficient-condition reformulation, not a proof of the hypothesis.
4. **The run has not verified the inequality numerically, and the paper's own
   author concedes it is unproved.** [Editor's note, librarian:] I removed an
   earlier sentence asserting the inequality is "trivially true for large n"
   as-written, because P_{n-1}(1) carries factorial-scale coefficients of
   mixed structure and the sign of its leading term is not established by any
   held source or by a computation in this run. The only verified facts are
   (a) the implication reduces to `p_n ≤ max K` (Gatti's Theorem 4, whose
   proof is invalid per `gatti-2020-theorem4-proof-invalid`), and (b) the
   author's own statement that current prime bounds are insufficient.

**Bearing:** the MDPI paper adds no load-bearing mathematics to this run. It is
a second restatement of the Alkan/Gatti global K-criterion (whose valid-
extension content is held), published in a peer-reviewed journal, whose proof
of the load-bearing inequality is the same invalid Theorem 4. Do not cite it as
a route to GC; cite it, if at all, as the peer-reviewed record that the
`p_n − 2^{n−1} ≤ P_{n−1}(1)` reformulation is acknowledged (by its own author)
to be unproved.
