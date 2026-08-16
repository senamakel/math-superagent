"""For n=8 (small), list every distinct set in S2_char with the realizing (d,d') pair,
so we can see the structural characterization of which sets occur."""
from lib.collapse import S2_char, downset, run_count

def main():
    n = 8
    c = S2_char(n)
    ms = {d: downset(d, n) for d in range(2, n)}
    # pick for each distinct set the lexicographically smallest realizing pair
    for A in sorted(c, key=lambda a: (len(a), sorted(a))):
        pair = None
        for d in range(2, n):
            for dp in range(2, n):
                if frozenset(ms[d] ^ ms[dp]) == A:
                    pair = (d, dp)
                    break
            if pair: break
        mask = ''.join('1' if j in A else '0' for j in range(n))
        d, dp = pair
        md = ''.join('1' if j in ms[d] else '0' for j in range(n))
        mdp = ''.join('1' if j in ms[dp] else '0' for j in range(n))
        print(f"A={mask} d={d}({md}) d'={dp}({mdp}) size={len(A)} runs={run_count(A)} mult={c[A]}")

if __name__ == "__main__":
    main()
