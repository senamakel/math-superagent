# Direct OEIS search — full 15-term amoeba sequence

Source: https://oeis.org/search?q=1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267,5949063&fmt=text (converted plain text)

## What it establishes

The direct OEIS search for the full 15-term sequence returns exactly
**"No results."** The full text is a single boilerplate reply; there are
no entries, no A-number, no formulae. This is an authoritative negative:
the sequence as computed is not in the OEIS.

## Bearing on D(N)

- No closed form, recurrence, or further terms can be looked up for D(N)
  from OEIS.
- The run's own BFS/DP route is the only route to D(10000); there is no
  catalogued structural shortcut to find.
- Negative finding worth retaining so nobody re-queries these exact terms.

```claim
id: dN-not-in-oeis
statement: The 15-term amoeba sequence D(0..14)=1,1,3,9,30,...,5949063 returns "No results" from a direct OEIS search; it is not catalogued.
hypotheses: the 15 terms as BFS-verified to N=14
holds-here: yes
status: asserted (OEIS search result, a machine query not a theorem)
bearing: closes the lookup route; D(10000) must come from structure the run derives itself
anchor: research/L1.0/oeis_direct.md
```
