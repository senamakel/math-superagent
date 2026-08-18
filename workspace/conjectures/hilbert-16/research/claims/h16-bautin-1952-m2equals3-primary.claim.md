```claim
id: h16-bautin-1952-m2equals3-primary
statement: Bautin (1952), "On the number of limit cycles appearing with variation of the coefficients from an equilibrium state of the type of a focus or a center" (Mat. Sb. (N.S.) 30(72):1 (1952) 181–196): the maximum number of small-amplitude limit cycles that can appear from a focus/center equilibrium of a quadratic system as the coefficients vary over ALL variations is exactly 3 (M(2) = 3), and a quadratic system with 3 small-amplitude cycles is exhibited. Under the condition (a10−b01)²+4a10b01 < 0 the family reduces to the canonical focus form (II) in the six coefficients λ1,…,λ5, where λ1=λ4=λ5=0 is the center condition (Px+Qy=0); the polar-coordinate radial equation (III) expanded in ρ gives the Lyapunov quantities, and the ideal they generate (the Bautin ideal) has the finite-generation structure that makes degree-4 the first obstruction.
hypotheses: quadratic planar polynomial systems; small-amplitude cycles about a single focus/center; all coefficient variations. This is the LOCAL problem (a single equilibrium), NOT the global H(2) (Shi/Chen–Wang's 4 cycles are global, from separate nests).
holds-here: yes — this is the literature boundary the run's Bautin oracle (task bautin-m2-oracle) must reproduce before trusting anything computed past it.
status: asserted
evidence: PRIMARY full text held at research/sources/bautin-1952-full.pdf.full.md (mathnet full-text PDF, Russian); summary research/summaries/bautin-1952-full.pdf.md; western-form confirmation in Coppel 1966 survey §3 (research/summaries/coppel-1966-survey-quadratic-systems.md).
falsifier: a quadratic system with 4 small-amplitude cycles from a single focus. None known; M(2)=3 is the standard accepted boundary.
sources: https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&paperid=5421&what=fullt&option_lang=eng
anchor: research/sources/bautin-1952-full.pdf.full.md
note: The run's own kernel-checked results (L8 ∉ ⟨L4,L6⟩, BautinRecurrence identities) are memberships in the Bautin ideal of the canonical chart — they must NOT be quoted as M(2)=3 evidence either way; M(2)=3 itself is a Cited axiom in code/lean/Lib/Bautin.lean, not kernel-proved. The M(2)=3 statement is the calibration target for the Bautin oracle (code/bautin/lyapunov_quadratic.py), not yet machine-reproduced.
follows-from:
answers:
```
