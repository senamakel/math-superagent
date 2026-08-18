# PE1006 library digest (2026-08-18)

Memory indexing was unavailable during this digest; this workspace note preserves the findings for later indexing.

## Sources that bear directly

- [[lothaire-sturmian-words-primary-2026.full]] and [[perrin-sturmian-words-lecture2-mechanical.full]]: the PE1006 limit word is characteristic Sturmian/mechanical with slope alpha=1/phi^2=(3-sqrt(5))/2. The lower mechanical digit is floor((n+1)alpha+rho)-floor(n alpha+rho); rotation-cylinder intervals describe factors, and all intercepts of one irrational slope have the same language. Sturmian complexity is exactly k+1. Applies directly to the factor set, but gives no Psi formula.
- [[berstel-vuillon-coding-rotations.full]]: irrational rotation codings are recodable as Sturmian codings under stated irrationality/rational-independence conditions. Supports the rotation model only; it does not establish PE1006's representatives or second moment.
- [[chuan-fibonacci-words-fq1992.full]]: finite labelled Fibonacci words are cyclic shifts of a standard word (Theorems 6–7), with complete rotation classes at Fibonacci lengths. Useful for special Fibonacci-length checks, not general Psi.
- [[sivasankar-rama-fibonacci-factors-2022.full]]: studies enumeration/location of Fibonacci factors; the digest does not expose a clean theorem sufficient to justify the exact general-k window formula. Do not overclaim it.
- [[cassaigne-extremal-properties-fibonacci-word-2008.full]]: first-occurrence quotient for Fibonacci word rho'*=Phi+1, so prefixes of asymptotic length about 2.618k contain all length-k factors. This justifies bounded small brute checks, not the full computation.
- [[alessandri-berthe-three-distance-theorems.full]] and [[van-ravenstein-three-gap-theorem-1988-hal.full]]: orbit gaps have at most three lengths and are continued-fraction controlled; factor frequencies correspond to interval lengths. Explains rotation geometry and possible special autocorrelation reductions, but does not prove Psi aggregation.

## Exact arithmetic sources

- [[oi-wiki-universal-euclidean-floor-sum.full]], [[universal-euclidean-geometric-weight-fhq.full]], and [[loj138-universal-euclidean-floor-moments.full]]: universal Euclidean recursion evaluates fixed-size monoid/moment states for affine floor paths, including geometric weights and floor/floor^2 moments, in logarithmic coefficient complexity independent of n. Applies to the inner floor-moment arithmetic only after the intercept aggregation is proved.
- [[atcoder-internal-math-hpp.full]] and [[atcoder-math-hpp-v151.full]]: exact base floor_sum recurrence and O(log m) complexity; useful independent implementation reference, but no geometric-weight or PE1006 result.

## Sources that do not help the requested result

Cassaigne's recurrence/repetition details beyond first occurrence; Rauzy factor-frequency bounds; Obryant's parity theorem for sum of factor heights; Berstel's Fibonacci survey abstract (body unavailable); Chuan 2003 moment/conjugacy results (special cyclic classes only); automatic-sequence/Cobham papers (Fibonacci word is not ordinary k-automatic and this is not an automatic decision problem); generic three-gap literature (geometry only); Babichev-Shpakova lattice-rectangle paper (different weighted-floor application). None supplies the missing fixed-dimensional joint-intercept aggregation for Psi(10^18).

## Contradictions / corrections

The recalled claim that Cassaigne gives first-occurrence quotient Phi+1 is consistent with the local source note. A previously held general-k cyclic pair-correlation identity is explicitly restricted to k=F_n-1; using it at arbitrary k would be incorrect. The slope convention must be alpha=1/phi^2 for the problem's digits, not 1/phi (the latter is a complemented convention in some sources).