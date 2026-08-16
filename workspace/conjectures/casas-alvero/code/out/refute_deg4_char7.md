# Refutation: CA degree 4 is false over F_7 (p=7 a bad prime for n=4)

`find_counterexample` on `code/refute/ca_deg4_char7.p` returned
**CounterSatisfiable** (SZS status), a genuine finite-model counterexample.

## Witness, hand-checked

f = x^4 + x^3 + 4x over F_7, with Hasse derivatives H_1, H_2, H_3:

| | value table on c0..c6 (=0..6) |
| --- | --- |
| f  | [0, 6, 4, 1, 0, 0, 3]  (roots: 0, 5, 6) |
| H_1 = 4x^3+3x^2+4 | [4, 4, 6, 6, 0, 5, 3] |
| H_2 = 6x^2+3x | [0, 2, 2, 0, 3, 4, 3] |
| H_3 = 4x+1 | [1, 5, 2, 6, 3, 0, 4] |

Common roots:
- H_1 and f share root 5: H_1(5)=4·125+3·25+4=579=82·7+5... check: 4·125=500, 3·25=75, +4 = 579. 579 mod 7 = 579−82·7=579−574=5. Hmm, wait. Let me recompute.

Recompute H_1(5): 4·5³ + 3·5² + 4 = 4·125 + 3·25 + 4 = 500+75+4 = 579. 579 mod 7: 7·82=574, rem 5. That's 5, not 0!

But the model says h1(c4)=c0=0 where c4 is the element with value... wait, c4='$i_5'. f('$i_5')='$i_1'=c0 (value 0), and h1('$i_5')='$i_1'=c0 (value 0). So common root is at the element whose value-label... 

Hold on — I need to be careful about which F_7 element 'fmb_$i_5' IS. The names c0..c6 are just aliases for the 7 domain elements. In my encoding, c0=0, c1=1, ..., c6=6 as *axiom labels* only — I asserted their distinctness, and the value tables literally say f(c4)=c0. The engine didn't know c4 "means" 4. The value table is just a function assignment.

So the actual witness polynomial is determined by which x in F_7 has f(x)=0 etc. My hand-check fixed c_k = k. The engine's model is the same abstract structure: there are 7 labels, f has the value pattern [0,6,4,1,0,0,3], H_1=[4,4,6,6,0,5,3], etc. The model satisfies hyp1 (∃: f=0 & H_1=0), hyp2, hyp3, and falsifies the pure-power goal.

The relevant check is whether this value-table structure corresponds to a real polynomial over F_7. But actually — my hand computation already confirmed it does NOT correspond: I computed H_1(5)=5, not 0, for f=x^4+x^3+4x. So my claimed witness polynomial was WRONG in the H_1 table.

So the value table in the .p file does NOT match any real polynomial for f=x^4+x^3+4x. Let me recheck what polynomial gives f=[0,6,4,1,0,0,3] and H_1=[4,4,6,6,0,5,3].

## Recheck whether the encoded tables correspond to a real polynomial

Let me reconsider. I need to determine what set of polynomials over F_7 realize the encoded function tables. Let me recompute the Hasse derivatives of f=x^4+x^3+4x properly.

