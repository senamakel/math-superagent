# Bollobás, Leader, Walters — "Lion and Man — Can Both Win?"

Source: arXiv:0909.2524 ([abs](https://arxiv.org/abs/0909.2524)),
[DOI 10.48550/arXiv.0909.2524](https://doi.org/10.48550/arXiv.0909.2524); published Israel
J. Math. 189 (2012) 267–286. Full text: `research/sources/bollobas-leader-walters-lion-man-both-win.full.md`.

## What it establishes

The paper treats continuous-time pursuit-evasion ("lion and man") in a general metric space
with *equal* speeds, and asks a delicate question: is it exactly one of the lion and the man
who has a winning strategy?

**Main results**
- In any *compact* metric space, at least one player has a winning strategy.
- Surprisingly, there are (compact) metric spaces in which **both** the lion and the man
  have winning strategies.
- There is also a metric space in which, for **two lions vs one man**, neither player has a
  winning strategy.
- Connections to fixed-point properties and open problems.

## Why it matters for this run

This is precisely the sort of "pathological" pursuit–evasion model that the Abel et al.
"Escaping a Polygon" paper explicitly **avoids** by restricting to **locally rectifiable
regions**, where the pursuit–escape game has a **unique critical speed ratio r\*** and a
unique winner. In other words: the value-bifurcation pathologies in this paper are
circumvented in the setting PE 761 lives in (a pool, hence locally rectifiable). It
therefore *frames* why the Abel et al. well-posedness theorem (the gearbox behind the
stewbasic n-gon formula) is needed and what it rules out.

It also gives the classic historical bibliography of the lion-and-man lineage it inherits:
Rado (1930s), Besicovitch (1952 escape in the disk), Littlewood (1953 proof), Croft
(1964, "Lion and Man: a Postscript", where bounded-curvature paths allow lion capture and
n lions catch a man in the n-ball while the man escapes n−1 lions), Sgall (2001, David
Gale's discrete-time quadrant problem), and the differential-games books of Isaacs (1965)
and Lewin.

## What it does NOT settle
- No critical *speed-ratio* thresholds for escape (it studies equal speeds).
- No polygon / pool critical speeds. The hexagon value is not here.
- The disk escape here is the *unequal-information* equal-speed lion-and-man, not the
  swimmer-runner speed-ratio game of PE 761.

## Claims

```claim
id: lion-man-metric-space-both-win
statement: In continuous-time pursuit–evasion in a compact metric space at least one player has a winning strategy, and there exist compact metric spaces in which both the lion and the man can have winning strategies, and a space in which 2 lions vs 1 man gives no winner either way.
hypotheses: continuous-time, equal top speeds, general metric space.
holds-here: no — PE 761's pool is locally rectifiable, where Abel et al. prove a unique critical speed ratio and winner; the pathologies this paper exhibits are exactly why the locally-rectifiable (pool) restriction matters.
status: proved (published paper).
bearing: explains the well-posedness assumption behind the Abel et al. model that the stewbasic n-gon formula and the hexagon answer rest on; provides the canonical lion-and-man bibliography (Rado/Besicovitch/Littlewood/Croft/Sgall/Isaacs/Lewin).
anchor: research/sources/bollobas-leader-walters-lion-man-both-win.full.md
```
