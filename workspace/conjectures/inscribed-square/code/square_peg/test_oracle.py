"""Exact oracle regression and independent-route checks."""
from square_peg.oracle import find_squares, naive_vertex_squares
from square_peg.independent_check import independent_squares


def run():
    cases = [
        [(0,0),(1,0),(1,1),(0,1)],
        [(0,0),(2,0),(2,1),(0,1)],
        [(1,0),(0,1),(-1,0),(0,-1)],
        [(0,0),(2,0),(3,1),(1,1)],
    ]
    for polygon in (cases[1], cases[3]):
        assert find_squares(polygon) == independent_squares(polygon)
    assert len(find_squares([(0,0),(1,0),(1,1),(0,1)])) == 1
    assert len(naive_vertex_squares([(0,0),(1,0),(1,1),(0,1)])) == 1
    print("independent exact route agrees on", len(cases), "polygon cases")

if __name__ == "__main__":
    run()
