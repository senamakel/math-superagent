import itertools

def defects(interior):
    return tuple(max(0, a-2) for a in interior)

def next_interior(interior):
    prev = [1] + list(interior)
    return tuple(abs(prev[i]-prev[i+1]) for i in range(len(interior)))

def main():
    for L in range(3, 10):
        found = 0
        for interior in itertools.product((0,2,4,6), repeat=L):
            if interior[-1] not in (0,2):
                continue
            child = next_interior(interior)
            d = defects(interior)
            dc = defects(child)
            common = L-1
            if any(dc[i] < d[i] for i in range(common)):
                continue
            if dc[0] > d[0]:
                found += 1
        print(f"L={L}: {found} universal refutations")

main()
