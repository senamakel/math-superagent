# Cassaigne, "Complexité et facteurs spéciaux", Bull. Belg. Math. Soc. 4 (1997) 67–88

Full text: `research/sources/cassaigne-complexite-facteurs-speciaux-1997.full.md`
(URL: https://emis.muni.cz/journals/BBMS/Bulletin/bul971/cassaigne.pdf; DOI 10.36045/bbms/1105730624;
the Project Euclid abstract page converted to 3.7 KB only; the EMIS mirror carries the full PDF, 58 KB, 1457 lines, French with English abstract.)

## What it establishes

The special-factor machinery for computing factor complexity of infinite words on a finite alphabet.
This is the exact framework behind the run's adopted approach `pe1006-rauzy-right-special-extension-recurrence`
and the claim `fibonacci-unique-special-factor-reverse`.

- **Definition** (Section 3.2): for a factorial extendable language L over a binary alphabet, u ∈ L is
  *right-special* if ua and ub are both in L, *left-special* if au and bu are both in L.
- **Proposition 3.1**: the number of right-special factors of length n equals the number of left-special
  factors, call it s(n), and
  s(n) = p(n+1) − p(n),
  where p(n) is the factor complexity. Proof: of the p(n) length-n factors, s(n) extend two ways, the rest
  one way, so p(n+1) = 2s(n) + (p(n) − s(n)). Immediate consequence: complexity is non-decreasing.
- **Bispecial factors** (Section 3.3): u is *bispecial* if special both sides; *strict* if ua,ub,au,bu
  generate 4 distinct two-sided extensions (L ∩ ΣuΣ of size 4), *ordinary* (3), *weak* (2).
- **Proposition 3.2**: with bs(n), bf(n) the counts of strict and weak bispecial factors,
  bs(n) − bf(n) = s(n+1) − s(n).
  Hence p is determined by bs, bf alone (Prop 3.1 + 3.2); in low-complexity words bispecial factors are few
  and often directly enumerable, which is the advertised route to exact complexity.
- **Proposition 3.3**: generating-function packaging: P(X) = (1 + X S(X))/(1−X) and
  S(X) = (1 + X(BS(X) − BF(X)))/(1−X) when p(1) = 2.
- The Fibonacci word's right-special tree is *filiform* (a single chain): Figure 3 shows the right-special
  factor tree for the Fibonacci word, which is exactly the run's right-special-run structure
  (right-special-factor run starts s_j = ⌊j·φ²⌋, verified k=1..1146 in CONTEXT.md).
- Rauzy-graph expansion rule (Figure 5): passing from length-n to length-(n+1) factor graph replaces each
  edge by a vertex and each vertex by 1/2/3/4 edges according as the word is non-special / special-non-bispecial
  or weak-bispecial / ordinary-bispecial / strict-bispecial.

## Relevance to PE1006

- The right-special factor is the single "fork" in the Fibonacci word's factor tree; s(n) = p(n+1) − p(n) = 1
  for every n (since p(n) = n+1), consistent with exactly one right-special factor of each length
  (claim `fibonacci-unique-special-factor-reverse`).
- The run's `directive9_transfer.py` and the adopted second route build the length-(k+1) factors from
  length-k ones via the right-special extension — Prop 3.1/3.2 is the source-level statement of why the
  extension counts work (each non-special factor extends uniquely; only the right-special one branches).
- The run's verified pattern Ψ(k+1) = 100Ψ(k) + 100V(R_k)² + 20S1(k) + J(k) is exactly a weighted version
  of this extension accounting.

## Claim block

```claim
id: cassaigne-special-factor-complexity
statement: For a factorial extendable language L over a binary alphabet with factor complexity p(n),
the number s(n) of right-special (equivalently left-special) factors of length n satisfies
s(n) = p(n+1) - p(n) (Prop 3.1), and with bs(n), bf(n) the strict and weak bispecial counts,
bs(n) - bf(n) = s(n+1) - s(n) (Prop 3.2); the generating-function forms are
P(X) = (1 + X S(X))/(1-X) and S(X) = (1 + X(BS(X) - BF(X)))/(1-X) when p(1) = 2 (Prop 3.3).
hypotheses: L factorial and extendable, binary alphabet, p(1) = 2 for the generating-function form.
holds-here: yes — the Fibonacci word's factor language is factorial and extendable on {0,1},
p(n) = n+1, and s(n) = 1 for every n (one right-special factor of each length, the reverse of the
length-n prefix, claim fibonacci-unique-special-factor-reverse); the right-special tree is filiform.
status: sourced
bearing: Source-level statement of the special-factor extension accounting behind the adopted
Rauzy/right-special route (pe1006-rauzy-right-special-extension-recurrence) and the verified
Psi(k+1)-from-Psi(k) right-extension pattern: each non-special factor extends uniquely, only the
right-special one forks, so the k+1 -> k+2 factor transition is controlled by the single special factor.
anchor: research/sources/cassaigne-complexite-facteurs-speciaux-1997.full.md
  (Prop 3.1 p.71-72, Prop 3.2 p.73, Prop 3.3 p.73-74; Figure 3 = Fibonacci right-special tree)
```

## Acquisition notes

- Project Euclid `.full` URL returned only a 3.7 KB abstract page (converted), not the full text;
  the EMIS mirror PDF (https://emis.muni.cz/journals/BBMS/Bulletin/bul971/cassaigne.pdf) converted cleanly.
- The DIMACS "BWT: Ten Years Later" PDF (http://dimacs.rutgers.edu/Workshops/BWT/bwt10.pdf) 404'd;
  the Dagstuhl festschrift chapter (Fici, Mantaci, Restivo, Romana, Rosone, Sciortino, "BWT and Combinatorics
  on Words") was downloaded instead as the modern survey of the Sturmian/BWT connection.
