# Precedent pass — candidate approaches tested against the literature

This note records the claim blocks arising from taking the three candidate
approaches to the literature. See the approach files themselves for the full
precedent analysis:

- `research/approaches/pe1006-contiguous-window-cyclic-minus-prefix.md` (refuted)
- `research/approaches/pe1006-rauzy-right-special-extension-recurrence.md` (grounded)
- `research/approaches/pe1006-zeckendorf-automatic-digit-dp.md` (refuted)

```claim
id: cobham-bes-frougny-multiplicatively-independent-conversion
statement: Two linear numeration systems (over Pisot bases) are mutually
recognisable / convertible by finite automata only if their bases are
multiplicatively dependent. In particular, since 10 and phi = (1+sqrt5)/2 are
multiplicatively independent Pisot numbers, Zeckendorf (base-phi/Fibonacci)
representation and decimal (base-10) representation cannot be converted or
jointly processed by a finite automaton.
hypotheses: linear numeration systems with Pisot bases; multiplicatively
independent means 10^a != phi^b for a,b in Z except a=b=0.
holds-here: yes — PE1006's windows carry base-10 values (10^{k-1-j}) at
positions indexed by Zeckendorf (r+j), so a digit-DP over Zeckendorf for a
decimal-weighted value needs exactly the prohibited conversion.
status: sourced
bearing: Refutes the Zeckendorf-automatic digit-DP candidate: its mechanism
computes base-10 window values from Zeckendorf positions, which requires
automaton conversion between multiplicatively independent bases. Blocks the
digit-DP route (and any claim that the base-10-weighted window map v(r) is
Zeckendorf-regular).
anchor: Frougny, "On multiplicatively dependent linear numeration systems, and
periodic points", RAIRO-ITA 36 (2002) 143-157, doi:10.1051/ita:2002015, quoting
Bès's theorem — full text NOW ON DISK at
research/sources/frougny-mult-dep-linear-numeration-2002-irif.full.md (Theorem
2, Corollary 1, Prop 8 match this statement; the intro quotes Bès's Cobham
generalisation verbatim); Berend & Frougny, "Computability by finite automata
and Pisot bases", Math. Systems Theory 27 (1994) 275-282; Frougny,
"Representation of numbers and finite automata", Math. Systems Theory 25 (1992)
37-60; Cobham 1969 for integer bases.
```

```claim
id: unique-right-special-sturmian-sourced
statement: A Sturmian word has exactly one right-special factor of each length:
p(n+1)-p(n) = #{right-special factors of length n} = 1 for a Sturmian word
(Cassaigne's special-factor complexity difference), and for the Fibonacci word
the unique right-special length-n factor is the reverse of the n-prefix
f[0..n-1]^R.
hypotheses: Sturmian word (Fibonacci word = f, fixed point of 0->01, 1->0);
factor complexity p(n) = n+1.
holds-here: yes — reinforces the run's pattern-hunt recurrence for Psi(k+1) via
right-extension structure.
status: sourced
bearing: Grounds the Rauzy-graph right-special extension recurrence candidate:
the unique R_k with both right extensions is the structural hinge of
Psi(k+1)=100Psi(k)+100V(R_k)^2+20S1(k)+J(k), and its exact value is
literature-specified.
anchor: Cassaigne, "Complexité des facteurs spéciaux", Bull. Belg. Math. Soc. 4
(1997) 67-88 (claim special-factor-complexity-difference in library); Du, Mousavi,
Schaeffer & Shallit, arXiv:1406.0670, Thm 18 (claim
fibonacci-unique-special-factor-reverse); Masáková & Pelantová, arXiv:0809.0603.
```

```claim
id: fibonacci-word-contiguous-factors-position-theorem
statement: The k+1 distinct length-k factors of the (rabbit, 1<->0 complement of
PE1006's S) Fibonacci word occur as contiguous windows at first-occurrence
positions (Sivasankar & Rama), with the count k+1 invariant under the digit
complement; but the SPECIFIC positions "r = F_n-k-1..F_n-1 of the doubled
standard word q_n q_n" asserted by the contiguous-window candidate are NOT a
verbatim literature statement — they are a solver-verification task against
mech_psi/brute.
hypotheses: F(n) <= k < F(n+1); Fibonacci word in rabbit convention.
holds-here: yes for the set identity (count k+1), with the caveat that the
explicit q_n q_n window positions are verified in-container, not cited.
status: asserted
bearing: Grounds the set half of the contiguous-window candidate while honestly
marking the specific-position claim as solver-verified, not literature — so the
candidate's O(log) collapse (the one distinct contribution) has no source and is
what refutes it as an independent method.
anchor: Sivasankar & Rama, "Two-dimensional Fibonacci Words: Tandem repeats and
factor complexity", arXiv:2204.13977, Thm 7 (claim
sivasankar-rama-position-theorem in library).
```
