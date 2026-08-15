"""Search for a finite-support refutation of R-weighted-excess-potential.

The rung: exists summable w_i>=0, w_1>0, P=sum w_i d_i non-increasing over
the row operator for EVERY nonneg-integer absolute-difference array,
d_i = max(0, A(i)-2).

A robust universal refutation: a parent row A (interior a_1..a_L, even values,
A(0)=1) whose child A' (interior length L-1) satisfies, on the COMMON columns
i=1..L-1:  d'_i >= d_i for all i, with d'_1 > d_1 (strict), AND the parent's
DROPPED final column L has d_L = 0 (i.e. a_L in {0,2}).

Then for ANY weights: P(A') - P(A) = sum_{i=1}^{L-1}(d'_i - d_i) w_i - d_L w_L
>= (d'_1 - d_1) w_1 > 0. Universal refutation, finite support.
"""
import itertools

def defects(interior):
    return tuple(max(0, a-2) for a in interior)

def next_interior(interior):
    prev = [1] + list(interior)
    return tuple(abs(prev[i]-prev[i+1]) for i in range(len(interior)))

def main():
    print("Search: parent ends in {0,2} (defect 0 on dropped column),")
    print("child dominates on common columns with strict increase at col 1.")
    for L in range(3, 10):
        found = 0
        ex = None
        for interior in itertools.product((0,2,4,6), repeat=L):
            if interior[-1] not in (0,2):  # dropped column must have defect 0
                continue
            child = next_interior(interior)
            d = defects(interior)   # length L
            dc = defects(child)     # length L-1
            # common columns 1..L-1 (0-indexed 0..L-2)
            common = L-1
            if any(dc[i] < d[i] for i in range(common)):
                continue
            if not (dc[0] > d[0]):
                continue
            found += 1
            if ex is None:
                ex = (interior, child, d, dc)
        print(f"L={L}: {found} universal refutations")
        if ex:
            interior, child, d, dc = ex
            print(f"  parent interior={interior} d_parent={d}")
            print(f"  child  interior={child}  d_child ={dc}")

main()
