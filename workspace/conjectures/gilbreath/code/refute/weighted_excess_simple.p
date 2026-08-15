% Attack R-weighted-excess-potential: NO weight sequence (w_i>=0, w_1>0)
% makes P_k = sum w_i*max(0,A_k(i)-2) non-increasing on every array.
%
% Counterexample pair: A=(1,4,0) -> A'=(3,4).
%   parent defects d  = (0, 2, 0)   (col2=2)
%   child  defects d' = (1, 2)      (col1=1, col2=2)
%   P(A)  = 2*w2 ; P(A') = w1 + 2*w2
%   monotonicity P(A')<=P(A)  ==>  w1 <= 0, contradicting w1 > 0.
%
% Encode: the claim (conjecture) is that some admissible weight makes
% monotonicity hold on this pair.  If find_counterexample returns a model,
% the pair is NOT monotone-satisfiable, i.e. every admissible weight fails.

fof(admissible, axiom,
    ( w1 > 0 & w2 >= 0 & w3 >= 0 )).

% monotonicity on the pair, phrased as an existence:
fof(goal, conjecture,
    ( w1 + 2*w2 =< 2*w2 )).