f = x^4 + x^3 + 4x.
- H_1 = (1/1!) f' = 4x^3 + 3x^2 + 4.  [Hasse H_1 = ordinary first derivative]
- H_2 = (1/2!) f'' = (12x^2+6x)/2 = 6x^2 + 3x.
- H_3 = (1/6) f''' = (24x+6)/6 = 4x + 1.

H_3 = 4x+1. Roots: 4x+1=0 → x = -1·4^{-1} = -1·2 = -2 = 5 mod 7. H_3(5)=0. f(5)=5^4+5^3+4·5 = 625+125+20 = 770. 770 mod 7 = 0 (7·110). So common root 5 for H_3. ✓ [h3 table: h3(c5)=c0? h3='$i_6'... in my table h3=[1,5,2,6,3,0,4] indexed c0..c6 so h3@c5=0. And f@c5=0. ✓ In labels: c5 maps to value-5 element. So common root "5" ✓.]

H_2 = 6x^2+3x = 3x(2x+1). Roots x=0, 2x+1=0→x=-1·2^{-1}... 2^{-1} mod 7 = 4, so x=-4=3. Roots 0 and 3. f(0)=0, so common root 0 ✓. [h2 table [0,2,2,0,3,4,3]: h2@0=0, f@0=0 ✓.]

H_1 = 4x^3+3x^2+4. Does it have a root shared with f? Let me just compute the value table of H_1 for x=0..6:
- H_1(0)=4
- H_1(1)=4+3+4=11=4
- H_1(2)=4·8+3·4+4=32+12+4=48=6
- H_1(3)=4·27+3·9+4=108+27+4=139=139−19·7=139−133=6
- H_1(4)=4·64+3·16+4=256+48+4=308=0  → H_1(4)=0
- H_1(5)=4·125+3·25+4=500+75+4=579=5
- H_1(6)=4·216+3·36+4=864+108+4=976=976−139·7=976−973=3

So H_1 table = [4,4,6,6,0,5,3] — this matches the encoded table! And f(4)=4^4+4^3+16=256+64+16=336=0. So H_1 and f share root 4 (H_1(4)=0, f(4)=0). ✓ [in labels h1@c4=0 and f@c4=0 ✓]

I made an arithmetic slip earlier ("H_1(5)") but the encoded table is correct: H_1(4)=0 and f(4)=0. The table [4,4,6,6,0,5,3] is exactly right.

f table: f(0)=0, f(1)=1+1+4=6, f(2)=16+8+8=32=4, f(3)=81+27+12=120=1, f(4)=336=0, f(5)=770=0, f(6)=1296+216+24=1536=? 1536−219·7=1536−1533=3. So f=[0,6,4,1,0,0,3]. ✓

Roots of f: 0, 4, 5. Three distinct roots → not a pure power.

So the real witness: f=x^4+x^3+4x over F_7, common roots:
- H_1 & f at 4
- H_2 & f at 0
- H_3 & f at 5
Three roots {0,4,5}, not a pure power. Counterexample. 

The model and my polynomial agree on all four tables. (My comment in the .p file said "root 4 for H1" — correct; and "hyp1 common root 4". The engine model shows f(5)=0 & h1(5)=0 where 5 here is the *element name* c5, whose value is... wait.)

Careful with label-vs-value again. In the .p, hyp1 = ∃X: f(X)=c0 & h1(X)=c0. In the model, the satisfying X is 'fmb_$i_5' = c4. f(c4)=c0 (0) and h1(c4)=c0 (0). Now which F_7 value is c4? In my polynomial encoding c4↔value 4, and f(4)=0, H_1(4)=0. ✓ Perfect match.

Everything checks. The counterexample is genuine and hand-verified.

## Status

The conjecture (CA degree 4 over F_7: f is a pure power) is falsified by
f = x^4 + x^3 + 4x over F_7. This is the third published bad prime for n=4
({3,5,7}), a refutation at a prime the run's refute folder had not covered
(previously only n=4 char 3 and char 5), and independently corroborates the
verified claim `badprimes-n4-minor-criterion-verified` (lcm_T J_T = 1575
= 3^2·5^2·7, so 7 | J_T ⇒ p=7 bad for n=4).

```claim
id: deg4-char7-refuted
status: checked — find_counterexample on code/refute/ca_deg4_char7.p returned
  CounterSatisfiable; model decoded to f = x^4 + x^3 + 4x over F_7 and
  re-verified by hand (value tables H_1=[4,4,6,6,0,5,3], H_2=[0,2,2,0,3,4,3],
  H_3=[1,5,2,6,3,0,4]; common roots 4, 0, 5; f has roots {0,4,5}, three
  distinct, so not a pure power).
holds-here: yes
statement: CA in degree 4 over F_7 (Hasse formulation) is false: f = x^4 +
  x^3 + 4x over F_7 shares a root with each Hasse derivative H_1, H_2, H_3
  (H_1(4)=f(4)=0, H_2(0)=f(0)=0, H_3(5)=f(5)=0) yet is NOT a pure power
  (roots {0,4,5}). Hence p=7 is a bad prime for n=4.
hypotheses: Hasse-derivative formulation of CA (the char-p convention the
  published bad-prime lists use); monic degree-4 f over F_7
evidence: checked — the TPTP finite-model counterexample was decoded and
  hand-recomputed in full (exact mod-7 arithmetic); all four value tables
  agree between the model and the polynomial f.
program: code/refute/ca_deg4_char7.p (+ find_counterexample)
capture: code/out/refute_deg4_char7.txt
anchor: research/sources/castryck2012_degree12_html.full.md (Thm 4)
falsifies: CA degree 4 over F_7 holding (i.e. every such f being a pure power)
```
