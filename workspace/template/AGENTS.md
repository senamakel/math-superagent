# Workspace instructions

## Method

- Read the complete problem before calculating. Restate it in your own words.
- State assumptions and define notation.
- Work the small cases and the worked example by hand first. They are the
  test oracle for everything that follows.
- Identify the mathematical objects involved and the classical theory that
  governs them before writing any full-size program.
- State the result the method rests on, why it applies, and what it reduces
  the work to, before implementing it.
- Do not search the answer space. Enumerating candidates or every object up to
  the stated bound until one matches is prohibited even when it terminates. If
  the cost grows with the bound in the statement, it is the wrong method.
- Find the answer by theory, not by exhaustion. The bound in the statement is
  chosen to defeat enumeration, so a method that scales with it is not slow,
  it is wrong. The intended solution is a structural fact — a recurrence, a
  bijection, a closed form, a symmetry, a classification — that makes most of
  the search space unnecessary to visit. Look for that fact before writing
  anything at full size, and write down which one you are relying on.
- Use brute force only on small instances, and only to test a conjecture or to
  validate the real method. Say when output is such a check.
- Attack your own method before trusting it. State what would have to be true
  for it to be wrong, then go looking for that case: the smallest input that
  breaks it, a boundary the derivation assumed away, a hypothesis of the
  theorem you have not checked holds here. A conjecture that has survived a
  deliberate attempt to break it is worth far more than one that has only ever
  been confirmed.
- Search for a counterexample as seriously as for a proof. If a few minutes of
  looking finds none, say what you searched and how far, because that bounds
  what the evidence supports.
- Find out how this problem has been attacked before. Name the standard
  approaches to problems of this shape, and say why the one you chose beats
  the others here. If a natural-looking approach fails, record why it fails —
  a known dead end is a result, and it stops the next attempt walking into it.
- State time and space complexity before running substantial code.
- Never use an algorithm with exponential time or space complexity.

## Evidence

- Assume your own recall is unreliable. Every number comes from a program you
  ran; every theorem comes from a source you can cite. If you can point to
  neither, say you do not know rather than filling the gap.

- Keep sourced facts separate from deductions.
- Save source URLs beside the claims they support.
- Verify a result by a second, independent route, or say it is unverified.
- Do not describe numerical evidence as proof.

## Housekeeping

- Put generated files under this workspace only.
- Externally sourced material lives in `research/`; the run's own derivations
  and programs do not.
- Record the objective and its completion criteria in `goal.md`.
- Keep provisional work in `scratchpad.md` and promote durable results to
  `memory.md`, including failed approaches and open questions.
- Never write credentials or environment values to workspace files.
- `trace.jsonl` is the runtime's own event log, and the tools refuse it. It is
  a verbatim replay of what you have already seen, so reading it would spend a
  large part of your context to learn nothing. Operators read it outside the
  run.
- Build reusable helpers in `toolkit.py` instead of rewriting the same routine
  in each script, and describe every one of them in `toolkit.md`.
