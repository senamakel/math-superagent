> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/brown-totientsum-ancillary.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/src/2506.07386v1/anc/totientsum.py | converted from plain text -->

## What is in it

- ! /usr/bin/env python3


## What it claims

def primegen(limit=inf):
    """
    Generates primes strictly less than limit almost-lazily by a segmented
    sieve of Eratosthenes.  Memory usage depends on the sequence of prime
    gaps; on Cramer's conjecture, it is O(sqrt(p) * log(p)^2), where p is
    the most-recently-yielded prime.

Input: limit -- a number (default = inf)

Output: sequence of integers

Examples:

>>> list(islice(primegen(), 19))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]

>>> list(primegen(71))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
    """
    # We do not sieve 2, so we ought to be able to get sigificant savings by halving the length of the sieve.
    # But the tiny extra computation involved in that seems to exceed the savings.
    yield from takewhile(lambda x: x < limit, (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47))
    pl, pg = [3,5,7], primegen()
    for p in pl: next(pg)
    while True:
        lo = pl[-1]**2
        if lo >= limit: break
        pl.append(next(pg))
        hi = min(pl[-1]**2, limit)
        sieve =…

def…

Input:…

*[digest of a 7909 character source; every section, statement, and proof in full at `research/sources/brown-totientsum-ancillary.full.md`]*
