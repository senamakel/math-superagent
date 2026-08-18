# Hilbert's 15th problem — Schubert calculus made rigorous, and what is left

## The original question, and its answer

> Establish rigorously, and with precise determination of the limits of their
> validity, the enumerative results of Schubert's calculus.

Schubert's *Kalkül der abzählenden Geometrie* (1879) computed numbers like *the
2 875 lines on a general quintic threefold* and *the 3 264 conics tangent to
five general conics* by a "principle of conservation of number" that had no
proof. Intersection theory — van der Waerden, Chevalley, Grothendieck, Fulton,
and Fulton–MacPherson's excess intersection formula — supplied the foundation,
so the *foundational* question is answered and is **not** this workspace's
target.

What Hilbert also asked for — **the precise determination of the limits of
validity** — is where the open questions are, and they are unusually concrete.

## The targets

### T1. Enumerative reality

Schubert's numbers count solutions over `C`. Over `R` the count varies, and the
question of *which* counts occur is largely open.

Recalled status — **to be confirmed or struck against sources**:

- **Shapiro–Shapiro conjecture**: for Schubert problems in a Grassmannian given
  by flags osculating the rational normal curve, all solutions are real. Proved
  by **Mukhin–Tarasov–Varchenko** (2009), by a route through the Bethe ansatz
  and the Gaudin model — one of the striking theorems of the subject.
- The **monotone conjecture**, the **secant conjecture** and their relatives —
  generalisations of Shapiro–Shapiro to flag varieties and to secant rather than
  osculating flags — are the subject of large computational experiments
  (Sottile and collaborators) and are **open** in general.
- **Which numbers of real solutions occur** for a given Schubert problem — the
  set of achievable real counts — is open for all but small cases.

### T2. Galois groups of Schubert problems

Every enumerative problem has a **Galois group**, acting on its solutions
(Jordan; revived by Harris and by Vakil). It is a subgroup of the full symmetric
group on the solutions, and it measures how much the solutions can be told
apart. Recalled: Vakil gave a criterion forcing "at least alternating"; Leykin,
Sottile, Brooks, White and others computed Galois groups of many Schubert
problems numerically; the general question — **which Schubert problems have
Galois group smaller than the full symmetric group** — is open, and each
individual problem with an unexpectedly small group is a discovery.

### T3. Limits of validity

Schubert's conservation-of-number arguments fail in specific, describable ways.
Which classical computations are actually *correct as stated*, which need excess
intersection, and which are wrong, is not fully catalogued. A verified audit of
a family of classical numbers is a real contribution.

## The cheap tests every candidate must pass first

1. **The transversality test.** Every enumerative count presumes the
   intersection is transverse for general flags. In positive characteristic and
   in special position it need not be, and an argument that never checks
   transversality has counted the wrong thing. Say where genericity was used.
2. **The complex-count test.** Any claimed real count must be at most the
   complex count, and congruent to it in the ways the topology forces (parity
   constraints from the real structure). A claimed real count violating either
   is an error in the solver, located immediately.
3. **The certification test.** Numerical algebraic geometry produces
   approximate solutions. A solution count is only a count once each solution
   is *certified* — an alpha-theory certificate, an interval Newton step, or an
   exact rational witness — and once distinct approximate solutions are
   certified to be distinct. Two numerically close roots that are actually one
   root break every count in this subject.

## What is genuinely unknown

- The monotone and secant conjectures, and the reality of Schubert problems for
  flag varieties beyond the settled Grassmannian case.
- Which sets of real solution counts occur for named Schubert problems.
- Which Schubert problems have Galois group a proper subgroup of the symmetric
  group; the classification is open even for small Grassmannians.
- Whether the Galois group of a Schubert problem is always at least alternating
  in cases Vakil's criterion does not reach.
- A complete audit of the classical Schubert numbers against modern intersection
  theory.
- Enumerative geometry over `R` for tangency problems (3 264 conics: how many
  can be real? — recalled as fully answerable and answered, so confirm it, and
  take the next family up).

## What counts as a result

In descending order of value.

1. A **proof** for a named case of the monotone or secant conjecture, or a
   counterexample — the counterexample being a certified real solution count
   that the conjecture forbids.
2. A Schubert problem whose Galois group is proved to be a proper subgroup, with
   the group identified and the proof not merely numerical — a certified
   monodromy computation plus a structural reason.
3. An exhaustive, certified table of real solution counts for a family of
   Schubert problems, with the certification method stated and the search
   bounded — this is what the conjectures above are tested against, and the
   existing tables are large but not exhaustive.
4. A verified audit of a set of classical Schubert numbers: recomputed by
   modern intersection theory, with each classical claim confirmed, corrected,
   or flagged as needing excess intersection.
5. An exact (non-numerical) solution of a Schubert problem the literature solves
   only numerically, via Gröbner bases over `Q`, with the ideal reported.
6. A refutation of a published claim or a folklore expectation, with a witness.

**Do not report an uncertified numerical count as a solution count.** Two
solutions that a solver could not separate are one solution until a certificate
says otherwise.
