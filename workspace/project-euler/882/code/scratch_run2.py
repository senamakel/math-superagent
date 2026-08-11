import sys
sys.setrecursionlimit(100000)
exec(open('/workspace/counting.py').read().split("def main")[0])

for n in range(1, 11):
    A, B = A_of_n(n), B_of_n(n)
    v = need_oneturn(A, B, {}, {})
    vs = int(v) if v != float('inf') else 'inf'
    print(f"n={n:2d} A={A:3d} B={B:3d} A-B={A-B:5d} S={vs}")
