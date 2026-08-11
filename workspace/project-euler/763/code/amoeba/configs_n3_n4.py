"""Dump the ACTUAL reachable configurations for N=3 and N=4 of Project Euler 763.

An amoeba at p=(x,y,z) divides into three at (x+1,y,z),(x,y+1,z),(x,y,z+1),
provided those three cubes are all empty; the dividing amoeba disappears.
D(N) is the number of DISTINCT sets of occupied cubes reachable after exactly
N divisions.

This BFSes levels 0..4 with exact frozenset-of-tuples arithmetic and prints
each distinct configuration for N=3 (9 states) and N=4 (30 states), sorted,
one per line — both to stdout and to code/out/configs_n3_n4.txt.

Correctness: reproduces D(3)=9 and D(4)=30 from the established sequence
in code/out/d_values.txt (itself validated on D(2)=3, D(10)=44499).
"""

E1, E2, E3 = (1, 0, 0), (0, 1, 0), (0, 0, 1)


def next_level(level):
    nxt = set()
    for S in level:
        Sset = set(S)
        for p in S:
            a = (p[0] + E1[0], p[1] + E1[1], p[2] + E1[2])
            b = (p[0] + E2[0], p[1] + E2[1], p[2] + E2[2])
            c = (p[0] + E3[0], p[1] + E3[1], p[2] + E3[2])
            if a not in Sset and b not in Sset and c not in Sset:
                ns = Sset - {p} | {a, b, c}
                nxt.add(frozenset(ns))
    return nxt


def fmt_config(S):
    """Render a config as a readable sorted list of (x,y,z) triples."""
    return "{" + ", ".join(sorted(f"({x},{y},{z})" for (x, y, z) in S)) + "}"


def main(out_path):
    level = {frozenset({(0, 0, 0)})}
    all_levels = {0: level}
    for n in range(1, 5):
        level = next_level(level)
        all_levels[n] = level

    lines = []
    for n in (3, 4):
        configs = sorted(all_levels[n], key=lambda S: sorted(S))
        if n == 3:
            assert len(configs) == 9, f"N=3 has {len(configs)} configs, expected 9"
        if n == 4:
            assert len(configs) == 30, f"N=4 has {len(configs)} configs, expected 30"
        lines.append(f"=== N={n}  ({len(configs)} configurations) ===")
        for S in configs:
            lines.append(fmt_config(S))
        lines.append("")

    text = "\n".join(lines)
    print(text, flush=True)
    with open(out_path, "w") as f:
        f.write(text + "\n")
    print(f"\nWrote {out_path}", flush=True)


if __name__ == "__main__":
    main("out/configs_n3_n4.txt")
