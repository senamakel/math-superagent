# Librarian cycle — Cobham theorem modern tier added (Durand–Rigo EMS 2021)

## What was added

1. **Durand & Rigo, "On Cobham's theorem", EMS Handbook of Automata Theory
   (2021), ch. 26, pp. 897–921** — full author postprint obtained from ORBi
   (https://orbi.uliege.be/bitstream/2268/39461/1/Chapter26.pdf, after the
   EMS DOI 404'd) → `research/sources/durand-rigo-on-cobham-theorem-ems-2021.full.md`
   Digest replaced with a real summary at
   `research/summaries/durand-rigo-on-cobham-theorem-ems-2021.md`.
   Key content for this run (verified in full text):
   - Example 2.1 names the Fibonacci numeration system explicitly
     (U0=1, U1=2, U_{n+2}=U_{n+1}+U_n, language L = 1{0,01}* ∪ {ε}) as a Pisot
     numeration system with β = (1+√5)/2 — the exact object whose independence
     from base 10 is this run's Cobham obstruction.
   - Theorem 1.1 (Cobham), Theorem 3.4 (automatic-word version), Theorem 4.7
     (Cobham–Semenov, higher dimension), Theorem 2.3/Prop 2.4 (Parry/Bertrand
     bridge).
2. **Lead recorded (not obtained, paywalled):** A. Bès, "An extension of the
   Cobham–Semënov theorem", JSL 65(1) (2000) 201–211, DOI 10.2307/2586532 —
   the *precise* Pisot-vs-Pisot statement (multiplicatively independent Pisot θ,
   θ′, U- and U′-recognizable ⟹ definable in ⟨N,+⟩). Both Cambridge Core and
   JSTOR paywalled; abstract statement recorded so the claim has a citable
   primary name even without full text.

## State of the claim and the library

- The claim `cobham-bes-frougny-multiplicatively-independent-conversion` now
  has **three anchors**: Bruyère–Hansel–Michaux–Villemaire 1994 (added last
  cycle, primary tier, Cobham–Semenov Thm 7.7 verified in full text),
  Frougny 2002 (linear numeration), and now Durand–Rigo 2021 (modern EMS
  survey with the Fibonacci/Pisot identification explicit).
- All four research requests remain closed (`answers:` lines present).
- OEIS lookups: raw Ψ(k) not catalogued (recorded), Lmin(k)=A344953,
  c1(k)=A189663 (recorded).
- Cognee was down again this cycle (remember_memory refused, server health
  timeout); the additions live in the workspace and will be stored when it
  recovers.

## Next-cycle recommendation

The library is saturated on the Cobham/non-automaticity side and on the
Sturmian/mechanical/floor-sum side. Frontier top rows left are paywalled
primaries (Morse–Hedlund 1940, Berstel 1986 Book of L) whose content is
covered by held surveys (Lothaire C2, Perrin–Restivo, Berstel 2007, Coven–
Hedlund abstract). The solver's wiring of mech_psi through ueuclid is the
scarce-resource item (directive 10 order); the librarian contributes nothing
further until that is done or a new gap opens.