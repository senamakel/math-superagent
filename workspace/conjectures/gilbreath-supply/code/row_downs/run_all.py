import sys, math
from itertools import product
sys.path.insert(0, '/workspace/code/row_downs')
from verify_downset_claims import downset, runs_of, is_power_of_two, part1, part2, part3

if __name__ == "__main__":
    part1()
    part2()
    part3(ns=(64, 128, 256))
