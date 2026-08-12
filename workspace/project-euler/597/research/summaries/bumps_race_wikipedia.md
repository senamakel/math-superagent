# Bumps race — Wikipedia — summary

- Source: Wikipedia "Bumps race". URL: https://en.wikipedia.org/wiki/Bumps_race (full text: research/sources/bumps_race_wikipedia.full.md)
- Content: the general format of bumping races (Oxford Torpids/Summer Eights, Cambridge May/Lent Bumps): crews line up single-file at set gaps along the bank, start by cannon, each crew tries to bump the boat ahead (physical contact, in some rules an overtake) before being bumped from behind; the bumper retires to the side, the bumped crew continues and may be bumped again; the day's finishing order sets the next day's starting order; divisions, "rowing over", overbumps, sandwich boats, blades/spoons/spades awards. Includes the crucial rule for a single race: a bump is a chain — crew A passes ahead of B if A bumped B or bumped someone who (directly or transitively) bumped B.
- Bearing on PE597: statement tier; confirms the abstraction in the problem statement matches the real rule (bumper out, bumped continues, transitive bump chain places the bumper higher). The PE597 model is a single-race speed-based idealization; the bump-chain order rule is exactly the real one.
- Restriction: descriptive/historical; no probability model.

```claim
id: torpids-real-world-rules
statement: In bumping races (Torpids among them), a boat that bumps retires immediately, the bumped boat continues and can be bumped again, and a boat's gain is by the transitive chain of bumps it caused; final position = chain-reachability order.
hypotheses: real rules as described by the tournament sources.
holds-here: the PE597 abstraction matches this description.
status: verified-against-source (Wikipedia Bumps race + Torpids in library)
bearing: sanctions the bump-graph-forest structure and new-order rule of the model.
anchor: research/sources/bumps_race_wikipedia.full.md
```