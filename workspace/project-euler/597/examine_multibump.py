#!/usr/bin/env python3
"""Demonstrate the multi-bump overwrite bug in brute.simulate_order.

The bug: bumped_by[k]=j records only the LAST boat to bump k. A bumped boat
continues rowing, so it can be bumped again; when that happens the earlier
bump edge is silently lost, and `above` (built by following the single out_of
chain) then misses the reachability the new order rule requires.
"""
from brute import simulate_order, parity_of_new_order

def show(n, L, speeds, label):
    above = simulate_order(n, L, speeds)
    par, order = parity_of_new_order(n, above)
    print(f"{label}: above={above} new_order={order} parity={par}")

# Scenario: 3 boats (indices 0,1,2). Boat 1 bumps boat 2, then boat 0 later
# bumps boat 2 as well (boat 2 keeps rowing). v2 slowest, v1>v2, v0>v2, and
# boat 0 catches the (continuing) boat 2 after boat 1 has already stopped on it.
# Need L large so nobody finishes first.
# Speeds: v0=1.0, v1=3.0, v2=0.5, L=1000
# Boat1 catches boat2 in (80-40)/(3-0.5)=40/2.5=16s. Boat0 then rows toward...
# boat0 speed 1.0 vs boat2 0.5; boat0 must catch boat2 eventually, passing the
# stopped boat1 (OUT) freely. Track boat2: at t=16 it is at 40+0.5*16=48; boat0
# start pos 0, boat0 position at t = 1.0*t until it stops. Boat0 passes boat1's
# stop point, keeps going, catches boat2 when 1.0*t = 48+0.5*(t-16)... 
# => t = 48+0.5t-8 => 0.5t=40 => t=80; boat2 at 40+40=80, boat0 at 80. bump.
show(3, 1000, [1.0, 3.0, 0.5], "boat1 bumps boat2, then boat0 bumps boat2")

# Bigger chain, 4 boats: boat0->boat2, boat1->boat2, then boat2->boat3 (bumped
# boat keeps rowing and later bumps the front boat).  Expect a lossy/multi-hop
# divergence when the intermediate is bumped twice.
# Speeds: v2 > v3, v1 > v2, v0 > v1? keep L big.
show(4, 2000, [2.0, 1.5, 1.0, 0.5], "4-boat chain")
