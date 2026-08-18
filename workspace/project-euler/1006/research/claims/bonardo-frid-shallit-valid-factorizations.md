```claim
id: bonardo-frid-shallit-valid-factorizations-formula
status: asserted
statement: For the Fibonacci word f (fixed point of mu: a->ab, b->a) and V(n) the number of valid factorizations of the length-n prefix f(0..n] into a decreasing sequence of standard Fibonacci words: if f[n]=a then V(n)=ceil(n/phi^2), equivalently the number of b's in f(0..n] plus one; if f[n]=b then V(n)=ceil(n/phi^3), equivalently the number of aa's in f(0..n] plus one. V(n) is the shuffle of the ceilings of two linear functions and is Fibonacci-regular.
hypotheses: n>=0; f the Fibonacci word a b a a b a b a ...; standard Fibonacci words f_i with f_0=a, f_1=b, f_{n+1}=f_n f_{n-1}; V(0)=1.
holds: yes — for the Fibonacci word, the complement convention of PE1006's S by 0<->1 letter relabel; factor sets invariant under complement.
source: https://ar5iv.labs.arxiv.org/html/1806.09534
```
