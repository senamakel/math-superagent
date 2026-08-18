> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/eliahou-fromentin-simonetto-2022-syracuse-falling-time-hal.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

```claim
id: efs-falling-time-14
statement: The falling time ft(n) (number of steps until the orbit first drops below n) satisfies ft(n) ≤ 14 for all n ∈ [1, 2^35 − 1] with n ≡ 3 mod 4 (Proposition 2.1).
hypotheses: n in [1, 2^35−1], n ≡ 3 mod 4; falling time of the accelerated map.
holds-here: true — a verified-numerically established bound on a restricted class (the n ≡ 3 mod 4 class up to 2^35).
evidence: proved/computed in source (Eliahou–Simonetto 2021/2022, Proposition 2.1).
status: verified-numerically
falsifies: an n in that range with ft(n) > 14, or an error in the computation.
```

```claim
id: efs-sft-9
statement: The Syracuse falling time sft(n) satisfies sft(n) ≤ 9 for all n ∈ [3, 2^35 − 1] with n ≡ 3 mod 4 (Proposition 3.6).
hypotheses: n in [3, 2^35−1], n ≡ 3 mod 4; Syracuse falling time of the odd-only map.
holds-here: true — a verified-numerically established bound on the n ≡ 3 mod 4 class.
evidence: proved/computed in source (Eliahou–Simonetto 2021/2022, Proposition 3.6).
status: verified-numerically
falsifies: an n in that range with sft(n) > 9, or an error in the computation.
```

```claim
id: efs-conjectures
statement: Conjectures: ft(n) ≤ B for some B ≥ 15 for all n ≥ 3 (Conj 2.3); ft(2^ℓ − 1) ≤ 4 for all ℓ ≥ 133 (Conj 4.2); sft(n) ≤ 2 for all odd n ≥ 2^5000 (Conj 5.2). All open.
hypotheses: none — conjectures.
holds-here: true — stated as conjectures in the source, verified computationally up to the stated bounds.
evidence: asserted as conjectures in source (Eliahou–Simonetto 2021/2022).
status: conjectured
falsifies: a counterexample exceeding the conjectured bound.
```

<!-- source: https://hal.science/hal-03294829v3/file/falling%20time.pdf | converted from PDF -->

## What it claims

HAL is a multi-disciplinary open access archive
for the deposit and dissemination of scientific re-
search documents, whether they are published or not.
The documents may come from teaching and research
institutions in France or abroad, or from public or pri-
vate research centers.
 L’archive ouverte pluridisciplinaire HAL, est des-
tinée au dépôt et à la diffusion de documents scien-
tifiques de niveau recherche, publiés ou non, émanant
des établissements d’enseignement et de recherche
français ou étrangers, des laboratoires publics ou
privés.

HAL Authorization

Is the Syracuse falling time bounded by 12?

Shalom Eliahou, Rénald Simonetto

To cite this version:

Shalom Eliahou, Rénald Simonetto. Is the Syracuse falling time bounded by 12?. 2021. ⟨hal-03294829v3⟩

Is the Syracuse falling time bounded by 12?

Shalom Eliahou∗ and R´enald Simonetto
†

Abstract
Let T : N → N denote the 3x+1 function, where T (n) = n/2 if n is
even, T (n) = (3n+1)/2 if n is odd. As an accelerated version of T , we
deﬁne a jump at n ≥ 1 by jp(n) = T (ℓ)(n), where ℓ is the number of
digits of n in base 2.…

## Statements it makes

Proposition 2.1 We have ft(n) ≤ 14 for all n ∈ [1, 2
35 − 1] such that
n ≡ 3 mod 4.
 3

Conjecture 2.3 There exists B ≥ 15 such that ft(n) ≤ B for all n ≥ 3.

Proposition 3.6 We have sft(n) ≤ 9 for all n ∈ [3, 2
35 − 1] such that n ≡
3 mod 4.

Conjecture 3.7 There exists C ≥ 10 such that sft(n) ≤ C for all n ≡
3 mod 4.

Proposition 4.1 Besides ft(2
5 − 1) = ft(26 − 1) = 8, we have ft(2
ℓ − 1) ≤ 5
for all 2 ≤ ℓ ≤ 100 000 with ℓ /∈ {5, 6}.

Conjecture 4.2 We have ft(2
ℓ − 1) ≤ 4 for all ℓ ≥ 133.

Proposition 4.3 Besides sft(2
5 − 1) = sft(26 − 1) = 5, and sft(2
24 − 1) = 4,
we have sft(2
ℓ − 1) ∈ {2, 3} for all ℓ ∈ [2, 4 624] \ {5, 6, 24},

Conjecture 4.4 We have sft(2
ℓ − 1) = 2 for all ℓ ≥ 4 625.

Conjecture 5.1 We have ft(n) ≤ 4 for all n ≥ 2
150.

Conjecture 5.2 We have sft(n) ≤ 2 for all odd n ≥ 2
5000.

*[digest of a 19236 character source; every section, statement, and proof in full at `research/sources/eliahou-fromentin-simonetto-2022-syracuse-falling-time-hal.full.md`]*
