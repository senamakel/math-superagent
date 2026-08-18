# Chuan, "Fibonacci Words" — rotation/standard-word structure claim

Source: https://www.fq.math.ca/Scanned/30-1/chuan.pdf
Summary: [[chuan-fibonacci-words-fq1992]]
Full text: [[chuan-fibonacci-words-fq1992.full]]

```claim
id: chuan-fibonacci-words-rotation-structure
statement: For distinct letters x,y and the n-th stage Fibonacci words
(w_1=x, w_2=y, w_{n+1}=w_n w_{n-1} or w_{n-1} w_n with arbitrary binary labels),
every Fibonacci word in F_n is a cyclic shift of the standard word w_n^0
(all-labels-0; Thm 6), and conversely every cyclic shift of w_n^0 is in F_n
(Thm 7) — the set F_n is exactly the full rotation class of w_n^0, of size F_n
(Cor 12: the F_n shifts T^{js}q_n with s=F_{n-2} (n odd) / F_{n-1} (n even),
0<=j<F_n, are pairwise distinct). Lemmas 8-9: for every 0<=v<=F_n-1 the
equation v = sum_j p_j*l(w_{j+1}^0) has a {0,1} solution, and
{j*F_{n-1} mod F_n : 0<=j<F_n} and {j*F_{n-2} mod F_n : 0<=j<F_n} are complete
residue systems mod F_n. Thm 11: in q_n = w_n^{0101...}, a letter is 'a' iff its
position k satisfies k ≡ j*t (mod F_n) with t = F_{n-1} (n odd) / F_{n-2}
(n even), 1<=j<=F_{n-2}. Thm 4/Lemma 5: w_n^0 = v_n u_n with v_n,u_n symmetric,
and l(w_n) = l(w_{n-1}) + l(w_{n-2}), with closed forms
l(w_n^1) = (F_{n-4}+1)l(x) + (F_{n-3}+1)l(y),
l(v_n) = (F_{n-3}-1)l(x) + (F_{n-2}-1)l(y).
hypotheses: x, y distinct letters (the 0/1 rabbit word, digit complement of
PE1006's S_n); lengths F_n = l(w_n^0) with F_1=F_2=1.
holds-here: yes — PE1006's length-k subwords are the length-k factors of the
(complemented) Fibonacci word, and the finite-word rotation structure of the
stage-n standard word is exactly what positions the contiguous windows that
yield the k+1 distinct factors (directive 9 Claim 1).
status: sourced — the paper proves each statement by induction in the text
(read and checked against the full text); nothing here re-derives them, and
the PE1006-side union with the Sturmian/position theorems (p(k)=k+1;
Sivasankar-Rama; arXiv:2207.04304 Lemma 2) is a synthesis, not a source
statement.
bearing: Primary finite-word source for the rotation/contiguous-window
identification in directive 9's reduction (the k+1 distinct length-k factors
are contiguous windows of the doubled standard word q_n q_n — the rotation
class is the anchor for which windows are available), and for the
Fibonacci-block length recurrence (Lemma 5) used to collapse the prefix sum of
v_r^2 in O(log). It does NOT establish the specific window range
r = F_n-k-1..F_n-1 of q_n q_n (that stays solver-verified vs mech_psi/brute).
anchor: research/sources/chuan-fibonacci-words-fq1992.full.md (Thm 4, 6, 7, 11;
Cor 12; Lemmas 5, 8, 9)
```

## What it implies for PE1006

The rotation class of the stage-n standard word (with letters at
Fibonacci-residue positions, Thm 11) is the finite-word structure behind the
way the k+1 distinct length-k factors sit as contiguous windows. Combined with
the Sturmian factor-complexity theorem already held, this supports — but does
not by itself state — directive 9 Claim 1's "windows of q_n q_n at positions
F_n-k-1..F_n-1", which remains a solver-verification task against
mech_psi/brute (see `fibonacci-word-contiguous-factors-position-theorem`).

## Access notes

Chuan–Ho "Locating factors of the infinite Fibonacci word" (TCS 2005,
DOI 10.1016/j.tcs.2005.08.033) and its 2010/2012 successors are paywalled at
ScienceDirect with no open mirror; this 1992 paper (free at fq.math.ca) covers
the finite rotation structure that route needs. The 1992 paper's Lemma 8 is the
"sum of distinct Fibonacci numbers" lemma (proof vehicle for Thm 7), NOT a
residue statement — the residue systems are Lemma 9.