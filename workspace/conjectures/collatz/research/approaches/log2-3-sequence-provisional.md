# Provisional pattern work — log2(3) continued fraction

The run's chosen line is Diophantine cycle exclusion. I extracted 100 CF terms of delta=log_2(3) with mpmath at 800 digits and repeated at 1600 digits; all 100 terms were stable. The first 50 exactly match Crandall 1978's published list:

`[1,1,1,2,2,3,1,5,2,23,2,2,1,1,55,1,4,3,1,1,15,1,9,2,5,7,1,1,4,8,1,11,1,20,2,1,10,1,4,1,1,1,1,1,37,4,55,1,1,49]`.

Exact convergent recurrence `p_n=a_n p_{n-1}+p_{n-2}`, `q_n=a_n q_{n-1}+q_{n-2}` gives `q_21=6,586,818,670` and `p_21=10,439,860,591`, exactly the Eliahou bounds recorded in Lagarias; `q_23=137,528,045,312`, matching Hercher's approximately `1.375e11` bound. `analyze_sequence` over q_n reports no low-degree polynomial structure; no fitted recurrence should be claimed. OEIS lookup matches A028507, but its note is not a proof. The Hercher-ladder interval program timed out, so the broader claim that every quoted ladder value is exactly the interval's minimal denominator remains unverified here.
