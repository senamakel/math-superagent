# Déprés — "Suite de permutations lors d'une course de n coureurs de vitesses constantes" (ENS Lyon research report, HAL hal-02300013, 2019)

**Summary.** Adjacent combinatorial study of the *sequence of permutations* taken over time by n runners with constant distinct speeds on a **circular** track of unit length, running indefinitely. Position-order at any instant (with no two tied) is a permutation of {1..n}; the study asks how many distinct permutations appear and with what frequencies.

Key results (deterministic speeds v_1<...<v_n):
- If the speeds are Q-linearly independent, **all n! permutations eventually appear**, and with **equal frequencies** (Kronecker-approximation argument on the torus).
- In general a geometric method computes the permutation frequencies for any speed configuration.
- n=2 case fully worked (periodic permutation sequence).
- Time-reversal duality: reversing time reverses permutations; relation to which reversed permutations occur in forward time.

**Relevance to PE597 — caveat, adjacent-contrast only.** This is *not* the finite-finish torpids model. Differences from the run's problem are decisive: (i) circular track with no finish line (no rear-removal, no "OUT"); (ii) deterministic speeds rather than iid Exp(1) random; (iii) infinite time, so every pair eventually passes and the final order is degenerate; (iv) no parity objective. Its genuine value is as a contrast in *permutation dynamics of moving particles*: it models overtakes as permutation transitions, and notes the permutation changes exactly when some pair crosses — the inversion/crossing picture that the run's pure-race limit (convex minorant = clusters = permutation cycles) also lives in. It does **not** advance p(13,1800).

Held because it is the thinnest corner of the library (deterministic-speed permutation-sequence literature) and a primary report on it is cheap and canonical (ENS Lyon, CC BY-NC-SA). Filed with the caveat so it is never cited as solving the finite-finish parity.

URL: https://hal.science/hal-02300013/document
