> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/odlyzko-1993-iterated-differences-latex-source.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

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

*[excerpt ends; 19219 characters not shown — see `research/sources/odlyzko-1993-iterated-differences-latex-source.full.md`]*
