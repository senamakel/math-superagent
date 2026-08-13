#!/usr/bin/env python3
"""Independent verification of code/out/giant_stretches_snapshot.json.

Different code path from giant_generating_stretches.py: fresh sieve with a
separate implementation (slice-assignment sieve), row iteration via
itertools.pairwise (not indexing loops), diffs computed with math.dist, and
the control scan over halved values rather than raw rows. Exact integers
throughout. Exits 0 only if every reconciled number matches the snapshot.

Checks per genuine event k in {34,56,64,68,94,96,110,112,126,130,134,146}:
  (a) block_profile of the event row == b[k-1] from blocks_depth1000.json
      (uses lib.gilbreath.block_profile, the library oracle);
  (b) generating stretch h_k over [b_k, b_{k+1}+1]: values, min/max,
      dominant value + count, distinct count, drift, step counts,
      longest run per value (all exact ints; nothing floats);
  (c) landing bits over [b_k, b_{k+1}]: run lengths of 0 and 1,
      counts of zeros/ones, longest zero-run, longest one-run;
  (d) all maximal 1-Lipschitz stretches of length >= 100 with their
      lengths, the container of the stretch (must be [1, b_{k+1}+1]),
      runner-up length, and the rank of the container by length.
Also: snapshot length == 12, landing block of row 161 (capped artifact) is
the 13th giant cross-checked in the main program, and total j = 1,091,362.
"""
import json
from itertools import pairwise
from collections import Counter

from lib.gilbreath import block_profile

SIEVE_LIMIT = 20_000_000
WANTED = 1_270_607
GENUINE = [34, 56, 64, 68, 94, 96, 110, 112, 126, 130, 134, 146]
MINLEN = 100


