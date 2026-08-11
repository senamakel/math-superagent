# Scratchpad

Reduction: minimize |a + b*sqrt(d) - pi|, |a|,|b|<=n.
- s = sqrt(d) = a0 + alpha, alpha={sqrt(d)} in (0,1).
- For fixed b, best a = round(pi - b*sqrt(d)); error = ||pi - b*sqrt(d)|| = distance to nearest integer = ||pi - b*alpha||.
- b>=0: error = circular distance between {b*alpha} and beta={pi};
- b<0: let t=-b>=0; error = ||pi + t*alpha|| = circular distance between {t*alpha} and { -pi } = 1-beta.
- Feasible bound Bpos ~ (n+pi)/sqrt(d), Bneg ~ (n-pi)/sqrt(d).

So the core subproblem (both signs): irrational alpha in (0,1), target beta in [0,1), bound B; find b in [0,B] minimizing dist({b alpha}, beta).
This is "best left/right alpha-approximation" — solved in O(log B) by Cabanillas-Lopez & Labbe (arXiv:1904.01874), Propositions 9 & 10 + Algorithm 3(ii).
