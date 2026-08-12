#!/usr/bin/env python3
"""Time one g_ratio call of indep_game_encoding at full grid to budget the run."""
import time
import math
import indep_game_encoding as ige

for shape in ['circle', 'square', 'hexagon']:
    t0 = time.time()
    g = ige.g_ratio(shape, 4.0, math.pi if shape == 'circle' else math.pi, 200000)
    t1 = time.time()
    print(f"{shape}: g_ratio(4.0, pi, 200000) = {g:.6f}  in {t1 - t0:.2f} s")