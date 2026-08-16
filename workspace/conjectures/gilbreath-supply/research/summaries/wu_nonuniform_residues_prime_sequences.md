# Summary — Nonuniform Distributions of Residues of Prime Sequences in Prime Moduli

Source: David Wu, arXiv:1908.07095 (2019). Full text: `[[wu_nonuniform_residues_prime_sequences.full]]`. Open access arXiv.

## What this establishes

A rigorous connection between the Hardy–Littlewood prime k-tuple conjecture and the frequencies of **patterns of consecutive primes of length k ≥ 2 mod q** — the higher-order (K>1) analogue of the pair-bias framework of Lemke Oliver–Soundararajan.

**Notation.** For a vector `a = (a1,…,ak)`, define
`π(x; q, a) = #{p_n ≤ x : p_{n+i−1} ≡ a_i (mod q) for 1 ≤ i ≤ k}` — the count of consecutive-prime sequences following pattern `a` mod q. The PNT in APs gives `π(x;q,(a)) ∼ li(x)/ϕ(q)`, i.e. equidistribution for length-1 patterns.

**The load-bearing higher-order fact (conditional on HL).** For length-k patterns with k ≥ 2, the frequencies are conjecturally NOT uniform, with biases larger than any O(x^{1/2+ϵ}) error (so they cannot be Chebyshev-bias artifacts). Example tabulated (mod 10, from [4]): `π(10^8; 10, (1,1)) ≈ 4.62×10^6`, `π(10^8; 10, (9,1)) ≈ 7.99×10^6`, versus the naive `10^8/ϕ(10)^2 = 6.25×10^6`. The dominant bias is controlled by the number of i with `a_{i+1} ≡ a_i (mod q)` (LOS's c2 coefficient), with LOS's original heuristic omitting lower-order terms that Wu adds.

**The parity barrier, in k-tuple form.** It is **not even known** whether `π(x; q, a) → ∞` for an arbitrary pattern `a` of length ≥ 2 (i.e. whether a non-constant consecutive-prime residue pattern occurs infinitely often). Only the constant patterns `(a,a,…,a)` are known to go to infinity: Shiu proved `π(x; q, (a,…,a)) → ∞`; Maynard strengthened to `π(x;q,(a,…,a)) > Cπ(x)` for a constant C and large x. So for length ≥ 2 patterns, only the *constant* (equal-residue) side is unconditional.

**The main theorem.** Under a Montgomery–Soundararajan-type estimate (3.5) extended to `S_{q,0}` (that the average order of `S_{q,0}(T)` over ℓ-element subsets is `(µ_ℓ/ℓ!)(−h log h + Ah)^{ℓ/2} + O(...)`, heuristically justified), the terms `S_∅, S_{0}, S_{h}, S_{0,h}` in the LOS heuristic, and hence `D_n(a,b;y)` and `D_{≥n}(a,b;y)`, are `O_n((log_2 y)^n / (log y)^{n/2−1})`. This lets one truncate the pair-frequency asymptotic `D(a,b;y)` at a specified n and control the errors — the mechanism for writing down the lower-order terms that explain the observed pair biases.

## What it implies here

This is the **direct K>1 companion** to the reopened pass's territory. The fold reads the mod-4 gap-parity string `h[j] = ((p_{j+1}−p_j)/2) mod 2`. The obstruction machine:

- **Higher-order residue patterns are the parity barrier's generalisation.** Just as the pair (length-2) frequency is open and L-function-inaccessible (ABGS/§9), the *length-k* pattern frequencies are open for every k ≥ 2, with only the constant patterns settled (Shiu/Maynard). So any K>1 functional of the fold that reads length-k structural constraints on the gap-parity string faces the same wall: the non-constant side at every order is conjectural.
- **Reinforces the negative transfer found for Lacasa.** The unconditional K>1 structure that exists on the gap sequence (forbidden patterns mod 6) is a *mod-6* phenomenon; the fold sees *mod-4 parity*, and the projection destroys it (see `research/notes/lacasa_parity_projection_transfer.md`). Wu confirms the residue pattern structure that *would* be readable (mod 4, any length) is exactly the conjectural, parity-barred part.
- **Sharpened statement of the open input.** The reopened pass's goal — a functional controllable by an arithmetic input strictly weaker than pointwise mod-4 switch density — would need a *length-k ≥ 3* pattern input on the gap-parity string. Wu shows no such input is known beyond the conjectural; the only unconditional statements are the constant-pattern ones (Shiu/Maynard), which are equal-residue and give *zero* runs — the wrong direction (SUPPLY needs *switches*).

## What it does NOT settle

- Nothing unconditional about non-constant patterns of length ≥ 2 (that is the open parity-barried core).
- Nothing about the fold matrix Φ or wt(Φ_n h) itself.
- The whole frequency theory is conditional on Hardy–Littlewood / the Montgomery–Soundararajan average-order assumption (3.5) — heuristic.

```claim
id: wu-length-k-pattern-frequencies-open
statement: For q ≥ 3 and a pattern a=(a1,…,ak) of length k≥2, the count
  π(x;q,a) of consecutive-prime sequences following a mod q is not known to tend to
  infinity (i.e. a non-constant consecutive-prime residue pattern is not known to occur
  infinitely often). Only the constant patterns (a,…,a) are unconditional: Shiu proved
  π(x;q,(a,…,a))→∞, Maynard proved π(x;q,(a,…,a))>Cπ(x). Observed (mod 10, x=10^8):
  π((1,1))≈4.62e6 vs π((9,1))≈7.99e6 vs naive 6.25e6 — length-2 frequencies are
  non-uniform, conjecturally (HL/LOS) with biases from the count of equal-adjacent entries.
hypotheses: consecutive primes; pattern length k≥2; mod q.
holds-here: yes — the SUPPLY parity string h[j]=((p_{j+1}−p_j)/2) mod 2 is a function of a
  length-2 residue pattern of consecutive primes, and the K>1 (length≥3) case is the reopened pass's
  territory; this is the precise form the parity barrier takes at every order.
status: asserted (the non-uniformity and the barrier; Shiu/Maynard parts proved).
bearing: sharpens the parity barrier to length-k ≥ 2: only constant (equal-residue) patterns are
  unconditional, which give the wrong (zero) direction for SUPPLY. The K>1 arithmetic input the
  reopened pass seeks on the gap-parity string is not known beyond the fault line this paper marks.
anchor: wu_nonuniform_residues_prime_sequences.full, §1 (eq. 1.1, the (1,1)/(9,1) data), §2 Conjecture 2.2, Theorem 3.1.
```

## Keyword map
consecutive prime patterns mod q; length-k pattern frequencies; parity barrier; Hardy–Littlewood k-tuple; Lemke Oliver–Soundararajan; Shiu; Maynard; higher-order correlation.
