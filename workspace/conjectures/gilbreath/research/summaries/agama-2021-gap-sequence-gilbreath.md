# Agama 2021 — On the Gap sequence and the Gilbreath conjecture

**Full text:** `research/sources/agama-2021-gap-sequence-gilbreath.full.md`
**Source URL:** https://arxiv.org/abs/2104.05258 (v3, 5 Apr 2026; math.CO)
**Complete text on disk.** arXiv:2104.05258, single author (T. Agama, AIMS Ghana).

## What it establishes

A **combinatorial reformulation framework** for the iterated-difference triangle —
nothing stronger. It defines, for a finite originator `a_1..a_n`:

- the *path of order k* = row `k` of the triangle (`d_j^k` are its *segments*);
- the *length* of a path `ι_{t,k} = Σ_j d_j^k` (row sum);
- the *circuit* = the whole triangle; its length `κ(n) = Σ_k ι_{n−k,k}`;
- the *trace of the s-th segment* `τ_{n,s} = Σ_{k=1}^{n−s} d_s^k` — the sum of the
  s-th entry across all rows. `τ_{n,1}` is the **sum of the leading entries**.

## Theorems (all elementary, all proved in the paper)

- Prop. 2.3: total number of segments in the whole triangle is `n(n−1)/2`.
- Prop. 3.2/3.3: row-sum bounds via the max adjacent difference in the previous
  row; if that max is ≤ c then some segment of the next row is ≤ c.
- Prop. 4.5, Thm. 4.7: inequalities relating circuit length, traces, and the
  originator's endpoints, e.g. `κ(n) + τ_{n,1} ≥ (2a_n − a_{n−1} − a_1) + Σ_{j≤n−2} d_j^{n−j}`.
- Prop. 5.1: if `τ_{n,s} < n − s` then some `d_s^t = 0`.
- Prop. 5.2: if all leading entries `d_1^k > 0` and `τ_{n,1} = n − 1`, then every
  leading entry equals 1 (one line: `n−1` positive integers summing to `n−1`).

## The "reduction"

Conjecture 5.3 restates Gilbreath's conjecture as: for the primes,
`d_1^k > 0` for all `1 ≤ k ≤ n−1` **and** `τ_{n,1} = n−1` for all `n ≥ 2`.
This is exactly equivalent to `A_k(0) = 1` for all k, since each leading entry is
a positive integer (odd by parity) — Prop. 5.2 is the if-direction of the same
statement. It is a **restatement in new vocabulary, not a proof mechanism**:
the trace condition is the conjecture itself, and no proposition in the paper
shows it holds for the primes.

## Bearing on this run

- Confirms (from a peer-path not yet in the library) that a "trace/reduction"
  approach ends in a tautology unless it proves something about the trace sum.
  The one genuinely usable observation: since every leading entry is a positive
  integer, **GC ⟺ (sum of the first k leading entries = k for every k)** — the
  partial sums of `A_k(0)` must be exactly the index. Equivalent, but it converts
  the claim into a statement about an increasing quantity with slope 1, which is
  the shape an invariant argument could target.
- The correct ScienceDirect PII for Gilbreath 2011 (S0022314X11001740) is
  recorded in the Houston blog source; the Agama reference list repeats the
  wrong Proth citation ("CR 87(2) 926", which the library has already refuted
  in `proth-citation-correction`) — an independent sign of the citation tangle
  around Proth's paper.

## Status

All propositions checked structurally against the triangle definition; they are
elementary and correct as stated. The paper proves **no new theorem about the
conjecture**; treat any claim that it "reduces" GC as a restatement, not progress.