# Torpids and Bumps race — Wikipedia statement tier — summary

- Source 1: Wikipedia "Torpids". URL: https://en.wikipedia.org/wiki/Torpids (full text: research/sources/torpids_wikipedia.full.md)
- Source 2: Wikipedia "Bumps race". URL: https://en.wikipedia.org/wiki/Bumps_race (full text: research/sources/bumps_race_wikipedia.full.md)
- Content: the real Oxford Torpids: annual bumping races on the Isis (Thames) at Oxford, one of two bumping-race series (the other is Summer Eights). Boats start in order at ~1.5-boat-length gaps, coxes holding bung lines; start by cannon. A crew bumps the boat in front by making physical contact (or, under some rules, by overtaking); the bumper then takes no further part, the bumped crew continues racing and may be bumped again (Torpids variant). Today's ordering of bumps among a division, the chain rule (A above B iff A bumped B directly or via an intermediate chain), and the "bumped boat continues, bumper out" rule are the exact real-world behavior the PE597 abstraction models. Bumps race covers the general format: divisions, "rowing over", blades/spoons/spades, overbumps, sandwich boats.
- Bearing on PE597: fixes the statement and the real-world rules; confirms the problem's abstraction (transitive bump chain ⇒ placed higher; bumped boat continues; bumper retired) agrees with the source description of Torpids, justifying the model's structural claims (bump graph is a forest with out-degree ≤ 1, edges strictly index-increasing).
- Restriction: descriptive/historical; no mathematics of speeds or probabilities.

```claim
id: torpids-real-world-rules
statement: In Torpids (Oxford bumping races) a pursuing boat that bumps is retired from the race, the bumped boat continues and may be bumped again, and a boat's final gain is measured by the chain of bumps it caused (directly or indirectly).
hypotheses: real-world rules as described by the tournament sources.
holds-here: the PE597 abstraction matches this description (bumper out/transparent, bumped continues, transitive chain defines the new order).
status: verified-against-source (Wikipedia Torpids + Bumps race in library)
bearing: sanctions the model's bump-graph-forest structure and the new-order rule.
anchor: research/sources/torpids_wikipedia.full.md, research/sources/bumps_race_wikipedia.full.md
```