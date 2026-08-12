"""Investigate the Q_k decomposition completeness. D(N)=sum over M of R(N,M).
The Q-decomposition D(N)=sum_k Q_k(N)3^(N-2k-1) only covers M with
e=2M-N-1>=0 i.e. M>=(N+1)/2. Compute M_min per N and see when M_min>=(N+1)/2.
Also test whether there is structure to the lower-M ('off-diagonal') part."""
import collections, glob

def sorted_key(path):
    return int(path.split('level_')[1].split('.')[0])

R = collections.defaultdict(dict)
for path in sorted(glob.glob('/workspace/data/level_*.txt'), key=sorted_key):
    N = int(path.split('level_')[1].split('.')[0])
    c = collections.Counter()
    for line in open(path):
        parts = line.strip().split('|')
        M = int(parts[1].strip())
        c[M] += 1
    R[N].update(c)
for line in open('/workspace/code/out/mhist_13_14.txt'):
    line = line.strip()
    if line.startswith('N=') and 'M=' in line and 'expected' not in line:
        lhs, val = line.replace(' ', '').split(':')
        N = int(lhs.split('M=')[0].replace('N=', ''))
        M = int(lhs.split('M=')[1])
        R.setdefault(N, collections.Counter())[M] = int(val)

D = {2:3,3:9,4:30,5:99,6:336,7:1134,8:3855,9:13086,10:44499,11:151263,
     12:514419,13:1749267,14:5949063}

print("N: M_min, (N+1)/2, M_max, full-M coverage of Q-decomp?")
for N in sorted(R):
    Ms = sorted(R[N])
    mmin, mmax = Ms[0], Ms[-1]
    covered = (mmin >= (N+1)/2)
    # sum covered (M>=(N+1)/2) vs total
    cov_sum = sum(v for M,v in R[N].items() if M >= (N+1)/2)
    tot = sum(R[N].values())
    print(f"N={N:2d}: M_min={mmin:2d} M_max={mmax:2d} (N+1)/2={(N+1)/2:4.1f} "
          f"all-M>=threshold={covered} cov_sum={cov_sum} tot={tot} "
          f"missing={tot-cov_sum}")

# Check: is M_min pattern recognizable?
print("\nM_min over N:", [R[N][min(R[N])] if False else min(R[N]) for N in sorted(R)])
print("M_min sequence:", [min(R[N]) for N in sorted(R)])
print("N-M_min sequence:", [N-min(R[N]) for N in sorted(R)])
