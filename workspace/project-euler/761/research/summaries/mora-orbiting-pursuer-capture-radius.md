# Mora, Von Moll, Weintraub, Casbeer, Chakravarthy — "Escape from an Orbiting Pursuer with a Nonzero Capture Radius" (arXiv:2310.01203)

Source: https://arxiv.org/abs/2310.01203 (math.OC, submitted 2 Oct 2023).
Full text: `research/sources/mora-orbiting-pursuer-capture-radius.full.md` → [[mora-orbiting-pursuer-capture-radius.full]]

## What the source establishes

The downloaded full text is **only the arXiv landing page**: it contains the
title, authors, and abstract, but not the paper body. So the only substantive
content available here is the abstract:

> Multi-agent containment: a fast evader (constant speed, constant heading)
> tries to escape a circular containment region orbited by a slower pursuer
> with a nonzero capture radius; the pursuer is constrained to move along the
> edge of the region and seeks to capture the evader. The paper gives multiple
> capture conditions for the single-pursuer case (defining the worst-case
> initial pursuer position), a parametric study of speed ratio / capture
> radius / evader initial location, and a reachability analysis of viable
> escape headings and reachable regions.

## Why it matters for this run

Structurally this is the same *boundary-constrained-pursuer vs interior-evader*
family as PE 761 (and sits beside Shishika–Kumar and Von Moll–Pachter in the
differential-games corner of the library). It is relevant as:
- **Canon-adjacent corroboration** that the perimeter-constrained-pursuer /
  interior-evader game with a speed-ratio threshold is an actively studied,
  legitimate formulation (same defence-as-before mechanism).
- It concerns a **circular** containment region and a *nonzero capture radius*,
  a fast evader, and asks reachability questions — not the regular-n-gon
  critical *speed ratio* with a speed-1 swimmer. It contributes no numeric
  value and no polygon/hexagon result.

%% == NOTE == %%
Because the downloaded text is only the abstract, nothing in the body can be
quoted or relied on. This source does **not** add a usable claim for this run.
If a substantive version is wanted, the actual PDF/HTML body must be fetched —
the landing page does not provide it.

```claim
id: mora-orbiting-pursuer-abstract-only
statement: arXiv:2310.01203 (Escape from an Orbiting Pursuer with a Nonzero Capture Radius) studies a fast constant-heading evader escaping a circular containment region orbited by a slower boundary-constrained pursuer with a nonzero capture radius, giving single-pursuer capture conditions, a speed-ratio/capture-radius/initial-location parametric study, and a reachability analysis of escape headings. The run's downloaded copy is the abstract landing page only (no paper body), so no further claim can be extracted.
hypotheses: circular containment, pursuer constrained to the boundary, evader faster, nonzero capture radius, reachability objectives.
holds-here: no usable claim — the game is circle + fast-evader + capture-radius, not the regular-n-gon speed-1-swimmer critical-ratio game; and the body is absent from the held copy.
status: asserted (abstract only; not executable from what is held).
bearing: the held copy contributes nothing usable; flags that this differential-game branch (Von Moll/Weintraub/Casbeer/Mora) is tangential background, not a route to V_hexagon.
anchor: research/sources/mora-orbiting-pursuer-capture-radius.full.md
```
