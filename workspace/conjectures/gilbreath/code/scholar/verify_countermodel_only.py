"""
Verification handoff for claim `g-supply-switch-count-not-one-point` (the linchpin
of the "Route B cannot be made unconditional" verdict).

NOT YET RUN this cycle (scholar has no execution tool). Hand to tool_builder.

The claim to confirm, by elementary reasoning + a trivial numeric check:
the balanced one-point marginals #{p≡1 mod 4} ≈ #{p≡3 mod 4} ≈ pi(x)/2 do NOT
force any positive lower bound on the consecutive-pair switch count
N_switch(x) = #{p_n ≤ x : p_{n+1} !≡ p_n (mod 4)}, because the ordering that
lists all 1-mod-4 primes then all 3-mod-4 primes is consistent with the
marginals and achieves exactly ONE switch.

The construction is a proof-by-inspection (no program needed): for any residue
multiset with counts {1:m, 3:m'}, the ordering [1,...,1,3,...,3] has exactly one
boundary, hence exactly 1 switch. The class counts do not pin the switch count.
The script below only restates that numerically, including on the real primes.

Run:  python3 code/scholar/verify_countermodel_only.py
Expect: prints the class counts, the natural-order switch count, and the
countermodel switch count == 1, ending with a PASS.
"""
