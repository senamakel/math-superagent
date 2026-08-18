<!-- source: https://doi.org/10.1007/s11227-025-07337-0 | converted from HTML -->

Improved verification limit for the convergence of the Collatz conjecture | The Journal of Supercomputing | Springer Nature Link

Skip to main content

# Improved verification limit for the convergence of the Collatz conjecture

- [Open access][1]
- Published: 02 May 2025

- Volume 81, article number 810 ( 2025)
- Cite this article

You have full access to this [open access][1] article

[Download PDF][2]

[Save article][3]

[View saved research][4]

[The Journal of Supercomputing][5] [Aims and scope][6] [Submit manuscript][7]

Improved verification limit for the convergence of the Collatz conjecture

[Download PDF][2]

## Abstract

This article presents our project, which aims to verify the Collatz conjecture computationally. As a main point of the article, we introduce a new result that pushes the limit for which the conjecture is verified up to \(2^{71}\). We present our baseline algorithm and then several sub-algorithms that enhance acceleration. The total acceleration from the first algorithm we used on the CPU to our best algorithm on the GPU is \(1\,335\times\). We further distribute individual tasks to thousands of parallel workers running on several European supercomputers. Besides the convergence verification, our program also checks for path records during the convergence test. We found four new path records.

### Similar content being viewed by others

### [Convergence verification of the Collatz problem][8]

Article 01 July 2020

### [Observations from Parallelising Three Maximum Common (Connected) Subgraph Algorithms][9]

Chapter © 2018

### [Computational Errors of the Extragradient Method for Equilibrium Problems][10]

Article 16 May 2018

### Explore related subjects

Discover the latest articles, books and news in related subjects, suggested using machine learning.

- [Algorithms][11]
- [Computability and Recursion Theory][12]
- [Computational Complexity][13]
- [Computational Number Theory][14]
- [Mathematics and Computing][15]
- [Optimization][16]
- [Parallel Metaheuristics in Optimization Problems][17]

## 1 Introduction

Collatz conjecture is one of the simplest unsolved problems in mathematics. It deals with iterations of the number theoretic function, which takes an odd integer *n*to \(3n+1\) and an even *n*to *n*/2. The conjecture asserts that iterations of this function starting at arbitrary positive number *n*always lead to the number 1. Jeffrey Lagarias, the famous mathematician, stated that the Collatz conjecture "is an extraordinarily difficult problem, completely out of reach of present-day mathematics" [[1][18]]. There is an extensive literature on this conjecture. Preprints [[2][19]] and [[3][20]] provide an overview of such papers.

Because the output of \(3n+1\) branch is even for odd *n*and therefore *n*/2 step must follow, we can replace this branch by \((3n+1)/2\). The Collatz conjecture now asserts that a sequence defined by repeatedly applying the function

