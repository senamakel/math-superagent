# OEIS A051953 — cototient

Source: https://oeis.org/A051953 — full text at
`research/sources/oeis-A051953-cototient.full.md`
[[oeis-A051953-cototient.full]]

## What this source establishes

**Definition.** a(n) = n − φ(n), the cototient: the number of positive
integers ≤ n sharing at least one prime factor with n.

**Values.** 0, 1, 1, 2, 1, 4, 1, 4, 3, 6, 1, 8, … (matches the run's
`code/out/seq_cototient.txt`).

**Comment relevant here.** cototient(n) ≡ n (mod 2) — so cototient(n+1) =
cototient(n) never holds (Labos Elemer) — which is why A063985(n) mod 2 has no
small period (checked by the run over 200000 terms: no period ≤ 1000).

## Hypotheses

n ≥ 1 integer. Holds here.

## What it lets this run do

- Names the per-sector hidden count: H(n) = 6·Σ_{k≤n}(k − φ(k)) =
  6·A063985(n), where A063985 is the partial sums of this sequence. Confirms
  the run's seq_cototient.txt used for pattern checks.

## What it does not settle

- No summatory values at 10⁸ (that is A063985).

## Claims

```claim
id: cototient-definition
statement: The cototient is n − φ(n); its partial sums are A063985(n), and
H(n) = 6·A063985(n) for the hexagonal orchard.
hypotheses: n ≥ 1 integer.
holds-here: yes — H(n) = 6·A063985(n) verified at n ≤ 10^8 (patterns.py).
status: sourced (OEIS A051953/A063985); checked here.
bearing: ties the per-sector hidden count to the cototient partial sums.
anchor: research/summaries/oeis-A051953-cototient.md
```
