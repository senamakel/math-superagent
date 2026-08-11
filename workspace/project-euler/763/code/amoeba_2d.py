"""2D amoeba BFS: amoeba at (x,y) divides into (x+1,y),(x,y+1) if both empty.
Count distinct reachable occupied sets after exactly N divisions.
Compare to A007902 = 1,1,2,4,9,20,46,105,243,561,1301,3014,...
"""
from functools import lru_cache

from lib.amoeba2d import next_level_fs2

def main():
    level = {frozenset([(0,0)])}
    print("N=0", 1)
    for n in range(1, 16):
        level = next_level_fs2(level)
        print(f"N={n}  D_2D={len(level)}")

main()
