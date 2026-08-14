# Refutation: G-stabilization candidate threshold is too small

## Statement attacked

The `G-stabilization` lemma's first-step candidate in both `research/backward/fib-subword-squares.md`
and `fibonacci-subword-squares.md`:

> n0(k) = smallest n with |S_{n-1}| >= k is a valid stabilization threshold:
> the length-k factor set of S_n is constant for all n >= n0(k), equals the set
> of length-k factors of the infinite Fibonacci word f = lim S_n, and has size
> exactly k+1.

## Hand counterexample (k=3)

Fibonacci words: S_0="0", S_1="01", S_2="010", S_3="01001", S_4="01001010".
Lengths: |S_n| = F_{n+2}: 1, 2, 3, 5, 8.

For k=3, the candidate gives n0(3) = smallest n with |S_{n-1}| ≥ 3. |S_2| = 3
≥ 3, so n0(3) = **3**. The claimed threshold word is S_3 = "01001".

The length-3 substrings of S_3 = "01001" are {010, 100, 001} — only **3**
distinct words.

But the true length-3 factor set of the infinite Fibonacci word f is
{001, 010, 100, 101} — **4** words (k+1). The word "101" is a genuine length-3
Fibonacci subword (it first appears in S_4 = "01001010"), yet it does NOT
appear in S_3.

Hence S_{n0(3)} = S_3 does not already contain the stabilised factor set:
the candidate n0(3)=3 is too small. The threshold as stated is **False**.

## Encoding and engine result

`code/refute/stab_k3c.p` encodes S_3 ("01001") as five positions with a
successor chain and binary labels, and asks whether "101" occurs as a length-3
factor.

`find_counterexample` returned **refuted (CounterSatisfiable)**: the model
{p0:0, p1:1, p2:0, p3:0, p4:1} = "01001" satisfies the axioms (the word is
exactly S_3) and falsifies the conjecture (no consecutive triple has labels
1,0,1). Checked by hand: consecutive triples are 010, 100, 001; none is 101.

## Inference for the run

- **The specific candidate is wrong.** The stabilization threshold is not the
  obvious "smallest n with |S_{n-1}| ≥ k". (Actually the true threshold is
  larger; e.g. for k=3 one needs n=4.)
- **Not a full refutation of G-stabilization itself.** The lemma's *conclusion*
  (the factor set stabilizes to f's, of size k+1) is a standard Sturmian fact
  and remains well supported. What is disproved is that *this particular
  candidate* n0(k) computes a valid threshold. The run must find the correct
  n0(k), not take |S_{n-1}| ≥ k as sufficient.

## Files

- `code/refute/stab_k3c.p` — TPTP problem, CounterSatisfiable.
- `code/refute/verify_threshold.py` — independent direct program producing the
  same k=3 result (S_3 has 3/4 factors; "101" missing).
- `code/refute/stabilization_threshold.py` — sweeps candidate vs empirical
  threshold over k=1..40.

```claim
id: PE1006-stabilization-candidate-too-small-k3
statement: The G-stabilization first-step candidate n0(k)=smallest n with |S_{n-1}|>=k is not a valid stabilization threshold. For k=3, n0(3)=3 but S_3="01001" has only 3 distinct length-3 factors {001,010,100}, missing the true factor "101" (which first appears in S_4). So S_{n0(3)} does not already contain the stabilized length-3 factor set of f.
hypotheses: Fibonacci words S_0="0",S_1="01",S_n=S_{n-1}S_{n-2}; |S_n|=F_{n+2}; length-k factor set of f has size k+1 and equals {001,010,100,101} for k=3.
holds-here: yes (disproof of the candidate threshold; the leaf conclusion of G-stabilization is separately a standard Sturmian fact).
status: checked — verified by TPTP find_counterexample (CounterSatisfiable on stab_k3c.p) and independently by direct program (S_3 has 3/4 factors).
bearing: The stabilization threshold for the lever must be chosen larger than "smallest n with |S_{n-1}|>=k"; the run's higher rungs (which replace substring scanning by a theorem with a computable n0(k)) must not use this candidate.
anchor: code/refute/stab_k3c.p; code/refute/verify_threshold.py
```
