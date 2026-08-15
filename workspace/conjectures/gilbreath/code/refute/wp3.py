import itertools

def next_row(interior):
    prev = [1] + list(interior)
    out = []
    for i in range(len(interior)):
        out.append(abs(prev[i] - prev[i+1]))
    return tuple(out)

def comp_dominates(a, b):
    n = min(len(a), len(b))
    if any(a[i] < b[i] for i in range(n)):
        return False
    return any(a[i] > b[i] for i in range(n))

def main():
    for L in range(2, 9):
        total = 0
        for interior in itertools.product((0, 2, 4), repeat=L):
            child = next_row(interior)
            dp = tuple(max(0, a-2) for a in interior)
            dc = tuple(max(0, a-2) for a in child)
            if comp_dominates(dc, dp):
                total += 1
        print(f"L={L}: {total} dominating transitions of {3**L}")

main()
