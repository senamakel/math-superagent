import math, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from al_automaton import algo_A, algo_B, perron_eigenvalue, scc_count

def main(Nmax):
    print("Family C(1,2^1,2^2,...,2^N): Abram-Lagarias label-product automaton")
    print(f"{'N':>2} {'#states':>10} {'#SCC':>5}   dim_H=log3(beta)")
    ms = []
    for N in range(1, Nmax+1):
        ms.append(2**N)
        t0 = time.time()
        ids, edges = algo_B(ms)
        n = len(ids); scc = scc_count(n, edges)
        b = perron_eigenvalue(n, edges)
        dim = math.log(b,3) if b>0 else 0.0
        print(f"{N:>2} {n:>10} {scc:>5}   {dim:.6f}   ({time.time()-t0:.2f}s)", flush=True)

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv)>1 else 10)
