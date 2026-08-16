"""Check the counter-model produced by code/refute/uc_with_three_set.p
against the canonical oracle.

Each slot s_i is a domain element; which elements e1..e4 it contains is given
by the member() predicate in the model. Decoding the model:

  member(fmb_1, fmb_1)=T, member(fmb_1,fmb_2)=F, member(fmb_1,fmb_3)=T,
  member(fmb_1,fmb_4)=F   =>  fmb_1 = {e1, e3}
  member(fmb_2,*): only member(fmb_2,fmb_4)=T  =>  fmb_2 = {e4}
  member(fmb_3,*): all False                     =>  fmb_3 = {}
  member(fmb_4,*): T,T,T,F for e1,e2,e3,e4       =>  fmb_4 = {e1,e2,e3}

Slot assignments in the model: s1=s2=s3=s4=fmb_1, s5=fmb_4, s6=fmb_3.
So the member sets named by the slots (with multiplicity) are:
  fmb_1, fmb_1, fmb_1, fmb_1, fmb_4, fmb_3
i.e. as a SET of distinct members: { {e1,e3}, {e1,e2,e3}, {} }  -- only 3 sets.

Note s1..s4 all equal the same object fmb_1, so the slots_distinct_sets axiom
became vacuous: the model collapsed the intended 6 distinct members onto 3,
and "no element in >=3 of the 6 slots" is satisfied only because 4 of the 6
slots name the same set.
"""
from lib.uc import decide_union_closed, abundance, abundant_elements

# Elements: e1=bit0, e2=bit1, e3=bit2, e4=bit3
# fmb_1 = {e1,e3} = 101b = 5
# fmb_4 = {e1,e2,e3} = 111b = 7
# fmb_3 = {} = 0
F = {5, 7, 0}
n = 4

print("Family (distinct member masks):", F)
print("distinct member count |F| =", len(F))
print("union-closed:", decide_union_closed(F))
ab = abundance(F, n)
print("abundance per element e1..e4:", ab)
print("abundant elements (2*count >= |F|):", abundant_elements(F, n))
print()
print("Interpretation: e1 appears in 2 of the 3 members = 2/3 >= 1/2.")
print("=> The family IS union-closed and HAS an abundant element (e1).")
print("=> It is NOT a counterexample to the rung 'contains a 3-set'.")
print("=> The 'refuted' verdict is an ENCODING BUG, not a refutation.")
