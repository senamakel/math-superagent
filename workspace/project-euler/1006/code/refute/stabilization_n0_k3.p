% Attack on G-stabilization candidate threshold n0(k) = min n: |S_{n-1}| >= k.
% For k=3, candidate n0(3)=3.  S_3 = "01001".  p(i) := position i has letter '1'.
% Universe is {a,b,c,d,e} = positions 0..4; the domain is fixed by a dom predicate.
fof(dom, axiom,
    dom(a) & dom(b) & dom(c) & dom(d) & dom(e)
    & a!=b & a!=c & a!=d & a!=e & b!=c & b!=d & b!=e
    & c!=d & c!=e & d!=e).
% S_3 = "01001": p(a)=0(F), p(b)=1(T), p(c)=0, p(d)=0, p(e)=1.
fof(ax, axiom,
    ~p(a) & p(b) & ~p(c) & ~p(d) & p(e)
    & (p(a) => $false) & (~p(b) => $false) & (p(c) => $false)
    & (p(d) => $false) & (~p(e) => $false)).
% Conjecture: "101" occurs as a contiguous length-3 factor of S_3.
fof(goal, conjecture,
    (position(a) & position(b) & position(c)
     & p(a) & ~p(b) & p(c))
  | (position(b) & position(c) & position(d)
     & p(b) & ~p(c) & p(d))
  | (position(c) & position(d) & position(e)
     & p(c) & ~p(d) & p(e))).
fof(pos_all, axiom, ! [X] : (dom(X) => position(X))).
