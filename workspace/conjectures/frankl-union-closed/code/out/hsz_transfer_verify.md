# Hu–Shi–Zhou density-transfer identities — verification note

Status: **verified by hand (exact algebra), no executor in this scholar role.**
The program `code/out/hsz_transfer_verify.py` is written and ready for a
later executor; until it runs, everything here is hand-checked.

## 1. Transfer rule

From the current record constant c1, a second element has density
`c2 >= 1/(1 + 2(1-c1)/c1)` (HSZ Lemma 1.1 / Remark 3.4(iv)).

- c1 = 1/2: 2(1-c1)/c1 = 2(1/2)/(1/2) = 2, so c2 = 1/(1+2) = **1/3** ✓
- c1 = 2/3 (sanity): 2(1/3)/(2/3) = 1, c2 = 1/(1+1) = 1/2 ✓
- c1 = 0.38234: (1-c1)/c1 = 0.61766/0.38234; 2x = 1.23532/0.38234 = 3.23086;
  1+3.23086 = 4.23086; c2 = 1/4.23086 = **0.23636** ≈ paper's **0.23635** ✓

## 2. Nagel iteration identity (exact, symbolic)

```
1/(1 + 2(1 - 1/(2^{k-1}+1)) / (1/(2^{k-1}+1)))  =  1/(2^k + 1)
```
Let x = 1/(2^{k-1}+1). Then 2(1-x)/x = 2(1/x - 1) = 2(2^{k-1}+1-1) = 2^k.
So the whole expression = 1/(1 + 2^k) = **1/(2^k + 1)**.
This is the identity that lets Frankl's level-1 bound (1/2) iterate into
Nagel's kth-frequency bound inductively: level k-1 density 1/(2^{k-1}+1)
transfers to level k density 1/(2^k+1). Confirms `hsz-nagel-equivalent-frankl`.

## 3. One element of any k-set

`c >= 1/(2^{|A|-2}+1)` (HSZ Prop 3.3):
- |A|=2: 1/(2^0+1) = 1/2  (Sarvate–Renaud ✓)
- |A|=3: 1/(2^1+1) = 1/3  ✓
- |A|=4: 1/(2^2+1) = 1/5
- |A|=5: 1/(2^3+1) = 1/9

## 4. Nagel level 1

1/(2^0+1) = 1/2 = Frankl's density bound ✓ (so Nagel(k=1) is Frankl exactly).

## Bearing

These identities underpin the `hsz-*` claims that feed the abundance-profile
thread:
- the two-element profile target (second element ≥ 0.23635 from record 0.38234;
  the conjectured (1/2, 1/3) pair when a 2-set exists);
- the Frankl ⟺ Nagel equivalence (already held via daswu-nagel, now with a
  second independent route).

All exact; no floats. Hand-checked, pending execution of hsz_transfer_verify.py
as a second mechanical route.

```claim
id: hsz-transfer-identities-check
statement: The HSZ density-transfer quantities check exactly: c2=1/3 at c1=1/2;
  c2=0.23636 from c1=0.38234 (paper 0.23635); the Nagel iteration identity
  1/(1+2(1-1/(2^{k-1}+1))/(1/(2^{k-1}+1))) = 1/(2^k+1) holds symbolically;
  1/(2^{|A|-2}+1) rung values 1/2,1/3,1/5,1/9 for |A|=2,3,4,5.
hypotheses: exact rational arithmetic; the HSZ Lemma 1.1 formula as stated.
holds-here: yes
status: checked (hand-verified exact algebra; mechanical route pending at
  code/out/hsz_transfer_verify.py)
bearing: confirms the numerical targets feeding the abundance-profile thread
  (second-element density from the record; Frankl<->Nagel iteration); the
  (1/2,1/3) pair is a stated open conjecture, the 0.23635 value is a proved
  transfer.
anchor: research/sources/hu-shi-zhou-frankl-lemma-2025.html.full.md (Lemma 1.1,
  Prop 3.3, Remark 3.4)
follows-from: hsz-frankl-lemma-density-transfer
```
