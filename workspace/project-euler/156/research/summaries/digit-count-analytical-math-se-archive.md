# Math.SE 47477 — "Number of occurrences of the digit 1 in the numbers from 0 to n"

**Source:** https://math.stackexchange.com/questions/47477 (Wayback capture), archived full text: `[[digit-count-analytical-math-se-archive.full]]` — `research/sources/digit-count-analytical-math-se-archive.full.md`.

A 2011 Math.SE question that is exactly the Google puzzle / PE156 d=1 instance, with three answers. Useful as an independent *formulation* of the counting function, not as an answer source.

## What it establishes

- **The question** (Mark Zimmers, Jun 24 2011) restates f(n) = number of 1s in the decimal writings of 0..n; example f(12)=5; asks for the next n with f(n)=n. Commenters note it is **Project Euler problem #156** (link in the accepted answer).
- **crasic's answer (accepted, upvoted 8):** an analytical closed form for f(d, n) for any digit d and any base B:
  - Write n = [r_k, r_{k−1}, …, r_0] (list representation).
  - E(j) = j·10^{j−1} = total occurrences of any fixed nonzero digit in 0..(10^j − 1).
  - f(d,n) = Σ_{j=0..k} ( Σ_{i=0..r_j} 10^j·δ_{i−1,d} + r_j·E(j) + δ_{r_j,d}·(n[j:]+1) ), where n[j:] is the number formed by the last j digits.
  - Claims Mathematica evaluation gives 199981 as the next n with f(1,n)=n.
  - Notes the "big" problem (all digits 1–9) needs a faster method; the closed form alone is too slow for that.
- **Listing's answer:** a brute-force Mathematica scan prints 0, 1, 199981, 199982, …, 199990, 200000 for d=1 — consistent with the statement's oracle and `code/brute.py`.
- **S4M's answer:** partial bound argument — f(10^{n+1}−1) = 1 + 10^n + 10·f(10^n − 1); u_9 > v_9 and u_10 < v_10, so the answer is below 10^10 − 1 (a crude finiteness hint for d=1 only).

## Hypotheses and hold-here

- Counts 0..n for d=1: exactly PE156's f(n,1). For general d>0 it agrees with the paper's f_d as before.
- The crasic formula is stated without proof but matches the place-value identity; the run already verifies the identity computationally (`G1-checked`).

## Implication for this run

Independent statement of the closed form (a "second route" formulation that a counter-program could implement, distinct from the higher/current/lower branching). Also primary-sourced provenance that this problem is PE156 and that its intended difficulty is the all-digits sum, not the d=1 case.

## Does not settle

No bound on the full solution set for d=1..9 (S4M's bound is only for d=1 and only says "below 10^10 − 1"); no per-digit sums. Not the answer source.

```claim
id: mathse-analytic-form
statement: crasic's Math.SE answer gives f(d,n) = Σ_{j=0..k}( Σ_{i=0}^{r_j} 10^j·δ_{i−1,d} + r_j·E(j) + δ_{r_j,d}(n[j:]+1) ), E(j)=j·10^{j−1}, an independent analytical restatement of the per-position digit-count closed form, generalizable to any base B (10^k ↦ B^k).
hypotheses: decimal digits r_k..r_0 of n; d a single digit; n[j:] the integer of the last j digits.
holds-here: yes (d ∈ {1..9})
status: asserted (answer with no proof; agrees with the form verified by G1-checked and with Listing's brute-force 199981 result)
bearing: independent formulation usable as a second implementation route for f(n,d); provenance that this problem is PE156.
anchor: research/sources/digit-count-analytical-math-se-archive.full.md
```
