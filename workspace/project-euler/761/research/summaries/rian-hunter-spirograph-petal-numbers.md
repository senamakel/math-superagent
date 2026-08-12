# Rian Hunter — "The Number Hiding Inside the Spirograph, Part 2" (thelig.ht blog, cited by OEIS A328227)

Source: https://thelig.ht/petalnumbers/part2.html . Full text: `research/sources/rian-hunter-spirograph-petal-numbers.full.md`.

## What the source establishes

This is a recreational-math blog post (Rian Hunter) about "petal numbers" from a spirograph construction. Its relevance to this run is narrowly but genuinely that it **independently rediscovers the exact circle critical-speed identity and ties it to the OEIS catalogue entry**:

- The author's spirograph construction yields a constant p ≈ 4.6033388487... as b→∞ (the petal-tangency limit).
- A Reddit search (existentialpenguin) identified the OEIS entry A328227 — the constant defined as the solution of **(arccos(1/p) + π)² + 1 = p²** — which is **exactly the PE 761 circle identity** (V_circle ≈ 4.60333885). The post then derives that same equation from the spirograph, proving the two numbers coincide (with help from a BruhcamoleNibberDick sketch).
- It proves p is transcendental (so V_circle is not a simple algebraic closed form), and gives an efficient numerical method.
- Addendum computes the fixed points of tan x — the same object as A115365 (the smallest positive root of tan x = x, x ≈ 4.493409458, from which V_circle = √(1+x²)).

## Why it matters for this run

- **Confirms V_circle = 4.60333885 is catalogued as OEIS A328227** and is the key to the circle anchor and the n→∞ limit of the polygon formula.
- Gives a second, independent confirmation of the identity **V² = 1 + (π + arccos(1/V))²** (equivalently tan B = π + B with B = arccos(1/V)), matching the Ponder-This / Hesterberg / Lady-in-the-Lake derivations already held. It establishes these are all the same constant.
- Note the author's "4.60" spirograph constant ≠ the straight-dash π+1 red herring — it lands on the true staging-dash value, reinforcing which mechanism is correct.

**Caveats:** it is a blog, not a peer-reviewed source, and it concerns the circle only — no polygon/hexagon value. Its value is as the documented cross-reference behind OEIS A328227 and as corroboration of the circle constant's identity, not as a route to V_hexagon.

```claim
id: spirograph-circle-constant-a328227
statement: The constant p ≈ 4.60333884875 (the PE 761 circle critical speed V_circle) is the solution of (arccos(1/p)+pi)^2 + 1 = p^2, equivalently p = sqrt(1+x^2) with x the smallest positive root of tan x = x (OEIS A115365); it is catalogued as OEIS A328227 and equals 1/A213053. p is transcendental, so V_circle has no algebraic closed form.
hypotheses: unit circle escape game (circle pool, swimmer at center, runner on boundary); the identity p^2 = 1 + (pi + arccos(1/p))^2 is exactly the two-phase staging-dash critical condition cos B = 1/p, sin B = (pi+B)/p.
holds-here: yes for the circle anchor - reproduces V_circle = 4.60333885 and confirms it is the n->infinity limit of the regular-n-gon formula.
status: sourced (OEIS A328227 catalogue record + this blog's rediscovery and transcendence proof); blog is not peer-reviewed but the catalogue entry is authoritative.
bearing: encyclopedic corroboration that V_circle is catalogued and transcendental; cross-reference for all circle treatments; no hexagon value.
anchor: research/sources/rian-hunter-spirograph-petal-numbers.full.md
```

## What it does not settle
- No polygon/hexagon value (circle only).
- Blog provenance; used only as corroboration, not as the primary derivation of the formula.