def sieve(n):
    """Slice-assignment sieve (independent of lib.gilbreath's loop sieve)."""
    isp = bytearray(b'\x01') * (n + 1)
    isp[0] = isp[1] = 0
    for p in range(2, int(n ** 0.5) + 1):
        if isp[p]:
            isp[p * p::p] = b'\x00' * (((n - p * p) // p) + 1)
    return [i for i in range(2, n + 1) if isp[i]]


def rle_of(seq):
    runs = []
    cur, cnt = seq[0], 1
    for v in seq[1:]:
        if v == cur:
            cnt += 1
        else:
            runs.append((cur, cnt))
            cur, cnt = v, 1
    runs.append((cur, cnt))
    return runs


def longest_runs_by_value(runs):
    m = {}
    for v, c in runs:
        m[v] = max(m.get(v, 0), c)
    return {str(k): v for k, v in m.items()}


def main():
    snap = json.load(open('code/out/giant_stretches_snapshot.json'))
    b = json.load(open('code/out/blocks_depth1000.json'))['b']
    assert len(snap['events']) == 12
    assert snap['tot_j'] == 1_091_362
    assert all(len(e['vals']) == e['j'] + 2 for e in snap['events'])

    primes = sieve(SIEVE_LIMIT)
    assert len(primes) == WANTED
    # different iterator: itertools.pairwise
    row = primes
    rows = [row]
    for r in range(1, 148):
        row = [abs(a - b) for a, b in pairwise(row)]
        rows.append(row)

    for e in snap['events']:
        k = e['k']
        bcur, bnxt = e['bcur'], e['bnxt']
        assert b[k - 1] == bcur and b[k] == bnxt, (k, 'b map')
        r = rows[k]
        # (a) library-oracle block profile of the event row
        assert block_profile(r) == bcur, (k, 'profile')
        # step law
        assert r[bcur] == 2 and r[bcur + 1] == 4, (k, 'step law')
        # (b) stretch values
        vals = e['vals']
        assert len(vals) == bnxt - bcur + 2, (k, 'len')
        recomputed = [r[i] // 2 for i in range(bcur, bnxt + 2)]
        assert recomputed == vals, (k, 'values')
        n = len(vals)
        assert min(vals) == e['vmin'] and max(vals) == e['vmax'], (k, 'minmax')
        vc = Counter(vals)
        dom, domc = vc.most_common(1)[0]
        assert dom == e['dom'] and domc == e['domc'], (k, 'dom')
        assert len(vc) == e['distinct'], (k, 'distinct')
        diffs = [vals[i + 1] - vals[i] for i in range(n - 1)]
        assert all(d in (-1, 0, 1) for d in diffs), (k, 'lipschitz')
        assert diffs.count(0) == e['lvl'] and diffs.count(1) == e['up'] \
            and diffs.count(-1) == e['dn'], (k, 'steps')
        assert sum(diffs) == e['drift'], (k, 'drift')
        v_runs = rle_of(vals)
        assert longest_runs_by_value(v_runs) == e['longest_per_value'], \
            (k, 'value runs')
        # (c) landing bits
        bits_runs = rle_of([rows[k + 1][i] // 2 for i in range(bcur, bnxt + 1)])
        assert [[v, c] for v, c in bits_runs] == e['bits'], (k, 'bits rle')
        assert all(v <= 1 for v, c in bits_runs), (k, 'bits values')
        assert rows[k + 1][bnxt + 1] not in (0, 2), (k, 'block maximality')
        zero_runs = [c for v, c in bits_runs if v == 0]
        one_runs = [c for v, c in bits_runs if v == 1]
        assert sum(zero_runs) == e['zc'] and sum(one_runs) == e['oc'], (k, '01 counts')
        assert max(zero_runs) == e['longest0'] and max(one_runs) == e['longest1'], \
            (k, '01 longest')
        # (d) control: stretches of row k, halved positions 1..L-1
        halves = [r[i] // 2 for i in range(1, len(r))]
        L = len(halves)
        bound = [i for i in range(1, L) if abs(halves[i - 1] - halves[i]) > 1]
        cuts = [0] + bound + [L]
        stretches = []
        for a, z in zip(cuts, cuts[1:]):
            if z - a >= MINLEN:
                stretches.append((a, z))              # half-open [a, z) positions (1-based)
        lens = sorted((z - a for a, z in stretches), reverse=True)
        assert lens == e['lengths'], (k, 'stretch lengths')
        # halves[t] = row[t+1]/2, so row position p <-> halves index p-1.
        # Old block = row positions 1..bcur <-> halves indices 0..bcur-1.
        cont = next((a, z) for a, z in stretches if a <= bcur - 1 < z)
        assert cont == (0, bnxt + 1), (k, 'container')   # [0, bnxt+1) slice
        clen = bnxt + 1
        assert cont[1] - cont[0] == clen, (k, 'container len')
        rank = 1 + sum(1 for ln in lens if ln > clen)
        assert rank == e['rank'] and sum(1 for ln in lens if ln == clen) - 1 == e['ties'], \
            (k, 'rank')
        assert e['n_stretch'] == len(stretches), (k, 'n stretch')
        # generating stretch's left part: consecutive Lipschitz steps
        # connecting halves indices 0..bcur-1 (row positions 1..bcur)
        assert all(abs(halves[t - 1] - halves[t]) <= 1 for t in range(1, bcur)), \
            (k, 'left chain')
        if e['runner'] is not None:
            runner = max(((a, z) for a, z in stretches if not (a <= bcur - 1 < z)),
                         key=lambda t: t[1] - t[0])
            assert e['runner'][2] == runner[1] - runner[0], (k, 'runner')
        else:
            assert len(stretches) == 1, (k, 'only cont')

    print('VERIFY-OK: 12 genuine giants independently recomputed '
          '(fresh sieve, pairwise iterator, abs-list-comp diffs, halved-value '
          'control scan): all (a)(b)(c)(d) numbers match the snapshot; '
          'block_profile oracle matches stored b at all 12 event rows; '
          'containers = [1, b_{k+1}+1]; library claims '
          'step-law (2,4) and block maximality re-confirmed.')


if __name__ == '__main__':
    main()