# Grimmelt–Teräväinen (2026), two Chen primes
[[grimmelt-teravainen-exceptional-set-goldbach-two-chen-primes-arxiv-2508.16400.full]]

Source: https://arxiv.org/abs/2508.16400 (v2, 29 Jul 2026).

**Canonical claim already filed** in `research/notes/claims-exceptional-set-and-circle-method.md` as `grimmelt-teravainen-2025-two-chen-primes` (statement, hypotheses, status, evidence there). This note is the per-source digest.

The paper defines \(\mathcal P_k\) as integers with at most \(k\) prime factors and calls primes \(p\) with \(p+2\in\mathcal P_2\) Chen primes. Theorem 1.1: there is an effective constant δ>0 such that all but O(N^(1−δ)) integers m≤N with m≡4 (mod 6) are sums of two Chen primes p1+p2. Both δ and the implied constant are effective in principle but not numerically supplied.

The proof constructs a nonnegative model for a Chen-prime sieve. Key inputs: (i) a power-saving Fourier approximation of primes by a Cramér rough-number model, (ii) efficient sieving for large prime factors (power-saving Bombieri–Vinogradov) and small prime factors (fundamental lemma), (iii) treatment of a possible exceptional zero. The authors state that any improvement would require major progress toward twin primes or binary Goldbach. The paper supersedes the authors' earlier preprint (E(N,2,3) ≪ N^(1−δ)) and improves on the logarithmic-saving results of Tolev (5,7), Meng (3,8), Matomäki (2,7).

Bearing for this run: directly motivates the computation task `chen-prime-goldbach-computation` (verify n ≡ 4 mod 6 are sums of two Chen primes up to a stated bound B) and the thesis `chen-prime-exceptional-set`. It provides no closure theorem turning a single Goldbach counterexample into many exceptions — the structural-closure gap stands.