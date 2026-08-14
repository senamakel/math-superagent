% Refute: "101 is a length-3 factor of S_3" (the G3/G-stabilization candidate
% n0(3)=3 threshold).  Encoding over a 5-position domain {p0..p4} with a binary
% alphabet label l: pos->{0,1}.
%
% Axioms fix the word S_3 = 0 1 0 0 1  ("01001").  We claim the length-3 factor
% "101" does not occur.  The engine should find the model {p0:0,p1:1,p2:0,
% p3:0,p4:1} which satisfies the axioms and falsifies "101 occurs".

fof(dom, axiom,
    (domain(p0) & domain(p1) & domain(p2) & domain(p3) & domain(p4)
     & (p0 != p1) & (p0 != p2) & (p0 != p3) & (p0 != p4)
     & (p1 != p2) & (p1 != p3) & (p1 != p4)
     & (p2 != p3) & (p2 != p4)
     & (p3 != p4)
     & ! [X] : (domain(X) => (X = p0 | X = p1 | X = p2 | X = p3 | X = p4)))).

% labels: 0 at p0,p2,p3 ; 1 at p1,p4
fof(lab0, axiom, label(p0) = zero).
fof(lab1, axiom, label(p1) = one).
fof(lab2, axiom, label(p2) = zero).
fof(lab3, axiom, label(p3) = zero).
fof(lab4, axiom, label(p4) = one).

% successor relation on positions (p0->p1->p2->p3->p4), only adjacent pairs.
fof(succ, axiom,
    (nxt(p0,p1) & nxt(p1,p2) & nxt(p2,p3) & nxt(p3,p4)
     & ! [X,Y] : (nxt(X,Y) =>
            ((X=p0 & Y=p1) | (X=p1 & Y=p2) | (X=p2 & Y=p3) | (X=p3 & Y=p4))))).

% Conjecture: some position X has label=1 at X, label=0 at next, label=1 at
% next-next.  (i.e. "101" is a length-3 factor of S_3)
fof(goal, conjecture,
    ? [X,Y,Z] : (nxt(X,Y) & nxt(Y,Z)
                 & label(X) = one & label(Y) = zero & label(Z) = one)).
