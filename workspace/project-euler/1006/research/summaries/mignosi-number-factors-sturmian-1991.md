# Mignosi 1991 — On the number of factors of Sturmian words

**Source:** F. Mignosi, *Theoretical Computer Science* 82 (1991) 71–84, doi:10.1016/0304-3975(91)90172-x.
**Status: abstract/record page only.** Full text is paywalled (ScienceDirect).
**Held in library as:** `research/sources/mignosi-number-factors-sturmian-1991.full.md` (record page HTML).

## What the source establishes

From the abstract: For m ≥ 1,
\[
\operatorname{card}(A_m) = 1 + \sum_{i=1}^{m} (m - i + 1)\,\varphi(i)
\]
where \(A_m\) is the set of **length-m factors of all Sturmian words** (the *finite Sturmian language*, i.e. the union over every Sturmian word) and \(\varphi\) is Euler's totient. The result was conjectured by Dulucq & Gouyou-Beauchamps (1987), who proved it implies the complement language is inherently ambiguous.

The paper also gives a "combinatorial version of the Riemann hypothesis" (not relevant here).

## What this is NOT for PE1006

- This is **not** the run's count. PE1006's \(F_k\) is the factor set of a *single* Sturmian word (the Fibonacci word), which has \(|F_k| = k+1\). Mignosi's \(A_m\) is the union over *all* Sturmian words — a strictly larger object.
- The totient formula is the canonical reference for the *finite Sturmian language* and is cited in this role by Berstel 2007, Berthé 1996, Choffrut–Karhumäki 1997, and the Lothaire chapter already held.
- No new engine for G4: the gap remains the fixed-dimensional joint second-moment aggregation, which this source does not address.

## In-library coverage

- The Berstel 2007 survey (`berstel-sturmian-episturmian-survey-2007.full.md`) and Berthé 1996 (`berthe-frequences-facteurs-sturmiennes-1996.full.md`) cite and use the Mignosi enumeration. The formula's substance is accessible through those sources.
- The companion paper — de Luca & Mignosi, "Some combinatorial properties of Sturmian words", TCS 136 (1994) 361–385 — is also paywalled; its content is covered in-library by the Perrin–Restivo note and the Lothaire chapter.

## Claim

```claim
id: mignosi-1991-sturmian-language-count
statement: For m≥1, the number of distinct length-m factors occurring in *any* Sturmian word (the finite Sturmian language) is
  card(A_m) = 1 + Σ_{i=1}^{m} (m−i+1) φ(i)
where φ is Euler's totient.
hypotheses: Sturmian = irrational-slope mechanical words; infinite binary.
holds-here: no — PE1006's F_k is the factor set of a *single* Sturmian word (Fibonacci word), which has |F_k|=k+1, not this union count.
status: asserted (from abstract only; full text not consulted; formula hand-verified for m=1..4 in research/notes/verification-mignosi-1991-totient.md)
bearing: Confirms that the run's k+1 count is the correct one for a single Sturmian word, as the larger union count would be a different problem.
anchor: research/sources/mignosi-number-factors-sturmian-1991.full.md
follows-from: none (primary enumeration; cited by Berstel 2007, Berthé 1996, Choffrut–Karhumäki, Lothaire)

```