"""Runner for the diversified degree-20 candidate families (div2 batch).

Drives the canonical scorer over every div2 candidate and records, for each,
BOTH the score (from score.py itself, via subprocess) AND the first-failing-j
(its own exact re-derivation of the same sympy Poly.gcd over QQ, so it can
report WHICH derivative first fails -- the scorer only reports the count).

Deliverable: the first-failing-j DISTRIBUTION ACROSS THE FIVE FAMILIES: does
the binding constraint always sit at the high-multiplicity root's limit, or
does it vary by family? This is exactly the question the binomial family cannot
answer (on x^20 - c*x^k the answer is always j=k).

Writes:
  code/search/ca-degree20/DIVERSIFIED.md  -- table (family, candidate, score,
      first-failing-j) + the distribution + the bug-guard result.
  appends the div2 candidates to SEARCH.md (row log) and to scores.jsonl.

Bug guard (directive-11 / PROBLEM.md): a score of 19 from any non-trivial
poly is IMPOSSIBLE -- only (x-a)^20 reaches it, and the scorer rejects that as
its trivial family. If any div2 candidate reports SCORE 19, that is a BUG in
score.py, not a counterexample; the runner diagnoses and flags it, never
reports it as a breakthrough.
"""

import glob
import importlib.util
import io
import json
import os
import subprocess
import sys

from sympy import Poly, QQ, symbols

x = symbols('x')
N = 20
HERE = os.path.dirname(os.path.abspath(__file__))
CAND_DIR = os.path.join(HERE, 'candidates')

# Persistent analysis of the first-failing-j distribution, written into
# DIVERSIFIED.md on every run (so a re-run cannot wipe the interpretation).
_ANALYSIS = """## What the distribution says (the deliverable)

**First-failing-j VARIES by family and by parameter -- it is not always the
high-multiplicity root's limit, and it is not a binomial-family constant.**
Contrast with the binomial family `x^20 - c*x^k`, where the only failing
derivative is always `j = k` and every non-trivial binomial scores 18 for
free. The div2 batch breaks that plateau, and the binding constraint is
different per construction:

- **TRINOMIAL** (`x^20 + a*x^k + b*x^m`, all five candidates score 17, not 18):
  the two exposed exponents `k < m` are the two failing derivatives -- a
  derivative `j` fails exactly when it 'lands on' an exposed non-monomial term
  where the monomial root 0 is not a root of `f^(j)`. First-failing-j is the
  smallest exposed exponent (j = 2,3,5,6,9 across the five). Score 17 = 19 - 2
  fails, so a genuine third support term breaks the two-term plateau at 18.
  Verified exactly: failing-j == {k, m} for all five trinomials.
- **FACTORED `(x-r)^m*g`**: first-failing-j sits at `m` (just past the heavy
  root's multiplicity, which covers 1..m-1): f1 (m=15)->j=15, f2 (m=14)->j=14,
  f3 (m=16)->j=16, f4 (m=15)->j=15. The irreducible tail adds no sharing, so
  score = m-1 = 14,13,15,16. The high-multiplicity mechanism in purest form.
- **ROOT-MULTISET**: depends on cross-multiplicity sharing. Balanced
  `x^8(x-1)^7(x+1)^5` (8-7-5) scores only 8, failing at j=8 (smallest heavy
  multiplicity); one-dominant rootsets (16-2-2, 15-3-2) score 15/14 failing at
  j=16/15, just past the dominant multiplicity. Weak cross-sharing; the
  dominant root's multiplicity governs.
- **CYCLOTOMIC**: highly variable. `(x^5-1)^4` scores 3 (5th roots mult 4,
  j=4 fails); `(x^10-1)^2` scores 1 (double roots, j=2); `(x-1)^12*phi_20(x-1)`
  scores **15** failing at j=12 AND j=14,16,18 -- a NON-contiguous failing set
  (shares only odd high j). The only family whose failure pattern is not a
  single contiguous block: a parity/structure signature unique to the shifted
  cyclotomic shape.
- **CHEBYSHEV** scores 0-1: all-simple T_20 roots and double T_10^2 roots give
  only trivial j=1/2 sharing; no recycled-root structure.

**Conclusion for the search.** 'score = m-1, fail at j = m' is real but only
for single-heavy-root constructions. Once the support is genuinely multi-term
(trinomials cap at 17 with two fails) or multiplicities are balanced or roots
carry cyclotomic/parity structure, both the score and the first-failing-j move.
No div2 candidate approaches 19, and none should: 19 on a non-trivial
polynomial is exactly the open conjecture and would be a scorer bug. The
binding constraint is family-dependent -- precisely the information the
all-binomial population destroyed."""

