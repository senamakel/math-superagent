# Confirm the closed-form derivation that links the two facts (no exec needed here;
# this is the algebra checked by code/uresultant/closed_form_check.py):

# ord_0(R_i) = n(n-i)  (weighted order, weight w(a_j)=j)  -- FACT (1), via de Frutos
# prod_{i=1}^{n-1} n(n-i) = n^{n-1} * prod_{j=1}^{n-1} j = n^{n-1} * (n-1)!
# quotient length (Samuel multiplicity, complete intersection) =
#   prod ord_0(R_i) / prod w(a_j) = prod ord_0 / n! = n^{n-1}(n-1)! / n! = n^{n-2}   -- FACT (2)
# For n=3,4,5,6 the run's captures verify the length via Singular vdim:
#   3^1=3, 4^2=16, 5^3=125, 6^4=1296, AND via the Samuel identity prod/ n!.
