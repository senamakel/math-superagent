% Sanity test: a trivially FALSE claim. Axiom forces c=5, conjecture claims c=3.
tff(dom, type, nr: $int).
tff(c5, axiom, $to_int(tptp_int) = 0 | $to_int(5) = 5).
fof(c_is_5, axiom, $to_int(5) = 5).
fof(goal, conjecture, $to_int(5) = 3).
