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

from lib.amoeba import next_level_fs

def fmt_config(S):
    """Render a config as a readable sorted list of (x,y,z) triples."""
    return "{" + ", ".join(sorted(f"({x},{y},{z})" for (x, y, z) in S)) + "}"


def main(out_path):
    level = {frozenset({(0, 0, 0)})}
    all_levels = {0: level}
    for n in range(1, 5):
        level = next_level_fs(level)
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
