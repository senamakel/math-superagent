> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/ponder-this-april-2004-digits.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://research.ibm.com/haifa/ponderthis/challenges/April2004.html | converted from HTML -->

## What is in it

  - Solution
  - Solvers
  - Related posts
    - [Ponder This Challenge - August 2026 - The Wheel of Buttons][3]
    - [Ponder This Challenge - July 2026 - Return of the Superheroes][4]
    - [Ponder This Challenge - June 2026 - The Superhero Team Movies][5]
    - [Ponder This Challenge - May 2026 - The Powers of a Binary Matrix][6]


## What it claims

My friend compulsively records television programs on his VCR. To this end, he has a very large stock of VCR cassettes. He has long given up on trying to label these cassettes with any meaningful names. Now he just numbers them. The numbers go from 1 up and are consecutive.

In order to label the cassettes, he uses the digit stickers that come with a bought cassette. Each cassette comes with one sticker for each digit.

So, for example, to label the first cassette, he uses just the sticker "1" and keeps the rest. To label the second, he uses just the sticker "2" and keeps the rest. To label the tenth, he uses two stickers, one "1" and one "0", and keeps the rest. To label the eleventh, he uses one "1" sticker from the stickers he just got, and one "1" sticker which he had in stock from the previous ten. And so on.

The question is, what is the number of the first cassette which he will no longer be able to label in this way (i.e., that will deplete his stock of stickers to the point that he will not be able to form the desired number)? Please give your answer for general B, as well…

## Statements it makes

Lemma: For all b and n, c(1, n) >= c(b, n).
Proof: There is a 1-to-1 mapping between the occurrences of any particular digit b != 1 and the occurrences of digit 1, with digit b in the bit position valued B^d, d >= 0, of numeral n' being paired with digit 1 in the same bit position of a lesser numeral, n' - (b-1)*B^d if b > 1 or n' - (B-1)*B^d if b = 0. So for every occurrence of digit b contributing to c(b, n) there is an occurrence of digit 1 contributing to c(1, n) -- QED. Let C(n) = c(1, n) and E(n) = C(n)-n, the desired integer N being the least such that E(N) > 0. Let Z = B-1, the largest digit.

Lemma: The leading (leftmost) digit of N must be 1.
Proof: Assume N to have a leading digit b > 1. Let M be the largest numeral less than N with a leading 1 (its digits being 1ZZ...Z), let m be the largest numeral with one fewer digits than N (ZZ...Z), and let m' be N with its leading digit removed; so E(N) = E(M) + (d-2)*E(m) + E(m'). Since M < N, m < N, and m' < N, it must be that E(M) <= 0, E(m) <= 0, E(m') <= 0, and consequently E(N) <= 0, a contradiction -- QED, reductio ad absurdum. So 1 followed by D >= 0 additional digits expresses N.

*[digest of a 17805 character source; every section, statement, and proof in full at `research/sources/ponder-this-april-2004-digits.full.md`]*
