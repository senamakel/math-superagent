# Belcher et al. — "Improved Bounds on the Sizes of S·P Numbers" (distinct class)

Source: https://ar5iv.labs.arxiv.org/html/0806.3585
(`research/sources/belcher-et-al-on-sp-numbers.arxiv.full.md`).

Justice et al. (the arxiv listing is the Kominers–Kominers improvement note);
Mathematical Gazette thread on **S·P numbers**.

**Definition of an S·P number (this paper's subject, NOT the PE 719 class).**
An integer equal to the product of its decimal digits times the sum of its
decimal digits. Classic examples: 135 = 1·3·5·(1+3+5) and 144 = 1·4·4·(1+4+4).

**What the paper establishes.** Improved finiteness bounds on the sizes of S·P
numbers (the earlier Mathematics Gazette result was "at most 60 digits"; here
the bound is sharpened, and a base-2 analogue is treated). The operation is
`product-of-digits × sum-of-digits`, a distinctly different operation from the
split-into-blocks-and-sum of PE 719.

**Why it does NOT help this run.** The name-collision "S·P" (used for these
digit-product×digit-sum numbers) is one of the three distractors a search for
"SP numbers / number splitting" can resolve to, alongside the two-block Kaprekar
class and SSPDS (see `research/notes/librarian-dead-ends.md` §4). None of its
results — finiteness of how many such numbers exist — transfers to the S-number
definition (blocks of a square summing to the root). It neither bears on
T(10¹²) nor should be fetched again.

```claim
id: sp-numbers-distinct-class
statement: S·P numbers (integer = product-of-digits times sum-of-digits; only 0,1,135,144 exist) are a distinct class from PE 719 S-numbers (blocks of a square summing to the root); their theory gives no result for T(10^12).
hypotheses: decimal; definitions of the two classes as stated.
holds-here: yes (it is a different problem)
status: asserted
bearing: prevents a future run from mistaking the S·P-number literature for the S-number problem; discard as a lead.
anchor: research/summaries/belcher-et-al-on-sp-numbers.arxiv.md
```
