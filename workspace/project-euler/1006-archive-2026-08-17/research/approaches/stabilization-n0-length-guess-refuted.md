# Refutation: the G-stabilization threshold guess n0(k) = min{ n : |S_{n-1}| >= k }

## The attack

`G-stabilization` (correct lemma): the set of length-k factors of S_n is
constant for all n >= n0(k), equals the length-k factor set of the infinite
Fibonacci word f, and has cardinality k+1. The lemma is *true* (standard
Sturmian fact, uniformly recurrent word, monotone growth of the factor set).

Its **first step** proposed an explicit candidate threshold:

    n0(k) = the smallest n with |S_{n-1}| >= k

(with |S_m| = F_{m+2} the Fibonacci word lengths). I attacked that candidate,
not the lemma: a wrong threshold guidance is exactly the kind of small concrete
falsehood the run should be warned away from before it builds on it.

## Counterexample: k = 3

|S_2| = |"010"| = 3 >= 3, so the candidate gives **n0(3) = 3**. But

    S_3 = S_2 S_1 = "010" + "01" = "01001"

has length-3 factor set {010, 100, 001} — **3 words, missing 101**. The full
length-3 factor set of the infinite Fibonacci word is {001, 010, 100, 101}
(4 = k+1 words), and in fact the published oracle depends on 101: it is the
factor read as 101 whose square 101² = 10201 is the largest term of
Ψ(3) = 1 + 100 + 10000 + 10201 = 20302. Removing 101 would give 1+100+10000
= 10101 ≠ 20302.

The factor set reaches size 4 only at n = 4: S_4 = S_3 S_2 = "01001010",
whose length-3 factors are 010,100,001,010,101,010 → distinct {010,100,001,101}.

So the candidate n0(3) = 3 is **false**: at n0(3) the length-3 factor set is
not yet the full set and is not constant (it grows 3 → 4 from n=3 to n=4).
The correct stabilization index for k=3 is n0(3) = 4.

## Why the guess fails in general

The length-k factor set of S_n is the full (size k+1) set iff S_n has
*already* realized every factor, and the last factor to appear is not
controlled by mere length |S_n| >= k+1. The right threshold is a *recurrence
depth* (how far into f must a prefix go before every length-k factor has
appeared), not a bare length bound. |S_{n-1}| >= k guarantees S_n has *at least
one* window of each start but says nothing about which set of windows is
realized.

## TPTP confirmation

`code/refute/stabilization_n0_k3.p` encodes the k=3 case: axioms fix p(0..4)
as the letters of S_3 = "01001" (p = F,T,F,F,T); the conjecture asserts the
factor "101" occurs contiguously. `find_counterexample` returned
`CounterSatisfiable`: an explicit 5-element model satisfying the axioms with
p = (F,T,F,F,T) that falsifies the conjecture. This is exactly the hand check:
S_3 has no "101", so its factor set (3 words) is not the full set (4 words).

## Result

- The **lemma** `G-stabilization` remains true — this refutes only the *first
  step's candidate formula* for n0(k).
- The candidate `n0(k) = min n : |S_{n-1}| >= k` is **refuted** (smallest case
  k=3). It is a length bound, not a recurrence-depth bound, so it systematically
  undershoots. Any code or proof that assumes the factor set is stable at that
  threshold is wrong.

```claim
id: PE1006-n0-length-guess-refuted-small
statement: The candidate threshold n0(k) = smallest n with |S_{n-1}| >= k is FALSE: for k=3, |S_2|=3>=3 gives n0(3)=3, but S_3="01001" has length-3 factor set {010,100,001} (3 words), missing 101; the full size-4 set {001,010,100,101} (whose 101 term is needed for Psi(3)=20302) appears only at n=4. A length bound |S_n|>=k+1 does not guarantee every length-k factor has appeared; the true n0(k) is a recurrence-depth threshold, not a length threshold.
hypotheses: Fibonacci word lengths |S_m| = F_{m+2}; factor set of S_3 from direct enumeration.
holds-here: yes — this is the counterexample to the first-step candidate, not a hypothesis check.
status: checked — hand-enumerated S_3 = "01001" and S_4 = "01001010"; confirmed by find_counterexample (CounterSatisfiable) on code/refute/stabilization_n0_k3.p, and Psi(3)=20302 (sum 1+100+10000+10201) requires the 101 factor.
bearing: G-stabilization lemma stands, but the first-step candidate threshold must be replaced by a recurrence-depth threshold (e.g. smallest n such that the prefix of f of length |S_n| realizes all k+1 factors), not min{ n : |S_{n-1}| >= k }.
anchor: research/approaches/stabilization-n0-length-guess-refuted.md
answers: G-stabilization first step
contradicts: the candidate formula n0(k)=min{n:|S_{n-1}|>=k}
```
