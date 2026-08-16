#!/usr/bin/env python3
"""Sanity: confirm the sign convention [r_a!=r_b] <=> chi(r_a)chi(r_b)=-1.

r in {1,3}. chi(x) = -1 iff x==3 mod 4 else +1. So:
  r_a=1,r_b=1 : chi=1*1=1 -> product +1, [!=]=0 -> (-1)^0=+1. ok
  r_a=1,r_b=3 : chi=1*-1=-1 -> product -1, [!=]=1 -> (-1)^1=-1. ok
  r_a=3,r_b=1 : -1 -> [!=]=1 -> -1. ok
  r_a=3,r_b=3 : +1 -> [!=]=0 -> +1. ok
So (-1)^{[r_a!=r_b]} == chi(r_a)chi(r_b) exactly, no extra sign.
"""
