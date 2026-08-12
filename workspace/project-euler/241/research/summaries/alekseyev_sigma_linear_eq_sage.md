> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/alekseyev_sigma_linear_eq_sage.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://raw.githubusercontent.com/maxale/multiplicative_functions/main/sigma_linear_eq.sage | converted from plain text -->

## What is in it

- to support case b=0;…
        - Reference sequences
        - Main function res_solve_sigma_abc()
- print('Current:', (a,b,c,M), g)
- g must divide n
            if gcd(M,g)>1:
                return None
            f =…
- for prime p, a*sigma(p) - b*p - c = (a-b)*p + (a-c)
        if a==b==c:
            if…
- for n >= 2 and a>=b,  c = a*sigma(n) - b*n >= a*(n+1) - b*n = (a-b)*n + a >= 3*a - 2*b…
- lower and upper bounds for omega and bigomega
        omg_lb, omg_ub = aux.get('omega',…
- print('succ Omega:', Omg_lb, Omg_ub)
- reduce_abc guarantees that gcd(b,g)==1, gcd(g,M) == 1, and min(prime_factors(g)) >=…
- Note that p is not necessarily spf(n)
        - Prime Wheel ADDED: 20251013
- we have sigma(n)/n <= n/phi(n) = prod_{p|n} p/(p-1).
- …


## What it claims

Implementation of the algorithm proposed in the paper:
* M. A. Alekseyev. "Computing bounded solutions to linear Diophantine equations with the sum of divisors", 2026.
  arXiv:2601.17832 [math.NT] https://arxiv.org/abs/2601.17832

Brief history:
* 20260127: Minor bugfix; OEIS A391615, A391617 included in the references
* 20260124: First public release
'''

print(f'sigma_linear_eq.sage ver. {__version__}\n\tSage ver. {sage.version.version}')

load('par_setup.sage')
# for robin_bound()
load('sigma_over_n_bound.sage')

import itertools
import functools
import time
from collections import deque

proof.arithmetic(False)

*[digest of a 25323 character source; every section, statement, and proof in full at `research/sources/alekseyev_sigma_linear_eq_sage.full.md`]*
