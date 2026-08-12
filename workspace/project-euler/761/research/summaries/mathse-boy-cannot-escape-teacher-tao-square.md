# Math.SE q.1555855 — "Prove that the boy cannot escape the teacher" (Tao square-pool, 6x)

Source: https://math.stackexchange.com/questions/1555855 (via Wayback, 2023 snapshot).
Full text: `research/sources/mathse-boy-cannot-escape-teacher-tao-square.full.md`.

## Setup (adjacent problem — the square-pool ancestry of PE 761)

- **Tao, *Solving Mathematical Problems*, ch. 5 (Analytic Geometry), Problem 5.4 (p. 79).**
  In the centre of a **square** swimming pool is a boy; his teacher (who cannot swim) is at
  one **corner**. Teacher runs **3×** the boy's swim speed. Boy can run faster than teacher
  on land. Can the boy escape? (Answer: yes — solved affirmatively in the text, attributed
  to Taylor 1989, p. 34, Q2.)
- **Follow-up (this thread):** with the teacher running **6×** as fast, show the boy
  **cannot** escape. Hint: draw an imaginary **inner square of side 1/6** centred at O; once
  the boy leaves it, the teacher gains the upper hand.

## What the thread establishes

The accepted solution analyzes the boy's possible exits (bottom side, a side, top side)
from the inner square of side 1/6 and shows each is intercepted by the teacher running at
6× speed along the boundary. Key structural idea:

- While the boy stays inside the inner square, the teacher can position so that any later
  exit is covered; the critical quantity is the comparison between the time for the boy to
  reach a boundary exit and the time for the teacher to run along the square's *perimeter*
  to that same exit point.
- This is the **same boundary-time equalization principle** that governs PE 761's critical
  speed: the swimmer's straight-line escape time to a boundary point vs the runner's
  perimeter travel time to that point; the "inner square" is exactly a homothetic scaled
  safe region.

The thread is also a good *negative control*: at speed ratio **6 > V_square ≈ 5.7886** the
teacher wins — consistent with the square critical speed from the run's stewbasic/David K
formula (a 6× teacher beats the square's threshold).

## Why it matters for this run

- Directly cited by the run's own CANON source (stewbasic's n-gon thread links to it):
  fixing the ancestry: Tao's square-pool problem → general n-gon (Math.SE 1762665) →
  PE 761.
- Demonstrates the "homothetic scaled safe region" idea (inner square of side 1/6) that the
  run identifies as the general mechanism (safe region = pool scaled v× smaller).
- Provides a **numeric sanity anchor**: 6 > 5.7886 ⇒ capture, matching V_square.

## What it does NOT settle

- Not an exact critical-speed derivation for the square (does not compute 5.78859314; it
  only proves 6× suffices to catch and 3× fails to).
- No hexagon content; the hexagon critical speed is not addressed anywhere in this thread.

## Claims

```claim
id: tao-square-pool-6x-capture
statement: In the square pool with the boy at the centre and teacher at a corner, a 6x speed teacher can prevent escape using an inner-square argument; the same setup with a 3x teacher admits escape. The inner square of side 1/6 is a homothetic scaled safe region, and the escape/interception decision is the boundary-time equalization.
hypotheses: square pool; boy at centre, teacher at corner constrained to boundary; speed ratios 3x (escape) and 6x (capture); instantaneous manoeuvres.
holds-here: yes as the square-pool ancestry and mechanism validation — consistent with V_square ≈ 5.7886 (6 > V_square ⇒ capture; 3 < V_square ⇒ escape), the same boundary-time mechanism PE 761 uses.
status: asserted (Math.SE problem solution; original problem from Tao's book, itself from Taylor 1989).
bearing: fixes the problem family's ancestry, validates the homothetic scaled safe-region mechanism and the boundary-time equalization principle behind the n-gon formula.
anchor: research/sources/mathse-boy-cannot-escape-teacher-tao-square.full.md
```