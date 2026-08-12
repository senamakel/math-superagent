# Abundancy outlaws of the form (σ(N)+t)/N — Holdener & Stanton, JIS 2007

Source: https://cs.uwaterloo.ca/journals/JIS/VOL10/Holdener/holdener7.pdf — `[[holdener_stanton_outlaws.full]]`

## What it establishes (useful here)

- **Abundancy index** I(n) = σ(n)/n; **abundancy outlaw** = rational > 1 not in the image of I.
- **Property 2.2.** If I(n) = r/s in lowest terms then **s | n**. This is the key leverage for PE 241: p(n) = k+1/2 = (2k+1)/2 with gcd(2k+1,2)=1, so **2 | n** — every hemiperfect is even. Independent of the parity argument in the A159907 note; two routes to the same fact.
- **Erdős-type Property 2.3.** If m < k < σ(m) and gcd(k,m)=1 then k/m is an outlaw. This is *not* a PE 241 tool: PE 241's k+1/2 are *indices*, not outlaws.
- Theorems 3.2/4.2 and Corollaries 5.2–5.7: if (σ(N)+t)/N is in lowest terms and certain divisor conditions hold, it is an outlaw. These are about showing a candidate rational is *not* any abundancy — the opposite direction from the run's need, which is identifying which n *satisfy* k+1/2.

## What it lets this run do

Property 2.2 gives a **proof-grade** derivation of evenness for candidates (s=2|n), confirming the parity half of the 2-adic reduction, and is the cleanest theoretical justification for starting the candidate DFS from an even 2-adic part. Nothing in the paper bears on the step of the method beyond that: it classifies rationals that FAIL to be abundancies, whereas we need the ones that succeed.

## Does not help (why)

The outlaw constructions are the "are these rationals ruled out" direction; the run needs "which n give these rationals". They do not bound or enumerate solutions. So most of the paper is not operative for PE 241; Property 2.2 is the transferable piece.

```claim
id: property22-denominator-divides
statement: If I(n)=sigma(n)/n = r/s in lowest terms, then s | n (gcd(r,s)=1 implies s|n since s | n and gcd(k,m)=1).
hypotheses: n>=2, r/s in lowest terms
holds-here: yes (r=2k+1 odd, s=2)
status: proved
bearing: proves every candidate is even; sets the 2-adic base of the DFS
anchor: research/sources/holdener_stanton_outlaws.full.md
```
