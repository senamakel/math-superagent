> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/swett-esc-verification-history.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://web.archive.org/web/20060803103919/http://math.uindy.edu/swett/esc.htm | converted from HTML -->

## What it claims

We think of E(n), or its abbreviated form S(n), as a "filter". Gathering a set of such filters, we use a C++ program to establish that a relatively small set of integers less than one hundred trillion (=10^14) "pass through" this larger filter. For the remaining integers k, those "trapped" by the filter, ESC(k) is known to be true by the Theorem (and by a pair of Lemmas, below).

An additional but basic fact about ESC is used to tighten the filter, and the C++ algorithm avoids consideration of some "well-known" residue classes mod 840. Specifically,

|

**Lemma 1:**

|

|

If k > 0 and k is not relatively prime to some positive integer m < 4000 then ESC(k) is true.

|

|

|

|

|

|

**Lemma 2:**

|

|

If k > 0 and the least residue of k, mod 840, is not in {1, 121, 169, 289, 361, 529} then ESC(k) is true.

|

The current version of the C++ program "filters" the first 100.8 trillion positive integers, using the two Lemmas and the filters S(n) for n = 1, 2, ..., 1000. Since ESC(n) need only be proven for prime n within this range (see Lemma 4 below), the program then eliminates…

|

## Statements it makes

**Theorem:**

**Lemma 1:**

**Lemma 2:**

**Lemma 3: **

**Lemma 4: **

*[digest of a 7070 character source; every section, statement, and proof in full at `research/sources/swett-esc-verification-history.full.md`]*