$$\begin{aligned} T(n)&= {\left\{ \begin{array}{ll} (3n + 1) / 2, & \text {for odd }n,\\ n / 2, & \text {for even }n,\\ \end{array}\right. } \end{aligned}$$

(1)

always converges to the cycle passing through the number 1 for arbitrary positive integer *n*. The conjecture has never been proven. There is, however, experimental evidence and heuristic arguments that support it. At the time of writing this article, all starting values up to \(2^{68}\) were computer-checked [[4][21]]. This paper presents a result that pushes this limit to \(2^{71}\).

We have created a distributed heterogeneous computing system that sequentially tests all integers and thus pushes the boundary beyond which the Collatz conjecture is explored. The system runs on supercomputers in Europe and consists of thousands of parallel workers to which work is centrally assigned. Workers compute their tasks either on the CPU or on the GPU. This paper describes the architecture and development of this system.

The rest of the paper is organized as follows. Section [2][22] reviews related work, especially competitive projects and the results achieved so far. Section [3][23] explains all the algorithms we used in the convergence verification. Section [4][24] deals with the distribution of individual tasks to thousands of parallel workers. Section [5][25] provides a performance evaluation of the algorithms from Sect. [3][23]. Section [6][26] presents the achieved results. Finally, Sect. [7][27] concludes the paper.

## 2 Related work

Several current or past projects seek to disprove or verify the Collatz conjecture. Convergence addresses the question of whether all initial numbers tested will eventually reach the value 1. We focus on the projects that check for the convergence of the conjecture for all numbers up to some upper bound. The path records are starting values that set new records for the highest point of trajectory before reaching 1. The programs that check for convergence usually also collect path records. The question is how far the Collatz conjecture has been computationally verified and how fast (numbers per second) the methods in such projects are. The measure numbers per second means the number of initial numbers verified per second, which does include numbers that are not checked at all.

As the first tracked record, in 1973, Dunn [[5][28]] verified the convergence below approximately \(2^{24.78}\). In 1992, Leavens and Vermeulen [[6][29]] verified the convergence for all numbers below approximately \(2^{45.67}\).

Before 2012, Eric Roosendaal [[7][30]] checked all numbers up to \(2^{60}\) on the CPUs. Meanwhile, Tomás Oliveira e Silva [[8][31]] checked the numbers up to \(5 \times 2^{60}\) using a different software/hardware. Up to that moment, Tomás Oliveira e Silva and Eric Roosendaal alternated in the lead. According to information published on Oliveira e Silva’s website, the speed of his program was about \(2^{31}\) numbers per second on computers at that time. Eric Roosendaal estimates the theoretical speed of his algorithm on GPU as approximately \(2^{38.86}\) numbers per second. However, this is a projected speed; no such program exists.

In 2017, the yoyo@home project [[9][32]] checked for convergence of all numbers up to \(87 \times 2^{60}\). Their CPU code checked about \(2^{35.48}\) numbers per second and core. 1 000 volunteers participated in the project, and each number was independently checked twice.

Also, in 2017, Honda et al. [[10][33]] claimed they can check \(2^{40.25}\) numbers per second on the GPU. Their program is, however, only able to verify 64-bit numbers.

From 2019 to 2021, our project [[4][21]] verified the convergence of all numbers below \(2^{68}\). We used CPUs as well as GPUs along with the power of supercomputers. Our CPU implementation achieved a speedup to \(2^{31.97}\) numbers/second, whereas the speed on GPUs reached the limit of \(2^{37.68}\) numbers/second. Both implementations can check 128-bit numbers. This article is a continuation of our previous work.

Unlike [[4][21]], the implementation of sieves in this paper is much more sophisticated (and thus faster). Unlike [[4][21]], we compared many sieve sizes and different settings, and the results are given in Sect. [5][25]. The contributions of this paper include (a) introduction of \(3^k\) sieves and optimized code for the sieve of the size of \(3^2\) (Sect. [3.2][34]), (b) extending the algorithm to a distributed environment (Sect. [4][24]), (c) comparison of different algorithms under different settings (Sect. [5][25]), (d) publishing the result where the project verified all numbers below \(2^{71}\) (Sect. [6][26]). My motivation was to push the limit to which the Collatz conjecture is verified, and possibly find a counterexample.

## 3 Algorithms

This section will explain all the algorithms we used in the convergence testing. Primarily, the same algorithms are used on both CPU and GPU. Another issue is distributing convergence testing across multiple computers, which we will cover in the next section.

### 3.1 Baseline testing

The baseline testing is an algorithm by which the iterations of the Collatz function are calculated. The first thing that comes to mind is to use Eq. ( [1][35]) directly. Indeed, we can formulate a naive convergence verification algorithm, as listed in Algorithm 1. The \(\langle n \rangle _2\) is the result of *n*modulo 2 operator. The algorithm tests the numbers in ascending order. This way, we can stop testing when *n*drops below the initial value \(n_0\) (since all numbers below were already tested). In more detail, the algorithm tests a single number and thus has to be repeated on each number independently, from the smallest to the largest one.

**Algorithm 1**

[image: Algorithm 1]

[Full size image][36]

Naive algorithm

In [[4][21]], we tracked *T*(*n*)-trajectory on \(n + 1\) rather than directly on *n*. The trick is that when the function calculating *T*(*n*) iterates, we switch between *n*and \(n + 1\) to always use only multiplication with no additive operation. For example, the trajectory on *n*of 12 is (6, 3, 5, 8, 4, 2, 1), whereas on \(n + 1\), the same trajectory is (7, 4, 6, 9, 5, 3, 2). We use the \(\operatorname {ctz}\) operation, which counts the number of trailing zero bits following the least significant nonzero bit, and then perform multiple divisions by two and multiple multiplications by three at once (for details see [[4][21]]). Thus, we merge several even as well as odd steps into single ones. Moreover, the powers of three can be precomputed in a small look-up table, and these multiplications can be performed using a single multiplication. In other words, combining a number of *k*consecutive even steps leads to \(a 2^k \longrightarrow a\), and combining a number of *k*consecutive odd steps leads to \(a 2^k - 1 \longrightarrow a 3^k - 1\). Thus, if the binary representation of a number ends in *k*zeros, we have the first case, and if it ends in *k*ones, the second one. The procedure is listed in Algorithm 2. One can verify that for odd *n*, the average number of iterates computed in a single step for Algorithm 2 is 4.

For those for which it is not obvious that a number with *k*trailing zeros in its binary representation will result in *k*consecutive odd steps, we offer another perspective on the matter. Rather than defining the *T*(*n*) as in ( [1][35]), and tracking the trajectory directly on *n*, we can track the same trajectory on \(n+1\) with the auxiliary function

$$\begin{aligned} T_1(n) = {\left\{ \begin{array}{ll} (n+1)/2 & \quad \text { if }n \equiv 1 \pmod {2}, \\ 3n/2 & \quad \text { if }n \equiv 0 \pmod {2}. \end{array}\right. } \end{aligned}$$

(2)

Thus, the multiplying by 3 just moved to the even branch. The trick is that when calculating the function iterates, our algorithm switches between *n*and \(n+1\) in such a way that we always use only the even branch of either *T*or \(T_1\). Therefore, the above functions can be expressed as

$$\begin{aligned} T(n) = {\left\{ \begin{array}{ll} T_1(n+1)-1 & \quad \text { if }n \equiv 1 \pmod {2}, \\ n/2 & \quad \text { if }n \equiv 0 \pmod {2}, \end{array}\right. } \end{aligned}$$

(3)

and

$$\begin{aligned} T_1(n) = {\left\{ \begin{array}{ll} T(n-1)+1 & \quad \text { if }n \equiv 1 \pmod {2}, \\ 3n/2 & \quad \text { if }n \equiv 0 \pmod {2}. \end{array}\right. } \end{aligned}$$

(4)

So, by suitably switching these two equations, we can always use the \(\operatorname {ctz}\) operation and perform several steps at once. Therefore, we can perform several \((3n+1)\) steps at once.

**Algorithm 2**

[image: Algorithm 2]

[Full size image][37]

New algorithm used in [[4][21]]

Comparison with the baseline testing algorithm, where the time is given per a work unit of the size of \(2^{30}\), gives us 8.8976 s for Algorithm 1 and 5.7024 s for Algorithm 2. This quick comparison reveals that Algorithm 2 is about 36 % faster. The results were obtained on a 3.0 GHz CPU (AMD Ryzen Threadripper 2990WX). For this reason, we decided to optimize further only Algorithm 2.

### 3.2 Sieve \(3^k\)

Imagine the following step on numbers of the form \(2n+1\) (odd numbers).

$$\begin{aligned} 2n + 1 \rightarrow \frac{3(2n + 1) + 1}{2} = 3n + 2 \end{aligned}$$

(5)

Notice that \(3n + 2 > 2n + 1\), and the algorithm tests the numbers in ascending order. This step tells us that there is no need to test numbers of the form \(3n+2\) because it was already tested in the \(2n+1\) test. This will allow us to reduce the number of tested values by 33.33 %. We call this optimization modulo 3 sieving. The same procedure can be used for the initial numbers of the general form \(3^k n + m\). For example, using \(3^2\) sieve, the percentage of eliminated initial numbers is 44.44 %. However, higher \(3^k\) sieves bring almost no acceleration (for \(3^6 = 729\) the percentage is only 45.95 %). Table [1][38] summarizes the percentage of sieves up to \(3^6\). Note that there is no improvement between \(3^2\) and \(3^3\) sieves.

**Table 1 Residues modulo \(3^k\) and percentage of initial values eliminated by this sieve**

[Full size table][39]

Using a \(3^k\) sieve is a time-critical operation. Therefore, much optimization was devoted to it. For example, the following piece of code tests whether an initial number passes the \(3^2\) sieving. It is based on the identity \(2^{60} \equiv 1 \pmod {9}\). The problem is how to calculate modulo 9 from the 128-bit data type using only the 64-bit type. Since we know that \(2^{60} \equiv 1 \pmod {9}\), we can shift the number 60 bits to the right (from position \(2^{60}\) to position 1). This is how we break a 128-bit data type into several 64-bit ones. We then simply call the modulo operation on a 64-bit data type.

[image: figure c]

### 3.3 Sieve \(2^k\)

Let \(T^k\) denote the *k*th iteration of the function *T*. The general form [[11][40]] of \(T^k(n)\) is

$$\begin{aligned} T^k(2^k n_H + n_L) = 3^{\operatorname {odd}(n_L)} n_H + T^k(n_L), \end{aligned}$$

(6)

where \(\operatorname {odd}(n_L)\) is the number of odd steps of *T*(*n*) that were taken in the computation of \(T^k(n_L)\). We basically split *n*as \(n = 2^k n_H + n_L\), i.e., *k*lowest significant bits (least significant bits) along with the rest of the high significant bits. Competitive programs use this equation to perform *k*steps at once (two tables have the size of \(2^k\) entries, and indices correspond to \(n_L\)). However, we used this acceleration technique to build a large sieve (the size of the sieve is \(2^k\) bits). Using the sieve, we test only those numbers that (a) do not converge or (b) join the path of a lower number in *k*steps. This is the reason why the entry of such a sieve is just one bit ( \(2^k\) bits in total). As might be expected, the acceleration obtained from this method is significant.

For those who find the above explanation unclear, we offer a slightly simpler view of the matter. Look at Equation ( [6][41]). It gives you a way to calculate *k*iterations of a *T*(*n*) function at once. On the left side, you see \(T^k(2^k n_H + n_L)\), which means that to calculate *k*iterations, we have to split the number into two parts \(n = 2^k n_H + n_L\). For all \(n_L\) we precalculate (a) \(\operatorname {odd}(n_L)\) and (b) \(T^k(n_L)\). Now we can jump *k*steps forward just using two pre-calculated tables. It holds that \(0 \le n_L < 2^k\). Now the question is whether the initial value is greater than the value on the right side of ( [6][41]), formally \(n_H 3^{\operatorname {odd}(n_L)} + T^k(n_L) < 2^k n_H + n_L\) for all \(n_H > 0\). If the answer is yes, the ending number drops below the starting number, and we can end the verification. This is the principle of the \(2^k\) sieve.

### 3.4 Solving congruence classes concurrently

Our CPU and GPU programs can concurrently verify \(2^{k}\) (*k*matches the sieve size) numbers of the same congruence class. This mainly means that the program verifies the work units having the size of \(2^{\text {task size}}\) numbers and solves the lowest *k*bits at once, where \(k < \text {task size}\). After *k*least significant bits, the code paths diverge. This results in a verification of individual numbers up to \(2^{\text {task size}}\).

For example, consider Algorithm 2. The concurrent algorithm solves a class of \(2^k\) numbers having *k*least significant bit in common. The \(2^k\) sieve is applied before the concurrent algorithm starts (note that the lowest *k*bits are the index into the \(2^k\) sieve). In contrast, the \(3^k\) sieve is applied when solving bits greater than *k*.

## 4 Distributed computing

This section deals with distributing individual tasks to thousands of concurrent workers. All the algorithms described in the previous section are implemented for the CPU and GPU and referred to as the worker. The GPU code is written in OpenCL (both NVIDIA and AMD are supported), whereas the CPU code is written in C. The code uses 128-bit integer compiler extensions. The CPU worker uses the GMP library to resolve computation above 128 bits (for arbitrary precision arithmetic).

All \(\alpha\) s (see Algorithm 2) that occurred during the convergence test of the range are summed together to raise the checksum (proof of work). These checksums are recorded on the server. The maximum value of \(n_{\text {max}}\) that occurred during the convergence test for a given interval is also detected and recorded on the server. Our implementation can verify work units of \(2^{\text {task size}} = 2^{40}\) 128-bit numbers. We experimented with several values for task size. The selected value turned out to be small enough to be processed in a maximum of a few hours on conventional CPUs and large enough to allow such units to be managed by a regular server. The server manages \(2^{32}\) work units, which allows up to \(2^{72}\) numbers to be explored. A record of each work unit occupies 322 bits on the server (161 gigabytes for the whole \(2^{32}\) space). The data is stored in these 322 bits comprising a calculation time, number of 128-bit overflows, offset of maximum value encountered in the calculation, checksum, client ID, and some bit flags.

Table [2][42] provides examples of ranges that are calculated by every worker from task id.

**Table 2 Ranges of numbers for workers depending on task id. Ranges are expressed using hexadecimal numbers**

[Full size table][43]

**Fig. 1**

[image: Fig. 1]

[Full size image][44]

An architecture of the distributed computing project. The numbers indicate the multiplicity of individual boxes. The server always runs in a single instance

The architecture of our project is shown in Fig. [1][45]. It consists of three components—the server, clients, and workers. The server runs in a single instance in our university’s infrastructure. Clients are run by job scheduling systems (PBS, TORQUE, SGE, Slurm) in the infrastructure of various supercomputers in Europe. A single computing node can host a single client or several clients. Clients are multi-threaded and can serve several CPU or GPU workers. Clients spawn workers and correspond to individual CPU cores or GPUs.

The server and clients run on different computers. They communicate with each other using the TCP/IP protocol. The communication protocol has been specially designed to have low latency (all client-to-server requests precede server-to-client responses). Individual requests that the server can serve include Request Assignment, Request Lowest Incomplete Assignment, Return Assignment, Interrupt Assignment, Request Multiple Assignments, and others.

Conversely, the client and workers run on the same computer. They communicate with each other via the worker’s standard output (stdout). For these purposes, we have developed an extensive text protocol. Messages in this log include the time elapsed while solving the work unit, checksum, the initial value for the maximum value reached during the solution of the work unit, the sequence number of the work unit (task id), and others.

This whole system can serve thousands of workers working simultaneously. It uses various supercomputers for this. MetaCentrum operates and manages distributed computing infrastructure consisting of computing resources owned by CESNET (an association of universities of the Czech Republic and the Czech Academy of Sciences) in the Czech Republic. IT4Innovations National Supercomputing Center operates the most powerful supercomputing systems in the Czech Republic. At present, IT4Innovations runs three supercomputers, including the Czech most powerful supercomputer, Karolina. The LUMI supercomputer is the most powerful supercomputing system in Europe (and, at the time we were solving our project, third most powerful in the world). A few examples of how powerful the system can be are shown in Table [3][46]. MetaCentrum supercomputer provides up to 2 000 CPUs cores, whereas Karolina provides 128 cores per node (AMD Zen 2 EPYC 7H12), and finally LUMI supercomputer provides eight AMD MI250X GPUs per node.

**Table 3 Supercomputers used in the computational verification of the Collatz conjecture. WU/sec stands for work units per second. Measured at the end of May 2023**

[Full size table][47]

Notice in Table [3][46] that the resulting performance is massively higher when GPUs are included compared to the CPU-only situation. During our verification, we consumed 12 395 CPU-years (average time per solving a single work unit is 6 min and 25 s) and 159 GPU-years (average time is 7 s). This includes even very slow machines. The typical average duration at the time of writing is much lower.

Someone might be interested in how individual assignments are distributed to workers. Each client asks the server to allocate a range to search. The server allocates the smallest unassigned range and sends it to the client. The client then passes the range to the worker (workers can occupy one CPU core or one GPU). Since multiple workers can run in parallel (multiple threads, or multiple GPUs) on a single computing node, each client actually requests several ranges and distributes them to multiple workers.

## 5 Evaluation

This section provides a performance evaluation of the algorithms from Sect. [3][23]. The comparison is performed on AMD Ryzen Threadripper 2990WX and NVIDIA GeForce RTX 2080 Ti. The evaluation starts with comparing \(2^k\) sieve sizes and \(2^k\) sieve compression. Then, we evaluate the benefit of \(3^k\) sieves. Finally, we deal with processing congruence classes concurrently. In all cases, we use a work unit of the size of \(2^{40}\) (the time is given per \(2^{40}\) numbers). The only evaluation metric is time given in seconds. At the end of the section, we also mention the speed-up factor. The paper evaluates these techniques: using a \(2^k\) sieve, solving congruence classes concurrently, and using a \(3^k\) sieve.

We experimented with many sieve sizes and concluded that the sieve size \(2^{34}\) is optimal for the CPU implementation, while the size \(2^{24}\) is optimal for GPUs. See Table [4][48] a and b. Note that \(2^{34}\) bits equals 2 gigabytes. So, the consequence is a huge memory footprint. However, we have found that these sieves are formed by several constantly repeated bit patterns. More precisely, such sieves are formed by only fifty constantly repeated 64-bit patterns (which can be stored using indices in a small look-up table). In our project, we use 8-bit indices. However, the compression ratio can reach the value of around 1:10 if 64-bit patterns are represented by a 6-bit index.

**Table 4 Comparison of sieve sizes. The best result is in bold**

[Full size table][49]

Now, we compare the benefits of the \(2^k\) sieve compression using a look-up table. The comparison is shown in Table [5][50] a and b. On the CPU, we can see that as the sieve size increases, the compression becomes less and less effective. In the case of \(2^{24}\) sieve, the speedup is about 3 %, whereas in the case of \(2^{34}\) sieve the speedup is zero. However, we must realize that compression also saves disk space (1:8 ratio) and allows files to be copied to computing nodes faster. Without compression, large sieves could not be distributed to computing nodes. On the GPU, the compression provides speedup using \(2^{32}\) sieve. However, \(2^{24}\) sieve is faster; compression does not help here.

Without compression, it is possible to distribute the \(2^{32}\) sieve to the CPU clients. The compression enables the distribution of the \(2^{34}\) sieve. From Table [4][48] a, the speedup is about 4 %.

**Table 5 Speed comparison of an enabled/disabled sieve compression. The best result is in bold**

[Full size table][51]

We also compare the efficiency of \(3^k\) sieves. See Table [6][52]. \(2^{34}\) sieve is used on the CPU, while \(2^{24}\) sieve is used on the GPU. The CPU computes the same congruence classes concurrently. We can see that \(3^k\) sieves bring some acceleration. On the CPU, it is purely about the number of reduced initial numbers. On the GPU, a \(3^2\) sieve seems to be breaking thread convergence; \(3^1\) is slightly faster.

**Table 6 Efficiency comparison of \(3^k\) sieves. \(2^k\) sieve compression was disabled in all cases. The best result is in bold**

[Full size table][53]

As another evaluation point, we compare the efficiency of computing the same congruence classes concurrently. The comparison is given in Table [7][54] a and b. The time is given per a work unit of the size of \(2^{40}\), and sieve \(3^2\) is used. Overflow means the ulong data type (OpenCL) is insufficient for intermediate calculations. It can be seen that, on the CPU, this algorithm brings a massive speedup (e.g., \(3.27\times\) for sieve \(2^{34}\)). The situation on GPUs is the opposite; the algorithm does not bring any acceleration.

**Table 7 Speed comparison of an enabled/disabled concurrently solving congruence classes. The best result is in bold**

[Full size table][55]

We now look at how much cumulative speedup each algorithm brings. See corresponding Tables [8][56] and [9][57]. The baseline algorithm also computes the checksum and maximum value reached during the computation. The baseline algorithm is Algorithm 2. Showing the speedup over Algorithm 1 would not be fair because it is not implemented in an optimized form. The tables mentioned above show that the best GPU implementation is \(52.1\times\) faster than the best CPU implementation. The total speedup from the first algorithm we started with on the CPU to our best algorithm on the GPU is \(1\,335.9\times\).

**Table 8 Overall comparison on the CPU**

[Full size table][58]

**Table 9 Overall comparison on the GPU**

[Full size table][59]

## 6 Results

At the time of writing this article, we have managed to verify the convergence of the Collatz conjecture for all numbers up to the limit of \(2^{71}\) (which is equal to \(2\,048 \times 2^{60}\)). This is the moment when the length of a non-trivial cycle rises to 355 504 839 929 [[12][60]]. See Table [10][61] for a timeline from the start of our project.

**Table 10 Timeline of our project verifying the convergence of the Collatz conjecture**

[Full size table][62]

The *n*is called the path record if, for all \(m < n\), the inequality \(t(m) < t(n)\) holds, where *t*(*n*) is the highest number occurring in the sequence starting at *n*. During the verification, we found five new path records (sequence A006884 in The On-Line Encyclopedia of Integer Sequences). The initial values for path records are

-

274 133 054 632 352 106 267,

-

1 378 299 700 343 633 691 495,

-

1 735 519 168 865 914 451 271,

-

1 765 856 170 146 672 440 559, and

-

2 358 909 599 867 980 429 759.

Lagarias and Weiss [[13][63]] predicted using the large deviation theory for random walks that the highest number occurring in the sequence for a path record *n*grows like \(n^2\). The results recorded up to \(2^{71}\) agree with this prediction.

To allow other developers and scientists to benefit from this work and build on it, the programs used in this article have been released as open-source software. Footnote 1

## 7 Conclusion

This article presents our project aiming to computationally verify the convergence of the Collatz conjecture. In our previous article, in 2020, we verified the convergence up to the limit \(2^{68}\). This paper presents a result that further pushes this limit to \(2^{71}\).

We presented several sub-algorithms that bring some acceleration to our baseline algorithm. The paper further dealt with the distribution of individual tasks to thousands of parallel workers. While doing so, our system runs on several supercomputers in Europe. The workers compute their tasks either on the CPU or on the GPU. On GPU, the code is written in OpenCL, and both NVIDIA and AMD cards are supported.

We further evaluated our algorithms and found that our best GPU implementation is \(52\times\) faster than our best CPU implementation. The total speedup from the first algorithm we used several years ago on the CPU to our best algorithm today on the GPU is \(1\,335\times\).

## Notes

1.

[https://github.com/xbarin02/collatz][64], commit 53c2a06.

## References

1.

Lagarias JC (ed) (2010) The Ultimate Challenge: The 3x + 1 Problem. American Mathematical Society

2.

Lagarias JC (2003) The \(3x+1\) problem: An annotated bibliography (1963–1999) (sorted by author). [arXiv:math/0309224][65]

3.

Lagarias JC (2006) The \(3x+1\) problem: An annotated bibliography, II (2000-2009). [arXiv:math/0608208][66]

4.

Barina D (2021) Convergence verification of the Collatz problem. J Super Comput 77(3):2681–2688. [https://doi.org/10.1007/s11227-020-03368-x][67]

[Article][68] [Google Scholar][69]

5.

Dunn R (1973) On Ulam’s Problem. University of Colorado at Boulder, Tech. rep

[Google Scholar][70]

6.

Leavens GT, Vermeulen M (1992) 3x+1 Search programs. Comput Math Appl 24(11):79–99. [https://doi.org/10.1016/0898-1221(92)90034-F][71]

[Article][72] [MathSciNet][73] [MATH][74] [Google Scholar][75]

7.

Roosendaal E (2019) personal communication

8.

Oliveira e Silva T (2010) Empirical verification of the 3x+1 and related conjectures. In: Lagarias JC (ed) The Ultimate Challenge: The 3x+1 Problem. American Mathematical Society, pp 189–207

9.

Hercher C (2018) Über die Länge nicht-trivialer Collatz-Zyklen. Die Wurzel 6 and 7

10.

Honda T, Ito Y, Nakano K (2017) GPU-accelerated exhaustive verification of the Collatz conjecture. Int J Netw Comput 7(1):69–85

[Google Scholar][76]

11.

Silva TOE (1999) Maximum excursion and stopping time record-holders for the \(3x+1\) problem: computational results. Math Comput 68(225):371–384. [https://doi.org/10.1090/S0025-5718-99-01031-5][77]

[Article][78] [MathSciNet][79] [MATH][80] [Google Scholar][81]

12.

Hercher C (2023) There are no Collatz \(m\) -cycles with \(m \le 91\). J Integer Seq 26(3):1–22

[MathSciNet][82] [MATH][83] [Google Scholar][84]

13.

Lagarias JC, Weiss A (1992) The \(3x + 1\) problem: two stochastic models. Annals Appl Probab 2(1):229–261. [https://doi.org/10.1214/aoap/1177005779][85]

[Article][86] [MathSciNet][87] [MATH][88] [Google Scholar][89]

[Download references][90]

## Acknowledgements

Computational resources were provided by the e-INFRA CZ project (ID:90254), supported by the Ministry of Education, Youth and Sports of the Czech Republic.

## Funding

Open access publishing supported by the institutions participating in the CzechELib Transformative Agreement.

## Author information

### Authors and Affiliations

1.

Faculty of Information Technology, Brno University of Technology, Bozetechova 1/2, Brno, Czech Republic

David Barina

Authors

1. David Barina

[View author publications][91]

Search author on: [PubMed][92] [Google Scholar][93]

### Corresponding author

Correspondence to [David Barina][94].

## Additional information

### Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Rights and permissions

**Open Access**This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/][95].

[Reprints and permissions][96]

## About this article

[image: Check for updates. Verify currency and authenticity via CrossMark] [97]

### Cite this article

Barina, D. Improved verification limit for the convergence of the Collatz conjecture. *J Supercomput***81**, 810 (2025). https://doi.org/10.1007/s11227-025-07337-0

[Download citation][98]

-

Accepted: 21 April 2025

-

Published: 02 May 2025

-

Version of record: 02 May 2025

-

DOI: https://doi.org/10.1007/s11227-025-07337-0

### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative

### Keywords

- [Collatz conjecture][99]
- [Software optimization][100]
- [Parallel computing][101]
- [Number theory][102]

### Profiles

1. David Barina [View author profile][103]


## Links

[1]: https://www.springernature.com/gp/open-science/about/the-fundamentals-of-open-access-and-open-research
[2]: /content/pdf/10.1007/s11227-025-07337-0.pdf
[3]: /article/10.1007/s11227-025-07337-0/save-research?_csrf=ju3oN1HXrHBpO3iboV3FoPgFSBWEsok-
[4]: /saved-research
[5]: /journal/11227
[6]: /journal/11227/aims-and-scope
[7]: https://submission.nature.com/new-submission/11227/3
[8]: https://link.springer.com/10.1007/s11227-020-03368-x?fromPaywallRec=false
[9]: https://link.springer.com/10.1007/978-3-319-93031-2_22?fromPaywallRec=false
[10]: https://link.springer.com/10.1007/s40840-018-0632-y?fromPaywallRec=false
[11]: /subjects/algorithms
[12]: /subjects/computability-and-recursion-theory
[13]: /subjects/computational-complexity
[14]: /subjects/computational-number-theory
[15]: /subjects/mathematics-and-computing
[16]: /subjects/optimization
[17]: /subjects/parallel-metaheuristics-in-optimization-problems
[18]: /article/10.1007/s11227-025-07337-0#ref-CR1
[19]: /article/10.1007/s11227-025-07337-0#ref-CR2
[20]: /article/10.1007/s11227-025-07337-0#ref-CR3
[21]: /article/10.1007/s11227-025-07337-0#ref-CR4
[22]: /article/10.1007/s11227-025-07337-0#Sec2
[23]: /article/10.1007/s11227-025-07337-0#Sec3
[24]: /article/10.1007/s11227-025-07337-0#Sec8
[25]: /article/10.1007/s11227-025-07337-0#Sec9
[26]: /article/10.1007/s11227-025-07337-0#Sec10
[27]: /article/10.1007/s11227-025-07337-0#Sec11
[28]: /article/10.1007/s11227-025-07337-0#ref-CR5
[29]: /article/10.1007/s11227-025-07337-0#ref-CR6
[30]: /article/10.1007/s11227-025-07337-0#ref-CR7
[31]: /article/10.1007/s11227-025-07337-0#ref-CR8
[32]: /article/10.1007/s11227-025-07337-0#ref-CR9
[33]: /article/10.1007/s11227-025-07337-0#ref-CR10
[34]: /article/10.1007/s11227-025-07337-0#Sec5
[35]: /article/10.1007/s11227-025-07337-0#Equ1
[36]: /article/10.1007/s11227-025-07337-0/figures/a
[37]: /article/10.1007/s11227-025-07337-0/figures/b
[38]: /article/10.1007/s11227-025-07337-0#Tab1
[39]: /article/10.1007/s11227-025-07337-0/tables/1
[40]: /article/10.1007/s11227-025-07337-0#ref-CR11
[41]: /article/10.1007/s11227-025-07337-0#Equ6
[42]: /article/10.1007/s11227-025-07337-0#Tab2
[43]: /article/10.1007/s11227-025-07337-0/tables/2
[44]: /article/10.1007/s11227-025-07337-0/figures/1
[45]: /article/10.1007/s11227-025-07337-0#Fig1
[46]: /article/10.1007/s11227-025-07337-0#Tab3
[47]: /article/10.1007/s11227-025-07337-0/tables/3
[48]: /article/10.1007/s11227-025-07337-0#Tab4
[49]: /article/10.1007/s11227-025-07337-0/tables/4
[50]: /article/10.1007/s11227-025-07337-0#Tab5
[51]: /article/10.1007/s11227-025-07337-0/tables/5
[52]: /article/10.1007/s11227-025-07337-0#Tab6
[53]: /article/10.1007/s11227-025-07337-0/tables/6
[54]: /article/10.1007/s11227-025-07337-0#Tab7
[55]: /article/10.1007/s11227-025-07337-0/tables/7
[56]: /article/10.1007/s11227-025-07337-0#Tab8
[57]: /article/10.1007/s11227-025-07337-0#Tab9
[58]: /article/10.1007/s11227-025-07337-0/tables/8
[59]: /article/10.1007/s11227-025-07337-0/tables/9
[60]: /article/10.1007/s11227-025-07337-0#ref-CR12
[61]: /article/10.1007/s11227-025-07337-0#Tab10
[62]: /article/10.1007/s11227-025-07337-0/tables/10
[63]: /article/10.1007/s11227-025-07337-0#ref-CR13
[64]: https://github.com/xbarin02/collatz
[65]: https://arxiv.org/pdf/math/0309224
[66]: https://arxiv.org/pdf/math/0608208
[67]: https://doi.org/10.1007/s11227-020-03368-x
[68]: https://link.springer.com/doi/10.1007/s11227-020-03368-x
[69]: http://scholar.google.com/scholar_lookup?amp;title=Convergence%20verification%20of%20the%20Collatz%20problem&amp;journal=J%20Super%20Comput&amp;doi=10.1007%2Fs11227-020-03368-x&amp;volume=77&amp;issue=3&amp;pages=2681-2688&amp;publication_year=2021&amp;author=Barina%2CD
[70]: http://scholar.google.com/scholar_lookup?amp;title=On%20Ulam%E2%80%99s%20Problem&amp;publication_year=1973&amp;author=Dunn%2CR
[71]: https://doi.org/10.1016/0898-1221(92)90034-F
[72]: https://doi.org/10.1016%2F0898-1221%2892%2990034-F
[73]: http://www.ams.org/mathscinet-getitem?mr=1186722
[74]: http://www.emis.de/MATH-item?0780.11068
[75]: http://scholar.google.com/scholar_lookup?amp;title=3x%2B1%20Search%20programs&amp;journal=Comput%20Math%20Appl&amp;doi=10.1016%2F0898-1221%2892%2990034-F&amp;volume=24&amp;issue=11&amp;pages=79-99&amp;publication_year=1992&amp;author=Leavens%2CGT&amp;author=Vermeulen%2CM
[76]: http://scholar.google.com/scholar_lookup?amp;title=GPU-accelerated%20exhaustive%20verification%20of%20the%20Collatz%20conjecture&amp;journal=Int%20J%20Netw%20Comput&amp;volume=7&amp;issue=1&amp;pages=69-85&amp;publication_year=2017&amp;author=Honda%2CT&amp;author=Ito%2CY&amp;author=Nakano%2CK
[77]: https://doi.org/10.1090/S0025-5718-99-01031-5
[78]: https://doi.org/10.1090%2FS0025-5718-99-01031-5
[79]: http://www.ams.org/mathscinet-getitem?mr=1613719
[80]: http://www.emis.de/MATH-item?0919.11020
[81]: http://scholar.google.com/scholar_lookup?amp;title=Maximum%20excursion%20and%20stopping%20time%20record-holders%20for%20the%20%24%243x%2B1%24%24%203%20x%20%2B%201%20problem%3A%20computational%20results&amp;journal=Math%20Comput&amp;doi=10.1090%2FS0025-5718-99-01031-5&amp;volume=68&amp;issue=225&amp;pages=371-384&amp;publication_year=1999&amp;author=Silva%2CTOE
[82]: http://www.ams.org/mathscinet-getitem?mr=4569874
[83]: http://www.emis.de/MATH-item?1536.11052
[84]: http://scholar.google.com/scholar_lookup?amp;title=There%20are%20no%20Collatz%20%24%24m%24%24%20m%20-cycles%20with%20%24%24m%20%5Cle%2091%24%24%20m%20%E2%89%A4%2091&amp;journal=J%20Integer%20Seq&amp;volume=26&amp;issue=3&amp;pages=1-22&amp;publication_year=2023&amp;author=Hercher%2CC
[85]: https://doi.org/10.1214/aoap/1177005779
[86]: https://doi.org/10.1214%2Faoap%2F1177005779
[87]: http://www.ams.org/mathscinet-getitem?mr=1143401
[88]: http://www.emis.de/MATH-item?0742.60027
[89]: http://scholar.google.com/scholar_lookup?amp;title=The%20%24%243x%20%2B%201%24%24%203%20x%20%2B%201%20problem%3A%20two%20stochastic%20models&amp;journal=Annals%20Appl%20Probab&amp;doi=10.1214%2Faoap%2F1177005779&amp;volume=2&amp;issue=1&amp;pages=229-261&amp;publication_year=1992&amp;author=Lagarias%2CJC&amp;author=Weiss%2CA
[90]: https://citation-needed.springer.com/v2/references/10.1007/s11227-025-07337-0?format=refman&amp;flavour=references
[91]: /search?sortBy=newestFirst&amp;contributor=David%20Barina
[92]: https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&amp;term=David%20Barina
[93]: https://scholar.google.co.uk/scholar?as_q=&amp;num=10&amp;btnG=Search+Scholar&amp;as_epq=&amp;as_oq=&amp;as_eq=&amp;as_occt=any&amp;as_sauthors=%22David%20Barina%22&amp;as_publication=&amp;as_ylo=&amp;as_yhi=&amp;as_allsubj=all&amp;hl=en
[94]: mailto:ibarina@fit.vutbr.cz
[95]: http://creativecommons.org/licenses/by/4.0/
[96]: https://s100.copyright.com/AppDispatchServlet?title=Improved%20verification%20limit%20for%20the%20convergence%20of%20the%20Collatz%20conjecture&amp;author=David%20Barina&amp;contentID=10.1007%2Fs11227-025-07337-0&amp;copyright=The%20Author%28s%29&amp;publication=1573-0484&amp;publicationDate=2025-05-02&amp;publisherName=SpringerNature&amp;orderBeanReset=true&amp;oa=CC%20BY
[97]: https://crossmark.crossref.org/dialog/?doi=10.1007/s11227-025-07337-0
[98]: https://citation-needed.springer.com/v2/references/10.1007/s11227-025-07337-0?format=refman&amp;flavour=citation
[99]: /search?query=Collatz%20conjecture&amp;facet-discipline=#34;Computer%20Science&#34;
[100]: /search?query=Software%20optimization&amp;facet-discipline=#34;Computer%20Science&#34;
[101]: /search?query=Parallel%20computing&amp;facet-discipline=#34;Computer%20Science&#34;
[102]: /search?query=Number%20theory&amp;facet-discipline=#34;Computer%20Science&#34;
[103]: /researchers/74224120SN
