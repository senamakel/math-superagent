import sys
sys.path.insert(0, "/workspace/code")
from lib.unitfield import moser_spindle_points, diamond_points, minkowski_sum, unit_graph
from frac_chro_calib import chi_f, graph_from_points
import scipy.optimize as opt

moser = graph_from_points(moser_spindle_points())
print("Moser spindle: vertices,edges =", moser[0], len(moser[1]))
v, nset = chi_f(moser)
print("  chi_f(Moser) =", v, " (#independent sets =", nset, ")")

c5 = (5, [(0,1),(1,2),(2,3),(3,4),(4,0)])
print("C5: chi_f =", chi_f(c5)[0], " [expect 2.5]")

diam = graph_from_points(diamond_points())
print("Diamond: vertices =", diam[0], "edges =", len(diam[1]))
print("  chi_f(Diamond) =", chi_f(diam)[0], " [expect 3]")

M = moser_spindle_points()
S = minkowski_sum(M, M)
g = graph_from_points(S)
print("Moser+Moser: vertices =", g[0], "edges =", len(g[1]))