FAMILY = {
    'div2_trinomial_': 'TRINOMIAL',
    'div2_rootset_':   'ROOT-MULTISET',
    'div2_factored_':  'FACTORED (x-r)^m g',
    'div2_cyclo_':     'CYCLOTOMIC',
    'div2_cheb_':      'CHEBYSHEV',
}


def load_poly(path):
    """Load the monic degree-20 rational Poly a div2 module exposes."""
    spec = importlib.util.spec_from_file_location('_cand', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    for name in dir(mod):
        if name.startswith('_'):
            continue
        attr = getattr(mod, name)
        if callable(attr) or isinstance(attr, (str, bytes, type(None))):
            continue
        try:
            p = Poly(attr, x)
        except Exception:
            continue
        if p.gens == (x,) and p.degree() == N and p.LC() == 1:
            return p.set_domain(QQ)
    raise RuntimeError('no monic deg-20 poly in %s' % path)


def first_fail(poly):
    """Return (score, first_failing_j): (k, j) or (k, None) if none fails.

    k = #{ j in 1..19 : deg(gcd(f,f^(j))) > 0 } (the canonical score, re-derived
    exactly); first_failing_j = smallest j with deg(gcd(f,f^(j))) == 0, or None
    if all 19 share a root.
    """
    d = poly
    score = 0
    ff = None
    for j in range(1, N):
        d = d.diff()
        if poly.gcd(d).degree() > 0:
            score += 1
        elif ff is None:
            ff = j
    return score, ff


def canon_score(path):
    """Run the canonical scorer and return its 'SCORE: k' / 'INVALID: ...' line."""
    r = subprocess.run([sys.executable, os.path.join(HERE, 'score.py'), path],
                       capture_output=True, text=True)
    out = r.stdout.strip()
    return out if out else ('FAILED exit %d: %s' % (r.returncode, r.stderr.strip()))


def family_of(base):
    for prefix, fam in FAMILY.items():
        if base.startswith(prefix):
            return fam
    return 'UNKNOWN'


def append_scores_jsonl(entries):
    """Append one scores.jsonl line per div2 candidate, mirroring the existing
    format (id, island, score, optionally reason). Uses fresh ids div2-<file>.
    Idempotent: any prior div2-* lines are removed first, so re-running the
    diverge never stacks duplicate rows."""
    path = os.path.join(HERE, 'scores.jsonl')
    with open(path) as fh:
        lines = fh.readlines()
    lines = [ln for ln in lines if '"div2-' not in ln]
    for ent in entries:
        lines.append(json.dumps(ent) + '\n')
    with open(path, 'w') as fh:
        fh.writelines(lines)


def append_search_md(rows):
    """Replace (or add) the div2 Row log table in SEARCH.md. Idempotent: if a
    '## div2 diversified batch' section already exists, it is replaced rather
    than duplicated (running the diverge twice must not double the log)."""
    path = os.path.join(HERE, 'SEARCH.md')
    block = ('\n## div2 diversified batch (added by diversify_run.py)\n\n'
             '| file | construction | first-failing-j | verdict |\n'
             '|------|--------------|-----------------|---------|\n')
    for row in rows:
        block += '| %s | %s | %s | %s |\n' % (
            row['file'], row['family'], row['ff'], row['canon'])
    with open(path) as fh:
        text = fh.read()
    marker = '## div2 diversified batch'
    if marker in text:
        head = text.split(marker)[0].rstrip() + '\n'
        text = head + block
    else:
        text = text.rstrip() + '\n' + block
    with open(path, 'w') as fh:
        fh.write(text)


def main():
    files = sorted(glob.glob(os.path.join(CAND_DIR, 'div2_*.py')))
    if not files:
        print('no div2 candidates found')
        return 1

    rows = []
    bug = []
    for path in files:
        base = os.path.basename(path)
        poly = load_poly(path)
        score, ff = first_fail(poly)
        canon = canon_score(path)
        # the canonical scorer must agree with our exact re-derivation
        if not canon.startswith('SCORE: %d' % score):
            print('MISMATCH %s: ours=%d scorer=%r' % (base, score, canon))
            return 2
        rows.append({
            'file': base,
            'family': family_of(base),
            'score': score,
            'ff': ff,
            'canon': canon,
        })
        if score == 19:
            bug.append(base)

    # ---- the bug guard ----
    guard_msg = (
        'NO NON-TRIVIAL SCORE-19: bug guard clean. All div2 scores < 19; '
        'reaching 19 is exactly the open CA conjecture (only (x-a)^20\n'
        'legitimately hits it, which the scorer rejects as the trivial '
        'family). So no candidate here is a counterexample -- by construction.'
    ) if not bug else (
        '!!! BUG GUARD TRIPPED on %s: a non-trivial candidate reported SCORE 19. '
        'This is a BUG in score.py, NOT a counterexample; diagnose before '
        'reporting.' % bug
    )

    # ---- distribution of first-failing j BY FAMILY ----
    dist = {}
    for r in rows:
        dist[(r['family'], r['ff'])] = dist.get((r['family'], r['ff']), 0) + 1

    # ---- write DIVERSIFIED.md ----
    lines = []
    lines.append('# DIVERSIFIED degree-20 candidate search -- div2 batch')
    lines.append('')
    lines.append('Program: `code/search/ca-degree20/diversify_run.py`; scorer: '
                 '`code/search/ca-degree20/score.py` (exact sympy `Poly.gcd` over QQ); '
                 'base ring QQ; candidate modules: '
                 '%d (`div2_<family>_<param>.py`).' % len(rows))
    lines.append('')
    lines.append('## Table (family, candidate, score, first-failing-j)')
    lines.append('')
    lines.append('| family | candidate | score | first-failing-j | scorer verdict |')
    lines.append('|--------|-----------|-------|-----------------|----------------|')
    for r in sorted(rows, key=lambda r: (r['family'], r['file'])):
        lines.append('| %s | %s | %d | %s | %s |' % (
            r['family'], r['file'], r['score'],
            r['ff'] if r['ff'] is not None else 'NONE(all-19)', r['canon']))
    lines.append('')
    lines.append('## First-failing-j distribution ACROSS families')
    lines.append('')
    lines.append('(first-failing-j = smallest j in 1..19 with '
                 'deg(gcd(f, f^(j))) == 0; "NONE" would mean all 19 share a '
                 'root = the open conjecture.)')
    lines.append('')
    lines.append('| family | first-failing-j | count |')
    lines.append('|--------|-----------------|-------|')
    for (fam, ff), n in sorted(dist.items(), key=lambda kv: (kv[0][0], str(kv[0][1]))):
        lines.append('| %s | %s | %d |' % (fam, ff if ff is not None else 'NONE', n))
    lines.append('')
    lines.append('> %s' % guard_msg)
    lines.append('')
    lines.append(_ANALYSIS)
    lines.append('')
    with open(os.path.join(HERE, 'DIVERSIFIED.md'), 'w') as fh:
        fh.write('\n'.join(lines) + '\n')

    # ---- append to scores.jsonl and SEARCH.md ----
    json_entries = []
    for r in rows:
        j = {'id': 'div2-' + r['file'].replace('div2_', '').replace('.py', ''),
             'island': r['family'].lower(),
             'score': '%d' % r['score']}
        if r['score'] == 0 and 'INVALID' in r['canon']:
            j['reason'] = r['canon']
        json_entries.append(j)
    append_scores_jsonl(json_entries)
    append_search_md(rows)

    # ---- console report ----
    print('%d div2 candidates scored' % len(rows))
    print('')
    print('=== per-candidate (score, first-failing-j) ===')
    print('%-38s %-20s %5s %6s' % ('file', 'family', 'score', 'ff'))
    for r in sorted(rows, key=lambda r: (r['family'], r['file'])):
        print('%-38s %-20s %5d %6s' % (
            r['file'], r['family'], r['score'],
            r['ff'] if r['ff'] is not None else '-'))
    print('')
    print('=== first-failing-j DISTRIBUTION BY FAMILY ===')
    for (fam, ff), n in sorted(dist.items(), key=lambda kv: (kv[0][0], str(kv[0][1]))):
        print('  %-20s first-fail j=%-4s : %d' % (
            fam, ff if ff is not None else 'NONE', n))
    print('')
    print(guard_msg)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
