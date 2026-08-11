# Shared context

What the run's reference library establishes, in the words of the run rather
than of the sources. The research team writes this; everyone reads it.

It exists because `research/INDEX.md` answers a different question. The index
says what each file *is* — one row per source, so reading it means holding
thirteen descriptions in your head and doing the synthesis yourself, every
time, in every role. This file says what the library *means for this problem*:
the definitions and results now available, what they let the run compute or
rule out, and where two sources disagree.

Keep it short enough to read on every turn — a few hundred words. It is not a
summary of the sources; it is the standing brief that a new attempt, a new
approach, or a fresh judgement can act on without opening anything.

## Established

- The spacings of the order statistics of n i.i.d. Exp(1) variables are
  **independent** exponentials: X_(1) ~ Exp(n) and X_(i)−X_(i−1) ~ Exp(n+1−i).
  Equivalently, after the smallest of a set of independent exponentials fires,
  the survivors stay independent exponentials with their original rates
  (memoryless "clocks" view). Source:
  `research/exponential_order_statistics_memoryless_kth.md` (KTH course notes,
  Timo Koski, SF2955; theorem with full Jacobian proof). This is exactly the
  structure memory.md flagged as the likely key to an exact (non-MC,
  non-enumerative) integration over the iid Exp(1) boat speeds in PE 597: it
  lets the bump/finish chronology decompose into products over independent
  exponential rates rather than high-dimensional integrals over the speeds.

## Contradictions

None. The source agrees with the run's working model (speeds iid Exp(1),
memoryless property).

## Gaps

The library holds the exponential order-statistics theory, but no source yet
derives the specific event-chronology decomposition (bump-chain parity
integral) for this race; that is the run's own derivation task, not a
literature lookup.
