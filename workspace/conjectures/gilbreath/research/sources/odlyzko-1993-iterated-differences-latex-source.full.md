<!-- source: https://www-users.cse.umn.edu/~odlyzko/doc/arch/gilbreath.conj.tex | converted from plain text -->

\documentstyle[11pt,amstex,amssymb]{amsart}
\newtheorem{theorem}{Theorem}
\newtheorem{corollary}{Corollary}
\newtheorem{lemma}{Lemma}
\newtheorem{prop}{Proposition}
\newcommand{\eqn}[1]{(\ref{#1})}
\newcommand{\dd}{\ldots}
%\setlength{\textwidth}{4.75in}
\linewidth=\textwidth
\hsize=\textwidth
\columnwidth\textwidth
%\setlength{\textheight}{8.25in}

%\def\Proof{\par\noindent{\bf Proof\/}:\enspace}
\renewcommand{\theequation}{\arabic{section}.\arabic{equation}}

\catcode`\@=11
\renewcommand{\section}{
        \setcounter{equation}{0}
        \@startsection {section}{1}{\z@}{-3.5ex plus -1ex minus
        -.2ex}{2.3ex plus .2ex}{\large\bf}
        }
\catcode`@=12

\title[Iterated Differences of Primes]{Iterated Absolute Values of Differences of Consecutive Primes}
\author[Andrew M. Odlyzko]{Andrew M. Odlyzko \\
~~ \\ [-.09in]
AT\&T Bell Laboratories, Murray Hill, NJ 07974}
\dedicatory{Dedicated to the memory of D.~H. Lehmer}
\thanks{1991 Mathematics Subject Classification:
Primary 11N05, 11Y99.
Secondary 11K36, 11Y16, 68Q25}
\begin{document}
\maketitle
\begin{abstract}
Let $d_0 (n) = p_n$, the $n$-th prime, for $n \ge 1$, and let $d_{k+1} (n) = | d_k (n) - d_k (n+1) |$ for $k \ge 0$, $n \ge 1$.
A well known conjecture, usually ascribed to Gilbreath but actually due to
Proth in the 19-th century, says that $d_k (1) =1$ for all $k \ge 1$.
This paper reports on a computation that verified this conjecture
for $k \le \pi (10^{13}) \approx 3 \times 10^{11}$.
It also discusses the evidence and the heuristics about this conjecture.
It is very likely that similar conjectures are also valid for
many other integer sequences.
\end{abstract}
\setlength{\baselineskip}{1.25\baselineskip}

\section{Introduction}
Let $p_1 = 2$, $p_2 =3 , \ldots$ be the primes in their natural ordering,
and set
\begin{equation}
\label{eq101}
\begin{array}{r@{~}l@{~}l}
d_0 (n) & = & p_n ~, ~~~~~~n \ge 1 \\
~~ \\
d_{k+1} (n) & = & | d_k (n) - d_k (n+1) | ~, ~~~~~~k \ge 0 , ~~~~n \ge 1 ~.
\end{array}
\end{equation}
Table~1 shows $d_k (n)$ for $0 \le k \le 20$, $1 \le n \le 20$.
Note
that $d_k (1) =1$ for $1 \le k \le 20$.
As was pointed out by H.~C. Williams, Proth \cite{Proth} claimed to prove that $d_k (1) =1$ for all $k \ge 1$, but his proof was faulty.
More recently, Gilbreath (unpublished) independently conjectured that $d_k (1) =1$
for all $k \ge 1$. (See Problem~A10 in \cite{Guy}, and also \cite{KR}.)
This is usually referred to as Gilbreath's conjecture.

Gilbreath's conjecture was verified for $k \le 63, 419$, that is for all
primes
\linebreak
$< 792, 731$, by Killgrove and Ralston \cite{KR},
who were fellow students of Gilbreath at UCLA in the late 1950's.
This paper reports on a verification of this conjecture for all primes
$< 10^{13}$, so that
$d_k (1) =1$ for $1 \le k \lesssim 3.4 \times 10^{11}$.
The computational results are presented in Section~3, and the algorithms
that were used are described in Section~4.

For a general sequence $d_0 (n)$, to compute $d_k (1)$ it is necessary to compute $d_j (i)$ for all $i+j \le k+1$, so that for $k \sim 3.4 \times 10^{11}$
approximately $5 \times 10^{22}$
numbers have to be computed,
far too many for the technology of today or the near future.
The computations for $d_0 (n) = p_n$ were possible because of special properties of the primes.
Note that $d_k (1)$ is odd and $d_k (2), d_k (3) , \ldots$, are even for all $ k \ge 1$.
If for some $N$ we find a $K$ such that $d_K (1) =1$ while $d_K (n) =0$ or 2 for all $1 \le n \le N$, then we can conclude that $d_k (1) =1$ for $K \le k \le N + K-1$.
Let $G(N)$ denote the minimal $k$ (if it exists) such that $d_j (1) =1$
for $1 \le j \le k$ and $d_k (n) =0$ or 2 for $1 \le n \le N$.
Computations show that $G(N)$ does  exist for all $N$ that have been checked and is small.
Table~2 presents some values.
(Similar observations have been made before, cf.~pp.~34--35 in
\cite{Sier}.)

A rigorous proof of Gilbreath's conjecture appears out of reach given our knowledge of primes.
Maximal gaps between consecutive primes around $x$ are thought to be not much larger than $( \log x )^2$.
(There is a conjecture of Cram\'{e}r \cite{Cramer} that these gaps are $O(( \log x)^2 )$, and numerical evidence \cite{Brent1,Brent2,YP} supports this conjecture as well as a slightly stronger one of Shanks \cite{Shanks}.
There are heuristic arguments, based on work of Maier \cite{Maier}, that suggest the true order of magnitude might be slightly larger, but
at most by some fractional power of $\log \log x$.)
However, the best published result is that of Mozzochi \cite{Mozz},
namely that these gaps are $\le x^{0.548}$ for large $x$,
and even on the assumption of the Riemann Hypothesis the bound for gaps can currently be lowered only to $x^{1/2 + o(1)}$ as $x \to \infty$.
Further, gaps are thought to behave randomly, but nothing has been proved in this direction.
Thus it is conceivable that for some $n$, $d_1 (n)$ is huge, while
$d_1 (j)$ for $1 \le j \le n-1$ are small and evenly distributed, so that $d_2 (n-1)$, $d_3 (n-2) , \ldots , d_n (1)$ are all large.

Section~2 discusses some heuristics which indicate that Gilbreath's conjecture
is likely to be true.
They also indicate what results might suffice to prove this conjecture, and
support the suggestion that corresponding conjectures are likely to hold
for many other sequences.
\section{Heuristics}
The Gilbreath conjecture appears difficult because there are few tools for
studying absolute values of differences of a sequence.
We will argue that this difficulty is not serious, and that a proof of Gilbreath's conjecture could probably be obtained if we could prove results about primes that appear much simpler.
Unfortunately those results are also unreachable with known tools.

The $d_k (n)$ for $k \ge 1$, $n \ge 2$, are even, and so $d_k (n) \equiv 0$ or 2 $( \bmod 4)$ in that range.
We note that the definition \eqn{eq101}
then implies that
\begin{equation}
\label{eq201}
d_{k+1} (n) \equiv d_k (n) + d_k (n+1) ~~~( \bmod 4 )
\end{equation}
for $k \ge 1$, $n \ge 2$.
This converts a problem defined by absolute values into one
involving linear congruences modulo~4.
Further, these congruences are of the simplest possible type,
those that occur in Pascal's triangle modulo~2.
(Modulus~4 arises only because of the factor~2 that is present in
the $d_k (n)$.)
If the primes are truly as random as they appear, the $d_1 (n)$
modulo~4 behave randomly, and then the linear congruence
\eqn{eq201} suggests that the $d_k (n)$ $(\bmod~4)$ are random.
It seems likely therefore that about half of the $d_k (n)$ will
be $0~( \bmod~4 )$ and half will be $2~ (\bmod~4)$, with
neighboring values almost independent.
Numerical evidence supports the conjecture that the $d_1 (n)
/2$, reduced modulo~2, are asymptotically independent for large
$n$.
(This is true only asymptotically, though, and among the $d_1
(n)/2$ for small $n$, there is an excess of odd ones, so that
2956 of the $d_1 (n)/2$ for $2 \le n \le 5001$ are odd, for
example.
Such dependencies among small primes were apparently first
noted by F. Roesler and his students in unpublished work about 6 years ago.)
This independence follows also from the Cram\'{e}r probabilistic
model
\cite{Cramer}, which predicts that gaps between consecutive
primes follow the Poisson law.
There is a proof by Gallagher \cite{Gal} that a form of the
Poisson law for prime gaps follows from a quantitative form of
the Hardy-Littlewood prime $k$-tuple conjecture, and one can
apply Gallagher's arguments directly to conclude that the $d_1
(n)/2$ reduced modulo~2 are independent for nearby values of
$n$.
At present no method is available for proving anything
rigorously.
If one could prove that the $d_1 (n)$ modulo~4 are
asymptotically independent, the proof might provide enough
machinery to show that along any path through which a large $d_1 (n)$ (which would, after all, have to be $\le n^{0.55}$ for $n$
large) could possibly produce a large $d_k (1)$, there would be enough collisions with nonzero
values of $d_j (m)$ to reduce the influence of this large
difference.
(What complicates the possible analysis of this kind is that
a large $d_1 (n)$ would not necessarily produce $d_n (1) > 1$,
but possibly only $d_m (1) > 1$ for some $m > n$.)

The arguments above apply to many other sequences in which the
first element is a 1, the others even, and where the gaps
between consecutive elements are not too large and are
sufficiently random.
Therefore, as has been observed before (cf.~Problem~A10 of \cite{Guy}), there
is probably not too much special about the primes in Gilbreath's
conjecture.

\section{Computational results}
Table~2 shows the value of $G(N)$ for various $N$ up to $N = \pi
(10^{13} )$.
The function $G(N)$ describes the extreme behavior that is observed.
To consider the average behavior, let $g(n)$ for $n \ge 2$ be the least $k$ such that
$d_j (n) =0$ or 2 for $k \le j \le k+ 1000$.
(It is likely that for all $n$ that were computed,
$d_j (n) = 0$ or 2 for all $j \ge g(n)$, but we cannot prove that.
If true, it would imply Gilbreath's conjecture.)
The average value of $g(n)$ (derived from sampling over intervals of length
$8 \times 10^7$)
is presented in Table~3 for several values of $n$.
The values of $g(n)$ are considerably smaller than $G(N)$, and this was used to increase the speed of the algorithm,
as is noted in Section~3.

Figures~1--3 show graphs of $d_k (n)$ for $\pi (10^{12}) +1 \le n \le \pi (10^{12}) +10^4$ for $k=1,50$, and 100.
This interval appears to be typical, and the graphs show that the process quickly reduces almost all entries to 0 and 2 (the two heavy lines on Figures~2 and 3), with only a few large
values that require many additional iterations to reduce.
Table~4 shows average values of $d_k (n)$ for
$\pi (10^{12}) +1 \le n \le \pi (10^{12} ) + \pi (8 \times 10^6) = \pi (10^{12})) + 289182$ and
various values of $k$.
In this set, $d_k (n)$ is reduced to 0 and 2 for $k=213$.
We note that the average values of $d_k (n)$ are not monotone
decreasing with $k$.

At the end of the Introduction, we noted that if huge gaps between consecutive primes existed, then Gilbreath's conjecture might be false.
Large values of $g(n)$ (and therefore of $G(N)$) do appear to be associated to large prime gaps.
Every large value of $g(n)$ that was looked at carefully (a very
small selection, it should be stressed) was due to a large
prime gap.
There were some large prime gaps that did not lead to large
values of $g(n)$, since other prime gaps nearby served to reduce
it in.
Statistically, though, the association between large prime gaps
and large values of $g(n)$ is noticeable.
Over $10^4$ blocks of length $8 \times 10^6$ each around $5.25
\times 10^{12}$ (see Section~4 for a definition), the
correlation between maximal values of $g(n)$ and maximal prime
gaps in a block was 0.52.
The largest value of $g(n)$ that was found, $g(n) = 635$ for $n$ close to
$\pi (7.17716 \times 10^{12} )$, is due to the prime gaps 674,
which is the largest one up to that height (\cite{Brent1,YP}).
The second largest value of $g(n)$,
$g(n) = 589$
for $n$ close to $\pi (2.61494 \times 10^{12} )$, is due to the
prime gaps 652, which is also the largest one up to its height.

To provide some information about large primes, computations
were also done with a set of primes near $10^{50}$ that had been
computed by the author earlier for a different purpose.
Let $u_0 (1) < u_0 (2) < \dd < u_0 (8737)$ be the primes in the
interval $[10^{50}, 10^{50} + 10^6]$, and let $u_{k+1} (n) = |
u_k (n) - u_k (n+1) |$ for $k \ge 0$, $n+k \le 8737$.
It was found that $\displaystyle\max_{1 \le n \le 8736} u_1 (n) =
920$, and $u_{436} (n) = 0$ or 2 for all $1 \le n \le 8301$, so
that 436 iterations sufficed to reduce this finite sequence.

The interval $[10^{100} , 10^{100} + 10^7]$ was also tested.
Deterministic primality tests would have required too much time,
so this interval was first sieved by small primes, and then the remaining
elements were tested using the probable prime tests in the Maple
symbolic manipulation system.
Thus although the 43271 integers that were found to be all the probable
primes are likely to be prime, this has not been rigorously established.
The largest gaps between any two consecutive probable primes was 2592, and 1417 iterations were required to reduce the iterated differences
to 0's and 2's.

\section{Algorithms}
Computation was performed in blocks $B= [b_1 , b_2 ]$ of integers from $b_1$ (which was always even)
to $b_2$ (which was odd), with the length of the block varying between
$5 \times 10^5$ and $8 \times 10^6$.
The first step was to compute the primes in $B$ using a previously computed table of primes $\le b_2^{1/2}$.
There is an extensive literature on prime number sieves (for example
\cite{BH,Beng,Pr1,Pr2,Pr3,Pr4,Sor1,Sor2}) and there are some theoretically extremely fast algorithms, such as the Pritchard method \cite{Pr1} that finds all primes $\le x$ in $O(x ( \log \log x)^{-1} )$ arithmetic operations.
However, for numbers of the sizes considered here, the conventional versions
of the sieve of
Eratosthenes are both faster and simpler to implement (cf. \cite{Sor2}), and so an algorithm similar to the ``segmented sieve'' of Bays and Hudson \cite{BH}
and of Brent \cite{Brent1} was used.
Since on the processor that was used access to memory was more of a bottleneck than processor speed, some of the operations were segmented further so as to
fit into the cache memory.

Once the primes in a block $B$ were determined, they were used together with the last 1000 primes from the preceding block to carry out the second phase, the absolute value of differences iterations.
(The number 1000 was chosen to exceed anticipated values of $G(N)$.)
Between 50 and 75 iterations were performed on the whole array, and this sufficed to reduce most entries to 0's and 2's.
This procedure took most
of the computing time of the second phase.
Finally, the remaining values of $d_k (n) > 2$ were grouped into
sets that were isolated from each other, and further iterations
were performed on those sets.
The block $B = [10^{12}, 10^{12} + 8 \times 10^6 -1]$, which
appears to be rather typical, contained $289,182$ primes.
After 75 iterations, there were 4640 values of $n$ with $d_{75}
(n) > 2$, and they were grouped into 516 sets which together
with the 0 and 2 entries that were associated covered $18,698$
values of $n$.
(Enough of the adjoining 0 and 2 entries were included to ensure validity of the computation.)
This procedure substantially improved the performance of the
algorithm.
Further speedups can be obtained by more sophisticated versions
of this strategy.

Programs were written in Fortran.
They were run on a Silicon Graphics 4D-220 computer that has 4 R3000 MIPS Computers 25~MHz processors, each rated at about 18~mips, and 128~Mbytes of main memory.
(The memory that was required for the programs varied between 5 and 20 megabytes, so was not a constraint.)
Programs were run at a low priority so as to use only spare cycles.
The code was not carefully optimized, and a speedup by a factor of 2 can probably be achieved.
Total run time (for a single processor) was several months,
with about 2 sec. necessary to process an interval of length $10^6$.
About half the machine time was spent in sieving for primes, and half in computing the iterated absolute
values of the differences.

There is some question about the reliability of a computation as long as this one,
especially since there are no easy methods for checking
the results.
The results stated in the text and in the tables are thought to be
correct, but cannot be fully guaranteed.
All instances where a value of $g(n) > 500$ was found were checked,
and one error was discovered that way.
The block $B = [M,M+8 \times 10^6)$ for $M= 8.972168 \times 10^{12}$
had been processed in two separate runs which gave maximal values of $g(n)$
for $n \in B$ of 914 and 261, respectively, with the higher value supposedly
due to a prime gap of 1158.
There is no such gap at this height, and 261 is the correct value, as
additional computations showed.
It was not possible to find out what caused the error.

\clearpage
\begin{thebibliography}{Brent22}
\setlength{\baselineskip}{1.25\baselineskip}
%\bibitem[BH]{BH}
\bibitem{BH}
C. Bays and R.~H. Hudson,
The segmented sieve of Eratosthenes and primes in arithmetic progressions to
$10^{12}$, {\em BIT 17} (1977), 121--127.
%\bibitem[Beng]{Beng}
\bibitem{Beng}
S.~A. Bengelloun,
An incremental primal sieve,
{\em Acta Inform. 23} (1986), 119--125.
%\bibitem[Brent1]{Brent1}
\bibitem{Brent1}
R.~P. Brent,
The first occurrence of large gaps between successive primes,
{\em Math. Comp. 27} (1973), 959--963.
%\bibitem[Brent2]{Brent2}
\bibitem{Brent2}
R.~P. Brent,
The first occurrence of certain large prime gaps,
{\em Math. Comp. 35} (1980), 1435--1436.
%\bibitem[Cramer]{Cramer}
\bibitem{Cramer}
H. Cram\'{e}r, On the order of magnitude of the difference
between consecutive prime numbers,
{\em Acta Arith. 2} (1937), 23--46.
%\bibitem[Gal]{Gal}
\bibitem{Gal}
P.~X. Gallagher, On the distribution of primes in short
intervals,
{\em Mathematika 23} (1976), 4--9.
%\bibitem[Guy]{Guy}
\bibitem{Guy}
R.~K. Guy,
{\em Unsolved Problems in Number Theory},
Springer, 1981.
%\bibitem[KR]{KR}
\bibitem{KR}
R.~B. Killgrove and K.~E. Ralston,
On a conjecture concerning the primes,
{\em Math. Comp.} ({\em Math. Tables Aids Comp.}) {\em 13} (1959), 121--122.
%\bibitem[Maier]{Maier}
\bibitem{Maier}
H. Maier,
Primes in short intervals,
{\em Michigan Math. J. 32} (1985), 221--225.
%\bibitem[Mozz]{Mozz}
\bibitem{Mozz}
C.~J. Mozzochi,
On the difference between consecutive primes,
{\em J. Number Theory 24} (1986), 181--187.
%\bibitem[Pr1]{Pr1}
\bibitem{Pr1}
P. Pritchard,
A sublinear additive sieve for finding prime numbers,
{\em Comm. ACM 24} (1981), 18--23.
%\bibitem[Pr2]{Pr2}
\bibitem{Pr2}
P. Pritchard,
Explaining the wheel sieve, {\em Acta Inform 17} (1982), 477--485.
%\bibitem[Pr3]{Pr3}
\bibitem{Pr3}
P. Pritchard,
Fast compact prime number sieves (among others),
{\em J. Algorithms 4} (1983), 332--344.
%\bibitem[Pr4]{Pr4}
\bibitem{Pr4}
P. Pritchard,
Linear prime-number sieves;
A family tree,
{\em Science of Computer Programming 9} (1987), 17--35.
%\bibitem[Proth]{Proth}
\bibitem{Proth}
F. Proth,
Sur la s\'{e}rie des nombres premiers,
{\em Nouvelle Correspondence Math\'{e}matique 4} (1878), 236--240.
%\bibitem[Shanks]{Shanks}
\bibitem{Shanks}
D. Shanks, On maximal gaps between consecutive primes,
{\em Math. Comp. 18} (1964), 646--651.
%\bibitem[Sier]{Sier}
\bibitem{Sier}
W. Sierpinski,
{\em A Selection of Problems in the Theory of Numbers},
Pergamon Press, 1964.
%\bibitem[Sor1]{Sor1}
\bibitem{Sor1}
J. Sorenson,
An introduction to prime number sieves, Computer Science Technical Report \#909, Univ. of Wisconsin-Madison, Jan.~1990.
%\bibitem[Sor2]{Sor2}
\bibitem{Sor2}
J. Sorenson,
An analysis of two prime number sieves,
Computer Science Technical Report \#1028,
Univ. of Wisconsin-Madison, June 1991.
%\bibitem[YP]{YP}
\bibitem{YP}
J. Young and A. Potler,
First occurrence prime gaps,
{\em Math. Comp. 52}
(1989), 221--224.
\end{thebibliography}
\clearpage
\begin{table}
\begin{center}
\begin{tabular}{r|rrrrrrrrrrrrrrrrrrrr}
\multicolumn{1}{c}{$k \Bigl\backslash n$} & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 & 19 & 20 \\ \cline{2-21}
0 & 2 & 3 & 5 & 7 & 11 & 13 & 17 & 19 & 23 & 29 & 31 & 37 & 41 & 43 & 47 & 53 & 59 & 61 & 67 & 71 \\
~~ \\ [-.05in]
1 & 1 & 2 & 2 & 4 & 2 & 4 & 2 & 4 & 6 & 2 & 6 & 4 & 2 & 4 & 6 & 6 & 2 & 6 & 4 & 2 \\
2 & 1 & 0 & 2 & 2 & 2 & 2 & 2 & 2 & 4 & 4 & 2 & 2 & 2 & 2 & 0 & 4 & 4 & 2 & 2 & 4 \\
3 & 1 & 2 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 2 & 0 & 0 & 0 & 2 & 4 & 0 & 2 & 0 & 2 & 2 \\
4 & 1 & 2 & 0 & 0 & 0 & 0 & 2 & 2 & 2 & 2 & 0 & 0 & 2 & 2 & 4 & 2 & 2 & 2 & 0 & 2 \\
5 & 1 & 2 & 0 & 0 & 0 & 2 & 0 & 0 & 0 & 2 & 0 & 2 & 0 & 2 & 2 & 0 & 0 & 2 & 2 & 2 \\
6 & 1 & 2 & 0 & 0 & 2 & 2 & 0 & 0 & 2 & 2 & 2 & 2 & 2 & 0 & 2 & 0 & 2 & 0 & 0 & 0 \\
7 & 1 & 2 & 0 & 2 & 0 & 2 & 0 & 2 & 0 & 0 & 0 & 0 & 2 & 2 & 2 & 2 & 2 & 0 & 0 & 0 \\
8 & 1 & 2 & 2 & 2 & 2 & 2 & 2 & 2 & 0 & 0 & 0 & 2 & 0 & 0 & 0 & 0 & 2 & 0 & 0 & 0 \\
9 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 2 & 0 & 0 & 2 & 2 & 0 & 0 & 0 & 2 & 2 & 0 & 0 & 0 \\
10 & 1 & 0 & 0 & 0 & 0 & 0 & 2 & 2 & 0 & 2 & 0 & 2 & 0 & 0 & 2 & 0 & 2 & 0 & 0 & 2 \\
11 & 1 & 0 & 0 & 0 & 0 & 2 & 0 & 2 & 2 & 2 & 2 & 2 & 0 & 2 & 2 & 2 & 2 & 0 & 2 & 2 \\
12 & 1 & 0 & 0 & 0 & 2 & 2 & 2 & 0 & 0 & 0 & 0 & 2 & 2 & 0 & 0 & 0 & 2 & 2 & 0 & 2 \\
13 & 1 & 0 & 0 & 2 & 0 & 0 & 2 & 0 & 0 & 0 & 2 & 0 & 2 & 0 & 0 & 2 & 0 & 2 & 2 & 2 \\
14 & 1 & 0 & 2 & 2 & 0 & 2 & 2 & 0 & 0 & 2 & 2 & 2 & 2 & 0 & 2 & 2 & 2 & 0 & 0 & 2 \\
15 & 1 & 2 & 0 & 2 & 2 & 0 & 2 & 0 & 2 & 0 & 0 & 0 & 2 & 2 & 0 & 0 & 2 & 0 & 2 & 0 \\
16 & 1 & 2 & 2 & 0 & 2 & 2 & 2 & 2 & 2 & 0 & 0 & 2 & 0 & 2 & 0 & 2 & 2 & 2 & 2 & 0 \\
17 & 1 & 0 & 2 & 2 & 0 & 0 & 0 & 0 & 2 & 0 & 2 & 2 & 2 & 2 & 2 & 0 & 0 & 0 & 2 & 0 \\
18 & 1 & 2 & 0 & 2 & 0 & 0 & 0 & 2 & 2 & 2 & 0 & 0 & 0 & 0 & 2 & 0 & 0 & 2 & 2 & 0 \\
19 & 1 & 2 & 2 & 2 & 0 & 0 & 2 & 0 & 0 & 2 & 0 & 0 & 0 & 2 & 2 & 0 & 2 & 0 & 2 & 0 \\
20 & 1 & 0 & 0 & 2 & 0 & 2 & 2 & 0 & 2 & 2 & 0 & 0 & 2 & 0 & 2 & 2 & 2 & 2 & 2 & 0 \\
\multicolumn{21}{c}{~~~~} \\
\end{tabular}
\end{center}

\caption{Iterated differences $d_k (n)$ for $0 \le k \le 20$, $1 \le n \le 20$.}
\end{table}
\clearpage
\begin{table}
\begin{center}
\begin{tabular}{c|c|c}
$x$ & $\pi (x)$ & $G( \pi (x))$ \\ \hline
~~ \\ [-.09in]
$10^2$ & 25 & 5 \\
$10^3$ & 168 & 15 \\
$10^4$ & 1,229 & 35 \\
$10^5$ & 9,592 & 65 \\
$10^6$ & 78,498 & 95 \\
$10^7$ & 664,579 & 135 \\
$10^8$ & 5,761,455 & 175 \\
$10^9$ & 50,847,534 & 248 \\
$10^{10}$ & 455,052,511 & 329 \\
$10^{11}$ & 4,118,054,813 & 417 \\
$10^{12}$ & 37,607,912,018 & 481 \\
$10^{13}$ & 346,065,536,839 & 635 \\
\multicolumn{3}{c}{~~~}
\end{tabular}
\end{center}

\caption{Smallest $k$ such that $d_k (n) =0,1$, or 2 for all $n < \pi (x)$.}
\end{table}

\begin{table}
\begin{center}
\begin{tabular}{c|c}
$N$ & Average of $g(n)$ \\ \hline
~~ \\ [-.09in]
$10^8$ & 22.1 \\
$10^{10}$ & 27.0 \\
$10^{12}$ & 32.8 \\
\multicolumn{2}{c}{~~~}
\end{tabular}
\end{center}

\caption{Average values of $g(n)$ for $n$ near $N$.}
\end{table}

\begin{table}
$$
\begin{array}{c|c}
\multicolumn{1}{c}{k} & \multicolumn{1}{c}{\mbox{average of $d_k (n)$}} \\ \hline
~~ \\ [-.09in]
~~1 & 27.66 \\
~~2 & 25.51 \\
~~3 & 19.63 \\
~~4 & 19.69 \\
~~5 & 13.50 \\
~ & ~ \\
~10 & ~8.33 \\
~20 & ~4.93 \\
~50 & ~1.76 \\
100 & ~1.15 \\
150 & ~1.01 \\
\multicolumn{2}{c}{~~~}
\end{array}
$$

\caption{Average values of $d_k (n)$ for various $k$, averaged
over $289182$ values of $n$ near $\pi (10^{12} )$.}
\end{table}
\clearpage
\begin{figure}
\caption{Differences $d_1 (n)$ for $10^4$ primes near $10^{12}$.}
\end{figure}

\begin{figure}
\caption{Differences $d_{50} (n)$ for $10^4$ primes near $10^{12}$.}
\end{figure}

\begin{figure}
\caption{Differences $d_{100} (n)$ for $10^4$ primes near $10^{12}$.}
\end{figure}
\end{document}
