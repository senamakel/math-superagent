<!-- source: https://users.math.msu.edu/users/iwenmark/Teaching/MTH810/web-coding-book.pdf | converted from PDF -->

Essential Coding Theory

Venkatesan Guruswami Atri Rudra1 Madhu Sudan

March 15, 2019

1Department of Computer Science and Engineering, University at Buffalo, SUNY. Work supported by
NSF CAREER grant CCF-0844796.
 2

Foreword

This book is based on lecture notes from coding theory courses taught by Venkatesan Gu-
ruswami at University at Washington and CMU; by Atri Rudra at University at Buffalo, SUNY
and by Madhu Sudan at Harvard and MIT.

This version is dated March 15, 2019. For the latest version, please go to

http://www.cse.buffalo.edu/faculty/atri/courses/coding-theory/book/

The material in this book is supported in part by the National Science Foundation under CA-
REER grant CCF-0844796. Any opinions, ﬁndings and conclusions or recomendations expressed
in this material are those of the author(s) and do not necessarily reﬂect the views of the National
Science Foundation (NSF).

©Venkatesan Guruswami, Atri Rudra, Madhu Sudan, 2018.
This work is licensed under the Creative Commons Attribution-NonCommercial-
NoDerivs 3.0 Unported License. To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-nd/3.0/ or send a letter to Creative Commons, 444
Castro Street, Suite 900, Mountain View, California, 94041, USA.

34

Contents

I The Basics 17

1 The Fundamental Question 19
1.1 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
1.2 Some deﬁnitions and codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
1.3 Error correction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
1.4 Distance of a code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
1.5 Hamming Code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
1.6 Hamming Bound . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
1.7 Generalized Hamming Bound . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
1.8 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
1.9 Bibliographic Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38

2 A Look at Some Nicely Behaved Codes: Linear Codes 39
2.1 Finite Fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
2.2 Linear Subspaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
2.3 Properties of Linear Codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
2.4 Hamming Codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
2.5 Family of codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
2.6 Efﬁcient Decoding of Hamming codes . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
2.7 Dual of a Linear Code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
2.8 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
2.9 Bibliographic Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58

3 Probability as Fancy Counting and the q-ary Entropy Function 59
3.1 A Crash Course on Probability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
3.2 The Probabilistic Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
3.3 The q-ary Entropy Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
3.4 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
3.5 Bibliographic Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72

II The Combinatorics 73

4 What Can and Cannot Be Done-I 75

5

4.1 Asymptotic Version of the Hamming Bound . . . . . . . . . . . . . . . . . . . . . . . 75
4.2 Gilbert-Varshamov Bound . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
4.3 Singleton Bound . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
4.4 Plotkin Bound . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
4.5 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
4.6 Bibliographic Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91

5 The Greatest Code of Them All: Reed-Solomon Codes 93
5.1 Polynomials and Finite Fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
5.2 Reed-Solomon Codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
5.3 A Property of MDS Codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
5.4 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
5.5 Bibliographic Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108

6 What Happens When the Noise is Stochastic: Shannon’s Theorem 109
6.1 Overview of Shannon’s Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
6.2 Shannon’s Noise Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
6.3 Shannon’s Result for BSCp . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
6.4 Hamming vs. Shannon . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
6.5 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
6.6 Bibliographic Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126

7 Bridging the Gap Between Shannon and Hamming: List Decoding 127
7.1 Hamming versus Shannon: part II . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
7.2 List Decoding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
7.3 Johnson Bound . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
7.4 List-Decoding Capacity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
7.5 List Decoding from Random Errors . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
7.6 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
7.7 Bibliographic Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 146

8 What Cannot be Done-II 147
8.1 Elias-Bassalygo bound . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
8.2 The MRRW bound: A better upper bound . . . . . . . . . . . . . . . . . . . . . . . . . 149
8.3 A Breather . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
8.4 Bibliographic Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150

III The Codes 151

9 When Polynomials Save the Day: Polynomial Based Codes 153
9.1 The generic construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 154
9.2 The low degree case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155
9.3 The case of the binary ﬁeld . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157

6

9.4 The general case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
9.5 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165
9.6 Bibliographic Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 166

10 From Large to Small Alphabets: Code Concatenation 167
10.1 Code Concatenation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
10.2 Zyablov Bound . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 169
10.3 Strongly Explicit Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 171
10.4 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174
10.5 Bibliographic Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 174

11 Information Theory Strikes Back: Polar Codes 175
11.1 Achieving Gap to Capacity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 176
11.2 Reduction to Linear Compression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 177
11.3 The Polarization Phenomenon . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 178
11.4 Polar codes, Encoder and Decoder . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 184
11.5 Analysis: Speed of Polarization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
11.6 Entropic Calculations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 201
11.7 Summary and additional information . . . . . . . . . . . . . . . . . . . . . . . . . . . 204
11.8 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 205
11.9 Bibliographic Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 206

IV The Algorithms 209

12 Decoding Concatenated Codes 211
12.1 A Natural Decoding Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 211
12.2 Decoding From Errors and Erasures . . . . . . . . . . . . . . . . . . . . . . . . . . . . 214
12.3 Generalized Minimum Distance Decoding . . . . . . . . . . . . . . . . . . . . . . . . 215
12.4 Bibliographic Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 219

13 Efﬁciently Achieving the Capacity of the BSCp 221
13.1 Achieving capacity of B SCp . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 221
13.2 Decoding Error Probability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224
13.3 The Inner Code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 224
13.4 The Outer Code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 225
13.5 Discussion and Bibliographic Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . 227

14 Decoding Reed-Muller Codes 229
14.1 A natural decoding algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 229
14.2 Majority Logic Decoding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 236
14.3 Decoding by reduction to Reed-Solomon decoding . . . . . . . . . . . . . . . . . . . 238
14.4 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 244
14.5 Bibliographic Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 246

7

15 Efﬁcient Decoding of Reed-Solomon Codes 247
15.1 Unique decoding of Reed-Solomon codes . . . . . . . . . . . . . . . . . . . . . . . . 247
15.2 List Decoding Reed-Solomon Codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . 252
15.3 Extensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267
15.4 Bibliographic Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 269

16 Efﬁciently Achieving List Decoding Capacity 271
16.1 Folded Reed-Solomon Codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 271
16.2 List Decoding Folded Reed-Solomon Codes: I . . . . . . . . . . . . . . . . . . . . . . 275
16.3 List Decoding Folded Reed-Solomon Codes: II . . . . . . . . . . . . . . . . . . . . . . 278
16.4 Bibliographic Notes and Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . 288

V The Applications 293

17 Cutting Data Down to Size: Hashing 295
17.1 Why Should You Care About Hashing? . . . . . . . . . . . . . . . . . . . . . . . . . . . 295
17.2 Avoiding Hash Collisions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 297
17.3 Almost Universal Hash Function Families and Codes . . . . . . . . . . . . . . . . . . 300
17.4 Data Possession Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 301
17.5 Bibliographic Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 305

18 Securing Your Fingerprints: Fuzzy Vaults 307
18.1 Some quick background on ﬁngerprints . . . . . . . . . . . . . . . . . . . . . . . . . 307
18.2 The Fuzzy Vault Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 309
18.3 The Final Fuzzy Vault . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 312
18.4 Bibliographic Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 314

19 Finding Defectives: Group Testing 315
19.1 Formalization of the problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 315
19.2 Bounds on t a(d , N ) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 317
19.3 Bounds on t (d , N ) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 318
19.4 Coding Theory and Disjunct Matrices . . . . . . . . . . . . . . . . . . . . . . . . . . . 322
19.5 An Application in Data Stream Algorithms . . . . . . . . . . . . . . . . . . . . . . . . 325
19.6 Summary of best known bounds . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 330
19.7 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 331
19.8 Bibliographic Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 333

A Notation Table 343

B Some Useful Facts 345
B.1 Some Useful Inequalities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 345
B.2 Some Useful Identities and Bounds . . . . . . . . . . . . . . . . . . . . . . . . . . . . 347

8

C Background on Asymptotic notation, Algorithms and Complexity 349
C.1 Asymptotic Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 349
C.2 Bounding Algorithm run time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 351
C.3 Randomized Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 355
C.4 Efﬁcient Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 358
C.5 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 362
C.6 Bibliographic Notes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 364

D Basic Algebraic Algorithms 365
D.1 Executive Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 365
D.2 Groups, Rings, Fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 365
D.3 Polynomials . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 366
D.4 Vector Spaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 368
D.5 Finite Fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 370
D.6 Algorithmic aspects of Finite Fields . . . . . . . . . . . . . . . . . . . . . . . . . . . . 376
D.7 Algorithmic aspects of Polynomials . . . . . . . . . . . . . . . . . . . . . . . . . . . . 378
D.8 Exercises . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 383

E Some Information Theory Essentials 385
E.1 Entropy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 385
E.2 Joint and conditional entropy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 387
E.3 Mutual information . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 390

910

List of Figures

1.1 Decoding for Akash English, one gets “I need little little (trail)mix." . . . . . . . . . 19
1.2 Coding process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
1.3 Bad example for unique decoding. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
1.4 Illustration for proof of Hamming Bound . . . . . . . . . . . . . . . . . . . . . . . . . 34

3.1 The q-ary Entropy Function . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66

4.1 The Hamming and GV bounds for binary codes . . . . . . . . . . . . . . . . . . . . . 76
4.2 An illustration of Gilbert’s greedy algorithm (Algorithm 6) for the ﬁrst ﬁve iterations. 77
4.3 Construction of a new code in the proof of the Singleton bound. . . . . . . . . . . . 80
4.4 The Hamming, GV and Singleton bound for binary codes. . . . . . . . . . . . . . . . 81
4.5 R vs δ tradeoffs for binary codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83

6.1 The communication process . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
6.2 Binary Symmetric Channel BSCp . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
6.3 Binary Erasure Channel BECα . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
6.4 The sets Dm partition the ambient space {0, 1}n. . . . . . . . . . . . . . . . . . . . . . 114
6.5 The shell Sm of inner radius (1 − γ)pn and outer radius (1 + γ)pn. . . . . . . . . . . 115
6.6 Illustration of Proof of Shannon’s Theorem . . . . . . . . . . . . . . . . . . . . . . . . 117

7.1 Bad example of unique decoding revisited . . . . . . . . . . . . . . . . . . . . . . . . 128
7.2 Comparing the Johnson Bound with Unique decoding and Singleton bounds . . . 134
7.3 An error pattern . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
7.4 Illustration of notation used in the proof of Theorem 7.5.1 . . . . . . . . . . . . . . . 140
7.5 An error pattern in the middle of the proof . . . . . . . . . . . . . . . . . . . . . . . . 141

8.1 Bounds on R vs δ for binary codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 148

10.1 Concatenated code Cout ◦Cin. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 168
10.2 The Zyablov bound for binary codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170

11.1 The 2 × 2 Basic Polarizing Transform. Included in brown are the conditional entropies of the variables,
11.2 The n × n Basic Polarizing Transform. . . . . . . . . . . . . . . . . . . . . . . . . . . . 183
11.3 Block structure of the Basic Polarizing Transform. Circled are a block at the 2nd level and two 2nd level

12.1 Encoding and Decoding of Concatenated Codes . . . . . . . . . . . . . . . . . . . . . 212

11

12.2 All values of θ ∈ [qi , qi +1) lead to the same outcome . . . . . . . . . . . . . . . . . . . 219

13.1 Efﬁciently achieving capacity of BSCp . . . . . . . . . . . . . . . . . . . . . . . . . . . 222
13.2 Error Correction cannot decrease during “folding" . . . . . . . . . . . . . . . . . . . 225

15.1 A received word in 2-D space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 248
15.2 The closest polynomial to a received word . . . . . . . . . . . . . . . . . . . . . . . . 249
15.3 Error locator polynomial for a received word . . . . . . . . . . . . . . . . . . . . . . . 250
15.4 The tradeoff between rate R and the fraction of errors that can be corrected by Algorithm 22.256
15.5 A received word in 2-D space for the second Reed-Solomon . . . . . . . . . . . . . . 257
15.6 An interpolating polynomial Q(X , Y ) for the received word in Figure 15.5. . . . . . 258
15.7 The two polynomials that need to be output are shown in blue. . . . . . . . . . . . . 258
15.8 The tradeoff between rate R and the fraction of errors that can be corrected by Algorithm 22 and Algor
15.9 Multiplicity of 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 261
15.10Multiplicity of 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 262
15.11Multiplicity of 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 262
15.12A received word in 2-D space for the third Reed-Solomon . . . . . . . . . . . . . . . 263
15.13An interpolating polynomial Q(X , Y ) for the received word in Figure 15.12. . . . . . 263
15.14The ﬁve polynomials that need to be output are shown in blue. . . . . . . . . . . . . 264

16.1 Encoding for Reed-Solomon Codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . 272
16.2 Folded Reed-Solomon code for m = 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . 272
16.3 Folded Reed-Solomon code for general m ≥ 1 . . . . . . . . . . . . . . . . . . . . . . 272
16.4 Error pattern under unfolding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 273
16.5 Error pattern under folding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 274
16.6 Performance of Algorithm 26 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 278
16.7 An agreement in position i . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 279
16.8 More agreement with a sliding window of size 2. . . . . . . . . . . . . . . . . . . . . . 279
16.9 Performance of Algorithm 27 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 282
16.10An upper triangular system of linear equations . . . . . . . . . . . . . . . . . . . . . 283

18.1 The minutiae are unordered and form a set, not a vector. . . . . . . . . . . . . . . . 309

19.1 Pick a subset S (not necessarily contiguous). Then pick a column j that is not present in S. There will always
19.2 Construction of the ﬁnal matrix MC ∗ from MCout and MCin from Example 19.4.3. The rows in MC ∗ that corr

E.1 Relationship between entropy, joint entropy, conditional entropy, and mutual information for two random

12

List of Tables

3.1 Uniform distribution over F2×2
2 along with values of four random variables. . . . . . 60

8.1 High level summary of results seen so far. . . . . . . . . . . . . . . . . . . . . . . . . . 149

10.1 Strongly explicit binary codes that we have seen so far. . . . . . . . . . . . . . . . . . 167

13.1 An overview of the results seen so far . . . . . . . . . . . . . . . . . . . . . . . . . . . 221
13.2 Summary of properties of Cout and Cin . . . . . . . . . . . . . . . . . . . . . . . . . . 223

1314

List of Algorithms

1 Error Detector for Parity Code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
2 Naive Maximum Likelihood Decoder . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3 Naive Decoder for Hamming Code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
4 Decoder for Any Linear Code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
5 Efﬁcient Decoder for Hamming Code . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
6 Gilbert’s Greedy Code Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
7 qO(k) time algorithm to compute a code on the GV bound . . . . . . . . . . . . . . . 89
8 Generating Irreducible Polynomial . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
9 POLAR COMPRESSOR(Z, S) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 180
10 Successive Cancellation Decompressor SCD(W, P, S) . . . . . . . . . . . . . . . . . . 181
11 BASIC POLAR ENCODER(Z; n, S) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 185
12 BASIC POLAR DECODER: BPD(W; n, p) . . . . . . . . . . . . . . . . . . . . . . . . . . . 186
13 Natural Decoder for Cout ◦Cin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 212
14 Generalized Minimum Decoder (ver 1) . . . . . . . . . . . . . . . . . . . . . . . . . . 216
15 Generalized Minimum Decoder (ver 2) . . . . . . . . . . . . . . . . . . . . . . . . . . 218
16 Deterministic Generalized Minimum Decoder‘ . . . . . . . . . . . . . . . . . . . . . 219
17 Decoder for efﬁciently achieving BSCp capacity . . . . . . . . . . . . . . . . . . . . . 223
18 SIMPLE REED-MULLER DECODER . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 233
19 Majority Logic Decoder . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 238
20 REED-SOLOMON-BASED DECODER . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 241
21 Welch-Berlekamp Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 251
22 The First List Decoding Algorithm for Reed-Solomon Codes . . . . . . . . . . . . . . 255
23 The Second List Decoding Algorithm for Reed-Solomon Codes . . . . . . . . . . . . 259
24 The Third List Decoding Algorithm for Reed-Solomon Codes . . . . . . . . . . . . . 264
25 Decoding Folded Reed-Solomon Codes by Unfolding . . . . . . . . . . . . . . . . . . 273
26 The First List Decoding Algorithm for Folded Reed-Solomon Codes . . . . . . . . . 276
27 The Second List Decoding Algorithm for Folded Reed-Solomon Codes . . . . . . . 280
28 The Root Finding Algorithm for Algorithm 27 . . . . . . . . . . . . . . . . . . . . . . 287
29 Pre-Processing for Data Possession Veriﬁcation . . . . . . . . . . . . . . . . . . . . . 301
30 Veriﬁcation for Data Possession Veriﬁcation . . . . . . . . . . . . . . . . . . . . . . . 302
31 Decompression Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 302
32 Decompression Algorithm Using List Decoding . . . . . . . . . . . . . . . . . . . . . 304
33 UNLOCK2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 311

15

34 LOCK3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 312
35 UNLOCK2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 313
36 Decoder for Separable Matrices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 320
37 Naive Decoder for Disjunct Matrices . . . . . . . . . . . . . . . . . . . . . . . . . . . . 322
38 Initialization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 327
39 Update . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 327
40 Report Heavy Items . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 328
41 Simple Search . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 353
42 Sampling algorithm for GAPHAMMING . . . . . . . . . . . . . . . . . . . . . . . . . . 357
43 An average-case algorithm for GAPHAMMING . . . . . . . . . . . . . . . . . . . . . . 358
44 Exponential time algorithm for MAXLINEAREQ . . . . . . . . . . . . . . . . . . . . . 359
45 Reduction from MAXCUT to MAXLINEAREQ . . . . . . . . . . . . . . . . . . . . . . . 362
46 ROOT-FIND(Fq , f ) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 382
47 LINEAR-ROOT-FIND(Fq , g ) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 382

16

Part I

The Basics

17

Chapter 1

The Fundamental Question

1.1 Overview

Communication is a fundamental need of our modern lives. In fact, communication is some-
thing that humans have been doing for a long time. For simplicity, let us restrict ourselves to
English. It is quite remarkable that different people speaking English can be understood pretty
well: even if e.g. the speaker has an accent. This is because English has some built-in redun-
dancy, which allows for “errors" to be tolerated. This came to fore for one of the authors when
his two and a half year old son, Akash, started to speak his own version of English, which we will
dub “Akash English." As an example,

Figure 1.1: Decoding for Akash English, one gets “I need little little (trail)mix."

With some practice Akash’s parents were able to “decode" what Akash really meant. In fact,

19

Akash could communicate even if he did not say an entire word properly and gobbled up part(s)
of word(s).
The above example shows that having redundancy in a language allows for communication
even in the presence of (small amounts of) differences and errors. Of course in our modern
digital world, all kinds of entities communicate (and most of the entities do not communicate
in English or any natural language for that matter). Errors are also present in the digital world,
so these digital communications also use redundancy.
Error-correcting codes (henceforth, just codes) are clever ways of representing data so that
one can recover the original information even if parts of it are corrupted. The basic idea is to
judiciously introduce redundancy so that the original information can be recovered even when
parts of the (redundant) data have been corrupted.
For example, when packets are transmitted over the Internet, some of the packets get cor-
rupted or dropped. Packet drops are resolved by the TCP layer by a combination of sequence
numbers and ACKs. To deal with data corruption, multiple layers of the TCP/IP stack use a form
of error correction called CRC Checksum [79]. From a theoretical point of view, the checksum
is a terrible code (for that matter so is English). However, on the Internet, the current dominant
mode of operation is to detect errors and if errors have occurred, then ask for retransmission.
This is the reason why the use of checksum has been hugely successful in the Internet. However,
there are other communication applications where re-transmission is not an option. Codes are
used when transmitting data over the telephone line or via cell phones. They are also used in
deep space communication and in satellite broadcast (for example, TV signals are transmitted
via satellite). Indeed, asking the Mars Rover to re-send an image just because it got corrupted
during transmission is not an option–this is the reason that for such applications, the codes
used have always been very sophisticated.
Codes also have applications in areas not directly related to communication. In particu-
lar, in the applications above, we want to communicate over space. Codes can also be used to
communicate over time. For example, codes are used heavily in data storage. CDs and DVDs
work ﬁne even in presence of scratches precisely because they use codes. Codes are used in Re-
dundant Array of Inexpensive Disks (RAID) [15] and error correcting memory [14]. Sometimes,
in the Blue Screen of Death displayed by Microsoft Windows family of operating systems, you
might see a line saying something along the lines of “parity check failed"–this happens when
the code used in the error-correcting memory cannot recover from error(s). Also, certain con-
sumers of memory, e.g. banks, do not want to suffer from even one bit ﬂipping (this e.g. could
mean someone’s bank balance either got halved or doubled–neither of which are welcome1).
Codes are also deployed in other applications such as paper bar codes; for example, the bar
code used by UPS called MaxiCode [13]. Unlike the Internet example, in all of these applica-
tions, there is no scope for “re-transmission."
In this book, we will mainly think of codes in the communication scenario. In this frame-
work, there is a sender who wants to send (say) k message symbols over a noisy channel. The
sender ﬁrst encodes the k message symbols into n symbols (called a codeword) and then sends

1This is a bit tongue-in-cheek: in real life banks have more mechanisms to prevent one bit ﬂip from wreaking
havoc.
 20

it over the channel. The receiver gets a received word consisting of n symbols. The receiver then
tries to decode and recover the original k message symbols. Thus, encoding is the process of
adding redundancy and decoding is the process of removing errors.
Unless mentioned otherwise, in this book we will make the following assumption:

The sender and the receiver only communicate via the channel.a In other words, other than
some setup information about the code, the sender and the receiver do not have any other
information exchange (other than of course what was transmitted over the channel). In
particular, no message is more likely to be transmitted over another.

aThe scenario where the sender and receiver have a “side-channel" is an interesting topic that has been
studied but is outside the scope of this book.

The fundamental question that will occupy our attention for almost the entire book is the
tradeoff between the amount of redundancy used and the number of errors that can be cor-
rected by a code. In particular, we would like to understand:

Question 1.1.1. How much redundancy do we need to correct a given amount of errors? (We
would like to correct as many errors as possible with as little redundancy as possible.)

Intuitively, maximizing error correction and minimizing redundancy are contradictory goals:
a code with higher redundancy should be able to tolerate more number of errors. By the end of
this chapter, we will see a formalization of this question.
Once we determine the optimal tradeoff, we will be interested in achieving this optimal
tradeoff with codes that come equipped with efﬁcient encoding and decoding. (A DVD player
that tells its consumer that it will recover from a scratch on a DVD by tomorrow is not exactly
going to be a best-seller.) In this book, we will primarily deﬁne efﬁcient algorithms to be ones
that run in polynomial time.2

1.2 Some deﬁnitions and codes

To formalize Question 1.1.1, we begin with the deﬁnition of a code.

Deﬁnition 1.2.1 (Code). A code of block length n over an alphabet Σ is a subset of Σn. Typically,
we will use q to denote |Σ|.3

Remark 1.2.1. We note that the ambient space Σn can be viewed as a set of sequences, vectors
or functions. In other words, we can think of a vector (v1, . . . , vn) ∈ Σn as just the sequence
v1, . . . , vn (in order) or a vector tuple (v1, . . . , vn) or as the function f : [n] → Σ such that f (i ) = vi .

2We are not claiming that this is the correct notion of efﬁciency in practice. However, we believe that it is a good
deﬁnition as the “ﬁrst cut"– quadratic or cubic time algorithms are deﬁnitely more desirable than exponential time
algorithms: see Section C.4 for more on this.
3Note that q need not be a constant and can depend on n: we’ll see codes in this book where this is true.

21

Sequences assume least structure on Σ and hence are most generic. Vectors work well when Σ
has some structure (and in particular is what is known as a ﬁeld, which we will see next chapter).
Functional representation will be convenient when the set of coordinates has structure (e.g.,
[n] may come from a ﬁnite ﬁeld of size n). For now, however, the exact representation does not
matter and the reader can work with representation as sequences.

We will also frequently use the following alternate way of looking at a code. Given a code
C ⊆ Σn, with |C | = M , we will think of C as a mapping of the following form:

C : [M ] → Σn.

In the above, we have used to notation [M ] for any integer M ≥ 1 to denote the set {1, 2, . . . , M }.
We will also need the notion of dimension of a code.

Deﬁnition 1.2.2 (Dimension of a code). Given a code C ⊆ Σn, its dimension is given by

k def
= logq |C |.

Let us begin by looking at two speciﬁc codes. Both codes are deﬁned over Σ = {0, 1} (also
known as binary codes). In both cases |C | = 24 and we will think of each of the 16 messages as a
4 bit vector.
We ﬁrst look at the so-called parity code, which we will denote by C⊕. Given a message
(x1, x2, x3, x4) ∈ {0, 1}4, its corresponding codeword is given by

C⊕(x1, x2, x3, x4) = (x1, x2, x3, x4, x1 ⊕ x2 ⊕ x3 ⊕ x4),

where the ⊕ denotes the EXOR (also known as the XOR or Exclusive-OR) operator. In other
words, the parity code appends the parity of the message bits (or takes the remainder of the
sum of the message bits when divided by 2) at the end of the message. Note that such a code
uses the minimum amount of non-zero redundancy.
The second code we will look at is the so-called repetition code. This is a very natural code
(and perhaps the ﬁrst code one might think of). The idea is to repeat every message bit a ﬁxed
number of times. For example, we repeat each of the 4 message bits 3 times and we use C3,r ep
to denote this code.
Let us now try to look at the tradeoff between the amount of redundancy and the number of
errors each of these codes can correct. Even before we begin to answer the question, we need
to deﬁne how we are going to measure the amount of redundancy. One natural way to deﬁne
redundancy for a code with dimension k and block length n is by their difference n − k. By this
deﬁnition, the parity code uses the least amount of redundancy. However, one “pitfall" of such
a deﬁnition is that it does not distinguish between a code with k = 100 and n = 102 and another
code with dimension and block length 2 and 4, respectively. Intuitively, the latter code is using
more redundancy. This motivates the following notion of measuring redundancy.

Deﬁnition 1.2.3 (Rate of a code). The rate of a code with dimension k and block length n is
given by
 R def
= k
n .

22

Note that the higher the rate, the lesser the amount of redundancy in the code. Also note that
as k ≤ n, R ≤ 1.4 Intuitively, the rate of a code is the average amount of real information in each
of the n symbols transmitted over the channel. So, in some sense, rate captures the complement
of redundancy. However, for historical reasons, we will deal with the rate R (instead of the more
obvious 1−R) as our notion of redundancy. Given the above deﬁnition, C⊕ and C3,r ep have rates
of 4
5 and 1
3 . As was to be expected, the parity code has a higher rate than the repetition code.
We have formalized the notion of redundancy as the rate of a code as well as other param-
eters of a code. However, to formalize Question 1.1.1, we still need to formally deﬁne what it
means to correct errors. We do so next.

1.3 Error correction

Before we formally deﬁne error correction, we will ﬁrst formally deﬁne the notion of encoding.

Deﬁnition 1.3.1 (Encoding function). Let C ⊆ Σn. An equivalent description of the code C is an
injective mapping E : [|C |] → Σn called the encoding function.

Next we move to error correction. Intuitively, we can correct a received word if we can re-
cover the transmitted codeword (or equivalently the corresponding message). This “reverse"
process is called decoding.

Deﬁnition 1.3.2 (Decoding function). Let C ⊆ Σn be a code. A mapping D : Σn → [|C |] is called
a decoding function for C .

The deﬁnition of a decoding function by itself does not give anything interesting. What we
really need from a decoding function is that it recovers the transmitted message. This notion is
captured next.

Deﬁnition 1.3.3 (Error Correction). Let C ⊆ Σn and let t ≥ 1 be an integer. C is said to be t -error-
correcting if there exists a decoding function D such that for every message m ∈ [|C |] and error
pattern e with at most t errors, D (C (m) + e)) = m.

Figure 1.3 illustrates how the deﬁnitions we have examined so far interact.
We will also very brieﬂy look at a weaker form of error recovery called error detection.

Deﬁnition 1.3.4 (Error detection). Let C ⊆ Σn and let t ≥ 1 be an integer. C is said to be t -error-
detecting if there exists a detecting procedure D such that for every message m and every error
pattern e with at most t errors, D outputs a 1 if (C (m) + e) ∈ C and 0 otherwise.

Note that a t -error correcting code is also a t -error detecting code (but not necessarily the
other way round): see Exercise 1.1. Although error detection might seem like a weak error recov-
ery model, it is useful in settings where the receiver can ask the sender to re-send the message.
For example, error detection is used quite heavily in the Internet.
With the above deﬁnitions in place, we are now ready to look at the error correcting capa-
bilities of the codes we looked at in the previous section.

4Further, in this book, we will always consider the case k > 0 and n < ∞ and hence, we can also assume that
R > 0.
 23

m  C ( m ) 

e n c o d i n g   f u n c t i o n 
 c h a n n e l 

e 
 y   =   C ( m )   +   e  m 

d e c o d i n g   f u n c t i o n 

Figure 1.2: Coding process

1.3.1 Error-Correcting Capabilities of Parity and Repetition codes

In Section 1.2, we looked at examples of parity code and repetition code with the following
properties:
 C⊕ : q = 2, k = 4, n = 5, R = 4/5.

C3,r ep : q = 2, k = 4, n = 12, R = 1/3.

We will start with the repetition code. To study its error-correcting capabilities, we will con-
sider the following natural decoding function. Given a received word y ∈ {0, 1}12, divide it up
into four consecutive blocks (y1, y2, y3, y4) where every block consists of three bits. Then, for
every block yi (1 ≤ i ≤ 4), output the majority bit as the message bit. We claim this decoding
function can correct any error pattern with at most 1 error. (See Exercise 1.2.) For example, if a
block of 010 is received, since there are two 0’s we know the original message bit was 0. In other
words, we have argued that

Proposition 1.3.1. C3,r ep is a 1-error correcting code.

However, it is not too hard to see that C3,r ep cannot correct two errors. For example, if both
of the errors happen in the same block and a block in the received word is 010, then the original
block in the codeword could have been either 111 or 000. Therefore in this case, no decoder can
successfully recover the transmitted message.5

Thus, we have pin-pointed the error-correcting capabilities of the C3,r ep code: it can cor-
rect one error, but not two or more. However, note that the argument assumed that the error
positions can be located arbitrarily. In other words, we are assuming that the channel noise
behaves arbitrarily (subject to a bound on the total number of errors). Obviously, we can model
the noise differently. We now brieﬂy digress to look at this issue in slightly more detail.

Digression: Channel Noise. As was mentioned above, until now we have been assuming the
following noise model, which was ﬁrst studied by Hamming:

5Recall we are assuming that the decoder has no side information about the transmitted message.

24

Any error pattern can occur during transmission as long as the total number of er-
rors is bounded. Note that this means that the location as well as the nature
6 of the
errors is arbitrary.

We will frequently refer to Hamming’s model as the Adversarial Noise Model. It is important
to note that the atomic unit of error is a symbol from the alphabet. So for example, if the error
pattern is (1, 0, 1, 0, 0, 0) and we consider the alphabet to be {0, 1}, then the pattern has two errors.
However, if our alphabet is {0, 1}3 (i.e. we think of the vector above as ((1, 0, 1), (0, 0, 0)), with
(0, 0, 0) corresponding to the zero element in {0, 1}3), then the pattern has only one error. Thus,
by increasing the alphabet size we can also change the adversarial noise model. As the book
progresses, we will see how error correction over a larger alphabet is easier than error correction
over a smaller alphabet.
However, the above is not the only way to model noise. For example, we could also have
following error model:

No more than 1 error can happen in any contiguous three-bit block.

First note that, for the channel model above, no more than four errors can occur when a code-
word in C3,r ep is transmitted. (Recall that in C3,r ep , each of the four bits is repeated three times.)
Second, note that the decoding function that takes the majority vote of each block can suc-
cessfully recover the transmitted codeword for any error pattern, while in the worst-case noise
model it could only correct at most one error. This channel model is admittedly contrived, but
it illustrates the point that the error-correcting capabilities of a code (and a decoding function)
are crucially dependent on the noise model.
A popular alternate noise model is to model the channel as a stochastic process. As a con-
crete example, let us brieﬂy mention the binary symmetric channel with crossover probability
0 ≤ p ≤ 1, denoted by BSCp , which was ﬁrst studied by Shannon. In this model, when a (binary)
codeword is transferred through the channel, every bit ﬂips independently with probability p.
Note that the two noise models proposed by Hamming and Shannon are in some sense two
extremes: Hamming’s model assumes no knowledge about the channel (except that a bound
on the total number of errors is known
7 while Shannon’s noise model assumes complete knowl-
edge about how noise is produced. In this book, we will consider only these two extreme noise
models. In real life, the situation often is somewhere in between.
For real life applications, modeling the noise model correctly is an extremely important
task, as we can tailor our codes to the noise model at hand. However, in this book we will
not study this aspect of designing codes at all, and will instead mostly consider the worst-case
noise model. Intuitively, if one can communicate over the worst-case noise model, then one
could use the same code to communicate over nearly every other noise model with the same
amount of noise.

6For binary codes, there is only one kind of error: a bit ﬂip. However, for codes over a larger alphabet, say {0, 1, 2},
0 being converted to a 1 and 0 being converted into a 2 are both errors, but are different kinds of errors.
7A bound on the total number of errors is necessary; otherwise, error correction would be impossible: see
Exercise 1.3.
 25

We now return to C⊕ and examine its error-correcting capabilities in the worst-case noise
model. We claim that C⊕ cannot correct even one error. Suppose y = 10000 is the received word.
Then we know that an error has occurred, but we do not know which bit was ﬂipped. This is
because the two codewords u = 00000 and v = 10001 differ from the received word y in exactly
one bit. As we are assuming that the receiver has no side information about the transmitted
codeword, no decoder can know what the transmitted codeword was.
Thus, from an error-correction point of view, C⊕ is a terrible code (as it cannot correct even
1 error). However, we will now see that C⊕ can detect one error. Consider Algorithm 1. Note that

Algorithm 1 Error Detector for Parity Code
INPUT: Received word y = (y1, y2, y3, y4, y5)
OUTPUT: 1 if y ∈ C⊕ and 0 otherwise

1: b ← y1 ⊕ y2 ⊕ y3 ⊕ y4 ⊕ y5
2: RETURN 1 ⊕ b ⊲ If there is no error, then b = 0 and hence we need to "ﬂip" the bit for the
answer

when no error has occurred during transmission, yi = xi for 1 ≤ i ≤ 4 and y5 = x1 ⊕ x2 ⊕ x3 ⊕ x4,
in which case b = 0 and we output 1 ⊕ 0 = 1 as required. If there is a single error then either
yi = xi ⊕ 1 (for exactly one 1 ≤ i ≤ 4) or y5 = x1 ⊕ x2 ⊕ x3 ⊕ x4 ⊕ 1. It is easy to check that in this
case, b = 1. In fact, one can extend this argument to obtain the following result (see Exercise 1.4).

Proposition 1.3.2. The parity code C⊕ can detect an odd number of errors.

Let us now revisit the example that showed that one cannot correct one error using C⊕.
Recall, we considered two codewords in C⊕, u = 00000 and v = 10001 (which are codewords
corresponding to messages 0000 and 1000, respectively). Now consider the scenarios in which
u and v are each transmitted and a single error occurs resulting in the received word r = 10000.
Thus, given the received word r and the fact that at most one error can occur, the decoder has
no way of knowing whether the original transmitted codeword was u or v. Looking back at the
example, it is clear that the decoder is “confused" because the two codewords u and v do not
differ in many positions. This notion is formalized in the next section.

1.4 Distance of a code

We now deﬁne a notion of distance that captures the concept that the two vectors u and v are
“close-by."

Deﬁnition 1.4.1 (Hamming distance). Given two vectors u, v ∈ Σn the Hamming distance be-
tween u and v, denoted by ∆(u, v), is the number of positions in which u and v differ.

The Hamming distance is a distance in a very formal mathematical sense: see Exercise 1.5.
Note that the deﬁnition of Hamming distance just depends on the number of differences and
not the nature of the difference. For example, consider the vectors u and v from the previous

26

section. One can see that their Hamming distance is ∆(u, v) = 2. Now consider the vector w =
01010. Note that even though v ̸= w, we have that the Hamming distance ∆(u, w) = 2.
Armed with the notion of Hamming distance, we now deﬁne another important parameter
of a code.

Deﬁnition 1.4.2 (Minimum distance). Let C ⊆ Σn. The minimum distance (or just distance) of
C is deﬁned to be d = min
c1̸=c2∈C ∆(c1, c2)

It is easy to check that the repetition code C3,r ep has distance 3. Indeed, any two distinct
messages will differ in at least one of the message bits. After encoding, the difference in one
message bit will translate into a difference of three bits in the corresponding codewords. We
now claim that the distance of C⊕ is 2. This is a consequence of the following observations. If
two messages m1 and m2 differ in at least two places then ∆(C⊕(m1),C⊕(m2)) ≥ 2 (even if we
just ignored the parity bits). If two messages differ in exactly one place then the parity bits in
the corresponding codewords are different which implies a Hamming distance of 2 between
the codewords. Thus, C⊕ has smaller distance than C3,r ep and can correct less number of errors
than C3,r ep . This suggests that a larger distance implies greater error-correcting capabilities.
The next result formalizes this intuition.

Proposition 1.4.1. Given a code C , the following are equivalent:

1. C has minimum distance d ≥ 2,

2. If d is odd, C can correct (d − 1)/2 errors.

3. C can detect d − 1 errors.

4. C can correct d − 1 erasures.8

Remark 1.4.1. Property (2) above for even d is slightly different. In this case, one can correct up
to d
2 − 1 errors but cannot correct d
2 errors. (See Exercise 1.6.)

Before we prove Proposition 1.4.1, let us apply it to the codes C⊕ and C3,r ep which have
distances of 2 and 3 respectively. Proposition 1.4.1 implies the following facts that we have
already proved:

• C3,r ep can correct 1 error (Proposition 1.3.1).

• C⊕ can detect 1 error but cannot correct 1 error (Proposition 1.3.2).

The proof of Proposition 1.4.1 will need the following decoding function. Maximum like-
lihood decoding (MLD) is a well-studied decoding method for error correcting codes, which

8In the erasure noise model, the receiver knows where the errors have occurred. In this model, an erroneous
symbol is denoted by “?", with the convention that any non-? symbol is a correct symbol.

27

outputs the codeword closest to the received word in Hamming distance (with ties broken arbi-
trarily). More formally, the MLD function denoted by D M LD : Σn → C is deﬁned as follows. For
every y ∈ Σn, D M LD (y) = arg min
c∈C ∆(c, y).

Algorithm 2 is a naive implementation of the MLD.

Algorithm 2 Naive Maximum Likelihood Decoder
INPUT: Received word y ∈ Σn

OUTPUT: D M LD (y)

1: Pick an arbitrary c ∈ C and assign z ← c

2: FOR every c′ ∈ C such that c ̸= c′ DO

3: IF ∆(c′, y) < ∆(z, y) THEN

4: z ← c′

5: RETURN z

Proof of Proposition 1.4.1 We will complete the proof in two steps. First, we will show that if
property 1 is satisﬁed then so are properties 2,3 and 4. Then we show that if property 1 is not
satisﬁed then none of properties 2,3 or 4 hold.

1. implies 2. Assume C has distance d . We ﬁrst prove 2 (for this case assume that d = 2t + 1).
We now need to show that there exists a decoding function such that for all error patterns with
at most t errors it always outputs the transmitted message. We claim that the MLD function
has this property. Assume this is not so and let c1 be the transmitted codeword and let y be the
received word. Note that ∆(y, c1) ≤ t . (1.1)

As we have assumed that MLD does not work, D M LD (y) = c2 ̸= c1. Note that by the deﬁnition of
MLD, ∆(y, c2) ≤ ∆(y, c1). (1.2)

Consider the following set of inequalities:

∆(c1, c2) ≤ ∆(c2, y) + ∆(c1, y) (1.3)

≤ 2∆(c1, y) (1.4)

≤ 2t (1.5)

= d − 1, (1.6)

where (1.3) follows from the triangle inequality (see Exercise 1.5), (1.4) follows from (1.2) and
(1.5) follows from (1.1). (1.6) implies that the distance of C is at most d − 1, which is a contra-
diction.
 28

1. implies 3. We now show that property 3 holds, that is, we need to describe an algorithm
that can successfully detect whether errors have occurred during transmission (as long as the
total number of errors is bounded by d − 1). Consider the following error detection algorithm:
check if the received word y = c for some c ∈ C (this can be done via an exhaustive check). If
no errors occurred during transmission, y = c1, where c1 was the transmitted codeword and the
algorithm above will accept (as it should). On the other hand if 1 ≤ ∆(y, c1) ≤ d − 1, then by the
fact that the distance of C is d , y ̸∈ C and hence the algorithm rejects, as required.

1. implies 4. Finally, we prove that property 4 holds. Let y ∈ (Σ ∪ {?})n be the received word.
First we claim that there is a unique c = (c1, . . . , cn) ∈ C that agrees with y (i.e. yi = ci for ev-
ery i such that yi ̸= ?). (For the sake of contradiction, assume that this is not true, i.e. there
exists two distinct codewords c1, c2 ∈ C such that both c1 and c2 agree with y in the unerased
positions. Note that this implies that c1 and c2 agree in the positions i such that yi ̸= ?. Thus,
∆(c1, c2) ≤ |{i |yi = ?}| ≤ d − 1, which contradicts the assumption that C has distance d .) Given
the uniqueness of the codeword c ∈ C that agrees with y in the unerased position, an algorithm
to ﬁnd c is as follows: go through all the codewords in C and output the desired codeword.

¬1. implies ¬2. For the other direction of the proof, assume that property 1 does not hold,
that is, C has distance d − 1. We now show that property 2 cannot hold: i.e., for every decoding
function there exists a transmitted codeword c1 and a received word y (where ∆(y, c1) ≤ (d −1)/2)
such that the decoding function cannot output c1. Let c1 ̸= c2 ∈ C be codewords such that
∆(c1, c2) = d − 1 (such a pair exists as C has distance d − 1). Now consider a vector y such that
∆(y, c1) = ∆(y, c2) = (d − 1)/2. Such a y exists as d is odd and by the choice of c1 and c2. Below is
an illustration of such a y (matching color implies that the vectors agree on those positions):

d −1
2n − d + 1
 c1

c2

y

d −1
2

Figure 1.3: Bad example for unique decoding.

Now, since y could have been generated if either of c1 or c2 were the transmitted codeword,
no decoding function can work in this case.9

9Note that this argument is just a generalization of the argument that C⊕ cannot correct 1 error.

29

¬1. implies ¬3. For the remainder of the proof, assume that the transmitted word is c1 and
there exists another codeword c2 such that ∆(c2, c1) = d − 1. To see why property 3 is not true,
let y = c2. In this case, either the error detecting algorithm detects no error, or it declares an
error when c2 is the transmitted codeword and no error takes place during transmission.

¬1. implies ¬4. We ﬁnally argue that property 4 does not hold. Let y be the received word in
which the positions that are erased are exactly those where c1 and c2 differ. Thus, given y both
c1 and c2 could have been the transmitted codeword, and no algorithm for correcting (at most
d − 1) erasures can work in this case. ■
Proposition 1.4.1 implies that Question 1.1.1 can be reframed as

Question 1.4.1. What is the largest rate R that a code with distance d can have?

We have seen that the repetition code C3,r ep has distance 3 and rate 1/3. A natural follow-up
question (which is a special case of Question 1.4.1) is to ask

Question 1.4.2. Can we have a code with distance 3 and rate R > 1
3 ?

1.5 Hamming Code

With the above question in mind, let us consider the so-called Hamming code, which we will
denote by C H . Given a message (x1, x2, x3, x4) ∈ {0, 1}4, its corresponding codeword is given by

C H (x1, x2, x3, x4) = (x1, x2, x3, x4, x2 ⊕ x3 ⊕ x4, x1 ⊕ x3 ⊕ x4, x1 ⊕ x2 ⊕ x4).

It is easy to check that this code has the following parameters:

C H : q = 2, k = 4, n = 7, R = 4/7.

We will show shortly that C H has a distance of 3. We would like to point out that we could
have picked the three parities differently. The reason we mention the three particular parities
above is due to historical reasons. We leave it as an exercise to deﬁne an alternate set of parities
such that the resulting code still has a distance of 3: see Exercise 1.9.
Before we move on to determining the distance of C H , we will need another deﬁnition.

Deﬁnition 1.5.1 (Hamming Weight). Let q ≥ 2. Given any vector v ∈ {0, 1, 2, . . . , q − 1}n, its Ham-
ming weight, denoted by w t (v) is the number of non-zero symbols in v.

30

For example, if v = 01203400, then w t (v) = 4.
We now look at the distance of C H .

Proposition 1.5.1. C H has a distance of 3.

Proof. We will prove the claimed property by using two properties of C H :

min
c∈C H ,c̸=0 w t (c) = 3, (1.7)

and min
c∈C H ,c̸=0 w t (c) = min
c1̸=c2∈C H ∆(c1, c2) (1.8)

The proof of (1.7) follows from a case analysis on the Hamming weight of the message bits. Let
us use x = (x1, x2, x3, x4) to denote the message vector.

• Case 0: If w t (x) = 0, then C H (x) = 0, which means we do not have to consider this code-
word.

• Case 1: If w t (x) = 1 then at least two parity check bits in (x2⊕x3⊕x4, x1⊕x2⊕x4, x1⊕x3⊕x4)
are 1 (see Exercise 1.10). So in this case, w t (C H (x)) ≥ 3.

• Case 2: If w t (x) = 2 then at least one parity check bit in (x2⊕x3⊕x4, x1⊕x2⊕x4, x1⊕x3⊕x4)
is 1 (see Exercise 1.11). So in this case, w t (C H (x)) ≥ 3.

• Case 3: If w t (x) ≥ 3 then obviously w t (C H (x)) ≥ 3.

Thus, we can conclude that min
c∈C H ,c̸=0w t (c) ≥ 3. Further, note that w t (C H (1, 0, 0, 0)) = 3, which

along with the lower bound that we just obtained proves (1.7).
We now turn to the proof of (1.8). For the rest of the proof, let x = (x1, x2, x3, x4) and y =
(y1, y2, y3, y4) denote the two distinct messages. Using associativity and commutativity of the ⊕
operator, we obtain that C H (x) +C H (y) = C H (x + y),

where the “+" operator is just the bit-wise ⊕ of the operand vectors10. Further, it is easy to verify
that for two vectors u, v ∈ {0, 1}n, ∆(u, v) = w t (u + v) (see Exercise 1.12). Thus, we have

min
x̸=y∈{0,1}4 ∆(C H (x),C H (y)) = min
x̸=y∈{0,1}4 w t (C H (x + y))

= min
x̸=0∈{0,1}4 w t (C H (x)),

where the second equality follows from the observation that {x+y|x ̸= y ∈ {0, 1}n} = {x ∈ {0, 1}n|x ̸=
0}. Recall that w t (C H (x)) = 0 if and only if x = 0 and this completes the proof of (1.8). Combining
(1.7) and (1.8), we conclude that C H has a distance of 3.

10E.g. (0, 1, 1, 0) + (1, 1, 1, 0) = (1, 0, 0, 0).
 31

The second part of the proof could also be shown in the following manner. It can be veriﬁed
easily that the Hamming code is the set {x · G H |x ∈ {0, 1}4}, where G H is the following matrix
(where we think x as a row vector).11

G H =
 






1 0 0 0 0 1 1
0 1 0 0 1 0 1
0 0 1 0 1 1 0
0 0 0 1 1 1 1







In fact, any binary code (of dimension k and block length n) that is generated12 by a k × n
matrix is called a binary linear code. (Both C⊕ and C3,r ep are binary linear codes: see Exer-
cise 1.13.) This implies the following simple fact.

Lemma 1.5.2. For any binary linear code C and any two messages x and y, C (x)+C (y) = C (x+y).

Proof. For any binary linear code, we have a generator matrix G. The following sequence of
equalities (which follow from the distributivity and associativity properties of the Boolean EXOR
and AND operators) proves the lemma.

C (x) +C (y) = x · G + y · G

= (x + y) · G

= C (x + y)

We stress that in the lemma above, x and y need not be distinct. Note that due to the fact that
b ⊕b = 0 for every b ∈ {0, 1}, x+x = 0, which along with the lemma above implies that C (0) = 0.13

We can infer the following result from the above lemma and the arguments used to prove (1.8)
in the proof of Proposition 1.5.1.

Proposition 1.5.3. For any binary linear code, its minimum distance is equal to minimum Ham-
ming weight of any non-zero codeword.

Thus, we have seen that C H has distance d = 3 and rate R = 4
7 while C3,r ep has distance d = 3
and rate R = 1
3 . Thus, the Hamming code is provably better than the repetition code (in terms
of the tradeoff between rate and distance) and thus, answers Question 1.4.2 in the afﬁrmative.
The next natural question is

Question 1.5.1. Can we have a distance 3 code with a rate higher than that of C H ?

11Indeed (x1, x2, x3, x4) · G H = (x1, x2, x3, x4, x2 ⊕ x3 ⊕ x4, x1 ⊕ x3 ⊕ x4, x1 ⊕ x2 ⊕ x4), as desired.
12That is, C = {x · G|x ∈ {0, 1}
k }, where addition is the ⊕ operation and multiplication is the AND operation.
13This of course should not be surprising as for any matrix G, we have 0 · G = 0.

32

We will address this question in the next section.

1.6 Hamming Bound

Now we switch gears to present our ﬁrst tradeoff between redundancy (in the form of the di-
mension of a code) and its error-correction capability (in the form of its distance). In particular,
we will ﬁrst prove a special case of the so-called Hamming bound for a distance of 3.
We begin with another deﬁnition.

Deﬁnition 1.6.1 (Hamming Ball). For any vector x ∈ [q]
n,

B (x, e) = {y ∈ [q]
n|∆(x, y) ≤ e}.

Next, we prove an upper bound on the dimension of every code with distance 3.

Theorem 1.6.1 (Hamming bound for d = 3). Every binary code with block length n, dimension
k, distance d = 3 satisﬁes k ≤ n − log2(n + 1).

Proof. Given any two codewords, c1 ̸= c2 ∈ C , the following is true (as C has distance
14 3):

B (c1, 1) ∩ B (c2, 1) = ;. (1.9)

See Figure 1.4 for an illustration. Note that for all x ∈ {0, 1}n (see Exercise 1.16),

|B (x, 1)| = n + 1. (1.10)

Now consider the union of all Hamming balls centered around some codeword. Obviously, their
union is a subset of {0, 1}n. In other words,
∣ ⋃

c∈CB (c, 1)∣ ≤ 2n. (1.11)

As (
1.9) holds for every pair of distinct codewords,
∣ ⋃

c∈CB (c, 1)∣ = ∑

c∈C |B (c, 1)|

= ∑

c∈C(n + 1) (1.12)

= 2k · (n + 1), (1.13)

14Assume that y ∈ B (c1, 1)∩B (c2, 1), that is ∆(y, c1) ≤ 1 and ∆(y, c2) ≤ 1. Thus, by the triangle inequality ∆(c1, c2) ≤
2 < 3, which is a contradiction.
 33

1

1

c1
 {0, 1}n

1

c2
 1
 11

Figure 1.4: Hamming balls of radius 1 are disjoint. The ﬁgure is technically not correct: the balls
above are actually balls in the Euclidean space, which is easier to visualize than the Hamming
space.

where (1.12) follows from (1.10) and (1.13)) the fact that C has dimension k. Combining (1.13)
and (1.11), we get 2k (n + 1) ≤ 2n,

or equivalently
 2k ≤ 2n

n + 1 .

Taking log2 of both sides we get the desired bound:

k ≤ n − log2(n + 1).

Thus, Theorem 1.6.1 shows that for n = 7, C H has the largest possible dimension for any
binary code of block length 7 and distance 3 (as for n = 7, n − log2(n + 1) = 4). In particular,
it also answers Question 1.5.1 for n = 7 in the negative. Next, will present the general form of
Hamming bound.

1.7 Generalized Hamming Bound

We start with a new notation.

Deﬁnition 1.7.1. A code C ⊆ Σn with dimension k and distance d will be called a (n, k, d )Σ code.
We will also refer it to as a (n, k, d )|Σ| code.

We now proceed to generalize Theorem 1.6.1 to any distance d .

34

Theorem 1.7.1 (Hamming Bound for any d ). For every (n, k, d )q code

k ≤ n − logq
 




⌊ (d −1)
2
 ⌋
∑

i =0
 (
n
i
 )

(q − 1)i
 


 .

Proof. The proof is a straightforward generalization of the proof of Theorem 1.6.1. For nota-

tional convenience, let e = ⌊ (d −1)
2
 ⌋
. Given any two codewords, c1 ̸= c2 ∈ C , the following is true

(as C has distance
15 d ): B (c1, e) ∩ B (c2, e) = ;. (1.14)

We claim that for all x ∈ [q]
n,
 |B (x, e)| = e∑

i =0
 (n
i
 )

(q − 1)i . (1.15)

Indeed any vector in B (x, e) must differ from x in exactly 0 ≤ i ≤ e positions. In the summation(n
i ) is the number of ways of choosing the differing i positions and in each such position, a
vector can differ from x in q − 1 ways.
Now consider the union of all Hamming balls centered around some codeword. Obviously,
their union is a subset of [q]
n. In other words,
∣ ⋃

c∈CB (c, e)∣ ≤ q n. (1.16)

As (
1.14) holds for every pair of distinct codewords,
∣ ⋃

c∈CB (c, e)∣ = ∑

c∈C |B (c, e)|

= q k e∑

i =0
 (n
i
 )
(q − 1)i , (1.17)

where (
1.17) follows from (1.15) and the fact that C has dimension k. Combining (1.17) and
(1.16) and taking logq of both sides we will get the desired bound:

k ≤ n − logq
 ( e∑

i =0
 (n
i
 )

(q − 1)i )
 .

Note that the Hamming bound gives a partial answer to Question 1.4.1. In particular, any
code of distance d can have rate R at most

1 − logq (∑e
i =0 (n
i )
(q − 1)i )

n .

Further, the Hamming bound also leads to the following deﬁnition:

15Assume that y ∈ B (c1, e)∩B (c2, e), that is ∆(y, c1) ≤ e and ∆(y, c2) ≤ e. Thus, by the triangle inequality, ∆(c1, c2) ≤
2e ≤ d − 1, which is a contradiction.
 35

Deﬁnition 1.7.2. Codes that meet Hamming bound are called perfect codes.

Intuitively, a perfect code leads to the following perfect “packing": if one constructs Ham-

ming balls of radius ⌊ d −1
2
 ⌋ around all the codewords, then we would cover the entire ambient
space, i.e. every possible vector will lie in one of these Hamming balls.
One example of perfect code is the (7, 4, 3)2 Hamming code that we have seen in this chapter
(so is the family of general Hamming codes that we will see in the next chapter). A natural
question to ask is if

Question 1.7.1. Other than the Hamming codes, are there any other perfect (binary) codes?

We will see the answer shortly.

1.8 Exercises

Exercise 1.1. Show that any t -error correcting code is also t -error detecting but not necessarily
the other way around.

Exercise 1.2. Prove Proposition 1.3.1.

Exercise 1.3. Show that for every integer n, there is no code with block length n that can handle
arbitrary number of errors.

Exercise 1.4. Prove Proposition 1.3.2.

Exercise 1.5. A distance function on Σn (i.e. d : Σn × Σn → R) is called a metric if the following
conditions are satisﬁed for every x, y, z ∈ Σn:

1. d (x, y) ≥ 0.

2. d (x, y) = 0 if and only if x = y.

3. d (x, y) = d (y, x).

4. d (x, z) ≤ d (x, y) + d (y, z). (This property is called the triangle inequality.)

Prove that the Hamming distance is a metric.

Exercise 1.6. Let C be a code with distance d for even d . Then argue that C can correct up to
d /2 − 1 many errors but cannot correct d /2 errors. Using this or otherwise, argue that if a code
C is t -error correctable then it either has a distance of 2t + 1 or 2t + 2.

Exercise 1.7. In this exercise, we will see that one can convert arbitrary codes into code with
slightly different parameters:
 36

1. Let C be an (n, k, d )2 code with d odd. Then it can be converted into an (n + 1, k, d + 1)2
code.

2. Let C be an (n, k, d )Σ code. Then it can be converted into an (n − 1, k, d − 1)Σ code.

Note: Other than the parameters of the code C , you should not assume anything else about the
code. Also your conversion should work for every n, k, d ≥ 1.

Exercise 1.8. In this problem we will consider a noise model that has both errors and erasures. In
particular, let C be an (n, k, d )Σ code. As usual a codeword c ∈ C is transmitted over the channel
and the received word is a vector y ∈ (Σ ∪ {?})
n, where as before a ? denotes an erasure. We will
use s to denote the number of erasures in y and e to denote the number of (non-erasure) errors
that occurred during transmission. To decode such a vector means to output a codeword c ∈ C
such that the number of positions where c disagree with y in the n − s non-erased positions is
at most e. For the rest of the problem assume that

2e + s < d . (1.18)

1. Argue that the output of the decoder for any C under (1.18) is unique.

2. Let C be a binary code (but not necessarily linear). Assume that there exists a decoder D
that can correct from < d /2 many errors in T (n) time. Then under (1.18) one can perform
decoding in time O(T (n)).

Exercise 1.9. Deﬁne codes other than C H with k = 4, n = 7 and d = 3.

Hint: Refer to the proof of Proposition 1.5.1 to ﬁgure out the properties needed from the three parities.

Exercise 1.10. Argue that if w t (x) = 1 then at least two parity check bits in (x2 ⊕ x3 ⊕ x4, x1 ⊕ x2 ⊕
x4, x1 ⊕ x3 ⊕ x4) are 1.

Exercise 1.11. Argue that if w t (x) = 2 then at least one parity check bit in (x2 ⊕ x3 ⊕ x4, x1 ⊕ x2 ⊕
x4, x1 ⊕ x3 ⊕ x4) is 1.

Exercise 1.12. Prove that for any u, v ∈ {0, 1}n, ∆(u, v) = w t (u + v).

Exercise 1.13. Argue that C⊕ and C3,r ep are binary linear codes.

Exercise 1.14. Let G be a generator matrix of an (n, k, d )2 binary linear code. Then G has at least
kd ones in it.

Exercise 1.15. Argue that in any binary linear code, either all all codewords begin with a 0 of
exactly half of the codewords begin with a 0.

Exercise 1.16. Prove (1.10).

Exercise 1.17. Show that there is no binary code with block length 4 that achieves the Hamming
bound.
 37

Exercise 1.18. (∗) There are n people in a room, each of whom is given a black/white hat chosen
uniformly at random (and independent of the choices of all other people). Each person can see
the hat color of all other people, but not their own. Each person is asked if (s)he wishes to guess
their own hat color. They can either guess, or abstain. Each person makes their choice without
knowledge of what the other people are doing. They either win collectively, or lose collectively.
They win if all the people who don’t abstain guess their hat color correctly and at least one
person does not abstain. They lose if all people abstain, or if some person guesses their color
incorrectly. Your goal below is to come up with a strategy that will allow the n people to win
with pretty high probability. We begin with a simple warmup:

(a) Argue that the n people can win with probability at least 1
2 .

Next we will see how one can really bump up the probability of success with some careful mod-
eling, and some knowledge of Hamming codes. (Below are assuming knowledge of the general
Hamming code (see Section 2.4). If you do not want to skip ahead, you can assume that n = 7
in the last part of this problem.

(b) Lets say that a directed graph G is a subgraph of the n-dimensional hypercube if its vertex
set is {0, 1}n and if u → v is an edge in G, then u and v differ in at most one coordinate.
Let K (G) be the number of vertices of G with in-degree at least one, and out-degree zero.
Show that the probability of winning the hat problem equals the maximum, over directed
subgraphs G of the n-dimensional hypercube, of K (G)/2n.

(c) Using the fact that the out-degree of any vertex is at most n, show that K (G)/2n is at most
n
n+1 for any directed subgraph G of the n-dimensional hypercube.

(d) Show that if n = 2r − 1, then there exists a directed subgraph G of the n-dimensional hy-
percube with K (G)/2n = n
n+1 .

Hint: This is where the Hamming code comes in.

1.9 Bibliographic Notes

Coding theory owes its origin to two remarkable papers: one by Shannon and the other by Ham-
ming [52] both of which were published within a couple of years of each other. Shannon’s paper
deﬁned the BSCp channel (among others) and deﬁned codes in terms of its encoding func-
tion. Shannon’s paper also explicitly deﬁned the decoding function. Hamming’s work deﬁned
the notion of codes as in Deﬁnition 1.2.1 as well as the notion of Hamming distance. Both the
Hamming bound and the Hamming code are (not surprisingly) due to Hamming. The speciﬁc
deﬁnition of Hamming code that we used in this book was the one proposed by Hamming and
is also mentioned in Shannon’s paper (even though Shannon’s paper pre-dates Hamming’s).
The notion of erasures was deﬁned by Elias.
One hybrid model to account for the fact that in real life the noise channel is somewhere
in between the extremes of the channels proposed by Hamming and Shannon is the Arbitrary
Varying Channel (the reader is referred to the survey by Lapidoth and Narayan [66]).

38

Chapter 2

A Look at Some Nicely Behaved Codes:
Linear Codes

Let us now pause for a bit and think about how we can represent a code. In general, a code
C : [q]
k −→ [q]
n can be stored using nq k symbols from [q] (n symbols for each of the q k code-
words) or nq k log q bits. For constant rate codes, this is exponential space, which is prohibitive
even for modest values of k like k = 100. A natural question is whether we can do better. Intu-
itively, the code must have some extra structure that would facilitate a succinct representation.
We will now look at a class of codes called linear codes that have more structure than general
codes which leads to some other nice properties. We have already seen binary linear codes in
Section 1.5, that is: C ⊆ {0, 1}n is linear code if for all c1, c2 ∈ C , c1 +c2 ∈ C , where the “+" denotes
bit-wise XOR.

Deﬁnition 2.0.1 (Linear Codes). Let q be a prime power (i.e. q = p s for some prime p and
integer s ≥ 1). C ⊆ {0, 1, ..., q − 1}n is a linear code if it is a linear subspace of {0, 1, ..., q − 1}n. If C
has dimension k and distance d then it will be referred to as an [n, k, d ]q or just an [n, k]q code.

Of course, the above deﬁnition is not complete because we have not yet deﬁned a linear
subspace. We do that next.

2.1 Finite Fields

To deﬁne linear subspaces, we will need to work with (ﬁnite) ﬁelds. At a high level, we need
ﬁnite ﬁelds since when we talk about codes, we deal with ﬁnite symbols/numbers and we want
to endow these symbols with the same math that makes arithmetic over real numbers work.
Finite ﬁelds accomplish this precise task. We begin with a quick overview of ﬁelds.
Informally speaking, a ﬁeld is a set of elements on which one can do addition, subtraction,
multiplication and division and still stay in the set. More formally,

Deﬁnition 2.1.1. A ﬁeld F is given by a triple (S, +, ·), where S is the set of elements and +, · are
functions F × F → F with the following properties:

39

• CLOSURE: For every a, b ∈ S, we have both a + b ∈ S and a · b ∈ S.

• ASSOCIATIVITY: + and · are associative: that is, for every a, b, c ∈ S, a + (b + c) = (a + b) + c
and a · (b · c) = (a · b) · c.

• COMMUTATIVITY: + and · are commutative: that is, for every a, b ∈ S, a + b = b + a and
a · b = b · a.

• DISTRIBUTIVITY: · distributes over +: that is, for every a, b, c ∈ S, a · (b + c) = a · b + a · c.

• IDENTITIES: There exists special elements 0 and 1 in S such that the following holds for
every a ∈ S: a + 0 = a and a · 1 = a.

• INVERSES: For every a ∈ S, there exists its unique additive inverse −a such that a + (−a) =
0. Also for every a ∈ S \ {0}, there exists its unique multiplicative inverse a−1 such that
a · a−1 = 1.

With the usual semantics for + and ·, R (set of real number) is a ﬁeld, but Z (set of integers)
is not a ﬁeld as division of two integers results in a rational number that need not be an inte-
ger (the set of rational numbers itself is a ﬁeld though: see Exercise 2.1). In this course, we will
exclusively deal with ﬁnite ﬁelds. As the name suggests these are ﬁelds with a ﬁnite set of ele-
ments. (We will overload notation and denote the size of a ﬁeld |F| = |S|.) The following is a well
known result.

Theorem 2.1.1 (Size of Finite Fields). The size of any ﬁnite ﬁeld is p s for prime p and integer
s ≥ 1.

One example of a ﬁnite ﬁeld that we have seen is the ﬁeld with S = {0, 1}, which we will
denote by F2 (we have seen this ﬁeld in the context of binary linear codes). For F2, addition
is the XOR operation, while multiplication is the AND operation. The additive inverse of an
element in F2 is the number itself while the multiplicative inverse of 1 is 1 itself.
Let p be a prime number. Then the integers modulo p form a ﬁeld, denoted by Fp (and also
by Zp ), where the addition and multiplication are carried out modulo p. For example, consider
F7, where the elements are {0, 1, 2, 3, 4, 5, 6}. We have (4 + 3) mod 7 = 0 and 4 · 4 mod 7 = 2.
Further, the additive inverse of 4 is 3 as (3 + 4) mod 7 = 0 and the multiplicative inverse of 4 is 2
as 4 · 2 mod 7 = 1.
More formally, we prove the following result.

Lemma 2.1.2. Let p be a prime. Then Fp = ({0, 1, . . . , p − 1}, +p , ·p ) is a ﬁeld, where +p and ·p are
addition and multiplication modulo p.

Proof. The properties of associativity, commutativity, distributivity and identities hold for in-
tegers and hence, they hold for Fp . The closure property follows since both the “addition" and
“multiplication" are done modulo p, which implies that for any a, b ∈ {0, . . . , p −1}, a +p b, a ·p b ∈
{0, . . . , p −1}. Thus, to complete the proof, we need to prove the existence of unique additive and
multiplicative inverses.
 40

Fix an arbitrary a ∈ {0, . . . , p − 1}. Then we claim that its additive inverse is p − a mod p. It is
easy to check that a + p − a = 0 mod p. Next we argue that this is the unique additive inverse.
To see this note that the sequence a, a + 1, a + 2, . . . , a + p − 1 are p consecutive numbers and
thus, exactly one of them is a multiple of p, which happens for b = p − a mod p, as desired.
Now ﬁx an a ∈ {1, . . . , p − 1}. Next we argue for the existence of a unique multiplicative uni-
verse a−1. Consider the set of numbers T = {a ·p b|b ∈ {1, . . . , p − 1}}. We claim that all these
numbers are unique. To see this, note that if this is not the case, then there exist b1 ̸= b2 ∈
{0, 1, . . . , p − 1} such that a · b1 = a · b2 mod p, which in turn implies that a · (b1 − b2) = 0 mod p.
Since a and b1 −b2 are non-zero numbers, this implies that p divides a · (b1 −b2). Further, since
a and |b1 −b2| are both at most p −1, this implies that multiplying a and (b1 −b2) mod p results
in p, which is a contradiction since p is prime. Thus, we have argued that |T | = p − 1 and since
each number in T is in [p − 1], we have that T = [p − 1]. Thus, we can conclude that there exists
a unique element b such that a · b = 1 mod p and thus, b is the required a−1.

One might think that there could be different ﬁnite ﬁelds with the same number of elements.
However, this is not the case:

Theorem 2.1.3. For every prime power q there is a unique ﬁnite ﬁeld with q elements (up to
isomorphism1).

Thus, we are justiﬁed in just using Fq to denote a ﬁnite ﬁeld on q elements.

2.2 Linear Subspaces

We are ﬁnally ready to deﬁne the notion of a linear subspace.

Deﬁnition 2.2.1 (Linear Subspace). For any non-empty subset S ⊆ Fn
q is a linear subspace if the
following properties hold:

1. For every x, y ∈ S, x + y ∈ S, where the addition is vector addition over Fq (that is, do addi-
tion component wise over Fq ).

2. For every a ∈ Fq and x ∈ S, a ·x ∈ S, where the multiplication is done component-wise over
Fq .

Here is a (trivial) example of a linear subspace of F3
5:

S1 = {(0, 0, 0), (1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4)}. (2.1)

Note that for example (1, 1, 1) + (3, 3, 3) = (4, 4, 4) ∈ S1 and 2 · (4, 4, 4) = (3, 3, 3) ∈ S1 as required
by the deﬁnition. Here is another somewhat less trivial example of a linear subspace over F3
3:

S2 = {(0, 0, 0), (1, 0, 1), (2, 0, 2), (0, 1, 1), (0, 2, 2), (1, 1, 2), (1, 2, 0), (2, 1, 0), (2, 2, 1). (2.2)

Note that (1, 0, 1) + (0, 2, 2) = (1, 2, 0) ∈ S2 and 2 · (2, 0, 2) = (1, 0, 1) ∈ S2 as required.

1An isomorphism φ : S → S′ is a map (such that F = (S, +, ·) and F′ = (S′, ⊕, ◦) are ﬁelds) where for every a1, a2 ∈ S,
we have φ(a1 + a2) = φ(a1) ⊕ φ(a2) and φ(a1 · a2) = φ(a1) ◦ φ(a2).

41

Remark 2.2.1. Note that the second property implies that 0 is contained in every linear sub-
space. Further for any subspace over F2, the second property is redundant: see Exercise 2.4.

Before we state some properties of linear subspaces, we state some relevant deﬁnitions.

Deﬁnition 2.2.2 (Span). Given a set B = {v1, . . . , vℓ}. The span of B is the set of vectors
{ ℓ∑

i =1 ai · vi |ai ∈ Fq for every i ∈ [ℓ]

}
 .

Deﬁnition 2.2.3 (Linear independence of vectors). We say that v1, v2, . . . vk are linearly indepen-
dent if for every 1 ≤ i ≤ k and for every (k − 1)-tuple (a1, a2, . . . , ai −1, ai +1, . . . , ak ) ∈ Fk−1
q ,

vi ̸= a1v1 + . . . + ai −1vi −1 + ai +1vi +1 + . . . + ak vk .

In other words, vi is not in the span of the set {v1, . . . , vi −1, vi +1, . . . , vn}.

For example the vectors (1, 0, 1), (1, 1, 1) ∈ S2 are linearly independent.

Deﬁnition 2.2.4 (Rank of a matrix). The rank of matrix in F
k×k
q is the maximum number of
linearly independent rows (or columns). A matrix in Fk×n
q with rank min(k, n) is said to have full
rank.

One can deﬁne the row (column) rank of a matrix as the maximum number of linearly in-
dependent rows (columns). However, it is a well-known theorem that the row rank of a matrix
is the same as its column rank. For example, the matrix below over F3 has full rank (see Exer-
cise 2.5):
 G2 = ( 1 0 1
0 1 1
 ) . (2.3)

Any linear subspace satisﬁes the following properties (the full proof can be found in any
standard linear algebra textbook).

Theorem 2.2.1. If S ⊆ Fq n is a linear subspace then

1. |S| = q k for some k ≥ 0. The parameter k is called the dimension of S.

2. There exists at least one set of vectors v1, ..., vk ∈ S called basis elements such that every x ∈ S
can be expressed as x = a1v1 + a2v2 + ... + anvn where ai ∈ Fq for 1 ≤ i ≤ k. In other words,
there exists a full rank k × n matrix G (also known as a generator matrix) with entries from
Fq such that every x ∈ S, x = (a1, a2, ...ak ) · G where

G =
 





←− v1 −→
←− v2 −→
...
←− vk −→






 .

42

3. There exists a full rank (n − k) × n matrix H (called a parity check matrix) such that for
every x ∈ S, H xT = 0.

4. G and H are orthogonal, that is, G · H T = 0.

Proof Sketch.

Property 1. We begin with the proof of the ﬁrst property. For the sake of contradiction, let
us assume that q k < |S| < q k+1, for some k ≥ 0. Iteratively, we will construct a set of linearly
independent vectors B ⊆ S such that |B | ≥ k + 1. Note that by the deﬁnition of a linear subspace
the span of B should be contained in S. However, this is a contradiction as the size of the span
of B is at least
2 q k+1 > |S|.
To complete the proof, we show how to construct the set B in a greedy fashion. In the ﬁrst
step pick v1 to be any non-zero vector in S and set B ← {v1} (we can ﬁnd such a vector as |S| >
q k ≥ 1). Now say after the step t (for some t ≤ k), |B | = t . Now the size of the span of the current
B is q t ≤ q k < |S|. Thus there exists a vector vt +1 ∈ S \ B that is linearly independent of vectors
in B . Set B ← B ∪ {vt +1}. Thus, we can continue building B until |B | = k + 1, as desired.

Property 2. We ﬁrst note that we can pick B = {v1, . . . , vk } to be any set of k linearly indepen-
dent vectors– this just follows from the argument above for Property 1.1. This is because the
span of B is contained in S. However, since |S| = q k and the span of B has q k vectors, the two
have to be the same.

Property 3. Property 3 above follows from another fact that every linear subspace S has a null
space N ⊆ Fn
q such that for every x ∈ S and y ∈ N , 〈x, y〉 = 0. Further, it is known that N itself is
a linear subspace of dimension n − k. (The claim that N is also a linear subspace follows from
the following two facts: for every x, y, z ∈ Fn
q , (i) 〈x, y + z〉 = 〈x, y〉 + 〈x, z〉 and (ii) for any a ∈ Fq ,
〈x, ay〉 = a ·〈x, y〉.) In other words, there exists a generator matrix H for it. This matrix H is called
the parity check matrix of S.

Property 4. See Exercise 2.8.

As examples, the linear subspace S1 in (2.1) has as one of its generator matrices

G1 = ( 1 1 1 )

and as one of its parity check matrices
 H1 = ( 1 2 2
2 2 1
 ) .

Further, the linear subspace S2 in (2.2) has G2 as one of its generator matrices and has the fol-
lowing as one of its parity check matrices

H2 = ( 1 1 2 ) .

Finally, we state another property of linear subspaces that is useful.

2See Exercise 2.7.
 43

Lemma 2.2.2. Given matrix G of dimension k × n that is a generator matrix of subspace S1 and
matrix H of dimension (n −k)×n that is a parity check matrix of subspace S2 such that G H T = 0,
then S1 = S2.

Proof. We ﬁrst prove that S1 ⊆ S2. Given any c ∈ S1, there exists x ∈ Fk
q such that c = xG. Then,

H · cT = H · (xG)T = HG T xT = (
G H T )T xT = 0,

which implies that c ∈ S2, as desired.
To complete the proof note that as H has full rank, its null space (or S2) has dimension
n − (n − k) = k (this follows from a well known fact from linear algebra called the rank-nullity
theorem). Now as G has full rank, the dimension of S1 is also k. Thus, as S1 ⊆ S2, it has to be the
case that S1 = S2.3

2.3 Properties of Linear Codes

Theorem 2.2.1 gives two alternate characterizations of an [n, k]q linear code C :

• C is generated by its k × n generator matrix G. As an example that we have already seen,
the [7, 4, 3]2 Hamming code has the following generator matrix:

G =
 





 1 0 0 0 0 1 1
0 1 0 0 1 0 1
0 0 1 0 1 1 0
0 0 0 1 1 1 1







• C is also characterized by an (n −k)×n parity check matrix H . We claim that the following
matrix is a parity check matrix of the [7, 4, 3]2 Hamming code:

H =
 

 0 0 0 1 1 1 1
0 1 1 0 0 1 1
1 0 1 0 1 0 1




Indeed, it can be easily veriﬁed that G · H T = 0. Then Lemma 2.2.2 proves that H is indeed
a parity check matrix of the [7, 4, 3]2 Hamming code.

We now look at some consequences of the above characterizations of an [n, k]q linear code
C . We started this chapter with a quest for succinct representation of a code. Note that both the
generator matrix and the parity check matrix can be represented using O(n2) symbols from Fq
(which is much smaller than the exponential representation of a general code). More precisely
(see Exercise 2.10),

3If not, S1 ⊂ S2 which implies that that |S2| ≥ |S1| + 1. The latter is not possible if both S1 and S2 have the same
dimension.
 44

Proposition 2.3.1. Any [n, k]q linear code can be represented with min(nk, n(n − k)) symbols
from Fq .

There is an encoding algorithm for C that runs in O(n2) (in particular O(kn)) time– given a
message m ∈ Fk
q , the corresponding codeword C (m) = m · G, where G is the generator matrix of
C . (See Exercise 2.11.)

Proposition 2.3.2. For any [n, k]q linear code, given its generator matrix, encoding can be done
with O(nk) operations over Fq .

There is an error-detecting algorithm for C that runs in O(n2). This is a big improvement
over the naive brute force exponential time algorithm (that goes through all possible codewords
c ∈ C and checks if y = c). (See Exercise 2.12.)

Proposition 2.3.3. For any [n, k]q linear code, given its parity check matrix, error detection can
be performed in O(n(n − k)) operations over Fq .

Next, we look at some alternate characterizations of the distance of a linear code.

2.3.1 On the Distance of a Linear Code

We start with the following property, which we have seen for the special case of binary linear
codes (Proposition 1.5.3).

Proposition 2.3.4. For a [n, k, d ]q code C ,

d = min
c∈C ,
c̸=0 w t (c).

Proof. To show that d is the same as the minimum weight we show that d is no more than the
minimum weight and d is no less than the minimum weight.
First, we show that d is no more than the minimum weight. We can see this by considering
∆(0, c′) where c′ is the non-zero codeword in C with minimum weight; its distance from 0 is
equal to its weight. Thus, we have d ≤ w t (c′), as desired.
Now, to show that d is no less than the minimum weight, consider c1 ̸= c2 ∈ C such that
∆(c1, c2) = d . Note that c1 − c2 ∈ C (this is because −c2 = −1 · c2 ∈ C , where −1 is the additive
inverse of 1 in Fq and c1 − c2 = c1 + (−c2), which in in C by the deﬁnition of linear codes). Now
note that w t (c1 − c2) = ∆(c1, c2) = d , since the non-zero symbols in c1 − c2 occur exactly in the
positions where the two codewords differ. Further, since c1 ̸= c2, c1 − c2 ̸= 0, which implies that
the minimum Hamming weight of any non-zero codeword in C is at most d .

Next, we look at another property implied by the parity check matrix of a linear code.

Proposition 2.3.5. For any [n, k, d ]q code C with parity check matrix H , d is the minimum num-
ber of linearly dependent4 columns in H .

4A set of vectors is linearly dependent if it is not linearly independent.

45

Proof. By Proposition 2.3.4, we need to show that the minimum weight of a non-zero codeword
in C is the minimum number of linearly dependent columns. Let t be the minimum number of
linearly dependent columns in H . To prove the claim we will show that t ≤ d and t ≥ d .
For the ﬁrst direction, Let c ̸= 0 ∈ C be a codeword with w t (c) = d . Now note that, by the
deﬁnition of the parity check matrix, H ·cT = 0. Working through the matrix multiplication, this
gives us that ∑n
i =1 ci H i , where

H =
 

 ↑ ↑ ↑ ↑
H 1 H 2 · · · H i · · · H n

↓ ↓ ↓ ↓
 



and c = (c1, . . . , cn). Note that we can skip multiplication for those columns for which the corre-
sponding bit ci is zero, so for this to be zero, those H i with ci ̸= 0 are linearly dependent. This
means that d ≥ t , as the columns corresponding to non-zero entries in c are one instance of
linearly dependent columns.
For the other direction, consider the minimum set of columns from H , H i1, H i2, . . . , H it that
are linearly dependent. This implies that there exists non-zero elements c ′
i1, . . . , c ′
it ∈ Fq such

that c ′
ii H i1 + . . . + c ′
it H it = 0. (Note that all the c ′
i j are non-zero as no set of less than t columns

are linearly dependent.) Now extend c ′
i1, . . . , c ′
it to the vector c′ such that c ′
j = 0 for j ̸∈ {i1, . . . , i t }.

Note that we have H · (
c′)T = 0 and thus, we have c′ ∈ C . This in turn implies that d ≤ w t (c′) = t
(where recall t is the minimum number of linearly independent columns in H ).

2.4 Hamming Codes

We now change gears and look at the general family of linear codes, which were discovered by
Hamming. So far we have seen the [7, 4, 3]2 Hamming code (in Section 1.5). In fact, for any r ≥ 2
there is a [2r − 1, 2r − r − 1, 3]2 Hamming code. Thus in Section 1.5, we have seen this code for
r = 3.

Deﬁnition 2.4.1. Deﬁne the r × (2r − 1) matrix Hr over F2, such that the i th column H
i
r , 1 ≤ i ≤
2r − 1, is the binary representation of i (note that such a representation is a vector in {0, 1}r ).

For example, for the case we have seen (r = 3),

H3 =
 


0 0 0 1 1 1 1
0 1 1 0 0 1 1
1 0 1 0 1 0 1


 .

Note that by its deﬁnition, the code that has Hr as its parity check matrix has block length 2r −1
and dimension 2r − r − 1. This leads to the formal deﬁnition of the general Hamming code.

Deﬁnition 2.4.2. The [2r −1, 2r −r −1]2 Hamming code, denoted by C H ,r has parity check matrix
Hr .
 46

In other words, the general [2r − 1, 2r − r − 1]2 Hamming code is the code

{c ∈ {0, 1}2r −1|Hr · cT = 0}.

Next we argue that the above Hamming code has distance 3 (in Proposition 1.5.1, we argued
this for r = 3).

Proposition 2.4.1. The Hamming code [2r − 1, 2r − r − 1, 3]2 has distance 3.

Proof. No two columns in Hr are linearly dependent. If they were, we would have H
i
r + H j
r =
0, but this is impossible since they differ in at least one bit (being binary representations of
integers, i ̸= j ). Thus, by Proposition 2.3.5, the distance is at least 3. It is at most 3, since (e.g.)
H
1
r + H
2
r + H
3
r = 0.

Now note that under the Hamming bound for d = 3 (Theorem 1.6.1), k ≤ n − log2(n + 1), so
for n = 2r − 1, k ≤ 2r − r − 1. Hence, the Hamming code is a perfect code. (See Deﬁnition 1.7.2.)
In Question 1.7.1, we asked which codes are perfect codes. Interestingly, the only perfect
binary codes are the following:

• The Hamming codes which we just studied.

• The trivial [n, 1, n]2 codes for odd n (which have 0n and 1n as the only codewords): see
Exercise 2.22.

• Two codes due to Golay [36].

2.5 Family of codes

Until now, we have mostly studied speciﬁc codes, that is, codes with ﬁxed block lengths and
dimension. The only exception was the “family" of [2r − 1, 2r − r − 1, 3]2 Hamming codes (for
r ≥ 2) that we studied in the last section. We will see shortly, when we do an asymptotic study
of codes, that it makes more sense to talk about a family of codes. First, we deﬁne the notion of
family of codes:

Deﬁnition 2.5.1 (Family of codes). Let q ≥ 2. Let {ni }i ≥1 be an increasing sequence of block
lengths and suppose there exists sequences {ki }i ≥1 and {di }i ≥1 such that for all i ≥ 1 there exists
an (ni , ki , di )q code Ci . Then the sequence C = {Ci }i ≥1 is a family of codes. The rate of C is
deﬁned as
 R(C ) = lim
i →∞
 { ki
ni
 } .

The relative distance of C is deﬁned as
δ(C ) = lim
i →∞
 { di
ni
 } .

47

For example, C H the family of Hamming code is a family of codes with ni = 2i − 1, ki = 2i −
i − 1, di = 3 and thus,
 R(C H ) = lim
i →∞ 1 − i

2i − 1 = 1,

and
 δ(C H ) = lim
i →∞ 3

2i − 1 = 0.

We will mostly work with families of codes from now on. This is necessary as we will study the
asymptotic behavior of algorithms for codes, which does not make sense for a ﬁxed code. For
example, when we say that a decoding algorithm for a code C takes O(n2) time, we would be
implicitly assuming that C is a family of codes and that the algorithm has an O(n2) running time
when the block length is large enough. From now on, unless mentioned otherwise, whenever
we talk about a code, we will be implicitly assuming that we are talking about a family of codes.
Given that we can only formally talk about asymptotic run time of algorithms, we now also
state our formal notion of efﬁcient algorithms:

We’ll call an algorithm related to a code of block length n to be efﬁcient, if it runs in time
polynomial in n.

For all the speciﬁc codes that we will study in this book, the corresponding family of codes
will be a “family" in a more natural sense. By this we mean that all the speciﬁc codes in a family
of codes will be the “same" code except with different parameters. A bit more formally, we will
consider families {Ci }i ≥1, where given only the ‘index’ i , one can compute a sufﬁcient descrip-
tion of Ci efﬁciently.5

Finally, the deﬁnition of a family of codes allows us to present the ﬁnal version of the big
motivating question for the book. The last formal version of the main question we considered
was Question 1.4.1, where we were interested in the tradeoff of rate R and distance d . The
comparison was somewhat unfair because R was a ratio while d was an integer. A more appro-
priate comparison should be between rate R and the relative distance δ. Further, we would be
interested in tackling the main motivating question for families of codes, which results in the
following ﬁnal version:

Question 2.5.1. What is the optimal tradeoff between R(C ) and δ(C ) that can be achieved by
some code family C ?

5We stress that this is not always going to be the case. In particular, we will consider “random" codes where this
efﬁcient constructibility will not be true.
 48

2.6 Efﬁcient Decoding of Hamming codes

We have shown that the Hamming code has a distance of 3 and thus, by Proposition 1.4.1, can
correct one error. However, this is a combinatorial result and does not give us an efﬁcient al-
gorithm. One obvious candidate for decoding is the MLD function. Unfortunately, the only
implementation of MLD that we know is the one in Algorithm 2, which will take time 2Θ(n),
where n is the block length of the Hamming code. However, we can do much better. Consider
the following simple algorithm: given the received word y, ﬁrst check if it is indeed a valid code-
word. If it is, we are done. Otherwise, ﬂip each of the n bits and check if the resulting vector is
a valid codeword. If so, we have successfully decoded from one error. (If none of the checks are
successful, then we declare a decoding failure.) Algorithm 3 formally presents this algorithm
(where C H ,r is the [2r − 1, 2r − r − 1, 3]2 Hamming code).6

Algorithm 3 Naive Decoder for Hamming Code
INPUT: Received word y
OUTPUT: c if ∆(y, c) ≤ 1 else Fail

1: IF y ∈ C H ,r THEN

2: RETURN y

3: FOR i = 1 . . . n DO

4: y
′ ← y + ei ⊲ ei is the i th standard basis vector

5: IF y
′ ∈ C H ,r THEN

6: RETURN y
′

7: RETURN Fail

It is easy to check that Algorithm 3 can correct up to 1 error. If each of the checks y
′ ∈ C H ,r
can be done in T (n) time, then the time complexity of the proposed algorithm will be O(nT (n)).
Note that since C H ,r is a linear code (and dimension k = n − O(log n)) by Proposition 2.3.3, we
have T (n) = O(n log n). Thus, the proposed algorithm has running time O(n2 log n).
Note that Algorithm 3 can be generalized to work for any linear code C with distance 2t +
1 (and hence, can correct up to t errors): go through all possible error vectors z ∈ [q]
n (with
w t (z) ≤ t ) and check if y − z is in the code or not. Algorithm 4 presents the formal algorithm
(where C is an [n, k, 2t + 1]q code).
The number of error patterns z considered by Algorithm 4 is7 ∑t
i =0 (n
i )
(q − 1)i ≤ O((nq)t ).
Further by Proposition 2.3.3, Step 4 can be performed with O(n2) operations over Fq . Thus, Al-
gorithm 4 runs with O(nt +2q t ) operations over Fq , which for q being a small polynomial in n,
is nO(t ) operations. In other words, the algorithm will have polynomial running time for codes
with constant distance (though the running time would not be practical even for moderate val-
ues of t ).

6Formally speaking, a decoding algorithm should return the transmitted message x but Algorithm 3 actually
returns C H ,r (x). However, since C H ,r is a linear code, it is not too hard to see that one can obtain x from C H ,r (x) in
O(n3) time: see Exercise 2.23. Further, for C H ,r one can do this in O(n) time: see Exercise 2.24.
7Recall (1.15).
 49

Algorithm 4 Decoder for Any Linear Code
INPUT: Received word y
OUTPUT: c ∈ C if ∆(y, c) ≤ t else Fail

1: FOR i = 0 . . . t DO

2: FOR S ⊆ [n] such that |S| = i DO

3: FOR z ∈ Fn
q such that w t (zS) = w t (z) = i DO

4: IF y − z ∈ C THEN

5: RETURN y − z

6: RETURN Fail

However, it turns out that for Hamming codes there exists a decoding algorithm with an
O(n2) running time. To see this, ﬁrst note that if the received word y has no errors, then Hr ·y
T =
0. If not, then y = c + ei , where c ∈ C and ei is the unit vector with the only nonzero element at
the i -th position. Thus, if H
i
r stands for the i -th column of Hr ,

Hr · y
T = Hr · cT + Hr · (ei )T = Hr · (ei )T = H
i
r ,

where the second equality follows as Hr · cT = 0, which in turn follows from the fact that c ∈ C .
In other words, Hr · y
T gives the location of the error. This leads to Algorithm 5.

Algorithm 5 Efﬁcient Decoder for Hamming Code
INPUT: Received word y
OUTPUT: c if ∆(y, c) ≤ 1 else Fail

1: b ← Hr · y
T .

2: Let i ∈ [n] be the number whose binary representation is b

3: IF y − ei ∈ C H THEN

4: RETURN y − ei

5: RETURN Fail

Note that Hr is an r × n matrix where n = 2r − 1 and thus, r = Θ(log n). This implies Step 1 in
Algorithm 5, which is a matrix vector multiplication can be done in time O(n log n). By a similar
argument and by Proposition 2.3.3 Step 3 can be performed in O(n log n) time, and therefore
Algorithm 5 overall runs in O(n log n) time. Thus,

Theorem 2.6.1. The [n = 2r −1, 2r −r −1, 3]2 Hamming code is 1-error correctable. Furthermore,
decoding can be performed in time O(n log n).

2.7 Dual of a Linear Code

Until now, we have thought of parity check matrix as deﬁning a code via its null space. However,
we are not beholden to think of the parity check matrix in this way. A natural alternative is to use
the parity check matrix as a generator matrix. The following deﬁnition addresses this question.

50

Deﬁnition 2.7.1 (Dual of a code). Let H be a parity check matrix of a code C , then the code
generated by H is called the dual of C . For any code C , its dual is denoted by C ⊥.

It is obvious from the deﬁnition that if C is an [n, k]q code, then C ⊥ is an [n, n − k]q code.
The ﬁrst example that might come to mind is C ⊥
H ,r , which is also known as the Simplex code
(we will denote it by CSi m,r ). Adding an all 0’s column to Hr and using the resulting matrix as
a generating matrix, we get the Hadamard code (we will denote it by C H ad , r ). We claim that
CSi m,r and C H ad ,r are [2r − 1, r, 2r −1]2 and [2r , r, 2r −1]2 codes respectively. The claimed block
length and dimension follow from the deﬁnition of the codes, while the distance follows from
the following result.

Proposition 2.7.1. CSi m,r and C H ad ,r both have distances of 2r −1.

Proof. We ﬁrst show the result for C H ad ,r . In fact, we will show something stronger: every non-
zero codeword in C H ad ,r has weight exactly equal to 2r −1 (the claimed distance follows from
Proposition 2.3.4). Consider a message x ̸= 0. Let its i th entry be xi = 1. x is encoded as

c = (x1, x2, . . . , xr )(H 0
r , H 1
r , . . . , H 2r −1
r ),

where H j
r is the binary representation of 0 ≤ j ≤ 2r − 1 (that is, it contains all the vectors in
{0, 1}r ). Further note that the j th bit of the codeword c is 〈x, H j
r 〉. Group all the columns of the
generator matrix into pairs (u, v) such that v = u + ei (i.e. v and u are the same except in the i th
position). Notice that this partitions all the columns into 2r −1 disjoint pairs. Then,

〈x, v〉 = 〈x, u + ei 〉 = 〈x, u〉 + 〈x, ei 〉 = 〈x, u〉 + xi = 〈x, u〉 + 1.

Thus we have that exactly one of 〈x, v〉 and 〈x, u〉 is 1. As the choice of the pair (u, v) was arbitrary,
we have proved that for any non-zero codeword c such that c ∈ C H ad , w t (c) = 2r −1.
For the simplex code, we observe that all codewords of C H ad ,3 are obtained by padding a 0 to
the beginning of the codewords in CSi m,r , which implies that all non-zero codewords in CSi m,r
also have a weight of 2r −1, which completes the proof.

We remark that the family of Hamming code has a rate of 1 and a (relative) distance of 0
while the families of Simplex/Hadamard codes have a rate of 0 and a relative distance of 1/2.
Notice that both code families either have rate or relative distance equal to 0. Given this, the
following question is natural special case of Question 2.5.1:

Question 2.7.1. Does there exist a family of codes C such that R(C ) > 0 and δ(C ) > 0 hold
simultaneously?

Codes that have the above property are called asymptotically good.

51

2.8 Exercises

Exercise 2.1. Prove that the set of rationals (i.e. the set of reals of the form a
b , where both a and
b ̸= 0 are integers), denoted by Q, is a ﬁeld.

Exercise 2.2. Let q be a prime power. Let x ∈ Fq such that x ̸∈ {0, 1}. Then prove that for any
n ≤ q − 1: n∑

i =0 xi = xn+1 − 1
x − 1 .

Exercise 2.3. The main aim of this exercise is to prove the following identity that is true for any
α ∈ Fq : αq = α (2.4)

To make progress towards the above we will prove a sequence of properties of groups. A group G
is a pair (S, ◦) where the operator ◦ : G ×G → G such that ◦ is commutative8 and the elements of S
are closed under ◦. Further, there is a special element ι ∈ S that is the identity element and every
element a ∈ S has an inverse element b ∈ S such that a ◦ b = ι. Note that a ﬁnite ﬁeld Fq consists
of an additive group with the + operator (and 0 as additive identity) and a multiplicative group
on the non-zero elements of Fq (which is also denoted by F∗
q ) with the · operator (and 1 as the
multiplicative identity).9

For the rest of the problem let G = (S, ·) be a multiplicative group with |G| = m. Prove the
following statements.

1. For any β ∈ G, let o(β) be the smallest integer o such that βo = 1. Prove that such an o ≤ m
always exists. Further, argue that T = {1, β, . . . , βo−1} also forms a group. (T, ·) is called a
sub-group of G and o(β) is called the order of β.

2. For any g ∈ G, deﬁne the coset (w.r.t. T ) as

g T = {g · β|β ∈ T }.

Prove that if g ·h−1 ∈ T then g T = hT and g T ∩hT = ; otherwise. Further argue that these
cosets partition the group G into disjoint sets.

3. Argue that for any g ∈ G, we have |g T | = |T |.

4. Using the above results or otherwise, argue that for any β ∈ G, we have

βm = 1.

5. Prove (2.4).

Exercise 2.4. Prove that for q = 2, the second condition in Deﬁnition 2.2.1 is implied by the ﬁrst
condition.

8Technically, G is an abelian group.
9Recall Deﬁnition 2.1.1.
 52

Exercise 2.5. Prove that G2 from (2.3) has full rank.

Exercise 2.6. In this problem we will look at the problem of solving a system of linear equa-
tions over Fq . That is, one needs to solve for unknowns x1, . . . , xn given the following m linear
equations (where ai , j , bi ∈ Fq for 1 ≤ i ≤ m and 1 ≤ j ≤ n):

a1,1x1 + a1,2x2 + · · · + a1,n xn = b1.

a2,1x1 + a2,2x2 + · · · + a2,n xn = b2.

...

am,1x1 + am,2x2 + · · · + am,n xn = bm.

1. (Warm-up) Convince yourself that the above problem can be stated as A · xT = b
T , where
A is an m × n matrix over Fq , x ∈ Fn
q and b ∈ Fm
q .

2. (Upper Triangular Matrix) Assume n = m and that A is upper triangular, i.e. all diagonal
elements (ai ,i ) are non-zero and all lower triangular elements (ai , j , i > j ) are 0. Then
present an O(n2) time
10 algorithm to compute the unknown vector x.

3. (Gaussian Elimination) Assume that A has full rank (or equivalently a rank of n.)

(a) Prove that the following algorithm due to Gauss converts A into an upper triangular
matrix. By permuting the columns if necessary make sure that a1,1 ̸= 0. (Why can
one assume w.l.o.g. that this can be done?) Multiply all rows 1 < i ≤ n with a1,1
ai ,1 and
then subtract a1, j from the (i , j )th entry 1 ≤ j ≤ n. Recurse with the same algorithm
on the (n −1)×(n −1) matrix A′ obtained by removing the ﬁrst row and column from
A. (Stop when n = 1.)

(b) What happens if A does not have full rank? Show how one can modify the algorithm
above to either upper triangulate a matrix or report that it does not have full rank.
(Convince yourself that your modiﬁcation works.)

(c) Call a system of equations A · xT = b
T consistent if there exists a solution to x ∈ Fn
q .
Show that there exists an O(n3) algorithm that ﬁnds the solution if the system of
equations is consistent and A has full rank (and report “fail" otherwise).

4. (m < n case) Assume that A has full rank, i.e. has a rank of m. In this scenario either the
system of equations is inconsistent or there are q n−m solutions to x. Modify the algorithm
from above to design an O(m2n) time algorithm to output the solutions (or report that the
system is inconsistent).

• Note that in case the system is consistent there will be q n−m solutions, which might
be much bigger than O(m2n). Show that this is not a problem as one can represent
the solutions as system of linear equations. (I.e. one can have n − m “free" variables
and m “bound" variables.)

10For this problem, any basic operation over Fq takes unit time.

53

5. (m > n case) Assume that A has full rank, i.e. a rank of n. In this scenario either the
system of equations is inconsistent or there is a unique solution to x. Modify the algorithm
from above to design an O(m2n) time algorithm to output the solution (or report that the
system is inconsistent).

6. (Non-full rank case) Give an O(m2n) algorithm for the general case, i.e. the m ×n matrix A
need not have full rank. (The algorithm should either report that the system of equations
is inconsistent or output the solution(s) to x.)

Exercise 2.7. Prove that the span of k linearly independent vectors over Fq has size exactly q k .

Exercise 2.8. Let G and H be a generator and parity check matrix of the same linear code of
dimension k and block length n. Then G · H T = 0.

Exercise 2.9. Let C be an [n, k]q linear code with a generator matrix with no all zeros columns.
Then for every position i ∈ [n] and α ∈ Fq , the number of codewords c ∈ C such that ci = α is
exactly q k−1.

Exercise 2.10. Prove Proposition 2.3.1.

Exercise 2.11. Prove Proposition 2.3.2.

Exercise 2.12. Prove Proposition 2.3.3.

Exercise 2.13. A set of vector S ⊆ Fn
q is called t -wise independent if for every set of positions
I with |I | = t , the set S projected to I has each of the vectors in Ft
q appear the same number
of times. (In other words, if one picks a vector (s1, . . . , sn) from S at random then any of the t
random variables are uniformly and independently random over Fq ).
Prove that any linear code C whose dual C ⊥ has distance d ⊥ is (d ⊥ − 1)-wise independent.

Exercise 2.14. A set of vectors S ⊆ Fk
2 is called ε-biased sample space if the following property
holds. Pick a vector X = (x1, . . . , xk ) uniformly at random from S. Then X has bias at most ε, that
is, for every I ⊆ [k], ∣Pr
 (∑

i ∈I xi = 0
)
 − Pr
 (∑

i ∈I xi = 1
)∣ ≤ ε.

We will look at some connections of such sets to codes.

1. Let C be an [n, k]2 code such that all non-zero codewords have Hamming weight in the
range [( 1

2 − ε) n, ( 1
2 + ε) n]
. Then there exists an ε-biased space of size n.

2. Let C be an [n, k]2 code such that all non-zero codewords have Hamming weight in the
range [( 1
2 − γ
) n, ( 1
2 + γ
) n] for some constant 0 < γ < 1/2. Then there exists an ε-biased

space of size nO(γ
−1·log(1/ε)).

Exercise 2.15. Let C be an [n, k, d ]q code. Let y = (y1, . . . , yn) ∈ (Fq ∪ {?})n be a received word11

such that yi =? for at most d − 1 values of i . Present an O(n3) time algorithm that outputs a
codeword c = (c1, . . . , cn) ∈ C that agrees with y in all un-erased positions (i.e., ci = yi if yi ̸=?) or
states that no such c exists. (Recall that if such a c exists then it is unique.)

11A ? denotes an erasure.
 54

Exercise 2.16. In the chapter, we did not talk about how to obtain the parity check matrix of a
linear code from its generator matrix. In this problem, we will look at this “conversion" proce-
dure.

(a) Prove that any generator matrix G of an [n, k]q code C (recall that G is a k × n matrix) can
be converted into another equivalent generator matrix of the form G
′ = [Ik |A], where Ik is
the k × k identity matrix and A is some k × (n − k) matrix. By “equivalent," we mean that
the code generated by G
′ has a linear bijective map to C .

Note that the code generated by G
′ has the message symbols as its ﬁrst k symbols in the
corresponding codeword. Such codes are called systematic codes. In other words, every
linear code can be converted into a systematic code. Systematic codes are popular in
practice as they allow for immediate access to the message symbols.

(b) Given an k × n generator matrix of the form [Ik |A], give a corresponding (n − k) × n par-
ity check matrix. Brieﬂy justify why your construction of the parity check matrix is correct.

Hint: Try to think of a parity check matrix that can be decomposed into two submatrices: one will be closely

related to A and the other will be an identity matrix, though the latter might not be a k × k matrix).

(c) Use part (b) to present a generator matrix for the [2r − 1, 2r − r − 1, 3]2 Hamming code.

Exercise 2.17. So far in this book we have seen that one can modify one code to get another
code with interesting properties (for example, the construction of the Hadamard code from the
Simplex code from Section 2.7 and Exercise 1.7). In this problem you will need to come up with
more ways of constructing new codes from existing ones.
Prove the following statements (recall that the notation (n, k, d )q code is used for general
codes with q k codewords where k need not be an integer, whereas the notation [n, k, d ]q code
stands for a linear code of dimension k):

1. If there exists an (n, k, d )2m code, then there also exists an (nm, km, d ′ ≥ d )2 code.

2. If there exists an [n, k, d ]2m code, then there also exists an [nm, km, d ′ ≥ d ]2 code.

3. If there exists an [n, k, d ]q code, then there also exists an [n − d , k − 1, d ′ ≥ ⌈d /q⌉]q code.

4. If there exists an [n, k, δn]q code, then for every m ≥ 1, there also exists an (
nm, k/m, (
1 − (1 − δ)m) · nm)
q m
code.

5. If there exists an [n, k, δn]2 code, then for every odd m ≥ 1, there also exists an [
nm, k, 1
2 · (
1 − (1 − 2δ)m) · nm

code.

Note: In all the parts, the only things that you can assume about the original code are only the
parameters given by its deﬁnition– nothing else!

55

Exercise 2.18. Let C1 be an [n, k1, d1]q code and C2 be an [n, k2, d2]q code. Then deﬁne a new
code as follows: C1 ⊖C2 = {(c1, c1 + c2)|c1 ∈ C1, c2 ∈ C2}.

Next we will prove interesting properties of this operations on codes:

1. If Gi is the generator matrix for Ci for i ∈ [2], what is a generator matrix for C1 ⊖C2?

2. Argue that C1 ⊖C2 is an [2n, k1 + k2, d def
= min(2d1, d2)]q code.

3. Assume there exists algorithms Ai for code Ci for i ∈ [2] such that: (i) A1 can decode from
e errors and s erasures such that 2e +s < d1 and (ii) A2 can decode from ⌊(d2−1)/2⌋ errors.
Then argue that one can correct ⌊(d − 1)/2⌋ errors for C1 ⊖C2.

Hint: Given a received word (y1, y2) ∈ Fn
q ×Fn
q , ﬁrst apply A2 on y2 −y1. Then create an intermediate received

word for A1.

4. We will now consider a recursive construction of a binary linear code that uses the ⊖ op-
erator. For integers 0 ≤ r ≤ m, we deﬁne the code C (r, m) as follows:

• C (r, r ) = Fr
2 and C (0, r ) is the code with only two codewords: the all ones and all
zeroes vector in Fr
2.

• For 1 < r < m, C (r, m) = C (r, m − 1) ⊖C (r − 1, m − 1).

Determine the parameters of the code C (r, m).

Exercise 2.19. Let C1 be an [n1, k1, d1]2 binary linear code, and C2 an [n2, k2, d2] binary linear
code. Let C ⊆ Fn1×n2
2 be the subset of n1 × n2 matrices whose columns belong to C1 and whose
rows belong to C2. C is called the tensor of C1 and C2 and is denoted by C1 ⊗C2.
Prove that C is an [n1n2, k1k2, d1d2]2 binary linear code.

Exercise 2.20. In Section 2.4 we considered the binary Hamming code. In this problem we will
consider the more general q-ary Hamming code. In particular, let q be a prime power and r ≥ 1
be an integer. Deﬁne the following r × n matrix Hq,r , where each column is an non-zero vector
from Fr
q such that the ﬁrst non-zero entry is 1. For example,

H3,2 = (
0 1 1 1
1 0 1 2
)

In this problem we will derive the parameters of the code. Deﬁne the generalized Hamming
code C H ,r,q to be the linear code whose parity check matrix is Hq,r . Argue that

1. The block length of C H ,r,q is n = q r −1
q−1 .

2. C H ,q,r has dimension n − r .

3. C H ,q,r has distance 3.
 56

Exercise 2.21. Design the best 6-ary code (family) with distance 3 that you can.

Hint: Start with a 7-ary Hamming code.

Exercise 2.22. Prove that the [n, 1, n]2 code for odd n (i.e. the code with the all zeros and all ones
vector as it only two codewords) attains the Hamming bound (Theorem 1.7.1).

Exercise 2.23. Let C be an [n, k]q code with generator matrix G. Then given a codeword c ∈ C
one can compute the corresponding message in time O(kn2).

Exercise 2.24. Given a c ∈ C H ,r , one can compute the corresponding message in time O(n).

Exercise 2.25. Let C be an (n, k)q code. Prove that if C can be decoded from e errors in time
T (n), then it can be decoded from n + c errors in time O((nq)c · T (n)).

Exercise 2.26. Show that the bound of kd of the number of ones in the generator matrix of any
binary linear code (see Exercise 1.14) cannot be improved for every code.

Exercise 2.27. Let C be a linear code. Then prove that (
C ⊥)⊥ = C .

Exercise 2.28. Note that for any linear code C , the codewords 0 is in both C and C ⊥. Show that
there exists a linear code C such that it shares a non-zero codeword with C ⊥.

Exercise 2.29. We go into a bit of diversion and look at how ﬁnite ﬁelds are different from inﬁnite
ﬁelds (e.g. R). Most of the properties of linear subspaces that we have used for linear codes (e.g.
notion of dimension, the existence of generator and parity check matrices, notion of duals) also
hold for linear subspaces over R.12 One trivial property that holds for linear subspaces over
ﬁnite ﬁelds that does not hold over R is that linear subspaces over Fq with dimension k has size
q k (though this is a trivial consequence that Fq are ﬁnite ﬁeld while R is an inﬁnite ﬁeld). Next,
we consider a more subtle distinction.
Let S ⊆ Rn be a linear subspace over R and let S⊥ is the dual of S. Then show that

S ∩ S⊥ = {0} .

By contrast, linear subspaces over ﬁnite ﬁelds can have non-trivial intersection with their duals
(see e.g. Exercise 2.28).

Exercise 2.30. A linear code C is called self-orthogonal if C ⊆ C ⊥. Show that

1. The binary repetition code with even number of repetitions is self-orthogonal.

2. The Hadamard code C H ad ,r is self-orthogonal.

Exercise 2.31. A linear code C is called self dual if C = C ⊥. Show that for

1. Any self dual code has dimension n/2.

2. Prove that the following code is self-dual

{(x, x)|x ∈ Fk
2 }.

12A linear subspace S ⊆ R
n is the same as in Deﬁnition 2.2.1 where all occurrences of the ﬁnite ﬁeld Fq is replaced
by R.
 57

Exercise 2.32. Given a code C a puncturing of C is another code C ′ where the same set of po-
sitions are dropped in all codewords of C . More precisely, if C ⊆ Σn and the set of punctured
positions is P ⊆ [n], then the punctured code is {(ci )i ̸∈P |(c1, . . . , cn) ∈ C }.
Prove that a linear code with no repetitions (i.e. there are no two positions i ̸= j such that for
every codeword c ∈ C , ci = ci ) is a puncturing of the Hadamard code. Hence, Hadamard code is
the “longest" linear code that does not repeat.

Exercise 2.33. In this problem we will consider the long code. For the deﬁnition, we will use the
functional way of looking at the ambient space as mentioned in Remark 1.2.1. A long code of
dimension k is a binary code such that the codeword corresponding to x = Fk
2 , is the function

f : {0, 1}2k → {0, 1} deﬁned as follows. For any m ∈ {0, 1}Fk
2 , we have f ((mα)α∈Fk
2 ) = mx. Derive the
parameters of the long code.
Finally, argue that the long code is the code with the longest block length such that the
codewords do not have a repeated coordinate (i.e. there does not exists i ̸= j such that for every
codeword c, ci = c j ). (Contrast this with the property of Hadamard code above.)

2.9 Bibliographic Notes

Finite ﬁelds are also called Galois ﬁelds (another common notation for Fq is GF (q)), named
after Évariste Galois, whose worked laid the foundations of their theory. (Galois led an extremely
short and interesting life, which ended in death from a duel.) For a more thorough treatment
refer to any standard text on algebra or the book on ﬁnite ﬁelds by Lidl and Niederreiter [69].
The answer to Question 1.7.1 was proved by van Lint [101] and Tietavainen [100].

58

Chapter 3

Probability as Fancy Counting and the q-ary
Entropy Function

In the ﬁrst half of this chapter, we will develop techniques that will allow us to answer questions
such as

Question 3.0.1. Does there exist a [2, 2, 1]2 code?

We note that the answer to the above question is trivially yes: just pick the generator matrix
to be the 2 × 2 identity matrix. However, we will use the above as a simple example to illustrate
a powerful technique called the probabilistic method.
As the name suggests, the method uses probability. Before we talk more about the proba-
bilistic method, we do a quick review of the basics of probability that we will need in this book.

3.1 A Crash Course on Probability

In this book, we will only consider probability distributions deﬁned over ﬁnite spaces. In par-
ticular, given a ﬁnite domain D, a probability distribution is deﬁned as a function

p : D → [0, 1] such that ∑

x∈D p(x) = 1,

where [0, 1] is shorthand for the interval of all real numbers between 0 and 1. In this book, we
will primarily deal with the following special distribution:

Deﬁnition 3.1.1 (Uniform Distribution). The uniform distribution over D, denoted by UD, is
given by
 UD(x) = 1
|D| for every x ∈ D.

Typically we will drop the subscript when the domain D is clear from the context.

59

G U (G) V00 V01 V10 V11
( 0 0
0 0
 ) 1
16 0 0 0 0
( 0 0
0 1
 ) 1
16 0 1 0 1
( 0 0
1 0
 ) 1
16 0 1 0 1
( 0 0
1 1
 ) 1
16 0 2 0 2
( 0 1
0 0
 ) 1
16 0 0 1 1
( 0 1
0 1
 ) 1
16 0 1 1 0
( 0 1
1 0
 ) 1
16 0 1 1 2
( 0 1
1 1
 ) 1
16 0 2 1 1
 G U (G) V00 V01 V10 V11
( 1 0
0 0
 ) 1
16 0 0 1 1
( 1 0
0 1
 ) 1
16 0 1 1 2
( 1 0
1 0
 ) 1
16 0 1 1 0
( 1 0
1 1
 ) 1
16 0 2 1 1
( 1 1
0 0
 ) 1
16 0 0 2 2
( 1 1
0 1
 ) 1
16 0 1 2 1
( 1 1
1 0
 ) 1
16 0 1 2 1
( 1 1
1 1
 ) 1
16 0 2 2 0

Table 3.1: Uniform distribution over F2×2
2 along with values of four random variables.

For example, consider the domain D = F2×2
2 , i.e. the set of all 2 × 2 matrices over F2. (Note
that each such matrix is a generator matrix of some [2, 2]2 code.) The ﬁrst two columns of Ta-
ble 3.1 list the elements of this D along with the corresponding probabilities for the uniform
distribution.
Typically, we will be interested in a real-valued function deﬁned on D and how it behaves
under a probability distribution deﬁned over D. This is captured by the notion of a random
variable:

Deﬁnition 3.1.2 (Random Variable). Let D be a ﬁnite domain and I ⊂ R be a ﬁnite
1 subset. Let
p be a probability distribution deﬁned over D. A random variable is a function:

V : D → I .

The expectation of V is deﬁned as
 E[V ] = ∑

x∈D p(x) · V (x).

For example, given (i , j ) ∈ {0, 1}2, let Vi j denote the random variable Vi j (G) = w t (
(i , j ) · G),
for any G ∈ F2×2
2 . The last four columns of Table 3.1 list the values of these four random variables.
In this book, we will mainly consider binary random variables, i.e., with I = {0, 1}. In partic-
ular, given a predicate or event E over D, we will deﬁne its indicator variable to be a function

1In general, I need not be ﬁnite. However, for this book this deﬁnition sufﬁces.

60

1E : D → {0, 1} such that for any x ∈ D:

1E (x) =
 {
1 if E (x) = true

0 otherwise.

For example,
 1V01=0
 ((
0 1
0 0
)) = 1 and 1V01=0
 ((
0 1
1 1
)) = 0.

In most cases we will shorten this notation to 1E (x) or simply 1E . Finally, sometimes we will
abuse notation and use E instead of 1E .
As a further use of indicator variables, consider the expectations of the four indicator vari-
ables:
 E [1V00=0] = 16 · 1
16 = 1.

E [1V01=0] = 4 · 1
16 = 1
4 . (3.1)

E [1V10=0] = 4 · 1
16 = 1
4 . (3.2)

E [1V11=0] = 4 · 1
16 = 1
4 . (3.3)

3.1.1 Some Useful Results

Before we proceed, we record a simple property of indicator variables that will be useful. (See
Exercise 3.1.)

Lemma 3.1.1. Let E be any event. Then

E [1E ] = Pr [E is true] .

Next, we state a simple yet useful property of expectation of a sum of random variables:

Proposition 3.1.2 (Linearity of Expectation). Given random variables V1, . . . ,Vm deﬁned over the
same domain D and with the same probability distribution p, we have

E
 [ m∑

i =1Vi
 ]
 = m∑

i =1 E [Vi ] .

Proof. For notational convenience, deﬁne V = V1 + · · · + Vm. Thus, we have

E[V ] = ∑

x∈DV (x) · p(x) (3.4)

= ∑

x∈D
 ( m∑

i =1Vi (x)
)
 · p(x) (3.5)

= m∑

i =1
 ∑

x∈DVi (x) · p(x) (3.6)

= m∑

i =1 E[Vi ]. (3.7)

61

In the equalities above, (3.4) and (3.7) follow from the deﬁnition of expectation of a random
variable. (3.5) follows from the deﬁnition of V and (3.6) follows by switching the order of the
two summations.

As an example, we have
 E [
1V01=0 + 1V10=0 + 1V11=0] = 3
4 (3.8)

Frequently, we will need to deal with the probability of the union of events. We will use the
following result to upper bound such probabilities:

Proposition 3.1.3 (Union Bound). Given m binary random variables A1, . . . , Am, we have

Pr
 [( m⋁

i =1 Ai
 )
 = 1
]
 ≤ m∑

i =1 Pr [Ai = 1] .

Proof. For every i ∈ [m], deﬁne Si = {x ∈ D|Ai (x) = 1}.

Then we have
 Pr
 [( m⋁

i =1 Ai
 )
 = 1
]
 = ∑

x∈∪m=1Si p(x) (3.9)

≤ m∑

i =1
 ∑

x∈Si p(x) (3.10)

= m∑

i =1 Pr[Ai = 1]. (3.11)

In the above, (3.9) and (3.11) follow from the deﬁnition of Si . (3.10) follows from the fact that
some of the x ∈ ∪i Si get counted more than once.

We remark that the union bound is tight when the events are disjoint. (In other words, using
the notation in the proof above, when Si ∩ S j = ; for every i ̸= j .)
As an example, let A1 = 1V01=0, A2 = 1V10=0 and A3 = 1V11=0. Note that in this case the event
A1 ∨ A2 ∨ A3 is the same as the event that there exists a non-zero m ∈ {0, 1}2 such that w t (m·G) =
0. Thus, the union bound implies (that under the uniform distribution over F
2×2
2 )

Pr [
There exists an m ∈ {0, 1}2 \ {(0, 0)}, such that w t (mG) = 0] ≤ 3
4 . (3.12)

Finally, we present two bounds on the probability of a random variable deviating signiﬁ-
cantly from its expectation. The ﬁrst bound holds for any random variable:

Lemma 3.1.4 (Markov Bound). Let V be a non-zero random variable. Then for any t > 0,

Pr[V ≥ t ] ≤ E[V ]
t .

In particular, for any a ≥ 1,
 Pr[V ≥ a · E[V ]] ≤ 1
a .

62

Proof. The second bound follows from the ﬁrst bound by substituting t = a · E[V ]. Thus, to
complete the proof, we argue the ﬁrst bound. Consider the following sequence of relations:

E[V ] = ∑

i ∈[0,t ) i · Pr[V = i ] + ∑

i ∈[t ,∞) i · Pr[V = i ] (3.13)

≥ ∑

i ≥t i · Pr[V = i ] (3.14)

≥ t · ∑

i ≥t Pr[V = i ] (3.15)

= t · Pr[V ≥ t ]. (3.16)

In the above relations, (3.13) follows from the deﬁnition of expectation of a random variable and
the fact that V is positive. (3.14) follows as we have dropped some non-negative terms. (3.15)
follows by noting that in the summands i ≥ t . (3.16) follows from the deﬁnition of Pr[V ≥ t ].
The proof is complete by noting that (3.16) implies the claimed bound.

The second bound works only for sums of independent random variables. We begin by
deﬁning independent random variables:

Deﬁnition 3.1.3 (Independence). Two random variables A and B are called independent if for
every a and b in the ranges of A and B respectively, we have

Pr[A = a ∧ B = b] = Pr[A = a] · Pr[B = b].

For example, for the uniform distribution in Table 3.1, let A denote the bit G0,0 and B denote
the bit G0,1. It can be veriﬁed that these two random variables are independent. In fact, it can be
veriﬁed all the random variables corresponding to the four bits in G are independent random
variables. (We’ll come to a related comment shortly.)
Another related concept that we will use is that of probability of an event happening condi-
tioned on another event happening:

Deﬁnition 3.1.4 (Conditional Probability). Given two events A and B deﬁned over the same
domain and probability distribution, we deﬁne the probability of A conditioned on B as

Pr[A|B ] = Pr[A and B ]
Pr[B ] .

For example, note that
 Pr[1V01=1|G0,0 = 0] = 4/16
1/2 = 1
2 .

The above deﬁnition implies that two events A and B are independent if and only if Pr[A] =
Pr[A|B ]. We will also use the following result later on in the book (see Exercise 3.2):

Lemma 3.1.5. For any two events A and B deﬁned on the same domain and the probability
distribution: Pr[A] = Pr[A|B ] · Pr[B ] + Pr[A|¬B ] · Pr[¬B ].

63

Next, we state the deviation bound. (We only state it for sums of binary random variables,
which is the form that will be needed in the book.)

Theorem 3.1.6 (Chernoff Bound). Let X1, . . . , Xm be independent binary random variables and
deﬁne X = ∑ Xi . Then the multiplicative Chernoff bound sates that for 0 < ε ≤ 1,

Pr [|X − E(X )| > εE(X )] < 2e−ε2E(X )/3,

and the additive Chernoff bound states that

Pr [|X − E(X )| > εm] < 2e−ε2m/2.

We omit the proof, which can be found in any standard textbook on randomized algorithms.
Finally, we present an alternate view of uniform distribution over product spaces and then
use that view to prove a result that we will use later in the book. Given probability distributions
p1 and p2 over domains D1 and D2 respectively, we deﬁne the product distribution p1 × p2 over
D1 × D2 as follows: every element (x, y) ∈ D1 × D2 under p1 × p2 is picked by choosing x from
D1 according to p1 and y is picked independently from D2 under p2. This leads to the following
observation (see Exercise 3.4).

Lemma 3.1.7. For any m ≥ 1, the distribution UD1×D2×···×Dm is identical2 to the distribution
UD1 × UD2 × · · · × UDm .

For example, the uniform distribution in Table 3.1 can be described equivalently as follows:
pick each of the four bits in G independently and uniformly at random from {0, 1}.
We conclude this section by proving the following result:

Lemma 3.1.8. Given a non-zero vector m ∈ Fk
q and a uniformly random k × n matrix G over Fq ,
the vector m · G is uniformly distributed over Fn
q .

Proof. Let the ( j , i )th entry in G (1 ≤ j ≤ k, 1 ≤ i ≤ n) be denoted by g j i . Note that as G is a ran-
dom k ×n matrix over Fq , by Lemma 3.1.7, each of the g j i is an independent uniformly random
element from Fq . Now, note that we would be done if we can show that for every 1 ≤ i ≤ n, the
i th entry in m · G (call it bi ) is an independent uniformly random element from Fq . To ﬁnish
the proof, we prove this latter fact. If we denote m = (m1, . . . , mk ), then bi = ∑k
j =1 m j g j i . Note
that the disjoint entries of G participate in the sums for bi and b j for i ̸= j . Given our choice of
G, this implies that the random variables bi and b j are independent. Hence, to complete the
proof we need to prove that bi is a uniformly independent element of Fq . The rest of the proof
is a generalization of the argument we used in the proof of Proposition 2.7.1.
Note that to show that bi is uniformly distributed over Fq , it is sufﬁcient to prove that bi
takes every value in Fq equally often over all the choices of values that can be assigned to
g1i , g2i , . . . , gki . Now, as m is non-zero, at least one of the its element is non-zero. Without
loss of generality assume that m1 ̸= 0. Thus, we can write bi = m1g1i + ∑k
j =2 m j g j i . Now, for

every ﬁxed assignment of values to g2i , g3i , . . . , gki (note that there are q k−1 such assignments),
bi takes a different value for each of the q distinct possible assignments to g1i (this is where we
use the assumption that m1 ̸= 0). Thus, over all the possible assignments of g1i , . . . , gki , bi takes
each of the values in Fq exactly q k−1 times, which proves our claim.

2We say two distributions p1 and p2 on D are identical if for every x ∈ D, p1(x) = p2(x).

64

3.2 The Probabilistic Method

The probabilistic method is a very powerful method in combinatorics which can be used to
show the existence of objects that satisfy certain properties. In this course, we will use the prob-
abilistic method to prove existence of a code C with certain property P . Towards that end, we
deﬁne a distribution D over all possible codes and prove that when C is chosen according to D:

Pr [
C has property P ] > 0 or equivalently Pr [
C doesn’t have property P ] < 1.

Note that the above inequality proves the existence of C with property P .
As an example consider Question 3.0.1. To answer this in the afﬁrmative, we note that the
set of all [2, 2]2 linear codes is covered by the set of all 2 × 2 matrices over F2. Then, we let D be
the uniform distribution over F2×2
2 . Then by Proposition 2.3.4 and (3.12), we get that

Pr
UF2×2
2 [There is no [2, 2, 1]2 code] ≤ 3
4 < 1,

which by the probabilistic method answers the Question 3.0.1 in the afﬁrmative.
For the more general case, when we apply the probabilistic method, the typical approach
will be to deﬁne (sub-)properties P1, . . . , Pm such that P = P1 ∧P2 ∧P3 . . .∧Pm and show that for
every 1 ≤ i ≤ m:
 Pr [
C doesn’t have property Pi ] = Pr [
Pi ] < 1
m .

Finally, by the union bound, the above will prove that
3 Pr [
C doesn’t have property P ] < 1, as
desired.
As an example, an alternate way to answer Question 3.0.1 in the afﬁrmative is the following.
Deﬁne P1 = 1V01≥1, P2 = 1V10≥1 and P3 = 1V11≥1. (Note that we want a [2, 2]2 code that satisﬁes
P1 ∧ P2 ∧ P3.) Then, by (3.1), (3.2) and (3.3), we have for i ∈ [3],

Pr [
C doesn’t have property Pi ] = Pr [
Pi ] = 1
4 < 1
3 ,

as desired.
Finally, we mention a special case of the general probabilistic method that we outlined
above. In particular, let P denote the property that the randomly chosen C satisﬁes f (C ) ≤ b.
Then we claim (see Exercise 3.5) that E[ f (C )] ≤ b implies that Pr[C has property P ] > 0. Note
that this implies that E[ f (C )] ≤ b implies that there exists a code C such that f (C ) ≤ b.

3.3 The q-ary Entropy Function

We begin with the deﬁnition of a function that will play a central role in many of our combina-
torial results.

3Note that P = P1 ∨ P2 ∨ · · · ∨ Pm.
 65

Deﬁnition 3.3.1 (q-ary Entropy Function). Let q be an integer and x be a real number such that
q ≥ 2 and 0 ≤ x ≤ 1. Then the q-ary entropy function is deﬁned as follows:

Hq (x) = x logq (q − 1) − x logq (x) − (1 − x) logq (1 − x).

Figure 3.1 presents a pictorial representation of the Hq function for the ﬁrst few values of q.
For the special case of q = 2, we will drop the subscript from the entropy function and denote

 0

 0.1

 0.2

 0.3

 0.4

 0.5

 0.6

 0.7

 0.8

 0.9

 1
  0  0.2  0.4  0.6  0.8  1Hq(x)  --->
x  --->

q=2
q=3
q=4

Figure 3.1: A plot of Hq (x) for q = 2, 3 and 4. The maximum value of 1 is achieved at x = 1−1/q.

H2(x) by just H (x), that is, H (x) = −x log x − (1 − x) log(1 − x), where log x is deﬁned as log2(x)
(we are going to follow this convention for the rest of the book).
Under the lens of Shannon’s entropy function, H (x) denotes the entropy of the distribution
over {0, 1} that selects 1 with probability x and 0 with probability 1 − x. However, there is no
similar analogue for the more general Hq (x). The reason why this quantity will turn out to be
so central in this book is that it is very closely related to the “volume" of a Hamming ball. We
make this connection precise in the next subsection.

3.3.1 Volume of Hamming Balls

It turns out that in many of our combinatorial results, we will need good upper and lower
bounds on the volume of a Hamming ball. Next we formalize the notion of the volume of a
Hamming ball:

Deﬁnition 3.3.2 (Volume of a Hamming Ball). Let q ≥ 2 and n ≥ r ≥ 1 be integers. Then the
volume of a Hamming ball of radius r is given by

V olq (r, n) = |Bq (0, r )| = r∑

i =0
 (
n
i
 )
(q − 1)i .

66

The choice of 0 as the center for the Hamming ball above was arbitrary: since the volume
of a Hamming ball is independent of its center (as is evident from the last equality above), we
could have picked any point as the center.
We will prove the following result:

Proposition 3.3.1. Let q ≥ 2 be an integer and 0 ≤ p ≤ 1 − 1
q be a real number. Then:

(i) V olq (pn, n) ≤ q Hq (p)n; and

(ii) for large enough n, V olq (pn, n) ≥ q Hq (p)n−o(n).

Proof. We start with the proof of (i). Consider the following sequence of relations:

1 = (p + (1 − p))n

= n∑

i =0
 (
n
i
 )
p i (1 − p)n−i (3.17)

=
 pn∑

i =0
 (
n
i
 )
p i (1 − p)n−i + n∑

i =pn+1
 (n
i
 )
p i (1 − p)n−i

≥
 pn∑

i =0
 (
n
i
 )
p i (1 − p)n−i (3.18)

=
 pn∑

i =0
 (
n
i
 )
(q − 1)i ( p
q − 1
 )i (1 − p)n−i

=
 pn∑

i =0
 (
n
i
 )
(q − 1)i (1 − p)n ( p
(q − 1)(1 − p)
 )i

≥
 pn∑

i =0
 (
n
i
 )
(q − 1)i (1 − p)n ( p
(q − 1)(1 − p)
 )pn (3.19)

=
 pn∑

i =0
 (
n
i
 )
(q − 1)i ( p
q − 1
 )pn (1 − p)(1−p)n (3.20)

≥ V olq (pn, n)q −Hq (p)n. (3.21)

In the above, (3.17) follows from the binomial expansion. (3.18) follows by dropping the second
sum and (3.19) follows from the facts that p
(q−1)(1−p) ≤ 1 (as4 p ≤ 1−1/q). Rest of the steps except

(3.21) follow from rearranging the terms. (3.21) follows as q −Hq (p)n = ( p
q−1
 )pn (1 − p)(1−p)n.
(3.21) implies that 1 ≥ V olq (pn, n)q −Hq (p)n,

which proves (i).

4Indeed, note that p
(q−1)(1−p) ≤ 1 is true if p
1−p ≤ q−1
1 , which in turn is true if p ≤ q−1
q , where the last step follows
from Lemma B.2.1.
 67

We now turn to the proof of part (ii). For this part, we will need Stirling’s approximation for
n! (Lemma B.1.2).
By the Stirling’s approximation, we have the following inequality:
( n
pn
)
 = n!
(pn)!((1 − p)n)!

> (n/e)n

(pn/e)pn((1 − p)n/e)(1−p)n · 1
√
2πp(1 − p)n · eλ1(n)−λ2(pn)−λ2((1−p)n)

= 1

p pn(1 − p)(1−p)n · ℓ(n), (3.22)

where ℓ(n) = eλ1(n)−λ2(pn)−λ2((1−p)n)
p2πp(1−p)n .

Now consider the following sequence of relations that complete the proof:

V olq (pn, n) ≥
 ( n
pn
)
(q − 1)pn (3.23)

> (q − 1)pn

p pn(1 − p)(1−p)n · ℓ(n) (3.24)

≥ q Hq (p)n−o(n). (3.25)

In the above (3.23) follows by only looking at one term. (3.24) follows from (3.22) while (3.25)
follows from the deﬁnition of Hq (·) and the fact that for large enough n, ℓ(n) is q −o(n).

Next, we consider how the q-ary entropy function behaves for various ranges of its parame-
ters.

3.3.2 Other Properties of the q-ary Entropy function

We begin by recording the behavior of q-ary entropy function for large q.

Proposition 3.3.2. For small enough ε, 1 − Hq (ρ) ≥ 1 − ρ − ε for every 0 < ρ ≤ 1 − 1/q if and only
if q is 2Ω(1/ε).

Proof. We ﬁrst note that by deﬁnition of Hq (ρ) and H (ρ),

Hq (ρ) = ρ logq (q − 1) − ρ logq ρ − (1 − ρ) logq (1 − ρ)

= ρ logq (q − 1) + H (ρ)/ log2 q.

Now if q ≥ 21/ε, we get that Hq (ρ) ≤ ρ + ε

as logq (q − 1) ≤ 1 and H (ρ) ≤ 1. Thus, we have argued that for q ≥ 21/ε, we have 1 − Hq (ρ) ≥
1 − ρ − ε, as desired.
 68

Next, we consider the case when q = 2o(1/ε). We begin by claiming that for small enough ε,

if q ≥ 1/ε2 then logq (q − 1) ≥ 1 − ε.

Indeed, logq (q − 1) = 1 + (1/ ln q) ln(1 − 1/q) = 1 − O ( 1
q ln q
 ),5 which is at least 1 − ε for q ≥ 1/ε2

(and small enough ε).
Finally, if q = 2o( 1
ε ), then for ﬁxed ρ,

H (ρ)/ log q = ε · ω(1).

Then for q = 2o( 1
ε ) (but q ≥ 1/ε2) we have

ρ logq (q − 1) + H (ρ)/ log q ≥ ρ − ε + ε · ω(1) > ρ + ε,

which implies that 1 − Hq (ρ) < 1 − ρ − ε,

as desired. For q ≤ 1/ε2, Lemma 3.3.3 shows that 1 − Hq (ρ) ≤ 1 − H1/ε2(ρ) < 1 − ρ − ε, as desired.

We will also be interested in how Hq (x) behaves for ﬁxed x and increasing q:

Lemma 3.3.3. Let q ≥ 2 be an integer and let 0 ≤ ρ ≤ 1 − 1/q, then for any real m ≥ 1 such that

q m−1 ≥ (
1 + 1
q − 1
 )q−1 , (3.26)

we have Hq (ρ) ≥ Hq m (ρ).

Proof. Note that Hq (0) = Hq m (0) = 0. Thus, for the rest of the proof we will assume that ρ ∈
(0, 1 − 1/q].
As observed in the proof of Proposition 3.3.2, we have

Hq (ρ) = ρ · log(q − 1)
log q + H (ρ) · 1
log q .

Using this, we obtain

Hq (ρ) − Hq m (ρ) = ρ ( log(q − 1)
log q − log(q m − 1)
m log q
 ) + H (ρ) ( 1
log q − 1
m log q
 ) .

The above in turn implies that

1
ρ · m log q · (Hq (ρ) − Hq m (ρ)) = log(q − 1)m − log(q m − 1) + H (ρ)
ρ (m − 1)

5The last equality follows from the fact that by Lemma B.2.2, for 0 < x < 1, ln(1 − x) = −O(x).

69

≥ log(q − 1)m − log(q m − 1) + H (1 − 1/q)
1 − 1/q (m − 1) (3.27)

= log(q − 1)m − log(q m − 1) + (m − 1) (
log q
q − 1 + log q
q − 1
 )

= log ( (q − 1)m

q m − 1 · ( q
q − 1
 )m−1 · q m−1
q−1 )

= log
 ( (q − 1) · q m−1 · q m−1
q−1

q m − 1
 )

≥ 0 (3.28)

In the above (3.27) follows from the fact that H (ρ)/ρ is decreasing
6 in ρ and that ρ ≤ 1 − 1/q.
(3.28) follows from the claim that (q − 1) · q m−1
q−1 ≥ q.

Indeed the above follows from (3.26).
Finally, note that (3.28) completes the proof.

Since (1 + 1/x)x ≤ e (by Lemma B.2.5), we also have that (3.26) is also satisﬁed for m ≥ 1 +
1
ln q . Further, we note that (3.26) is satisﬁed for every m ≥ 2 (for any q ≥ 3), which leads to the
following (also see Exercise 3.6):

Corollary 3.3.4. Let q ≥ 3 be an integer and let 0 ≤ ρ ≤ 1 − 1/q, then for any m ≥ 2, we have

Hq (ρ) ≥ Hq m (ρ).

Next, we look at the entropy function when its input is very close to 1.

Proposition 3.3.5. For small enough ε > 0,

Hq
 (
1 − 1
q − ε) ≤ 1 − cq ε2,

where cq is a constant that only depends on q.

Proof. The intuition behind the proof is the following. Since the derivative of Hq (x) is zero at
x = 1 − 1/q, in the Taylor expansion of Hq (1 − 1/q − ε) the ε term will vanish. We will now make
this intuition more concrete. We will think of q as ﬁxed and 1/ε as growing. In particular, we
will assume that ε < 1/q. Consider the following equalities:

Hq (1 − 1/q − ε) = − (
1 − 1
q − ε) logq
 ( 1 − 1/q − ε
q − 1
 ) − ( 1
q + ε) logq
 ( 1
q + ε)

6Indeed, H (ρ)/ρ = log(1/ρ) − (1/ρ − 1) log(1 − ρ). Note that the ﬁrst term is deceasing in ρ. We claim that the
second term is also decreasing in ρ– this e.g. follows from the observation that −(1/ρ − 1) ln(1 − ρ) = (1 − ρ)(1 +
ρ/2! + ρ2/3! + · · · ) = 1 − ρ/2 − ρ2(1/2 − 1/3!) − · · · is also decreasing in ρ.

70

= − logq
 ( 1
q
 (
1 − εq
q − 1
 )) + ( 1
q + ε) logq
 ( 1 − (εq)/(q − 1)
1 + εq
 )

= 1 − 1
ln q
 [
ln (
1 − εq
q − 1
 ) − ( 1
q + ε) ln ( 1 − (εq)/(q − 1)
1 + εq
 )]

= 1 + o(ε2) − 1
ln q
 [
− εq
q − 1 − ε2q 2

2(q − 1)2 − ( 1
q + ε) (− εq
q − 1

− ε2q 2

2(q − 1)2 − εq + ε2q 2

2
 )] (3.29)

= 1 + o(ε2) − 1
ln q
 [
− εq
q − 1 − ε2q 2

2(q − 1)2

− ( 1
q + ε) (
− εq 2

q − 1 + ε2q 3(q − 2)
2(q − 1)2
 )]

= 1 + o(ε2) − 1
ln q
 [
− ε2q 2

2(q − 1)2 + ε2q 2

q − 1 − ε2q 2(q − 2)
2(q − 1)2
 ] (3.30)

= 1 − ε2q 2

2 ln q(q − 1) + o(ε2)

≤ 1 − ε2q 2

4 ln q(q − 1)
 (3.31)

(3.29) follows from the fact that for |x| < 1, ln(1 + x) = x − x2/2 + x3/3 − . . . (Lemma B.2.2) and
by collecting the ε3 and smaller terms in o(ε2). (3.30) follows by rearranging the terms and by
absorbing the ε3 terms in o(ε2). The last step is true assuming ε is small enough.

Next, we look at the entropy function when its input is very close to 0.

Proposition 3.3.6. For small enough ε > 0,

Hq (ε) = Θ ( 1
log q · ε log ( 1
ε
 )) .

Proof. By deﬁnition

Hq (ε) = ε logq (q − 1) + ε logq (1/ε) + (1 − ε) logq (1/(1 − ε)).

Since all the terms in the RHS are positive we have

Hq (ε) ≥ ε log(1/ε)/ log q. (3.32)

Further, by Lemma B.2.2, (1 − ε) logq (1/(1 − ε)) ≤ 2ε/ ln q for small enough ε. Thus, this implies
that
 Hq (ε) ≤ 2 + ln(q − 1)
ln q · ε + 1
ln q · ε ln ( 1
ε
 ) . (3.33)

(3.32) and (3.33) proves the claimed bound.
 71

We will also work with the inverse of the q-ary entropy function. Note that Hq (·) on the
domain [0, 1 − 1/q] is a bijective map into [0, 1]. Thus, we deﬁne H −1
q (y) = x such that Hq (x) = y
and 0 ≤ x ≤ 1 − 1/q. Finally, we will need the following lower bound:

Lemma 3.3.7. For every 0 ≤ y ≤ 1 − 1/q and for every small enough ε > 0,

H −1
q (y − ε2/c ′
q ) ≥ H −1
q (y) − ε,

where c ′
q ≥ 1 is a constant that depends only on q.

Proof. It is easy to check that H −1
q (y) is a strictly increasing convex function when y ∈ [0, 1]. This
implies that the derivative of H −1
q (y) increases with y. In particular, (H −1
q )′(1) ≥ (H −1
q )′(y) for

every 0 ≤ y ≤ 1. In other words, for every 0 < y ≤ 1, and (small enough) δ > 0, H −1
q (y)−H −1
q (y−δ)
δ ≤

H −1
q (1)−H −1
q (1−δ)
δ . Proposition 3.3.5 along with the facts that H −1
q (1) = 1−1/q and H −1
q is increasing
completes the proof if one picks c ′
q = max(1, 1/cq ) and δ = ε2/c ′
q .

3.4 Exercises

Exercise 3.1. Prove Lemma 3.1.1.

Exercise 3.2. Prove Lemma 3.1.5.

Exercise 3.3. In this exercise, we will see a common use of the Chernoff bound (Theorem 3.1.6).
Say we are trying to determine an (unknown) value x ∈ F to which we have access to via a ran-
domized algorithm A that on input (random) input r ∈ {0, 1}m outputs an estimate A (r) of x
such that
 Pr
r [A(r) = x] ≥ 1
2 + γ,

for some 0 < γ < 1
2 . Then show that for any t ≥ 1 with O ( t
γ2 ) calls to A one can determine x with

probability at least 1 − e−t .

Hint: Call A with independent random bits and take majority of the answer and then use the Chernoff bound.

Exercise 3.4. Prove Lemma 3.1.7.

Exercise 3.5. Let P denote the property that the randomly chosen C satisﬁes f (C ) ≤ b. Then
E[ f (C )] ≤ b implies that Pr[C has property P ] > 0.

Exercise 3.6. Show that for any Q ≥ q ≥ 2 and ρ ≤ 1 − 1/q, we have HQ (ρ) ≤ Hq (ρ).

3.5 Bibliographic Notes

Shannon was one of the very early adopters of probabilistic method (and we will see one such
use in Chapter 6). Later, the probabilistic method was popularized Erd˝os. For more on proba-
bilistic method, see the book by Alon and Spencer [3].
Proofs of various concentration bounds can e.g. be found in [23].

72

Part II

The Combinatorics

73

Chapter 4

What Can and Cannot Be Done-I

In this chapter, we will try to tackle Question 2.5.1. We will approach this trade-off in the fol-
lowing way:

If we ﬁx the relative distance of the code to be δ, what is the best rate R that we can
achieve?

Note that an upper bound on R is a negative result, while a lower bound on R is a positive result.
In this chapter, we will consider only one positive result, i.e. a lower bound on R called the
Gilbert-Varshamov bound in Section 4.2. In Section 4.1, we recall a negative result that we have
already seen– Hamming bound and state its asymptotic version to obtain an upper bound on
R. We will consider two other upper bounds: the Singleton bound (Section 4.3), which gives
a tight upper bound for large enough alphabets (but not binary codes) and the Plotkin bound
(Section 4.4).

4.1 Asymptotic Version of the Hamming Bound

We have already seen an upper bound in Section 1.7 due to Hamming. However, we had stated
this as an upper bound on the dimension k in terms of n, q and d . We begin by considering the
trade-off between R and δ given by the Hamming bound. Recall that Theorem 1.7.1 states the
following:
 k
n ≤ 1 − logq V olq (⌊ d −1
2
 ⌋ , n)

n
Recall that Proposition 3.3.1 states following lower bound on the volume of a Hamming ball:

V olq
 (⌊ d − 1
2
 ⌋ , n) ≥ q Hq ( δ
2
 )
n−o(n),

which implies the following asymptotic version of the Hamming bound:

R ≤ 1 − Hq
 ( δ
2
 ) + o(1).

See Figure 4.1 for a pictorial description of the Hamming bound for binary codes.

75

 0

 0.1

 0.2

 0.3

 0.4

 0.5

 0.6

 0.7

 0.8

 0.9

 1
  0  0.2  0.4  0.6  0.8  1R
δ
 Hamming bound
GV bound

Figure 4.1: The Hamming and GV bounds for binary codes. Note that any point below the GV
bound is achievable by some code while no point above the Hamming bound is achievable by
any code. In this part of the book we would like to push the GV bound as much up as possible
while at the same time try and push down the Hamming bound as much as possible.

4.2 Gilbert-Varshamov Bound

Next, we will switch gears by proving our ﬁrst non-trivial lower bound on R in terms of δ. (In
fact, this is the only positive result on the R vs δ tradeoff question that we will see in this book.)
In particular, we will prove the following result:

Theorem 4.2.1 (Gilbert-Varshamov Bound). Let q ≥ 2. For every 0 ≤ δ < 1 − 1
q , and 0 < ε ≤
1 − Hq (δ), there exists a code with rate R ≥ 1 − Hq (δ) − ε and relative distance δ.

The bound is generally referred to as the GV bound. For a pictorial description of the GV
bound for binary codes, see Figure 4.1. We will present the proofs for general codes and linear
codes in Sections 4.2.1 and 4.2.2 respectively.

4.2.1 Greedy Construction

We will prove Theorem 4.2.1 for general codes by the following greedy construction (where
d = δn): start with the empty code C and then keep on adding vectors not in C that are at Ham-
ming distance at least d from all the existing codewords in C . Algorithm 6 presents a formal
description of the algorithm and Figure 4.2 illustrates the ﬁrst few executions of this algorithm.
We claim that Algorithm 6 terminates and the C that it outputs has distance d . The latter
is true by step 2, which makes sure that in Step 3 we never add a vector c that will make the
distance of C fall below d . For the former claim, note that, if we cannot add v at some point, we

76

Algorithm 6 Gilbert’s Greedy Code Construction
INPUT: n, q, d
OUTPUT: A code C ⊆ [q]
n of distance d ≥≥ 11

1: C ← ;

2: WHILE there exists a v ∈ [q]
n such that ∆(v, c) ≥ d for every c ∈ C DO

3: Add v to C

4: RETURN C
 [q]n
 c1
d − 1

c2 c3

c4

c5

Figure 4.2: An illustration of Gilbert’s greedy algorithm (Algorithm 6) for the ﬁrst ﬁve iterations.

cannot add it later. Indeed, since we only add vectors to C , if a vector v ∈ [q]
n is ruled out in a
certain iteration of Step 2 because ∆(c, v) < d , then in all future iterations, we have ∆(v, c) < d
and thus, this v will never be added in Step 3 in any future iteration.
The running time of Algorithm 6 is qO(n). To see this, note that Step 2 in the worst-case could
be repeated for every vector in [q]
n, that is at most q n times. In a naive implementation, for each
iteration, we cycle through all vectors in [q]
n and for each vector v ∈ [q]
n, iterate through all (at
most q n) vectors c ∈ C to check whether ∆(c, v) < d . If no such c exists, then we add v to C .
Otherwise, we move to the next v. However, note that we can do slightly better– since we know
that once a v is “rejected" in an iteration, it’ll keep on being rejected in the future iterations, we
can ﬁx up an ordering of vectors in [q]
n and for each vector v in this order, check whether it can
be added to C or not. If so, we add v to C , else we move to the next vector in the order. This
algorithm has time complexity O(nq 2n), which is still qO(n).
Further, we claim that after termination of Algorithm 6
⋃

c∈C B (c, d − 1) = [q]
n.

This is because if the above is not true, then there exists a vector v ∈ [q]
n \C , such that ∆(v, c) ≥ d
and hence v can be added to C . However, this contradicts the fact that Algorithm 6 has termi-

77

nated. Therefore, ∣ ⋃

c∈C B (c, d − 1)∣ = q n. (4.1)

It is not too hard to see that
 ∑

c∈C |B (c, d − 1)| ≥ ∣ ⋃

c∈C B (c, d − 1)∣ ,

which by (
4.1) implies that ∑

c∈C |B (c, d − 1)| ≥ q n

or since the volume of a Hamming ball is translation invariant,

∑

c∈C V olq (d − 1, n) ≥ q n.

Since ∑c∈C V olq (d − 1, n) = V olq (d − 1, n) · |C |, we have

|C | ≥ q n

V olq (d − 1, n)

≥ q n

q nHq (δ) (4.2)

= q n(1−Hq (δ)),

as desired. In the above, (4.2) follows from the fact that

V olq (d − 1, n) ≤ V olq (δn, n)

≤ q nHq (δ), (4.3)

where the second inequality follows from the upper bound on the volume of a Hamming ball in
Proposition 3.3.1.
It is worth noting that the code from Algorithm 6 is not guaranteed to have any special struc-
ture. In particular, even storing the code can take exponential space. We have seen in Proposi-
tion 2.3.1 that linear codes have a much more succinct representation. Thus, a natural question
is:

Question 4.2.1. Do linear codes achieve the R ≥ 1 − Hq (δ) tradeoff that the greedy construc-
tion achieves?

Next, we will answer the question in the afﬁrmative.

78

4.2.2 Linear Code Construction

Now we will show that a random linear code, with high probability, lies on the GV bound. The
construction is a use of the probabilistic method (Section 3.2).
By Proposition 2.3.4, we are done if we can show that there exists a k ×n matrix G of full rank
(for k = (1 − Hq (δ) − ε)n) such that

For every m ∈ Fk
q \ {0}, w t (mG) ≥ d .

We will prove the existence of such a G by the probabilistic method. Pick a random linear code
by picking a random k × n matrix G where each of kn entries is chosen uniformly and indepen-
dently at random from Fq . Fix m ∈ Fk
q \ {0}. Recall that by Lemma 3.1.8, for a random G, mG is a
uniformly random vector from Fn
q . Thus, we have

P r [w t (mG) < d ] = V olq (d − 1, n)

q n

≤ q nHq (δ)

q n , (4.4)

where (4.4) follows from (4.3). Thus, by the union bound (Lemma 3.1.3)

P r [There exists a non-zero m, w t (mG) < d ] ≤ q k q −n(1−Hq (δ))

= q −ε·n,

where the equality follows by choosing k = (1− Hq (δ)−ε)n. Since q −εn ≪ 1, by the probabilistic
method, there exists a linear code C with relative distance δ.
All that’s left is to argue that the code C has dimension at least k = (1 − Hq (δ) − ε)n. To show
this, we need to show that the chosen generator matrix G has full rank. Note that there is a non-
zero probability that a uniformly matrix G does not have full rank. There are two ways to deal
with this. First, we can show that with high probability a random G does have full rank, so that
|C | = q k . Further, the proof above has already shown that, with high probability, the distance is
greater than zero, which implies that distinct messages will be mapped to distinct codewords
and thus |C | = q k . In other words, C does indeed have dimension k, as desired

Discussion. We now digress a bit to discuss some consequences of the proofs of the GV bound.
We ﬁrst note that the probabilistic method proof shows something stronger than Theo-
rem 4.2.1: most linear codes (with appropriate parameters) meet the Gilbert-Varshamov bound.
Note that we can also pick a random linear code by picking a random (n −k)×n parity check
matrix. This also leads to a proof of the GV bound: see Exercise 4.1.
Finally, we note that Theorem 4.2.1 requires δ < 1 − 1
q . An inspection of Gilbert and Var-

shamov’s proofs shows that the only reason the proof required that δ ≤ 1 − 1
q is because it is

needed for the volume bound (recall the bound in Proposition 3.3.1)– V olq (δn, n) ≤ q Hq (δ)n– to
hold. It is natural to wonder if the above is just an artifact of the proof or, for example:

79
 d − 1

c1

c2

ci

c j

cM
 c
′
i

c
′
i
 n − d + 1

Figure 4.3: Construction of a new code in the proof of the Singleton bound.

Question 4.2.2. Does there exists a code with R > 0 and δ > 1 − 1
q ?

We will return to this question in Section 4.4.

4.3 Singleton Bound

We will now change gears again and prove an upper bound on R (for ﬁxed δ). We start by proving
the Singleton bound.

Theorem 4.3.1 (Singleton Bound). For every (n, k, d )q code,

k ≤ n − d + 1.

Proof. Let c1, c2, . . . , cM be the codewords of an (n, k, d )q code C . Note that we need to show
M ≤ q n−d +1. To this end, we deﬁne c′
i to be the preﬁx of the codeword ci of length n − d + 1 for
every i ∈ [M ]. See Figure 4.3 for a pictorial description.
We now claim that for every i ̸= j , c′
i ̸= c′
j . For the sake of contradiction, assume that there
exits an i ̸= j such that c′
i = c′
j . Notice this implies that ci and c j agree in all the ﬁrst n − d +
1 positions, which in turn implies that ∆(ci , c j ) ≤ d − 1. This contradicts the fact that C has
distance d . Thus, M is the number of preﬁxes of codewords in C of length n − d + 1, which
implies that M ≤ q n−d +1 as desired.
 80

 0

 0.2

 0.4

 0.6

 0.8

 1
  0  0.2  0.4  0.6  0.8  1R
δ
 Hamming bound
GV bound
Singleton bound

Figure 4.4: The Hamming, GV and Singleton bound for binary codes.

Note that the asymptotic version of the Singleton bound states that k/n ≤ 1 − d /n + 1/n. In
other words,
 R ≤ 1 − δ + o(1).

Figure 4.4 presents a pictorial description of the asymptotic version of the Singleton bound.
It is worth noting that the bound is independent of the alphabet size. As is evident from Fig-
ure 4.4, the Singleton bound is worse than the Hamming bound for binary codes. However, this
bound is better for larger alphabet sizes. In fact, we will look at a family of codes called Reed-
Solomon codes in Chapter 5 that meets the Singleton bound. However, the alphabet size of the
Reed-Solomon codes increases with the block length n. Thus, a natural follow-up question is
the following:

Question 4.3.1. Given a ﬁxed q ≥ 2, does there exist a q-ary code that meets the Singleton
bound?

We’ll see an answer to this question in the next section.

81

4.4 Plotkin Bound

In this section, we will study the Plotkin bound, which will answer Questions 4.2.2 and 4.3.1.
We start by stating the bound.

Theorem 4.4.1 (Plotkin bound). The following holds for any code C ⊆ [q]
n with distance d :

1. If d = (
1 − 1
q
 ) n, |C | ≤ 2qn.

2. If d > (
1 − 1
q
 ) n, |C | ≤ qd
qd −(q−1)n .

Note that the Plotkin bound (Theorem 4.4.1) implies that a code with relative distance δ ≥
1 − 1
q , must necessarily have R = 0, which answers Question 4.2.2 in the negative.
Before we prove Theorem 4.4.1, we make a few remarks. We ﬁrst note that the upper bound
in the ﬁrst part of Theorem 4.4.1 can be improved to 2n for q = 2. (See Exercise 4.12.) Second, it
can be shown that this bound is tight. (See Exercise 4.13.) Third, the statement of Theorem 4.4.1
gives a trade-off only for relative distance greater than 1 − 1/q. However, as the following corol-
lary shows, the result can be extended to work for 0 ≤ δ ≤ 1 − 1/q. (See Figure 4.5 for an illustra-
tion for binary codes.)

Corollary 4.4.2. For any q-ary code with relative distance 0 ≤ δ ≤ 1 − 1
q ,

R ≤ 1 − ( q
q − 1
 ) δ + o(1).

Proof. Deﬁne d = δn. The proof proceeds by shortening the codewords. We group the code-

words so that they agree on the ﬁrst n − n′ symbols, where n′ = ⌊ qd
q−1
 ⌋ − 1. (We will see later why

this choice of n′ makes sense.) In particular, for any x ∈ [q]
n−n′, deﬁne the ‘preﬁx code’

Cx = {(cn−n′+1, . . . cn) | (c1 . . . cN ) ∈ C , (c1 . . . cn−n′) = x} .

For all x, Cx has distance d as C has distance d .1 Additionally, it has block length n′ < ( q
q−1
 ) d

and thus, d > (1 − 1
q
 ) n′. By Theorem 4.4.1, this implies that

|Cx| ≤ qd
qd − (q − 1)n′ ≤ qd , (4.5)

where the second inequality follows from the fact that qd − (q − 1)n′ is an integer.
Note that by the deﬁnition of Cx:
 |C | = ∑

x∈[q]n−n′ |Cx| ,

1If for some x, c1 ̸= c2 ∈ Cx, ∆(c1, c2) < d , then ∆((x, c1), (x, c2)) < d , which implies that the distance of C is less
than d (as by deﬁnition of Cx, both (x, c1), (x, c2) ∈ C ), which in turn is a contradiction.

82

 0

 0.2

 0.4

 0.6

 0.8

 1
  0  0.2  0.4  0.6  0.8  1R
δ
 Hamming bound
GV bound
Singleton bound
Plotkin bound

Figure 4.5: The current bounds on the rate R vs. relative distance δ for binary codes. The GV
bound is a lower bound on R while the other three bounds are upper bounds on R.

which by (4.5) implies that

|C | ≤ ∑

x∈[q]n−n′ qd = q n−n′ · qd ≤ q n− q
q−1 d +o(n) = q n(1−δ· q
q−1 +o(1)).

In other words, R ≤ 1 − ( q
q−1
 ) δ + o(1) as desired.

Note that Corollary 4.4.2 implies that for any q-ary code of rate R and relative distance δ
(where q is a constant independent of the block length of the code), R < 1 − δ. In other words,
this answers Question 4.3.1 in the negative.

Let us pause for a bit at this point and recollect the bounds on R versus δ that we have proved
till now. Figure 4.5 depicts all the bounds we have seen till now (for q = 2). The GV bound is
the best known lower bound at the time of writing of this book. Better upper bounds are known
and we will see one such trade-off (called the Elias-Bassalygo bound) in Section 8.1.

Now, we turn to the proof of Theorem 4.4.1, for which we will need two more lemmas. The
ﬁrst lemma deals with vectors over real spaces. We quickly recap the necessary deﬁnitions.
Consider a vector v in Rn, that is, a tuple of n real numbers. This vector has (Euclidean) norm

∥v∥ = √v 2
1 + v 2
2 + . . . + v 2
n, and is a unit vector if and only if its norm is 1. The inner product of
two vectors, u and v, is 〈u, v〉 = ∑i ui · vi . The following lemma gives a bound on the number of
vectors that can exist such that every pair is at an obtuse angle with each other.

Lemma 4.4.3 (Geometric Lemma). Let v1, v2, . . . , vm ∈ RN be non-zero vectors.

83

1. If 〈vi , v j 〉 ≤ 0 for all i ̸= j , then m ≤ 2N .

2. Let vi be unit vectors for 1 ≤ i ≤ m. Further, if 〈vi , v j 〉 ≤ −ε < 0 for all i ̸= j , then m ≤ 1 + 1
ε .2

(Item 1 is tight: see Exercise 4.14.) The proof of the Plotkin bound will need the existence of a
map from codewords to real vectors with certain properties, which the next lemma guarantees.

Lemma 4.4.4 (Mapping Lemma). Let C ⊆ [q]
n. Then there exists a function f : C −→ R
nq such
that

1. For every c ∈ C , ∥ f (c)∥ = 1.

2. For every c1 ̸= c2 such that c1, c2 ∈ C , 〈 f (c1), f (c2)〉 = 1 − ( q
q−1
 ) ( ∆(c1,c2)
n
 ) .

We defer the proofs of the lemmas above to the end of the section. We are now in a position
to prove Theorem 4.4.1.
Proof of Theorem 4.4.1 Let C = {c1, c2, . . . , cm}. For all i ̸= j ,

〈 f (ci ), f (c j )〉 ≤ 1 − ( q
q − 1
 ) ∆(ci , c j )

n ≤ 1 − ( q
q − 1
 ) d
n .

The ﬁrst inequality holds by Lemma 4.4.4, and the second holds as C has distance d .

For part 1, if d = (
1 − 1
q
 ) n = (q−1)n
q , then for all i ̸= j ,

〈 f (ci ), f (c j )〉 ≤ 0

and so by the ﬁrst part of Lemma 4.4.3, m ≤ 2nq, as desired.

For part 2, d > ( q−1
q
 ) n and so for all i ̸= j ,

〈 f (ci ), f (c j )〉 ≤ 1 − ( q
q − 1
 ) d
n = − ( qd − (q − 1)n
(q − 1)n
 )

and, since ε def
= ( qd −(q−1)n
(q−1)n
 ) > 0, we can apply the second part of Lemma 4.4.3. Thus, m ≤ 1 +

(q−1)n
qd −(q−1)n = qd
qd −(q−1)n , as desired ✷

4.4.1 Proof of Geometric and Mapping Lemmas

Next, we prove Lemma 4.4.3.

2Note that since vi and v j are both unit vectors, 〈vi , v j 〉 is the cosine of the angle between them.

84

Proof of Lemma 4.4.3. We begin with a proof of the ﬁrst result. The proof is by induction on
n. Note that in the base case of N = 0, we have m = 0, which satisﬁes the claimed inequality
m ≤ 2N .
In the general case, we have m ≥ 1 non-zero vectors v1, . . . , vm ∈ RN such that for every i ̸= j ,

〈vi , v j 〉 ≤ 0. (4.6)

Since rotating all the vectors by the same amount does not change the sign of the inner
product (nor does scaling any of the vectors), w.l.o.g. we can assume that vm = 〈1, 0, . . . , 0〉. For
1 ≤ i ≤ m − 1, denote the vectors as vi = 〈αi , yi 〉, for some αi ∈ R and yi ∈ RN −1. Now, for any
i ̸= 1, 〈v1, vi 〉 = 1·αi +∑m
i =2 0 = αi . However, note that (4.6) implies that 〈v1, vi 〉 ≤ 0, which in turn
implies that αi ≤ 0. (4.7)

Next, we claim that at most one of y1, . . . , ym−1 can be the all zeroes vector, 0. If not, assume
w.l.o.g., that y1 = y2 = 0. This in turn implies that

〈v1, v2〉 = α1 · α2 + 〈y1, y2〉

= α1 · α2 + 0

= α1 · α2
> 0,

where the last inequality follows from the subsequent argument. As v1 = 〈α1, 0〉 and v2 = 〈α2, 0〉
are non-zero, this implies that α1, α2 ̸= 0. (4.7) then implies that α1, α2 < 0. However, 〈v1, v2〉 > 0
contradicts (4.6).
Thus, w.l.o.g., assume that v1, . . . , vm−2 are all non-zero vectors. Further, note that for every
i ̸= j ∈ [m − 2], 〈yi , y j 〉 = 〈vi , v j 〉 − αi · α j ≤ 〈vi , v j 〉 ≤ 0. Thus, we have reduced problem on m
vectors with dimension N to an equivalent problem on m−2 vectors with dimension dimension
N − 1. If we continue this process, we can conclude that every loss in dimension of the vector
results in twice in loss in the numbers of the vectors in the set. Induction then implies that
m ≤ 2N , as desired.
We now move on to the proof of the second part. Deﬁne z = v1 + . . . + vm. Now consider the
following sequence of relationships:

∥z∥
2 = m∑

i =1
∥vi ∥
2 + 2∑

i < j〈vi , v j 〉 ≤ m + 2 ·
 (m
2
 )
 · (−ε) = m(1 − εm + ε).

The inequality follows from the facts that each vi is a unit vector and the assumption that for
every i ̸= j , 〈vi .v j 〉 ≤ −ε. As ∥z∥
2 ≥ 0,
 m(1 − εm + ε) ≥ 0.

Since m ≥ 1, we have that 1 − εm + ε ≥ 0

85

or εm ≤ 1 + ε.

Thus, we have m ≤ 1 + 1
ε , as desired. ✷
Finally, we prove Lemma 4.4.4.

Proof of Lemma 4.4.4. We begin by deﬁning a map φ : [q] → Rq with certain properties. Then
we apply φ to all the coordinates of a codeword to deﬁne the map f : Rq → R
nq that satisﬁes the
claimed properties. We now ﬁll in the details.
Deﬁne φ : [q] → Rq as follows. For every i ∈ [q], we deﬁne

φ(i ) =
 〈 1
q , 1
q , . . . , −(q − 1)
q
︸ ︷︷ ︸
i thposition
, . . . 1
q
 〉
 .

That is, all but the i ’th position in φ(i ) ∈ Rq has a value of 1/q and the i th position has value
−(q − 1)/q.
Next, we record two properties of φ that follow immediately from its deﬁnition. For every
i ∈ [q],
 φ(i )2 = (q − 1)
q 2 + (q − 1)2

q 2 = (q − 1)
q . (4.8)

Also for every i ̸= j ∈ [q],
 〈φ(i ), φ( j )〉 = (q − 2)
q 2 − 2(q − 1)
q 2 = − 1
q . (4.9)

We are now ready to deﬁne our ﬁnal map f : C → R
nq . For every c = (c1, . . . , cn) ∈ C , deﬁne

f (c) =
 √ q
n(q − 1) · (
φ(c1), φ(c2), . . . , φ(cn)) .

(The multiplicative factor √ q
n(q−1) is to ensure that f (c) for any c ∈ C is a unit vector.)
To complete the proof, we will show that f satisﬁes the claimed properties. We begin with
condition 1. Note that
 ∥ f (c)∥
2 = q
(q − 1)n · n∑

i =1
 ∣φ(i )∣2 = 1,

where the ﬁrst equality follows from the deﬁnition of f and the second equality follows from
(4.8).
We now turn to the second condition. For notational convenience, deﬁne c1 = (x1, . . . , xn)
and c2 = (y1, . . . , yn). Consider the following sequence of relations:

〈 f (c1), f (c2)〉 = n∑

ℓ=1
 〈 f (xℓ), f (yℓ)〉
 86

=
 [ ∑

ℓ:xℓ̸=yℓ
 〈φ(xℓ), φ(yℓ)〉 + ∑

ℓ:xℓ=yℓ
 〈φ(xℓ), φ(yℓ)〉]
 · ( q
n(q − 1)
 )

=
 [ ∑

ℓ:xℓ̸=yℓ
 ( −1
q
 ) + ∑

ℓ:xℓ=yℓ
 ( q − 1
q
 )]
 · ( q
n(q − 1)
 ) (4.10)

= [
∆(c1, c2) ( −1
q
 ) + (n − ∆(c1, c2)) ( q − 1
q
 )] · ( q
n(q − 1)
 ) (4.11)

= 1 − ∆(c1, c2) ( q
n(q − 1)
 ) [ 1
q + q − 1
q
 ]

= 1 − ( q
q − 1
 ) ( ∆(c1, c2)
n
 ) ,

as desired. In the above, (4.10) is obtained using (4.9) and (4.8) while (4.11) follows from the
deﬁnition of the Hamming distance. ✷

4.5 Exercises

Exercise 4.1. Pick a (n − k) × n matrix H over Fq at random. Show that with high probability the
code whose parity check matrix is H achieves the GV bound.

Exercise 4.2. Recall the deﬁnition of an ε-biased space from Exercise 2.14. Show that there exists
an ε-biased space of size O(k/ε2).

Hint: Recall part 1 of Exercise 2.14.

Exercise 4.3. Argue that a random linear code as well as its dual both lie on the corresponding
GV bound.

Exercise 4.4. In Section 4.2.2, we saw that random linear code meets the GV bound. It is natural
to ask the question for general random codes. (By a random (n, k)q code, we mean the following:
for each of the q k messages, pick a random vector from [q]
n. Further, the choices for each
codeword is independent.) We will do so in this problem.

1. Prove that a random q-ary code with rate R > 0 with high probability has relative distance
δ ≥ H −1
q (1 − 2R − ε). Note that this is worse than the bound for random linear codes in
Theorem 4.2.1.

2. Prove that with high probability the relative distance of a random q-ary code of rate R is
at most H −1
q (1 − 2R) + ε. In other words, general random codes are worse than random
linear codes in terms of their distance.

Hint: Use Chebyshev’s inequality.

Exercise 4.5. We saw that Algorithm 6 can compute an (n, k)q code on the GV bound in time
qO(n). Now the construction for linear codes is a randomized construction and it is natural to
ask how quickly can we compute an [n, k]q code that meets the GV bound. In this problem,

87

we will see that this can also be done in qO(n) deterministic time, though the deterministic
algorithm is not that straight-forward anymore.

1. Argue that Theorem 4.2.1 gives a qO(kn) time algorithm that constructs an [n, k]q code
on the GV bound. (Thus, the goal of this problem is to “shave" off a factor of k from the
exponent.)

2. A k ×n Toeplitz Matrix A = {Ai , j }k , n
i =1, j =1 satisﬁes the property that Ai , j = Ai −1, j −1. In other
words, any diagonal has the same value. For example, the following is a 4 × 6 Toeplitz
matrix: 





 1 2 3 4 5 6
7 1 2 3 4 5
8 7 1 2 3 4
9 8 7 1 2 3
 






A random k × n Toeplitz matrix T ∈ Fk×n
q is chosen by picking the entries in the ﬁrst row
and column uniformly (and independently) at random.

Prove the following claim: For any non-zero m ∈ F
k
q , the vector m · T is uniformly dis-
tributed over Fn
q , that is for every y ∈ Fn
q , Pr [m · T = y
] = q −n.

3. Brieﬂy argue why the claim in part 2 implies that a random code deﬁned by picking its
generator matrix as a random Toeplitz matrix with high probability lies on the GV bound.

4. Conclude that an [n, k]q code on the GV bound can be constructed in time qO(k+n).

Exercise 4.6. Show that one can construct the parity check matrix of an [n, k]q code that lies on
the GV bound in time qO(n).

Exercise 4.7. So far in Exercises 4.5 and 4.6, we have seen two constructions of [n, k]q code on
the GV bound that can be constructed in qO(n) time. For constant rate codes, at the time of
writing of this book, this is fastest known construction of any code that meets the GV bound.
For k = o(n), there is a better construction known, which we explore in this exercise.
We begin with some notation. For the rest of the exercise we will target a distance of d = δn.
Given a message m ∈ Fk
q and an [n, k]q code C , deﬁne the indicator variable:

Wm(C ) = { 1 if w t (C (m)) < d
0 otherwise.

Further, deﬁne D(C ) = ∑

m∈Fk
q \{0}Wm(C ).

We will also use D(G) and Wm(G) to denote the variables above for the code C generated by G.
Given an k × n matrix M , we will use M i to denote the i th column of M and M ≤i to denote
the column submatrix of M that contains the ﬁrst i columns. Finally below we will use G to
denote a uniformly random k × n generator matrix and G to denote a speciﬁc instantiation of
the generator matrix. We will arrive at the ﬁnal construction in a sequence of steps. In what
follows deﬁne k < (1 − Hq (δ))n for large enough n.

88

1. Argue that C has a distance d if and only if D(C ) < 1.

2. Argue that E [D(G )] < 1.

3. Argue that for any 1 ≤ i < n and ﬁxed k × n matrix G,

min
v∈Fk
q E [
D(G )|G ≤i = G ≤i , G i +1 = v
] ≤ E [
D(G )|G ≤i = G ≤i ] .

4. We are now ready to deﬁne the algorithm to compute the ﬁnal generator matrix G: see Al-
gorithm 7. Prove that Algorithm 7 outputs a matrix G such that the linear code generated

Algorithm 7 qO(k) time algorithm to compute a code on the GV bound
INPUT: Integer parameters 1 ≤ k ̸= n such that k < (1 − Hq (δ)n)
OUTPUT: An k × n generator matrix G for a code with distance δn

1: Initialize G to be the all 0s matrix ⊲ This initialization is arbitrary

2: FOR every 1 ≤ i ≤ n DO

3: G i ← arg minv∈Fk
q E [D(G )|G ≤i = G ≤i , G i +1 = v
]

4: RETURN G

by G is an [n, k, δn]q code. Conclude that this code lies on the GV bound.

5. Finally, we will analyze the run time of Algorithm 7. Argue that Step 2 can be implemented
in poly (
n, q k ) time. Conclude Algorithm 7 can be implemented in time poly (
n, q k )
.

Hint: It might be useful to maintain a data structure that keeps track of one number for every non-zero

m ∈ Fk
q throughout the run of Algorithm 7.

Exercise 4.8. In this problem we will derive the GV bound using a graph-theoretic proof, which
is actually equivalent to the greedy proof we saw in Section 4.2.1. Let 1 ≤ d ≤ n and q ≥ 1 be
integers. Now consider the graph Gn,d ,q = (V, E ), where the vertex set is the set of all vectors in
[q]
n. Given two vertices u ̸= v ∈ [q]
n, we have the edge (u, v) ∈ E if and only if ∆(u, v) < d . An
independent set of a graph G = (V, E ) is a subset I ⊆ V such that for every u ̸= v ∈ I , we have that
(u, v) is not an edge. We now consider the following sub-problems:

1. Argue that any independent set C of Gn,d ,q is a q-ary code of distance d .

2. The degree of a vertex in a graph G is the number of edges incident on that vertex. Let ∆
be the maximum degree of any vertex in G = (V, E ).Then argue that G has an independent
set of size at least |V |
∆+1 .

3. Using parts 1 and 2 argue the GV bound.

89

Exercise 4.9. In this problem we will improve slightly on the GV bound using a more sophisti-
cated graph-theoretic proof. Let Gn,d ,q and N and ∆ be as in the previous exercise (Exercise 4.8).
So far we used the fact that Gn,d ,q has many vertices and small degree to prove it has a large in-
dependent set, and thus to prove there is a large code of minimum distance d . In this exercise
we will see how a better result can be obtained by counting the number of “triangles” in the
graph. A triangle in a graph G = (V, E ) is a set {u, v, w} ⊂ V of three vertices such that all three
vertices are adjancent, i.e., (u, v), (v, w), (w, u) ∈ E . For simplicity we will focus on the case where
q = 2 and d = n/5, and consider the limit as n → ∞.

1. Prove that a graph on N vertices of maximum degree ∆ has at most O(N ∆
2) triangles.

2. Prove that the number of triangle in graph Gn,d ,2 is at most

2n · ∑

0≤e≤3d /2
 (n
e
 )
 · 3e .

Hint: Fix u and let e count the number of coordinates where at least one of v or w disagree
with u. Prove that e is at most 3d /2.

3. Simplify the expression in the case where d = n/5 to show that the number of triangles in
Gn,n/5,2 is O(N · ∆
2−η) for some η > 0.

4. A famous result in the “probabilistic method” shows (and you don’t have to prove this),
that if a graph on N vertices of maximum degree ∆ has at most O(N · ∆
2−η) triangles,
then it has an independent set of size Ω( N
∆ log ∆). Use this result to conclude that there
is a binary code of block length n and distance n/5 of size Ω(n2n/
( n
n/5)). (Note that this
improves over the GV-bound by an Ω(n) factor.)

Exercise 4.10. Use part 2 from Exercise 1.7 to prove the Singleton bound.

Exercise 4.11. Let C be an (n, k, d )q code. Then prove that ﬁxing any n −d +1 positions uniquely
determines the corresponding codeword.

Exercise 4.12. Let C be a binary code of block length n and distance n/2. Then |C | ≤ 2n. (Note
that this is a factor 2 better than part 1 in Theorem 4.4.1.)

Exercise 4.13. Prove that the bound in Exercise 4.12 is tight– i.e. there exists binary codes C with
block length n and distance n/2 such that |C | = 2n.

Exercise 4.14. Prove that part 1 of Lemma 4.4.3 is tight.

Exercise 4.15. In this exercise we will prove the Plotkin bound (at least part 2 of Theorem 4.4.1)
via a purely combinatorial proof.

Given an (n, k, d )q code C with d > (1 − 1
q
 ) n deﬁne

S = ∑

c1̸=c2∈C ∆(c1, c2).

For the rest of the problem think of C has an |C | × n matrix where each row corresponds to a
codeword in C . Now consider the following:
 90

1. Looking at the contribution of each column in the matrix above, argue that

S ≤ (1 − 1
q
 ) · n|C |2.

2. Look at the contribution of the rows in the matrix above, argue that

S ≥ |C | (|C | − 1) · d .

3. Conclude part 2 of Theorem 4.4.1.

Exercise 4.16. In this exercise, we will prove the so called Griesmer Bound. For any [n, k, d ]q ,
prove that
 n ≥ k−1∑

i =0
 ⌈ d

q i
 ⌉ .

Hint: Recall Exercise 2.17.

Exercise 4.17. Use Exercise 4.16 to prove part 2 of Theorem 4.4.1 for linear codes.

Exercise 4.18. Use Exercise 4.16 to prove Theorem 4.3.1 for linear code.

4.6 Bibliographic Notes

Theorem 4.2.1 was proved for general codes by Edgar Gilbert ([35]) and for linear codes by Rom
Varshamov ([102]). Hence, the bound is called the Gilbert-Varshamov bound. The Singleton
bound (Theorem 4.3.1) is due to Richard C. Singleton [92]. For larger (but still constant) values
of q, better lower bounds than the GV bound are known. In particular, for any prime power
q ≥ 49, there exist linear codes, called algebraic geometric (or AG) codes that outperform the
corresponding GV bound3. AG codes out of the scope of this book. One starting point could be
the following [56].
The proof method illustrated in Exercise 4.15has a name– double counting: in this speciﬁc
case this follows since we count S in two different ways.

3The lower bound of 49 comes about as AG codes are only deﬁned for q being a square (i.e. q = (q ′)
2) and it
turns out that q ′ = 7 is the smallest value where AG bound beats the GV bound.

9192

Chapter 5

The Greatest Code of Them All:
Reed-Solomon Codes

In this chapter, we will study the Reed-Solomon codes. Reed-Solomon codes have been studied
a lot in coding theory. These codes are optimal in the sense that they meet the Singleton bound
(Theorem 4.3.1). We would like to emphasize that these codes meet the Singleton bound not
just asymptotically in terms of rate and relative distance but also in terms of the dimension,
block length and distance. As if this were not enough, Reed-Solomon codes turn out to be more
versatile: they have many applications outside of coding theory. (We will see some applications
later in the book.)
These codes are deﬁned in terms of univariate polynomials (i.e. polynomials in one un-
known/variable) with coefﬁcients from a ﬁnite ﬁeld Fq . It turns out that polynomials over Fp ,
for prime p, also help us deﬁne ﬁnite ﬁelds Fp s , for s > 1. To kill two birds with one stone
1, we
ﬁrst do a quick review of polynomials over ﬁnite ﬁelds. Then we will deﬁne and study some
properties of Reed-Solomon codes.

5.1 Polynomials and Finite Fields

We begin with the formal deﬁnition of a (univariate) polynomial.

Deﬁnition 5.1.1. Let Fq be a ﬁnite ﬁeld with q elements. Then a function F (X ) = ∑∞
i =0 fi X i , fi ∈
Fq is called a polynomial.

For our purposes, we will only consider the ﬁnite case; that is, F (X ) = ∑d
i =0 fi X i for some
integer d > 0, with coefﬁcients fi ∈ Fq , and fd ̸= 0. For example, 2X 3+X 2+5X +6 is a polynomial
over F7.
Next, we deﬁne some useful notions related to polynomials. We begin with the notion of
degree of a polynomial.

1No birds will be harmed in this exercise.
 93

Deﬁnition 5.1.2. For F (X ) = ∑d
i =0 fi X i with fd ̸= 0, we call d the degree of F (X ). We denote the
degree of the polynomial F (X ) by deg(F ).

For example, 2X 3 + X 2 + 5X + 6 has degree 3.
Let Fq [X ] be the set of polynomials over Fq , that is, with coefﬁcients from Fq . Let F (X ),G(X ) ∈
Fq [X ] be polynomials. Then Fq [X ] has the following natural operations deﬁned on it:

Addition:
 F (X ) +G(X ) =
 max(deg(F ),deg(G))∑

i =0 ( fi + gi )X i ,

where the addition on the coefﬁcients is done over Fq . For example, over F2, X + (1 + X ) =
X · (1 + 1) + 1 · (0 + 1) = 1 (recall that over F2, 1 + 1 = 0).2

Multiplication:
 F (X ) · G(X ) =
 deg(F )+deg(G)∑

i =0
 (min(i ,deg(F ))∑

j =0 p j · qi − j
 )
 X i ,

where all the operations on the coefﬁcients are over Fq . For example, over F2, X (1 + X ) =
X + X 2; (1+ X )2 = 1+2X + X 2 = 1+ X 2, where the latter equality follows since 2 ≡ 0 mod 2.

Next, we deﬁne a root of a polynomial.

Deﬁnition 5.1.3. α ∈ Fq is a root of a polynomial F (X ), if F (α) = 0.

For instance, 1 is a root of 1 + X 2 over F2.
We will also need the notion of a special class of polynomials, which are analogous to how
prime numbers are special for natural numbers.

Deﬁnition 5.1.4. A polynomial F (X ) is irreducible if for every G1(X ),G2(X ) such that F (X ) =
G1(X )G2(X ), we have min(deg(G1), deg(G2)) = 0

For example, 1 + X 2 is not irreducible over F2, as (1 + X )(1 + X ) = 1 + X 2. However, 1 + X + X 2

is irreducible, since its non-trivial factors have to be from the linear terms X or X + 1. However,
it is easy to check that neither is a factor of 1 + X + X 2. (In fact, one can show that 1 + X + X 2

is the only irreducible polynomial of degree 2 over F2– see Exercise 5.1.) A word of caution: if
a polynomial E (X ) ∈ Fq [X ] has no root in Fq , it does not mean that E (X ) is irreducible. For
example consider the polynomial (1 + X + X 2)2 over F2– it does not have any root in F2 but it
obviously is not irreducible.
Just as the set of integers modulo a prime is a ﬁeld, so is the set of polynomials modulo an
irreducible polynomial:

Theorem 5.1.1. Let E (X ) be an irreducible polynomial with degree at least 2 over Fp , p prime.
Then the set of polynomials in Fp [X ] modulo E (X ), denoted by Fp [X ]/E (X ), is a ﬁeld.

2This will be a good time to remember that operations over a ﬁnite ﬁeld are much different from operations over
integers/reals. For example, over reals/integers X + (X + 1) = 2X + 1.

94

The proof of the theorem above is similar to the proof of Lemma 2.1.2, so we only sketch the
proof here. In particular, we will explicitly state the basic tenets of Fp [X ]/E (X ).

• Elements are polynomials in Fp [X ] of degree at most s − 1. Note that there are p s such
polynomials.

• Addition: (F (X ) +G(X )) mod E (X ) = F (X ) mod E (X ) + G(X ) mod E (X ) = F (X ) + G(X ).
(Since F (X ) and G(X ) are of degree at most s − 1, addition modulo E (X ) is just plain poly-
nomial addition.)

• Multiplication: (F (X ) · G(X )) mod E (X ) is the unique polynomial R(X ) with degree at
most s − 1 such that for some A(X ), R(X ) + A(X )E (X ) = F (X ) · G(X )

• The additive identity is the zero polynomial, and the additive inverse of any element F (X )
is −F (X ).

• The multiplicative identity is the constant polynomial 1. It can be shown that for every
element F (X ), there exists a unique multiplicative inverse (F (X ))−1.

For example, for p = 2 and E (X ) = 1+X +X 2, F2[X ]/(1+X +X 2) has as its elements {0, 1, X , 1+
X }. The additive inverse of any element in F2[X ]/(1 + X + X 2) is the element itself while the
multiplicative inverses of 1, X and 1 + X in F2[X ]/(1 + X + X 2) are 1, 1 + X and X respectively.
A natural question to ask is if irreducible polynomials exist for every degree. Indeed, they
do:

Theorem 5.1.2. For all s ≥ 2 and Fp , there exists an irreducible polynomial of degree s over Fp . In

fact, the number of such irreducible polynomials is Θ ( p s

s
 ).

The result is true even for general ﬁnite ﬁelds Fq and not just prime ﬁelds but we stated the
version over prime ﬁelds for simplicity. Given any monic 3 polynomial E (X ) of degree s, it can be
veriﬁed whether it is an irreducible polynomial by checking if gcd(E (X ), X q s − X ) = E (X ). This
is true as the product of all monic irreducible polynomials in Fq [X ] of degree exactly s is known
to be the polynomial X q s − X . Since Euclid’s algorithm for computing the gcd(F (X ),G(X )) can
be implemented in time polynomial in the minimum of deg(F ) and deg(G) and log q (see Sec-
tion D.7.2), this implies that checking whether a given polynomial of degree s over Fq [X ] is
irreducible can be done in time poly(s, log q).
This implies an efﬁcient Las Vegas algorithm4 to generate an irreducible polynomial of de-
gree s over Fq . Note that the algorithm is to keep on generating random polynomials until it
comes across an irreducible polynomial (Theorem 5.1.2 implies that the algorithm will check
O (p s) polynomials in expectation). Algorithm 8 presents the formal algorithm.
The above discussion implies the following:

3I.e. the coefﬁcient of the highest degree term is 1. It is easy to check that if E (X ) = es X s + es−1X s−1 + · · · + 1 is
irreducible, then e−1
s · E (X ) is also an irreducible polynomial.
4A Las Vegas algorithm is a randomized algorithm which always succeeds and we consider its time complexity
to be its expected worst-case run time.
 95

Algorithm 8 Generating Irreducible Polynomial
INPUT: Prime power q and an integer s > 1
OUTPUT: A monic irreducible polynomial of degree s over Fq

1: b ← 0

2: WHILE b = 0 DO

3: F (X ) ← X s + ∑s−1
i =0 fi X i , where each fi is chosen uniformly at random from Fq .

4: IF gcd(F (X ), X q s − X ) = F (X ) THEN

5: b ← 1.

6: RETURN F (X )

Corollary 5.1.3. There is a Las Vegas algorithm to generate an irreducible polynomial of degree s
over any Fq in expected time poly(s, log q).

Now recall that Theorem 2.1.3 states that for every prime power p s, there a unique ﬁeld Fp s .
This along with Theorems 5.1.1 and 5.1.2 imply that:

Corollary 5.1.4. The ﬁeld Fp s is Fp [X ]/E (X ), where E (X ) is an irreducible polynomial of degree
s.

5.2 Reed-Solomon Codes

Recall that the Singleton bound (Theorem 4.3.1) states that for any (n, k, d )q code, k ≤ n − d + 1.
Next, we will study Reed-Solomon codes, which meet the Singleton bound, i.e. satisfy k = n −
d + 1 (but have the unfortunate property that q ≥ n). Note that this implies that the Singleton
bound is tight, at least for q ≥ n.
We begin with the deﬁnition of Reed-Solomon codes.

Deﬁnition 5.2.1 (Reed-Solomon code). Let Fq be a ﬁnite ﬁeld. Let α1, α2, ...αn be distinct el-
ements (also called evaluation points) from Fq and choose n and k such that k ≤ n ≤ q. We
deﬁne an encoding function for Reed-Solomon code as RS : F
k
q → Fn
q as follows. A message
m = (m0, m1, ..., mk−1) with mi ∈ Fq is mapped to a degree k − 1 polynomial.

m 7→ fm(X ),

where
 fm(X ) = k−1∑

i =0 mi X i . (5.1)

Note that fm(X ) ∈ Fq [X ] is a polynomial of degree at most k − 1. The encoding of m is the
evaluation of fm(X ) at all the αi ’s :

RS(m) = ( fm(α1), fm(α2), ..., fm(αn)) .

We call this image Reed-Solomon code or RS code. A common special case is n = q − 1 with the

set of evaluation points being F∗ def
= F \ {0}.
 96

For example, the ﬁrst row below are all the codewords in the [3, 2]3 Reed-Solomon codes
where the evaluation points are F3 (and the codewords are ordered by the corresponding mes-
sages from F2
3 in lexicographic order where for clarity the second row shows the polynomial
fm(X ) for the corresponding m ∈ F2
3 in gray):

(0,0,0), (1,1,1), (2,2,2), (0,1,2), (1,2,0), (2,0,1), (0,2,1), (1,0,2), (2,1,0)
0, 1, 2, X, X+1, X+2, 2X, 2X+1, 2X+2

Notice that by deﬁnition, the entries in {α1, ..., αn} are distinct and thus, must have n ≤ q.
We now turn to some properties of Reed-Solomon codes.

Claim 5.2.1. RS codes are linear codes.

Proof. The proof follows from the fact that if a ∈ Fq and f (X ), g (X ) ∈ Fq [X ] are polynomials of
degree ≤ k −1, then a f (X ) and f (X )+ g (X ) are also polynomials of degree ≤ k −1. In particular,
let messages m1 and m2 be mapped to fm1(X ) and fm2(X ) where fm1(X ), fm2(X ) ∈ Fq [X ] are
polynomials of degree at most k − 1 and because of the mapping deﬁned in (5.1), it is easy to
verify that: fm1(X ) + fm2(X ) = fm1+m2(X ),

and a fm1(X ) = fam1(X ).

In other words, RS(m1) + RS(m2) = RS(m1 + m2)

aRS(m1) = RS(am1).

Therefore RS is a [n, k]q linear code.

The second and more interesting claim is the following:

Claim 5.2.2. RS is a [n, k, n − k + 1]q code. That is, it matches the Singleton bound.

The claim on the distance follows from the fact that every non-zero polynomial of degree
k − 1 over Fq [X ] has at most k − 1 (not necessarily distinct) roots, which we prove ﬁrst (see
Proposition 5.2.3 below). This implies that if two polynomials agree on more than k − 1 places
then they must be the same polynomial– note that this implies two polynomials when evaluated
at the same n points must differ in at least n−(k −1) = n−k +1 positions, which is what we want.

Proposition 5.2.3 (“Degree Mantra"). A nonzero polynomial f (X ) of degree t over a ﬁeld Fq has
at most t roots in Fq

Proof. We will prove the theorem by induction on t . If t = 0, we are done. Now, consider f (X )
of degree t > 0. Let α ∈ Fq be a root such that f (α) = 0. If no such root α exists, we are done. If
there is a root α, then we can write
 f (X ) = (X − α)g (X )

97

where deg(g ) = deg( f ) − 1 (i.e. X − α divides f (X )). Note that g (X ) is non-zero since f (X ) is
non-zero. This is because by the fundamental rule of division of polynomials:

f (X ) = (X − α)g (X ) + R(X )

where deg(R) ≤ 0 (as the degree cannot be negative this in turn implies that deg(R) = 0) and
since f (α) = 0, f (α) = 0 + R(α),

which implies that R(α) = 0. Since R(X ) has degree zero (i.e. it is a constant polynomial), this
implies that R(X ) ≡ 0.
Finally, as g (X ) is non-zero and has degree t − 1, by induction, g (X ) has at most t − 1 roots,
which implies that f (X ) has at most t roots.

We are now ready to prove Claim 5.2.2

Proof of Claim 5.2.2. We start by proving the claim on the distance. Fix arbitrary m1 ̸= m2 ∈
Fk
q . Note that fm1(X ), fm2(X ) ∈ Fq [X ] are distinct polynomials of degree at most k − 1 since
m1 ̸= m2 ∈ Fk
q . Then fm1(X ) − fm2(X ) ̸= 0 also has degree at most k − 1. Note that w t (RS(m2) −
RS(m1)) = ∆(RS(m1), RS(m2)). The weight of RS(m2)−RS(m1) is n minus the number of zeroes
in RS(m2) − RS(m1), which is equal to n minus the number of roots that fm1(X ) − fm2(X ) has
among {α1, ..., αn}. That is,

∆(RS(m1), RS(m2)) = n − |{αi | fm1(αi ) = fm2(αi )}|.

By Proposition 5.2.3, fm1(X ) − fm2(X ) has at most k − 1 roots. Thus, the weight of RS(m2) −
RS(m1) is at least n − (k − 1) = n − k + 1. Therefore d ≥ n − k + 1, and since the Singleton bound
(Theorem 4.3.1) implies that d ≤ n−k+1, we have d = n−k+1.5 The argument above also shows
that distinct polynomials fm1(X ), fm2(X ) ∈ Fq [X ] are mapped to distinct codewords. (This is
because the Hamming distance between any two codewords is at least n − k + 1 ≥ 1, where the
last inequality follows as k ≤ n.) Therefore, the code contains q k codewords and has dimension
k. The claim on linearity of the code follows from Claim 5.2.1. ✷
Recall that the Plotkin bound (Corollary 4.4.2) implies that to achieve the Singleton bound,
the alphabet size cannot be a constant. Thus, some dependence of q on n in Reed-Solomon
codes is unavoidable.
Let us now ﬁnd a generator matrix for RS codes (which exists by Claim 5.2.1). By Deﬁ-
nition 5.2.1, any basis fm1, ..., fmk of polynomial of degree at most k − 1 gives rise to a basis
RS(m1), ..., RS(mk ) of the code. A particularly nice polynomial basis is the set of monomials
1, X , ..., X i , ..., X k−1. The corresponding generator matrix, whose i th row (numbering rows from
0 to k − 1 ) is (α
i
1, α
i
2, ..., α
i
j , ..., α
i
n)

and this generator matrix is called the Vandermonde matrix of size k × n:

5See Exercise 5.3 for an alternate direct argument.
 98
















 1 1 1 1 1 1
α1 α2 · · · α j · · · αn
α
2
1 α
2
2 · · · α
2
j · · · α
2
n
... ... . . . ... . . . ...
α
i
1 α
i
2 · · · α
i
j · · · α
i
n
... ... . . . ... . . . ...
α
k−1
1 α
k−1
2 · · · α
k−1
j · · · α
k−1
n
 















The class of codes that match the Singleton bound have their own name, which we deﬁne
and study next.

5.3 A Property of MDS Codes

Deﬁnition 5.3.1 (MDS codes). An (n, k, d )q code is called Maximum Distance Separable (MDS)
if d = n − k + 1.

Thus, Reed-Solomon codes are MDS codes.
Next, we prove an interesting property of an MDS code C ⊆ Σn with integral dimension k.
We begin with the following notation.

Deﬁnition 5.3.2. For any subset of indices S ⊆ [n] of size exactly k and a code C ⊆ Σn, CS is the
set of all codewords in C projected onto the indices in S.

MDS codes have the following nice property that we shall prove for the special case of Reed-
Solomon codes ﬁrst and subsequently for the general case as well.

Proposition 5.3.1. Let C ⊆ Σn of integral dimension k be an MDS code, then for all S ⊆ [n] such
that |S| = k, we have |CS| = Σk .

Before proving Proposition 5.3.1 in its full generality, we present its proof for the special case of
Reed-Solomon codes.
Consider any S ⊆ [n] of size k and ﬁx an arbitrary v = (v1, . . . , vk ) ∈ Fk
q , we need to show that
there exists a codeword c ∈ RS (assume that the RS code evaluates polynomials of degree at
most k − 1 over α1, . . . , αn ⊆ Fq ) such that cS = v. Consider a generic degree k − 1 polynomial
F (X ) = ∑k−1
i =0 fi X i . Thus, we need to show that there exists F (X ) such that F (αi ) = vi for all i ∈
S, where |S| = k.

For notational simplicity, assume that S = [k]. We think of fi ’s as unknowns in the equations
that arise out of the relations F (αi ) = vi . Thus, we need to show that there is a solution to the
following system of linear equations:
 99

( p0 p1 · · · pk−1 )
 








 1 1 1
α1 αi αk
α
2
1 α
2
i α
2
k
... ... ...
α
k−1
1 α
k−1
i α
k−1
k
 








 =
 







 v1
v2
v3
...
vk
 








The above constraint matrix is a Vandermonde matrix and is known to have full rank (see Ex-
ercise 5.7). Hence, by Exercise 2.6, there always exists a unique solution for (p0, . . . , pk−1). This
completes the proof for Reed-Solomon codes.

Next, we prove the property for the general case which is presented below

Proof of Proposition 5.3.1. Consider a |C | × n matrix where each row represents a codeword
in C . Hence, there are |C | = |Σ|k rows in the matrix. The number of columns is equal to the
block length n of the code. Since C is Maximum Distance Separable, its distance d = n − k + 1.

Let S ⊆ [n] be of size exactly k. It is easy to see that for any ci ̸= c j ∈ C , the corresponding
projections ci
S and c j
S ∈ CS are not the same. As otherwise △(ci , c j ) ≤ d −1, which is not possible
as the minimum distance of the code C is d . Therefore, every codeword in C gets mapped to a
distinct codeword in CS. As a result, |CS| = |C | = |Σ|k . As CS ⊆ Σk , this implies that CS = Σk , as
desired. ✷
Proposition 5.3.1 implies an important property in pseudorandomness: see Exercise 5.8 for
more.

5.4 Exercises

Exercise 5.1. Prove that X 2 + X + 1 is the unique irreducible polynomial of degree two over F2.

Exercise 5.2. Argue that any function f : Fq → Fq is equivalent to a polynomial P (X ) ∈ Fq [X ] of
degree at most q − 1: that is, for every α ∈ Fq

f (α) = P (α).

Exercise 5.3. For any [n, k]q Reed-Solomon code, exhibit two codewords that are at Hamming
distance exactly n − k + 1.

Exercise 5.4. Let RSF∗
q [n, k] denote the Reed-Solomon code over Fq where the evaluation points
is Fq (i.e. n = q). Prove that (
RSFq [n, k]
)⊥ = RSFq [n, n − k],

that is, the dual of these Reed-Solomon codes are Reed-Solomon codes themselves. Conclude
that Reed-Solomon codes contain self-dual codes (see Exercise 2.31 for a deﬁnition).

Hint: Exercise 2.2 might be useful.
 100

Exercise 5.5. Since Reed-Solomon codes are linear codes, by Proposition 2.3.3, one can do error
detection for Reed-Solomon codes in quadratic time. In this problem, we will see that one can
design even more efﬁcient error detection algorithm for Reed-Solomon codes. In particular, we
will consider data streaming algorithms (see Section 19.5 for more motivation on this class of al-
gorithms). A data stream algorithm makes a sequential pass on the input, uses poly-logarithmic
space and spend only poly-logarithmic time on each location in the input. In this problem we
show that there exists a randomized data stream algorithm to solve the error detection problem
for Reed-Solomon codes.

1. Give a randomized data stream algorithm that given as input a sequence (i1, α1), . . . , (in, αn) ∈
[m] × Fq that implicitly deﬁnes y ∈ Fm
q , where for any ℓ ∈ [m], yℓ = ∑ j ∈[n]|i j =ℓ αℓ, decides
whether y = 0 with probability at least 2/3. Your algorithm should use O(log q(m + n))
space and polylog(q(m + n)) time per position of y. For simplicity, you can assume that
given an integer t ≥ 1 and prime power q, the algorithm has oracle access to an irreducible
polynomial of degree t over Fq .

Hint: Use Reed-Solomon codes.

2. Given [q, k]q Reed-Solomon code C (i.e. with the evaluation points being Fq ), present a
data stream algorithm for error detection of C with O(log q) space and polylogq time per
position of the received word. The algorithm should work correctly with probability at
least 2/3. You should assume that the data stream algorithm has access to the values of k
and q (and knows that C has Fq as its evaluation points).

Hint: Part 1 and Exercise 5.4 should be helpful.

Exercise 5.6. We have deﬁned Reed-Solomon in this chapter and Hadamard codes in Section 2.7.
In this problem we will prove that certain alternate deﬁnitions also sufﬁce.

1. Consider the Reed-Solomon code over a ﬁeld Fq and block length n = q − 1 deﬁned as

RSF∗
q [n, k, n − k + 1] = {(p(1), p(α), . . . , p(α
n−1)) | p(X ) ∈ F[X ] has degree ≤ k − 1}

where α is the generator of the multiplicative group F∗ of F.6

Prove that

RSF∗
q [n, k, n − k + 1] = {(c0, c1, . . . , cn−1) ∈ Fn | c(α
ℓ) = 0 for 1 ≤ ℓ ≤ n − k ,

where c(X ) = c0 + c1X + · · · + cn−1X n−1} . (5.2)

Hint: Exercise 2.2 might be useful.

2. Recall that the [2r , r, 2r −1]2 Hadamard code is generated by the r ×2r matrix whose i th (for
0 ≤ i ≤ 2r − 1) column is the binary representation of i . Brieﬂy argue that the Hadamard

6This means that F∗
q = {1, α, . . . , αn−1}. Further, αn = 1.

101

codeword for the message (m1, m2, . . . , mr ) ∈ {0, 1}r is the evaluation of the (multivariate)
polynomial m1X1 + m2X2 + · · · + mr Xr (where X1, . . . , Xr are the r variables) over all the
possible assignments to the variables (X1, . . . , Xr ) from {0, 1}r .

Using the deﬁnition of Hadamard codes above (re)prove the fact that the code has dis-
tance 2r −1.

Exercise 5.7. Prove that the k × k Vandermonde matrix (where the (i , j )th entry is α
i
j ) has full
rank (where α1, . . . , αk are distinct).

Exercise 5.8. A set S ⊆ Fn
q is said to be a t -wise independent source (for some 1 ≤ t ≤ n) if given a
uniformly random sample (X1, . . . , Xn) from S, the n random variables are t -wise independent:
i.e. any subset of t variables are uniformly independent random variables over Fq . We will
explore properties of these objects in this exercise.

1. Argue that the deﬁnition of t -wise independent source is equivalent to the deﬁnition in
Exercise 2.13.

2. Argue that for any k ≥ 1, any [n, k]q code C is a 1-wise independent source.

3. Prove that any [n, k]q MDS code is a k-wise independent source.

4. Using part 3 or otherwise prove that there exists a k-wise independent source over F2 of
size at most (2n)k . Conclude that k(log2 n + 1) uniformly and independent random bits
are enough to compute n random bits that are k-wise independent. Improve the bound
slightly to show that k(log2 n − log2 log2 n + O(1))-random bits are enough to generate k-
wise independent source over F2.

5. For 0 < p ≤ 1/2, we say the n binary random variables X1, . . . , Xn are p-biased and t -
wise independent if any of the t random variables are independent and Pr [Xi = 1] = p
for every i ∈ [n]. For the rest of the problem, let p be a power of 1/2. Then show that
any t · log2(1/p)-wise independent random variables can be converted into t -wise in-
dependent p-biased random variables. Conclude that one can construct such sources
with t log2(1/p)(1 + log2 n) uniformly random bits. Then improve this bound to t (1 +
max(log2(1/p), log2 n)) uniformly random bits.

Exercise 5.9. In many applications, errors occur in “bursts"– i.e. all the error locations are con-
tained in a contiguous region (think of a scratch on a DVD or disk). In this problem we will use
how one can use Reed-Solomon codes to correct bursty errors.
An error vector e ∈ {0, 1}n is called a t -single burst error pattern if all the non-zero bits in e
occur in the range [i , i + t − 1] for some 1 ≤ i ≤ n = t + 1. Further, a vector e ∈ {0, 1}n is called a
(s, t )-burst error pattern if it is the union of at most s t -single burst error pattern (i.e. all non-
zero bits in e are contained in one of at most s contiguous ranges in [n]).
We call a binary code C ⊆ {0, 1}n to be (s, t )-burst error correcting if one can uniquely decode
from any (s, t )-burst error pattern. More precisely, given an (s, t )-burst error pattern e and any
codeword c ∈ C , the only codeword c′ ∈ C such that (c + e) − c′ is an (s, t )-burst error pattern
satisﬁes c′ = c.
 102

1. Argue that if C is (st )-error correcting (in the sense of Deﬁnition 1.3.3), then it is also (s, t )-
burst error correcting. Conclude that for any ε > 0, there exists code with rate Ω(ε2) and
block length n that is (s, t )-burst error correcting for any s, t such that s · t ≤ ( 1
4 − ε) · n.

2. Argue that for any rate R > 0 and for large enough n, there exist (s, t )-burst error correcting

as long as s·t ≤ ( 1−R−ε
2 )·n and t ≥ Ω ( log n
ε
 )
. In particular, one can correct from 1
2 −ε fraction
of burst-errors (as long as each burst is “long enough") with rate Ω(ε) (compare this with
item 1).

Hint: Use Reed-Solomon codes.

Exercise 5.10. In this problem we will look at a very important class of codes called BCH codes7.
Let F = F2m . Consider the binary code CBCH deﬁned as RSF[n, k, n − k + 1] ∩ Fn
2 .

1. Prove that CBCH is a binary linear code of distance at least d = n − k + 1 and dimension at
least n − (d − 1) log2(n + 1).

Hint: Use the characterization (5.2) of the Reed-Solomon code from Exercise 5.6.

2. Prove a better lower bound of n − ⌈ d −1
2
 ⌉ log2(n + 1) on the dimension of CBCH.

Hint: Try to ﬁnd redundant checks among the “natural” parity checks deﬁning CBCH).

3. For d = 3, CBCH is the same as another code we have seen. What is that code?

4. For constant d (and growing n), prove that CBCH have nearly optimal dimension for dis-
tance d , in that the dimension cannot be n − t log2(n + 1) for t < d −1
2 .

Exercise 5.11. Show that for 1 ≤ k ≤ n, ⌈ k
2
 ⌉ log2(n +1) random bits are enough to compute n-bits
that are k-wise independent. Note that this is an improvement of almost a factor of 2 from the
bound from Exercise 5.8 part 4 (and this new bound is known to be optimal).

Hint: Use Exercises 2.13 and 5.10.

Exercise 5.12. In this exercise, we continue in the theme of Exercise 5.10 and look at the inter-
section of a Reed-Solomon code with Fn
2 to get a binary code. Let F = F2m . Fix positive integers
d , n with (d −1)m < n < 2m, and a set S = {α1, α2, . . . , αn} of n distinct nonzero elements of F. For
a vector v = (v1, . . . , vn) ∈ (F∗)n of n not necessarily distinct nonzero elements from F, deﬁne the
Generalized Reed-Solomon code GRSS,v,d as follows:

GRSS,v,d = {(v1p(α1), v2p(α2), . . . , vn p(αn)) | p(X ) ∈ F[X ] has degree ≤ n − d } .

1. Prove that GRSS,v,d is an [n, n − d + 1, d ]F linear code.

2. Argue that GRSS,v,d ∩ Fn
2 is a binary linear code of rate at least 1 − (d −1)m
n .

7The acronym BCH stands for Bose-Chaudhuri-Hocquenghem, the discoverers of this family of codes.

103

3. Let c ∈ Fn
2 be a nonzero binary vector. Prove that (for every choice of d , S) there are at most
(2m − 1)n−d +1 choices of the vector v for which c ∈ GRSS,v,d .

4. Using the above, prove that if the integer D satisﬁes Vol2(n, D − 1) < (2m − 1)d −1 (where
Vol2(n, D − 1) = ∑D−1
i =0 (n
i )
), then there exists a vector v ∈ (F∗)n such that the minimum dis-
tance of the binary code GRSS,v,d ∩ Fn
2 is at least D.

5. Using parts 2 and 4 above (or otherwise), argue that the family of codes GRSS,v,d ∩ Fn
2
contains binary linear codes that meet the Gilbert-Varshamov bound.

Exercise 5.13. In this exercise we will show that the dual of a GRS code is a GRS itself with dif-
ferent parameters. First, we state the obvious deﬁnition of GRS codes over a general ﬁnite ﬁeld
Fq (as opposed to the deﬁnition over ﬁelds of characteristic two in Exercise 5.12). In particular,
deﬁne the code GRSS,v,d ,q as follows:

GRSS,v,d ,q = {(v1p(α1), v2p(α2), . . . , vn p(αn)) | p(X ) ∈ Fq [X ] has degree ≤ n − d } .

Then show that (
GRSS,v,d ,q )⊥ = GRSS,v′,n−d +2,q ,

where v
′ ∈ Fn
q is a vector with all non-zero components.

Exercise 5.14. In Exercise 2.16, we saw that any linear code can be converted in to a systematic
code. In other words, there is a map to convert Reed-Solomon codes into a systematic one. In
this exercise the goal is to come up with an explicit encoding function that results in a systematic
Reed-Solomon code.
In particular, given the set of evaluation points α1, . . . , αn, design an explicit map f from
Fk
q to a polynomial of degree at most k − 1 such that the following holds. For every message
m ∈ Fk
q , if the corresponding polynomial is fm(X ), then the vector ( fm(αi ))

i ∈[n] has the message
m appear in the corresponding codeword (say in its ﬁrst k positions). Further, argue that this
map results in an [n, k, n − k + 1]q code.

Exercise 5.15. In this problem, we will consider the number-theoretic counterpart of Reed-
Solomon codes. Let 1 ≤ k < n be integers and let p1 < p2 < · · · < pn be n distinct primes.
Denote K = ∏k
i =1 pi and N = ∏n
i =1 pi . The notation ZM stands for integers modulo M , i.e.,
the set {0, 1, . . . , M − 1}. Consider the Chinese Remainder code deﬁned by the encoding map
E : ZK → Zp1 × Zp2 × · · · × Zpn deﬁned by:

E (m) = (m mod p1, m mod p2, · · · , m mod pn) .

(Note that this is not a code in the usual sense we have been studying since the symbols at
different positions belong to different alphabets. Still notions such as distance of this code make
sense and are studied in the question below.)
Suppose that m1 ̸= m2. For 1 ≤ i ≤ n, deﬁne the indicator variable bi = 1 if E (m1)i ̸= E (m2)i
and bi = 0 otherwise. Prove that ∏n
i =1 p bi
i > N /K .
Use the above to deduce that when m1 ̸= m2, the encodings E (m1) and E (m2) differ in at
least n − k + 1 locations.
 104

Exercise 5.16. In this problem, we will consider derivatives over a ﬁnite ﬁeld Fq . Unlike the case
of derivatives over reals, derivatives over ﬁnite ﬁelds do not have any physical interpretation
but as we shall see shortly, the notion of derivatives over ﬁnite ﬁelds is still a useful concept. In
particular, given a polynomial f (X ) = ∑t
i =0 fi X i over Fq , we deﬁne its derivative as

f ′(X ) = t −1∑

i =0(i + 1) · fi +1 · X i .

Further, we will denote by f (i )(X ), the result of applying the derivative on f i times. In this
problem, we record some useful facts about derivatives.

1. Deﬁne R(X , Z ) = f (X + Z ) = ∑t
i =0 ri (X ) · Z i . Then for any j ≥ 1,

f ( j )(X ) = j ! · r j (X ).

2. Using part 1 or otherwise, show that for any j ≥ char(Fq ),8 f ( j )(X ) ≡ 0.

3. Let j ≤ char(Fq ). Further, assume that for every 0 ≤ i < j , f (i )(α) = 0 for some α ∈ Fq . Then
prove that (X − α) j divides f (X ).

4. Finally, we will prove the following generalization of the degree mantra (Proposition 5.2.3).
Let f (X ) be a non-zero polynomial of degree t and m ≤ char(Fq ). Then there exists at most⌊ t
m ⌋ distinct elements α ∈ Fq such that f ( j )(α) = 0 for every 0 ≤ j < m.

Exercise 5.17. In this exercise, we will consider a code that is related to Reed-Solomon codes
and uses derivatives from Exercise 5.16. These codes are called derivative codes.
Let m ≥ 1 be an integer parameter and consider parameters k > char(Fq ) and n such that
m < k < nm. Then the derivative code with parameters (n, k, m) is deﬁned as follow. Consider
any message m ∈ Fk
q and let fm(X ) be the message polynomial as deﬁned for the Reed-Solomon
code. Let α1, . . . , αn ∈ Fq be distinct elements. Then the codeword for m is given by







 fm(α1) fm(α2) · · · fm(αn)
f (1)
m (α1) f (1)
m (α2) · · · f (1)
m (αn)
... ... ... ...
f (m−1)
m (α1) f (m−1)
m (α2) · · · f (m−1)
m (αn)
 





 .

Prove that the above code is an [
n, k
m , n − ⌊ k−1
m
 ⌋]
q m -code (and is thus MDS).

Exercise 5.18. In this exercise, we will consider another code related to Reed-Solomon codes
that are called Folded Reed-Solomon codes. We will see a lot more of these codes in Chapter 16.
Let m ≥ 1 be an integer parameter and let α1, . . . , αn ∈ Fq are distinct elements such that for
some element γ ∈ F∗
q , the sets {αi , αi γ, αi γ
2, . . . , αi γ
m−1}, (5.3)

8char(Fq ) denotes the characteristic of Fq . That is, if q = p s for some prime p, then char(Fq ) = p. Any natural
number i in Fq is equivalent to i mod char(Fq ).
 105

are pair-wise disjoint for different i ∈ [n]. Then the folded Reed-Solomon code with parameters
(m, k, n, γ, α1, . . . , αn) is deﬁned as follows. Consider any message m ∈ Fk
q and let fm(X ) be the
message polynomial as deﬁned for the Reed-Solomon code. Then the codeword for m is given
by: 





 fm(α1) fm(α2) · · · fm(αn)
fm(α1 · γ) fm(α2 · γ) · · · fm(αn · γ)
... ... ... ...
fm(α1 · γ
m−1) fm(α2 · γ
m−1) · · · fm(αn · γ
m−1)
 




 .

Prove that the above code is an [
n, k
m , n − ⌊ k−1
m
 ⌋]
q m -code (and is thus, MDS).

Exercise 5.19. In this problem we will see that Reed-Solomon codes, derivative codes (Exer-
cise 5.17) and folded Reed-Solomon codes (Exercise 5.18) are all essentially special cases of
a large family of codes that are based on polynomials. We begin with the deﬁnition of these
codes.
Let m ≥ 1 be an integer parameter and deﬁne m < k ≤ n. Further, let E1(X ), . . . , En(X ) be
n polynomials over Fq , each of degree m. Further, these polynomials pair-wise do not have
any non-trivial factors (i.e. gcd(Ei (X ), E j (X )) has degree 0 for every i ̸= j ∈ [n].) Consider any
message m ∈ Fk
q and let fm(X ) be the message polynomial as deﬁned for the Reed-Solomon
code. Then the codeword for m is given by:

( fm(X ) mod E1(X ), fm(X ) mod E2(X ), . . . , fm(X ) mod En(X )) .

In the above we think of fm(X ) mod Ei (X ) as an element of Fq m . In particular, given given a
polynomial of degree at most m − 1, we will consider any bijection between the q m such poly-
nomials and Fq m . We will ﬁrst see that this code is MDS and then we will see why it contains
Reed-Solomon and related codes as special cases.

1. Prove that the above code is an [
n, k
m , n − ⌊ k−1
m
 ⌋]
q m -code (and is thus, MDS).

2. Let α1, . . . , αn ∈ Fq be distinct elements. Deﬁne Ei (X ) = X − αi . Argue that for this special
case the above code (with m = 1) is the Reed-Solomon code.

3. Let α1, . . . , αn ∈ Fq be distinct elements. Deﬁne Ei (X ) = (X − αi )m. Argue that for this
special case the above code is the derivative code (with an appropriate mapping from
polynomials of degree at most m − 1 and Fm
q , where the mapping could be different for
each i ∈ [n] and can depend on Ei (X )).

4. Let α1, . . . , αn ∈ Fq be distinct elements and γ ∈ F∗
q such that (5.3) is satisﬁed. Deﬁne
Ei (X ) = ∏m−1
j =0 (X − αi · γ j ). Argue that for this special case the above code is the folded
Reed-Solomon code (with an appropriate mapping from polynomials of degree at most
m − 1 and Fm
q , where the mapping could be different for each i ∈ [n] and can depend on
Ei (X )).
 106

Exercise 5.20. In this exercise we will develop a sufﬁcient condition to determine the irreducibil-
ity of certain polynomials called the Eisenstein’s criterion.
Let F (X , Y ) be a polynomial of Fq . Think of this polynomial as over X with coefﬁcients as
polynomials in Y over Fq . Technically, we think of the coefﬁcients as coming from the ring of
polynomials in Y over Fq . We will denote the ring of polynomials in Y over Fq as Fq (Y ) and we
will denote the polynomials in X with coefﬁcients from Fq (Y ) as Fq (Y )[X ].
In particular, let F (X , Y ) = X t + ft −1(Y ) · X t −1 + · · · + f0(Y ),

where each fi (Y ) ∈ Fq (Y ). Let P (Y ) be a prime for Fq (Y ) (i.e. P (Y ) has degree at least one and
if P (Y ) divides A(Y ) · B (Y ) then P (Y ) divides at least one of A(Y ) or B (Y )). If the following
conditions hold:

(i) P (Y ) divides fi (Y ) for every 0 ≤ i < t ; but

(ii) P 2(Y ) does not divide f0(Y )

then F (X , Y ) does not have any non-trivial factors over Fq (Y )[X ] (i.e. all factors have either
degree t or 0 in X ).
In the rest of the problem, we will prove this result in a sequence of steps:

1. For the sake of contradiction assume that F (X , Y ) = G(X , Y ) · H (X , Y ) where

G(X , Y ) =
 t1∑

i =0 gi (Y ) · X I and H (X , Y ) =
 t2∑

i =0 hi (Y ) · X i ,

where 0 < t1, t2 < t . Then argue that P (Y ) does not divide both of g0(Y ) and h0(Y ).

For the rest of the problem WLOG assume that P (Y ) divides g0(Y ) (and hence does not
divide h0(Y )).

2. Argue that there exists an i ∗ such that P (Y ) divide gi (Y ) for every 0 ≤ i < i ∗ but P (Y ) does
not divide gi ∗(Y ) (deﬁne g t (Y ) = 1).

3. Argue that P (Y ) does not divide fi (Y ). Conclude that F (X , Y ) does not have any non-
trivial factors, as desired.

Exercise 5.21. We have mentioned objects called algebraic-geometric (AG) codes, that general-
ize Reed-Solomon codes and have some amazing properties: see for example, Section 4.6. The
objective of this exercise is to construct one such AG code, and establish its rate vs distance
trade-off.
Let p be a prime and q = p 2. Consider the equation

Y p + Y = X p+1 (5.4)

over Fq .
 107

1. Prove that there are exactly p 3 solutions in Fq × Fq to (5.4). That is, if S ⊆ F2
q is deﬁned as

S = {
(α, β) ∈ F2
q | βp + β = αp+1}

then |S| = p 3.

2. Prove that the polynomial F (X , Y ) = Y p + Y − X p+1 is irreducible over Fq .

Hint: Exercise 5.20 could be useful.

3. Let n = p 3. Consider the evaluation map ev : Fq [X , Y ] → Fn
q deﬁned by

ev( f ) = ( f (α, β) : (α, β) ∈ S) .

Argue that if f ̸= 0 and is not divisible by Y p + Y − X p+1, then ev( f ) has Hamming weight
at least n − deg( f )(p + 1), where deg( f ) denotes the total degree of f .

Hint: You are allowed to make use of Bézout’s theorem, which states that if f , g ∈ Fq [X , Y ] are nonzero

polynomials with no common factors, then they have at most deg( f )deg(g ) common zeroes.

4. For an integer parameter ℓ ≥ 1, consider the set Fℓ of bivariate polynomials

Fℓ = { f ∈ Fq [X , Y ] | deg( f ) ≤ ℓ, degX ( f ) ≤ p}

where degX ( f ) denotes the degree of f in X .

Argue that Fℓ is an Fq -linear space of dimension (ℓ + 1)(p + 1) − p(p+1)
2 .

5. Consider the code C ⊆ Fn
q for n = p 3 deﬁned by

C = {
ev( f ) | f ∈ Fℓ} .

Prove that C is a linear code with minimum distance at least n − ℓ(p + 1).

6. Deduce a construction of an [n, k]q code with distance d ≥ n − k + 1 − p(p − 1)/2.

(Note that Reed-Solomon codes have d = n − k + 1, whereas these codes are off by p(p −
1)/2 from the Singleton bound. However they are much longer than Reed-Solomon codes,
with a block length of n = q 3/2, and the deﬁciency from the Singleton bound is only o(n).)

5.5 Bibliographic Notes

Reed-Solomon codes were invented by Irving Reed and Gus Solomon [84]. Even though Reed-
Solomon codes need q ≥ n, they are used widely in practice. For example, Reed-Solomon codes
are used in storage of information in CDs and DVDs. This is because they are robust against
burst-errors that come in contiguous manner. In this scenario, a large alphabet is then a good
thing since bursty errors will tend to corrupt the entire symbol in Fq unlike partial errors, e.g.
errors over bits. (See Exercise 5.9.)
It is a big open question to present a deterministic algorithm to compute an irreducible
polynomial of a given degree with the same time complexity as in Corollary 5.1.3. Such results
are known in general if one is happy with polynomial dependence on q instead of log q. See the
book by Shoup [91] for more details.
 108

Chapter 6

What Happens When the Noise is Stochastic:
Shannon’s Theorem

Shannon was the ﬁrst to present a rigorous mathematical framework for communication, which
(as we have already seen) is the problem of reproducing at one point (typically called the “re-
ceiver" of the channel) a message selected at another point (called the “sender" to the channel).
Unlike Hamming, Shannon modeled the noise stochastically, i.e. as a well deﬁned random pro-
cess. He proved a result that pin-pointed the best possible rate of transmission of information
over a very wide range of stochastic channels. In fact, Shannon looked at the communication
problem at a higher level, where he allowed for compressing the data ﬁrst (before applying any
error-correcting code), so as to minimize the amount of symbols transmitted over the channel.
In this chapter, we will study some stochastic noise models most of which were proposed
by Shannon. We then prove an optimal tradeoff between the rate and fraction of errors that are
correctable for a speciﬁc stochastic noise model called the Binary Symmetric Channel.

6.1 Overview of Shannon’s Result

Shannon introduced the notion of reliable communication
1 over noisy channels. Broadly, there
are two types of channels that were studied by Shannon:

• (Noisy Channel) This type of channel introduces errors during transmission, which result
in an incorrect reception of the transmitted signal by the receiver. Redundancy is added
at the transmitter to increase reliability of the transmitted data. The redundancy is taken
off at the receiver. This process is termed as Channel Coding.

• (Noise-free Channel) As the name suggests, this channel does not introduce any type of
error in transmission. Redundancy in source data is used to compress the source data at
the transmitter. The data is decompressed at the receiver. The process is popularly known
as Source Coding.

1That is, the ability to successfully send the required information over a channel that can lose or corrupt data.

109

Figure 6.1 presents a generic model of a communication system, which combines the two con-
cepts we discussed above.

(Decoded) Message

Message Encoder
Source
 Encoder

ChannelChannel
Decoder

Source
 Decoder
Channel

Figure 6.1: The communication process

In Figure 6.1, source coding and channel coding are coupled. In general, to get the optimal
performance, it makes sense to design both the source and channel coding schemes simultane-
ously. However, Shannon’s source coding theorem allows us to decouple both these parts of the
communication setup and study each of these parts separately. Intuitively, this makes sense:
if one can have reliable communication over the channel using channel coding, then for the
source coding the resulting channel effectively has no noise.
For source coding, Shannon proved a theorem that precisely identiﬁes the amount by which
the message can be compressed: this amount is related to the entropy of the message. We will
not talk much more about source coding in in this book. (However, see Exercises 6.10, 6.11
and 6.12.) From now on, we will exclusively focus on the channel coding part of the commu-
nication setup. Note that one aspect of channel coding is how we model the channel noise. So
far we have seen Hamming’s worst case noise model in some detail. Next, we will study some
speciﬁc stochastic channels.

6.2 Shannon’s Noise Model

Shannon proposed a stochastic way of modeling noise. The input symbols to the channel are
assumed to belong to some input alphabet X , while the channel outputs symbols from its out-
put alphabet Y . The following diagram shows this relationship:

X ∋ x → channel → y ∈ Y

The channels considered by Shannon are also memoryless, that is, noise acts independently
on each transmitted symbol. In this book, we will only study discrete channels where both the
alphabets X and Y are ﬁnite. For the sake of variety, we will deﬁne one channel that is contin-
uous, though we will not study it in any detail later on.

110

The ﬁnal piece in speciﬁcation of a channel is the transition matrix M that governs the pro-
cess of how the channel introduces error. In particular, the channel is described in the form of
a matrix with entries as the crossover probability over all combination of the input and output
alphabets. For any pair (x, y) ∈ X × Y , let Pr(y|x) denote the probability that y is output by the
channel when x is input to the channel. Then the transition matrix is given by M(x, y) = Pr(y|x).
The speciﬁc structure of the matrix is shown below.

M =
 




 ...
· · · Pr(y|x) · · ·
...
 





Next, we look at some speciﬁc instances of channels.

Binary Symmetric Channel (BSC). Let 0 ≤ p ≤ 1. The Binary Symmetric Channel with crossover
probability p or BSCp is deﬁned as follows. X = Y = {0, 1}. The 2 × 2 transition matrix can nat-
urally be represented as a bipartite graph where the left vertices correspond to the rows and
the right vertices correspond to the columns of the matrix, where M(x, y) is represented as the
weight of the corresponding (x, y) edge. For BSCp , the graph is illustrated in Figure 6.2.

0 0

1 1

1 − p

p

1 − p

p

Figure 6.2: Binary Symmetric Channel BSCp

The corresponding transition matrix would look like this:

( 0 1
0 1 − p p
1 p 1 − p
 ).

In other words, every bit is ﬂipped with probability p. We claim that we need to only con-
sider the case when p ≤ 1
2 , i.e. if we know how to ensure reliable communication over BSCp for
p ≤ 1
2 , then we can also handle the case of p > 1
2 . (See Exercise 6.1.)

q-ary Symmetric Channel (qSC). We now look at the generalization of BSCp to alphabets of
size q ≥ 2. Let 0 ≤ p ≤ 1 − 1
q . (As with the case of BSCp , we can assume that p ≤ 1 − 1
q – see
Exercise 6.2.) The q-ary Symmetric Channel with crossover probability p, or qSCp , is deﬁned
as follows. X = Y = [q]. The transition matrix M for qSCp is deﬁned as follows.

M (x, y) = { 1 − p if y = x
p
q−1 if y ̸= x

In other words, every symbol is retained as is at the output with probability 1−p and is distorted
to each of the q − 1 possible different symbols with equal probability of p
q−1 .

111

Binary Erasure Channel (BEC) In the previous two examples that we saw, X = Y . However,
this might not always be the case.
Let 0 ≤ α ≤ 1. The Binary Erasure Channel with erasure probability α (denoted by BECα) is
deﬁned as follows. X = {0, 1} and Y = {0, 1, ?}, where ? denotes an erasure. The transition matrix
is as follows:
 0 0

?

1 1

1 − α

α

α

1 − α

Figure 6.3: Binary Erasure Channel BECα

In Figure 6.3 any missing edge represents a transition that occurs with 0 probability. In other
words, every bit in BECα is erased with probability α (and is left unchanged with probability
1 − α).

Binary Input Additive Gaussian White Noise Channel (BIAGWN). We now look at a channel
that is continuous. Let σ ≥ 0. The Binary Input Additive Gaussian White Noise Channel with
standard deviation σ or BIAGWNσ is deﬁned as follows. X = {−1, 1} and Y = R. The noise is
modeled by the continuous Gaussian probability distribution function. The Gaussian distribu-
tion has lots of nice properties and is a popular choice for modeling noise continuous in nature.
Given (x, y) ∈ {−1, 1} × R, the noise y − x is distributed according to the Gaussian distribution of
mean of zero and standard deviation of σ. In other words,

Pr (y | x) = 1

σ
p
2π · exp (
− ( (y − x)2

2σ2
 ))

6.2.1 Error Correction in Stochastic Noise Models

We now need to revisit the notion of error correction from Section 1.3. Note that unlike Ham-
ming’s noise model, we cannot hope to always recover the transmitted codeword. As an ex-
ample, in BSCp there is always some positive probability that a codeword can be distorted into
another codeword during transmission. In such a scenario no decoding algorithm can hope
to recover the transmitted codeword. Thus, in some stochastic channels there is always some
decoding error probability (where the randomness is from the channel noise): see Exercise 6.14
for example channels where one can have zero decoding error probability. However, we would
like this error probability to be small for every possible transmitted codeword. More precisely,
for every message, we would like the decoding algorithm to recover the transmitted message
with probability 1 − f (n), where limn→∞ f (n) → 0; that is, f (n) is o(1). Ideally, we would like to
have f (n) = 2−Ω(n). We will refer to f (n) as the decoding error probability.

112

6.2.2 Shannon’s General Theorem

Recall that the big question of interest in this book is the tradeoff between the rate of the code
and the fraction of errors that can be corrected. For stochastic noise models that we have seen,
it is natural to think of the fraction of errors to be the parameter that governs the amount of
error that is introduced by the channel. For example, for BSCp , we will think of p as the fraction
of errors.
Shannon’s remarkable theorem on channel coding was to precisely identify when reliable
transmission is possible over the stochastic noise models that he considered. In particular, for
the general framework of noise models, Shannon deﬁned the notion of capacity, which is a
real number such that reliable communication is possible if and only if the rate is less than the
capacity of the channel. In other words, given a noisy channel with capacity C , if information is
transmitted at rate R for any R < C , then there exists a coding scheme that guarantees negligible
probability of miscommunication. On the other hand if R > C , then regardless of the chosen
coding scheme there will be some message for which the decoding error probability is bounded
from below by some constant.
In this chapter, we are going to state (and prove) Shannon’s general result for the special case
of BSCp .

6.3 Shannon’s Result for BSCp

We begin with a notation. For the rest of the chapter, we will use the notation e ∼ BSCp to
denote an error pattern e that is drawn according to the error distribution induced by BSCp . We
are now ready to state the theorem.

Theorem 6.3.1 (Shannon’s Capacity Theorem for BSC). For real numbers p, ε such that 0 ≤ p < 1
2
and 0 ≤ ε ≤ 1
2 − p, the following statements are true for large enough n:

1. There exists a real δ > 0, an encoding function E : {0, 1}k → {0, 1}n and a decoding function
D : {0, 1}n → {0, 1}k where k ≤ ⌊(1 − H (p + ε)) n⌋, such that the following holds for every
m ∈ {0, 1}k : Pr
e∼BSCp [D(E (m) + e)) ̸= m] ≤ 2−δn.

2. If k ≥ ⌈(1 − H (p) + ε)n⌉ then for every pair of encoding and decoding functions, E : {0, 1}k →
{0, 1}n and D : {0, 1}n → {0, 1}k , there exists m ∈ {0, 1}k such that

Pr
e∼BSCp [D(E (m) + e)) ̸= m] ≥ 1
2 .

Note that Theorem 6.3.1 implies that the capacity of BSCp is 1 − H (p). It can also be shown
that the capacity of qSCp and BECα are 1 − Hq (p) and 1 − α respectively. (See Exercises 6.6
and 6.7.)
The entropy function appears in Theorem 6.3.1 due to the same technical reason that it
appears in the GV bound: the entropy function allows us to use sufﬁciently tight bounds on the
volume of a Hamming ball (Proposition 3.3.1).

113

6.3.1 Proof of Converse of Shannon’s Capacity Theorem for BSC

We start with the proof of part (2) of Theorem 6.3.1. (Proof of part (1) follows in the next section.)
For the proof we will assume that p > 0 (since when p = 0, 1 − H (p) + ε > 1 and so we have
nothing to prove). For the sake of contradiction, assume that the following holds for every m ∈
{0, 1}k :
 Pr
e∼BSCp [D(E (m) + e) ̸= m] ≤ 1
2 .

Deﬁne Dm to be the set of received words y that are decoded to m by D, that is,

Dm = {y|D(y) = m} .

The main idea behind the proof is the following: ﬁrst note that the sets Dm partition the
entire space of received words {0, 1}n (see Figure 6.4 for an illustration) since D is a function.

Dm
 {0, 1}n

Figure 6.4: The sets Dm partition the ambient space {0, 1}n.

Next we will argue that since the decoding error probability is at most a 1/2, then Dm for
every m ∈ {0, 1}k is “large." Then by a simple packing argument, it follows that we cannot have
too many distinct m, which we will show implies that k < (1−H (p)+ε)n: a contradiction. Before
we present the details, we outline how we will argue that Dm is large. Let Sm be the shell of radius
[(1 − γ)pn, (1 + γ)pn] around E (m), that is,

Sm = B (
E (m), (1 + γ)pn) \ B (
E (m), (1 − γ)pn) .

We will set γ > 0 in terms of ε and p at the end of the proof. (See Figure 6.5 for an illustra-
tion.) Then we argue that because the decoding error probability is bounded by 1/2, most of
the received words in the shell Sm are decoded correctly, i.e. they fall in Dm. To complete the
argument, we show that number of such received words is indeed large enough.
Fix an arbitrary message m ∈ {0, 1}k . Note that by our assumption, the following is true
(where from now on we omit the explicit dependence of the probability on the BSCp noise for
clarity):
 Pr [E (m) + e ̸∈ Dm] ≤ 1
2 . (6.1)

114

(1 + γ)pn

(1 − γ)pn

E (m)

Figure 6.5: The shell Sm of inner radius (1 − γ)pn and outer radius (1 + γ)pn.

Further, by the (multiplicative) Chernoff bound (Theorem 3.1.6),

Pr [E (m) + e ̸∈ Sm] ≤ 2−Ω(γ
2n). (6.2)

(6.1) and (6.2) along with the union bound (Proposition 3.1.3) imply the following:

Pr [E (m) + e ̸∈ Dm ∩ Sm] ≤ 1
2 + 2−Ω(γ
2n).

The above in turn implies that

Pr [E (m) + e ∈ Dm ∩ Sm] ≥ 1
2 − 2−Ω(γ
2n) ≥ 1
4 , (6.3)

where the last inequality holds for large enough n. Next we upper bound the probability above
to obtain a lower bound on |Dm ∩ Sm|.
It is easy to see that
 Pr [E (m) + e ∈ Dm ∩ Sm] ≤ |Dm ∩ Sm| · pmax,

where pmax = max
y∈Sm Pr [E (m) + e = y
] = max
d ∈[(1−γ)pn,(1+γ)pn] p d (1 − p)n−d .

In the above, the second equality follows from the fact that all error patterns with the same
Hamming weight appear with the same probability when chosen according to BSCp . Next, note
that p d (1 − p)n−d is decreasing in d for p ≤ 1
2 .2 Thus, we have

pmax = p (1−γ)pn(1 − p)n−(1−γ)pn = ( 1 − p
p
 )γpn · p pn(1 − p)(1−p)n = ( 1 − p
p
 )γpn 2−nH (p).

2Indeed pd (1 − p)
n−d = (p/(1 − p))
d (1 − p)
n and the bound p ≤ 1
2 implies that the ﬁrst exponent is at most 1,
which implies that the expression is decreasing in d .
 115

Thus, we have shown that

Pr [E (m) + e ∈ Dm ∩ Sm] ≤ |Dm ∩ Sm| · ( 1 − p
p
 )γpn 2−nH (p),

which, by (6.3), implies that
 |Dm ∩ S| ≥ 1
4 · ( 1 − p
p
 )−γpn 2nH (p). (6.4)

Next, we consider the following sequence of relations:

2n = ∑

m∈{0,1}k |Dm| (6.5)

≥ ∑

m∈{0,1}k |Dm ∩ Sm|

≥ 1
4
 ( 1
p − 1)−γpn ∑

m∈{0,1}k 2H (p)n (6.6)

= 2k−2 · 2H (p)n−γp log(1/p−1)n

> 2k+H (p)n−εn. (6.7)

In the above, (6.5) follows from the fact that for m1 ̸= m2, Dm1 and Dm2 are disjoint. (6.6) follows
from (6.4). (6.7) follows for large enough n and if we pick γ = ε
2p log
( 1
p −1) . (Note that as 0 < p < 1
2 ,

γ = Θ(ε).)
(6.7) implies that k < (1 − H (p) + ε)n, which is a contradiction. The proof of part (2) of The-
orem 6.3.1 is complete.

Remark 6.3.1. It can be veriﬁed that the proof above can also work if the decoding error prob-
ability is bounded by 1 − 2−βn (instead of the 1/2 in part (2) of Theorem 6.3.1) for small enough
β = β(ε) > 0.

Next, we will prove part (1) of Theorem 6.3.1.

6.3.2 Proof of Positive Part of Shannon’s Theorem

Proof Overview. The proof of part (1) of Theorem 6.3.1 will be done by the probabilistic
method (Section 3.2). In particular, we randomly select an encoding function E : {0, 1}k →
{0, 1}n. That is, for every m ∈ {0, 1}k pick E (m) uniformly and independently at random from
{0, 1}n. D will be the maximum likelihood decoding (MLD) function. The proof will have the
following two steps:

• (Step 1) For any arbitrary m ∈ {0, 1}k , we will show that for a random choice of E, the prob-
ability of failure, over BSCp noise, is small. This implies the existence of a good encoding
function for any arbitrary message.
 116

• (Step 2) We will show a similar result for all m. This involves dropping half of the code
words.

Note that there are two sources of randomness in the proof:

1. Randomness in the choice of encoding function E and

2. Randomness in the noise.

We stress that the ﬁrst kind of randomness is for the probabilistic method while the second
kind of randomness will contribute to the decoding error probability.

“Proof by picture" of Step 1. Before proving part (1) of Theorem 6.3.1, we will provide a pic-
torial proof of Step 1. We begin by ﬁxing m ∈ {0, 1}k . In Step 1, we need to estimate the following
quantity:
 EE
 [ Pr
e∼BSCp [D (E (m) + e) ̸= m]
] .

By the additive Chernoff bound (Theorem 3.1.6), with all but an exponentially small proba-
bility, the received word will be contained in a Hamming ball of radius (p + ε′) n (for some ε′ > 0
that we will choose appropriately). So one can assume that the received word y with high prob-
ability satisﬁes ∆(E (m), y) ≤ (p +ε′)n. Given this, pretty much the only thing to do is to estimate
the decoding error probability for such a y. Note that by the fact that D is MLD, an error can
happen only if there exists another message m′ such that ∆(E (m′), y) ≤ ∆(E (m), y). The latter
event implies that ∆(E (m′), y) ≤ (p + ε′)n (see Figure 6.6).

y
 (p + ε′)n

(p + ε′)n
 E (m)E (m′)

Figure 6.6: Hamming balls of radius (p + ε′) n and centers E (m) and y) illustrates Step 1 in the
proof of part (1) of Shannon’s capacity theorem for the BSC.

Thus, the decoding error probability is upper bounded by

Pr
e∼BSCp
 [
E (m′) ∈ B (
y, (p + ε′) n)] = V ol2 ((p + ε′) n, n)

2n ≈ 2H(p)n

2n ,

117

where the last step follows from Proposition 3.3.1. Finally, by the union bound (Proposition 3.1.3),
the existence of such a “bad" m′ is upper bounded by ≈ 2k 2nH (p)
2n , which by our choice of k is
2−Ω(n), as desired.

The Details. For notational convenience, we will use y and E (m) + e interchangeably:

y = E (m) + e.

That is, y is the received word when E (m) is transmitted and e is the error pattern.
We start the proof by restating the decoding error probability in part (1) of Shannon’s capac-
ity theorem for BSCp (Theorem 6.3.1) by breaking up the quantity into two sums:

Pr
e∼BSCp [D (E (m) + e) ̸= m] = ∑

y∈B (E (m),(p+ε′)n) Pr [
y|E (m)] · 1D(y)̸=m

+ ∑

y̸∈B (E (m),(p+ε′)n) Pr [
y|E (m)] · 1D(y)̸=m,

where 1D(y)̸=m is the indicator function for the event that D(y) ̸= m given that E (m) was the
transmitted codeword and we use y|E (m) as a shorthand for “y is the received word given that
E (m) was the transmitted codeword." As 1D(y)̸=m ≤ 1 (since it takes a value in {0, 1}) and by the
(additive) Chernoff bound (Theorem 3.1.6) we have

Pr
e∼BSCp [D (E (m) + e) ̸= m] ≤ ∑

y∈B (E (m),(p+ε′)n) Pr [
y|E (m)] · 1D(y)̸=m + e−(ε′)2n/2.

In order to apply the probabilistic method (Section 3.2), we will analyze the expectation
(over the random choice of E ) of the decoding error probability, which by the upper bound
above satisﬁes

EE
 [ Pr
e∼BSCp [D (E (m) + e) ̸= m]
] ≤ e−(ε′)2n/2+ ∑

y∈B(E (m),(p+ε′)n) Pr
e∼BSCp
 [
y|E (m)]·EE [
1D(y)̸=m] . (6.8)

In the above, we used linearity of expectation (Proposition 3.1.2) and the fact that the distribu-
tions on e and E are independent.
Next, for a ﬁxed received word y and the transmitted codeword E (m) such that ∆(y, E (m)) ≤
(p + ε′)n we estimate EE [
1D(y)̸=m]
. Since D is MLD, we have

EE [1D(y)̸=m] = Pr
E
 [
1D(y)̸=m|E (m)] ≤ ∑

m′̸=m Pr [
∆ (E (
m′) , y
) ≤ ∆ (E (m) , y
) |E (m)] , (6.9)

where in the above “|E (m)" is short for “being conditioned on E (m) being transmitted" and the
inequality follows from the union bound (Proposition 3.1.3) and the fact that D is MLD.

118

Noting that ∆(E (m′), y) ≤ ∆(E (m), y) ≤ (p + ε′)n (see Figure 6.6), by (6.9) we have

EE [
1D(y)̸=m] ≤ ∑

m′̸=m Pr [E (
m′) ∈ B (
y, (p + ε′) n) |E (m)]

= ∑

m′̸=m
 ∣B (
y, (p + ε′) n)∣

2n (6.10)

≤ ∑

m′̸=m
 2H(p+ε′)n

2n (6.11)

<2k · 2−n(1−H(p+ε′))

≤2n(1−H(p+ε))−n(1−H(p+ε′)) (6.12)

=2−n(H(p+ε)−H(p+ε′)). (6.13)

In the above, (6.10) follows from the fact that the choice for E (m′) is independent of E (m).
(6.11) follows from the upper bound on the volume of a Hamming ball (Proposition 3.3.1), while
(6.12) follows from our choice of k.
Using (6.13) in (6.8), we get

EE
 [ Pr
e∼BSCp [D(E (m) + e) ̸= m]] ≤e−(ε′)2n/2 + 2−n(H(p+ε)−H(p+ε′)) ∑

y∈B (E (m),(p+ε′)n) Pr [y|E (m)]

≤e−(ε′)2n/2 + 2−n(H(p+ε)−H(p+ε′)) ≤ 2−δ′n, (6.14)

where the second inequality follows from the fact that
∑

y∈B (E (m),(p+ε′)n) Pr [
y|E (m)] ≤ ∑

y∈{0,1}n Pr [
y|E (m)] = 1

and the last inequality follows for large enough n, say ε′ = ε/2 and by picking δ
′ > 0 to be small
enough. (See Exercise 6.3.)
Thus, we have shown that for any arbitrary m the average (over the choices of E ) decoding
error probability is small. However, we still need to show that the decoding error probability is
exponentially small for all messages simultaneously. Towards this end, as the bound holds for
each m, we have
 Em
 [
EE
 [ Pr
e∼BSCp [D (E (m) + e) ̸= m]
]] ≤ 2−δ′n.

The order of the summation in the expectation with respect to m and the summation in the
expectation with respect to the choice of E can be switched (as the probability distributions are
deﬁned over different domains), resulting in the following expression:

EE
 [
Em
 [ Pr
e∼BSCp [D (E (m) + e) ̸= m]
]] ≤ 2−δ′n.

By the probabilistic method, there exists an encoding function E ∗ (and a corresponding
decoding function D ∗) such that
 119

Em
 [ Pr
e∼BSCp
 [
D ∗ (
E ∗ (m) + e
) ̸= m]
] ≤ 2−δ′n. (6.15)

(6.15) implies that the average decoding error probability is exponentially small. However,
recall we need to show that the maximum decoding error probability is small. To achieve such
a result, we will throw away half of the messages, i.e. expurgate the code. In particular, we will
order the messages in decreasing order of their decoding error probability and then drop the
top half. We claim that the maximum decoding error probability for the remaining messages is
2 · 2−δ′n. Next, we present the details.

From Average to Worst-Case Decoding Error Probability. We begin with the following “aver-
aging" argument.

Claim 6.3.2. Let the messages be ordered as m1, m2, . . . , m2k and deﬁne

Pi = Pr
e∼BSCp [D(E (mi ) + e) ̸= mi ] .

Assume that P1 ≤ P2 ≤ . . . ≤ P2k and (6.15) holds, then P2k−1 ≤ 2 · 2−δ′n

Proof. By the deﬁnition of Pi ,

1

2k
 2k∑

i =1 Pi = Em Pr
e∼BSCp [D(E (m) + e) ̸= m]

≤ 2−δ′n, (6.16)

where (6.16) follows from (6.15). For the sake of contradiction assume that

P2k−1 > 2 · 2−δ′n. (6.17)

So,
 1

2k
 2k∑

i =1 Pi ≥ 1

2k
 2k∑

i =2k−1+1 Pi (6.18)

> 2 · 2−δ′n · 2k−1

2k (6.19)

> 2−δ′n, (6.20)

where (6.18) follows by dropping half the summands from the sum. (6.19) follows from (6.17)
and the assumption on the sortedness of Pi . The proof is now complete by noting that (6.20)
contradicts (6.16).
 120

Thus, our ﬁnal code will have m1, . . . , m2k−1 as its messages and hence, has dimension k ′ =
k − 1. Deﬁne δ = δ
′ + 1
n . In the new code, maximum error probability is at most 2−δn. Also if we
picked k ≤ ⌊(
1 − H (p + ε)) n⌋ + 1, then k ′ ≤ ⌊(
1 − H (p + ε)) n⌋, as required. This completes the
proof of Theorem 6.3.1.
We have shown that a random code can achieve capacity. However, we do not know of even
a succinct representation of general codes. A natural question to ask is if random linear codes
can achieve the capacity of BSCp . The answer is yes: see Exercise 6.4.
For linear code, representation and encoding are efﬁcient. But the proof does not give an
explicit construction. Intuitively, it is clear that since Shannon’s proof uses a random code it
does not present an ‘explicit’ construction. Below, we formally deﬁne what we mean by an
explicit construction.

Deﬁnition 6.3.1. A code C of block length n is called explicit if there exists a poly(n)-time al-
gorithm that computes a succinct description of C given n. For linear codes, such a succinct
description could be a generator matrix or a parity check matrix.

We will also need the following stronger notion of an explicitness:

Deﬁnition 6.3.2. A linear [n, k] code C is called strongly explicit, if given any index pair (i , j ) ∈
[k] × [n], there is a poly(log n) time algorithm that outputs Gi , j , where G is a generator matrix of
C .
 Further, Shannon’s proof uses MLD for which only exponential time implementations are
known. Thus, the biggest question left unsolved by Shannon’s work is the following.

Question 6.3.1. Can we come up with an explicit construction of a code of rate 1 − H (p + ε)
with efﬁcient decoding and encoding algorithms that achieves reliable communication over
BSCp ?

As a baby step towards the resolution of the above question, one can ask the following ques-
tion:

Question 6.3.2. Can we come up with an explicit construction with R > 0 and p > 0?

Note that the question above is similar to Question 2.7.1 in Hamming’s world. See Exercise 6.13
for an afﬁrmative answer.

6.4 Hamming vs. Shannon

As a brief interlude, let us compare the salient features of the works of Hamming and Shannon
that we have seen so far:
 121

HAMMING SHANNON
Focus on codewords itself Directly deals with encoding and decoding functions
Looked at explicit codes Not explicit at all
Fundamental trade off: rate vs. distance Fundamental trade off: rate vs. error
(easier to get a handle on this)
Worst case errors Stochastic errors

Intuitively achieving positive results in the Hamming world is harder than achieving positive
results in Shannon’s world. The reason is that the adversary in Shannon’s world (e.g. BSCp ) is
much weaker than the worst-case adversary in Hamming’s world (say for bits). We make this
intuition (somewhat) precise as follows:

Proposition 6.4.1. Let 0 ≤ p < 1
2 and 0 < ε ≤ 1
2 − p. If an algorithm A can handle p + ε fraction of
worst case errors, then it can be used for reliable communication over BSCp

Proof. By the additive Chernoff bound (Theorem 3.1.6), with probability ≥ 1−e −ε2n
2 , the fraction
of errors in BSCp is ≤ p + ε. Then by assumption on A, it can be used to recover the transmitted
message.

Note that the above result implies that one can have reliable transmission over BSCp with
any code of relative distance 2p + ε (for any ε > 0).
A much weaker converse of Proposition 6.4.1 is also true. More precisely, if the decoding
error probability is exponentially small for the BSC, then the corresponding code must have
constant relative distance (though this distance does not come even close to achieving say the
Gilbert-Varshamov bound). For more see Exercise 6.5.

6.5 Exercises

Exercise 6.1. Let (E , D) be a pair of encoder and decoder that allows for successful transmission
over BSCp for every p ≤ 1
2 . Then there exists a pair (E ′, D ′) that allows for successful transmission
over BSCp′ for any p ′ > 1/2. If D is (deterministic) polynomial time algorithm, then D ′ also has
to be a (deterministic) polynomial time algorithm.

Exercise 6.2. Let (E , D) be a pair of encoder and decoder that allows for successful transmission
over qSCp for every p ≤ 1 − 1
q . Then there exists a pair (E ′, D ′) that allows for successful trans-

mission over qSCp′ for any p ′ > 1 − 1
2 . If D is polynomial time algorithm, then D ′ also has to be
a polynomial time algorithm though D ′ can be a randomized algorithm even if D is determin-
istic.3

Exercise 6.3. Argue that in the positive part of Theorem 6.3.1, one can pick δ = Θ(ε2). That is,
for 0 ≤ p < 1/2 and small enough ε, there exist codes of rate 1 − H (p) − ε and block length n that
can be decoded with error probability at most 2−Θ(ε2)n over BSCp .

3A randomized D ′ means that given a received word y the algorithm can use random coins and the decoding
error probability is over both the randomness from its internal coin tosses as well as the randomness from the
channel.
 122

Exercise 6.4. Prove that there exists linear codes that achieve the BSCp capacity. (Note that in
Section 6.3 we argued that there exists not necessarily a linear code that achieves the capacity.)

Hint: Modify the argument in Section 6.3: in some sense the proof is easier.

Exercise 6.5. Prove that for communication on BSCp , if an encoding function E achieves a max-
imum decoding error probability (taken over all messages) that is exponentially small, i.e., at
most 2−γn for some γ > 0, then there exists a δ = δ(γ, p) > 0 such that the code deﬁned by E has
relative distance at least δ. In other words, good distance is necessary for exponentially small
maximum decoding error probability.

Exercise 6.6. Prove that the capacity of the qSCp is 1 − Hq (p).

Exercise 6.7. The binary erasure channel with erasure probability α has capacity 1 − α. In this
problem, you will prove this result (and its generalization to larger alphabets) via a sequence of
smaller results.

1. For positive integers k ≤ n, show that less than a fraction q k−n of the k × n matrices G
over Fq fail to generate a linear code of block length n and dimension k. (Or equivalently,
except with probability less than q k−n, the rank of a random k × n matrix G over Fq is k.)

Hint: Try out the obvious greedy algorithm to construct a k × n matrix of rank k. You will see that you will

have many choices every step: from this compute (a lower bound on) the number of full rank matrices that

can be generated by this algorithm.

2. Consider the q-ary erasure channel with erasure probability α (qECα, for some α, 0 ≤ α ≤
1): the input to this channel is a ﬁeld element x ∈ Fq , and the output is x with probability
1 − α, and an erasure ‘?’ with probability α. For a linear code C generated by an k × n
matrix G over Fq , let D : (Fq ∪ {?})n → C ∪ {fail} be the following decoder:

D(y) = { c if y agrees with exactly one c ∈ C on the unerased entries in Fq
fail otherwise

For a set J ⊆ {1, 2, . . . , n}, let Perr(G|J ) be the probability (over the channel noise and choice
of a random message) that D outputs fail conditioned on the erasures being indexed by J .
Prove that the average value of Perr(G|J ) taken over all G ∈ Fk×n
q is less than q k−n+|J |.

3. Let Perr(G) be the decoding error probability of the decoder D for communication using
the code generated by G on the qECα. Show that when k = Rn for R < 1 − α, the average
value of Perr(G) over all k × n matrices G over Fq is exponentially small in n.

4. Conclude that one can reliably communicate on the qECα at any rate less than 1−α using
a linear code.

Exercise 6.8. Consider a binary channel whose input/output alphabet is {0, 1}, where a 0 is trans-
mitted faithfully as a 0 (with probability 1), but a 1 is transmitted as a 0 with probability 1
2 and a
1 with probability 1/2. Compute the capacity of this channel.

123

Hint: This can be proved from scratch using only simple probabilistic facts already stated/used in the book.

Exercise 6.9. Argue that Reed-Solomon codes from Chapter 5 are strongly explicit codes (as in
Deﬁnition 6.3.2).

Exercise 6.10. In this problem we will prove a special case of the source coding theorem. For
any 0 ≤ p ≤ 1/2, let D(p) be the distribution on {0, 1}n, where each of the n bits are picked
independently to be 1 with probability p and 0 otherwise. Argue that for every ε > 0, strings
from D(p) can be compressed with H (p + ε) · n bits for large enough n.
More precisely show that for any constant 0 ≤ p ≤ 1/2 and every ε > 0, for large enough
n there exists an encoding (or compression) function E : {0, 1}n → {0, 1}∗ and a decoding (or
decompression) function D : {0, 1}∗ → {0, 1}n such that
4

1. For every x ∈ {0, 1}n, D(E (x)) = x, and

2. Ex←D(p) [|E (x)|] ≤ H (p + ε) · n, where we use |E (x)| to denote the length of the string E (x).
In other words, the compression rate is H (p + ε).

Hint: Handle the “typical" strings from D and non-typical strings separately.

Exercise 6.11. Show that if there is a constructive solution to Shannon’s channel coding theorem
with E being a linear map, then there is a constructive solution to Shannon’s source coding
theorem in the case where the source produces a sequence of independent bits of bias p.
More precisely, let (E , D) be an encoding and decoding pairs that allows for reliable com-
munication over BSCp with exponentially small decoding error and E is a linear map with rate
1 − H (p) − ε. Then there exists a compressing and decompressing pair (E ′, D ′) that allows for
compression rate H (p)+ε (where compression rate is as deﬁned in part 2 in Exercise 6.10). The
decompression algorithm D ′ can be randomized and is allowed exponentially small error prob-
ability (where the probability can be taken over both the internal randomness of D ′ and D(p)).
Finally if (E , D) are both polynomial time algorithms, then (E ′, D ′) have to be polynomial time
algorithms too.

Exercise 6.12. Consider a Markovian source of bits, where the source consists of a 6-cycle with
three successive vertices outputting 0, and three successive vertices outputting 1, with the prob-
ability of either going left (or right) from any vertex is exactly 1/2. More precisely, consider
a graph with six vertices v0, v1, . . . , v5 such that there exists an edge (vi , v(i +1) mod 6) for every
0 ≤ i ≤ 5. Further the vertices vi for 0 ≤ i < 3 are labeled ℓ(vi ) = 0 and vertices v j for 3 ≤ j < 6
are labeled ℓ(v j ) = 1. Strings are generated from this source as follows: one starts with some
start vertex u0 (which is one of the vi ’s): i.e. the start state is u0. Any any point of time if the
current state if u, then the source outputs ℓ(u). Then with probability 1/2 the states moves to
each of the two neighbors of u.
Compute the optimal compression rate of this source.

4We use {0, 1}
∗ to denote the set of all binary strings.

124

Hint: Compress “state diagram" to a minimum and then make some basic observations to compress the source

information.

Exercise 6.13. Given codes C1 and C2 with encoding functions E1 : {0, 1}k1 → {0, 1}n1 and E2 :
{0, 1}k2 → {0, 1}n2 let E1 ⊗ E2 : {0, 1}k1×k2 → {0, 1}n1×n2 be the encoding function obtained as fol-
lows: view a message m as a k1 × k2 matrix. Encode the columns of m individually using the
function E1 to get an n1 × k2 matrix m′. Now encode the rows of m′ individually using E2 to get
an n1×n2 matrix that is the ﬁnal encoding under E1⊗E2 of m. Let C1⊗C2 be the code associated
with E1 ⊗ E2 (recall Exercise 2.19).
For i ≥ 3, let Hi denote the [2i − 1, 2i − i − 1, 3]2-Hamming code. Let Ci = Hi ⊗ Ci −1 with
C3 = H3 be a new family of codes.

1. Give a lower bound on the relative minimum distance of Ci . Does it go to zero as i → ∞?

2. Give a lower bound on the rate of Ci . Does it go to zero as i → ∞?

3. Consider the following simple decoding algorithm for Ci : Decode the rows of the rec’d
vector recursively using the decoding algorithm for Ci −1. Then decode each column ac-
cording to the Hamming decoding algorithm (e.g. Algorithm 5). Let δi denote the proba-
bility of decoding error of this algorithm on the BSCp . Show that there exists a p > 0 such
that δi → 0 as i → ∞.

Hint: First show that δi ≤ 4i δ2
i −1.

Exercise 6.14. We consider the problem of determining the best possible rate of transmission on
a stochastic memoryless channel with zero decoding error probability. Recall that a memoryless
stochastic channel is speciﬁed by a transition matrix M s.t. M(x, y) denotes the probability of y
being received if x was transmitted over the channel. Further, the noise acts independently on
each transmitted symbol. Let D denote the input alphabet. Let R(M) denote the best possible
rate for a code C such that there exists a decoder D such that for every c ∈ C , Pr[D(y) ̸= c] = 0,
where y is picked according to the distribution induced by M when c is transmitted over the
channel (i.e. the probability that y is a received word is exactly ∏n
i =1 M(ci , yi ) where C has block
length n). In this exercise we will derive an alternate characterization of R(M).
We begin with some deﬁnitions related to graphs G = (V, E ). An independent set S of G is a
subset S ⊆ V such that there is no edge contained in S, i.e. for every u ̸= v ∈ S, (u, v) ̸∈ E . For a
given graph G , we use α(G ) to denote the size of largest independent set in G . Further, given
an integer n ≥ 1, the n-fold product of G , which we will denote by G n, is deﬁned as follows:
G n = (V n, E ′), where ((u1, . . . , un), (v1, . . . , vn)) ∈ E ′ if and only if for every i ∈ [n] either ui = vi or
(ui , vi ) ∈ E .
Finally, deﬁne a confusion graph GM = (V, E ) as follows. The set of vertices V = D and for
every x1 ̸= x2 ∈ D, (x, y) ∈ E if and only if there exists a y such that M(x1, y) ̸= 0 and M(x2, y) ̸= 0.

125

1. Prove that
 R(M) = lim
n→∞ 1
n · log|D| (
α (
G n
M)) .5 (6.21)

2. A clique cover for a graph G = (V, E ) is a partition of the vertices V = {V1, . . . ,Vc } (i.e. Vi and
V j are disjoint for every i ̸= j ∈ [c] and ∪i Vi = V ) such that the graph induced on Vi is a
complete graph (i.e. for every i ∈ [c] and x ̸= y ∈ Vi , we have (x, y) ∈ E ). We call c to be the
size of the clique cover V1, . . . ,Vc . Finally, deﬁne ν(G ) to be the size of the smallest clique
cover for G . Argue that α(G )n ≤ α(G n) ≤ ν(G )n.

Conclude that log|D| α(G ) ≤ R(M) ≤ log|D| ν(G ). (6.22)

3. Consider any transition matrix M such that the corresponding graph C4 = GM is a 4-cycle
(i.e. the graph ({0, 1, 2, 3}, E ) where (i , i + 1 mod 4) ∈ E for every 0 ≤ i ≤ 3). Using part 2 or
otherwise, argue that R(M) = 1
2 .

4. Consider any transition matrix M such that the corresponding graph C5 = GM is a 5-cycle
(i.e. the graph ({0, 1, 2, 4}, E ) where (i , i + 1 mod 5) ∈ E for every 0 ≤ i ≤ 4). Using part 2
or otherwise, argue that R(M) ≥ 1
2 · log5 5. (This lower bound is known to be tight: see
Section 6.6 for more.)

6.6 Bibliographic Notes

Shannon’s results that were discussed in this chapter appeared in his seminal 1948 paper [89].
All the channels mentioned in this chapter were considered by Shannon except for the B EC
channel, which was introduced by Elias.
The proof method used to prove Shannon’s result for BSCp has its own name– “random
coding with expurgation."
Elias [27] answered Question 6.3.2 (the argument in Exercise 6.13 is due to him).

5In literature, R(M) is deﬁned with log|D| replaced by log2. We used the deﬁnition in (6.21) to be consistent with
our deﬁnition of capacity of a noisy channel. See Section 6.6 for more.

126

Chapter 7

Bridging the Gap Between Shannon and
Hamming: List Decoding

In Section 6.4, we made a qualitative comparison between Hamming and Shannon’s world. We
start this chapter by doing a more quantitative comparison between the two threads of coding
theory. In Section 7.2 we introduce the notion of list decoding, which potentially allows us to
go beyond the (quantitative) results of Hamming and approach those of Shannon’s. Then in
Section 7.3, we show how list decoding allows us to go beyond half the distance bound for any
code. Section 7.4 proves the optimal trade-off between rate and fraction of correctable errors via
list decoding. Finally, in Section 7.5, we formalize why list decoding could be a useful primitive
in practical communication setups.

7.1 Hamming versus Shannon: part II

Let us compare Hamming and Shannon theories in terms of the asymptotic bounds we have
seen so far (recall rate R = k
n and relative distance δ = d
n ).

• Hamming theory: Can correct ≤ δ
2 fraction of worse case errors for codes of relative dis-
tance δ. By the Singleton bound (Theorem 4.3.1),

δ ≤ 1 − R,

which by Proposition 1.4.1 implies that p fraction of errors can be corrected has to satisfy

p ≤ 1 − R
2 .

The above can be achieved via efﬁcient decoding algorithms for example for Reed-Solomon
codes (we’ll see this later in the book).

• Shannon theory: In qSCp , for 0 ≤ p < 1 − 1/q, we can have reliable communication with
R < 1 − Hq (p). It can be shown that
 127
 bad examples

bad examples

δ
2
 δ
2

δ
2

δ
2
 > δ
2
 c1

c2
c3

c4 y

z

Figure 7.1: In this example vectors are embedded into Euclidean space such that the Euclidean
distance between two mapped points is the same as the Hamming distance between vectors.
c1, c2, c3, c4 are codewords. The dotted lines contain the “bad examples," that is, the received
words for which unique decoding is not possible.

1. 1 − Hq (p) ≤ 1 − p (this is left as an exercise); and

2. 1− Hq (p) ≥ 1− p −ε, for large enough q– in particular, q = 2Ω(1/ε) (Proposition 3.3.2).

Thus, we can have reliable communication with p ∼ 1 − R on qSCp for large enough q.

There is a gap between Shannon and Hamming world: one can correct twice as many errors
in Shannon’s world. One natural question to ask is whether we can somehow “bridge" this gap.
Towards this end, we will now re-visit the the bad example for unique decoding (Figure 1.3) and
consider an extension of the bad example as shown in Figure 7.1.
Recall that y and the codewords c1 and c2 form the bad example for unique decoding that
we have already seen before. Recall that for this particular received word we can not do error
recovery by unique decoding since there are two codewords c1 and c2 having the same distance
δ
2 from vector y. On the other hand, the received word z has an unique codeword c1 with dis-
tance p > δ
2 . However, unique decoding does not allow for error recovery from z. This is because
by deﬁnition of unique decoding, the decoder must be able to recover from every error pattern
(with a given Hamming weight bound). Thus, by Proposition 1.4.1, the decoded codeword can-
not have relative Hamming distance larger than δ/2 from the received word. In this example,
because of the received word y, unique decoding gives up on the opportunity to decode z.
Let us consider the example in Figure 7.1 for the binary case. It can be shown that the
number of vectors in dotted lines is insigniﬁcant compared to volume of shaded area (for large
enough block length of the code). The volume of all Hamming balls of radius δ
2 around all the

128

2k codewords is roughly equal to:
 2k 2nH ( δ
2 ),

which implies that the volume of the shaded area (without the dotted lines) is approximately
equal to:
 2n − 2k 2nH ( δ
2 ).

In other words, the volume when expressed as a fraction of the volume of the ambient space is
roughly:
 1 − 2−n(1−H ( δ
2 )−R), (7.1)

where k = Rn and by the Hamming bound (Theorem 1.3) R ≤ 1 − H ( δ
2 ). If R < 1 − H ( δ
2 ) then
second term of (7.1) is very small. Therefore the number of vectors in shaded area (without
the bad examples) is almost all of the ambient space. Note that by the stringent condition on
unique decoding none of these received words can be decoded (even though for such received
words there is a unique closest codeword). Thus, in order to be able to decode such received
vectors, we need to relax the notion of unique decoding. We will consider such a relaxation
called list decoding next.

7.2 List Decoding

The new notion of decoding that we will discuss is called list decoding as the decoder is allowed
to output a list of answers. We now formally deﬁne (the combinatorial version of) list decoding:

Deﬁnition 7.2.1. Given 0 ≤ ρ ≤ 1, L ≥ 1, a code C ⊆ Σn is (ρ, L)-list decodable if for every received
word y ∈ Σn, ∣{c ∈ C |∆(y, c) ≤ ρn}∣ ≤ L

Given an error parameter ρ, a code C and a received word y, a list-decoding algorithm
should output all codewords in C that are within (relative) Hamming distance ρ from y. Note
that if the fraction of errors that occurred during transmission is at most ρ then the transmitted
codeword is guaranteed to be in the output list. Further, note that if C is (ρ, L)-list decodable
then the algorithm will always output at most L codewords for any received word. In other
words, for efﬁcient list-decoding algorithm, L should be a polynomial in the block length n
(as otherwise the algorithm will have to output a super-polynomial number of codewords and
hence, cannot have a polynomial running time). Thus, the restriction of L being at most some
polynomial in n is an a priori requirement enforced by the fact that we are interested in efﬁ-
cient polynomial time decoding algorithms. Another reason for insisting on a bound on L is
that otherwise the decoding problem can become trivial: for example, one can output all the
codewords in the code. Finally, it is worthwhile to note that one can always have an exponential
time list-decoding algorithm: go through all the codewords in the code and pick the ones that
are within ρ (relative) Hamming distance of the received word.
Note that in the communication setup, we need to recover the transmitted message. In
such a scenario, outputting a list might not be useful. There are two ways to get around this
“problem":
 129

1. Declare a decoding error if list size > 1. Note that this generalizes unique decoding (as
when the number of errors is at most half the distance of the code then there is a unique
codeword and hence, the list size will be at most one). However, the gain over unique
decoding would be substantial only if for most error patterns (of weight signiﬁcantly more
than half the distance of the code) the output list size is at most one. Fortunately, it can
be show that:

• For random codes, with high probability, for most error patterns, the list size is at
most one. In other words, for most codes, we can hope to see a gain over unique
decoding. The proof of this fact follows from Shannon’s proof for the capacity for
qSC: the details are left as an exercise.

• In Section 7.5, we show that the above behavior is in fact general: i.e. for any code
(over a large enough alphabet) it is true that with high probability, for most error
patterns, the list size is at most one.

Thus, using this option to deal with multiple answers, we still deal with worse case errors
but can correct more error patterns than unique decoding.

2. If the decoder has access to some side information, then it can use that to prune the list.
Informally, if the worst-case list size is L, then the amount of extra information one needs
is O(log L). This will effectively decrease
1 the dimension of the code by O(log L), so if L
is small enough, this will have negligible effect on the rate of the code. There are also
application (especially in complexity theory) where one does not really care about the
rate being the best possible.

Recall that Proposition 1.4.1 implies that δ/2 is the maximum fraction of errors correctable
with unique decoding. Since list decoding is a relaxation of unique decoding, it is natural to
wonder

Question 7.2.1. Can we correct more than δ/2 fraction of errors using list decoding?

and if so

Question 7.2.2. What is the maximum fraction of errors correctable using list decoding?

In particular, note that the intuition from Figure 7.1 states that the answer to Question 7.2.1
should be yes.

1Note that side information effectively means that not all possible vectors are valid messages.

130

7.3 Johnson Bound

In this section, we will indeed answer Question 7.2.1 in the afﬁrmative by stating a bound due
to Johnson. To setup the context again, recall that Proposition 1.4.1 implies that any code with
relative distance δ is (δ/2, 1)-list decodable.
Notice that if we can show a code for some e > ⌊ d −1
2
 ⌋ is (e/n, nO(1))-list decodable, then
(combinatorially) it is possible to list decode that code up to e errors. We’ll show by proving the
Johnson bound that this is indeed the case for any code.

Theorem 7.3.1 (Johnson Bound). Let C ⊆ [q]
n be a code of distance d . If ρ < Jq ( d
n
 ), then C is a
(ρ, qd n)-list decodable code, where the function Jq (δ) is deﬁned as

Jq (δ) = (
1 − 1
q
 ) (

1 −
 √

1 − qδ
q − 1
 )
 .

Proof (for q = 2). The proof technique that we will use has a name: double counting. The main
idea is to count the same quantity in two different ways to get both an upper and lower bound
on the same quantity. These bounds then imply an inequality and we will derive our desired
bound from this inequality.
We have to show that for every binary code C ⊆ {0, 1}n with distance d (i.e. for every c1 ̸= c2 ∈
C , ∆(c1, c2) ≥ d ) and every y ∈ {0, 1}n, |B (y, e) ⋂C | ≤ 2d n.
Fix arbitrary C and y. Let c1, . . . , cM ∈ B (y, e). We need to show that M ≤ 2d n. Deﬁne c′
i =
ci − y for 1 ≤ i ≤ M . Then we have the following:

(i) w t (c′
i ) ≤ e for 1 ≤ i ≤ M because ci ∈ B (y, e).

(ii) ∆(c′
i , c′
j ) ≥ d for every i ̸= j because ∆(ci , c j ) ≥ d .

Deﬁne S = ∑

i < j ∆(c′
i , c′
j ).

We will prove both an upper and a lower bound on S from which we will extract the required
upper bound on M . Then from (ii) we have

S ≥
 (M
2
 )

d (7.2)

Consider the n × M matrix (c′T
1 , · · · , c′T
M ). Deﬁne mi as the number of 1’s in the i -th row for
1 ≤ i ≤ n. Then the i -th row of the matrix contributes the value mi (M − mi ) to S because this
is the number of 0-1 pairs in that row. (Note that each such pair contributes one to S.) This
implies that
 S = n∑

i =1 mi (M − mi ). (7.3)

131

Deﬁne ¯e = ∑

i
 mi
M .

Note that n∑

i =1 mi = M∑

j =1 w t (ci ) ≤ eM ,

where the inequality follows From (i) above. Thus, we have

¯e ≤ e.

Using the Cauchy-Schwartz inequality (i.e., 〈x, y〉 ≤ ||x|| · ||y|| for x, y ∈ R
n) by taking x =
(m1, · · · , mn), y = (1/n, · · · , 1/n), we have

( ∑n
i =1 mi
n
 )2 ≤
 ( n∑

i =1 m2
i
 ) 1
n . (7.4)

Thus, from (7.3)

S = n∑

i =1 mi (M − mi ) = M 2 ¯e − n∑

i =1 m2
i ≤ M 2 ¯e − (M ¯e)2

n = M 2( ¯e − ¯e2

n ), (7.5)

where the inequality follows from (7.4). By (7.2) and (7.5),

M 2 ( ¯e − ¯e2

n
 ) ≥ M (M − 1)
2 d ,

which implies that

M ≤ d n
d n − 2n ¯e + 2 ¯e2 = 2d n
2d n − n2 + n2 − 4n ¯e + 4 ¯e2 = 2d n
(n − 2 ¯e)2 − n(n − 2d )

≤ 2d n
(n − 2e)2 − n(n − 2d ) , (7.6)

where the last inequality follows from the fact that ¯e ≤ e. Then from

e
n < 1
2
 

1 −
 √

1 − 2d
n
 

 ,

we get n − 2e > √
n(n − 2d ).

In other words (n − 2e)2 > n(n − 2d ).

Thus, (n −2e)2 −n(n −2d ) ≥ 1 because n, e are all integers and therefore, from (7.6), we have
M ≤ 2d n as desired.
 132

Next, we prove the following property of the function Jq (·), which along with the Johnson
bound answers Question 7.2.1 in the afﬁrmative.

Lemma 7.3.2. Let q ≥ 2 be an integer and let 0 ≤ x ≤ 1 − 1
q . Then the following inequalities hold:

Jq (x) ≥ 1 − p1 − x ≥ x
2 ,

where the second inequality is tight for x > 0.

Proof. We start with by proving the inequality

(
1 − 1
q
 ) (
1 −
 √

1 − xq
q − 1
 )
 ≥ 1 − p1 − x.

Indeed, both the LHS and RHS of the inequality are zero at x = 0. Further, it is easy to check
that the derivatives of the LHS and RHS are 1√1− xq
q−1 and 1p
1−x respectively. The former is always

larger than the latter quantity. This implies that the LHS increases more rapidly than the RHS,
which in turn proves the required inequality.
The second inequality follows from the subsequent relations. As x ≥ 0,

1 − x + x2

4 ≥ 1 − x,

which implies that (1 − x
2
 )2 ≥ 1 − x,

which in turn implies the required inequality. (Note that the two inequalities above are strict
for x > 0, which implies that 1 − p
1 − x > x/2 for every x > 0, as desired.)

Theorem 7.3.1 and Lemma 7.3.2 imply that for any code, list decoding can potentially cor-
rect strictly more errors than unique decoding in polynomial time, as long as q is at most some
polynomial in n (which will be true of all the codes that we discuss in this book). This answers
Question 7.2.1 in the afﬁrmative. See Figure 7.2 for an illustration of the gap between the John-
son bound and the unique decoding bound.
Theorem 7.3.1 and Lemma 7.3.2 also implies the following “alphabet-free" version of the
Johnson bound.

Theorem 7.3.3 (Alphabet-Free Johnson Bound). If e ≤ n − p
n(n − d ), then any code with dis-
tance d is (e/n, qnd )-list decodable for all the q.

A natural question to ask is the following:
 133

 0

 0.2

 0.4

 0.6

 0.8

 1
  0  0.2  0.4  0.6  0.8  1Fraction of errors (p) --->
Rate (R) --->
 Singleton bound
Johnson bound
Unique decoding bound

Figure 7.2: The trade-off between rate R and the fraction of errors that can be corrected. 1 − p
R
is the trade-off implied by the Johnson bound. The bound for unique decoding is (1−R)/2 while
1 − R is the Singleton bound (and the list decoding capacity for codes over large alphabets).

Question 7.3.1. Is the Johnson bound tight?

The answer is yes in the sense that there exist linear codes with relative distance δ such
that we can ﬁnd Hamming ball of radius larger than Jq (δ) with super-polynomially many code-
words. On the other hand, in the next section, we will show that, in some sense, it is not tight.

7.4 List-Decoding Capacity

In the previous section, we saw what can one achieve with list decoding in terms of distance of
a code. In this section, let us come back to Question 7.2.2. In particular, we will consider the
trade-off between rate and the fraction of errors correctable by list decoding. Unlike the case of
unique decoding and like the case of BSCp , we will be able to prove an optimal trade-off.
Next, we will prove the following result regarding the optimal trade-off between rate of a
code and the fraction of errors that can be corrected via list decoding.

Theorem 7.4.1. Let q ≥ 2, 0 ≤ p < 1 − 1
q , and ε > 0. Then the following holds for codes of large
enough block length n:

(i) If R ≤ 1 − Hq (p) − ε, then there exists a (p,O ( 1
ε ))
-list decodable code.

(ii) If R > 1 − Hq (p) + ε, every (
ρ, L)-list decodable code has L ≥ q Ω(n).

134

Thus, the List-decoding capacity2 is 1 − Hq (p) (where p is the fraction of errors). Further,
this fully answers Question 7.2.2. Finally, note that this exactly matches capacity for qSCp and
hence, list decoding can be seen as a bridge between Shannon’s world and Hamming’s world.
The remarkable aspect of this result is that we bridge the gap between these worlds by allowing
the decoder to output at most O(1/ε) many codewords.

7.4.1 Proof of Theorem 7.4.1

We begin with the basic idea behind the proof of part (i) of the theorem.
As in Shannon’s proof for capacity of BSCp , we will use the probabilistic method (Section 3.2).
In particular, we will pick a random code and show that it satisﬁes the required property with
non-zero probability. In fact, we will show that a random code is (ρ, L)-list decodable with high
probability as long as:
 R ≤ 1 − Hq (p) − 1
L
The analysis will proceed by proving that probability of a “bad event" is small. “Bad event"
means there exist messages m0, m1, · · · , mL ∈ [q]
Rn and a received code y ∈ [q]
n such that:

∆ (
C (mi ), y)) ≤ ρn, for every 0 ≤ i ≤ L.

Note that if a bad event occurs, then the code is not a (ρ, L)-list decodable code. The probability
of the occurrence of any bad event will then be calculated by an application of the union bound.
Next, we restate Theorem 7.4.1 and prove a stronger version of part (i). (Note that L = ⌈ 1
ε ⌉ in
Theorem 7.4.2 implies Theorem 7.4.1.)

Theorem 7.4.2 (List-Decoding Capacity). Let q ≥ 2 be an integer, and 0 < ρ < 1 − 1
q be a real
number.

(i) Let L ≥ 1 be an integer, then there exists an (
ρ, L)-list decodable code with rate

R ≤ 1 − Hq (ρ) − 1
L

(ii) For every (
ρ, L) code of rate 1 − Hq (ρ) + ε, it is necessary that L ≥ 2Ω(εn).

Proof. We start with the proof of (i). Pick a code C at random where

|C | = q k , where k ≤ (
1 − Hq (ρ) − 1
L
 ) n.

That is, as in Shannon’s proof, for every message m, pick C (m) uniformly and independently at
random from [q]
n.

2Actually the phrase should be something like “capacity of worst case noise model under list decoding" as the
capacity is a property of the channel. However, in the interest of brevity we will only use the term list-decoding
capacity.
 135

Given y ∈ [q]
n , and m0, · · · , mL ∈ [q]
k , the tuple (y, m0, · · · , mL) deﬁnes a bad event if

C (mi ) ∈ B (y, ρn), 0 ≤ i ≤ L.

Note that a code is (ρ, L)-list decodable if and only if there does not exist any bad event.
Fix y ∈ [q]
n and m0, · · · , mL ∈ [q]
k .
Note that for ﬁxed i , by the choice of C , we have:

Pr[C (mi ) ∈ B (y, ρn)] = V olq (ρn, n)

q n ≤ q −n(1−Hq (ρ)), (7.7)

where the inequality follows from the upper bound on the volume of a Hamming ball (Proposi-
tion 3.3.1). Now the probability of a bad event given (y, m0, · · · , mL) is

Pr
 [ L⋀

i =0C (mi ) ∈ B (y, ρn)
]
 = L∏

0 Pr[C (mi ) ∈ B (y, ρn)] ≤ q −n(L+1)(1−Hq (ρ)), (7.8)

where the equality follows from the fact that the random choices of codewords for distinct mes-
sages are independent and the inequality follows from (7.7). Then,

Pr[ There is a bad event] ≤ q n( q k

L + 1
)
q −n(L+1)(1−Hq (ρ)) (7.9)

≤ q n q Rn(L+1)q −n(L+1)(1−Hq (ρ)) (7.10)

= q −n(L+1)[1−Hq (ρ)− 1
L+1 −R]

≤ q −n(L+1)[1−Hq (ρ)− 1
L+1 −1+Hq (ρ)+ 1
L ] (7.11)

= q − n
L

< 1

In the above, (7.9) follows by the union bound (Lemma 3.1.3) with (7.8) and by counting the

number of y’s (which is q n), and the number of L + 1 tuples (which is ( q k

L+1)
). (7.10) follows from
the fact that (a
b) ≤ ab and k = Rn. (7.11) follows by assumption R ≤ 1 − Hq (ρ) − 1
L . The rest of the
steps follow from rearranging and canceling the terms. Therefore, by the probabilistic method,
there exists C such that it is (ρ, L)-list decodable.

Now we turn to the proof of part (ii). For this part, we need to show the existence of a y ∈ [q]
n

such that |C ∩ B (y, ρn)| is exponentially large for every C of rate R ≥ 1 − Hq (ρ) + ε. We will again
use the probabilistic method to prove this result.
Pick y ∈ [q]
n uniformly at random. Fix c ∈ C . Then

Pr[c ∈ B (y, ρn)] = Pr[y ∈ B (c, ρn)]

= V olq (ρn, n)

q n (7.12)

≥ q −n(1−Hq (ρ))−o(n), (7.13)

136

where (7.12) follows from the fact that y is chosen uniformly at random from [q]
n and (7.13)
follows by the lower bound on the volume of the Hamming ball (Proposition 3.3.1).
We have
 E [|C ∩ B (y, ρn)|] = ∑

c∈C E [1c∈B (y,ρn)] (7.14)

= ∑

c∈C Pr[c ∈ B (y, ρn)]

≥ ∑

c∈C q −n(1−Hq (ρ)+o(n)) (7.15)

= q n[R−1+Hq (ρ)−o(1)]

≥ q Ω(εn)
 (7.16)

In the above, (7.14) follows by the linearity of expectation (Proposition 3.1.2), (7.15) follows
from (7.13), and (7.16) follows by choice of R. Hence, by the probabilistic method, there exists y
such that |B (y, ρn) ∩C | is q Ω(n), as desired.

The above proof can be modiﬁed to work for random linear codes. (See Exercise ??.)
We now return to Question 7.3.1. Note that by the Singleton bound, the Johnson bound im-
plies that for any code one can hope to list decode from about p ≤ 1 − p
R fraction of errors.
However, this trade-off between p and R is not tight. Note that Lemma 3.3.2 along with Theo-
rem 7.4.1 implies that for large q, the list decoding capacity is 1 − R > 1 − p
R. Figure 7.2 plots
and compares the relevant trade-offs.
Finally, we have shown that the list decoding capacity is 1 − Hq (p). However, we showed the
existence of a code that achieves the capacity by the probabilistic method. This then raises the
following question:

Question 7.4.1. Do there exist explicit codes that achieve list decoding capacity?

Also the only list decoding algorithm that we have seen so far is the brute force algorithm that
checks every codeword to see if they need to be output. This also leads to the follow-up question

Question 7.4.2. Can we achieve list decoding capacity with efﬁcient list decoding algorithms?

A more modest goal related to the above would be the following:

137

Question 7.4.3. Can we design an efﬁcient list decoding algorithm that can achieve the John-
son bound? In particular, can we efﬁciently list decode a code of rate R from 1 − p
R fraction
of errors?

7.5 List Decoding from Random Errors

In this section, we formalize the intuition we developed from Figure 7.1. In particular, recall
that we had informally argued that for most error patterns we can correct beyond the δ/2 bound
for unique decoding (Proposition 1.4.1). Johnson bound (Theorem 7.3.1) tells us that one can
indeed correct beyond δ/2 fraction of errors. However, there are two shortcomings. The ﬁrst is
that the Johnson bounds tells us that the output list size is qd n but it does not necessarily imply
that for most error patterns, there is unique by closest codewords (i.e. one can uniquely recover
the transmitted codeword). In other words, Johnson bound is a “true" list decoding result and
tells us nothing about the behavior of codes on the “average." The second aspect is that the
Johnson bound holds for up to 1 − p
1 − δ fraction of errors. Even though it is more than δ/2 for
every δ > 0, the bound e.g. is not say twice the unique decoding bound for every δ > 0.
Next we show that for any code with relative distance δ (over a large enough alphabet size)
for most error patterns, the output of a list decoder for any fraction of errors arbitrarily close to
δ will have size one. In fact, the result is somewhat stronger: it show that even if one ﬁxes the
error locations arbitrarily, for most error patterns the output list size is one.

Theorem 7.5.1. Let ε > 0 be a real and q ≥ 2Ω(1/ε) be an integer. Then the following is true for any
0 < δ < 1 − 1/q and large enough n. Let C ⊆ {0, 1, ...q − 1}n be a code with relative distance δ and
let S⊆ [n] such that |S| = (1 − ρ)n, where (0 < ρ ≤ δ − ε).
Then, for all c ∈ C and all but a q −Ω(εn) fraction of error patterns, e ∈ {0, 1...q − 1}n such that

eS = 0 and w t (e) = ρn (7.17)

the only codeword within Hamming distance ρn of c + e is c itself.

For illustration of the kinds of error pattern we will deal with, see Figure 7.3.

eS

S
 0e

Figure 7.3: Illustration of the kind of error patterns we are trying to count.

Before we present the proof, we present certain corollaries (the proofs of which we leave as
exercises). First the result above implies a similar result of the output list size being one for the

138

following two random noise models: (i) uniform distribution over all error patterns of weight
ρn and (ii) qSCp . In fact, we claim that the result also implies that any code with distance at
least p + ε allows for reliable communication over qSCp . (Contrast the 2p + ε distance that was
needed for a similar result that was implied by Proposition 6.4.1.)
Finally, we present a lemma (the proof is left as an exercise) that will be crucial to the proof
of Theorem 7.5.1.

Lemma 7.5.2. Let be C be an (n, k, d )q code. If we ﬁx the values in n − d + 1 out of the n positions
in a possible codeword, then at most one codeword in C can agree with the ﬁxed values.

Proof of Theorem 7.5.1. For the rest of the proof, ﬁx a c ∈ C . For notational convenience deﬁne
ES to be the set of all error patterns e such that eS = 0 and w t (e) = ρn. Note that as every error
position has (q − 1) non-zero choices and there are ρn such positions in [n] \ S, we have

|Es| = (q − 1)ρn. (7.18)

Call an error pattern e ∈ Es as bad if there exists another codeword c′ ̸= c such that

△(c′, c + e) ≤ ρn.

Now, we need to show that the number of bad error patterns is at most

q −Ω(εn)|Es|.

We will prove this by a somewhat careful counting argument.
We begin with a deﬁnition.

Deﬁnition 7.5.1. Every error pattern e is associated with a codeword c(e), which is the closest
codeword which lies within Hamming distance ρn from it.

For a bad error pattern we insist on having c(e) ̸= c– note that for a bad error pattern such a
codeword always exists. Let A be the set of positions where c(e) agrees with c + e.
The rest of the argument will proceed as follows. For each possible A, we count how many
bad patterns e are associated with it (i.e. c + e and c(e) agree exactly in the positions in A). To
bound this count non-trivially, we will use Lemma 7.5.2.
Deﬁne a real number α such that |A| = αn. Note that since c(e) and c + e agree in at least
1 − ρ positions, α ≥ 1 − ρ ≥ 1 − δ + ε. (7.19)

For now let us ﬁx A with |A| = αn and to expedite the counting of the number of bad error
patterns, let us deﬁne two more sets:
 A1 = A ∩ S,

and A2 = A \ A1.

139

A

S
 A1
 A2

e

c + e

c(e)

Figure 7.4: Illustration of notation used in the proof of Theorem 7.5.1. Positions in two different
vectors that agree have the same color.
.

See Figure 7.4 for an illustration of the notation that we have ﬁxed so far.
Deﬁne β such that |A1| = βn. (7.20)

Note that this implies that |A2| = (α − β)n. (7.21)

Further, since A1 ⊆ A, we have β ≤ α.

To recap, we have argued that every bad error pattern e corresponds to a codeword c(e) ̸= c
and is associated with a pair of subsets (A1, A2). So, we ﬁx (A1, A2) and then count the number
of bad e ’s that map to (A1, A2). (Later on we will aggregate this count over all possible choices
of (A1, A2).)
Towards this end, ﬁrst we overestimate the number of error patterns e that map to (A1, A2)
by allowing such e to have arbitrary values in [n] \ (S ∪ A2). Note that all such values have to be
non-zero (because of (7.17). This implies that the number of possible distinct e[n]\(S∪A2) is at
most (q − 1)n−|S|−|A2| = q n−(1−ρ)n−(α−β)n, (7.22)

where the equality follows from the given size of S and (7.21). Next ﬁx a non-zero x and let us
only consider error patterns e such that
 e[n]\(S∪A2) = x.

Note that at this stage we have an error pattern e as depicted in Figure 7.5.

140
 ??e
 S
 A1 A2

0 x

Figure 7.5: Illustration of the kind of error patterns we are trying to count now. The ? denote
values that have not been ﬁxed yet.

Now note that if we ﬁx c(e)A2, then we would also ﬁx eA2 (as (c + e)A2 = (c(e))A2). Recall that
c is already ﬁxed and hence, this would ﬁx e as well. Further, note that

c(e)A1 = (c + e)A1 = cA1.

This implies that c(e)A1 is already ﬁxed and hence, by Lemma 7.5.2 we would ﬁx c(e) if we ﬁx (say
the ﬁrst) (1−δ)n+1−|A1| positions in c(e)A2. Or in other words, by ﬁxing the ﬁrst (1−δ)n+1−|A1|
positions in eA2, e would be completely determined. Thus, the number of choices for e that have
the pattern in Figure 7.5 is upper bounded by

q (1−δ)n+1−|A1| = (q − 1)(1−δ)n+1−βn, (7.23)

where the equality follows from (7.20).
Thus, by (7.22) and (7.23) the number of possible bad error patterns e that map to (A1, A2)
is upper bounded by

(q − 1)n−(1−ρ)n−αn+βn+(1−δ)n+1−βn ≤ (q − 1)ρn−εn+1 = (q − 1)−εn+1|Es|,

where the inequality follows from (7.19) and the equality follows from (7.18).
Finally, summing up over all choices of A = (A1, A2) (of which there are at most 2n), we get
that the total number of bad patterns is upper bounded by

2n · (q − 1)−εn+1 · |ES| ≤ q
 n
log2 q − εn
2 + 1
2 · |E A| ≤ q −εn/4 · |ES|,

where the ﬁrst inequality follows from q − 1 ≥ pq (which in turn is true for q ≥ 3) while the
last inequality follows from the fact that for q ≥ Ω(1/ε) and large enough n, n+1/2
log2 q < εn
4 . This
completes the proof. ✷
It can be shown that Theorem 7.5.1 is not true for q = 2o(1/ε). The proof is left as an exercise.

7.6 Exercises

Exercise 7.1. Show that with high probability, a random linear code is (ρ, L)-list decodable code
as long as
 R ≤ 1 − Hq (ρ) − 1
⌈logq (L + 1)⌉ . (7.24)

141

Hint: Think how to ﬁx (7.8) for random linear code.

Exercise 7.2. In this exercise we will see how we can "ﬁx" the dependence on L is the rate of
random linear codes from Exercise 7.1. In particular, we will consider the following family of
codes that are somewhere between linear and general codes and are called pseudolinear codes,
which are deﬁned as follows.
Let q be a prime power and let 1 ≤ k ≤ n and L ≥ 1 be integers. Then an (n, k, L, r, q)-family
of pseudolinear codes is deﬁned as follows. Let H be the parity check matrix of an [q k − 1, q k −
1 − r, L + 1]q linear code and H
′ be an extension of H with the ﬁrst column being 0 (and the
rest being H). Every code in the family is indexed by a matrix A ∈ Fn×r
q . Fix such a A. Then the
corresponding code CA is deﬁned as follows. For any x ∈ F
k
q , we have

CA(x) = A · H
′
x,

where H
′
x is the column corresonding to x, when though of as an integer between 0 and q k − 1.
Next, we will argue that random pseudolinear codes have near optimal list decodability:

1. Fix non-zero messages m1, . . . mL. Then for a random code CA from an (n, k, L, r, q)-family
of pseudolinear code family, the codewords CA(m1), . . . ,CA(mL) are independent random
vectors in Fn
q .

2. Deﬁne (n, k, L, q)-family of pseudolinear codes to be (n, k, L,O(kL), q)-family of pseudo-
linear codes. Argue that (n, k, L, q)-family of pseudolinear codes exist.

Hint: Exercise 5.10 might be helpful.

3. Let ε > 0 and q ≥ 2 be a prime power. Further let 0 ≤ ρ < 1 − 1/q. Then for a large enough
n and k such that k
n ≥ 1 − Hq (ρ) − 1
L − ε,

a random (n, k, L, q)-pesudolinear code is (ρ, L)-list decodable.

4. Show that one can construct a (ρ, L)-list decodable pseudolinear code with rate at least
1 − Hq (ρ) − 1
L − ε in qO(kL+n) time.

Hint: Use method of conditional expectations.

Exercise 7.3. In this exercise we will consider a notion of “average" list decoding that is closely
related to our usual notion of list decoding. As we will see in some subsequent exercises, some-
times it is easier to work with this average list decoding notion.

1. We begin with an equivalent deﬁnition of our usual notion of list decoding. Argue that
a code C is (ρ, L) list decodable if and only if for every y ∈ [q]
n and every subset of L + 1
codewords c0, . . . , cL we have that
 max
0≤i ≤L ∆(y, ci ) > ρn.

142

2. We deﬁne a code C to be (ρ, L)-average list decodable if for every y ∈ [q]
n and L + 1 code-
words c0, . . . , cL we have 1
L · L∑

i =0 ∆(y, ci ) > ρn.

Argue that if C is (ρ, L)-average list decodable then it is also (ρ, L)-list decodable.

3. Argue that if C is (ρ, L)-list decodable then it is also (ρ(1−γ), ⌈L/γ⌉)-average list decodable
(for any 0 < γ < ρ).

Exercise 7.4. In Section 7.5 we saw that for any code one can correct arbitrarily close to relative
distance fraction of random errors. In this exercise we will see that one can prove a weaker
result. In particular let D be an arbitrary distribution on Bq (0, ρn). Then argue that for most
codes, the list size with high probability is 1. In other words, show that for 1 − o(1), fraction of
codes C we have that for every codeword c ∈ C

Pr
e←D
 [
|Bq (c + e, ρn) ∩C | > 1] = o(1).

Hint: Adapt the proof of Theorem 6.3.1 from Section 6.3.2.

Exercise 7.5. We call a code (ρ, L)-erasure list-decodable is informally for any received word with
at most ρ fraction of erasures at most L codewords agree with it in the unerased positions. More
formally, an (n, k)q -code C is (ρ, L)-erasure list-decodable if for every y ∈ [q]
(1−ρ)n and every
subset T ⊆ [n] with |T | = (1 − ρ)n, we have that
∣{c ∈ C |cT = y}∣ ≤ L.

In this exercise you will prove some simple bounds on the best possible rate for erasure-list
decodable code.

1. Argue that if C has distance d then it is ( d −1

n , 1)-erasure list decodable.

2. Show that there exists a (ρ, L)-erasure list decodable code of rate

L
L + 1 · (1 − ρ) − Hq (ρ)

L − γ,

for any γ > 0.

3. Argue that there exists a linear (ρ, L)-erasure list decodable code with rate

J − 1
J · (1 − ρ) − Hq (ρ)

J − 1 − γ,

where J = ⌈
logq (L + 1)⌉ and γ > 0.

4. Argue that the bound in item 2 is tight for large enough L by showing that if a code of rate
1 − ρ + ε is (ρ, L)-erasure list decodable then L is 2Ωε(n).

143

Exercise 7.6. In this exercise we will see an alternate characterization of erasure list-decodable
code for linear codes, which we will use to show separation between linear and non-linear code
in the next exercise.
Given a linear code C ⊆ Fn
q and an integer 1 ≤ r ≤ n, deﬁne the r ’th generalized Hamming
distance, denoted by dr (C ), as follows. First given a set D ⊆ FN
q , we deﬁne the support of D as
the union of the supports of vectors in D. More precisely

supp(D) = {i | there exists (u1, . . . , un) ∈ S such that ui ̸= 0}.

Then dr (C ) is size of the smallest support of all r -dimensional subcodes of C .
Argue the following:

1. (Warmup) Convince yourself that d1(C ) is the usual Hamming distance of C .

2. Prove that C is (ρn, L)-erasure list-decodable if and only if d1+⌊logq L⌋(C ) > ρn.

Exercise 7.7. In this exercise we use the connection between generalized Hamming distance
and erasure list decodability from Exercise 7.6 to show an “exponential separation" between
linear and non-linear codes when it comes to list decoding from erasure.
Argue the following:

1. Let C be an [n, k]q code. Then show that the average support size of r -dimensional sub-
codes of C is exactly q r − 1
q r · |C |
|C | − 1 · n.

2. From previous part or otherwise, conclude that if for an [n, k]q code C we have dr (C ) >
n(1 − q −r ), then we have
 |C | ≤ dr (C )
dr (C ) − n(1 − q −r ) ,

Note that the above bound for r = 1 recovers the Plotkin bound (second part of Theo-
rem 4.4.1).

3. Argue that any (family) of code C with dr (C ) = δr · n, its rate satisﬁes:

R(C ) ≤ 1 − q r

q r − 1 · δr + o(1).

Hint: Use a the result from previous part on a code related to C .

4. Argue that for small enough ε > 0, any linear (1 − ε, L)-erasure list decodable code with
positive rate must have L ≥ Ω(1/ε).

5. Argue that there exist (1 − ε,O(log(1/ε)))-erasure list decodable code with positive (in fact
Ω(ε)) rate. Conclude that there exists non-linear codes that have the same erasure list
decodability but with exponentially smaller list sizes than linear codes.

144

Exercise 7.8. In this exercise we will prove an analog of the Johnson bound (Theorem 7.3.1) but
for erasure list-decodable codes. In particular, let C be an (n, k, δn)q code. Then show that for

any ε > 0, C is an (( q
q−1 − ε) δ, q
(q−1)ε
 )-erasure list decodable.

Hint: The Plotkin bound (Theorem 4.4.1) might be useful.

Exercise 7.9. Let C be a q-ary (ρ, L)-(average) list decodable of rate R, then show that there exists
another (ρ, L)-(average) list decodable code with rate at least

R + Hq (λ) − 1 − o(1),

for any λ ∈ (ρ, 1 − 1/q] such that all codewords in C ′ have Hamming weight exactly λn.

Hint: Try to translate C .

Exercise 7.10. In this exercise, we will prove a lower bound on the list size of list decodable codes
that have optimal rate. We do this via a sequence of following steps:

1. Let C ⊆ [q]
n be a (ρ, L − 1)-list decodable code such that all codewords have Hamming
weight exactly λn for
 λ = ρ + 1
2L · ρL.

Then prove that
 |C | < 2L2

λL .

Hint: It might be useful to use the following result due to Erdös [29] (where we choose the variables to match

the relevant ones in the problem). Let A be a family of subsets of [n]. Then if every A ∈ A has size at least

2L2/λL, then there exist distinct A1, . . . , AL ∈ A such that ∩
L
i =1 Ai has size at least nλL
2 .

2. Argue that any q-ary (ρ, L − 1)-list decodable code C (for large enough block length) has

rate at most 1 − Hq (ρ) − bρ,q · ρL

L for some constant bρ,q that only depends on ρ and q.

Hint: Use the previous part and Exercise 7.9.

3. Argue that any q-ary (ρ, L)-list decodable C with rate 1−Hq (ρ)−ε mush satisfy L ≥ Ωρ,q (log(1/ε)).

Exercise 7.11. It follows from Theorem 7.4.1 that a random code of rate 1 − Hq (ρ) − ε with high
probability is (ρ,O(1/ε))-list decodable. On the other hand, the best lower bound on the list
size for codes of rate 1 − Hq (ρ) − ε (for constant p, q) is Ω(log(1/ε)) (as we just showed in Exer-
cise 7.10). It is natural to wonder if one can perhaps do a better argument for random codes. In
this exercise, we will show that our argument for random codes is the best possible (for random
codes). We will show this via the following sequence of steps:

1. Let C be a random (n, k)q code of rate 1 − Hq (ρ) − ε. For any y ∈ [q]
n and any subset
S ⊆ [q]
k of size L + 1, deﬁne the random event E (y, S) that for every m ∈ S, C (m) is at
Hamming distance at most ρn from y. Deﬁne

W = ∑

y,S E (y, S).

Argue that C is (ρ, L)-list decodable if and only if W = 0.

145

2. Deﬁne µ = q −n · V olq (ρn, n).

Argue that
 E [W ] ≥ 1
(L + 1)L+1 · µL+1 · q n · q k(L+1).

3. Argue that
 σ
2(Z ) ≤ q 2n · L+1∑

ℓ=1(L + 1)2(L+1) · q k(2L+2−ℓ) · µ
2L−ℓ+3.

Hint: Analyze the probability of both events E (y, S) and E (z, T ) happening together for various intersection

sizes ℓ = |S ∩ T |.

4. Argue that C is (
ρ, 1−Hq (ρ)
2ε
 )
-list decodable with probability at most q −Ωρ,ε(n).

Hint: Use Chebyschev’s inequality.

7.7 Bibliographic Notes

List decoding was deﬁned by Elias [28] and Wozencraft [105].
The result showing that for random error patterns, the list size with high probability is one
for the special case of Reed-Solomon codes was shown by McEliece [72]. The result for all codes
was proved by Rudra and Uurtamo [86]
In applications of list decoding in complexity theory (see for example [97],[38, Chap. 12]),
side information is used crucially to prune the output of a list decoding algorithm to compute
a unique answer.
Guruswami [37] showed that the answer to Question 7.3.1 is yes in the sense that there ex-
ist linear codes with relative distance δ such that we can ﬁnd Hamming ball of radius larger
than Jq (δ) with super-polynomially many codewords. This result was proven under a number-
theoretic assumption, which was later removed by [47].
(7.24) implies that there exist linear codes with rate 1 − Hq (ρ) − ε that are (
ρ, qO(1/ε))-list
decodable. (This is also true for most linear codes with the appropriate parameters.) However,
for a while just for q = 2, we knew the existence of (
ρ,O(1/ε))-list decodable codes [41] (though
it was not a high probability result). Guruswami, Håstad and Kopparty resolved this “gap" by
showing that random linear codes of rate 1 − Hq (ρ) − ε are (ρ,O(1/ε))-list decodable (with high
probability) [40].
 146

Chapter 8

What Cannot be Done-II

In this brief interlude of a chapter, we revisit the trade-offs between rate and relative distance
for codes. Recall that the best (and only) lower bound on R that we have seen is the GV bound
and the best upper bound on R that we have have seen so far is a combination of the Plotkin
and Hamming bounds (see Figure 4.5). In this chapter, we will prove the ﬁnal upper bound on
R in this book due to Elias and Bassalygo. Then we will mention the best known upper bound
on rate (but without stating or proving it). Finally, we will conclude by summarizing what we
have seen so far and laying down the course for the rest of the book.

8.1 Elias-Bassalygo bound

We begin with the statement of a new upper bound on the rate called the Elias-Bassalygo bound.

Theorem 8.1.1 (Elias-Bassalygo bound). Every q-ary code of rate R, distance δ, and large enough
block length, satisﬁes the following:
 R ≤ 1 − Hq (Jq (δ)) + o (1)

See Figure 8.1 for an illustration of the Elias-Bassalygo bound for binary codes. Note that
this bound is tighter than all the previous upper bounds on rate that we have seen so far.
The proof of Theorem 8.1.1 uses the following lemma:

Lemma 8.1.2. Given a q-ary code, C ⊆ [q]
nand 0 ≤ e ≤ n, there exists a Hamming ball of radius

e with at least |C |V olq (e,n)
q n codewords in it.

Proof. We will prove the existence of the required Hamming ball by the probabilistic method.
Pick a received word y ∈ [q]
n at random. It is easy to check that the expected value of |B (y, e)∩C |

is |C |V olq (e,n)
q n . (We have seen this argument earlier in the proof of part (ii) of Theorem 7.4.2.)
This by the probabilistic method implies the existence of a y ∈ [q]
n such that

|B (y, e) ∩C | ≥ |C |V olq (e, n)

q n ,

as desired.
 147

 0

 0.2

 0.4

 0.6

 0.8

 1
  0  0.2  0.4  0.6  0.8  1R
δ
 Hamming bound
GV bound
Singleton bound
Plotkin bound
Elias-Bassalygo bound

Figure 8.1: Singleton, Hamming, Plotkin, GV and Elias-Bassalygo bounds on rate versus dis-
tance for binary codes.

Proof of Theorem 8.1.1. Let C ⊆ [q]
n be any code with relative distance δ. Deﬁne e = n Jq (δ)−
1. By Lemma 8.1.2, there exists a Hamming ball with B codewords such that the following
inequality is true:
 B ≥ |C |V olq (e, n)

q n .

By our choice of e and the Johnson bound (Theorem 7.3.1), we have

B ≤ qd n.

Combining the upper and lower bounds on B implies the following

|C | ≤ qnd · q n

V olq (e, n) ≤ q n(1−Hq(Jq (δ))+o(1)),

where the second inequality follows from our good old lower bound on the volume of a
Hamming ball (Proposition 3.3.1) and the fact that qd n ≤ qn2 ≤ q o(n) for large enough n. This
implies that the rate R of C satisﬁes:

R ≤ 1 − Hq (Jq (δ)) + o (1) ,

as desired. ✷

148

8.2 The MRRW bound: A better upper bound

The MRRW bound (due to McEliece, Rodemich, Rumsey and Welch) is based on a linear pro-
gramming approach introduced by Delsarte to bound the rate of a code. The MRRW bound
is a better upper bound than the Elias-Bassalygo bound (though we will not state or prove the
bound in this book). However, there is a gap between the Gilbert-Varshamov (GV) bound and
the MRRW bound. The gap still exists to this day. To give one data point on the gap, consider
δ = 1
2 −ε (think of ε → 0), the GV bound gives a lower bound on R of Ω (
ε2) (see Proposition 3.3.5),
while the MRRW bound gives an upper bound on R of O (ε2 log ( 1
ε ))
.

8.3 A Breather

Let us now recap the combinatorial results that we have seen so far. Table 8.1 summarizes what
we have seen so far for binary codes in Shannon’s world and Hamming’s world (under both
unique and list decoding settings).

Shannon Hamming

BSCp Unique List

1-H
(p) is capacity R ≥ 1 − H (δ) 1 − H (p) is list decoding capacity
R ≤ M RRW
Explicit codes at capacity? Explicit Asymptotically good codes? Explicit codes at capacity?
Efﬁcient decoding algorithm? Efﬁcient decoding algorithms? Efﬁcient decoding algorithms?

Table 8.1: High level summary of results seen so far.

For the rest of the section, we remind the reader about the deﬁnition of explicit codes (Def-
inition 6.3.1) and strongly explicit codes (Deﬁnition 6.3.2).

We begin with BSCp . We have seen that the capacity of BSCp is 1 − H (p). The most nat-
ural open question is to obtain the capacity result but with explicit codes along with efﬁcient
decoding (and encoding) algorithms (Question 6.3.1).
Next we consider Hamming’s world under unique decoding. For large enough alphabets,
we have seen that Reed-Solomon codes (Chapter 5) meet the Singleton bound (Theorem 4.3.1).
Further, the Reed-Solomon codes are strongly explicit
1. The natural question then is

Question 8.3.1. Can we decode Reed-Solomon codes up to half its distance?

For smaller alphabets, especially binary codes, as we have seen in the last section, there is a
gap between the best known lower and upper bounds on the rate of a code with a given relative

1The proof is left as an exercise.
 149

distance. Further, we do not know of an explicit construction of a binary code that lies on the
GV bound. These lead to the following questions that are still wide open:

Open Question 8.3.1. What is the optimal trade-off between R and δ?

Open Question 8.3.2.

Does there exist an explicit construction of (binary) codes on the GV bound?

If we scale down our ambitions, the following is a natural weaker version of the second ques-
tion above:

Question 8.3.2. Do there exist explicit asymptotically good binary codes?

We also have the following algorithmic counterpart to the above question:

Question 8.3.3. If one can answer Question 8.3.2, then can we decode such codes efﬁciently
from a non-zero fraction of errors?

For list decoding, we have seen that the list decoding capacity is 1 − Hq (p). The natural
open questions are whether we can achieve the capacity with explicit codes (Question 7.4.1)
along with efﬁcient list decoding algorithms (Question 7.4.2).
In the remainder of the book, we will focus on the questions mentioned above (and sum-
marized in the last two rows of Table 8.1).

8.4 Bibliographic Notes

The McEliece-Rodemich-Rumsey-Welch (MRRW) bound was introduced in 1977 in the paper
[73].
 150

Part III

The Codes

151

Chapter 9

When Polynomials Save the Day:
Polynomial Based Codes

As we saw in Chapter 5, The Reed-Solomon codes give a remarkable family of codes with op-
timal dimension vs. distance tradeoff. They even match the Singleton bound (recall Theo-
rem 4.3.1), get k = n − d + 1 for a code of block length n, distance d and dimension k. However
they achieve this remarkable performance only over large alphabets, namely when the alpha-
bet size q ≥ n. In fact, so far in this book, we have not seen any explicit asymptotically good
code other than a Reed-Solomon code. This naturally leads to the following question (which is
a weaker form for Question 8.3.2):

Question 9.0.1. Do there exist explicit asymptotically good codes for small alphabets q ≪ n?

In this chapter we study an extension of Reed-Solomon codes, called the (generalized) Reed-
Muller codes, that lead to codes over smaller alphabets while losing in the dimension-distance
tradeoff (but under certain settings do answer Question 9.0.1 in the afﬁrmative).

The main idea is to extend the notion of functions we work with, to multivariate functions.
(See Exercise 5.2 for equivalence between certain Reed-Solomon codes and univariate func-
tions.) Just working with bivariate functions (functions on two variables), allows us to get codes
of block length n = q 2, and more variables can increase the length further for the same alpha-
bet size. We look at functions of total degree at most r . Analysis of the dimension of the code
reduces to simple combinatorics. Analysis of the distance follows from “polynomial-distance”
lemmas, whose use is ubiquitous in algebra, coding theory and computer science, and we de-
scribe these in the sections below. We start with the generic construction.

153

9.1 The generic construction

Recall that for a monomial Xd = X d1
1 · X d2
2 · · · X dm
m its total degree is d1 + d2 + · · · + dm. We next
extend this to the deﬁnition of the degree of a polynomial:

Deﬁnition 9.1.1. The total degree of a polynomial P (X) = ∑d cdXd over Fq (i.e. every cd ∈ Fq ) is
the maximum over d such that cd ̸= 0, of the total degree of Xd. We denote the total degree of P
by deg(P ).

For example, the degree of the polynomial 3X 3Y 4 + X 5 + Y 6 is 7.
In turns out that when talking about Reed-Muller codes, it is convenient to switch back and
forth between multivariate functions and multivariate polynomials. We can extend the notion
above to functions from Fm
q → Fq . For f : Fm
q → Fq let deg( f ) be the minimal degree of a polyno-
mial P ∈ Fq [X1, . . . , Xm] (where Fq [X1, . . . , Xm] denotes the set of all m-variate polynomials with
coefﬁcients from Fq ) such that f (α) = P (α) for every α ∈ Fm
q . Note that since (by Exercise 2.3) for
every a ∈ Fq we have aq − a = 0, it follows that a minimal degree polynomial does not contain
monomials with degree more than q − 1 any single variable. In what follows,

Deﬁnition 9.1.2. We use degXi (p) to denote the degree of polynomial p in variable Xi and
degXi ( f ) to denote the degree of (the minimal polynomial corresponding to) a function f in
variable Xi .

For example degX (3X 3Y 4 + X 5 + Y 6) = 5 and degY (3X 3Y 4 + X 5 + Y 6) = 6. Further, in this
notation we have for every function f : Fm
q → Fq , degXi ( f ) ≤ q − 1 for every i ∈ [m].
Reed-Muller codes are given by three parameters: a prime power q and positive integers m
and r , and consist of the evaluations of m-variate polynomials of degree at most r over all of
the domain Fm
q .

Deﬁnition 9.1.3 (Reed-Muller Codes). The Reed-Muller code with parameters q, m, r , denoted
RM(q, m, r ), is the set of evaluations of all m-variate polynomials in Fq [X1, . . . , Xm] of total de-
gree at most r and individual degree at most q − 1 over all points in Fm
q . Formally

RM(q, m, r ) def
= { f : Fm
q → Fq | deg( f ) ≤ r } .

For example consider the case of m = q = 2 and r = 1. Note that all bivariate polynomials
over F2 of degree at most 1 are 0, 1, X1, X2, 1 + X1, 1 + X2, X1 + X2 and 1 + X1 + X2. Thus, we have
that (where the evaluation points for (X1, X2) are ordered as (0, 0), (0, 1), (1, 0), (1, 1)):

RM(2, 2, 1) = {(0, 0, 0, 0), (1, 1, 1, 1), (0, 0, 1, 1), (0, 1, 0, 1), (1, 1, 0, 0), (1, 0, 1, 0), (0, 1, 1, 0), (1, 0, 0, 1)} .

Also note that RM(q, m, 1) is almost the Hadamard code (see Exercise 5.6).
The Reed-Muller code with parameters (q, m, r ) clearly has alphabet Fq and block length
n = q m. Also it can be veriﬁed that RM(q, m, r ) is a linear code (see Exercise 9.1.) This leads to
the following question, which will be the primary focus of this chapter:

154

Question 9.1.1. What are the dimension and distance of an RM(q, m, r ) code?

The dimension of the code is the number of m-variate monomials of degree at most r , with
the condition that degree in each variable is at most q − 1. No simple closed form expression
for this that works for all choices of q, m and r is known, so we will describe the effects only in
some cases. The distance analysis of these codes takes a little bit more effort and we will start
with two simple settings before describing the general result.

9.2 The low degree case

We start by considering RM(q, m, r ) when r < q, i.e., the degree is smaller than the ﬁeld size. We
refer to this setting as the “low-degree” setting.

Dimension. The dimension of RM(q, m, r ) in the low-degree case turns out to have a nice
closed form, since we do not have to worry about the constraint that each variable has degree
at most q − 1: this is already imposed by restricting the total degree to at most r ≤ q − 1. This
leads to a nice expression for the dimension:

Proposition 9.2.1. The dimension of the Reed Muller code RM(q, m, r ) equals (m+r
r ) when r < q.

Proof. The dimension equals the size of the set

D =
 {

(d1, . . . , dm) ∈ Zm|di ≥ 0 for all i ∈ [m], m∑

i =1 di ≤ r
 }
 , (9.1)

since for every (d1, . . . , dm) ∈ D, the monomial X d1
1 · · · X dm
m is a monomial of degree at most r and
these are all such monomials. The closed form expression for the dimension follows by a simple
counting argument. (See Exercise 9.2).

Distance. Next we turn to the analysis of the distance of the code. To understand the distance
we will ﬁrst state and prove a simple fact about the number of zeroes a multivariate polynomial
can have. (We will have three versions of this in this chapter - with the third subsuming the ﬁrst
(Lemma 9.2.2) and second (Lemma 9.3.1), but the ﬁrst two will be slightly simpler to state and
remember.)

Lemma 9.2.2 (Polynomial Zero Lemma (low-degree case)). Let f ∈ Fq [X1, . . . , Xm] be a non-zero
polynomial with deg( f ) ≤ r . Then the fraction of zeroes of f is at most r
q , i.e.,

|{a ∈ Fm
q | f (a) = 0}|

q m ≤ r
q .

155

We make couple of remarks. First note that the above lemma for m = 1 is the degree mantra
(Proposition 5.2.3). We note that for every m ≥ 1 the above lemma is tight (see Exercise 9.3).
However, there exists polynomials for which the lemma is not tight (see Exercise 9.4).

Proof of Lemma 9.2.2. Note that the lemma statement is equivalent to saying that the probabil-
ity that f (a) = 0 is at most deg( f )
q when a = (a1, . . . , am) is chosen uniformly at random from Fm
q .
We claim that this holds by induction on m.
We will prove the lemma by induction on m ≥ 1. Note that the base case follows from the
degree mantra (Proposition 5.2.3). Now consider the case of m > 1 (and we assume that the
lemma is true for m − 1). To apply inductive hypothesis we ﬁrst write f as a polynomial in Xm
with coefﬁcients that are themselves polynomials in X1, . . . , Xm−1. So let

f = f0X 0
m + f1X 1
m + . . . ft X t
m,

where each fi (X1, . . . , Xm−1) is a polynomial from Fq [X1, . . . , Xm−1] and deg( fi ) ≤ r − i . Further-
more let t be the largest index such that ft is not zero. Now we consider picking a ∈ Fm
q in two
steps: We ﬁrst pick (a1, . . . , am−1) uniformly at random from Fm−1
q , and then we pick am uni-
formly from Fq . Let

f (a1,...,am−1)(Xm) = f0(a1, . . . , am−1)X 0
m + · · · + . . . ft (a1, . . . , am−1)X t
m.

We consider two possible events:

E1 = {(a1, . . . , am)| ft (a1, . . . , am−1) = 0}

and E2 = {((a1, . . . , am)| ft (a1, . . . , am−1) ̸= 0 and f (a1,...,am−1)(am) = 0}.

By the inductive hypothesis, we have that

Pr [E1] ≤ r − t
q , (9.2)

since deg( ft ) ≤ r − t and ft ̸= 0.
For every (a1, . . . , am−1) ∈ Fm−1
q such that ft (a1, . . . , am−1) ̸= 0 we also have that the univariate
polynomial f (a1,...,am−1)(Xm) is non-zero and of degree at most t , and so by the degree mantra
it has at most t roots. It follows that for every such (a1, . . . , am−1) the probability, over am, that
f (a1,...,am−1)(am) = 0 is at most t
q . In turn, it now immediately follows that

Pr [E2] ≤ t
q . (9.3)

Finally, we claim that if neither E1 nor E2 occur, then f (a) ̸= 0. This is immediate from the deﬁ-
nitions of E1 and E2, since if f (a1, . . . , am) = 0, it must either be the case that ft (a1, . . . , am−1) = 0
(corresponding to E1) or it must be that ft (a1, . . . , am−1) ̸= 0 and f (a1,...,am−1)(am) = 0 (covered by
E2). Note that this implies that Pra[ f (a) = 0] ≤ Pr [E1 ∪ E2]. The lemma now follows from the fact
that Pr
a [ f (a) = 0] ≤ Pr [E1 ∪ E2] ≤ Pr [E1] + Pr [E2] ≤ r
q ,

where the second inequality follows from the union bound (Proposition 3.1.3) and the ﬁnal
inequality follows from (9.2) and (9.3).
 156

Comparison with other codes

The lemmas above, while quite precise may not be fully transparent in explaining the asymp-
totics of the performance of the Reed-Muller codes, or contrast them with other codes we have
seen. We mention a few basic facts here to get a clearer comparison.
If we set m = 1 and r = k − 1, then we get the Reed-Solomon codes evaluated on all of Fq
(see Chapter 5). If we set m = k − 1, r = 1 and q = 2, then we get family of extended Hadamard
codes (extended by including all Hadamard codewords and their complements). For more on
this, see Exercise 5.6.
Thus Reed-Muller codes generalize some previously known codes - some with large alpha-
bets and some with small alphabets. Indeed if we wish the alphabet to be small compared to
the block length, then we can pick m to be a constant. For instance if we choose m = 2, we get
codes of length n over an alphabets of size p
n, while for any choice of relative distance δ, the
code has rate (1−δ)2

2 . In general for larger values of m, the code has alphabet size n1/m and rate
(1−δ)m

m! . (See Exercise 9.5.) Thus for small values of m and ﬁxed positive distance δ < 1 there is
a rate R > 0 such that, by choosing q appropriately large, one get codes on inﬁnitely long block
length n and alphabet n1/m with rate R and distance δ, which answers Question 9.0.1 in the
afﬁrmative.
This is one of the simplest such families of codes with this feature. We will do better in later
in the book (e.g. Chapter 10), and indeed get alphabet size q independent of n with R > 0 and
δ > 0. But for now this is best we have.

9.3 The case of the binary ﬁeld

Next we turn to a different extreme of parameter choices for the Reed-Muller codes. Here we ﬁx
the alphabet size q = 2 and see what varying m and r gets us.
Since we will prove a stronger statement later in Lemma 9.4.1, we only state the distance of
the code RM(2, m, r ) below, leaving the proof to Exercise 9.6.

Lemma 9.3.1 (Polynomial distance (binary case)). Let f be a non-zero polynomial from F2[X1. . . . , Xm]
with degXi ( f ) ≤ 1 for every i ∈ [m]. Then |{a ∈ Fm
2 | f (a) ̸= 0}| ≥ 2m−deg( f ).

Further, it can be established that the bound in Lemma 9.3.1 is tight (see Exercise 9.7).
The dimension of the code is relatively straightforward to analyze. The dimension is again
given by the number of monomials of degree at most r . Since the degree in each variable is
either zero or one, this just equals the number of subsets of [m] of size at most r . Thus we have:

Proposition 9.3.2. For any r ≤ m, the dimension of the Reed-Muller code RM(2, m, r ) is exactly
∑r
i =0 (m
i )
.

Lemma 9.3.1 and Proposition 9.3.2 imply the following result:

Theorem 9.3.3. For every r ≤ m, the Reed-Muller code RM(2, m, r ) is a code of block length 2m,
dimension ∑r
i =0 (m
i ) and distance 2m−r .
 157

Again, to get a sense of the asymptotics of this code, we can ﬁx τ > 0 and set r = τ · m and
let m → ∞. In this case we get a code of block length n (for inﬁnitely many n) with rate roughly
n H (τ)−1 and distance n−τ (see Exercise 9.8). So both the rate and the distance tend to zero at a
rate that is a small polynomial in the block length but the code has a constant sized alphabet.
(Note that this implies that we have made some progress towards answering Question 8.3.2.)

9.4 The general case

We now turn to the general case, where q is general and r is allowed to be larger than q − 1. We
will try to analyze the dimension and distance of this code. The distance turns out to still have
a clean expression, so we will do that ﬁrst. The dimension does not have a simple expression
describing it exactly, so we will give a few lower bounds that may be generally useful (and are
often asymptotically tight).

9.4.1 The general case: Distance

Lemma 9.4.1 (Polynomial distance (general case)). Let f be a non-zero polynomial from Fq [X1. . . . , Xm]
with degXi ( f ) ≤ q − 1 for every i ∈ [m] and deg( f ) ≤ r . Furthermore, let s, t be the unique non-
negative integers such that t ≤ q − 2 and
 s(q − 1) + t = r.

Then |{a ∈ Fm
q | f (a) ̸= 0}| ≥ (q − t ) · q m−s−1 ≥ q m− r
q−1 .

Hence, RM(q, m, r ) has distance at least q m− r
q−1 .

Before proving the lemma we make a few observations: The above lemma clearly generalizes
both Lemma 9.2.2 (which corresponds to the case s = 0) and Lemma 9.3.1 (where q = 2, s = r −1
and t = 1). In the general case the second lower bound is a little simpler and it shows that the
probability that a polynomial is non-zero at a uniformly chosen point in Fm
q is at least q −r /(q−1).
Finally, we note that Lemma 9.4.1 is tight for all settings of parameters (see Exercise 9.9).

Proof of Lemma 9.4.1. The proof is similar to the proof of Lemma 9.2.2 except we take advan-
tage of the fact that the degree in a single variable is at most q − 1. We also need to prove some
simple inequalities.
As in the proof of Lemma 9.2.2 we prove that for a random choice of a = (a1, . . . , am) ∈ Fm
q ,
the probability that f (a) ̸= 0 is at least
 (q − t ) · q −(s+1). (9.4)

Note that in contrast to the proof of Lemma 9.2.2 we focus on the good events — the polynomial
being non-zero — rather than on the bad events.

158

We prove the lemma by induction on m. In the case of m = 1 we have by the degree mantra
(Proposition 5.2.3) that the probability that f (a1) ̸= 0 is at least q−r
q . If r < q − 1 we have s = 0
and t = r and so the expression in (9.4) satisﬁes

(q − t ) · q −1 = q − r
q ≤ Pr[ f (a1) ̸= 0].

If r = q − 1 we have s = 1 and t = 0, but then again we have that (9.4) equals

q · q −2 = q − (q − 1)
q ≤ Pr[ f (a1) ̸= 0],

where the inequality follows from the degree mantra.
Now we turn to the inductive step. Assume the hypothesis is true for (m − 1)-variate poly-
nomials and let f = ∑b
i =0 fi X i
m where fi ∈ Fq [X1, . . . , Xm−1] with fb ̸= 0. Note 0 ≤ b ≤ q − 1 and
deg( fb) ≤ r − b. Let E be the event of interest to us, i.e.,

E = {(a1, . . . , am)| f (a1, . . . , am) ̸= 0}.

Let E1 = {(a1, . . . , am−1)| fb(a1, . . . , am−1) ̸= 0}.

We ﬁrst bound Pr [E |E1]. Fix a1, . . . , am−1 such that fb(a1, . . . , am−1) ̸= 0 and let

P (Z ) = b∑

i =0 fi (a1, . . . , am−1)Z i .

Note P is a non-zero polynomial of degree b and we have

Pr[ f (a1, . . . , am) = 0|a1, . . . , am−1] = Pr
am[P (am) ̸= 0].

Since by the degree mantra, a univariate polynomial of degree b has at most b roots, we have

Pr
am[P (am) ̸= 0] ≥ q − b
q .

We conclude
 Pr [E |E1] ≥ 1 − b
q .

Next we will bound Pr [E1]. This will allow us to lower bound the probability of E since

Pr [E ] ≥ Pr [E and E1] = Pr [E1] · Pr [E |E1] .

Recall that deg( fb) ≤ r − b. Write r − b = s′(q − 1) + t ′ where s′, t ′ ≥ 0 and t ′ ≤ q − 2. By induction
we have Pr [E1] = Pr[ fb(a1, . . . , am−1) ̸= 0] ≥ (q − t ′) · q −(s′+1).

159

Putting the two bounds together, we get

Pr [E ] ≥ Pr [E |E1] · Pr [E1] ≥ q − b
q · (q − t ′) · q −(s′+1).

We are now left with a calculation to verify that the bound above is indeed lower bounded
by (q − t ) · q −(s+1) and we do so in Claim 9.4.2 using the facts that t , t ′ ≤ q − 2, b ≤ q − 1, r =
s(q − 1) + t , and r − b = s′(q − 1) + t ′. In the claim further below (Claim 9.4.3), we also prove
(q − t ) · q −(s+1) ≥ q −r /(q−1) and this concludes the proof of the lemma.

Claim 9.4.2. If q, r, s, t , s′, t ′, b are non-negative integers such that r = s(q − 1) + t , r − b = s′(q −
1) + t ′, t , t ′ ≤ q − 2 and b ≤ q − 1 then we have

q − b
q · (q − t ′) · q −(s′+1) ≥ (q − t ) · q −(s+1).

Proof. The proof breaks up in to two cases depending on s − s′. Note that an equivalent deﬁni-
tion of s and s′ are that these are the quotients when we divide r and r − b respectively by q − 1.
Since 0 ≤ b ≤ q − 1, it follows that either s′ = s or s′ = s − 1. We consider the two cases separately.
If s = s′ we have t = t ′ + b and then it sufﬁces to show that

q − b
q · (q − t ′) ≥ q − (t ′ + b).

In turn this is equivalent to showing

(q − b)(q − t ′) ≥ q(q − (t ′ + b)).

But this is immediate since the expression on the left is

(q − b)(q − t ′) = q 2 − (b + t ′)q + bt ′ = q(q − (b + t ′)) + bt ′ ≥ q(q − (b + t ′)),

where the ﬁnal inequality uses bt ′ ≥ 0.
If s = s′ + 1 we have a bit more work. Here we have t + q − 1 = t ′ + b and it sufﬁces to show
that q − b
q · (q − t ′) · q ≥ (q − t ) = (2q − (t ′ + b + 1)).

Write q −b = α and q − t ′ = β. The expression on the left above simpliﬁes to αβ and on the right
to α + β − 1. Since b, t ′ ≤ q − 1, we also have α, β ≥ 1. So it sufﬁces to show that αβ ≥ α + β − 1.
This is true since αβ = α + α(β − 1) and we have α(β − 1) ≥ β − 1 since α ≥ 1 and β − 1 ≥ 0.
We thus conclude that the inequality holds for both s = s′ and s = s′ + 1 and this yields the
claim.

Claim 9.4.3. Let q, r, s, t be non-negative real numbers such that q ≥ 2, r = s(q − 1) + t and t ≤
q − 2. Then (q − t ) · q −(s+1) ≥ q −r /(q−1).

160

We remark that while the inequality is quite useful, the proof below is not particularly in-
sightful. We include it for completeness, but we recommend that the reader skip it unless nec-
essary.

Proof of Claim 9.4.3. We have four parameters in the inequality above. We will simplify it in
steps removing parameters one at a time. First we get rid of r by substituting r = s(q − 1) + t . So
it sufﬁces to prove:
 (q − t ) · q −(s+1) ≥ q −(s(q−1)+t )/(q−1) = q −s · q −t /(q−1).

We can get rid of q −s from both sides (since the remaining terms are non-negative) and so it
sufﬁces to prove: q − t
q ≥ q −t /(q−1).

Let fq (t ) = t
q + q −t /(q−1) − 1. The inequality above is equivalent to proving fq (t ) ≤ 0 for 0 ≤ t ≤
q − 2. We use some basic calculus to prove the above. Note that the ﬁrst and second derivatives
of fq with respect to t are given by f ′
q (t ) = 1
q − ln q
q−1 q −t /(q−1) and f ′′
q (t ) = (
ln(q)/(q − 1))2 q −t /(q−1).
In particular the second derivative is always positive which means fq (t ) is maximized at one of
the two end points of the interval t ∈ [0, q − 2]. We have fq (0) = 0 ≤ 0 as desired and so it sufﬁces
to prove that
 fq (q − 2) = q −(q−2)/(q−1) − 2
q ≤ 0.

Multiplying the expression above by q we have that it sufﬁces to show q 1/(q−1) ≤ 2 which in
turn is equivalent to proving q ≤ 2q−1 for every q ≥ 2. The ﬁnal inequality follows easily from
Bernoulli’s inequality (Lemma B.1.4) 1 + kx ≤ (1 + x)k which holds for every x ≥ −1 and k ≥ 1. In
our case we substitute x = 1 and k = q − 1 to conclude q ≤ 2q−1 as desired.

9.4.2 The general case: Dimension

For integers q, m, r let

Sq,m,r =
 {
d = (d1, . . . , dm) ∈ Zm|0 ≤ di ≤ q − 1 for all i ∈ [m] and , m∑

i =1 di ≤ r
 }
 (9.5)

and let Kq,m,r = |Sq,m,r |.

We start with the following, almost tautological, proposition.

Proposition 9.4.4. For every prime power q and integers m ≥ 1 and r ≥ 0, the dimension of the
code RM(q, m, r ) is Kq,m,r .

Proof. Follows from the fact that for every d = (d1, . . . , dm) ∈ Sq,m,r the associated monomial

Xd = X d1
1 · · · X dm
m is a monomial of degree at most r and individual degree at most q − 1. Thus
these monomials (i.e., their evaluations) form a basis for the Reed-Muller code RM(q, m, r ). (See
Exercise 9.10.)
 161

The deﬁnition of Kq,m,r does not give a good hint about its growth so below we give a few
bounds on Kq,m,r that help estimate its growth. Speciﬁcally the proposition below gives a lower
bound K −
q,m,r and an upper bound K +
q,m,r on Kq,m,r that are (1) given by simple expressions and
(2) within polynomial factors of each other for every setting of q, m, and r .

Proposition 9.4.5. For integers q ≥ 2, m ≥ 1 and r ≥ 0, let

K +
q,m,r ≜ min
 {
q m,
 (m + r
r
 )}

and let
 K −
q,m,r ≜
 { max {q m/2, q m − K +
q,m,(q−1)m−r
 } if r ≥ (q − 1)m/2

max {(m
r )
, 1
2 (⌊ 2r +m
m ⌋)m} if r < (q − 1)m/2

Then there are universal constants c1, c2 (c1 < 3.1 and c2 < 8.2 sufﬁce) such that

K −
q,m,r ≤ Kq,m,r ≤ K +
q,m,r ≤ c1 · (K −
q,m,r )c2

.

Proof. We tackle the inequalities in order of growing complexity of the proof. In our bounds we
use the fact that Kq,m,r is monotone non-decreasing in q as well as r (when other parameters
are ﬁxed)– see Exercise 9.11.
First we prove Kq,m,r ≤ K +
q,m,r . On the one hand we have

Kq,m,r ≤ Kq,m,(q−1)m = q m,

which follows by ignoring the total degree restriction and on the other hand we have

Kq,m,r ≤ Kr,m,r =
 (m + r
r
 )

,

whereas here we ignored the individual degree restriction.
Next we show K −
q,m,r ≤ Kq,m,r . First we consider the case r ≥ (q − 1)m/2. Here we argue

via symmetry. Consider a map that maps vectors d = (d1, . . . , dm) ∈ Zm with 0 ≤ di < q to d =
(q − 1 − d1, . . . , q − 1 − dm). The map d → d is a one-to-one map which maps vectors with ∑i di >
r to vectors with ∑
i di < (q − 1)m − r . In other words either d ∈ {0, . . . , q − 1}m is in Sq,m,r or
d ∈ Sq,m,(q−1)m−r , thus establishing

Kq,m,r = q m − Kq,m,(q−1)m−r .

Since r ≥ (q − 1)m/2 we have (q − 1)m − r ≤ r and so

Kq,m,r ≥ Kq,m,(q−1)m−r ,

which in turn implies Kq,m,r ≥ q m/2.

162

This establishes Kq,m,r ≥ K −
q,m,r when r ≥ (q − 1)m/2. Next, turning to the case r < (q − 1)m/2,
ﬁrst let q ′ = ⌊ 2r +m
m ⌋. We have Kq,m,r ≥ Kq ′,m,r ≥ (q ′)m/2

since r ≥ (q ′ − 1)m/2, and this yields

Kq,m,r ≥ (q ′)m/2 = 1
2
 (⌊ 2r + m
m
 ⌋)m .

Finally we also have
 Kq,m,r ≥ K2,m,r = r∑

i =0
 (m
i
 )
 ≥
 (
m
r
 )
,

thus establishing Kq,m,r ≥ K −
q,m,r when r < (q − 1)m/2.
Finally we turn to the inequalities showing K +
q,m,r ≤ c1 · (K −
q,m,r )c2. If r ≥ (q − 1)m/2 we have

q m

2 ≤ K −
q,m,r ≤ K +
q,m,r ≤ q m

establishing K +
q,m,r ≤ 2K −
q,m,r . Next we consider the case r < m/2. In this case we have

K −
q,m,r ≥
 (
m
r
 )
 ≥ (m/r )r ≥ 2r .

On the other hand we also have
(m + r
r
 )
 ≤ ( e(m + r )
r
 )r ≤ ( e · (3/2) · m
r
 )r = ( 3e
2
 )r · ( m
r
 )r .

From 2r ≤ K −
q,m,r we get ( 3e
2 )r ≤ (K −
q,m,r )log2(3e/2). Combining with ( m
r )r ≤ K −
q,m,r and K +
q,m,r ≤
(m+r
r ) we get
 K +
q,m,r ≤ ( 3e
2
 )r · ( m
r
 )r ≤ (K −
q,m,r )1+log2(3e/2)

. Finally, we consider the case m/2 ≤ r < (q − 1)m/2. In this range we have
⌊ 2r + m
m
 ⌋ = 1 + ⌊ 2r
m
 ⌋ ≥ 1 + r
m = m + r
m .

Thus
 K −
q,m,r ≥ 1
2
 (⌊ 2r + m
m
 ⌋)m ≥ 1
2
 ( m + r
m
 )m ≥ 1
2
 ( 3
2
 )m .

On the other hand we have

K +
q,m,r ≤
 (
m + r
m
 )
 ≤ ( e(m + r )
m
 )m = em · ( m + r
m
 )m .

Again we have ( m+r
m )m ≤ 2K −
q,m,r and em ≤ (2K −
q,m,r )log2(3e/2) and so K +
q,m,r ≤ (2K −
q,m,r )1+log2(3e/2).
Thus in all cases we have K +
q,m,r ≤ c1 · (K −
q,m,r )c2 for c2 = 1 + log2(3e/2) < 3.1 and c1 = 2c2 < 8.2, as
desired.
 163

We now give a few examples of codes that can be derived from the bounds above, to illus-
trate the variety offered by Reed-Muller codes. In each of the cases we set one or more of the
parameters among alphabet size, rate, (relative) distance or absolute distance to a constant and
explore the behavior in the other parameters. In all cases we use Lemma 9.4.1 to lower bound
the distance and Proposition 9.4.5 to lower bound the dimension.

Example 9.4.6 (RM Codes of constant alphabet size and (relative) distance.). Fix q and r < q −1
and consider m → ∞. Then the Reed-Muller codes RM(q, m, r ) are [N , K , D]q codes with block
length N = q m, distance D = δ · N for δ = 1 − r /q, with dimension

K ≥
 (m
r
 )
 ≥
 ( logq N

r
 )r .

In other words Reed-Muller codes yield codes of constant alphabet size and relative distance with
dimension growing as an arbitrary polynomial in the logarithm of the block length.

Example 9.4.7 (Binary RM Codes of rate close to 1 with constant (absolute) distance.). Fix q = 2
and d and let m → ∞. Then the Reed-Muller codes RM(2, m, m − d ) are [N , K , D]2 codes with
N = 2m, D = 2d and
 K ≥ N −
 (log2 N + d
d
 )
 ≥ N − (log2 N )d .

(See Exercise 9.12 for bound on K .) Note that the rate → 1 as N → ∞.

Example 9.4.8 (RM codes of constant rate and relative distance over polynomially small al-
phabets.). Given any ε > 0 and let m = ⌈ 1
ε ⌉ and now consider q → ∞ with r = q/2. Then the
Reed-Muller codes RM(q, m, r ) are [N , K , D]q codes with N = q m, D = N
2 and

K ≥ 1
2
 ( q + m
m
 )m ≥ 1
2mm · N .

Expressed in terms of N and ε, the codes have length N , dimension Ω (
ε1/ε) · N and relative dis-
tance 1/2 over an alphabet of size N ε.

Another natural regime is to consider the case of constant rate 1/2: see Exercise 9.13 for
more.
Finally we mention a range of parameters that has been very useful in the theory of com-
puter science. Here the alphabet size is growing with N , but very slowly. But the code has a ﬁxed
relative distance and dimension that is polynomially related to the block length.

Example 9.4.9 (RM Codes over polylogarithmic alphabets with polynomial dimension.). Given
0 < ε < 1, let q → ∞ and let r = q/2 and m = q ε. Then the Reed-Muller codes RM(q, m, r ) are
[N , K , D]q codes with N = q m, D = N
2 and

K ≥ 1
2
 ( q + m
m
 )m ≥ 1
2
 (q 1−ε)m = 1
2 · N 1−ε.

Expressed in terms of N and ε, the codes have length N , dimension Ω(N 1−ε) and relative distance
1/2 over an alphabet of size (log N )1/ε. (See Exercise 9.14 for claim on the bound on q.)

164

9.5 Exercises

Exercise 9.1. Argue that any RM(q, m, r ) is a linear code.

Exercise 9.2. Argue that for D as deﬁned in (9.1), we have

|D| =
 (
m + r
r
 )
.

Exercise 9.3. Show that Lemma 9.2.2 is tight in the sense that for every prime power q and inte-
gers m ≥ 1 and 1 ≤ r ≤ q − 1, there exists a polynomial with exactly r · q m−1 roots.

Exercise 9.4. Show that Lemma 9.2.2 is not tight for most polynomials. In particular show
that for every prime power q and integers m ≥ 1 and 1 ≤ r ≤ q − 1, a random polynomial in
Fq [X1, . . . , Xm] of degree r has q m−1 expected number of roots.

Exercise 9.5. Show that the Reed-Muller codes of Section 9.2 give rise to codes of relative dis-
tance δ (for any 0 < δ < 1) and block length n such that they have alphabet size of mpn and rate
(1−δ)m

m! .

Exercise 9.6. Prove Lemma 9.3.1.

Exercise 9.7. Prove that the lower bound in Lemma 9.3.1 is tight.

Exercise 9.8. Show that there exists a binary RM code with block length n, rate n H (τ)−1 and
relative distance n−τ for any 0 < τ < 1/2.

Exercise 9.9. Prove that the (ﬁrst) lower bound in Lemma 9.4.1 is tight for all settings of the
parameters.

Exercise 9.10. Prove that the evaluations of Xd for every d ∈ Sq,m,r (as in (9.5)) form a basis for
RM(q, m, r ).

Exercise 9.11. Argue that Kq,m,r is monotone non-decreasing in q as well as r (when other pa-
rameters are ﬁxed).

Exercise 9.12. Argue the claimed bound on K in Example 9.4.7.

Exercise 9.13. Figure out a RM code that has rate 1
2 and has as large a distance as possible and
as small an alphabet as possible.

Exercise 9.14. Prove the claimed bound on q in Example 9.4.9.

Exercise 9.15. In this problem we will talk about the dual of Reed-Muller codes, which turn out
to be Reed-Muller codes (with a different degree) themselves. We do so in a sequence of sub-
problems:

1. Show that for 1 ≤ j ≤ q − 1 ∑

α∈Fq α j ̸= 0

if and only if j = q − 1.

Hint: Use Exercise 2.2.
 165

2. Argue that for any m ≥ 1 and 1 ≤ j1, . . . , jm ≤ q − 1,

∑

(c1,...,cm )∈Fm
q
 m∏

i =1 c j1
i = 0

if and only if j1 = j2 = · · · = jm = q − 1.

3. Using the above or otherwise, show that for any 0 ≤ r < (q − 1) − s, we have

RM(q, m, r )⊥ = RM(q, m, m(q − 1) − r − 1).

9.6 Bibliographic Notes

We point out that the original code considered by Reed and Muller is the one in Section 9.3.

166

Chapter 10

From Large to Small Alphabets: Code
Concatenation

Recall Question 8.3.2 that we had asked before: Is there an explicit asymptotically good binary
code (that is, rate R > 0 and relative distance δ > 0)? In this chapter, we will consider this ques-
tion when we think of explicit code in the sense of Deﬁnition 6.3.1 as well as the stronger notion
of a strongly explicit code (Deﬁnition 6.3.2).
Let us recall all the (strongly) explicit codes that we have seen so far. (See Table 10.1 for an
overview.)
 Code R δ

Hamming 1 − O ( log n
n
 ) O ( 1
n )

Hadamard O ( log n
n
 ) 1
2
Reed-Solomon 1
2 O ( 1
log n
 )

Table 10.1: Strongly explicit binary codes that we have seen so far.

Hamming code (Section 2.4), which has rate R = 1 − O(log n/n) and relative distance δ =
O(1/n) and the Hadamard code (Section 2.7), which has rate R = O(log n/n) and relative dis-
tance 1/2. Both of these codes have extremely good R or δ at the expense of the other param-
eter. Next, we consider the Reed-Solomon code (of say R = 1/2) as a binary code, which does
much better– δ = 1
log n , as we discuss next.

Consider the Reed-Solomon over F2s for some large enough s. It is possible to get an [
n, n
2 , n
2 + 1]

2s
Reed-Solomon code (i.e. R = 1/2). We now consider a Reed-Solomon codeword, where every
symbol in F2s is represented by an s-bit vector. Now, the “obvious” binary code created by view-
ing symbols from F2s as bit vectors as above is an [ns, ns
2 , n
2 + 1]

2 code
1. Note that the distance

of this code is only Θ ( N
log N
 )
, where N = ns is the block length of the ﬁnal binary code. (Recall
that n = 2s and so N = n log n.)

1The proof is left as an exercise.
 167

The reason for the (relatively) poor distance is that the bit vectors corresponding to two
different symbols in F2s may only differ by one bit. Thus, d positions which have different F2s
symbols might result in a distance of only d as bit vectors.
To ﬁx this problem, we can consider applying a function to the bit-vectors to increase the
distance between those bit-vectors that differ in smaller numbers of bits. Note that such a func-
tion is simply a code! We deﬁne this recursive construction more formally next. This recursive
construction is called concatenated codes and will help us construct (strongly) explicit asymp-
totically good codes.

10.1 Code Concatenation

For q ≥ 2, k ≥ 1 and Q = q k , consider two codes which we call outer code and inner code:

Cout : [Q]
K → [Q]N ,

Cin : [q]
k → [q]
n.

Note that the alphabet size of Cout exactly matches the number of messages for Cin. Then given
m = (m1, . . . , mK ) ∈ [Q]
K , we have the code Cout ◦Cin : [q]
kK → [q]
nN deﬁned as

Cout ◦Cin(m) = (Cin(Cout(m)1), . . . ,Cin(Cout(m)N )) ,

where Cout(m) = (Cout(m)1, . . . ,Cout(m)N ) .

This construction is also illustrated in Figure 10.1.
 Cin

m1 m2 mK

Cout(m)1 Cout(m)2 Cout(m)N

Cin (Cout(m)1) Cin (Cout(m)2) Cin (Cout(m)N )

Cout

Cin Cin

Figure 10.1: Concatenated code Cout ◦Cin.

We now look at some properties of a concatenated code.

Theorem 10.1.1. If Cout is an (N , K , D)q k code and Cin is an (n, k, d )q code, then Cout ◦ Cin is an
(nN , kK , d D)q code. In particular, if Cout (Cin resp.) has rate R (r resp.) and relative distance δout
(δin resp.) then Cout ◦Cin has rate Rr and relative distance δout · δin.

168

Proof. The ﬁrst claim immediately implies the second claim on the rate and relative distance of
Cout ◦ Cin. The claims on the block length, dimension and alphabet of Cout ◦ Cin follow from the
deﬁnition.2 Next we show that the distance is at least d D. Consider arbitrary m1 ̸= m2 ∈ [Q]
K .
Then by the fact that Cout has distance D, we have

∆ (Cout (m1) ,Cout (m2)) ≥ D. (10.1)

Thus for each position 1 ≤ i ≤ N that contributes to the distance above, we have

∆ (
Cin (
Cout (m1)i ) ,Cin (
Cout (m2)i )) ≥ d , (10.2)

as Cin has distance d . Since there are at least D such positions (from (10.1)), (10.2) implies

∆ (Cout ◦Cin (m1) ,Cout ◦Cin (m2)) ≥ d D.

The proof is complete as the choices of m1 and m2 were arbitrary.

If Cin and Cout are linear codes, then so is Cout ◦ Cin, which can be proved for example, by
deﬁning a generator matrix for Cout ◦Cin in terms of the generator matrices of Cin and Cout. The
proof is left as an exercise.

10.2 Zyablov Bound

We now instantiate an outer and inner codes in Theorem 10.1.1 to obtain a new lower bound on
the rate given a relative distance. We’ll initially just state the lower bound (which is called the
Zyablov bound) and then we will consider the explicitness of such codes.
We begin with the instantiation of Cout. Note that this is a code over a large alphabet and
we have seen an optimal code over large enough alphabet: Reed-Solomon codes (Chapter 5).
Recall that the Reed-Solomon codes are optimal because they meet the Singleton bound 4.3.1.
Hence, let us assume that Cout meets the Singleton bound with rate of R, i.e. Cout has relative
distance δout > 1 − R. Note that now we have a chicken and egg problem here. In order for
Cout ◦ Cin to be an asymptotically good code, Cin needs to have rate r > 0 and relative distance
δin > 0 (i.e. Cin also needs to be an asymptotically good code). This is precisely the kind of code
we are looking for to answer Question 8.3.2! However the saving grace will be that k can be
much smaller than the block length of the concatenated code and hence, we can spend “more"
time searching for such an inner code.
Suppose Cin meets the GV bound (Theorem 4.2.1) with rate of r and thus with relative dis-
tance δin ≥ H −1
q (1 − r ) − ε, for some ε > 0. Then by Theorem 10.1.1, Cout ◦ Cin has rate of r R and
δ = (1 − R)(H −1
q (1 − r ) − ε). Expressing R as a function of δ and r , we get the following:

R = 1 − δ

H −1
q (1 − r ) − ε .

2Technically, we need to argue that the q kK messages map to distinct codewords to get the dimension of kK .
However, this follows from the fact, which we will prove soon, that Cout ◦ Cin has distance d D ≥ 1, where the in-
equality follows for d , D ≥ 1.
 169

 0

 0.2

 0.4

 0.6

 0.8

 1
  0  0.2  0.4  0.6  0.8  1R
δ
 GV bound
Zyablov bound

Figure 10.2: The Zyablov bound for binary codes. For comparison, the GV bound is also plotted.

Then optimizing over the choice of r , we get that the rate of the concatenated code satisﬁes

R ≥ max
0<r <1−Hq (δ+ε) r
 (

1 − δ

H −1
q (1 − r ) − ε
 )
 ,

where the bound of r < 1 − Hq (δ + ε) is necessary to ensure that R > 0. This lower bound on the
rate is called the Zyablov bound. See Figure 10.2 for a plot of this bound for binary codes.
To get a feel for how the bound behaves, consider the case when δ = 1
2 − ε. We claim that
the Zybalov bound states that R ≥ Ω(ε3). (Recall that the GV bound for the same δ has a rate of
Ω(ε2).) The proof of this claim is left as an exercise.
Note that the Zyablov bound implies that for every δ > 0, there exists a (concatenated) code
with rate R > 0. However, we already knew about the existence of an asymptotically good code
by the GV bound (Theorem 4.2.1). Thus, a natural question to ask is the following:

Question 10.2.1. Can we construct an explicit code on the Zyablov bound?

We will focus on linear codes in seeking an answer to the question above because linear codes
have polynomial size representation. Let Cout be an [N , K ]Q Reed-Solomon code where N =
Q − 1 (evaluation points being F∗
Q with Q = q k ). This implies that k = Θ(log N ). However we still
need an efﬁcient construction of an inner code that lies on the GV bound. We do not expect
to construct such a Cin in time poly(k) as that would answer Open Question 8.3.2! However,
since k = O(log N ), note that an exponential time in k algorithm is still a polynomial (in N ) time
algorithm.
There are two options for this exponential (in k) time construction algorithm for Cin:

170

• Perform an exhaustive search among all generator matrices for one satisfying the required
property for Cin. One can do this because the Varshamov bound (Theorem 4.2.1) states
that there exists a linear code which lies on the GV bound. This will take qO(kn) time.
Using k = r n (or n = O(k)), we get qO(kn) = qO(k2) = N O(log N ), which is upper bounded by
(nN )
O(log(nN )), a quasi-polynomial time bound.

• The second option is to construct Cin in qO(n) time and thus use (nN )
O(1) time overall. See
Exercise 10.1 for one way to construct codes on the GV bound in time qO(n).

Thus,

Theorem 10.2.1. We can construct a code that achieves the Zyablov bound in polynomial time.

In particular, we can construct explicit asymptotically good code in polynomial time, which
answers Question 10.2.1 in the afﬁrmative.
A somewhat unsatisfactory aspect of this construction (in the proof of Theorem 10.2.1) is
that one needs a brute force search for a suitable inner code (which led to the polynomial con-
struction time). A natural followup question is

Question 10.2.2. Does there exist a strongly explicit asymptotically good code?

10.3 Strongly Explicit Construction

We will now consider what is known as the Justesen code. The main insight in these codes is that
if we are only interested in asymptotically good codes, then the arguments in the previous sec-
tion would go through even if (i) we pick different inner codes for each of the N outer codeword
positions and (ii) most (but not necessarily all) inner code lie on the GV bound. It turns out that
constructing an “ensemble" of codes such that most of the them lie on the GV bound is much
easier than constructing a single code on the GV bound. For example, the ensemble of all linear
codes have this property– this is exactly what Varshamov proved. However, it turns out that we
need this ensemble of inner codes to be a smaller one than the set of all linear codes.
Justesen code is concatenated code with multiple, different linear inner codes. Speciﬁcally,
it is composed of an (N , K , D)q k outer code Cout and different inner codes C i
in : 1 ≤ i ≤ N . For-
mally, the concatenation of these codes, denoted by Cout ◦ (
C 1
in, . . . ,C N
in)
, is deﬁned as follows:

given a message m ∈ [q k ]K , let the outer codeword be denoted by (c1, . . . , cN ) def
= Cout(m). Then
Cout ◦ (
C 1
in, . . . ,C N
in) (m) = (
C 1
in(c1),C 2
in(c2), . . . ,C n
in(cN ))
.
We will need the following result.

Theorem 10.3.1. Let ε > 0. There exists an ensemble of inner codes C 1
in,C 2
in, . . . ,C N
in of rate 1
2 , where
N = q k − 1, such that for at least (1 − ε)N values of i , C i
in has relative distance ≥ H −1
q ( 1
2 − ε)
.

171

In fact, this ensemble is the following: for α ∈ F∗
q k , the inner code C α
in : Fk
q → F2k
q is deﬁned as

C α
in(x) = (x, αx). This ensemble is called the Wozencraft ensemble. We claim that C α
in for every
α ∈ F∗
q k is linear and is strongly explicit. (The proof if left as an exercise.)

10.3.1 Justesen code

For the Justesen code, the outer code Cout is a Reed-Solomon code evaluated over F∗
q k of rate

R, 0 < R < 1. The outer code Cout has relative distance δout = 1 − R and block length of N =
q k − 1. The set of inner codes is the Wozencraft ensemble {C α
in}α∈F∗
qk from Theorem 10.3.1. So

the Justesen code is the concatenated code C ∗ def
= Cout ◦ (C 1
in,C 2
in, . . . ,C N
in) with the rate R
2 . The
following proposition estimates the distance of C ∗.

Proposition 10.3.2. Let ε > 0. C ∗ has relative distance at least (1 − R − ε) · H −1
q ( 1
2 − ε)

Proof. Consider m1 ̸= m2 ∈ (Fq k )K . By the distance of the outer code |S| ≥ (1 − R)N , where

S = {
i |Cout(m1)i ̸= Cout(m2)i } .

Call the i th inner code good if C i
in has distance at least d def
= H −1
q ( 1
2 − ε)·2k. Otherwise, the inner
code is considered bad. Note that by Theorem 10.3.1, there are at most εN bad inner codes. Let
Sg be the set of all good inner codes in S, while Sb is the set of all bad inner codes in S. Since
Sb ≤ εN , |Sg | = |S| − |Sb| ≥ (1 − R − ε)N . (10.3)

For each good i ∈ S, by deﬁnition we have

∆ (
C i
in (
Cout (
m1)

i ) ,C i
in (
Cout (
m2)

i )) ≥ d . (10.4)

Finally, from (10.3) and (10.4), we obtain that the distance of C ∗ is at least

(1 − R − ε) · N d = (1 − R − ε)H −1
q
 ( 1
2 − ε) N · 2k,

as desired.

Since the Reed-Solomon codes as well as the Wozencraft ensemble are strongly explicit, the
above result implies the following:

Corollary 10.3.3. The concatenated code C ∗ from Proposition 10.3.2 is an asymptotically good
code and is strongly explicit.

Thus, we have now satisfactorily answered Question 10.2.2 modulo Theorem 10.3.1, which
we prove next.
 172

Proof of Theorem 10.3.1. Fix y = (y1, y2) ∈ F2k
q \{0}. Note that this implies that y1 = 0 and y2 = 0
are not possible. We claim that y ∈ C α
in for at most one α ∈ F∗
2k . The proof is by a simple case
analysis. First, note that if y ∈ C α
in, then it has to be the case that y2 = α · y1.

• Case 1: y1 ̸= 0 and y2 ̸= 0, then y ∈ C α
in, where α = y2
y1 .

• Case 2: y1 ̸= 0 and y2 = 0, then y ∉ C α
in for every α ∈ F∗
2k (as αy1 ̸= 0 since product of two
elements in F∗
2k also belongs to F∗
2k ).

• Case 3: y1 = 0 and y2 ̸= 0, then y ∉ C α
in for every α ∈ F∗
2k (as αy1 = 0).

Now assume that w t (y) < H −1
q (1 − ε)n. Note that if y ∈ C α
in, then C α
in is “bad”(i.e. has relative
distance < H −1
q ( 1
2 − ε)
). Since y ∈ C α
in for at most one value of α, the total number of bad codes
is at most
 ∣
{
y|w t (y) < H −1
q
 ( 1

2 − ε) · 2k}∣ ≤ V olq
 (H −1
q
 ( 1

2 − ε) · 2k, 2k)

≤ q Hq (H −1
q ( 1
2 −ε))·2k (10.5)

= q ( 1
2 −ε)·2k

= q k

q 2εk

< ε(q k − 1) (10.6)

= εN . (10.7)

In the above, (10.5) follows from our good old upper bound on the volume of a Hamming ball
(Proposition 3.3.1) while (10.6) is true for large enough k. Thus for at least (1 − ε)N values of α,
C α
in has relative distance at least H −1
q ( 1
2 − ε)
, as desired. ✷

By concatenating an outer code of distance D and an inner code of distance d , we can ob-
tain a code of distance at least ≥ Dd (Theorem 10.1.1). Dd is called the concatenated code’s de-
sign distance. For asymptotically good codes, we have obtained polynomial time construction
of such codes (Theorem 10.2.1, as well as strongly explicit construction of such codes (Corol-
lary 10.3.3). Further, since these codes were linear, we also get polynomial time encoding. How-
ever, the following natural question about decoding still remains unanswered.

Question 10.3.1. Can we decode concatenated codes up to half their design distance in poly-
nomial time?
 173

10.4 Exercises

Exercise 10.1. In Section 4.2.1, we saw that the Gilbert construction can compute an (n, k)q code
in time qO(n). Now the Varshamov construction (Section 4.2.2) is a randomized construction
and it is natural to ask how quickly can we compute an [n, k]q code that meets the GV bound.
In this exercise, we will see that this can also be done in qO(n) deterministic time, though the
deterministic algorithm is not that straight-forward anymore.

1. (A warmup) Argue that Varshamov’s proof gives a qO(kn) time algorithm that constructs
an [n, k]q code on the GV bound. (Thus, the goal of this exercise is to “shave" off a factor
of k from the exponent.)

2. A k ×n Toeplitz Matrix A = {Ai , j }k , n
i =1, j =1 satisﬁes the property that Ai , j = Ai −1, j −1. In other
words, any diagonal has the same value. For example, the following is a 4 × 6 Toeplitz
matrix: 





 1 2 3 4 5 6
7 1 2 3 4 5
8 7 1 2 3 4
9 8 7 1 2 3
 






A random k × n Toeplitz matrix T ∈ Fk×n
q is chosen by picking the entries in the ﬁrst row
and column uniformly (and independently) at random.

Prove the following claim: For any non-zero m ∈ F
k
q , the vector m · T is uniformly dis-
tributed over Fn
q , that is for every y ∈ Fn
q , Pr [m · T = y
] = q −n.

(Hint: Write down the expression for the value at each of the n positions in the vector m·T
in terms of the values in the ﬁrst row and column of T . Think of the values in the ﬁrst row
and column as variables. Then divide these variables into two sets (this “division" will
depend on m) say S and S. Then argue the following: for every ﬁxed y ∈ Fn
q and for every

ﬁxed assignment to variables in S, there is a unique assignment to variables in S such that
mT = y.)

3. Brieﬂy argue why the claim in part (b) implies that a random code deﬁned by picking its
generator matrix as a random Toeplitz matrix with high probability lies on the GV bound.

4. Conclude that an [n, k]q code on the GV bound can be constructed in time 2
O(k+n).

10.5 Bibliographic Notes

Code concatenation was ﬁrst proposed by Forney[30].
Justesen codes were constructed by Justesen [58]. In his paper, Justesen attributes the Wozen-
craft ensemble to Wozencraft.
 174

Chapter 11

Information Theory Strikes Back: Polar
Codes

We begin by recalling Question 13.4.1, which we re-produce for the sake of completeness:

Question 11.0.1. Can we get to within ε of capacity for BSCp (i.e. rate 1− H (p)−ε) via codes
with block length and decoding times that are poly(1/ε)?

In this chapter we introduce Polar codes, a class of codes developed from purely information-
theoretic insights. We then show how these codes lead to a resolution of Question 11.0.1, namely
how to get arbitrarily close to capacity on the binary symmetric channel with block length, and
decoding complexity growing polynomially in the inverse of the gap to capacity. This answers
in the afﬁrmative one of the most crucial questions in the Shannon setting.

This chapter is organized as follows. We deﬁne the precise question, after some simpliﬁ-
cation, in Section 11.1. In the same section, we discuss why the simpliﬁed question solves a
much more general problem. We then switch the problem from an error-correction question to
a linear-compression question in Section 11.2. This switch is very straightforward but very use-
ful in providing insight into the working of Polar codes. In Section 11.3 we introduce the idea of
polarization, which provides the essential insight to Polar codes. (We remark that this section
onwards is based on notions from Information Theory. The reader unfamiliar with the theory
should ﬁrst consult Appendix E to get familiar with the basic concepts.) In Section 11.4 we then
give a complete description of the Polar codes, and describe the encoding and decoding algo-
rithms. In Section 11.5 we then describe the analysis of these codes. We remark that the only
complex part of this chapter is this analysis and the construction and algorithms themselves
are quite simple (and extremely elegant) modulo this analysis.

175

11.1 Achieving Gap to Capacity

The goal of this section is to present a simple question that formalizes what it means to achieve
capacity with polynomial convergence, and to explain why this is the right question (and how
answering this positively leads to much more powerful results by standard methods).
Recall that for p ∈ [0, 1/2) the BSCp is the channel that takes as input a sequence of bits X =
(X1, . . . , Xn) and outputs the sequence Y = (Y1, . . . , Yn) where for each i , Xi = Yi with probability
1 − p and Xi ̸= Yi with probability p; and this happens independently for each i ∈ {1, . . . , n}. We
use the notation Z = (Z1, . . . , Zn) ∈ Bern(p)n to denote the error pattern, so that Y = X + Z.
Our target for this chapter is to prove the following theorem:

Theorem 11.1.1. For every p ∈ [0, 1/2) there is a polynomial n0(·) such that for every ε > 0 there
exist k, n and an encoder E : Fk
2 → Fn
2 and decoder D : Fn
2 → Fk
2 satisfying the following conditions:

Length and Rate The codes are short, and the rate is close to capacity, speciﬁcally, 1/ε ≤ n ≤
n0(1/ε) and k ≥ (1 − H (p) − ε) · n.

Running times The encoder and decoder run in time O(n log n) (where the O(·) notation hides a
universal constant independent of p and ε).

Failure Probability The probability of incorrect decoding is at most ε. Speciﬁcally, for every m ∈
Fk
2 , Pr
Z∈Bern(p)n[m ̸= D(E (m) + Z)] ≤ ε.

Theorem 11.1.1 is not the ultimate theorem we may want for dealing with the binary sym-
metric channel. For starters, it does not guarantee codes of all lengths, but rather only of one
ﬁxed length n for any ﬁxed choice of ε. Next, Theorem 11.1.1 only guarantees a small probabil-
ity of decoding failure, but not one that say goes to zero exponentially fast in the length of the
code. The strength of the theorem is (1) its simplicity - it only takes one parameter ε and delivers
a good code with rate ε close to capacity and (2) Algorithmic efﬁciency: the running time of the
encoder and decoder is a polynomial in 1/ε. It turns out both the weaknesses can be addressed
by applying the idea of concatenation of codes (Chapter 10) while preserving the strength. We
present the resulting theorem, leaving the proof of this theorem from Theorem 11.1.1 as an ex-
ercise. (See Exercise 11.1.)

Theorem 11.1.2. There exists polynomially growing functions n0 : [0, 1] → Z+ and T : Z+ → Z+

such that for all p ∈ [0, 1], ε > 0 there exists δ > 0, a function k : Z+ → Z+ and an ensemble of
function E = {En}n and D = {Dn}n such that for all n ∈ Z+ with n ≥ n0(1/ε) the following hold:

1. The codes are ε-close to capacity: Speciﬁcally, k = k(n) ≥ (1 − H (p) − ε)n, En : Fk
2 → Fn
2 and
Dn : Fn
2 → Fk
2 .

2. The codes correct p-fraction of errors with all but exponentially small probability: Speciﬁ-
cally Pr
Z∼Bern(p)n ,X∼U (Fk
2 )[Dn(En(X) + Z) ̸= X] ≤ exp(−δn).

3. Encoding and Decoding are efﬁcient: Speciﬁcally En and Dn run in time at most T (n/ε).

176

11.2 Reduction to Linear Compression

In this section we change our problem from that of coding for error-correction to compress-
ing a vector of independent Bernoulli random variables i.e., the error-pattern. (Recall that we
encountered compression in Exercise 6.10). We show that if the compression is linear and the
decompression algorithm is efﬁcient, then this turns into a linear code with efﬁcient decod-
ing (this is the converse of what we saw in Exercise 6.11). By virtue of being linear the code is
also polynomial time encodable, given the generator matrix. We explain this simple connection
below.
For n ≥ m, we say that a pair (H, D) where H ∈ Fn×m
2 , and D : Fm
2 → Fn
2 forms an τ-error linear
compression scheme for Bern(p)n if H has rank m and

Pr
Z∼Bern(p)n[D(Z · H) ̸= Z] ≤ τ.

We refer to the ratio m
n as the (compression) rate of the scheme (recall Exercise 6.10).

Proposition 11.2.1. Let (H, D) be a τ-error linear compression scheme for Bern(p)n with H ∈
Fn×m
2 . Let k = n − m and let G ∈ Fk×n
2 and G
∗ : Fn×k
2 be full-rank matrices such that G · H = 0 and
G · G
∗ = Ik (the k × k identity matrix). Then the encoder E : Fk
2 → Fn
2 given by

E (X ) = X · G

and the decoder D ′ : Fn
2 → Fk
2 given by

D ′(Y) = (Y − D(Y · H)) · G
∗

satisfy for every m ∈ Fk
2 : Pr
Z∈Bern(p)n[m ̸= D ′(E (m) + Z)] ≤ τ.

Remark 11.2.1. 1. Recall that straightforward linear algebra implies the existence of matri-
ces G and G
∗ above (see Exercise 11.2).

2. Note that the complexity of encoding is simply the complexity of multiplying a vector by
G. The complexity of decoding is bounded by the complexity of decompression plus the
complexity of multiplying by G
∗. In particular if all these operations can be carried out in
O(n log n) time then computing E and D ′ takes O(n log n) time as well.

3. Note that the above proves the converse of Exercise 6.11. These two results show that (at
least for linear codes), channel and source coding are equivalent.

Proof. Suppose D(Z · H) = Z. Then we claim that if Z is the error pattern, then decoding is
successful. To see this, note that

D ′(E (m) + Z) =(E (m) + Z − D((E (m) + Z) · H)) · G
∗ (11.1)

=(E (m) + Z − D(Z · H)) · G
∗ (11.2)

=(E (m) + Z − Z)) · G
∗ (11.3)

=E (m) · G
∗

=m. (11.4)

177

In the above (11.1) follows by deﬁnition of D ′, (11.2) follows from the fact that E (m) · H = m · G ·
H = 0, (11.3) follows by assumption that D(Z · H) = Z and (11.4) follows since E (m) = m · G and
G·G
∗ = I. Thus the probability of a decoding failure is at most the probability of decompression
failure, which by deﬁnition is at most τ, as desired.

Thus our updated quest from now on will be to

Question 11.2.1. Design a linear compression scheme for Bern(p)n of rate at most H (p) + ε.

See Exercise 11.3 on how one can answer Question 11.2.1 with a non-linear compression
scheme.
In what follows we will introduce the polarization phenomenon that will lead us to such a
compression scheme.

11.3 The Polarization Phenomenon

11.3.1 Information Theory Review

The only information theoretic notions that we need in this chapter are that of Entropy (see
Deﬁnition E.1.1) and Conditional Entropy (Deﬁnition E.2.2). We use the notations H (X ) to de-
note the entropy of a variable X and H (X |Y ) to be the conditional entropy, conditioned on Y .
The main properties of these notions we will use are the chain rule (see Theorem E.2.2):

H (X , Y ) = H (Y ) + H (X |Y ),

the fact that conditioning does not increase entropy (see Lemma E.2.4):

H (X |Y ) ≤ H (X ).

We also use the basic fact that the uniform distribution maximizes entropy (see Lemma E.1.2)
and so H (X ) ≤ log |Ω|

if Ω denotes the support of X . A ﬁnal fact that will be useful to keep in mind as we develop the
polar codes is that variables with low entropy are essentially determined, and variables with low
conditional entropy are predictable. We formalize this (with very loose bounds) below.

Proposition 11.3.1. Let α ≥ 0.

1. Let X be a random variable with H (X ) ≤ α. Then there exists x such that PrX [X ̸= x] ≤ α.

178

2. Let (X , Y ) be jointly distributed variables with H (X |Y ) ≤ α. Then the function

A(y) = argmax
x {Pr[X = x|Y = y]}

satisﬁes Pr
(X ,Y )[X ̸= A(Y )] ≤ α.

We defer the proof to Section 11.6.1.

11.3.2 Polarized matrices and decompression

We now return to the task of designing a matrix H (and corresponding matrices G and G
∗) such
that the map Z 7→ Z · H is a good compression scheme. As such we are seeking rectangular
matrices with some extra properties, but in this section we will convert this question into a
question about square invertible matrices.
For an invertible matrix P ∈ Fn×n
2 we consider its effect on Z = (Z1, . . . , Zn) ∼ Bern(p)n. Let
W = (W1, . . . ,Wn) be given by W = Z·P. Now consider the challenge of predicting the Wi ’s as they
arrive online. So when attempting to predict Wi we get to see

W<i ≜ (W1, . . . ,Wi −1)

and can use this to predict Wi . For arbitrary matrices (in particular the identity matrix), seeing
W<i gives us no advantage on predicting Wi . A matrix will be considered polarized if for an
appropriately large fraction of i ’s, Wi is highly predictable from W<i .
To formalize the notion of highly predictable we turn to information theory and simply re-
quire H (Wi |W<i ) ≤ τ for some very small parameter τ of our choice.1 How many i ’s should be
very predictable? Let S = Sτ = {i ∈ [n]|H (Wi |W<i ) ≥ τ}

denote the set of unpredictable bits. An entropy calculation tells us how small we can hope S
would be. Since P is invertible, we have (see Exercise 11.4):

H (W) = H (Z) = n · H (p), (11.5)

But by the chain rule we have
 H (W ) = n∑

i =1 H (Wi |W<i )

≤ ∑

i ∈S H (Wi |W<i ) + nτ (11.6)

≤ ∑

i ∈S H (Wi ) + nτ (11.7)

≤ |S| + nτ. (11.8)

1Eventually we will set τ = o(1/n).
 179

In the above, (11.6) follows by using deﬁnition of S and that |{i ̸∈ S}| ≤ n, (11.7) follows from the
fact that conditioning does not increase entropy and (11.8) follows from the fact that uniformity
maximizes entropy and so H (Wi ) ≤ 1. We thus conclude that |S| ≥ H (p) · n − nτ ≈ H (p) · n. So
the smallest that the set S can be is H (p) · n and we will allow an εn additive slack to get the
following deﬁnition.

Deﬁnition 11.3.1 (Polarizing matrix, unpredictable columns). We say that an invertible matrix
P ∈ Fn×n
2 is (ε, τ)-polarizing for Bern(p)n if for W = Z · P and

S = Sτ = {i ∈ [n]|H (Wi |W<i ) ≥ τ}

we have |S| ≤ (H (p) + ε)n. We refer to the set S as the set of unpredictable columns of P (and
{Wi }ı∈S as the unpredictable bits of W).

We next show how to get a compression scheme from a polarizing matrix (without necessar-
ily having an efﬁcient decompressor). The idea is simple: the compressor simply outputs the
“unpredictable” bits of W. Let WS = (Wi )i ∈S, the compression of Z is simply (Z · P)S. For the sake
of completeness, we record this in Algorithm 11.

Algorithm 9 POLAR COMPRESSOR(Z, S)
INPUT: String Z ∈ Fn
2 and subset S ⊆ [n]
OUTPUT: Compressed string W ∈ F|S|
2 ⊲ Assumes a polarizing matrix P ∈ Fn×n
2

1: RETURN (Z · P)S

Equivalently if we let PS denote the n ×|S| matrix whose columns correspond to indices in S,
then the compression of Z is Z · PS. So PS will be the matrix H we are seeking. Before turning to
the decompression, let us also specify G and G
∗ for this construction above. Indeed Exercise ??
shows that G = (
P −1) ¯S and G
∗ = P ¯S. In particular, the complexity of multiplying by P and P
−1

dominate the cost of the matrix multiplications needed in the encoding and decoding.
We ﬁnally turn to the task of describing the decompressor corresponding to compression
with a polarizing matrix P with unpredictable columns S. The method is a simple iterative one,
based on the predictor from Proposition 11.3.1 and is presented in Algorithm 10.
Next we argue that Algorithm 10 has low failure probability:

Lemma 11.3.2. If P is (ε, τ)-polarizing for Bern(p)n with unpredictable columns S, then the suc-
cessive cancellation decoder has failure probability at most τ · n, i.e.,

Pr
Z∈Bern(p)n[Z ̸= SCD((Z · P)S, P, S)] ≤ τ · n.

Thus if P is (ε, ε/n)-polarizing for Bern(p)n then the failure probability of the successive cancel-
lation decoder is at most ε.

2Note that the Successive Cancellation Decompressor, and Decompressors in general are not expected to work
correctly on every input. So the INPUT/OUTPUT relations don’t fully capture the goals of the algorithm. In such
cases, in the rest of the chapter we will include a PERFORMANCE PARAMETER which we wish to minimize that
attempts to capture the real goal of the algorithm.
 180

Algorithm 10 Successive Cancellation Decompressor SCD(W, P, S)

INPUT: S ⊆ [n], W ∈ FS
2 and P ∈ Fn×n
2
OUTPUT: ˜Z ∈ Fn
2 such that ( ˜Z · P)S = W
PERFORMANCE PARAMETER: 2 PrZ∼Bern(p)n [SCD((Z · P)S, P, S) ̸= Z] (smaller is better)

1: FOR i = 1 to n DO

2: IF i ∈ S THEN

3: ˜Wi ← Wi
4: ELSE

5: ˜Wi ← argmaxb∈F2 {Pr [
Wi = b|W<i = ˜W<i ]}

6: RETURN ˜Z ← P
−1 · ˜W

Proof. Let W = Z · P. Note that by Step 3 in Algorithm 10, we have for every i ∈ S, ˜Wi = Wi . For
any i ̸∈ S, by Proposition 11.3.1 applied with X = Wi , Y = W<i , α = τ we get that

Pr
Z [Wi ̸= Ai ( ˜W<i )] ≤ τ,

where Ai (·) is the corresponding function deﬁned for i ̸∈ S. By a union bound, we get that

Pr
Z [∃i s.t. Wi ̸= Ai ( ˜W<i )] ≤ τ · n.

Note that by step 5 in Algorithm 10 and the deﬁnition of Ai (·), we have ˜Wi = Ai ( ˜W<i ). But
if W ̸= ˜W there must exists a least i such that ˜Wi ̸= Wi . Thus we get Pr[W ̸= ˜W] ≤ τn and so
probability that SCD(WS, P, S) ̸= Z is at most τn.

To summarize this section we have learned that to prove Theorem 11.1.1 it sufﬁces to answer
the following question.

Question 11.3.1. Find an (ε, ε/n)-polarizing matrix P ∈ Fn×n
2 with n is bounded by a poly-
nomial in 1/ε; where SCD (potentially a re-implementation of Algorithm 10) as well as mul-
tiplication and inversion by P takes O(n log n) time.

Next we describe the idea behind the construction, which will answer the above question.

11.3.3 A polarizing primitive

Thus far in the chapter we have essentially only been looking at the problem from different
perspectives, but not yet suggested an idea on how to get the codes (or compression schemes)
that we desire (i.e. answer Question 11.3.1. It is this section that will provide the essence of the
idea, which is to start with a simple and basic polarization step, and then iterate it appropriately

181✞☛ ✁ ✂ ✁+ ✂ ✂✄(☎)✄(☎)✆✄☎✌✄(✆☎1✌☎)✄(✆☎(1✌☎))
+

Figure 11.1: The 2 × 2 Basic Polarizing Transform. Included in brown are the conditional en-
tropies of the variables, conditioned on variables directly above them.

many times to get a highly polarized matrix. Indeed it is this section that will explain the term
polarization (and why we use this term to describe the matrices we seek).
Recall that the ultimate goal of polarization is to start with many independent bits Z1, . . . , Zn
which are independent and slightly unpredictable (if p is small), and to produce some linear
transform that concentrates all the unpredictability into a fewer set of bits. In our basic primi-
tive we will try to do this with two bits. So we have Z1, Z2 such that H (Z1) = H (Z2) = p and we
wish to produce two bits W1,W2 such that at least one of these is less predictable than either
of Zi ’s. Since there are only 4 possible linear combinations of two bits (over F2) and three are
trivial (0, Z1, and Z2) we are left with only one candidate function namely Z1 + Z2. So we will
set W1 = Z1 + Z2. For W2 we are left with the trivial functions: 0 carries no information and so
is ruled out. Without loss of generality, the only remaining choice is W2 = Z2. So we look at this
transformation: P2 : (Z1, Z2) 7→ (W1,W2) = (Z1 + Z2, Z2). (See Figure 11.1.)
This is an invertible linear transformation given by the matrix

P2 = (
1 0
1 1
) .

So (see Exercise 11.5): H (W1,W2) = 2H (p). (11.9)

But some examination shows that H (W1) > H (Z1), H (Z2). In particular the probability that W1 is
1 is 2p(1 − p) ∈ (p, 1/2) and since H (·) is monotone increasing in this interval (see Exercise 11.6)
it follows that H (W1) > H (p) = H (Z1) = H (Z2). Thus W1 is less predictable than either of the
input bits; and now, thanks to the chain rule

H (W2|W1) = H (W1,W2) − H (W1) = H (Z1, Z2) − H (W1) = H (Z1) + H (Z2) − H (W1) < H (Z1), H (Z2).

In other words multiplying by P2 has separated the entropy of two equally entropic bits, into a
more entropic bit and a (conditionally) less entropic one. But of course this may be only slight
polarization and what we are hoping for is many bits that are almost completely determined by
preceding ones.
To get more polarization we apply this 2×2 operation repeatedly. Speciﬁcally, let P2(Z1, Z2) =
(Z1 + Z2, Z2). Then we let P4(Z1, Z2, Z3, Z4) = (W1,W2,W3,W4) = (P2(U1,U2), P2(U3,U4)) where

182

+
+

+

`✞☛ ✞☛ ✁✂✄☎✄✆✄☞✝✄☞✝✟✆✄☞✝✟☎✄✠✡✆✡☞✝✡☞✝✟✆✡☞✝✟☎✡✠✡☎
Figure 11.2: The n × n Basic Polarizing Transform.

(U1,U2) = P2(Z1, Z3) and (U3,U4) = P2(Z2, Z4). Thus the bit W1 = Z1 + Z2 + Z3 + Z4 has higher
entropy than say Z1 or even U1 = Z1 + Z3, whereas W4 = Z4 conditioned on (W1,W2,W3) can be
shown to have much lower entropy than Z4 (unconditionally) or even U4 = Z4 conditioned on
U2.
 The composition above can be extended easily to n bit inputs, when n is a power of two, to
get a linear transform Pn (See Figure 11.2. We will also give this transformation explicitly in the
next section).

It is also clear that some bits will get highly entropic due to these repeated applications of P2.
What is remarkable is that the polarization is nearly “perfect” - most bits Wi have conditional
entropy (conditioned on (W j ) j <i ) close to 1, or close to 0. This leads to the simple construction
of the polarizing matrix we will describe in the next section. A striking beneﬁt of this simple
construction is multiplying a vector by P only takes O(n log n) time, and so does multiplying by
the inverse of P. And most importantly a version of SCD (Algorithm 10) is also computable in
time O(n log n) and this leads to an overall compression and decompression algorithms running
in time O(n log n), which we describe in the next section.

We note that one missing element in our description is the challenge of determining the
exact set of indices S that include all the high-conditional-entropy bits. We will simply skirt
the issue and assume that this set is known for a given matrix P and given to the compres-
sion/decompression algorithms. So this leads to a non-uniform solution to compression and
decompression problem, as well as the task of achieving Shannon capacity on the binary sym-
metric channel. We stress that this is not an inherent problem with the polarization approach.
An explicit algorithm to compute S (or a small superset of S) is actually known and we discuss
this in Section 11.7.
 183

11.4 Polar codes, Encoder and Decoder

We begin with the description of polar codes along with the statement of the main results in Sec-
tion 11.4.1. We explicitly state the encoding algorithm and analyze its runtime in Section 11.4.2.
We present the decoder as well as its proof of correctness in Section 11.4.3.

11.4.1 The Code and Polarization Claims

We are now ready to describe the code.

Deﬁnition 11.4.1 (Basic polarizing matrix). We deﬁne the n × n polarization matrix Pn recur-
sively for n = 2, 4, 8, . . ., by describing the linear map Pn : Z 7→ Z · Pn. For n = 2 and Z ∈ F2
2 we
deﬁne P2(Z) = (Z1 + Z2, Z2).3 For n = 2t and Z = (U, V) for U, V ∈ Fn/2
2 we deﬁne

Pn(Z) = (Pn/2(U + V), Pn/2(V)).

Exercise 11.7 talks about explicit description of Pn as well as some extra properties.
In Section 11.5 we show that this matrix polarizes fast as n → ∞. The main theorem we will
prove is the following:

Theorem 11.4.1 ((Polynomially) Strong Polarization). Fix p ∈ (0, 1/2) and constant c. There ex-
ists a polynomial function n0 such that for every ε > 0 there exists n = 2t with 1/ε ≤ n ≤ n0(1/ε)
and a set E ⊆ [n] with |E | ≤ (ε/2)·n such that for every i ̸∈ E , the conditional entropy H (Wi |W<i ) ̸∈
(n−c , 1 − n−c )). Furthermore, if we let S = {i ∈ [n]|H (Wi |W<i ) ≥ n−c } then |S| ≤ (H (p) + ε) · n and
the matrix Pn is (ε, 1/nc )-polarizing for Bern(p)n with unpredictable columns S.

This theorem allows us to choose the threshold on how close to zero the conditional en-
tropy of the polarized bits can be, and this threshold can be the inverse of an arbitrarily high
degree polynomial in n. We will prove Theorem 11.4.1 in Section 11.5, which will be quite tech-
nical. But with the theorem in hand, it is quite simple to complete the description of the Basic
Polar Code along with the associated encoding and decoding algorithms, and to analyze their
performance.

Deﬁnition 11.4.2 (Basic Polar (Compressing) Code). Given p and ε ≤ 1/4, let n and S ⊆ [n] be
as given by Theorem 11.4.1 for c = 2. Then the Basic Polar Code with parameters p and ε maps
Z ∈ Fn
2 to Pn(Z)S.

Proposition 11.4.2 (Rate of the Basic Polar Code). For every p ∈ (0, 1/2) and ε > 0, the rate of the
Basic Polar Code with parameters p and ε is at most H (p) + ε.4

11.4.2 Encoding

The description of the map Pn(Z) is already explicitly algorithmic, modulo the computation of
the set S. For the sake of concreteness we write the algorithm below in Algorithm 11, assuming
S is given as input, and argue its running time.

3We will be using Pn to denote the n × n matrix and Pn to denote the corresponding linear map that acts on Z.
4Recall that we are trying to solve the compression problem now.

184

Algorithm 11 BASIC POLAR ENCODER(Z; n, S)
INPUT: n power of 2, Z ∈ Fn
2 and S ⊆ [n]
OUTPUT: Compression W ∈ FS
2 of Z given by W = (Pn(Z))S

1: RETURN W = (P (n, Z))S

2: function P(n, Z)

3: IF n = 1 THEN

4: RETURN Z

5: ELSE

6: Let U = (Z1, . . . , Zn/2) and V = (Zn/2+1, . . . , Zn)

7: RETURN (P (n/2, U + V), P (n/2, V))

Proposition 11.4.3. The running time of the BASIC POLAR ENCODER algorithm is O(n log n).

Proof. If T (n) denotes the running time of the algorithm on inputs of length n, then T (·) satis-
ﬁes the recurrence T (n) = 2T (n/2) + O(n), which implies the claimed runtime.

11.4.3 Decoding

Note that a polynomial time algorithm to compute Pr [
Wi = b|W<i = ˜W<i ] given b ∈ F2 and
˜W<i ∈ Fi −1
2 would lead to a polynomial time implementation of the SUCCESSIVE CANCELLATION
DECOMPRESSOR (Algorithm 10). However, we will go a step better and exploit the nice structure
of the Basic Polarizing Matrix to get an O(n log n) algorithm without much extra effort. The key
insight to this faster decoder is that the decoder works even if Z ∼ Bern(p1) × · · · × Bern(pn), i.e.,
even when the bits of Z are not identically distributed, as long as they are independent. This
stronger feature allows for a simple recursive algorithm. Speciﬁcally we use the facts that

1. If Z1 ∼ Bern(p1) and Z2 ∼ Bern(p2) are independent then Z1 + Z2 is a Bernoulli random
variable. Let b+(p1, p2) denote the bias (i.e., probability of being 1) of Z1 + Z2 (and so
Z1 + Z2 ∼ Bern(p +(p1, p2)) (see Exercise 11.8).

2. If Z1 ∼ Bern(p1) and Z2 ∼ Bern(p2) are sampled conditioned on Z1 + Z2 = a (for some
a ∈ F2) then Z2 is still a Bernoulli random variable. Let b|(p1, p2, a) denote the bias of Z2
conditioned on Z1 + Z2 = a. (Note that b|(p1, p2, 0) is not necessarily equal to b|(p1, p2, 1).)
See Exercise 11.9 for more.

We now use the functions b+ and b| deﬁned above to describe our decoding algorithm. We
switch our notation slightly to make for a cleaner description. Rather than being given the
vector WS ∈ F|S|
2 , we assume that our decoder is given as input a vector W ∈ (F2 ∪ {?})n where
Wi =? if and only if i ̸∈ S.
The main idea behind the decoding algorithm is that to complete W to a vector in Fn
2 , we
can ﬁrst focus on computing
 W[1, . . . , n/2] def
= (W1, . . . ,Wn/2).

185

It will turn out that we can use the fact that W[1, . . ., n/2] = Pn/2(Z ′
1, . . . , Z ′
n/2) where
5 Z ′
i ∈ Bern(b+(p, p))
are independent. This problem can be solved by recursion, and if we compute also the Z ′
i ’s
along the way, then we can turn to computing W [n/2 + 1, . . . , n] = Pn/2(Zn/2+1, . . . , Zn) but now
Zi is no longer drawn from Bern(p). Instead we have Zi ∼ Bern(b|(p, p, Z ′
i −n/2)) but the Zi ’s are
still independent. The stronger recursive condition allows us to also solve this problem recur-
sively. Details are given in Algorithm 12.

Algorithm 12 BASIC POLAR DECODER: BPD(W; n, p)
INPUT: n power of 2, W ∈ (F2 ∪ {?})n and 0 ≤ p < 1/2
OUTPUT: ˜Z ∈ Fn
2 such that for every i either Wi =? or ( ˜Z · P)i = Wi
PERFORMANCE PARAMETER: PrZ∼Bern(p)n [Z ̸= BPD((Z · Pn)S; n, p)]

1: ( ˜Z, ˜W, ρ) = RPD(W; n, (p, · · · , p))

2: RETURN ˜Z

3: function RECURSIVE POLAR DECODER: RPD((W; n, (p1, . . . , pn)))
INPUT: W ∈ (F2 ∪ {?})n and p1, . . . , pn ∈ [0, 1].
OUTPUT: ˜Z, ˜W ∈ Fn
2 with ˜W = Pn( ˜Z) and ( ˜W
)

S = WS. ρ = (ρ1, . . . , ρn) ∈ [0, 1]
n. ⊲ ˜Z is the main
output while ˜W and ρ will help us reason about correctness.
PERFORMANCE PARAMETER: PrZ∼Bern(p1)×···×Bern(pn )[ ˜Z ̸= Z] where ˜Z is the ﬁrst element of the
triple output by RPD((Z · Pn)S; n, (p1, . . . , pn))

4: IF n = 1 and W1 ∈ F2 THEN

5: RETURN (W1,W1, p1)

6: ELSE IF n = 1 and W1 =? THEN

7: RETURN (1, 1, p1) if p1 ≥ 1/2 and (0, 0, p1) otherwise

8: ELSE ⊲ n ≥ 2

9: W = (W
(1), W
(2)) where W
(1), W
(2) ∈ (F2 ∪ {?})n/2

10: FOR i = 1 to n/2 DO

11: let qi = b+(pi , pn/2+i )

12: Let ( ˜X, ˜W
1, ρ(1)) = RECURSIVE POLAR DECODER(W
(1); n/2, (q1, . . . , qn/2))

13: FOR i = 1 to n/2 DO

14: let ri = b|(pi , pn/2+i , ˜Xi )

15: Let ( ˜Y, ˜W
2, ρ(2)) = RECURSIVE POLAR DECODER(W
(2); n/2, (r1, . . . , rn/2))

16: Let ˜Z = ( ˜X + ˜Y, ˜Y), and let ˜W = ( ˜W
1, ˜W
2) and ρ = (ρ(1), ρ(2))

17: RETURN ( ˜Z, ˜W, ρ)

We assume that p + and p | can be computed in constant time, and with this assumption it is
straightforward to see that the above algorithm also has a running time of O(n log n), by using
the same recursive analysis that we used in the proof of Proposition 11.4.3. The correctness is a
bit more involved and we argue this in the next lemma.

5Note that this follows from deﬁnition of Pn.
 186

Lemma 11.4.4. Let Z ∼ Bern(p1)×· · ·×Bern(pn), and W = Pn(Z). Further let W
′ = (W ′
1, . . . ,W ′
n) be
given by W ′
i = Wi if i ∈ S and W ′
i =? otherwise. Let ( ˜Z, ˜W, ρ) = RECURSIVE POLAR DECODER(W
′; n, (p1, . . . , pn)).
Then, if H (Wi |W<i ) ≤ τ for every i ̸∈ S, we have the following:

(1) For every i , it is the case that PrZ[Wi = 1|W<i = ˜W<i ] = ρi .

(2) PrZ [
W ̸= ˜W
] ≤ τn.

(3) PrZ [
Z ̸= ˜Z
] ≤ τn.

Note that part (3) of Lemma 11.4.4 proves the same decoding error bound that we proved in
Lemma 11.3.2 for the SUCCESSIVE CANCELLATION DECODER (Algorithm 10).

Proof of Lemma 11.4.4. The main part of the lemma is part (1). Part (2) follows almost immedi-
ately from part (1) and Proposition 11.3.1. And part (3) is straightforward. We prove the parts in
turn below.
We begin by ﬁrst arguing that for every n that is a power of two:

˜W = Pn( ˜Z). (11.10)

For the base case of n = 1, lines 5 and 7 show that W1 = Z1 as desired.6 By induction (and lines 12
and 15) we have that ˜W
1 = Pn/2( ˜X) and ˜W
2 = Pn/2( ˜Y). Finally, line 16 implies that (the second
equality follows from the deﬁnition of Pn):

Pn( ˜Z) = Pn(( ˜X + ˜Y, ˜Y)) = (
Pn/2( ˜X + Y + Y), Pn/2(Y)) = ( ˜W
1, ˜W
2) = ˜W,

as desired.
Part (1) follows by induction on n. If n = 1 (where say we call RPD((W1), 1, (p ′′
1 ))) then the
claim follows since here we have ρ1 = p ′′
1 , W1 = Z1 and Z1 ∼ Bern(p ′′
1 ). For larger values of n, we
consider two cases (below we have Z = (U, V)).
If i ≤ n/2 then we have that Wi = Pn/2(U + V)i (via deﬁnition of Pn). Furthermore (U + V) ∼
Bern(q1) × · · · × Bern(qn/2). Thus by the inductive claim, the recursive call RECURSIVE POLAR
DECODER(W
′[1, . . . , n/2]; n/2, (q1, . . . , qn/2) satisﬁes

ρi = ρ(1)
i
= Pr
(U+V)∼Bern(q1)×···×Bern(qn/2)
 [
Wi = 1|W<i = ˜W<i ]

= Pr
Z∼Bern(p1)×···×Bern(pn )
 [
Wi = 1|W<i = ˜W<i ]

as desired. (In the above, the ﬁrst equality follows from the algorithm deﬁnition and the third
equality follows from the deﬁnition of qi .)
Now if i > n/2, note that the condition W[1, . . . , n/2] = ˜W[1, . . . , n/2] is equivalent to the con-
dition that U + V = ˜X (since W[1, . . . , n/2] = Pn/2(U + V) and ˜X = P −1
n/2( ˜W[1, . . . , n/2]), where the

6Note that when deﬁning Pn, the base case was n = 2 but note that if we started with n = 1 and deﬁne P1(Z ) = W ,
then the resulting deﬁnition is the same as on the we saw in Deﬁnition 11.4.1.

187

latter equality follows from (11.10) and the fact that the map Pn/2 is invertible). And now from
deﬁnition of Pn, we have W[n/2 + 1, . . . , n] = Pn/2(V). Conditioning on U + V = ˜X implies that
V ∼ Bern(r1) × · · · × Bern(rn/2) — this is exactly how ri ’s were deﬁned. Thus we have

Pr
Z∼Bern(p1)×···×Bern(pn )[Wi = 1|W<i = ˜W<i ]

= Pr
V∼Bern(r1)×Bern(rn/2)
 [
Pn/2(V)i −n/2 = 1|Pn/2(V)[1, . . . , i − n/2 − 1] = ˜W[n/2 + 1, . . . , i − 1] and U + V = ˜X
] .

By induction again on the recursive call to RECURSIVE POLAR DECODER(W
′[n/2+1, . . . , n]; n/2, (r1, . . . , rn/2))
we have the ﬁnal quantity above equals ρ(2)
i −n/2 = ρi (where the last equality follows from the al-
gorithm deﬁnition). This concludes the proof of part (1).
Part (2) follows from Proposition 11.3.1. We ﬁrst note that if i ∈ S, then by line 5 of the
algorithm we have Wi = ˜Wi . Now assume i ̸∈ S. We claim that ˜Wi = 1 if and only if ρi =
PrZ[Wi = 1|W<i = ˜W<i ] ≥ 1/2. To see this note that ρi = p ′
i when RECURSIVE POLAR DECODER
is called on the input (W ′
i , 1, p ′
i ). Then the claim follows from line 7 of the algorithm. Thus
˜Wi = argmaxb∈F2{{Pr[Wi = b|W<i = ˜W<i ]. By Proposition 11.3.1, applied to the variables X = Wi
and Y = W<i with α = τ we get
 Pr[Wi ̸= ˜Wi |W<i = ˜W<i ] ≤ τ.

By a union bound over i , we thus have

Pr[∃i ∈ [n] s.t. Wi ̸= ˜Wi |W<i = ˜W<i ] ≤ τn.

But if W ̸= ˜W there must exist a least index i such that Wi ̸= ˜Wi and so we have Pr[W ̸= ˜W] ≤ τn
concluding proof of part (2).
For part (3), note that by (11.10), if ˜W = W (which holds with probability at least 1 − τn from
part (2)), we have ˜Z = P −1
n ( ˜W) = P −1
n (W) = Z as desired.

The correctness of BASIC POLAR DECODER (Algorithm 12) follows immediately and we state
this explicitly below (see Exercise 11.10).

Corollary 11.4.5. For every input n = 2t , p ∈ [0, 1/2) and W ∈ (F2 ∪ {?})n, the BASIC POLAR DE-

CODER (Algorithm 12) runs in time O(n log n) and computes an output ˜Z ∈ Fn
2 such that Pn( ˜Z)i =
Wi holds for every i for which Wi ̸=?. Furthermore if (1) Z ∼ Bern(p)n, (2) WS = Pn(Z)S and (3)
H (Wi |W<i ) ≤ τ for every i ̸∈ S then PrZ[ ˜Z ̸= Z] ≤ τn.

To summarize the claims of this section, Theorem 11.4.1 guarantees the existence of a po-
larizing matrix as desired to satisfy the information-theoretic conditions of Question 11.3.1.
And Proposition 11.4.3 and Corollary 11.4.5 ensure that the encoding and descoding times are
O(n log n). This allows us to complete the proof of Theorem 11.1.1 (modulo the proof of Theo-
rem 11.4.1 — which will be proved in the next section).

Proof of Theorem 11.1.1. Recall from Proposition 11.2.1 and Question 11.3.1 that it sufﬁces to
ﬁnd, given p ∈ [0, 1/2) and ε > 0, an (ε, ε/n)-polarizing matrix P ∈ Fn×n
2 with n bounded by a
polynomial in 1/ε; such that multiplication by P and decompression take O(n log n) time.

188

Theorem 11.4.1 applied with parameters p, ε and c = 2 yields n and the matrix P = Pn ∈ Fn×n
2
that is (ε, 1/n2)-polarizing. Since Theorem 11.4.1 also guarantees ε ≥ 1/n, we have that Pn is
(ε, ε/n)-polarizing. Furthermore we have that there exists a set S ⊆ [n] with |S| ≤ (H (p) + ε)n
such that H (W ¯S|WS) ≤ ε when W = Z·P and Z ∼ Bern(p)n. Given such a set S we have, by Propo-
sition 11.4.3, that the time to compress Z ∈ Fn
2 to (Z · Pn)S is O(n log n). Finally Corollary 11.4.5
asserts that a decompression ˜Z can be computed given (Z · Pn)S in time O(n log n) and ˜Z equals
Z with probability at least 1 − ε thereby completing the proof of Theorem 11.1.1.

11.5 Analysis: Speed of Polarization

We now turn to the most crucial aspect of polarization - the fact that it happens, and it is fast
enough to deliver polynomial convergence to capacity. In this section we ﬁrst give an overview
of how we will think about polarization. We will then analyze the convergence by ﬁrst explor-
ing what happens in a single polarization step (i.e., the action of P2) and then showing how the
local effects aggregate after log2 n steps of polarization. This will lead us to the proof of Theo-
rem 11.4.1.

11.5.1 Overview of Analysis

We start by setting up some more notation. Recall n = 2t . In this section it will be convenient
for us to give names to intermediate variables {Z ( j )
i }(i ∈[n],0≤ j ≤t ) that are computed during the
computation of Pn(Z1, . . . , Zn). Let Z (0)
i = Zi . For 1 ≤ j ≤ t , let

(Z ( j )
i , Z ( j )
i +2t − j ) = P2(Z ( j −1)
i , Z ( j −1)
i +2t − j ) = (Z ( j −1)
i + Z ( j −1)
i +2t − j , Z ( j −1)
i +2t − j ). (11.11)

for every i ∈ [n] such that i and i + 2t − j are in the same “block at the j th” level. i.e., ⌈i /2t − j +1⌉ =
⌈(i + 2t − j )/2t − j +1⌉. (Alternatively one could say i and i + 2t − j as in the same dyadic interval of
size 2t − j +1.) Further,

Deﬁnition 11.5.1. We will say that a pair (i , i ′) are j th-level siblings if they are in the same block
at the j th level and i ′ = i + 2t − j .

Note that if one unravels the recursion in (11.11), then if Zi , Zi ′ are on the LHS, then (i , i ′)
are siblings at the j th level.
We now claim that (see Exercise 11.11):

Pn(Z) = (Z (t )
1 , . . . , Z (t )
n ). (11.12)

Figure 11.3 illustrates the block structure of Pn and the notion of j th level blocks and siblings at
the j th level.
In what follows we will pick a random i ∈ [n] and analyze the conditional entropy of Z ( j )
i |Z
( j )
<i
as j progresses from 0 to t (we independently pick i for different values of j ). Indeed let

X j = H (Z ( j )
i |Z
( j )
<i ).

189✞☛… ✁ ✞☛…  ✂✄ ✂

Figure 11.3: Block structure of the Basic Polarizing Transform. Circled are a block at the 2nd
level and two 2nd level siblings.

Clearly X0 = H (p) since Z (0)
i = Zi is independent of Z<i and is distributed according to Bern(p).
In what follows we will show that for every constant c if t is a sufﬁcient large then with high
probability over the choice of i , X t ̸∈ (n−c , 1 − n−c ). To track the evolution of X j as j increases,
we will ﬁrst try to analyze local polarization which will study how X j compares with X j −1. Def-
inition 11.5.2 below captures the desired effect of a local step, and the following lemma asserts
that the operator P2 does indeed satisfy the conditions of local polarization.

Deﬁnition 11.5.2 (Local Polarization). A sequence of random variables X0, . . . , X j , . . . , with X j ∈
[0, 1] is locally polarizing if the following conditions hold:

(1) (Unbiased): For every j , and a ∈ [0, 1] we have E[X j +1|X j = a] = a.

(2) (Variance in the middle): For every τ > 0, there exists θ = θ(τ) > 0 such that for all j , we
have: If X j ∈ (τ, 1 − τ) then |X j +1 − X j | ≥ θ.

(3) (Suction at the ends): For every c < ∞, there exists τ = τ(c) > 0 such that (i) if X j ≤ τ then
Pr[X j +1 ≤ X j /c] ≥ 1/2; and similarly (ii) if 1 − X j ≤ τ then Pr[(1 − X j +1 ≤ (1 − X j )/c] ≥ 1/2.

We further say a sequence is simple if for every sequence a0, . . . , a j , conditioned on X0 = a0, . . . , X j =
a j , there are two values a+ and a| such that X j +1 takes value a+ with probability 1/2 and a| with
probability 1/2.

Lemma 11.5.1 (Local Polarization). The sequence X0, . . . , X j , . . . , with X j = H (Z ( j )
i |Z
( j )
<i ) where i
is drawn uniformly from [n] is a simple and locally polarizing sequence.

We will prove Lemma 11.5.1 in Section 11.5.2 but use it below. But ﬁrst let us see what it does
and fails to do. While local polarization prevents the conditional entropies from staying static,
it doesn’t assert that eventually all conditional entropies will be close to 0 or close to 1, the kind
of strong polarization that we desire. The following deﬁnition captures our desire from a strong
polarizing process, and the lemma afterwards asserts that local polarization does imply strong
polarization.
 190

Deﬁnition 11.5.3 ((Polynomially) Strong Polarization). A sequence of random variables X0, X1, . . . , X t , . . .
with X j ∈ [0, 1] strongly polarizes if for all γ > 0 there exist α < 1 and β < ∞ such that for all t we
have Pr[X t ∈ (γt , 1 − γt )] ≤ β · αt .

Lemma 11.5.2 (Local vs. Global Polarization). If a sequence X0, . . . , X t , . . . , with X t ∈ [0, 1] is sim-
ple and locally polarizing, then it is also strongly polarizing.

Armed with Lemmas 11.5.1 and 11.5.2, proving Theorem 11.4.1 is just a matter of setting
parameters.

Proof of Theorem 11.4.1. We assume without loss of generality that c ≥ 1. (Proving the theorem
for larger c implies it also for smaller values of c.) Given p and c ≥ 1, let γ = 2−c . Let β < ∞
and α < 1 be the constants given by the deﬁnition of strong polarization (Deﬁnition 11.5.3) for
this choice of γ. We prove the theorem for n0(x) = max{8x, 2(2βx)⌈log(1/α)⌉}. Note that n0 is a

polynomial in x. Given ε > 0, let t = max {⌊log(8/ε)⌋ , ⌈ log(2β/ε)
log(1/α)
 ⌉} so that

n = 2t ≤ max {
8/ε, 2 · (2β/ε)1/ log(1/α)} = n0(1/ε).

Note that the choice of t gives β · αt ≤ ε/2 and γt = 2−c t = n−c . We also have n ≥ 4/ε and thus
2n−c ≤ 2n−1 ≤ ε/2. We show that for this choice and t and n, the polarizing transform Pn has the
desired properties — namely that the set S of variables of noticeably large conditional entropy
is of small size.
We ﬁrst show that the set of variables with intermediate conditional entropies is small. Let
us recall some notations from above, speciﬁcally (11.11). Let (Z ( j )
i ) denote the intermediate

results of the computation W = Pn(Z) = (Z (t )
1 , . . . , Z (t )
n ), and let X j = H (Z ( j )
i |Z
( j )
<i ) for a uniformly
random choice of i ∈ [n]. By Lemmas 11.5.1 and 11.5.2 we have that the sequence X0, . . . , X t , . . .
is strongly polarizing. By the deﬁnition of strong polarization, we have that

Pr
i ∈[n]
 [H (Wi |W<i ) ∈ (n−c , 1 − n−c )] = Pr
i
 [H (Z (t )
i |Z
(t )
<i ) ∈ (γt , 1 − γt )]

= Pr [X t ∈ (γt , 1 − γt )]

≤ βαt

≤ ε/2.

Thus we have that the set E = {i ∈ [n]|H (Wi |W<i ) ∈ (n−c , 1 − n−c )} satisﬁes |E | ≤ εn/2.
Finally, we argue the “Further" part. Indeed, we have

nH (p) = ∑

i ∈[n] H (Wi |W<i ) ≥ ∑

i ∈S\E H (Wi |W<i ) ≥ (|S| − |E |)(1 − n−c ),

where the ﬁrst equality follows from the chain rule and the last inequality follows from deﬁni-
tions of S and E . Re-arranging one gets that

|S| ≤ nH (p)
1 − n−c + εn/2 ≤ nH (p)(1 + 2n−c ) + εn/2 ≤ nH (p) + εn.

It remains to prove Lemmas 11.5.1 and 11.5.2 which we prove in the rest of this chapter.

191

11.5.2 Local Polarization

To understand how X j compares with X j −1, we start with some basic observations about these

variables, or more importantly the variables Z ( j )
i and Z ( j +1)
i (recall (11.11)). Let i and i ′ be j th

level siblings, so that (Z ( j )
i , Z ( j )
i ′ ) = P2(Z ( j −1)
i , Z ( j −1)
i ′ ). Our goal is to compare the pairs of con-

ditional entropies (H (Z ( j )
i |Z
( j )
<i ), H (Z ( j )
i ′ |Z
( j )
<i ′)) with (H (Z ( j −1)
i |Z
( j −1)
<i ), H (Z ( j −1)
i ′ |Z
( j −1)
<i ′ )). The col-
lection of variables involved and conditioning seem messy, so let us look at the structure of Pn
more carefully to simplify the above. We do this by noticing the Z ( j )
i is really independent of

most Z ( j )
i ′ (at least for small values of j ) and in particular the set of variables that Z ( j −1)
i and

Z ( j −1)
i ′ depend on are disjoint. Furthermore these two variables, and the sets of variables that
they depend on are identically distributed. Next, we present the details.
We begin with a useful notation. Given i ∈ [n = 2t ] and 0 ≤ j ≤ t , let

Si , j def
= {k ∈ [n]|i ≡ k mod 2t − j } .

Note that the ℓ1, ℓ2 ∈ Si , j need not be siblings at the j th level.

Proposition 11.5.3. For every 1 ≤ j ≤ t and j th level siblings i and i ′ with i < i ′ the following
hold:

(1) Si , j = Si ′, j = Si , j −1 ∪ Si ′, j −1.

(2) {Z ( j )
k |k ∈ Si , j } is independent of {Z ( j )
k |k ̸∈ Si , j }.

(3)
 H (Z ( j −1)
i |Z
( j −1)
<i ) = H (Z ( j −1)
i |Z
( j −1)
{k∈Si , j −1,k<i })

= H (Z ( j −1)
i |Z
( j −1)
{k∈Si , j ,k<i }) .

(4)
 H (Z ( j −1)
i ′ |Z
( j −1)
<i ′ ) = H
 (
Z ( j −1)
i ′ |Z
( j −1)
{k∈Si ′, j −1,k<i ′}
)

= H (Z ( j −1)
i ′ |Z
( j −1)
{k∈Si , j ,k<i }) .

(5)
 H (Z ( j )
i |Z
( j )
<i ) = H (Z ( j )
i |Z
( j )
{k∈Si , j ,k<i })

= H (Z ( j )
i |Z
( j −1)
{k∈Si , j ,k<i }) .

192

(6)
 H (Z ( j )
i ′ |Z
( j )
<i ′) = H (Z ( j )
i ′ | {
Z
( j )
i
 } ∪ Z
( j )
{k∈Si , j ,k<i })

= H (Z ( j )
i ′ | {Z ( j )
i
 } ∪ Z
( j −1)
{k∈Si , j ,k<i }) .

Proof. Part (1) follows from the deﬁnition of Si , j and the deﬁnition of siblings. Indeed, since
i ′ = i + 2t − j , we have i ≡ i ′ mod 2t − j , which implies the ﬁrst equality. The second equality
follows from the observations that k1 ≡ k2 mod 2t − j +1 implies k1 ≡ k2 mod 2t − j (this in turn
implies Si , j −1, Si ′, j −1 ⊆ Si , j ) and that if k ≡ i mod 2t − j +1 then k ̸≡ i ′ mod 2t − j and vice versa
(which in turn implies that Si , j −1 and Si ′, j −1 are disjoint. Part (2) follows from the fact that (see
Exercise 11.12):

Lemma 11.5.4. For every i , the set {Z ( j )
k |k ∈ Si , j } is determined completely by {Zk |k ∈ Si , j },

and the Zk ’s are all independent. The ﬁrst equality in part (3) follows immediately from part
(2), and the second uses part (1) and the fact that Z ( j −1)
i is independent of {Zk |k ∈ Si ′, j −1, k < i }

(the latter claim follows from the fact that Si , j −1 and Si ′, j −1 as disjoint, as argued in the proof of
part (1) above). The ﬁrst equality in part (4) is similar, whereas the second uses the additional
fact that Si ′, j −1 contains no elements between i and i ′. Indeed the latter observation implies

that H
 (
Z ( j −1)
i ′ |Z
( j −1)
{k∈Si ′, j −1,k<i ′}
)
 = H
 (
Z ( j −1)
i ′ |Z
( j −1)
{k∈Si ′, j −1,k≤i }
)
. But by part (2), Z ( j −1)
i ′ is independent

of Z ( j −1)
i and hence we have H
 (
Z ( j −1)
i ′ |Z
( j −1)
{
k∈Si ′, j −1,k<i ′}
)
 = H
 (
Z ( j −1)
i ′ |Z
( j −1)
{k∈Si ′, j −1,k<i }
)

. The second

equality in (4) then follows from parts (1) and (2). The ﬁrst equalities in parts (5) and (6) are
similar to the ﬁrst equality in part (3) with part (6) using the fact that {
k ∈ Si ′, j |k < i ′} = {i } ∪{k ∈ Si , j |k < i }. The second equality follows from the fact that (see Exercise 11.13):

Lemma 11.5.5. There is a one-to-one map from the variables Z
( j −1)
{k∈Si , j ,k<i } to the variables Z
( j )
{
k∈Si , j ,k<i },

and so conditioning on one set is equivalent to conditioning on the other.

To summarize the effect of Proposition 11.5.3 above, let us name the random variables U =
Z ( j −1)
i and V = Z ( j −1)
i ′ and further let A = {Z ( j −1)
k |k ∈ Si , j −1, k < i } and B = {Z ( j −1)
k |k ∈ Si ′, j −1, k < i ′}
.

By the proposition above, the conditional entropies of interest (i.e., those of i and i ′) at the
( j − 1)th stage are H (U |A) and H (V |B ). On the other hand the conditional entropies of interest
one stage later (i.e., at the j th stage) are H (U + V |A, B ) and H (V |A, B,U ). (Here we use that fact
that P2(U ,V ) = (U + V,V ).) By part (2) of Proposition 11.5.3 we also have that (U , A) and (V, B )
are independent of each other. Finally, by examination we also have that (see Exercise 11.14)

Lemma 11.5.6. (U , A) and (V, B ) are identically distributed.

193

So our concern turns to understanding the local polarization of two independent and iden-
tically distributed bits. If one could ignore the conditioning then this is just a problem about
two bits (U ,V ) and their polarization when transformed to (U + V,V ).
In the following lemma, we show how in the absence of conditioning these variables show
local polarization effects. (For our application it will be useful for us to allow the variables to
be not identically distributed, though still independent.) Suppose H (U ) = H (p1) and H (V ) =
H (p2), then notice that H (U + V ) = H (p1 ◦ p2) where

p1 ◦ p2 def
= p1(1 − p2) + p2(1 − p1).

In the following lemma we show how H (p1 ◦ p2) relates to H (p1) and H (p2).

Lemma 11.5.7. Let p1, p2 ∈ [0, 1/2] with p1 < p2 and τ ∈ (0, 1/2). Then we have:

(1) H (p1 ◦ p2) ≥ H (p2).

(2) There exists θ = θ(τ) > 0 such that if H (p1), H (p2) ∈ (τ, 1 − τ) then

H (p1 ◦ p2) − H (p2) ≥ θ.

(3) If H (p1), H (p2) ≤ τ then

H (p1 ◦ p2) ≥ (1 − 9/ log(1/τ))(H (p1) + H (p2)).

In particular, for every c < ∞, if τ ≤ 2−9c then

H (p1) + H (p2) − H (p1 ◦ p2) ≤ (H (p1) + H (p2))/c.

(4) If H (p1), H (p2) ≥ 1 − τ and τ ≤ 1 − H (1/4) then

H (p1 ◦ p2) ≥ 1 − 20τ(1 − H (p2)).

In particular, for every c ′ < ∞, if τ < 1/(20c ′) then

1 − H (p1 ◦ p2) ≤ (1 − H (p2))/c ′.

We defer the proof of the above lemma to Section 11.6.2.
The lemma above essentially proves that H (U +V ) satisﬁes the requirements for local polar-
ization relative to H (U ) and H (V ), but we still need to deal with the conditioning with respect
to A and B . We do this below using some careful applications of Markov’s inequality.

Lemma 11.5.8. If (U , A) and (V, B ) are identical and independent random variables with U ,V
being elements of F2 with H (U |A) = H (V |B ) = H (p), then the following hold:

(1) For every τ > 0 there exists θ > 0 such that if H (p) ∈ (τ, 1 − τ) then

H (U + V |A, B ) ≥ H (p) + θ.

194

(2) For every c < ∞ there exists τ > 0 such that if H (p) ≤ τ then

H (U + V |A, B ) ≥ (2 − 1/c)H (p),

and if H (p) ≥ 1 − τ then
 H (U + V |A, B ) ≥ 1 − 1/c(1 − H (p)).

Proof. Let pa = Pr[U = 1|A = a] so that H (p) = H (U |A) = EA[H (p A)]. Similarly let qb = Pr[V =
1|B = b]. In what follows we consider what happens when A and B are chosen at random. If
H (p A) and H (qB ) are close to their expectations, then the required polarization comes from
Lemma 11.5.7. But if H (p A) or H (qB ) can deviate signiﬁcantly from their expectation, then
polarization happens simply due to the fact that one of them is much larger than the other and
H (U + V |A = a, B = b) ≥ max{H (pa), H (qb)}. The details are worked out below.
We start with part (1). Let θ(·) be the function from part (2) of Lemma 11.5.7 so that if
H (p1), H (p2) ∈ (ρ, 1 − ρ) then H (p1 ◦ p2) − H (p2) ≥ θ(ρ). Given τ > 0 let θ1 = θ(τ/2). We prove

this part for θ = min { θ1
9 , τ2
36
 } > 0.
Let r1 = Pr
A [H (p A) ≤ τ/2],

r2 = Pr
A [H (p A) ∈ (τ/2, 1 − τ/2)],

and r3 = Pr
A [H (p A) ≥ 1 − τ/2].

(Note that since (U , A) and (V, B ) are identically and independently distributed if one replaces
p A by qB in the above equalities, then the equalities still remain valid. We will be implicitly
using this for the rest of the proof.) Since r1 + r2 + r3 = 1, at least one of them must be greater
than or equal to 1/3. Suppose r2 ≥ 1/3, then we have with probability at least 1/9, both H (p A) ∈
(τ/2, 1 − τ/2) and H (qB ) ∈ (τ/2, 1 − τ/2). Let a, b be such that H (pa), H (qb) ∈ (τ/2, 1 − τ/2). Then,
since U + V ∼ Bern(pa ◦ pb), by Lemma 11.5.7 part (2),

H (U + V |A = a, B = b) ≥ H (pa) + θ1.

And by Lemma 11.5.7 part (1), we have for all a, b,

H (U + V |A = a, B = b) ≥ H (pa).

Putting it together, we have

H (U + V |A, B ) ≥ EA[p A] + 1
9 · θ1 = H (p) + θ1
9 .

Next we consider the case where r3 ≥ 1/3. Now consider the probability that PrA[H (p A) ≤
1 − τ]. Notice that

1 − τ ≥ H (p) ≥ (1 − r3 − Pr
A [H (p A) ≤ 1 − τ]) · (1 − τ) + r3 · (1 − τ/2).

195

Rearranging we conclude
 Pr
A [H (p A) ≤ (1 − τ)] ≥ r3τ
2(1 − τ) ≥ τ
6 .

Thus with probability at least τ/18 we have A such that H (p A) ≤ (1−τ) and B such that H (qB ) ≥
1 − τ/2. Let a, b be such that H (pa) ≤ 1 − τ and H (qb) ≥ 1 − τ/2. We have (from part (1) of
Lemma 11.5.7)
 H (U + V |A = a, B = a) ≥ H (qb) ≥ H (pa) + τ
2 .

We conclude that in this case

H (U + V |A, B ) ≥ EA[H (p A)] + τ2

36 = H (p) + τ2

36 .

The case r1 ≥ 1/3 is similar and also yields

H (U + V |A, B ) ≥ H (p) + τ2/36.

Thus in all cases we have H (U + V |A, B ) ≥ H (p) + θ,

which completes the proof of part (1).
We now turn to part (2). We only prove the case where H (p) ≤ τ. The case where H (p) ≥ 1−τ
is similar and we omit that part (see Exercise 11.15). Given c < ∞, let τ′ = τ(4c) be the constant
from part (3) of Lemma 11.5.7 for constant 4c, so that if H (p1), H (p2) ≤ τ′ then

H (p1 ◦ p2) ≥ (
1 − 1
4c
 ) · (H (p1) + H (p2)) .

Now let τ = τ′
2c and H (p) ≤ τ. Deﬁne
 α = Pr
A
 [H (p A) ≥ τ′] .

By Markov’s inequality (Lemma 3.1.4) we have α ≤ 1/(2c). Let

γ = EA [H (p A)|H (p A) ≥ τ′] .

and δ = EA [H (p A)|H (p A) < τ′] .

We have H (p) = γα + δ(1 − α). (11.13)

We divide our analysis into four cases depending on whether H (p A) ≥ τ′ or not, and whether
H (qB ) ≥ τ′ or not. Let S11 denote the event that H (p A) ≥ τ′ and H (qB ) ≥ τ′ and S00 denotes the
event that H (p A) < τ′ and H (qB ) < τ′. Deﬁne S10 and S01 similarly.

196

We start with the case of S10. Let a, b be such that H (pa) ≥ τ′ and H (qb) < τ′. We have by part
(1) of Lemma 11.5.7, H (U + V |A = a, B = b) ≥ H (U |A = a) = H (pa) (and similarly H (U + V |A =
a, B = b) ≥ H (qb). Thus taking expectation after conditioning on (A, B ) ∈ S10 we have

E(A,B )|(A,B )∈S10 [H (U + V |A, B )] ≥ E [H (p A)|H (p A) ≥ τ′] = γ.

Similarly we have E(A,B )|(A,B )∈S01 [H (U + V |A, B )] ≥ γ

as well as E(A,B )|(A,B )∈S11 [H (U + V |A, B )] ≥ γ.

Note that S11 ∪ S10 ∪ S01 happen with probability 2α − α
2. Now we turn to S00. Let a, b be
such that H (pa), H (qb) < τ′. By Lemma 11.5.7 part (3) we have H (U + V |A = a, B = b) ≥ (1 −
1/(4c)) (H (pa) + H (qb))
. Taking expectations conditioned on (A, B ) ∈ S00 we get

E(A,B )|(A,B )∈S00 [H (U + V |A, B )] ≥ (
1 − 1
4c
 ) · (EA [H (p A)|H (p A) < τ′] + EB [H (qB )|H (qB ) < τ′])

= (
1 − 1
4c
 ) · 2δ.

Note ﬁnally that S00 happens with probability (1 − α)2. Combining the four cases we have

H (U + A|A, B ) ≥ (2α − α
2)γ + (1 − α)2 (
1 − 1
4c
 ) (2δ)

= 2αγ + (1 − α)2δ − α
2γ − (α)(1 − α)δ − 1
4c · (1 − α)22δ

= 2H (p) − α · H (p) − 1
2c · (1 − α)((1 − α)δ).

In the above, the last equality follows from (11.13). Part (2) now follows by using (1−α)δ ≤ H (p)
(which in turn follows from (11.13)) and α ≤ 1/(2c).

We are now ready to prove the local polarization lemma.

Proof of Lemma 11.5.1. Recall that X j = EI ∼[n][Z ( j )
I ]. Let X j = H (p). Note that conditioned on
the value of X j , for any ( j +1)-level siblings i < i ′, I is equally likely to equal i or i ′. Conditioning

on I ∈ {i , i ′}, with probability 1/2, I = i and with probability 1/2 I = i ′. Let U = Z ( j )
i , V = Z ( j )
i ′ ,

A = {Z ( j )
k |k < i , k ∈ Si , j } and B = {Z ( j )
k |k < i ′, k ∈ Si ′, j } then if I = i , X j = H (U |A) (this follows

from Lemma 11.5.3 part (3)) and if I = i ′ then X j = H (V |B ) (this follows from Lemma 11.5.3 part
(4)). Furthermore if I = i then X j +1 = H (U + V |A, B ) (this follows from (11.11) and parts (1) and
(5) from Lemma 11.5.3) and if I = i ′ then X j +1 = H (V |A, B,U ) (this follows from (11.11), parts
(1) and (6) from Lemma 11.5.3 and the fact that V |U and V |U + V have the same distribution).
With this setup, we are now ready to prove that the sequence X0, X1, . . . , satisfy the conditions
of local polarization, and furthermore are simple.

197

We argue the conditions hold for each conditioning I ∈ {i , i ′} and so hold without the con-
ditioning (the latter holds because the pairs {i , i ′} make a disjoint cover of [n] and hence for a
random I ∼ [n] is equally likely to fall in one of these pairs). The condition E[X j +1|X j = a] = a
follows from the fact that there is a bijection from (U ,V ) to (U + V,V ), and so

H (U + V |A, B ) + H (V |A, B,U ) = H (U |A) + H (V |B ).

Indeed, note that 2a is the RHS and 2X j +1 is the LHS of the above equality.
Now note that (see Exercise 11.16):

Lemma 11.5.9. (U , A) and (V, B ) are independently and identically distributed.

The variance in the middle condition follows from Lemma 11.5.8 part (1) and the suction at
the ends condition follows from Lemma 11.5.8 part (2). Finally simplicity follows from the fact
that with probability 1/2, X j = H (U + V |A, B ) and with probability 1/2, X j = H (V |A, B,U ).

11.5.3 Local vs. Global Polarization

Finally we prove Lemma 11.5.2 which shows that simple local polarization implies strong polar-
ization. We prove this part in two phases. First, we show that in the ﬁrst t /2 steps, the sequence
shows moderate polarization — namely, with all but exponentially small probability X t /2 is an
inverse exponential in t , but with a small constant base (so X t ̸∈ (
αt
1, 1 − αt
1) for some α1 < 1, but
α1 is close to 1). Next we show that conditioned on this moderate polarization, the sequence
gets highly polarized (so X t ̸∈ (
γt , 1 − γt ) for any γ > 0 of our choice), again with an exponentially
small failure probability. We start with part (1).
In what follows, let γ > 0 be given and let

c = max {
4, γ
8

16
 } .

Let τ = τ(c) be given by condition (3) of the deﬁnition of Local Polarization (Deﬁnition 11.5.2)
and
 θ = min {
1 − 1
c , θ(τ)}

where θ(τ) is the constant given by condition (2) of the same deﬁnition.
We start with the ﬁrst phase. We consider a potential function

φ j def
= min {√X j , √
1 − X j } .

We ﬁrst notice that φ j is expected to drop by a constant factor in each step of polarization.

Lemma 11.5.10.
 E [
φ j +1|φ j = a] ≤ (
1 − θ2

16
 ) · a.

198

Proof. Without loss of generality assume X j ≤ 1/2 (see Exercise 11.17) and so a = φ j = √X j and
so X j = a2. Using the simplicity of the sequence X0, . . . as well as the fact that E [X j +1|X j = a] =
a, we have that there exists δ such that X j +1 = a2 + δ with probability 1/2 and a2 − δ with
probability 1/2. Furthermore, if X j ≤ τ, by the unbiasedness and suctions at the ends condi-
tions, we have δ ≥ (1 − 1/c)a2 and if X j > τ by the variance in the middle condition, we have
δ ≥ θ(τ) ≥ θ(τ)a2. Thus in either case we have

δ ≥ θa2. (11.14)

We now bound E [
φ j +1] as follows:

E [
φ j +1] ≤ E [√X j +1]

= 1
2
 √a2 + δ + 1/2√a2 − δ

= a
2
 


√

1 + δ
a2 +
 √

1 − δ
a2
 



≤ a
2
 (1 + δ
2a2 − δ
2

16a4 + 1 − δ
2a2 − δ
2

16a4
 )

= a (
1 − δ
2

16a4
 )

≤ a (
1 − θ2

16
 ) .

In the above, the ﬁrst inequality follows from Lemma B.1.5 while the second inequality follows
from (11.14).

Lemma 11.5.11 (Weakly Polynomial Polarization). There exists α1 < 1 such that for all even t ,
we have Pr [X t /2 ∈ (αt
1, 1 − αt
1)] ≤ αt
1.

Proof. We ﬁrst prove by induction on j that

E [
φ j ] ≤ (1 − θ2

16
 ) j .

This is certainly true for j = 0 since φ0 ≤ 1. For higher j , by Lemma 11.5.10 we have

E [
φ j ] ≤ (
1 − θ2

16
 ) E [
φ j −1] ≤ (
1 − θ2

16
 ) j

as claimed. Let
 β =
 √

1 − θ2

16

199

and α1 = √
β (note that α1 < 1). By our claim, we have E [φt /2] ≤ βt . By Markov’s inequality
(Lemma 3.1.4), we now get that
 Pr [
φt /2 ≥ αt
1] ≤ βt

αt
1 = αt
1.

Finally we note that if φt /2 ≤ αt
1 then X t /2 ̸∈ (α
2t
1 , 1 − α
2t
1 ) and so in particular X t /2 ̸∈ (αt
1, 1 − αt
1).
We conclude that the probability that X t /2 ∈ (αt
1, 1 − αt
1) is at most αt
1, yielding the lemma.

We now turn to phase two of the polarization. Here we use the fact that if X t /2 is much
smaller than τ, then X j is very unlikely to become larger than τ for any t /2 ≤ j ≤ t . Furthermore
if it does not ever become larger than τ then X t is very likely to be close to its expected value
(which grows like γt ). The following lemmas provide the details. In the following recall that
τ = τ(c) where c ≥ 4.

Lemma 11.5.12. For all λ > 0, if X0 ≤ λ, then the probability there exists j > 0 such that X j ≥ τ is
at most λ/τ. Similarly if X0 ≥ 1 − λ, then the probability there exists j > 0 such that X j ≤ 1 − τ is
at most λ/τ.

The lemma above is a special case of Doob’s inequality for martingales. We give the (simple)
proof below.

Proof. We give the proof for the case X0 ≤ λ. The case X0 ≥ 1 − λ is symmetrical (see Exer-
cise 11.18). Notice that we wish to show that for every integer T > 0

Pr [ max
0≤t ≤T {X t } ≥ τ] ≤ λ/τ.

Let us create a related sequence of variables Yi as follows. Let Y0 = X0 and for i ≥ 1, if Yi −1 < τ
then Yi = Xi , else Yi = Yi −1. Note that for every i and a, by the simplicity of Xi ’s, we have
E [Yi |Yi −1 = a] = a. Note further that max0≤t ≤T {X t } ≥ τ if and only if YT ≥ τ. Thus

Pr [ max
0≤t ≤T {X t } ≥ τ] = Pr [YT ≥ τ] ≤ E [YT ]
τ ,

where the ﬁnal inequality is Markov’s inequality (Lemma 3.1.4). But

E [YT ] = E [YT −1] = · · · = E [Y0] = E [X0] ≤ λ

and this yields the lemma.

Lemma 11.5.13 (Weak to Strong Polarization). There exists α2 < 1 such that for every λ > 0 if
X0 ̸∈ (λ, 1 − λ), then the probability that X t /2 ∈ (γt , 1 − γt ) is at most λ/τ + αt
2.

Proof. Again we consider the case X0 ≤ λ with the other case being symmetrical (see Exer-
cise 11.19).
Let Zi = 1 if Xi < Xi −1 and 0 otherwise. For simple sequences, notice that Zi ’s are indepen-
dent and 1 with probability 1/2. Let Z = ∑t /2
i =1 Zi . We consider two possible “error” events. E1 is

200

the event that there exists 1 ≤ j ≤ t /2 such that X j ≥ τ, and E2 is the event that Z ≤ t /8. Note
that by Lemma 11.5.12, E1 happens with probability at most λ/τ and (by the Chernoff bounds–
Theorem 3.1.6) E2 happens with probability at most αt
2 for some α2 < 1. Now, if event E1 does
not occur, then X t /2 ≤ 2t /2 · c −Z X0 ≤ 2t /2c −Z .

The ﬁrst inequality follows from the subsequent argument. Using simplicity, we have with prob-
ability 1/2, X1 ≤ (1/c)X0 ≤ X0/4 (because of the suction at the ends condition) and with proba-
bility 1/2 X1 ≤ 2X0 (this follows the bound in the other case and the unbiasedness of the Xi s).
Further if E2 also does not occur we have

X t /2 ≤ 2t /2 · c −t /8 ≤ γt

by the choice of c = 1/(2/γ
2)4.

Proof of Lemma 11.5.2. Recall that we wish to show, given γ > 0, that there exists α < 1 and
β < ∞ such that for all t we have
 Pr [X t ∈ (
γt , 1 − γt )] ≤ β · αt .

Let α1 < 1 be the constant from Lemma 11.5.11. Let α2 < 1 be the constant from Lemma 11.5.13.
We prove this for α = max{α1, α2} < 1 and β = 2 + 1/τ < ∞.
Let E be the event that X t /2 ∈ (αt
1, 1 − αt
1). By Lemma 11.5.11 we have that Pr [E ] ≤ αt
1. Now
conditioned of E not occurring, using Lemma 11.5.13 with λ = αt
1, we have Pr [X t ∈ (γt , 1 − γt )
] ≤
αt
1/τ + αt
2. Thus putting the two together we get

Pr [X t ∈ (γt , 1 − γt )] ≤ αt
1 + αt
1
τ + αt
2 ≤ αt + αt

τ + αt = β · αt ,

as desired.

11.6 Entropic Calculations

In this section, we present the omitted proofs on various properties of entropy and probability
that mostly need some calculations.

11.6.1 Proof of Proposition 11.3.1

We begin with the ﬁrst part, which is a straightforward calculation expanding the deﬁnition.
For any i in the support of X , let pi denote PrX [X = i ] and let x = argmaxi {pi } be the value
maximizing this probability. Let px = 1 − γ. We wish to show that γ ≤ α. We now perform some
crude calculations that lead us to this bound.
If γ ≤ 1/2 we have
 α ≥ H (X )
 201

= ∑

i pi log 1
pi

≥ ∑

i ̸=x pi log 1
pi (11.15)

≥ ∑

i ̸=x pi log 1
∑ j ̸=x p j (11.16)

=
 ( ∑

i ̸=x pi
 )
 · log
 ( 1
∑ j ̸=x p j
 )

= γ · log 1/γ

≥ γ, (11.17)

as desired. In the above, (11.15) follows since all summands are non-negative, (11.16) follows
since for every i ̸= x, pi ≤ ∑ j ̸=x p j and (11.17) follows since γ ≤ 1/2 and so log 1/γ ≥ 1.
Now if γ > 1/2 we have a much simpler case since now we have

α ≥ H (X )

= ∑

i pi log 1
pi

≥ ∑

i pi log 1
px (11.18)

= log 1
px (11.19)

= log 1
1 − γ

≥ 1. (11.20)

(In the above, (11.18) follows since pi ≤ px, (11.19) follows since ∑
i pi = 1 and (11.20) follows
from the assumption that γ ≥ 1/2.) But γ is always at most 1 so in this case also we have α ≥ 1 ≥ γ
as desired.
We now consider the second part, which follows from the previous part via a simple averag-
ing argument. Given y and i , let pi ,y = PrX [X = i |Y = y] and let xy = argmaxi {pi ,y } be the value
maximizing this probability. Let γy = 1 − pxy ,y and note that γ = EY [γY ]. Let αy = H (X |Y = y)
and note again we have α = EY [αY ]. By the ﬁrst part, we have for every y, γy ≤ αy and so it
follows that γ = EY [γY ] ≤ EY [αY ] = α.

11.6.2 Proof of Lemma 11.5.7

The lemma follows in a relatively straightforward manner with parts (3) and (4) using Lemma B.2.3.
Part (1) is immediate from the monotonicity of the entropy function in the interval [0, 1/2]
(see Exercise 11.6). For 0 ≤ p1, p2 ≤ 1/2 we have p2 ≤ p1 ◦ p2 ≤ 1/2 and so (see Exercise 11.20)

H (p1 ◦ p2) ≥ H (p2). (11.21)

202

Next we turn to part (2). Let H −1(x) = p such that 0 ≤ p ≤ 1/2 such that H (p) = x. Note H −1

is well deﬁned and satisﬁes H −1(x) > 0 if x > 0 and H −1(x) < 1/2 if x < 1. Let

α = α(τ) = H −1(τ)(1 − 2H −1(1 − τ))

and β = β(τ) = 2H −1(1 − τ)(1 − H −1(1 − τ))

and γ = γ(τ) = log((1 − β)/β).

Note that α > 0 and β < 1/2 and so γ > 0. We prove that H (p1 ◦ p2) − H (p2) ≥ α · γ, and this will
yield part (2) for θ = θ(τ) = α · γ > 0.
First note that since H (p1), H (p2) ∈ (τ, 1 − τ), we have p1, p2 ∈ (H −1(τ), H −1(1 − τ)). Thus

p1 ◦ p2 − p2 = p2(1 − 2p1) + p1 − p2 = p1(1 − 2p2) ≥ H −1(τ)(1 − 2H −1(1 − τ)) = α.

Next we consider minp2≤q≤p1◦p2{H ′(q)}. Note that by Exercise 11.21 H ′(q) = log((1 − q)/q) and
this is minimized when q is maximum. The maximum value of q = p1 ◦ p2 is in turn maximized
by using the maximum values of p1, p2 = H −1(1 − τ). Thus we have that minp2≤q≤p1◦p2{H ′(q)} ≥
H ′(β) = γ. By elementary calculus we now conclude that

H (p1 ◦ p2) − h(p2) ≥ (p1 ◦ p2 − p2) · min
p2≤q≤p1◦p2{H ′(q)} ≥ α · γ = θ.

This concludes the proof of part (2).
Next we move to part (3). For this we ﬁrst describe some useful bounds on H (p). On the one
hand we have H (p) ≥ p log 1/p. For p ≤ 1/2 we also have −(1 − p) log(1 − p) ≤ (1/ ln 2)(1 − p)(p +
p 2) ≤ (1/ ln 2)p ≤ 2p. And so we have H (p) ≤ p(2 + log 1/p).
Summarizing, we have for p ≤ 1/2,

p log(1/p) ≤ H (p) ≤ p log(1/p) + 2p. (11.22)

We now consider H (p1) + H (p2) − H (p1 ◦ p2). We have

H (p1) + H (p2) − H (p1 ◦ p2)

≤ p1(log(1/p1) + 2) + p2(log(1/p2) + 2) − (p1 ◦ p2) log(1/(p1 ◦ p2)) (11.23)

≤ p1(log(1/p1) + 2) + p2(log(1/p2) + 2) − (p1 + p2 − 2p1p2) log(1/(2p2)) (11.24)

= p1 log(2p2/p1) + p2 log(2p2/p2) + 2p1p2 log(1/(2p2)) + 2(p1 + p2)

≤ p1 log(p2/p1) + 2p1p2 log(1/(p2)) + 6p2 (11.25)

≤ 2p1H (p2) + 7p2 (11.26)

≤ 2p1H (p2) + 7H (p2)/ log(1/p2) (11.27)

≤ 9H (p2)/ log(1/τ). (11.28)

In the above, (11.23) follows from (11.22), (11.24) follows from the fact that p1 ◦ p2 ≤ p1 + p2 ≤
2p2, (11.25) follows from the fact that 3(p1+p2) ≤ 6p2, (11.26) follows from the fact that p1 log(p2/p1) ≤

203

p2, (11.27) follows from (11.22) and (11.28) follows from the subsequent argument. Indeed by
deﬁnition of τ and (11.22) we have p2 log(1/p2) ≤ τ. Using the fact that p2 ≤ 1/2, this implies
that p2 ≤ τ, which in turn implies log(1/p2) ≥ log(1/τ). Similarly, we have p1 log(1/p1) ≤ τ,
which again with p1 ≤ 1/2, we have p1 ≤ τ ≤ 1/ log(1/τ) (where the second equality uses the fact
that τ < 1/2). This concludes the proof of part (3).
Finally we turn to part (4). Here we let H (pi ) = 1 − yi and pi = 1/2 − xi for i ∈ {1, 2}. Since
τ ≤ 1 − H (1/4) and H (pi ) ≥ 1 − τ, we have xi ≤ 1/4. By Lemma B.2.4, we have 1 − 5x2 ≤ H (1/2 −
x) ≤ 1 − x2 for x ≤ 1/4. Returning to our setup if 1 − τ ≥ H (1/4) and 1 − yi = H (pi ) ≥ 1 − τ, and
pi = 1/2 − xi , then 1 − x2
i ≥ 1 − yi , so
 xi ≤ pyi . (11.29)

Furthermore, p1 ◦ p2 = 1/2 − 2x1x2 and

H (p1 ◦ p2) = H (1/2 − 2x1x2)

≥ 1 − 20(x1x2)2

≥ 1 − 20y1 y2
= 1 − 20(1 − H (p1))(1 − H (p2))

≥ 1 − 20τ(1 − H (p2)),

where the second inequality follows from (11.29). This yields part (4).

11.7 Summary and additional information

In this chapter we showed how a very simple phenomenon leads to a very effective coding
and decoding mechanism. Even the idea of reducing error-correction to compression is novel,
though perhaps here the novelty is in the realization that this can idea can be put to good use.
The idea of using polarization to create a compression scheme, as well as the exact procedure
to create polarization are both radically novel, and remarkably effective.
Our description of this compression mechanism is nearly complete. The one omission is
that we do not show which columns of the matrix Pn should be used to produce the compressed
output — we only showed that a small subset exists. The reader should know that this aspect
can also be achieved effectively, and this was ﬁrst shown by Tal and Vardy [98], and adapted to
the case of strong polarization by Guruswami and Xia. Speciﬁcally there is a polynomial time
algorithm that given p, ε and c outputs n ≤ poly(1/ε), Pn ∈ Fn×n
2 and a set S ⊆ [n] such that
Pn is (ε, n−c )-polarizing for Bern(p)n with unpredictable columns S, and |S| ≤ (H (p) + ε)n. The
details are not very hard given the work so far, but still out of scope of this chapter.
Our analysis of local polarization differs from the literature in the absence of the use of “Mrs.
Gerber’s Lemma” due to Wyner and Ziv, which is a convexity claim that provides a convenient
way to deal with conditional entropies (essentially implying that the conditioning can be ig-
nored). In particular, it yields the following statement whose proof can be found as Lemma 2.2
in [21].
 204

Lemma 11.7.1. If (U , A) and (V, B ) are independent and U ,V are binary valued random vari-
ables with H (U |A) = H (p) and H (V |B ) = H (q), then H (U + V |A, B ) ≥ H (p(1 − q) + q(1 − p)).

The proof of the lemma uses the convexity of the function H (a ◦ H −1(x)) which turns out to
have a short, but delicate and technical proof which led us to omit it here. This lemma would
be a much cleaner bridge between the unconditioned polarization statement (Lemma 11.5.7)
and its conditional variant (Lemma 11.5.8). Unfortunately Lemma 11.7.1 is known to be true
only in the binary case whereas our proof method is applicable to larger alphabets (as shown
by Guruswami and Velingker [49]).

11.8 Exercises

Exercise 11.1. Prove Theorem 11.1.2 (assuming Theorem 11.1.1).

Exercise 11.2. Argue that the matrices G and G
∗ in Proposition 11.2.1 exist.

Exercise 11.3. Show that there exists a non-linear comrepssion scheme for Bern(p)n of rate at
most H (p) + ε.

Exercise 11.4. Prove (11.5).

Exercise 11.5. Prove (11.9).

Exercise 11.6. Show that H (p) is monotonically increasing for 0 ≤ p ≤ 1
2 .

Exercise 11.7. Give an explicit description of the polarizing matrix Pn such that Pn(Z) = Z · Pn.
Further, prove that Pn is its own inverse.

Exercise 11.8. Show that p +(p1, p2) = p1(1 − p2) + (1 − p1)p2.

Exercise 11.9. Show that
 p |(p1, p2, 0) = p1p2/(p1p2 + (1 − p1)(1 − p2))

and p |(p1, p2, 1) = (1 − p1)p2/((1 − p1)p2 + p1(1 − p2)).

Exercise 11.10. Prove Corollary 11.4.5.

Exercise 11.11. Prove (11.12).

Exercise 11.12. Prove Lemma 11.5.4.

Exercise 11.13. Prove Lemma 11.5.5.

Exercise 11.14. Prove Lemma 11.5.6.

Exercise 11.15. Prove part (2) of Lemma 11.5.8 for the case H (p) ≥ 1 − τ.

Exercise 11.16. Prove Lemma 11.5.9.

Exercise 11.17. Prove Lemma 11.5.10 for the case X j > 1/2.

205

Exercise 11.18. Prove Lemma 11.5.12 when X0 ≥ 1 − λ.

Exercise 11.19. Prove Lemma 11.5.13 when X0 > λ.

Exercise 11.20. Prove (11.21).

Exercise 11.21. H ′(q) = log((1 − q)/q).

11.9 Bibliographic Notes

Polar codes were invented in the remarkable paper by Arıkan [4] where he showed that they
achieve capacity in the limit of large block lengths n → ∞ with O(n log n) encoding time and
O(n log n) decoding complexity via the successive cancellation decoder. In particular, Arıkan
proved that the transform P ⊗t
2 is polarizing in the limit of t → ∞, in the sense that for any ﬁxed
γ > 0, the fraction of indices for which H (Wi | W<i ) ∈ (γ, 1 − γ), where W = P ⊗t
2 Z, is vanishing for
large t . In fact, Arıkan showed that one could take γ = γ(t ) = 2−5t /4, which led to an upper bound
of n · γ = O(1/n1/4) (block) decoding error probability for the successive cancellation decoder.
Soon afterwards, Arıkan and Teletar proved that one can take γ < 2−Ω(2βt ) for any β < 1/2, which
led to improved decoding error probability of 2−n−β as a function of the block length n = 2t . The
fall-off of the parameter γ in n was referred to as the “rate” of (limiting) polarization.
These works considered the basic 2 × 2 transform P2 and binary codes. More general trans-
forms, and non-binary codes, were considered later in [88, 64, 74]. These results showed that
limiting polarization is universal, as long as some minimal conditions are met by the basic ma-
trix being tensored.
The 2012 survey by ¸Sa¸so˘glu is an excellent and highly recommended resource for some of
the early works on polarization and polar codes [21]. Polar codes were widely described as the
ﬁrst constructive capacity achieving codes. Further, polarization was also found to be a versatile
technique to asymptotically resolve several other fundamental problems in information theory
such as lossless and lossy source coding problem, coding for broadcast, multiple access, and
wiretap channels, etc.
However, none of these works yield effective ﬁnite length bounds on the block length n
needed to achieve rates within ε of capacity, i.e., a rate at least 1 − h(p) − ε for the binary sym-
metric channel with crossover probability p. Without this it was not clear in what theoretical
sense polar codes are better than say Forney’s construction, which can also get within any de-
sired ε > 0 of capacity, but have complexity growing exponentially in 1/ε2 due to the need for
inner codes of length 1/ε2 that are decoded by brute-force.
A ﬁnite length analysis of polar codes, and strong polarization where the probability of not
polarizing falls off exponentially in t , and thus is polynomially small in the block length n =
2t , was established in independent works by Guruswami and Xia [50] and Hassani, Alishahi,
and Urbanke [54]. The latter tracked channel “Bhattacharyya parameters” whereas the former
tracked conditional entropies (as in the present chapter) which are a bit cleaner to deal with as
they form a martingale. This form of fast polarization made polar codes the ﬁrst, and so far only

206

known, family with block length and complexity scaling polynomially in 1/ε where ε is the gap
to capacity,
This analyis of strong polarization in the above works applied only to the 2 × 2 transofrm
and binary case. The strong polarization of the basic 2 × 2 transform was also established for
all prime alphabets in [49], leading to the ﬁrst construction of codes achieving the symmetric
capacity of all discrete memoryless channels (for prime alphabets) with polynomial complexity
in the gap to capacity. However, these analyses relied on rather speciﬁc inequalities (which were
in particular somewhat painful to establish for the non-binary case) and it was not clear what
exactly made them tick.
The recent work of the authors and Błasiok and Nakkiran [5] gave a modular and concep-
tually clear analysis of strong polarization by abstracting the properties needed from each local
step to conclude fast global polarization. This made the demands on the local evolution of the
conditional entropies rather minimal and qualitative, and enabled showing strong polarization
and polynomially fast convergence to capacity for the entire class of polar codes, not just the
binary 2 × 2 case. We followed this approach in this chapter, and in particular borrowed the
concepts of variance in the middle and suction at the ends for local polarization from this work.
However, we restrict attention to the basic 2 × 2 transform, and the binary symmetric channel,
and gave elementary self-contained proofs of the necessary entropic inequalities needed to es-
tablish the properties required of the local polarization step.
Another difference in our presentation is that we described the successive cancellation de-
coder for the polarizing transform P ⊗t
2 , which leads to clean recursive description based on a
more general primitive of decoding copies of independent but not necessary identical random
variables. In contrast, in many works, including Arıkan’s original paper [4], the decoding is de-
scribed for the transform followed by the bit reversal permutation. The polarization property
of the bit reversed transform is, however, notationally simpler to establish. Nevertheless, the
transform P ⊗t
2 commutes with the bit reversal permutation, so both the transforms, with or
without bit reversal, end up having identical polarization properties.

207208

Part IV

The Algorithms

209

Chapter 12

Decoding Concatenated Codes

In this chapter we study Question 10.3.1. Recall that the concatenated code Cout ◦Cin consists of
an outer [N , K , D]Q=q k code Cout and an inner [n, k, d ]q code Cin, where Q = O(N ). (Figure 12.1
illustrates the encoding function.) Then Cout ◦ Cin has design distance Dd and Question 10.3.1
asks if we can decode concatenated codes up to half the design distance (say for concatenated
codes that we saw in Section 10.2 that lie on the Zyablov bound). In this chapter, we begin
with a very natural unique decoding algorithm that can correct up to Dd /4 errors. Then we
will consider a more sophisticated algorithm that will allow us to answer Question 10.3.1 in the
afﬁrmative.

12.1 A Natural Decoding Algorithm

We begin with a natural decoding algorithm for concatenated codes that “reverses" the encod-
ing process (as illustrated in Figure 12.1). In particular, the algorithm ﬁrst decodes the inner
code and then decodes the outer code.

For the time being let us assume that we have a polynomial time unique decoding algo-

rithm DCout : [q k ]N → [q k ]K for the outer code that can correct up to D/2 errors.

This leaves us with the task of coming up with a polynomial time decoding algorithm for the
inner code. Our task of coming up with such a decoder is made easier by the fact that the
running time needs to be polynomial in the ﬁnal block length. This in turn implies that we
would be ﬁne if we pick a decoding algorithm that runs in singly exponential time in the inner
block length as long as the inner block length is logarithmic in the outer code block length.
(Recall that we put this fact to good use in Section 10.2 when we constructed explicit codes on
the Zyablov bound.) Note that the latter is what we have assumed so far and thus, we can use
the Maximum Likelihood Decoder (or MLD) (e.g. its implementation in Algorithm 2, which we
will refer to as DCin). Algorithm 13 formalizes this algorithm.
It is easy to check that each step of Algorithm 13 can be implemented in polynomial time.
In particular,
 211

Decoding of Cout ◦ Cin

m1 m2 mK

DCout

DCin DCin DCin

m1 m2 mK

Cout(m)1 Cout(m)2 Cout(m)N

Cin (Cout(m)1) Cin (Cout(m)2) Cin (Cout(m)N )

Cout

Cin Cin Cin

y ′
1

y1
 y ′
2

y2
 y ′
N

yN

y
′

y
 Encoding of Cout ◦ Cin

Figure 12.1: Encoding and Decoding of the concatenated code Cout ◦ Cin. DCout is a unique
decoding algorithm for Cout and DCin is a unique decoding algorithm for the inner code (e.g.
MLD).

Algorithm 13 Natural Decoder for Cout ◦Cin

INPUT: Received word y = (y1, · · · , yN ) ∈ [q n]N

OUTPUT: Message m′ ∈ [q k ]K

1: y
′ ← (y ′
1, · · · , y ′
N ) ∈ [q k ]N where

Cin (y ′
i ) = DCin (yi ) 1 ≤ i ≤ N .

2: m′ ← DCout (
y
′)

3: RETURN m′
 212

1. The time complexity of Step 1 is O(nq k ), which for our choice of k = O(log N ) (and con-
stant rate) for the inner code, is (nN )
O(1) time.

2. Step 2 needs polynomial time by our assumption that the unique decoding algorithm
DCout takes N O(1) time.

Next, we analyze the error-correction capabilities of Algorithm 13:

Proposition 12.1.1. Algorithm 13 can correct < Dd
4 many errors.

Proof. Let m be the (unique) message such that ∆ (
Cout ◦Cin (m) , y
) < Dd
4 .
We begin the proof by deﬁning a bad event as follows. We say a bad event has occurred (at
position 1 ≤ i ≤ N ) if yi ̸= Cin (Cout (m)i ). More precisely, deﬁne the set of all bad events to be

B = {
i |yi ̸= Cin (Cout (m)i )} .

Note that if |B| < D
2 , then the decoder in Step 2 will output the message m. Thus, to com-
plete the proof, we only need to show that |B| < D/2. To do this, we will deﬁne a superset
B′ ⊇ B and then argue that |B′| < D/2, which would complete the proof.
Note that if ∆ (yi ,Cin (Cout (m)i )) < d
2 then i ̸∈ B (by the proof of Proposition 1.4.1)– though
the other direction does not hold. We deﬁne B′ to be the set of indices where i ∈ B′ if and only
if
 ∆ (yi ,Cin (Cout (m)i )) ≥ d
2 .

Note that B ⊆ B′.
Now by deﬁnition, note that the total number of errors is at least |B′| · d
2 . Thus, if |B′| ≥ D
2 ,
then the total number of errors is at least D
2 · d
2 = Dd
4 , which is a contradiction. Thus, |B′| < D
2 ,
which completes the proof.

Note that Algorithm 13 (as well the proof of Proposition 12.1.1) can be easily adapted to work
for the case where the inner codes are different, e.g. Justesen codes (Section 10.3).
Thus, Proposition 12.1.1 and Theorem 12.3.3 imply that

Theorem 12.1.2. There exist an explicit linear code on the Zyablov bound that can be decoded
up to a fourth of the Zyablov bound in polynomial time.

This of course is predicated on the fact that we need a polynomial time unique decoder for
the outer code. Note that Theorem 12.1.2 implies the existence of an explicit asymptotically
good code that can be decoded from a constant fraction of errors.
We now state two obvious open questions. The ﬁrst is to get rid of the assumption on the
existence of DCout:

Question 12.1.1. Does there exist a polynomial time unique decoding algorithm for outer
codes, e.g. for Reed-Solomon codes?
 213

Next, note that Proposition 12.1.1 does not quite answer Question 10.3.1. We move to an-
swering this latter question next.

12.2 Decoding From Errors and Erasures

Now we digress a bit from answering Question 10.3.1 and talk about decoding Reed-Solomon
codes. For the rest of the chapter, we will assume the following result.

Theorem 12.2.1. An [N , K ]q Reed-Solomon code can be corrected from e errors (or s erasures) as
long as e < N −K +1
2 (or s < N − K + 1) in O(N 3) time.

We defer the proof of the result on decoding from errors to Chapter 15 and leave the proof
of the erasure decoder as an exercise. Next, we show that we can get the best of both worlds by
correcting errors and erasures simultaneously:

Theorem 12.2.2. An [N , K ]q Reed-Solomon code can be corrected from e errors and s erasures in
O(N 3) time as long as 2e + s < N − K + 1. (12.1)

Proof. Given a received word y ∈ (Fq ∪ {?})N with s erasures and e errors, let y
′ be the sub-vector
with no erasures. This implies that y
′ ∈ FN −s
q is a valid received word for an [N − s, K ]q Reed-
Solomon code. (Note that this new Reed-Solomon code has evaluation points that correspond-
ing to evaluation points of the original code, in the positions where an erasure did not occur.)
Now run the error decoder algorithm from Theorem 12.2.1 on y
′. It can correct y
′ as long as

e < (N − s) − K + 1
2 .

This condition is implied by (12.1). Thus, we have proved one can correct e errors under (12.1).
Now we have to prove that one can correct the s erasures under (12.1). Let z
′ be the output after
correcting e errors. Now we extend z
′ to z ∈ (Fq ∪{?})N in the natural way. Finally, run the erasure
decoding algorithm from Theorem 12.2.1 on z. This works as long as s < (N − K + 1), which in
turn is true by (12.1).
The time complexity of the above algorithm is O(N 3) as both the algorithms from Theo-
rem 12.2.1 can be implemented in cubic time.

Next, we will use the above errors and erasure decoding algorithm to design decoding algo-
rithms for certain concatenated codes that can be decoded up to half their design distance (i.e.
up to Dd /2).
 214

12.3 Generalized Minimum Distance Decoding

Recall the natural decoding algorithm for concatenated codes from Algorithm 13. In particular,
we performed MLD on the inner code and then fed the resulting vector to a unique decoding
algorithm for the outer code. A drawback of this algorithm is that it does not take into account
the information that MLD provides. For example, it does not distinguish between the situations
where a given inner code’s received word has a Hamming distance of one vs where the received
word has a Hamming distance of (almost) half the inner code distance from the closest code-
word. It seems natural to make use of this information. Next, we study an algorithm called the
Generalized Minimum Distance (or GMD) decoder, which precisely exploits this extra informa-
tion.
In the rest of the section, we will assume Cout to be an [N , K , D]q k code that can be decoded
(by DCout) from e errors and s erasures in polynomial time as long as 2e + s < D. Further, let Cin
be an [n, k, d ]q code with k = O(log N ) which has a unique decoder DCin (which we will assume
is the MLD implementation from Algorithm 2).
We will in fact look at three versions of the GMD decoding algorithm. The ﬁrst two will be
randomized algorithms while the last will be a deterministic algorithm. We will begin with the
ﬁrst randomized version, which will present most of the ideas in the ﬁnal algorithm.

12.3.1 GMD algorithm- I

Before we state the algorithm, let us look at two special cases of the problem to build some
intuition.
Consider the received word y = (y1, . . . , yN ) ∈ [q n]N with the following special property: for
every i such that 1 ≤ i ≤ N , either yi = y ′
i or ∆(yi , y ′
i ) ≥ d /2, where y ′
i = M LDCin(yi ). Now we
claim that if ∆(y,Cout ◦ Cin) < d D/2, then there are < D positions in y such that ∆(yi ,Cin(y ′
i )) ≥
d /2 (we call such a position bad). This is because, for every bad position i , by the deﬁnition of
y ′
i , ∆(yi ,Cin) ≥ d /2. Now if there are ≥ D bad positions, this implies that ∆(y,Cout ◦ Cin) ≥ d D/2,
which is a contradiction. Now note that we can decode y by just declaring an erasure at every
bad position and running the erasure decoding algorithm for Cout on the resulting vector.
Now consider the received word y = (y1, . . . , yN ) with the special property: for every i such
that i ∈ [N ], yi ∈ Cin. In other words, if there is an error at position i ∈ [N ], then a valid codeword
in Cin gets mapped to another valid codeword yi ∈ Cin. Note that this implies that a position
with error has at least d errors. By a counting argument similar to the ones used in the previous
paragraph, we have that there can be < D/2 such error positions. Note that we can now decode
y by essentially running a unique decoder for Cout on y (or more precisely on (x1, . . . , xN ), where
yi = Cin(xi )).
Algorithm 14 generalizes these observations to decode arbitrary received words. In particu-
lar, it smoothly “interpolates" between the two extreme scenarios considered above.
Note that if y satisﬁes one of the two extreme scenarios considered earlier, then Algorithm 14
works exactly the same as discussed above.
By our choice of DCout and DCin, it is easy to see that Algorithm 14 runs in polynomial time
(in the ﬁnal block length). More importantly, we will show that the ﬁnal (deterministic) version

215

Algorithm 14 Generalized Minimum Decoder (ver 1)

INPUT: Received word y = (y1, · · · , yN ) ∈ [q n]N

OUTPUT: Message m′ ∈ [q k ]K

1: FOR 1 ≤ i ≤ N DO

2: y ′
i ← DCin(yi ).

3: wi ← min (
∆(y ′
i , yi ), d
2
 ).

4: With probability 2wi
d , set y ′′
i ←?, otherwise set y ′′
i ← x, where y ′
i = Cin(x).

5: m′ ← DCout(y
′′), where y
′′ = (y ′′
1 , . . . , y ′′
N ).

6: RETURN m′

of Algorithm 14 can do unique decoding of Cout ◦Cin up to half of its design distance.
As a ﬁrst step, we will show that in expectation, Algorithm 14 works.

Lemma 12.3.1. Let y be a received word such that there exists a codeword Cout◦Cin(m) = (c1, . . . , cN ) ∈
[q n]N such that ∆(Cout ◦ Cin(m), y) < Dd
2 . Further, if y
′′ has e′ errors and s′ erasures (when com-
pared with Cout ◦Cin(m)), then E [
2e′ + s′] < D.

Note that if 2e′ + s′ < D, then by Theorem 12.2.2, Algorithm 14 will output m. The lemma
above says that in expectation, this is indeed the case.

Proof of Lemma 12.3.1. For every 1 ≤ i ≤ N , deﬁne ei = ∆(yi , ci ). Note that this implies that

N∑

i =1 ei < Dd
2 . (12.2)

Next for every 1 ≤ i ≤ N , we deﬁne two indicator variables:

X ?
i = 1y ′′
i =?,

and X e
i = 1Cin(y ′′
i )̸=ci and y ′′
i ̸=?.

We claim that we are done if we can show that for every 1 ≤ i ≤ N :

E [
2X e
i + X ?
i ] ≤ 2ei
d . (12.3)

Indeed, by deﬁnition we have: e′ = ∑

i X e
i and s′ = ∑

i X ?
i . Further, by the linearity of expectation

(Proposition 3.1.2), we get
 E [
2e′ + s′] ≤ 2
d
 ∑

i ei < D,

216

where the inequality follows from (12.2).
To complete the proof, we will prove (12.3) by a case analysis. Towards this end, ﬁx an arbi-
trary 1 ≤ i ≤ N .
Case 1: (ci = y ′
i ) First, we note that if y ′′
i ̸=? then since ci = y ′
i , we have X e
i = 0. This along with
the fact that Pr[y ′′
i =?] = 2wi
d implies

E [X ?
i ] = Pr[X ?
i = 1] = 2wi
d ,

and E [X e
i ] = Pr[X e
i = 1] = 0.

Further, by deﬁnition we have

wi = min (∆(y ′
i , yi ), d
2
 ) ≤ ∆(y ′
i , yi ) = ∆(ci , yi ) = ei .

The three relations above prove (12.3) for this case.
Case 2: (ci ̸= y ′
i ) As in the previous case, we still have

E [X ?
i ] = 2wi
d .

Now in this case, if an erasure is not declared at position i , then X e
i = 1. Thus, we have

E [X e
i ] = Pr[X e
i = 1] = 1 − 2wi
d .

Next, we claim that as ci ̸= y ′
i , ei + wi ≥ d , (12.4)

which implies
 E [
2X e
i + X ?
i ] = 2 − 2wi
d ≤ 2ei
d ,

as desired.
To complete the proof, we show (12.4) via yet another case analysis.
Case 2.1: (wi = ∆(y ′
i , yi ) < d /2) By deﬁnition of ei , we have

ei + wi = ∆(yi , ci ) + ∆(y ′
i , yi ) ≥ ∆(ci , y ′
i ) ≥ d ,

where the ﬁrst inequality follows from the triangle inequality and the second inequality follows
from the fact that Cin has distance d .
Case 2.2: (wi = d
2 ≤ ∆(y ′
i , yi )) As y ′
i is obtained from MLD, we have

∆(y ′
i , yi ) ≤ ∆(ci , yi ).

This along with the assumption on ∆(y ′
i , yi ), we get

ei = ∆(ci , yi ) ≥ ∆(y ′
i , yi ) ≥ d
2 .

This in turn implies that ei + wi ≥ d ,

as desired. ✷

217

12.3.2 GMD Algorithm- II

Note that Step 4 in Algorithm 14 uses “fresh" randomness for each i . Next we look at another
randomized version of the GMD algorithm that uses the same randomness for every i . In par-
ticular, consider Algorithm 15.

Algorithm 15 Generalized Minimum Decoder (ver 2)

INPUT: Received word y = (y1, · · · , yN ) ∈ [q n]N

OUTPUT: Message m′ ∈ [q k ]K

1: Pick θ ∈ [0, 1] uniformly at random.

2: FOR 1 ≤ i ≤ N DO

3: y ′
i ← DCin(yi ).

4: wi ← min (
∆(y ′
i , yi ), d
2
 ).

5: If θ < 2wi
d , set y ′′
i ←?, otherwise set y ′′
i ← x, where y ′
i = Cin(x).

6: m′ ← DCout(y
′′), where y
′′ = (y ′′
1 , . . . , y ′′
N ).

7: RETURN m′

We note that in the proof of Lemma 12.3.1, we only use the randomness to show that

Pr [y ′′
i =?
] = 2wi
d .

In Algorithm 15, we note that
Pr [y ′′
i =?
] = Pr [
θ ∈ [
0, 2wi
d
 )] = 2wi
d ,

as before (the last equality follows from our choice of θ). One can verify that the proof of
Lemma 12.3.1 can be used to show the following lemma:

Lemma 12.3.2. Let y be a received word such that there exists a codeword Cout◦Cin(m) = (c1, . . . , cN ) ∈
[q n]N such that ∆(Cout ◦ Cin(m), y) < Dd
2 . Further, if y
′′ has e′ errors and s′ erasures (when com-
pared with Cout ◦Cin(m)), then Eθ [
2e′ + s′] < D.

Next, we will see that Algorithm 15 can be easily “derandomized."

12.3.3 Derandomized GMD algorithm

Lemma 12.3.2 along with the probabilistic method shows that there exists a value θ∗ ∈ [0, 1] such
that Algorithm 15 works correctly even if we ﬁx θ to be θ∗ in Step 1. Obviously we can obtain
such a θ∗ by doing an exhaustive search for θ. Unfortunately, there are uncountable choices of
θ because θ ∈ [0, 1]. However, this problem can be taken care of by the following discretization
trick.
 218

Deﬁne Q = {0, 1} ∪ { 2w1
d , · · · , 2wN
d }. Then because for each i , wi = min(∆(y ′
i , yi ), d /2), we have

Q = {0, 1} ∪ {q1, · · · , qm}

where q1 < q2 < · · · < qm for some m ≤ ⌊ d
2
 ⌋
. Notice that for every θ ∈ [qi , qi +1), just before Step

6, Algorithm 15 computes the same y
′′. (See Figure 12.2 for an illustration as to why this is the
case.)
 Everything here is not an erasure θ

0 q1 q2 qi −1 1qi qi +1
 Everything gets ?

Figure 12.2: All values of θ ∈ [qi , qi +1) lead to the same outcome

Thus, we need to cycle through all possible values of θ ∈ Q, leading to Algorithm 16.

Algorithm 16 Deterministic Generalized Minimum Decoder‘

INPUT: Received word y = (y1, · · · , yN ) ∈ [q n]N

OUTPUT: Message m′ ∈ [q k ]K

1: Q ← { 2w1
d , · · · , 2wN
d } ∪ {0, 1}.

2: FOR θ ∈ Q DO

3: FOR 1 ≤ i ≤ N DO

4: y ′
i ← DCin(yi ).

5: wi ← min (∆(y ′
i , yi ), d
2
 )
.

6: If θ < 2wi
d , set y ′′
i ←?, otherwise set y ′′
i ← x, where y ′
i = Cin(x).

7: m′
θ ← DCout(y
′′), where y
′′ = (y ′′
1 , . . . , y ′′
N ).

8: RETURN m′
θ∗ for θ∗ = arg minθ∈Q ∆ (
Cout ◦Cin (m′
θ) , y
)

Note that Algorithm 16 is Algorithm 15 repeated |Q| times. Since |Q| is O(n), this implies
that Algorithm 16 runs in polynomial time. This along with Theorem 10.2.1 implies that

Theorem 12.3.3. For every constant rate, there exists an explicit linear binary code on the Zyablov
bound. Further, the code can be decoded up to half of the Zyablov bound in polynomial time.

Note that the above answers Question 10.3.1 in the afﬁrmative.

12.4 Bibliographic Notes

Forney in 1966 designed the Generalized Minimum Distance (or GMD) decoding [31].

219220

Chapter 13

Efﬁciently Achieving the Capacity of the
BSCp

Table 13.1 summarizes the main results we have seen so far for (binary codes).

Shannon Hamming
Unique Decoding List Decoding
Capacity 1 − H (p) (Thm 6.3.1) ≥ GV (Thm 4.2.1) 1 − H (p) (Thm 7.4.1)
≤ MRRW (Sec 8.2)
Explicit Codes ? Zyablov bound (Thm 10.2.1) ?
Efﬁcient Algorithms ? 1
2 · Zyablov bound (Thm 12.3.3) ?

Table 13.1: An overview of the results seen so far

In this chapter, we will tackle the open questions in the ﬁrst column of Table 13.1. Recall that
there exist linear codes of rate 1− H (p)−ε such that decoding error probability is not more than
2−δn, δ = Θ(ε2) on the B SCp (Theorem 6.3.1 and Exercise 6.3). This led to Question 6.3.1, which
asks if we can achieve the BSCp capacity with explicit codes and efﬁcient decoding algorithms?

13.1 Achieving capacity of B SC p

We will answer Question 6.3.1 in the afﬁrmative by using concatenated codes. The main intu-
ition in using concatenated codes is the following. As in the case of construction of codes on
the Zyablov bound, we will pick the inner code to have the property that we are after: i.e. a
code that achieves the BSCp capacity. (We will again exploit the fact that since the block length
of the inner code is small, we can construct such a code in a brute-force manner.) However,
unlike the case of the Zyablov bound construction, we do not know of an explicit code that is
optimal over say the qSCp channel. The main observation here is that the fact that the BSCp
noise is memory-less can be exploited to pick the outer code that can correct from some small
but constant fraction of worst-case errors.
 221

Before delving into the details, we present the main ideas. We will use an outer code Cout that
has rate close to 1 and can correct from some ﬁxed constant (say γ) fraction of worst-case errors.
We pick an inner code Cin that achieves the BSCp capacity with parameters as guaranteed by
Theorem 6.3.1. Since the outer code has rate almost 1, the concatenated code can be made
to have the required rate (since the ﬁnal rate is the product of the rates of Cout and Cin). For
decoding, we use the natural decoding algorithm for concatenated codes from Algorithm 13.
Assume that each of the inner decoders has a decoding error probability of (about) γ. Then the
intermediate received word y
′ has an expected γ fraction of errors (with respect to the outer
codeword of the transmitted message), though we might not have control over where the errors
occur. However, we picked Cout so that it can correct up to γ fraction of worst-case errors. This
shows that everything works in expectation. To make everything work with high probability (i.e.
achieve exponentially small overall decoding error probability), we make use of the fact that
since the noise in BSCp is independent, the decoding error probabilities of each of the inner
decodings is independent and thus, by the Chernoff bound (Theorem 3.1.6), with all but an
exponentially small probability y
′ has Θ(γ) fraction of errors, which we correct with the worst-
case error decoder for Cout. See Figure 13.1 for an illustration of the main ideas. Next, we present
the details.
 Can correct ≤ γ worst-case errors

m1 m2 mK

Dout

Din Din Din

y ′
1

y1
 y ′
2

y2
 y ′
N

yN

y
′

y
 Independent decoding error probability of ≤ γ
2

Figure 13.1: Efﬁciently achieving capacity of BSCp .

We answer Question 6.3.1 in the afﬁrmative by using a concatenated code Cout ◦Cin with the
following properties (where γ > 0 is a parameter that depends only on ε and will be ﬁxed later
on):

(i) Cout: The outer code is a linear [N , K ]2k code with rate R ≥ 1 − ε
2 , where k = O(log N ).
Further, the outer code has a unique decoding algorithm Dout that can correct at most γ
fraction of worst-case errors in time Tout(N ).

(ii) Cin: The inner code is a linear binary [n, k]2 code with a rate of r ≥ 1− H (p)−ε/2. Further,
there is a decoding algorithm Din (which returns the transmitted codeword) that runs in
time Tin(k) and has decoding error probability no more than γ
2 over B SCp .

222

Table 13.2 summarizes the different parameters of Cout and Cin.

Dimension Block q Rate Decoder Decoding Decoding
length time guarantee
Cout K N 2k 1 − ε
2 Dout Tout(N ) ≤ γ fraction of
worst-case errors
Cin k ≤ O(log N ) n 2 1 − H (p) − ε
2 Din Tin(k) ≤ γ
2 decoding error
probability over BSCp

Table 13.2: Summary of properties of Cout and Cin

Suppose C ∗ = Cout ◦Cin. Then, it is easy to check that

R(C ∗) = R · r ≥ (1 − ε
2
 ) · (1 − H (p) − ε
2
 ) ≥ 1 − H (p) − ε,

as desired.
For the rest of the chapter, we will assume that p is an absolute constant. Note that this
implies that k = Θ(n) and thus, we will use k and n interchangeably in our asymptotic bounds.
Finally, we will use N = nN to denote the block length of C ∗.
The decoding algorithm for C ∗ that we will use is Algorithm 13, which for concreteness we
reproduce as Algorithm 17.

Algorithm 17 Decoder for efﬁciently achieving BSCp capacity

INPUT: Received word y = (y1, · · · , yN ) ∈ [q n]N

OUTPUT: Message m′ ∈ [q k ]K

1: y
′ ← (y ′
1, · · · , y ′
N ) ∈ [q k ]N where
 Cin (y ′
i ) = Din (yi ) 1 ≤ i ≤ N .

2: m′ ← Dout (
y
′)

3: RETURN m′

Note that encoding C ∗ takes time

O(N 2k 2) + O(N kn) ≤ O(N 2n2) = O(N 2),

as both the outer and inner codes are linear
1. Further, the decoding by Algorithm 17 takes time

N · Tin(k) + Tout(N ) ≤ poly(N ),

1Note that encoding the outer code takes O(N 2) operations over Fq k . The term O(N 2k2) then follows from the

fact that each operation over Fq k can be implemented with O(k2) operations over Fq .

223

where the inequality is true as long as

Tout(N ) = N O(1) and Tin(k) = 2
O(k). (13.1)

Next, we will show that decoding via Algorithm 17 leads to an exponentially small decoding
error probability over B SCp . Further, we will use constructions that we have already seen in this
book to instantiate Cout and Cin with the required properties.

13.2 Decoding Error Probability

We begin by analyzing Algorithm 17.
By the properties of Din, for any ﬁxed i , there is an error at y ′
i with probability ≤ γ
2 . Each
such error is independent, since errors in B SCp itself are independent by deﬁnition. Because of

this, and by linearity of expectation, the expected number of errors in y
′ is ≤ γN
2 .
Taken together, those two facts allow us to conclude that, by the (multiplicative) Chernoff
bound (Theorem 3.1.6), the probability that the total number of errors will be more than γN

is at most e− γN
6 . Since the decoder Dout fails only when there are more than γN errors, this is
also the ﬁnal decoding error probability. Expressed in asymptotic terms, the error probability is

2−Ω( γN
n ).

13.3 The Inner Code

We ﬁnd Cin with the required properties by an exhaustive search among linear codes of di-
mension k with block length n that achieve the BSCp capacity by Shannon’s theorem (Theo-
rem 6.3.1). Recall that for such codes with rate 1 − H (p) − ε
2 , the MLD has a decoding error

probability of 2−Θ(ε2n) (Exercise 6.3). Thus, if k is at least Ω ( log( 1
γ )

ε2
 )
, Exercise 6.3 implies the exis-

tence of a linear code with decoding error probability at most γ
2 (which is what we need). Thus,
with the restriction on k from the outer code, we have the following restriction on k:

Ω
 ( log( 1
γ )

ε2
 )
 ≤ k ≤ O (log N ) .

Note, however, that since the proof of Theorem 6.3.1 uses MLD on the inner code and Al-
gorithm 2 is the only known implementation of MLD, we have Tin = 2
O(k) (which is what we
needed in (13.1). The construction time is even worse. There are 2
O(kn) generator matrices; for
each of these, we must check the error rate for each of 2k possible transmitted codewords, and
for each codeword, computing the decoding error probability requires time 2
O(n).2 Thus, the
construction time for Cin is 2
O(n2).

2To see why the latter claim is true, note that there are 2n possible received words and given any one of these
received words, one can determine (i) if the MLD produces a decoding error in time 2
O(k) and (ii) the probability
that the received word can be realized, given the transmitted codeword in polynomial time.

224

c1 c3 · · · cN −1

c2 c4 cN
⇓

c1 c2 c3 c4 · · · cN −1 cN

Figure 13.2: Error Correction cannot decrease during “folding." The example has k = 2 and a
pink cell implies an error.

13.4 The Outer Code

We need an outer code with the required properties. There are several ways to do this.
One option is to set Cout to be a Reed-Solomon code over F2k with k = Θ(log N ) and rate 1− ε
2 .
Then the decoding algorithm Dout, could be the error decoding algorithm from Theorem 12.2.2.
Note that for this Dout we can set γ = ε
4 and the decoding time is Tout(N ) = O(N 3).
Till now everything looks on track. However, the problem is the construction time for Cin,
which as we saw earlier is 2
O(n2). Our choice of n implies that the construction time is 2
O(log
2 N ) ≤
N O(log N ), which of course is not polynomial time. Thus, the trick is to ﬁnd a Cout deﬁned over a

smaller alphabet (certainly no larger than 2
O(plog N )). This is what we do next.

13.4.1 Using a binary code as the outer code

The main observation is that we can also use an outer code which is some explicit binary linear
code (call it C ′) that lies on the Zyablov bound and can be corrected from errors up to half its
design distance. We have seen that such a code can be constructed in polynomial time (Theo-
rem 12.3.3).
Note that even though C ′ is a binary code, we can think of C ′ as a code over F2k in the obvious
way: every k consecutive bits are considered to be an element in F2k (say via a linear map). Note
that the rate of the code does not change. Further, any decoder for C ′ that corrects bit errors
can be used to correct errors over F2k . In particular, if the algorithm can correct β fraction of
bit errors, then it can correct that same fraction of errors over F2k . To see this, think of the
received word as y ∈ (F2k )N ′/k , where N ′ is the block length of C ′ (as a binary code), which is at
a fractional Hamming distance at most ρ away from c ∈ (F2k )N ′/k . Here c is what once gets by
“folding" consecutive k bits into one symbol in some codeword c′ ∈ C ′. Now consider y
′ ∈ FN ′
2 ,
which is just “unfolded" version of y. Now note that each symbol in y that is in error (w.r.t. c)
leads to at most k bit errors in y
′ (w.r.t. c′). Thus, in the unfolded version, the total number of
errors is at most
 k · ρ · N ′

k = ρ · N ′.

(See Figure 13.2 for an illustration for k = 2.) Thus to decode y, one can just “unfold" y to y
′ and
use the decoding algorithm for C ′ (which can handle ρ fraction of errors) on y
′.

225

We will pick Cout to be C ′ when considered over F2k , where we choose

k = Θ
 ( log( 1
γ )

ε2
 )
 .

Further, Dout is the GMD decoding algorithm (Algorithm 16) for C ′.
Now, to complete the speciﬁcation of C ∗, we relate γ to ε. The Zyablov bound gives δout =
(1 − R)H −1(1 − r ), where R and r are the rates of the outer and inners codes for C ′. Now we can
set 1 − R = 2p
γ (which implies that R = 1 − 2p
γ) and H −1(1 − r ) = p
γ, which implies that r is3

1 −O (p
γ log 1
γ
 ). Since we picked Dout to be the GMD decoding algorithm, it can correct δout
2 = γ
fraction of errors in polynomial time, as desired.

The overall rate of Cout is simply R · r = (
1 − 2pγ
) · (1 − O (p
γ log 1
γ
 ))
. This simpliﬁes to 1 −

O (pγ log ( 1
γ
 ))
. Recall that we need this to be at least 1 − ε
2 . Thus, we would be done here if we

could show that ε is Ω (pγ log 1
γ
 )
, which would follow by setting

γ = ε3.

13.4.2 Wrapping Up

We now recall the construction, encoding and decoding time complexity for our construction

of C ∗. The construction time for Cin is 2
O(n2), which substituting for n, is 2
O( 1
ε4 log
2( 1
ε )). The
construction time for Cout, meanwhile, is only poly(N ). Thus, our overall, construction time is

poly(N ) + 2
O( 1
ε4 log
2( 1
ε )).
As we have seen in Section 13.1, the encoding time for this code is O(N 2), and the decoding

time is N O(1) + N ·2
O(n) = poly(N )+N ·2
O( 1
ε2 log
( 1
ε )). We also have shown that the decoding error

probability is exponentially small: 2−Ω( γN
n ) = 2−Ω(ε6N ). Thus, we have proved the following
result:

Theorem 13.4.1. For every constant p and 0 < ε < 1 − H (p), there exists a linear code C ∗ of block
length N and rate at least 1 − H (p) − ε, such that

(a) C ∗ can be constructed in time poly(N ) + 2
O(ε−5);

(b) C ∗ can be encoded in time O(N 2); and

(c) There exists a poly(N ) + N · 2
O(ε−5) time decoding algorithm that has an error probability
of at most 2−Ω(ε6N ) over the B SCp .

3Note that r = 1 − H (
pγ) = 1 + p
γ log p
γ + (1 − p
γ) log(1 − p
γ). Noting that log(1 − p
γ) = −
p
γ − Θ(γ), we can
deduce that r = 1 − O(
pγ log(1/γ)).
 226

Thus, we have answered in the afﬁrmative Question 6.3.1, which was the central open ques-
tion from Shannon’s work. However, there is a still somewhat unsatisfactory aspect of the result
above. In particular, the exponential dependence on 1/ε in the decoding time complexity is not
nice. This leads to the following question:

Question 13.4.1. Can we bring the high dependence on ε down to poly ( 1
ε ) in the decoding
time complexity?

13.5 Discussion and Bibliographic Notes

Forney answered Question 6.3.1 in the afﬁrmative by using concatenated codes. (As was men-
tioned earlier, this was Forney’s motivation for inventing code concatenation: the implication
for the rate vs. distance question was studied by Zyablov later on.)
We now discuss Question 13.4.1. For the binary erasure channel, the decoding time com-
plexity can be brought down to N ·poly( 1
ε ) using LDPC codes, speciﬁcally a class known as Tor-
nado codes developed by Luby et al. [71]. The question for binary symmetric channels, however,
is still open. Recently there have been some exciting progress on this front by the construction
of the so-called Polar codes.
We conclude by noting an improvement to Theorem 13.4.1. We begin with a theorem due to
Spielman:

Theorem 13.5.1 ([94]). For every small enough β > 0, there exists an explicit Cout of rate 1
1+β and

block length N , which can correct Ω ( β
2

(log 1
β )2
 ) errors, and has O(N ) encoding and decoding.

Clearly, in terms of time complexity, this is superior to the previous option in Section 13.4.1.
Such codes are called “Expander codes.” One can essentially do the same calculations as in

Section 13.4.1 with γ = Θ ( ε2

log
2(1/ε)
 )
.4 However, we obtain an encoding and decoding time of

N ·2poly( 1
ε ). Thus, even though we obtain an improvement in the time complexities as compared
to Theorem 13.4.1, this does not answer Question 13.4.1.

4This is because we need 1/(1 + β) = 1 − ε/2, which implies that β = Θ(ε).

227228

Chapter 14

Decoding Reed-Muller Codes

In this chapter we describe decoding algorithms for the Reed-Muller codes, introduced in Chap-
ter 9. Recall that these are the codes obtained by evaluations of multivariate polynomials over
all possible assignments to the variables. We will see several decoding algorithms for these
codes, ranging from simplistic ones that correct a constant fraction of the minimum distance
(with the constant depending on q), to algorithms based on more sophisticated concepts that
correct up to half the minimum distance.
To elaborate on the above, recall that the Reed-Muller code with parameters q, m, r is the
set of functions RM(q, m, r ) def
= { f : Fm
q → Fq | deg( f ) ≤ r } .

The minimum distance distance of the code is

∆q,m,r def
= (q − t ) · q m−s−1,

where s, t satisfy r = s(q − 1) + t and 0 ≤ t ≤ q − 2 (recall Lemma 9.4.1). We will ﬁrst describe an
algorithm to correct ε · ∆q,m,r for some constant ε > 0 that depends only on q. Later we will give

algorithms that correct ⌊ ∆q,m,r −1
2
 ⌋ errors.

14.1 A natural decoding algorithm

The main insight behind our ﬁrst decoding algorithm is the simple fact that the degree of poly-
nomials does not increase on afﬁne substitutions. Let us introduce this notion and then explain
why this might be useful in building decoding algorithms.

Deﬁnition 14.1.1. A one-dimensional s-variate afﬁne form a ∈ Fq [Z1, . . . , Zs] is a polynomial of
the form a(Z1, . . . , Zs) = ∑s
i =1 αi Zi + α0. In other words an afﬁne form is a polynomial of degree
at most 1. An m-dimensional s-variate afﬁne form A = 〈a1, . . . , am〉 is simply an m-tuple of one-
dimensional afﬁne forms.

For example A0 = 〈Z1 + Z2, Z1, Z2〉 is a 3-dimensional 2-variate afﬁne form over F2.

229

Deﬁnition 14.1.2. Given an m-variate polynomial P ∈ Fq [X1, . . . , Xm] and an m-dimensional s-
variate afﬁne form A = 〈a1, . . . , am〉 ∈ (Fq [Z ])m where Z = (Z1, . . . , Zs), the afﬁne substitution of
A into P is given by the polynomial P ◦ A ∈ Fq [Z ] given by (P ◦ A)(Z ) = P (a1(Z ), . . . , am(Z )).

Let A0 be the afﬁne form as above and let P0(X1, X2, X3) = X1X2 + X1X2X3 + X3 over F2. Then
we have

(P0◦ A0)(Z1, Z2) = (Z1+Z2)Z1+(Z1+Z2)Z1Z2+Z2 = Z 2
1 +Z1Z2+Z 2
1 Z2+Z1Z 2
2 +Z2 = Z1+Z1Z2+Z2,

where the last equality follows since we are working over F2.
Notice that the notion of afﬁne substitutions extends to functions naturally, viewing both
f and A as functions (given by the evaluations of corresponding polynomials) in the deﬁnition
above.
Afﬁne substitutions have nice algebraic, geometric, and probabilistic properties and these
combine to give us the decoding algorithm of this section. We introduce these properties in
order.

Proposition 14.1.1 (Degree of Afﬁne Substitutions). Afﬁne substitutions do not increase the de-
gree of a polynomial. Speciﬁcally, if A is an afﬁne form, then for every polynomial P , we have
deg(P ◦ A) ≤ deg(P ).

Proof. The proof is straightforward. First note that for any single monomial M = ∏m
i =1 X ri
i the
afﬁne substitution M ◦ A = ∏m
i =1 ai (Z )ri has degree at most deg(M ). Next note that if we write a
general polynomial as a sum of monomials, say P = ∑M cM · M , then the afﬁne substitution is
additive and so P ◦ A = ∑M cM (M ◦ A). The proposition now follows from the fact that

deg(P ◦ A) = deg(∑

M cM (M ◦ A)) ≤ max
M {deg(M ◦ A)} ≤ max
M deg(M )} = deg(P ).

We remark that the bound above can be tight (see Exercise 14.1) and that the result above
generalizes to the case when we replace each term by a degree d -polynomial instead of a degree
1-polynomial (see Exercise 14.2).
Next we turn to the geometric aspects of afﬁne substitutions. These aspects will be essential
for some intuition, though we will rarely invoke them formally.
One way to view afﬁne substitutions into functions is that we are viewing the restriction of a
function on a small subset of the domain. For example, when s = 1, then an afﬁne substitution
A into a function f , restricts the domain of the function to the set {A(z)|z ∈ Fq } where A(z) is of
the form az + b for some a, b ∈ Fm
q . This set forms a line in Fm
q with slope a and passing through
the point b. When s becomes larger, we look at higher dimensional (afﬁne) subspaces such as
planes (s = 2) and cubes (s = 3). While lines, planes and cubes are not exactly the same as in the
Euclidean space they satisfy many similar properties and this will be used to drive some of the
probabilistic thinking below.
In what follows we will be looking restrictions of two functions f and g on small-dimensional
afﬁne subspaces. On these subspaces we would like to argue that f and g disagree roughly as

230

often as they do on Fm
q . To do so, we use the fact that “random” afﬁne substitutions sample
uniformly from Fm
q . We formalize this below.
Consider a uniform choice of an afﬁne form A(z) = Mz + b, i.e., where M ∈ Fm×s
q and b ∈ Fm
q
are chosen uniformly and independently from their respective domains. (Note that this allows
M to be of less than full rank with positive probability, and we will allow this to keep calculations
simple and clean. We do warn the reader that this can lead to degenerate lines and subspaces -
e.g., when M is the zero matrix then these subspaces contain only one point.)

Proposition 14.1.2. (1) Fix z ∈ Fs
q . Then, for a uniformly random A, the point A(z) is dis-
tributed uniformly in Fm
q .

(2) Fix z ∈ Fs
q \ {0} and x ∈ Fm
q . and let A be chosen uniformly subject to the condition A(0) = x.
Then the point A(z) is distributed uniformly in Fm
q . Consequently, for every pair of functions
f , g : Fm
q → Fq , we have Pr
A
 [ f ◦ A(z) ̸= g ◦ A(z)
] = δ( f , g ).

Proof. Let A(z) = Mz + b where M ∈ Fm×s
q and b ∈ Fm
q are chosen uniformly and independently.
For part (1), we use the fact that for every ﬁxed M and z, Mz + b is uniform over Fm
q when b is
uniform. In particular, for every y ∈ Fm
q we have

Pr
b
 [
Mz + b = y] = Pr
b
 [
b = y − Mz] = q −m.

Since this holds for every M, it follows that

Pr
M,b
 [Mz + b = y
] = q −m

and so we conclude that A(z) = Mz + y is uniformly distributed over F
m
q .
For part (2), note that the condition A(0) = x implies b = x. So, for ﬁxed y ∈ Fm
q , we have

Pr
M,b
 [A(z) = y | A(0) = x
] = Pr
M
 [
Mz + x = y
] .

Now let z = (z1, . . . , zs) and denote the columns of M by M1, . . . , Ms so that

Mz = z1M1 + · · · + zs Ms.

Since z ̸= 0 we must have some zi ̸= 0 and let i be the largest such index. We note that for every
choice of M1, . . . , Mi −1, Mi +1, . . . , Ms, the probability, over the choice of Mi that Mz+x = y is q −m,
since this happens if and only if Mi = z−1
i (y − (z1M1 + · · · zi −1Mi −1 + x), and this event happens
with probability q −m. Averaging over the choices of the remaining columns of M, we still have

Pr
M,b
 [A(z) = y | A(0) = x
] = Pr
M
 [
Mz + x = y
] = q −m,

thus establishing that A(z) is distributed uniformly over Fm
q even when conditioned on A(0) = x.

231

Finally to see the ﬁnal implication of part (2), ﬁx functions f , g : Fm
q and let

E = {
y ∈ Fm
q | f (y) ̸= g (y)
} ,

so that δ( f , g ) = Pry [
y ∈ E ]
. We have

Pr
A
 [ f ◦ A(z) ̸= g ◦ A(z)
] = Pr
A [A(z) ∈ E ] ,

but since A(z) is uniform in Fm
q even given A(0) = x, we have

Pr
A [A(z) ∈ E ] = Pr
y [
y ∈ E ] = δ( f , g ),

as claimed.

14.1.1 The Actual Algorithm

Now we explain why afﬁne substitutions might help in decoding the Reed-Muller code. Recall
that the decoding problem for the Reed-Muller codes is the following:

• Input: Parameters q, m, r and e (bound on number of errors) and a function f : Fm
q →
Fq .

• Output: Polynomial P ∈ Fq [X1, . . . , Xm] with deg(P ) ≤ r such that |{x ∈ Fm
q | f (x) ̸=
P (x)}| ≤ e.

One way to recover the desired polynomial P is to output its value at every given point x ∈
Fm
q . (This works provided the polynomial P to be output is uniquely determined by f and the
number of errors, and that is the setting we will be working with.) In what follows we will do
exactly this. The main idea behind the algorithm of this section is the following: We will pick an
afﬁne form A such that A(0) = x and attempt to recover the polynomial P ◦ A. Evaluating P ◦ A(0)
gives us P (x) and so this sufﬁces, but why is the task of computing P ◦ A any easier? Suppose
we use an s-variate form A for small s. Then the function P ◦ A is given by q s values with s < m
this can be a much smaller sized function and so brute force methods would work faster. But
an even more useful observation is that if A is chosen at random such that A(0) = x, then most
of the q s points (in fact all but one) are random points and so unlikely to be erroneous. In
particular for any ﬁxed non-zero z, we would have with high probability f ◦ A(z) = P ◦ A(z),
where the probability is over the choice of A, assuming the number of errors is small. Since
q s < q m one can apply a union bound over the roughly q s choices of z to (hopefully) establish
that all the points z ∈ Fs
q \ {0} are not errors, and if this happens a further hope would be that
P ◦ A is uniquely determined by its values on Fs
q \ {0}. The two hopes are in tension with each
other — the former needs small values of s and the latter needs s to be large; and so we pick

an intermediate s, speciﬁcally s = ⌈ r +1
q−1
 ⌉
, where both conditions are realized and this yields the
algorithm below. We describe the algorithm ﬁrst and then explain this choice of parameters
later.
 232

Algorithm 18 SIMPLE REED-MULLER DECODER

INPUT: r < m, 0 < e ≤ 1
3 · q m−⌈(r +1)/(q−1)⌉, and function f : Fm
q → Fq .
OUTPUT: Polynomial P ∈ Fq [X1, . . . , Xm] with deg(P ) ≤ r such that |{x ∈ Fm
q | f (x) ̸= P (x)}| ≤ e, if
such a polynomial exists and NULL otherwise

FOR x ∈ Fm
q DO
g (x) =LOCAL-DECODE-RM-SIMPLE(x, f ).

RETURN INTERPOLATE (q, m, g , r, Fm
q )

procedure LOCAL-DECODE-RM-SIMPLE(x, f )
Repeat LOCAL-DECODE-RM-SIMPLE-ITER(x, f ) O(m log q) times and return most fre-
quent answer.

procedure LOCAL-DECODE-RM-SIMPLE-ITER(x, f )

Let s ← ⌈ r +1
q−1
 ⌉

Select an m-dimensional s-variate afﬁne form A uniformly conditioned on A(0) = x.

g ← INTERPOLATE (q, s, f ◦ A, r, F s
q \ {0})

IF g is NULL THEN
g ← 0

RETURN g (0).

procedure INTERPOLATE(q, m, f , r, S) ⊲ Returns a polynomial P ∈ Fq (Z1, . . . , Zs) such that
deg(P ) ≤ r and P (x) = f (x) for every x ∈ S and return NULL is no such P exists. ⊲ See
comments in Section 14.1.2 for more on how this algorithm can be implemented.

233

The detailed algorithm is given as Algorithm 18. Roughly the algorithm contains two loops.
The outer loop enumerates x ∈ Fn
q and invokes a subroutine LOCAL-DECODE-RM-SIMPLE that
determines P (x) correctly with very high probability. This subroutine creates an inner loop
which invokes a less accurate subroutine LOCAL-DECODE-RM-SIMPLE-ITER, which computes
P (x) correctly with probability 2
3 , many times and reports the most commonly occurring an-
swer. The crux of the algorithm is thus LOCAL-DECODE-RM-SIMPLE-ITER. This algorithm
picks a random afﬁne form A such that A(0) = x and assumes that f ◦ A(z) = P ◦ A(z) for ev-
ery non-zero z. Based on this assumption it interpolates the polynomial P ◦ A and returns
P ◦ A(0) = P (A(0)) = P (x).
The crux of the analysis is to show that the assumption holds with probability at least 2
3 over
the random choice of A provided the number of errors is small. We will undertake this analysis
next.

14.1.2 Analysis of the simple decoding algorithm

We ﬁrst show that each invocation of LOCAL-DECODE-RM-SIMPLE-ITER succeeds with high
probability:

Lemma 14.1.3. Let P ∈ Fq [X1, . . . , Xm] be a polynomial of degree at most r and let f : Fm
q → Fq be
such that
 e = |{x ∈ Fm
q | f (x) ̸= P (x)}| ≤ 1
3 · q m−⌈(r +1)/(q−1)⌉.

Then, for every x ∈ Fm
q , the probability that LOCAL-DECODE-RM-SIMPLE-ITER( f , x) returns P (x)
is at least 2/3.

Proof. Recall s = ⌈ r +1
q−1
 ⌉ and so e ≤ q m−s

3 . We use this condition in the analysis below.
Fix z ∈ Fs
q \ {0}. Since A was picked conditioned on A(0) = x, by part (2) of Proposition 14.1.2
we have that A(z) is a uniformly random element of Fm
q (and in particular this is independent
of x). So the probability that f (A(z)) ̸= P (A(z)) is exactly e
q m . Taking the union bound over all
z ∈ Fs
q \ {0} we get that

Pr
A
 [
∃z ∈ Fs
q \ {0} s.t. f (A(z)) ̸= P (A(z))
] ≤ (q s − 1) · e
q m ≤ e
q m−s ≤ 1
3 . (14.1)

So, with probability at least 2
3 , we have that f ◦A(z) = P ◦A(z) for every z ∈ Fs
q \{0}. We argue below
that if this holds, then LOCAL-DECODE-RM-SIMPLE-ITER( f , x) returns P (x) and this proves the
lemma.
Since P ◦ A is a polynomial in Fq [Z1, . . . , Zs] of degree at most r that agrees with f ◦ A on ev-
ery z ∈ Fs
q \ {0}, we have that the there exists at least one polynomial satisfying the condition of
the ﬁnal interpolation step in LOCAL-DECODE-RM-SIMPLE-ITER( f , x). It sufﬁces to show that
this polynomial is unique, but this follows from Exercise 14.4, which asserts that δ(P ◦ A, h) ≥ 2
q s
for every polynomial h ∈ Fq [Z1, . . . , Zs] of degree at most r , provided r < (q − 1)s. (Note that

our choice of s = ⌈ r +1
q−1
 ⌉ ensures this.) In particular this implies that every pair of polynomi-
als disagree on at least two points in Fs
q and so on at least one point in Fs
q \ {0}. Thus P ◦ A is

234

the unique polynomial that ﬁts the condition of the interpolation step in LOCAL-DECODE-RM-
SIMPLE-ITER( f , x) and so this subroutine returns P (x) with probability at least 2
3 .

We note that one can push the 1
3 fraction of errors to 1
2 − γ for any 0 < γ < 1/2 with a success
probability of 1
2 + γ (see Exercise 14.5).
With Lemma 14.1.3 in hand, some routine analysis sufﬁces to show the correctness of the
Simple Reed-Muller Decoder (Algorithm 18) and we do so in the theorem below.

Theorem 14.1.4. The Simple Reed-Muller Decoder (Algorithm 18) is a correct (randomized) poly-
nomial in n time algorithm decoding the Reed-Muller code RM(q, m, r ) from e ≤ 1
3 ·q m−⌈(r +1)/(q−1)⌉

errors.

Proof. Fix P ∈ Fq [X1, . . . , Xm] be a polynomial of degree at most r and f : Fm
q → Fq such that

e = |{x ∈ Fm
q | f (x) ̸= P (x)}| ≤ 1
3 · q m−⌈(r +1)/(q−1)⌉.

Further ﬁx x ∈ q m. Lemma 14.1.3 asserts that a call to LOCAL-DECODE-RM-SIMPLE-ITER( f , x)
returns P (x) with probability at least 2
3 . By an application of the Chernoff bounds (in par-
ticular, see Exercise 3.3), the majority of the O(m log q) calls to LOCAL-DECODE-RM-SIMPLE-
ITER( f , x) is P (x) except with probability exp(−m log q) and by setting the constant in the O(·)
appropriately, we an ensure this probability is at most q −m

3 . We thus conclude that for every
ﬁxed x ∈ Fm
q the probability that LOCAL-DECODE-RM-SIMPLE( f , x) does not return P (x) is at

most q −m

3 . By the union bound, we could that the probability that there exists x ∈ Fm
q such that
LOCAL-DECODE-RM-SIMPLE( f , x) ̸= P (x) is at most 1
3 . Thus with probability at least 2
3 the algo-
rithm computes P (x) correctly for every x and thus the interpolation returns P with probability
at least 2
3 .
The running time of the algorithm is easy to establish. Let Tint(n) denote the time it takes
to interpolate to ﬁnd the coefﬁcients of a polynomial P given its n evaluations. It is well-known
that Tint is a polynomial with near linear running time. (See Remarks on Interpolation below.)
We have that the LOCAL-DECODE-RM-SIMPLE-ITER takes time at most Tint(q s) per invocation,
and thus LOCAL-DECODE-RM-SIMPLE takes O(m · Tint(q s) · log q) steps per invocation. Since
LOCAL-DECODE-RM-SIMPLE is executed q m times by the overall algorithm, the overall run-
ning time is bounded by Tint(q m) + O(m · q m · Tint(q s) log q). Expressed in terms of n = q m and
emax = q m−s/3 and crudely bounding interpolation cost by a cubic function, this translates into

a running time of O(n3) + O ( n4

e3
max log n)
.

Remarks on Interpolation. As mentioned in the proof above, the running time of the algo-
rithm depends on the running time of the two interpolation steps in the algorithm DECODE-
RM-SIMPLE. To get polynomial time algorithms for either step, it sufﬁces to note that interpo-
lation is just solving a system of linear equations and thus can always be solved in cubic time
by Gaussian elimination (see Exercise 14.6). To make the steps more efﬁcient, one can use the
structure of polynomial interpolation to get some speedups for the ﬁrst interpolation step (see
Section 14.5). For the second, since we are only interested in evaluating P ◦ A(0), interpolation

235

is a bit of overkill. It turns out one can explicitly determine the exact linear form which de-
scribes P ◦ A(0) in terms of {P ◦ A(z)|z ∈ Fs
q \{0}} and this turns out to be extremely simple: In fact
P ◦ A(0) = − ∑
z∈Fs
q \{0} P ◦ A(z) (see Exercise 14.7).

Remark on Fraction of Errors corrected. The number of errors corrected by the Simple Reed-
Muller Decoder, 1
3 · q m−⌈(r +1)/(q−1)⌉, is complex and requires some explanation. It turns out that

this quantity is closely related to the distance of the code. For s = ⌈ r +1
q−1
 ⌉ if we now let t be such
that r = s(q −1)− t (note that this is different from the way we did this splitting in Lemma 9.4.1),
then from Lemma 9.4.1 we have that the distance of the code RM(q, m, r ) is (t + 1)q m−s where
1 ≤ t ≤ q − 1 (see Exercise 14.8). So in particular the distance of the code is between q m−s and
q m−s+1. In contrast, our algorithm corrects q m−s

3 errors, which is at least a 1
3q -fraction of the

distance of the code. Ideally we would like algorithms correcting up to 1
2 as many errors as the
distance, and this algorithm falls short by a “constant” factor, if q is a constant. In the rest of the
chapter we will try to achieve this factor of 1
2 .

14.2 Majority Logic Decoding

The algorithm of the previous section corrects errors up to a constant fraction of the distance
(with the constant depending on q, but not on m or r ) but is not the best one could hope for.
In this section we develop an algorithm that corrects the optimal number of errors over F2. The
main idea is to continue to explore the function over “afﬁne subspaces” but now the substi-
tutions will be much simpler. Speciﬁcally they will be of the form xi = bi for many different
choices of i where bi ∈ F2. This will leave us with a function on the unset variables and while we
won’t be able to determine the function completely on the remaining variables, we will be able
to determine some coefﬁcients and this will allow us to make progress.
The main idea driving this algorithm is the following proposition about degree r polynomi-
als.

Proposition 14.2.1. Let P ∈ F2[X1, . . . , Xm] be of degree r and let C ∈ F2 be the coefﬁcient of the
monomial ∏r
i =1 Xi in P . Then, for every b ∈ Fm−r
2 , it is the case that ∑a∈Fr
2 P (a, b) = C .

Proof. Let Pb(X1, . . . , Xr ) = P (X1, . . . , Xr , b), i.e., Pb is P restricted to the subspace Xi = bi for
r < i ≤ m. Note that the coefﬁcient of the monomial X1 · · · Xr in Pb remains C , since all other
monomial now have degree strictly less than r after the substitutions Xi = bi . (Note that we
used the fact that P has degree at most r to make this assertion.) So we can write Pb = C ·
X1 · · · Xr + g where deg(g ) < r . We wish to show that

∑

a∈Fr
2 Pb(a) = ∑

a∈Fr
2 C ·
 ( r∏

j =1 a j
 )
 + ∑

a∈Fr
2 g (a) = C .

We ﬁrst note that the ﬁrst summation is trivially C since all terms except when a1 = · · · = ar = 1
evaluate to zero and the term corresponding to a1 = · · · = ar = 1 evaluates to C . The proposition

236

now follows from Exercise 14.7 which asserts that for every polynomial g of degree less than r ,
the summation ∑
a∈Fr
2 g (a) = 0.

As such the proposition above only seems useful in the error-free setting — after all, it as-
sumes P is given correctly everywhere. But it extends to the setting of a small number of er-
rors immediately. Note that if a function f disagrees with polynomial P on at most e points
in Fm
2 then there are at most e choices of b ∈ Fm−r
2 for which ∑
a∈Fr
2 f (a, b) does not equal C .
In particular, if e < 2m−r /2 then the majority of choices of b lead to the correct value of C .
(And remarkably, for the class of degree r polynomials, this is exactly one less than half the
distance of the associated code.) Of course, the monomial ∏r
i =1 Xi is not (very) special. The
same reasoning allows us to compute the coefﬁcient of any monomial of degree r . For example
majorityb∈Fm−r
2 {∑
a∈Fr
2 f (a, b)} gives the coefﬁcient of X1 · · · Xr , and majorityb∈Fm−r
2 {∑a∈Fr
2 f (b, a)}
(note the exchange of a and b) gives the coefﬁcient of Xm−r +1 · · · Xm. (See Exercise 14.9.) With
appropriate notation for substituting a and b into the right places, we can calculate any other
monomial of degree r as well. And then downward induction on r allows us to compute coef-
ﬁcients of lower degree monomials. This leads us to the algorithm described next. For the sake
of completeness we also give the full analysis afterwards.

14.2.1 The Majority Logic Decoding Algorithm

We start with some notation that will help us describe the algorithm more precisely.

Deﬁnition 14.2.1. For S ⊆ [m] we let XS denote the monomial ∏i ∈S Xi .

Deﬁnition 14.2.2. For S ⊆ [m] with |S| = t and vectors a ∈ Ft
2 and b ∈ Fm−t
2 , let (S ← a, ¯S ← b)
denote the vector whose coordinates in S are given by a and coordinates in ¯S are given by b.

Deﬁnition 14.2.3. For S ⊆ [m] with |S| = t and vectors a ∈ Ft
2 and b ∈ Fm−t
2 , let f (S ← a, ¯S ← b)
denote the evaluation of f on (S ← a, ¯S ← b). In other words, let S = {i1, . . . , i t } with ik < ik+1 and
let ¯S = { j1, . . . , jm−t } with jk < jk+1. Then f (S ← a, ¯S ← b) = f (c) where c ∈ Fm
2 is the vector such
that cik = ak and c jℓ = bℓ.

The majority logic decoder details are presented in Algorithm 19.

14.2.2 The analysis

We next argue that the algorithm MAJORITY LOGIC DECODER (Algorithm 19) correct up to half
the errors for the RM(2, m, r ) code.

Lemma 14.2.2. On input f : Fm
2 → F2 that disagrees with a polynomial Q ∈ F2[X1, . . . , Xm] of
degree at most r on at most e < 1
2 · 2m−r points, the algorithm MAJORITY LOGIC DECODER( f )
correctly outputs Q.

Proof. Let Q(X ) = ∑S⊆[m] C ′
S XS and let Qt (X ) = ∑
S⊆[m]:|S|≥t C ′
S XS. We argue by downward in-
duction on t (from r + 1 down to 0) that Qt = Pt where Pt ’s are the polynomials computed by

237

Algorithm 19 Majority Logic Decoder

INPUT: r < m, 0 ≤ e < 1
2 2m−r , and function f : Fm
2 → F2.
OUTPUT: Output P such deg(P ) ≤ r and |{x ∈ F
m
2 |P (x) ̸= f (x)}| ≤ e.
Pr +1 ← 0

FOR t = r downto 0 DO
ft ← f − Pt +1
FOR every S ⊆ [m] with |S| = t DO

FOR every b ∈ Fm−t
2 DO
CS,b ← ∑a∈Ft
2 ft (S ← a, ¯S ← b).

CS ← majorityb {
CS,b}

Pt ← Pt +1 + ∑
S⊆[m],|S|=t CS XS

RETURN P0

our algorithm. The base case is obvious since Pr +1 = Qr +1 = 0. Assume now that Pt +1 = Qt +1
and so we have that ft = f − Pt +1 disagrees with Q − Qt +1 on at most e points. (See Exer-
cise 14.10.) We now argue that for every subset S ⊆ [m] with |S| = t , CS = C ′
S. Fix such a set
S. For b ∈ Fm−t
2 , we refer to the partial assignment ¯S ← b as a “subcube” corresponding to the
points {(S ← a, ¯S ← b)|a ∈ Ft
2}. We say that a subcube ¯S ← b is in error if there exists a such that
ft (S ← a, ¯S ← b) ̸= (Q − Qt +1)(S ← a, ¯S ← b). By Proposition 14.2.1, we have that if a subcube is
not in error then CS,b = C ′
S, since C ′
S is the coefﬁcient of XS in the polynomial (Q −Qt +1) (whose
degree is at most t ). Furthermore at most e subcubes can be in error (see Exercise 14.11). Fi-
nally, since the total number of subcubes is 2m−t ≥ 2m−r > 2e we thus have that a majority of
subcubes are not in error and so CS = majorityb{CS,b} = C ′
S.
Thus we have for every S with |S| = t that CS = C ′
S and so Qt = Pt , giving the inductive step.
So we have for every t , Pt = Qt and in particular P0 = Q0 = Q as desired.

The running time of the algorithm is easy to see as being at most n = 2m times the number
of coefﬁcients of a degree r polynomial, which is ∑r
i =0 (m
i ) ≤ n in the binary case. Thus O(n2) is
a crude upper bound on the running time of this algorithm. Note that this algorithm corrects

up to exactly ⌊ d −1
2
 ⌋ errors where d = 2m−r is the minimum distance of RM(2, m, r ). (Since d is

even, this quantity equals d
2 − 1.) We thus have the following theorem.

Theorem 14.2.3. For every 0 ≤ r < m, The Majority Logic Decoder (Algorithm 19), corrects up to
d
2 − 1 errors in the Reed-Muller code, RM(2, m, r ), in O(n2) time, where n = 2m is the block length
of the code and d = 2m−r is its minimum distance.

14.3 Decoding by reduction to Reed-Solomon decoding

The algorithms described so far were based on very basic ideas, but they have their limitations.
The SIMPLE REED-MULLER DECODER (Algorithm 18) fails to correct errors up to half the min-

238

imum distance. And the majority logic algorithm (Algorithm 19) seems to work only over F2
(where the monomial structure is especially simple). The ﬁnal algorithm we give uses a slightly
more sophisticated algebraic idea, but then ends up yielding an almost ‘trivial’ reduction to
Reed-Solomon decoding. (It is trivial in the sense that the reduction algorithm almost does no
work.) The resulting reduction can use any algorithm for Reed-Solomon decoding including
any of the ones from Chapter 15.
The crux of the reduction is a natural bijection between the vector space Fm
q and the ﬁeld
Fq m . This bijection converts the space of functions { f |Fm
q → Fq } to the space of functions { f :
Fq m → Fq } ⊆ { f : Fq m → Fq m }. Algorithmically, it is important that the bijection only acts on the
domain and so almost no work is needed to convert a function g ∈ { f |Fm
q → Fq } to its image
G ∈ { f : Fq m → Fq m } under the bijection. Thus Reed-Muller codes get transformed to a subcode
of some Reed-Solomon code, and corrupted Reed-Muller codewords get mapped to corrupted
Reed-Solomon codewords. Now comes the algebraic part: namely, analyzing how good is the
distance of the so-obtained Reed-Solomon code, or equivalently upper bounding the degree
of the polynomials G obtained by applying the bijection to g ∈ RM(q, m, r ). It turns out the
bijection preserves the distance exactly and so algorithms correcting the Reed-Solomon code
up to half its distance does the same for the Reed-Muller code.
In the rest of this section we ﬁrst describe the ‘nice’ bijection Φ from Fq m → Fm
q and intro-
duce a parameter called the extension degree that captures how good the bijection is. Then,
we analyze the extension degree of the bijection map and show that it ends up mapping Reed-
Muller codes to Reed-Solomon codes of the same distance, and thus an algorithm to decode
Reed-Solomon codes with errors up to half the distance of the code also yield algorithms to
decode Reed-Muller code with errors up to half the distance of the code.

14.3.1 A bijection from Fm
q vs. Fq m

The bijections we will eventually work with in this section will be linear-bijections. We introduce
this concept ﬁrst.

Deﬁnition 14.3.1. A function Φ : Fq m → Fm
q is said to be an Fq -linear bijection if

1. Φ is a bijection, i.e., Φ(u) = Φ(v) ⇒ u = v for every u, v ∈ Fq m .

2. Φ is Fq -linear, i.e., for every α, β ∈ Fq and u, v ∈ Fq m it is the case that Φ(αu +βv) = αΦ(u)+
βΦ(v).

(Above and throughout this section it will be useful to remember that Fq ⊆ Fq m and so oper-
ations such as αu for α ∈ Fq and u ∈ Fq m are well-deﬁned.)
Note that a linear bijection Φ : Fq m → Fm
q can be viewed as m functions (Φ1, . . . , Φm) with
Φi : Fq m → Fq so that Φ(u) = (Φ1(u), . . . , Φm(u)). Furthermore each Φi is a linear function from
Fq m → Fq and since Fq ⊆ Fq m , Φi can be viewed as a polynomial in Fq m [Z ] (see Exercise 14.12).
Our proposition below recalls the basic properties of such linearized polynomials.

Proposition 14.3.1. There exists an Fq -linear bijection from Fq m to Fm
q . If Φ = (Φ1, . . . , Φm) :
Fq m → Fm
q is an Fq -linear bijection then each Φi (Z ) is a trace function. Speciﬁcally there exist

239

λ1 . . . , λm ∈ Fq m , which are linearly independent over Fq , such that Φi (Z ) = Tr(λi Z ) = ∑m−1
j =0 λq j

i Z q j .

In particular deg(Φi ) = q m−1 and Φ is a linearized polynomial (i.e., only non-zero coefﬁcients are
for monomials of the form Z q j ).

Proof. Given a bijection Φ the fact that it is a Trace function follows from Proposition D.5.17,
which implies its degree and linearized nature (see Exercise 14.13). All that remains to show
is that a linear bijection exists. We claim that if λ1, . . . , λm ∈ Fq m are Fq -linearly independent
then Φ = (Φ1, . . . , Φm), with Φi (Z ) = Tr(λi Z ), is a Fq linear bijection. Linearity follows from the
linearity of Trace so all we need to verify is that this is a bijection. And since the domain and
range of Φ have the same cardinality, it sufﬁces to show that Φ is surjective. Consider the set

S = {(Φ(u)|u ∈ Fq m } ⊆ Fm
q .

By the linearity of Φ, S is a subspace of Fm
q . If S ̸= Fm
q (i.e., if Φ is not surjective) we must have
that elements of S satisfy some non-trivial constraint, i.e., there exists (α1, . . . , αm) ∈ Fm
q \{0} such
that ∑m
i =1 αi βi = 0 for every (β1, . . . , βm) ∈ S (see Exercise 14.14). But now consider

∑

i αi Φi (Z ) = ∑

i αi Tr (λi Z ) = Tr
 ((
∑

i αi λi
 )
 · Z
 )
 , (14.2)

where the last equality follows from the fact that Tr is a linear map (see Proposition D.5.17). On
the one hand (see Exercise 14.15) this is a non-zero polynomial in Z of degree at most q m−1,
while on the other hand it evaluates to zero on every u ∈ Fq m , which contradicts the degree
mantra. We conclude Φ is surjective, and hence it is an Fq -linear bijection.

Our goal is to use a linear bijection from Φ : Fq m → Fm
q (any such bijection will do for us)
to convert functions whose domain is Fm
q (which is the case for codewords of the Reed-Muller
code) to functions whose domain is Fq m . Speciﬁcally, given f : Fm
q → Fq and Φ : Fq m → Fm
q , let
f ◦ Φ : Fq m → Fm
q be the function ( f ◦ Φ)(u) = f (Φ(u)).
Key to the utility of this transformation is the analysis of how this blows up the degree of
the underlying polynomials. Recall that for a function F : Fq m → Fq m , its degree is deﬁned to be
the degree of the (unique) polynomial P ∈ Fq m [Z ] with deg(P ) < q m such that P (u) = F (u) for
every u ∈ Fq m . Our main challenge henceforth is to understand the question: If f : F
m
q → Fq is
a degree r polynomial, how large can the degree of f ◦ Φ be? We do not answer this question
right away, but deﬁne the parameter quantifying this effect next, and then design and analyze a
Reed-Muller decoding algorithm in terms of this parameter.

Deﬁnition 14.3.2. For prime power q and non-negative integers m and r , let the extension
degree of r over Fq m , denoted Rq,m(r ), be the maximum degree of p ◦ Φ over all choices of p ∈
Fq [X1, . . . , Xm] (or the associated function p : Fm
q → Fq ) of degree at most r and over all Fq -linear
bijections Φ : Fq m → Fq .

Our algorithm and its analysis are quite natural modulo the analysis of Rq,m(r ) and we de-
scribe them below.
 240

Algorithm 20 REED-SOLOMON-BASED DECODER
INPUT: q, r < m(q − 1), 0 ≤ e < (q m − Rq,m(r ))/2, and function f : Fm
q → Fq .
OUTPUT: Output p such deg(p) ≤ r and |{x ∈ F
m
q |P (x) ̸= f (x)}| ≤ e.
Let Φ : Fq m → Fm
q be an Fq -linear bijection

FOR u ∈ Fq m DO
F (u) ← f (Φ(u))

Let P be the output of decoding F using Reed-Solomon codes by Algorithm 21 ⊲ With inputs
k = Rq,m(r ) + 1, n = q m and n pairs (u, F (u)) for every u ∈ Fq m .

FOR u ∈ Fm
q DO
p(u) ← P (Φ
−1(u))

RETURN p

We note that the decoder here outputs a polynomial p ∈ Fq [X1, . . . , Xm] in terms of its func-
tion representation. If a coefﬁcient representation is desired one can use some interpolation
algorithm to convert it. Other than such interpolation, most of the transformation above is
mostly syntactic, since a normal representation of Fq m is already in the form of vectors in Fm
q via
some Fq -linear bijection. The only real work is in the call to the Reed-Solomon decoder.
Below we show that the algorithm above is correct for e < (q m − Rq,m(r ))/2. The crux of the
analysis is in showing that this quantity is actually half the distance of the Reed-Muller code,
and we defer that analysis to the next section.

Proposition 14.3.2. Let f : Fm
q → Fq be any function and let g : Fm
q → Fq be a degree r polynomial
such that |{u ∈ Fm
q | f (u) ̸= g (u)}| ≤ e < (q m−Rq,m(r ))/2. Then REED-SOLOMON-BASED DECODER( f )
returns g

Proof. Let G = g ◦ Φ. Then we have that deg(G) ≤ Rq,m(r ) and we have that {v ∈ Fq m |F (v) ̸=
G(v)}| ≤ e < (q m − Rq,m(r ))/2. Since the distance of the Reed-Solomon code with N = q m and
K = Rm,q (r ) + 1 is N − K + 1 = q m − Rq,m(r ) and e is less than half the distance, we have that
G is the unique polynomial with this property, and so the Reed-Solomon decoder must return
P = G. We conclude that p = P ◦ Φ
−1 = G ◦ Φ
−1 = g , as desired.

14.3.2 Analysis of Extension Degree

We start with a simple warmup result that already leads to an optimal algorithm for decoding
when r < q.

Proposition 14.3.3. Rq,m(r ) ≤ r · q m−1.

Proof. The proof following immediately from the deﬁnition and the fact that linear functions
are polynomials of degree q m−1. Speciﬁcally, let p ∈ Fq [X1, . . . , Xm] be of degree at most r and
let Φ = (Φ1, . . . , Φm) be an Fq -linear bijection. Then since each Φi is a polynomial of degree
q m−1 we have that p(Φ1(Z ), . . . , Φm(Z )) is a polynomial of degree at most r · q m−1. Finally since
the reduction modulo (Z q m − Z ) does not increase the degree we have p ◦ Φ is a polynomial of
degree at most r · q m−1, as desried.
 241

Corollary 14.3.4. If r < q then REED-SOLOMON-BASED DECODER decodes RM(q, m, r ) up to half
its minimum distance.

Proof. By Lemma 9.2.2 we have that the distance of the Reed-Muller code RM(q, m, r ) is (q −
r )·q m−1. From Proposition 14.3.3 we have that REED-SOLOMON-BASED DECODER decodes pro-
vided e < (q m − Rm,q (r ))/2 = (q m − r · q m−1)/2 = (q − r ) · q m−1/2, i.e., up to half the minimum
distance.

Finally we turn to the general case (i.e. r ≥ q). For this part, the crude bound that the
degree of f ◦ Φ is at most q m−1 · deg( f ) is no longer good enough. This bound is larger than q m,
whereas every function has degree at most q m −1. To get the ‘right’ degree bound on the degree
of f ◦ Φ, we now need to use the fact that we can reduce any polynomial modulo (Z q m − Z ) and
this leaves the underlying function on Fq m unchanged. Thus from this point on we will try to
understand the degree of f ◦Φ (mod Z q m − Z ). Using this reduction properly we will eventually
be able to get the correct bound on the degree of f ◦ Φ. We state the bound next and then work
our way towards proving it.

Lemma 14.3.5. Let r = s(q − 1) + t where 0 ≤ t < q − 1. Then Rq,m(r ) = q m − (q − t )q m−s−1.

We ﬁrst state the immediate consequence of Lemma 14.3.5 to the error-correction bound of
the Reed-Solomon-based decoder.

Theorem 14.3.6. For every prime power q, integers m ≥ 1 and 0 ≤ r < m(q − 1), the REED-
SOLOMON-BASED DECODER decodes RM(q, m, r ) up to half its minimum distance.

Proof. Let r = s(q − 1) + t with 0 ≤ t < q − 1. By the polynomial distance lemma (Lemma 9.4.1)
we have that the distance of the Reed-Muller code RM(q, m, r ) is (q − t ) · q m−s−1. Combining
Proposition 14.3.2 with Lemma 14.3.5 we have that REED-SOLOMON-BASED DECODER decodes
provided e < (q m − Rm,q (r ))/2 = (q − t ) · q m−s−1/2, i.e., up to half the minimum distance of
RM(q, r, m).

The proof of Lemma 14.3.5 is somewhat involved and needs some new notions. We intro-
duce these notions next.

Deﬁnition 14.3.3 (q-degree). For integer d , let d0, d1, d2, . . . denote its expansion in base q, i.e.,
d = ∑∞
i =0 di q i and 0 ≤ di < q for every i . For a monomial Z d , deﬁne its q-degree, denoted
degq (Z d ), to be the quantity ∑∞
i =0 di . For a polynomial p(Z ) = ∑d cd Z d , deﬁne its q-degree,

denoted degq (p), to be maxd |cd ̸=0{degq (Z d )}.

For example deg2(X 8 + X 3 + X + 1) = deg2(X 3) = 2.
We describe some basic properties of q-degree below. Informally, the proposition below
proves (in parts (1)-(3)) that the q-degree behaves just like the regular degree when it comes
to addition, multiplication and reduction modulo Z q m − Z . Note that while parts (1) and (2)
are natural, part (3) is already special in that it only holds for reduction modulo some special
polynomials. Finally part (4) of the proposition allows us to related the q-degree of a polynomial
with its actual degree and this will come in useful when we try to bound the degree of f ◦ Φ(
(mod Z )q m − Z ).
 242

Proposition 14.3.7. For every α, β ∈ Fq m and P, P1, P2 ∈ Fq m [Z ] we have:

(1) degq (αP1 + βP2) ≤ max{degq (P1), degq (P2)}.

(2) degq (P1 · P2) ≤ degq (P1) + degq (P2).

(3) degq (P (mod Z q m − Z )) ≤ degq (P ). (Note that here the total degree deg(P ) can be strictly
greater than q m.)

(4) deg(P ) < q m and degq (P ) = s(q − 1) + t for 0 ≤ t < q − 1 implies

deg(P ) ≤ q m − (q − t )q m−s−1.

Proof. Part (1) is immediate from the deﬁnition since the monomials of αP1 + βP2 is in the
union of the monomials of P1 and P2. Next, note that due to part (1), it sufﬁces to prove parts
(2)-(4) for monomials.
For part (2) for monomials, we wish to show that that degq (Z d · Z e ) ≤ degq (Z d ) + degq (Z e).
Let d = ∑i di q i , e = ∑i ei q i and let f = d +e = ∑i fi q i . Then it can be veriﬁed that for every i we
have ∑i
j =0 f j ≤ ∑i
j =0(d j + e j ) (see Exercise 14.16) and this eventually implies

degq (Z d +e) = ∑

j f j ≤ ∑

j (d j + e j ) = degq (Z d ) + degq (Z e). (14.3)

For part (3), note that since Z q i = ((Z q ⌊i /m⌋)m)i mod m,

Z q i (mod Z q m − Z ) = Z q (i mod m).

So Z di q i mod (Z q m − Z ) = Z di q (i mod m). (14.4)

We conclude that for d = ∑i di q i with 0 ≤ di < q we have:

degq (Z d mod (Z q m − Z )) = degq (Z ∑i di q i mod (Z q m − Z ))

≤ degq (Z ∑i di q i mod m )

≤ ∑

i degq (Z di q i mod m )

= ∑

i di

= degq (Z d ) ,

as desried. In the above, the ﬁrst inequality follows from Exercise 14.17 and the second inequal-
ity follows from part (2) while the ﬁnal two equalities follows from deﬁnition of degq (·).
Finally we turn to part (4), which compares the (actual) degree of a polynomial to its q-
degree. Again it sufﬁces to prove for monomials. Let d < q m be given by d = ∑m−1
i =0 di q i . Subject

243

to the condition ∑
i di ≤ s(q − 1) + t , we note that d is maximized when dm−1 = · · · = dm−s =
(q − 1) and dm−s−1 = t (see Exercise 14.18) in which case we get d + (q − t )q m−s−1 = q m, or
d = q m − (q − t )q m−s−1.

Our next lemma relates the degree of a multivariate function f : Fm
q → Fq to the q-degree of
f ◦ Φ for a linear bijection Φ.

Lemma 14.3.8. For every polynomial p ∈ Fq [X1, . . . , Xm] and every Fq -linear bijection, we have
degq (p ◦ Φ) ≤ deg(p).

Proof. By Proposition 14.3.7, part (1), it sufﬁces to prove the lemma for the special case of
monomials. Fix a monomial M (X1, . . . , Xm) = X r1
1 · · · X rm
m with ∑ j r j = r . Also ﬁx an Fq -linear
bijection Φ = (Φ1, . . . , Φm). Let ˜M denote the univariate polynomial M ◦ Φ (mod Z q m − Z ). Note
that M ◦ Φ(Z ) = ∏m
i =1 Φi (Z )ri . And note further that degq (Φi (Z )) = 1 for every i . By Proposi-
tion 14.3.7 part (2), we now conclude that degq (∏m
i =1 Φi (Z )ri ) ≤ ∑m
i =1 ri = r . Finally by Proposi-
tion 14.3.7 part (3) we have that

degq ( ˜M ) = degq (M ◦ Φ (mod Z q m − Z )
) ≤ degq (M ◦ Φ) ≤ r,

as desried.

We are now ready to prove Lemma 14.3.5 which asserts that Rq,m (s(q − 1) + t ) = q m − (q −
t )q m−s−1.

Proof of Lemma 14.3.5. We focus on proving Rq,m(s(q − 1) + t ) ≤ q m − (q − t )q m−s−1. The other
direction follows from Exercise 14.19. Fix a polynomial p ∈ Fq [X1, . . . , Xm] of degree at most
r = s(q − 1) + t and consider the function p ◦ Φ : Fq m → Fq m . This corresponds to the polynomial
˜p(Z ) = p(Φ1(Z ), . . . , Φm(Z )) mod (Z q m − Z )
. By Lemma 14.3.8 we have that degq ( ˜p) ≤ r . And
by construction deg( ˜p) < q m. So by Proposition 14.3.7, part (4), we have that deg( ˜p) ≤ q m −(q −
t )q m−s−1, yielding the lemma.

14.4 Exercises

Exercise 14.1. Show that if q > deg( f ), then for any polynomial P ∈ Fq [X1, . . . , Xm], there exists
an m-dimensional afﬁne form A such that deg(P ◦ A) = deg(P ).

Exercise 14.2. An s-variate d -form is a polynomial a(Z1, . . . , Zm) of degree at most d . Note that
d = 1 gives Deﬁnition 14.1.1. Similar to Deﬁnition 14.1.1 one can deﬁne an m-dimensional s-
variate d -form 〈a1, . . . , am〉. Finally, given such a d -form analogous to Deﬁnition 14.1.2, for an
m-variate polynomial P one can deﬁne P ◦ A.
Prove that deg(P ◦ A) ≤ d · deg(P ).

Exercise 14.3. Prove that for every pair z1 ̸= z2 ∈ Fs
q , for a random afﬁne form A, A(z1) and A(z2)
are distributed uniformly and independently over Fm
q .

244

Exercise 14.4. Show that any two distinct polynomials in Fq [Z1, . . . , Zs] of degree at most r <
q(s − 1) differ in at least two positions x ∈ Fs
q .

Hint: Use the polynomial distance lemma (Lemma 9.4.1).

Exercise 14.5. Let P ∈ Fq [X1, . . . , Xm] be a polynomial of degree at most r , 0 < γ < 1
2 and let
f : Fm
q → Fq be such that

e = |{x ∈ Fm
q | f (x) ̸= P (x)}| ≤ ( 1
2 − γ
) · q m−⌈(r +1)/(q−1)⌉.

Then, for every x ∈ Fm
q , the probability that LOCAL-DECODE-RM-SIMPLE-ITER( f , x) returns P (x)
is at least 1
2 + γ.

Exercise 14.6. Let g : Fm
q → Fq and integer 0 ≤ r < m(q −1)−1 be given. Then one can in O (q 3m)

operations compute a polynomial P ∈ Fq [X1, . . . , Xm] of degree at most r such that for every
x ∈ Fm
q , P (x) = g (x) (if such a polynomial exists).

Hint: Use Exercise 2.6.

Exercise 14.7. If P : Fs
q → Fq is a polynomial of degree r < s(q − 1) then

P (0) = − ∑

z∈Fs
q \{0} P (z).

Hint: Use Exercise 9.15.

Exercise 14.8. Let r = s(q − 1) − t . Then RM(q, s, r ) has distance at least (t + 1)q m−s.

Exercise 14.9. Let f : Fm
2 → F2 differ from a degree r polynomial P (of degree r ) in < 2m−r −1 lo-
cations. Show that majorityb∈Fm−r
2 {∑
a∈Fr
2 f (a, b)} gives the coefﬁcient of X1 · · · Xr in P (X1, . . . , Xm)
and majorityb∈Fm−r
2 {∑
a∈Fr
2 f (b, a)} (note the exchange of a and b) gives the coefﬁcient of Xm−r +1 · · · Xm
in P (X1, . . . , Xm).

Exercise 14.10. Let f , g : Fm
q → Fq disagree in e positions x ∈ Fm
q . Then for any function h : Fm
q →
Fq , the functions f − h and g − h also disagree in e positions.

Exercise 14.11. Let f , g : Fm
q → Fq disagree in e positions x ∈ Fm
q . Fix a subset S ⊆ [m] of size t .
Argue that there are at most e values of b ∈ Fm−t
q for which there is an a ∈ Ft
q such that f (S ←
a, ¯S ← b) ̸= g (S ← a, ¯S ← b).

Exercise 14.12. Let Φ : Fq m → Fm
q be a linear bijection. How that

1. Φ can be viewed as m functions (Φ1, . . . , Φm) with Φi : Fq m → Fq so that Φ(u) = (Φ1(u), . . . , Φm(u)).

2. Furthermore each Φi is a linear function from Fq m → Fq and each Φi can be viewed as a
polynomial in Fq m [Z ].

Exercise 14.13. Show that a linear-bijection is a linearized polynomial of degree q m−1.

Exercise 14.14. Argue that if a linear subspace S ⊂ Fm
q of dimension < m, then there (α1, . . . , αm) ∈
Fm
q \ {0} such that ∑m
i =1 αi βi = 0 for every (β1, . . . , βm) ∈ S.

245

Exercise 14.15. Argue that the polynomial Tr((∑
i αi λi ) · Z ) from (14.2) is

1. Non-zero and has degree at most q m−1; and

2. Evaluates to zero on all u ∈ Fq m .

Exercise 14.16. Let (d0, d1, . . . ) and (e0, e1, . . . ) be d and e in base q ≥ 2. Let f = d + e = ∑
i fi q i .
Then show that for every i we have ∑i
j =0 f j ≤ ∑i
j =0(d j + e j ).

Hint: Use induction.

Exercise 14.17. Show that

degq (Z ∑i di q i mod (Z q m − Z )) ≤ degq (Z ∑i di q i mod m ) .

Exercise 14.18. Show that subject to the condition ∑m−1
i =0 di ≤ s(q − 1) + t , that d = ∑m−1
i =0 di q i is
maximized when dm−1 = · · · = dm−s = (q − 1) and dm−s−1 = t .

Exercise 14.19. T ⊆ Fq be a set of size t . Consider the polynomial

p(X1, . . . , Xm) = (X q−1
1 − 1) · · · (X q−1
s − 1) · ∏

a∈T (X s+1 − a).

Note that deg(p) = s(q − 1) + t .

1. Prove that for every linear bijection Φ, we have deg(p ◦ Φ) ≥ q m − (q − t )q m−s−1.

Hint: How many zeroes does p have? What does this say about the degree of p ◦ Φ?

2. Conclude that Rq,m(r ) ≥ q m − (q − t )q m−s−1, where r = s(q − 1) + t where 0 ≤ t < q − 1.

14.5 Bibliographic Notes

We start with the history of the Majority Logic Decoder, Algorithm 19. This algorithm is the ﬁrst
non-trivial algorithm in coding theory, dating back to the paper of Reed [83] from 1954. Indeed
the codes were proposed by Muller [75] and the reason Reed’s name is associated with the codes
is due to the decoding algorithm. Despite their “in hindsight” simplicity, the algorithm is partic-
ularly clever and subtle. One proof of the subtlety is in the fact that the algorithm doesn’t seem
to extend immediately to non-binary settings — indeed even extending to the ternary case ends
up involving some careful reasoning (and is settled in the work of Kim and Kopparty [61]).
See [103, Chapter 10] for details on near-linear time polynomial interpolation algorithm.
The Simple Reed-Muller Decoder, Algorithm 18, originates from the work of Beaver and
Feigenbaum [7] and Lipton [70]. (We note that neither paper mentions the codes by name,
and only consider the case r < q.) Subsequent works by Gemmell et al. [32] and Gemmell and
Sudan [34] extended these algorithms to correct a number of errors close to (but not matching)
half the distance of the code. These algorithms also played a central role in the theory of “locally
decodable codes” that we will describe later in Chapter ??.
Finally, the Reed-Solomon-based Decoder, Algorithm 20, is due to Pellikaan and Wu [78],
who gave this algorithm in the context of “list-decoding”.

246

Chapter 15

Efﬁcient Decoding of Reed-Solomon Codes

So far in this book, we have shown how to efﬁciently decode explicit codes up to half of the
Zyablov bound (Theorem 12.3.3) and how to efﬁciently achieve the capacity of the BSCp (The-
orem 13.4.1). The proofs of both of these results assumed that one can efﬁciently do unique
decoding for Reed-Solomon codes up to half its distance (Theorem 12.2.1). In this chapter, we
present such a unique decoding algorithm. Then we will generalize the algorithm to a list de-
coding algorithm that efﬁciently achieves the Johnson bound (Theorem 7.3.1).

15.1 Unique decoding of Reed-Solomon codes

Consider the [n, k, d = n−k+1]q Reed-Solomon code with evaluation points (α1, · · · , αn). (Recall
Deﬁnition 5.2.1.) Our goal is to describe an algorithm that corrects up to e < n−k+1
2 errors in
polynomial time. Let y = (y1, · · · , yn) ∈ Fn
q be the received word. We will now do a syntactic shift
that will help us better visualize all the decoding algorithms in this chapter better. In particular,
we will also think of y as the set of ordered pairs {(α1, y1), (α2, y2), . . . , (αn, yn)}, that is, we think of
y as a collection of “points" in “2-D space." See Figure 15.1 for an illustration. From now on, we
will switch back and forth between our usual vector interpretation of y and this new geometric
notation.
Further, let us assume that there exists a polynomial P (X ) of degree at most k − 1 such that
∆ (
y, (P (αi ))
n
i =1) ≤ e. (Note that if such a P (X ) exists then it is unique.) See Figure 15.2 for an
illustration.
We will use reverse engineering to design a unique decoding algorithm for Reed-Solomon
codes. We will assume that we somehow know P (X ) and then prove some identities involving
(the coefﬁcients of) P (X ). Then to design the algorithm we will just use the identities and try
to solve for P (X ). Towards this end, let us assume that we also magically got our hands on a
polynomial E (X ) such that
 E (αi ) = 0 if and only if yi ̸= P (αi ) .

E (X ) is called an error-locator polynomial. We remark that there exists such a polynomial of

247

−7
 αi

2

3
 1 3 5

4

1
 −1

−2

−3

−4

−2−4−6
 −5 −3 −1
 2 4 6

n = 14, k = 2, e = 6

−7 7

yi

5

6

7
 −5

−6

Figure 15.1: An illustration of a received word for a [14, 2] Reed-Solomon code
(we have implicitly embedded the ﬁeld Fq in the set {−7, . . . , 7}). The evalua-
tions points are (−7, −5, −4, −3, −2, −1, 0, 1, 2, 3, 4, 5, 6, 7) and the received word is
(−7, 5, −4, −3, 2, −4, 0, 1, −2, 3, 4, −5, −2, 7).

degree at most e. In particular, consider the polynomial:

E (X ) = ∏

i :yi ̸=P (αi ) (X − αi ) .

See Figure 15.3 for an illustration of the E (X ) corresponding to the received word in Figure 15.1.

Now we claim that for every 1 ≤ i ≤ n,

yi E (αi ) = P (αi ) E (αi ) . (15.1)

To see why (15.1) is true, note that if yi ̸= P (αi ), then both sides of (15.1) are 0 (as E (αi ) = 0).
On the other hand, if yi = P (αi ), then (15.1) is obviously true.
All the discussion above does not seem to have made any progress as both E (X ) and P (X )
are unknown. Indeed, the task of the decoding algorithm is to ﬁnd P (X )! Further, if E (X ) is
known then one can easily compute P (X ) from y (the proof is left as an exercise). However,
note that we can now try and do reverse engineering. If we think of coefﬁcients of P (X ) (of
which there are k) and the coefﬁcients of E (X ) (of which there are e + 1) as variables, then we
have n equations from (15.1) in e + k + 1 variables. From our bound on e, this implies we have
more equations than variables. Thus, if we could solve for these unknowns, we would be done.

248
 P (X ) = X

2

3
 1 3 5

4

1
 −1

−2

−3

−4

−2−4−6
 −5 −3 −1
 2 4 6

n = 14, k = 2, e = 6

−7 7

yi

5

6

7
 −5

−6

−7
 αi

Figure 15.2: An illustration of the closest codeword P (X ) = X for the received word from Fig-
ure 15.1. Note that we are considering polynomials of degree 1, which are “lines."

However, there is a catch– these n equations are quadratic equations, which in general are NP-
hard to solve. However, note that for our choice of e, we have e + k − 1 ≪ n. Next, we will exploit
this with a trick that is sometimes referred to as linearization. The idea is to introduce new
variables so that we can convert the quadratic equations into linear equations. Care must be
taken so that the number of variables after this linearization step is still smaller than the (now
linear) n equations. Now we are in familiar territory as we know how to solve linear equations
over a ﬁeld (e.g. by Gaussian elimination). (See section 15.4 for some more discussion on the
hardness of solving quadratic equations and the linearization technique.)

To perform linearization, deﬁne N (X ) def
= P (X ) · E (X ). Note that N (X ) is a polynomial of
degree less than or equal to e + k − 1. Further, if we can ﬁnd N (X ) and E (X ), then we are done.
This is because we can compute P (X ) as follows:

P (X ) = N (X )
E (X ) .

The main idea in the Welch-Berlekamp algorithm is to “forget" what N (X ) and E (X ) are
meant to be (other than the fact that they are degree bounded polynomials).

15.1.1 Welch-Berlekamp Algorithm

Algorithm 21 formally states the Welch-Berlekamp algorithm.
As we have mentioned earlier, computing E (X ) is as hard as ﬁnding the solution polynomial
P (X ). Also in some cases, ﬁnding the polynomial N (X ) is as hard as ﬁnding E (X ). E.g., given

249

E (X ) is the product of these lines
 αi

2

3
 1 3 5

4

1
 −1

−2

−3

−4

−2−4−6
 −5 −3 −1
 2 4 6

−7 7

yi

5

6

7
 −5

−6

−7

n = 14, k = 2, e = 6

Figure 15.3: An illustration of the the error locator polynomial E (X ) = (X + 5)(X + 2)(X + 1)(X −
2)(X − 5)(X − 6) for the received word from Figure 15.1. Note that E (X ) is the product of the
green lines.

N (X ) and y (such that yi ̸= 0 for 1 ≤ i ≤ n) one can ﬁnd the error locations by checking positions
where N (αi ) = 0. While each of the polynomials E (X ) , N (X ) is hard to ﬁnd individually, the
main insight in the Welch-Berlekamp algorithm is that computing them together is easier.
Next we analyze the correctness and run time of Algorithm 21.

Correctness of Algorithm 21. Note that if Algorithm 21 does not output fail, then the algo-
rithm produces a correct output. Thus, to prove the correctness of Algorithm 21, we just need
the following result.

Theorem 15.1.1. If (P (αi ))n
i =1 is transmitted (where P (X ) is a polynomial of degree at most k −1)
and at most e < n−k+1
2 errors occur (i.e. ∆(y, (P (αi ))n
i =1) ≤ e), then the Welch-Berlekamp algo-
rithm outputs P (X ).

The proof of the theorem above follows from the subsequent claims.

Claim 15.1.2. There exist a pair of polynomials E ∗(X ) and N ∗(X ) that satisfy Step 1 such that
N ∗(X )
E ∗(X ) = P (X ).

Note that now it sufﬁces to argue that N1(X )
E1(X ) = N2(X )
E2(X ) for any pair of solutions ((N1(X ), E1(X ))
and (N2(X ), E2(X )) that satisfy Step 1, since Claim 15.1.2 above can then be used to see that ratio
must be P (X ). Indeed, we will show this to be the case:

250

Algorithm 21 Welch-Berlekamp Algorithm

INPUT: n ≥ k ≥ 1, 0 < e < n−k+1
2 and n pairs {(αi , yi )}n
i =1 with αi distinct
OUTPUT: Polynomial P (X ) of degree at most k − 1 or fail.

1: Compute a non-zero polynomial E (X ) of degree exactly e, and a polynomial N (X ) of degree
at most e + k − 1 such that yi E (αi ) = N (αi ) 1 ≤ i ≤ n. (15.2)

2: IF E (X ) and N (X ) as above do not exist or E (X ) does not divide N (X ) THEN

3: RETURN fail

4: P (X ) ← N (X )
E (X ) .

5: IF ∆(y, (P (αi ))n
i =1) > e THEN

6: RETURN fail

7: ELSE

8: RETURN P (X )

Claim 15.1.3. If any two distinct solutions (E1(X ), N1(X )) ̸= (E2(X ), N2(X )) satisfy Step 1, then
they will satisfy N1(X )
E1(X ) = N2(X )
E2(X ) .

Proof of Claim 15.1.2. We just take E ∗(X ) to be the error-locating polynomial for P (X ) and let
N ∗(X ) = P (X )E ∗(X ) where deg(N ∗(X )) ≤ deg(P (X ))+deg(E ∗(X )) ≤ e+k−1. In particular, deﬁne
E ∗(X ) as the following polynomial of degree exactly e:

E ∗(X ) = X e−∆(
y,(P (αi ))n=1) ∏

1≤i ≤n|yi ̸=P (αi )(X − αi ). (15.3)

By deﬁnition, E ∗(X ) is a non-zero polynomial of degree e with the following property:

E ∗(αi ) = 0 iff yi ̸= P (αi ).

We now argue that E ∗(X ) and N ∗(X ) satisfy (15.2). Note that if E ∗(αi ) = 0, then N ∗(αi ) =
P (αi )E ∗(αi ) = yi E ∗(αi ) = 0. When E ∗(αi ) ̸= 0, we know P (αi ) = yi and so we still have P (αi )E ∗(αi ) =
yi E ∗(αi ), as desired.

Proof of Claim 15.1.3. Note that the degrees of the polynomials N1(X )E2(X ) and N2(X )E1(X )
are at most 2e + k − 1. Let us deﬁne polynomial R(X ) with degree at most 2e + k − 1 as follows:

R(X ) = N1(X )E2(X ) − N2(X )E1(X ). (15.4)

Furthermore, from Step 1 we have, for every i ∈ [n] ,

N1(αi ) = yi E1(αi ) and N2(αi ) = yi E2(αi ). (15.5)

251

Substituting (15.5) into (15.4) we get for 1 ≤ i ≤ n:

R(αi ) = (yi E1(αi ))E2(αi ) − (yi E2(αi ))E1(αi )

= 0.

The polynomial R(X ) has n roots and

deg(R(X )) ≤ e + k − 1 + e

= 2e + k − 1

< n,

Where the last inequality follows from the upper bound on e. Since deg(R(X )) < n, by the degree
mantra (Proposition 5.2.3) we have R(X ) ≡ 0. This implies that N1(X )E2(X ) ≡ N2(X )E1(X ). Note
that as E1(X ) ̸= 0 and E2(X ) ̸= 0, this implies that N1(X )
E1(X ) = N2(X )
E2(X ) , as desired.

Implementation of Algorithm 21. In Step 1, N (X ) has e + k unknowns and E (X ) has e + 1
unknowns. For each 1 ≤ i ≤ n, the constraint in (15.2) is a linear equation in these unknowns.
Thus, we have a system of n linear equations in 2e + k + 1 < n + 2 unknowns. By claim 15.1.2,
this system of equations have a solution. The only extra requirement is that the degree of the
polynomial E (X ) should be exactly e. We have already shown E (X ) in equation (15.3) to satisfy
this requirement. So we add a constraint that the coefﬁcient of X e in E (X ) is 1. Therefore, we
have n + 1 linear equation in at most n + 1 variables, which we can solve in time O(n3), e.g. by
Gaussian elimination.
Finally, note that Step 4 can be implemented in time O(n3) by “long division.” Thus, we have
proved

Theorem 15.1.4. For any [n, k]q Reed-Solomon code, unique decoding can be done in O(n3) time
up to d −1
2 = n−k
2 number of errors.

Recall that the above is a restatement of the error decoding part of Theorem 12.2.1. Thus,
this ﬁlls in the ﬁnal missing piece from the proofs of Theorem 12.3.3 (decoding certain concate-
nated codes up to half of their design distance) and Theorem 13.4.1 (efﬁciently achieving the
BSCp capacity).

15.2 List Decoding Reed-Solomon Codes

Recall Question 7.4.3, which asks if there is an efﬁcient list decoding algorithm for a code of rate
R > 0 that can correct 1 − p
R fraction of errors. Note that in the question above, explicitness is
not an issue as e.g., a Reed-Solomon code of rate R by the Johnson bound is (1 − p
R,O(n2))-list
decodable (Theorem 7.3.1).
We will study an efﬁcient list decoding algorithm for Reed-Solomon codes that can correct
up to 1 − p
R fraction of errors. To this end, we will present a sequence of algorithms for (list)
decoding Reed-Solomon codes that ultimately will answer Question 7.4.3.

252

Before we talk about the algorithms, we restate the (list) decoding problem for Reed-Solomon
codes. Consider any [n, k]q Reed-Solomon code that has the evaluation set {α1, . . . , αm}. Below
is a formal deﬁnition of the decoding problem for Reed-Solomon codes:

• Input: Received word y = (y1, . . . , yn), yi ∈ Fq and error parameter e = n − t .

• Output: All polynomials P (X ) ∈ Fq [X ] of degree at most k − 1 such that P (αi ) = yi for
at least t values of i .

Our main goal of course is to make t as small as possible.

We begin with the unique decoding regime, where t > n + k
2 . We looked at the Welch-

Berlekamp algorithm in Algorithm 21, which we restate below in a slightly different form (that
will be useful in developing the subsequent list decoding algorithms).

• Step 1: Find polynomials N (X ) of degree k + e − 1, and E (X ) of degree e such that

N (αi ) = yi E (αi ), for every 1 ≤ i ≤ n

• Step 2: If Y −P (X ) divides Q(X , Y ) = Y E (X )−N (X ), then output P (X ) (assuming ∆(y, (P (αi ))n
i =1) ≤
e).

Note that Y −P (X ) divides Q(X , Y ) in Step 2 above if and only if P (X ) = N (X )
E (X ) , which is exactly
what Step 4 does in Algorithm 21.

15.2.1 Structure of list decoding algorithms for Reed-Solomon

Note that the Welch-Berlekamp Algorithm has the following general structure:

• Step 1: (Interpolation Step) Find non-zero Q(X , Y ) such that Q(αi , yi ) = 0, 1 ≤ i ≤ n.

• Step 2: (Root Finding Step) If Y − P (X ) is a factor of Q(X , Y ), then output P (X ) (assuming
it is close enough to the received word).

In particular, in the Welch-Berlekamp algorithm we have Q(X , Y ) = Y E (X )−N (X ) and hence,
Step 2 is easy to implement.
All the list decoding algorithms that we will consider in this chapter will have the above
two-step structure. The algorithms will differ in how exactly Step 1 is implemented. Before we
move on to the details, we make one observation that will effectively “take care of" Step 2 for us.
Note that Step 2 can be implemented if one can factorize the bivariate polynomial Q(X , Y ) (and
then only retain the linear factors of the form Y − P (X )). Fortunately, it is known that factoring
bivariate polynomials can be done in polynomial time (see e.g. [59]). We will not prove this
result in the book but will use this fact as a given.
Finally, to ensure the correctness of the two-step algorithm above for Reed-Solomon codes,
we will need to ensure the following:
 253

• Step 1 requires solving for the co-efﬁcients of Q(X , Y ). This can be done as long as the
number of coefﬁcients is greater than the the number of constraints. (The proof of this
fact is left as an exercise.) Also note that this argument is a departure from the correspond-
ing argument for the Welch-Berlekamp algorithm (where the number of coefﬁcients is
upper bounded by the number of constraints).

• In Step 2, to ensure that for every polynomial P (X ) that needs to be output Y − P (X ) di-
vides Q(X , Y ), we will add restrictions on Q(X , Y ). For example, for the Welch-Berlekamp
algorithm, the constraint is that Q(X , Y ) has to be of the form Y E (X ) − N (X ), where E (X )
and N (X ) are non-zero polynomials of degree e and at most e + k − 1 respectively.

Next, we present the ﬁrst instantiation of the algorithm structure above, which leads us to
our ﬁrst list decoding algorithm for Reed-Solomon codes.

15.2.2 Algorithm 1

The main insight in the list decoding algorithm that we will see is that if we carefully control the
degree of the polynomial Q(X , Y ), then we can satisfy the required conditions that will allow
us to make sure Step 1 succeeds. Then we will see that the degree restrictions, along with the
degree mantra (Proposition 5.2.3) will allow us to show Step 2 succeeds too. The catch is in
deﬁning the correct notion of degree of a polynomial. We do that next.
First, we recall the deﬁnition of maximum degree of a variable.

Deﬁnition 15.2.1. degX (Q) is the maximum degree of X in Q(X , Y ). Similarly, degY (Q) is the
maximum degree of Y in Q(X , Y )

For example, for Q(X , Y ) = X 2Y 3 + X 4Y 2 degX (Q) = 4 and degY (Q) = 3. Given degX (Q) = a
and degY (Q) = b, we can write Q(X , Y ) = ∑

0≤i ≤a,
0≤ j ≤b
 ci j X i Y j ,

where the coefﬁcients ci j ∈ Fq . Note that the number of coefﬁcients is equal to (a + 1)(b + 1).
The main idea in the ﬁrst list decoding algorithm for Reed-Solomon code is to place bounds
on degX (Q) and degY (Q) for Step 1. The bounds are chosen so that there are enough variables
to guarantee the existence of a Q(X , Y ) with the required properties. We will then use these
bound along with the degree mantra (Proposition 5.2.3) to argue that Step 2 works. Algorithm 22
presents the details. Note that the algorithm generalizes the Welch-Berlekamp algorithm (and
follows the two step skeleton outlined above).

Correctness of Algorithm 22. To ensure the correctness of Step 1, we will need to ensure that
the number of coefﬁcients for Q(X , Y ) (which is (ℓ + 1)(n/ℓ + 1)) is larger than the number of
constraints in (15.6 (which is n). Indeed,

(ℓ + 1) · ( n
ℓ + 1) > ℓ · n
ℓ = n.

254

Algorithm 22 The First List Decoding Algorithm for Reed-Solomon Codes
INPUT: n ≥ k ≥ 1, ℓ ≥ 1, e = n − t and n pairs {(αi , yi )}n
i =1
OUTPUT: (Possibly empty) list of polynomials P (X ) of degree at most k − 1

1: Find a non-zero Q(X , Y ) with degX (Q) ≤ ℓ, degY (Q) ≤ n
ℓ such that

Q(αi , yi ) = 0, 1 ≤ i ≤ n. (15.6)

2: L ← ;

3: FOR every factor Y − P (X ) of Q(X , Y ) DO

4: IF ∆(y, (P (αi ))n
i =1) ≤ e and deg(P ) ≤ k − 1 THEN

5: Add P (X ) to L.

6: RETURN L

To argue that the ﬁnal L in Step 6 contains all the polynomials P (X ) that need to be output.
In other words, we need to show that if P (X ) of degree ≤ k−1 agrees with Y in at least t positions,
then Y − P (X ) divides Q(X , Y ). Towards this end, we deﬁne

R(X ) def
= Q(X , P (X )).

Note that Y − P (X ) divides Q(X , Y ) if and only if R(X ) ≡ 0. Thus, we need to show R(X ) ≡ 0. For
the sake of contradiction, assume that R(X ) ̸≡ 0. Note that

deg(R) ≤ degX (Q) + deg(P ) · degY (Q) (15.7)

≤ ℓ + n(k − 1)
ℓ . (15.8)

On the other hand, if P (αi ) = yi then (15.6) implies that

Q(αi , yi ) = Q(αi , P (αi )) = 0.

Thus, αi is a root of R(X ). In other words R has at least t roots. Note that the degree mantra
(Proposition 5.2.3) this will lead to a contradiction if t > deg(R), which will be true if

t > ℓ + n(k − 1)
ℓ .

If we pick ℓ = p
n(k − 1), we will have t > 2pn(k − 1). Thus, we have shown

Theorem 15.2.1. Algorithm 22 can list decode Reed-Solomon codes of rate R from 1 − 2pR frac-
tion of errors. Further, the algorithm can be implemented in polynomial time.

The claim on the efﬁcient run time follows as Step 1 can be implemented by Gaussian elim-
ination and for Step 3, all the factors of Q(X , Y ) (and in particular all linear factors of the form
Y − P (X )) can be computed using e.g. the algorithm from [59].
The bound 1 − 2p
R is better than the unique decoding bound of 1−R
2 for R < 0.07. This is
still far from the 1 − p
R fraction of errors guaranteed by the Johnson bound. See Figure 15.2.2
for an illustration.
 255

 0

 0.2

 0.4

 0.6

 0.8

 1
  0  0.2  0.4  0.6  0.8  1R
δ
 Unique Decoding bound
Johnson bound
Algorithm 1

Figure 15.4: The tradeoff between rate R and the fraction of errors that can be corrected by
Algorithm 22.

15.2.3 Algorithm 2

To motivate the next algorithm, recall that in Algorithm 22, in order to prove that the root

ﬁnding step (Steps 3-6 in Algorithm 22) works, we deﬁned a polynomial R(X ) def
= Q(X , P (X )).
In particular, this implied that deg(R) ≤ degX (Q) + (k − 1) · degY (Q) (and we had to select t >
degX (Q) + (k − 1) · degY (Q)). One shortcoming of this approach is that the maximum degree of
X and Y might not occur in the same term. For example, in the polynomial X 2Y 3 + X 4Y 2, the
maximum X and Y degrees do not occur in the same monomial. The main insight in the new
algorithm is to use a more “balanced" notion of degree of Q(X , Y ):

Deﬁnition 15.2.2. The (1, w) weighted degree of the monomial X i Y j is i + w j . Further, the
(1, w)-weighted degree of Q(X , Y ) (or just its (1, w) degree) is the maximum (1, w) weighted
degree of its monomials.

For example, the (1, 2)-degree of the polynomial X Y 3 + X 4Y is max(1+3·2, 4+2·1) = 7. Also
note that the (1, 1)-degree of a bivariate polynomial Q(X , Y ) is its total degree (or the “usual"
deﬁnition of degree of a bivariate polynomial). Finally, we will use the following simple lemma
(whose proof we leave as an exercise):

Lemma 15.2.2. Let Q(X , Y ) be a bivariate polynomial of (1, w) degree D. Let P (X ) be a polyno-
mial such that deg(P ) ≤ w. Then we have

deg (Q(X , P (X ))) ≤ D.

256

Note that a bivariate polynomial Q(X , Y ) of (1, w) degree at most D can be represented as
follows: Q(X , Y ) def
= ∑

i +w j ≤D
i , j ≥0
 ci , j X i Y j ,

where ci , j ∈ Fq .
The new algorithm is basically the same as Algorithm 22, except that in the interpolation
step, we compute a bivariate polynomial of bounded (1, k − 1) degree. Before we state the pre-
cise algorithm, we will present the algorithm via an example. Consider the received word in
Figure 15.5.
 6

yi
 αi

2

3
 1 3 5

n = 14, k = 2, e = 9

4

1
 −1

−2

−3

−4

−2−4−6
 −5 −3 −1
 2 4

Figure 15.5: An illustration of a received word for the [14, 2] Reed-Solomon code from Fig-
ure 15.1 (where again we have implicitly embedded the ﬁeld Fq in the set {−7, . . . , 7}). Here we
have considered e = 9 errors which is more than what Algorithm 21 can handle. In this case, we
are looking for lines that pass through at least 5 points.

Now we want to interpolate a bivariate polynomial Q(X , Y ) with a (1, 1) degree of 4 that
“passes" through all the 2-D points corresponding to the received word from Figure 15.5. Fig-
ure 15.6 shows such an example.
Finally, we want to factorize all the linear factors Y − P (X ) of the Q(X , Y ) from Figure 15.6.
Figure 15.7 shows the two polynomials X and −X such that Y − X and Y + X are factors of
Q(X , Y ) from Figure 15.6.
We now precisely state the new list decoding algorithm in Algorithm 23.

Proof of Correctness of Algorithm 23. As in the case of Algorithm 22, to prove the correctness
of Algorithm 23, we need to do the following:
 257
 6

yi
 αi

2

3
 1 3 5
 L2(X , Y ) = Y − X

E (X , Y ) = Y 2/16 + X 2/49 − 1

Q(X , Y ) = L1(X , Y ) · L2(X , Y ) · E (X , Y )

n = 14, k = 2, e = 9
 L1(X , Y ) = Y + X

4

1
 −1

−2

−3

−4

−2−4−6
 −5 −3 −1
 2 4

Figure 15.6: An interpolating polynomial Q(X , Y ) for the received word in Figure 15.5.

6

yi
 αi

2

3
 1 3 5
 L2(X , Y ) = Y − X

E (X , Y ) = Y 2/16 + X 2/49 − 1

Q(X , Y ) = L1(X , Y ) · L2(X , Y ) · E (X , Y )

n = 14, k = 2, e = 9
 L1(X , Y ) = Y + X

4

1
 −1

−2

−3

−4

−2−4−6
 −5 −3 −1
 2 4

Figure 15.7: The two polynomials that need to be output are shown in blue.

• (Interpolation Step) Ensure that the number of coefﬁcients of Q(X , Y ) is strictly greater
than n.

• (Root Finding Step) Let R(X ) def
= Q(X , P (X )). We want to show that if P (αi ) ≥ yi for at least
t values of i , then R(X ) ≡ 0.

To begin with, we argue why we can prove the correctness of the root ﬁnding step. Note that
since Q(X , Y ) has (1, k − 1) degree at most D, Lemma 15.2.2 implies that

deg(R) ≤ D.

Then using the same argument as we used for the correctness of the root ﬁnding step of Algo-
rithm 22, we can ensure R(X ) ≡ 0 if we pick
 t > D.

258

Algorithm 23 The Second List Decoding Algorithm for Reed-Solomon Codes
INPUT: n ≥ k ≥ 1, D ≥ 1, e = n − t and n pairs {(αi , yi )}n
i =1
OUTPUT: (Possibly empty) list of polynomials P (X ) of degree at most k − 1

1: Find a non-zero Q(X , Y ) with (1, k − 1) degree at most D, such that

Q(αi , yi ) = 0, 1 ≤ i ≤ n. (15.9)

2: L ← ;

3: FOR every factor Y − P (X ) of Q(X , Y ) DO

4: IF ∆(y, (P (αi ))n
i =1) ≤ e and deg(P ) ≤ k − 1 THEN

5: Add P (X ) to L.

6: RETURN L

Thus, we would like to pick D to be as small as possible. On the other hand, Step 1 will need D
to be large enough (so that the number of variables is more than the number of constraints in
(15.9). Towards that end, let the number of coefﬁcients of Q(X , Y ) be

N = ∣{(i , j )|i + (k − 1) j ≤ D, i , j ∈ Z+}∣

To bound N , we ﬁrst note that in the deﬁnition above, j ≤ ⌊ D

k−1 ⌋. (For notational convenience,
deﬁne ℓ = ⌊ D
k−1 ⌋.) Consider the following sequence of relationships

N = ℓ∑

j =1

D−(k−1) j∑

i =0 1

= ℓ∑

j =0
(D − (k − 1) j + 1)

= ℓ∑

j =0
(D + 1) − (k − 1) ℓ∑

j =0 j

= (D + 1)(ℓ + 1) − (k − 1)ℓ(ℓ + 1)
2

= ℓ + 1
2 (2D + 2 − (k − 1)ℓ)

≥ ( ℓ + 1
2
 ) (D + 2) (15.10)

≥ D(D + 2)
2(k − 1) . (15.11)

In the above, (15.10) follows from the fact that ℓ ≤ D
k−1 and (15.11) follows from the fact that
D
k−1 − 1 ≤ ℓ.
 259

Thus, the interpolation step succeeds (i.e. there exists a non-zero Q(X , Y ) with the required
properties) if D(D + 2)
2(k − 1) > n.

The choice D = ⌈√
2(k − 1)n⌉

sufﬁces by the following argument:

D(D + 2)
2(k − 1) > D 2

2(k − 1) ≥ 2(k − 1)n
2(k − 1) = n.

Thus for the root ﬁnding step to work, we need t > ⌈p2(k − 1)n⌉, which implies the following
result:

Theorem 15.2.3. Algorithm 2 can list decode Reed-Solomon codes of rate R from up to 1 − p
2R
fraction of errors. Further, the algorithm runs in polynomial time.

Algorithm 2 runs in polynomial time as Step 1 can be implemented using Gaussian elimi-
nation (and the fact that the number of coefﬁcients is O(n)) while the root ﬁnding step can be
implemented by any polynomial time algorithm to factorize bivariate polynomials. Further, we
note that 1 − p
2R beats the unique decoding bound of (1 − R)/2 for R < 1/3. See Figure 15.2.3
for an illustration.

 0

 0.2

 0.4

 0.6

 0.8

 1
  0  0.2  0.4  0.6  0.8  1R
δ
 Unique Decoding bound
Johnson bound
Algorithm 1
Algorithm 2

Figure 15.8: The tradeoff between rate R and the fraction of errors that can be corrected by
Algorithm 22 and Algorithm 23.
 260

15.2.4 Algorithm 3

Finally, we present the list decoding algorithm for Reed-Solomon codes, which can correct 1 −pR fraction of errors. The main idea is to add more restrictions on Q(X , Y ) (in addition to its
(1, k − 1)-degree being at most D). This change will have the following implications:

• The number of constraints will increase but the number of coefﬁcients will remain the
same. This seems to be bad as this results in an increase in D (which in turn would result
in an increase in t ).

• However, this change will also increases the number of roots of R(X ) and this gain in the
number of roots more than compensates for the increase in D.

In particular, the constraint is as follows. For some integer parameter r ≥ 1, we will insist on
Q(X , Y ) having r roots at (αi , yi ), 1 ≤ i ≤ n.
To motivate the deﬁnition of multiplicity of a root of a bivariate polynomial, let us consider
the following simpliﬁed examples. In Figure 15.9 the curve Q(X , Y ) = Y − X passes through the

X

Y
 (0, 0)
 Y − X

Figure 15.9: Multiplicity of 1

origin once and has no term of degree 0.
In Figure 15.10, the curve Q(X , Y ) = (Y − X )(Y + X ) passes though the origin twice and has
no term with degree at most 1.
In Figure 15.11, the curve Q(X , Y ) = (Y − X )(Y + X )(Y − 2X ) passes through the origin thrice
and has no term with degree at most 2. More generally, if r lines pass through the origin, then
note that the curve corresponding to their product has no term with degree at most r − 1. This
leads to the following more general deﬁnition:

Deﬁnition 15.2.3. Q(X , Y ) has r roots at (0, 0) if Q(X , Y ) doesn’t have any monomial with degree
at most r − 1.
 261

Y + X
 X

Y
 (0, 0)
 Y − X

Figure 15.10: Multiplicity of 2

Y − 2X
 X

Y
 (0, 0)
 Y − X
Y + X
 Figure 15.11: Multiplicity of 3

The deﬁnition of a root with multiplicity r at a more general point follows from a simple
translation:

Deﬁnition 15.2.4. Q(X , Y ) has r roots at (α, β) if Qα,β(X , Y ) def
= Q(x +α, y +β) has r roots at (0, 0).

Before we state the precise algorithm, we will present the algorithm with an example. Con-
sider the received word in Figure 15.12.
Now we want to interpolate a bivariate polynomial Q(X , Y ) with (1, 1) degree 5 that “passes
twice" through all the 2-D points corresponding to the received word from Figure 15.12. Fig-
ure 15.13 shows such an example.
Finally, we want to factorize all the linear factors Y − P (X ) of the Q(X , Y ) from Figure 15.13.
Figure 15.14 shows the ﬁve polynomials of degree one are factors of Q(X , Y ) from Figure 15.13.

262

n = 10, k = 2, e = 6

yi
 αi

−1

−5

−7−9 1 2 5 8 11

Figure 15.12: An illustration of a received word for the [10, 2] Reed-Solomon code (where we
have implicitly embedded the ﬁeld Fq in the set {−9, . . . , 11}). Here we have considered e = 6
errors which is more than what Algorithm 23 can decode. In this case, we are looking for lines
that pass through at least 4 points.
 n = 10, k = 2, e = 6

yi
 αi

−1

−5

−7−9 1 2 5 8 11

Figure 15.13: An interpolating polynomial Q(X , Y ) for the received word in Figure 15.12.

(In fact, Q(X , Y ) exactly decomposes into the ﬁve lines.)
Algorithm 24 formally states the algorithm.

Correctness of Algorithm 24. To prove the correctness of Algorithm 24, we will need the fol-
lowing two lemmas (we defer the proofs of the lemmas above to Section 15.2.4):

Lemma 15.2.4. The constraints in (15.12) imply (r +1
2 ) constraints for each i on the coefﬁcients of
Q(X , Y ).
 263

n = 10, k = 2, e = 6

yi
 αi

−1

−5

−7−9 1 2 5 8 11

Figure 15.14: The ﬁve polynomials that need to be output are shown in blue.

Algorithm 24 The Third List Decoding Algorithm for Reed-Solomon Codes
INPUT: n ≥ k ≥ 1, D ≥ 1, r ≥ 1, e = n − t and n pairs {(αi , yi )}n
i =1
OUTPUT: (Possibly empty) list of polynomials P (X ) of degree at most k − 1

1: Find a non-zero Q(X , Y ) with (1, k − 1) degree at most D, such that

Q(αi , yi ) = 0, with multiplicity r for every 1 ≤ i ≤ n. (15.12)

2: L ← ;

3: FOR every factor Y − P (X ) of Q(X , Y ) DO

4: IF ∆(y, (P (αi ))n
i =1) ≤ e and deg(P ) ≤ k − 1 THEN

5: Add P (X ) to L.

6: RETURN L

Lemma 15.2.5. R(X ) def
= Q(X , P (X )) has r roots for every i such that P (αi ) = yi . In other words,
(X − αi )r divides R(X ).

Using arguments similar to those used for proving the correctness of Algorithm 23, to argue
the correctness of the interpolations step we will need

D(D + 2)
2(k − 1) > n
(r + 1
2
 )
,

where the LHS is an upper bound on the number of coefﬁcients of Q(X , Y ) as before from
(15.11) and the RHS follows from Lemma 15.2.4. We note that the choice

D = ⌈√
(k − 1)nr (r − 1)
⌉

264

works. Thus, we have shown the correctness of Step 1.
For the correctness of the root ﬁnding step, we need to show that the number of roots of
R(X ) (which by Lemma 15.2.5 is at least r t ) is strictly bigger than the degree of R(X ), which
from Lemma 15.2.2 is D. That is we would be ﬁne we if have,

t r > D,

which is the same as
 t > D
r ,

which in turn will follow if we pick
 t =
 ⌈√

(k − 1)n (1 − 1
r
 )⌉
 .

If we pick r = 2(k − 1)n, then we will need

t >
 ⌈√

(k − 1)n − 1
2
 ⌉
 > ⌈√
(k − 1)n⌉ ,

where the last inequality follows because of the fact that t is an integer. Thus, we have shown

Theorem 15.2.6. Algorithm 24 can list decode Reed-Solomon codes of rate R from up to 1 − p
R
fraction of errors. Further, the algorithm runs in polynomial time.

The claim on the run time follows from the same argument that was used to argue the poly-
nomial running time of Algorithm 23. Thus, Theorem 15.2.6 shows that Reed-Solomon codes
can be efﬁciently decoded up to the Johnson bound. For an illustration of fraction of errors
correctable by the three list decoding algorithms we have seen, see Figure 15.2.3.
A natural question to ask is if Reed-Solomon codes of rate R can be list decoded beyond
1 − pR fraction of errors. The answer is still not known:

Open Question 15.2.1. Given a Reed-Solomon code of rate R, can it be efﬁciently list decoded
beyond 1 − p
R fraction of errors?

Recall that to complete the proof of Theorem 15.2.6, we still need to prove Lemmas 15.2.4
and 15.2.5, which we do next.

Proof of key lemmas

Proof of Lemma 15.2.4. Let Q(X , Y ) = ∑

i , j
i +(k−1) j ≤D
 ci , j X i Y j

265

and Qα,β(X , Y ) = Q(X + α, Y + β) = ∑

i , j c α,β
i , j X i Y j .

We will show that

(i) c α,β
i , j are homogeneous linear combinations of ci , j ’s.

(ii) If Qα,β(X , Y ) has no monomial with degree < r , then that implies (r +1
2 ) constraints on

c α,β
i , j ’s.

Note that (i) and (ii) prove the lemma. To prove (i), note that by the deﬁnition:

Qα,β(X , Y ) = ∑

i , j c α,β
i , j X i Y j (15.13)

= ∑

i ′, j ′

i ′+(k−1) j ′≤D
 ci ′, j ′(X + α)i ′(Y + β) j ′ (15.14)

Note that, if i > i ′ or j > j ′, then c α,β
i , j doesn’t depend on c i ′, j ′. By comparing coefﬁcients of X i Y j

from (15.13) and (15.14), we obtain

c α,β
i , j = ∑

i ′>i
j ′> j
 ci ′, j ′
(i ′

i
 )( j ′

j
 )

α
i β j ,

which proves (i). To prove (ii), recall that by deﬁnition Qα,β(X , Y ) has no monomial of degree

< r . In other words, we need to have constraints c α,β
i , j = 0 if i + j ≤ r − 1. The number of such
constraints is
 |{(i , j )|i + j ≤ r − 1, i , j ∈ Z≥0}| =
 (r + 1
2
 )

,

where the equality follows from the following argument. Note that for every ﬁxed value of 0 ≤
j ≤ r − 1, i can take r − j values. Thus, we have that the number of constraints is

r −1∑

j =0 r − j = r∑

ℓ=1 ℓ =
 (r + 1
2
 )

,

as desired.

We now re-state Lemma 15.2.5 more precisely and then prove it.

Lemma 15.2.7. Let Q(X , Y ) be computed by Step 1 in Algorithm 24. Let P (X ) be a polynomial
of degree ≤ k − 1, such that P (αi ) = yi for at least t > D
r many values of i , then Y − P (X ) divides
Q(X , Y ).
 266

Proof. Deﬁne
 R(X ) def
= Q(X , P (X )).

As usual, to prove the lemma, we will show that R(X ) ≡ 0. To do this, we will use the following
claim.

Claim 15.2.8. If P (αi ) = yi , then (X − αi )r divides R(X ), that is αi is a root of R(X ) with multi-
plicity r .

Note that by deﬁnition of Q(X , Y ) and P (X ), R(X ) has degree ≤ D. Assuming the above claim
is correct, R(X ) has at least t · r roots. Therefore, by the degree mantra (Proposition 5.2.3), R(X )
is a zero polynomial as t · r > D. We will now prove Claim 15.2.8. Deﬁne

Pαi ,yi (X ) def
= P (X + αi ) − yi , (15.15)

and
 Rαi ,yi (X ) def
= R(X + αi ) (15.16)

= Q(X + αi , P (X + αi )) (15.17)

= Q(X + αi , Pαi ,yi (X ) + yi ) (15.18)

= Qαi ,yi (X , Pαi ,yi (X )), (15.19)

where (15.17), (15.18) and (15.19) follow from the deﬁnitions of R(X ), Pαi ,yi (X ) and Qαi ,yi (X , Y )
respectively.
By (15.16) if Rαi ,yi (0) = 0, then R(αi ) = 0. So, if X divides Rαi ,yi (X ), then X − αi divides R(X ).
(This follows from a similar argument that we used to prove Proposition 5.2.3.) Similarly, if X r

divides Rαi ,yi (X ), then (X − αi )r divides R(X ). Thus, to prove the lemma, we will show that X r

divides Rαi ,yi (X ). Since P (αi ) = yi when αi agrees with yi , we have Pαi ,yi (0) = 0. Therefore, X is
a root of Pαi ,yi (X ), that is, Pαi ,yi (X ) = X · g (X ) for some polynomial g (X ) of degree at most k −1.
We can rewrite
 Rαi ,yi (X ) = ∑

i ′, j ′ c αi ,yi
i ′, j ′ X i ′(Pαi ,yi (X )) j ′ = ∑

i ′, j ′ c αi ,yi
i ′, j ′ X i ′(X g (X )) j ′.

Now for every i ′, j ′ such that c αi ,yi
i ′, j ′ ̸= 0, we have i ′ + j ′ ≥ r as Qαi ,yi (X , Y ) has no monomial of

degree < r . Thus X r divides Rαi ,yi (X ), since Rαi ,yi (x) has no non-zero monomial X ℓ for any
ℓ < r .

15.3 Extensions

We now make some observations about Algorithm 24. In particular, the list decoding algorithm
is general enough to solve more general problems than just list decoding. In this section, we
present an overview of these extensions.
 267

Recall that the constraint (15.12) states that Q(X , Y ) has r ≥ 0 roots at (αi , yi ), 1 ≤ i ≤ n.
However, our analysis did not explicitly use the fact that the multiplicity is same for every i . In
particular, given non-zero integer multiplicities wi ≥ 0, 1 ≤ i ≤ n, Algorithm 24 can be general-
ized to output all polynomials P (X ) of degree at most k − 1, such that

∑

i :P (αi )=yi wi >
 √
√
√
√(k − 1)n n∑

i =0
 (wi + 1
2
 )

.

(We leave the proof as an exercise.) Note that till now we have seen the special case wi = r ,
1 ≤ i ≤ n.
Further, we claim that the αi ’s need not be distinct for the all of the previous arguments to
go through. In particular, one can generalize Algorithm 24 even further to prove the following
(the proof is left as an exercise):

Theorem 15.3.1. Given integer weights wi ,α for every 1 ≤ i ≤ n and α ∈ F, in polynomial time
one can output all P (X ) of degree at most k − 1 such that

∑

i wi ,P (αi ) >
 √
√
√
√(k − 1)n n∑

i =0
 ∑

α∈F
 (wi ,α + 1
2
 )
.

This will be useful to solve the following generalization of list decoding called soft decoding.

Deﬁnition 15.3.1. Under soft decoding problem, the decoder is given as input a set of non-
negative weights wi ,d (1 ≤ i ≤ n, α ∈ Fq ) and a threshold W ≥ 0. The soft decoder needs to output
all codewords (c1, c2, . . . , cn) in q-ary code of block length n that satisfy:

n∑

i =1 wi ,ci ≥ W.

Note that Theorem 15.3.1 solve the soft decoding problem with

W =
 √
√
√
√(k − 1)n n∑

i =0
 ∑

α∈F
 (wi ,α + 1
2
 )

.

Consider the following special case of soft decoding where wi ,yi = 1 and wi ,α = 0 for α ∈ F \
{yi } (1 ≤ i ≤ n). Note that this is exactly the list decoding problem with the received word
(y1, . . . , yn). Thus, list decoding is indeed a special case of soft decoding. Soft decoding has
practical applications in settings where the channel is analog. In such a situation, the “quan-
tizer” might not be able to pinpoint a received symbol yi with 100% accuracy. Instead, it can
use the weight wi ,α to denote its conﬁdence level that i th received symbol was α.
Finally, we consider a special case of soft called list recovery, which has applications in de-
signing list decoding algorithms for concatenated codes.

268

Deﬁnition 15.3.2 (List Recovery). Given Si ⊆ Fq , 1 ≤ i ≤ n where |Si | ≤ ℓ, output all [n, k]q
codewords (c1, . . . , cn) such that ci ∈ Si for at least t values of i . If for every valid input the
number of such codewords is at most L, then the corresponding code is called (1 − t /n, ℓ, L)-
list recoverable.

We leave the proof that list decoding is a special case of soft decoding as an exercise. Finally,
we claim that Theorem 15.3.1 implies the following result for list recovery (the proof is left as an
exercise):

Theorem 15.3.2. Given t > p(k − 1)ℓn, the list recovery problem with agreement parameter t for
[n, k]q Reed-Solomon codes can be solved in polynomial time.

15.4 Bibliographic Notes

In 1960, before polynomial time complexity was regarded as an acceptable notion of efﬁciency,
Peterson designed an O(N 3) time algorithm for the unique decoding of Reed-Solomon codes [80].
This algorithm was the ﬁrst efﬁcient algorithm for unique decoding of Reed-Solomon codes.
The Berlekamp-Massey algorithm, which used shift registers for multiplication, was even more
efﬁcient, achieving a computational complexity of O (N 2)
. Currently, an even more efﬁcient
algorithm, with a computational complexity of O (N poly(log N ))
, is known [82].
The Welch-Berlekamp algorithm, covered under US Patent [104], has a running time com-
plexity of O (N 3)
. We will follow a description of the Welch-Berlekamp algorithm provided by
Gemmell and Sudan in [33].
Håstad, Philips and Safra showed that solving a system of quadratic equations (even those
without any square terms like we have in (15.1)) over any ﬁeld Fq is NP-hard [55]. (In fact, it is
even hard to approximately solve this problem: i.e. where one tries to compute an assignment
that satisﬁes as many equations as possible.) Linearization is a trick that has been used many
times in theoretical computer science and cryptography. See this blog post by Dick Lipton for
more on this.
Algorithm 23 is due to Sudan [96] and Algorithm 24 is due to Guruswami and Sudan [48].
Near-linear time implementations of these list decoding algorithms are also known [2].
It is natural to ask whether Theorem 15.3.2 is tight for list recovery, i.e. generalize Open
Question 15.2.1 to list recovery. It was shown by Guruswami and Rudra that Theorem 15.3.2 is
indeed the best possible list recovery result for Reed-Solomon codes [43]. Thus, any algorithm
that answers Open Question 15.2.1 in some sense has to exploit the fact that in the list decoding
problem, the αi ’s are distinct. Recently it was shows by Rudra and Wootters that at least combi-
natorially, Reed-Solomon codes (with random evaluation points) are list decodable beyond the
Johnson bound [87]. On the ﬂip side, there are limits known on list decoding Reed-Solomon
codes (both unconditional ones due to Ben-Sasson et al. [8] as well as those based on hardness
of computing discrete log in the worst-case due to Cheng and Wan [16]) but none of them are
close to the Johnson bound (especially for constant rate Reed-Solomon codes).

269270

Chapter 16

Efﬁciently Achieving List Decoding Capacity

In the previous chapters, we have seen these results related to list decoding:

• Reed-Solomon codes of rate R > 0 can be list-decoded in polynomial time from 1 − p
R
errors (Theorem 15.2.6). This is the best algorithmic list decoding result we have seen so
far.

• There exist codes of rate R > 0 that are (
1 − R − ε,O ( 1
ε ))
-list decodable for q ≥ 2Ω( 1
ε ) (and
in particular for q = poly(n)) (Theorem 7.4.1 and Proposition 3.3.2). This of course is the
best possible combinatorial result.

Note that there is a gap between the algorithmic result and the best possible combinatorial
result. This leads to the following natural question:

Question 16.0.1. Are there explicit codes of rate R > 0 that can be list-decoded in polynomial
time from 1 − R − ε fraction of errors for q ≤ pol y(n)?

In this chapter, we will answer Question 16.0.1 in the afﬁrmative.

16.1 Folded Reed-Solomon Codes

We will now introduce a new type of code called the Folded Reed-Solomon codes. These codes
are constructed by combining every m consecutive symbols of a regular Reed-Solomon code
into one symbol from a larger alphabet. Note that we have already seen such a folding trick
when we instantiated the outer code in the concatenated code that allowed us to efﬁciently
achieve the BSCp capacity (Section 13.4.1). For a Reed-Solomon code that maps Fk
q → Fn
q , the
corresponding Folded Reed-Solomon code will map Fk
q → Fn/m
q m . We will analyze Folded Reed-

Solomon codes that are derived from Reed-Solomon codes with evaluation {1, γ, γ
2, γ
3, . . . , γ
n−1},

271

f (1) f (γ) f (γ
2) f (γ
3) · · · f (γ
n−2) f (γ
n−1)

Figure 16.1: Encoding f (X ) of degree ≤ k−1 and coefﬁcients in Fq corresponding to the symbols
in the message.

where γ is the generator of F∗
q and n ≤ q − 1. Note that in the Reed-Solomon code, a message is
encoded as in Figure 16.1.
For m = 2, the conversion from Reed-Solomon to Folded Reed-Solomon can be visualized
as in Figure 16.2 (where we assume n is even).

f (1) f (γ) f (γ
2) f (γ
3) · · · f (γ
n−2) f (γ
n−1)
⇓

f (1) f (γ
2) · · · f (γ
n−2)

f (γ) f (γ
3) f (γ
n−1)

Figure 16.2: Folded Reed-Solomon code for m = 2

For general m ≥ 1, this transformation will be as in Figure 16.3 (where we assume that m
divides n).
 f (1) f (γ) f (γ
2) f (γ
3) · · · f (γ
n−2) f (γ
n−1)
⇓

f (1) f (γ
m) f (γ
2m)
 · · ·
 f (γ
n−m)

f (γ) f (γ
m+1) f (γ
2m+1) f (γ
n−m+1)

... ... ... ...

f (γ
m−1) f (γ
2m−1) f (γ
3m−1) f (γ
n−1)

Figure 16.3: Folded Reed-Solomon code for general m ≥ 1

More formally, here is the deﬁnition of folded Reed-Solomon codes:

Deﬁnition 16.1.1 (Folded Reed-Solomon Code). The m-folded version of an [n, k]q Reed-Solomon
code C (with evaluation points {1, γ, . . . , γ
n−1}), call it C ′, is a code of block length N = n/m over
Fq m , where n ≤ q − 1. The encoding of a message f (X ), a polynomial over Fq of degree at most
k − 1, has as its j ’th symbol, for 0 ≤ j < n/m, the m-tuple ( f (γ j m) , f (
γ j m+1) , · · · , f (γ j m+m−1))
.

272

In other words, the codewords of C ′ are in one-one correspondence with those of the Reed-
Solomon code C and are obtained by bundling together consecutive m-tuple of symbols in
codewords of C .

16.1.1 The Intuition Behind Folded Reed-Solomon Codes

We ﬁrst make the simple observation that the folding trick above cannot decrease the list de-
codability of the code. (We have already seen this argument earlier in Section 13.4.1.)

Claim 16.1.1. If the Reed-Solomon code can be list-decoded from ρ fraction of errors, then the
corresponding folded Reed-Solomon code with folding parameter m can also be list-decoded from
ρ fraction of errors.

Proof. The idea is simple: If the Reed-Solomon code can be list decoded from ρ fraction of
errors (by say an algorithm A ), the Folded Reed-Solomon code can be list decoded by “unfold-
ing" the received word and then running A on the unfolded received word and returning the
resulting set of messages. Algorithm 25 has a more precise statement.

Algorithm 25 Decoding Folded Reed-Solomon Codes by Unfolding

INPUT: y = ((y1,1, . . . , y1,m), . . . , (yn/m,1, . . . , yn/m,m)) ∈ Fn/m
q m
OUTPUT: A list of messages in Fk
q

1: y
′ ← (y1,1, . . . , y1,m, . . . , yn/m,1, . . . , yn/m,m) ∈ Fn
q .

2: RETURN A (y
′)

The reason why Algorithm 25 works is simple. Let m ∈ Fk
q be a message. Let RS(m) and
FRS(m) be the corresponding Reed-Solomon and folded Reed-Solomon codewords. Now for
every i ∈ [n/m], if FRS(m)i ̸= (yi ,1, . . . , yi ,n/m) then in the worst-case for every j ∈ [n/m], RS(m)(i −1)n/m+ j ̸=
yi , j : i.e. one symbol disagreement over Fq m can lead to at most m disagreements over Fq . See
Figure 16.4 for an illustration.
f (1) f (γ
2) · · · f (γ
n−2)

f (γ) f (γ
3) f (γ
n−1)
⇓

f (1) f (γ) f (γ
2) f (γ
3) · · · f (γ
n−2) f (γ
n−1)

Figure 16.4: Error pattern after unfolding. A pink cell means an error: for the Reed-Solomon
code it is for RS(m) with y
′ and for folded Reed-Solomon code it is for FRS(m) with y

This implies that for any m ∈ Fk
q if ∆(y, FRS(m)) ≤ ρ · n
m , then ∆(y
′, RS(m)) ≤ m · ρ · n
m = ρ · n,
which by the properties of algorithm A implies that Step 2 will output m, as desired.

273

The intuition for a strict improvement by using Folded Reed-Solomon codes is that if the
fraction of errors due to folding increases beyond what it can list-decode from, that error pat-
tern does not need to be handled and can be ignored. For example, suppose a Reed-Solomon
code that can be list-decoded from up to 1
2 fraction of errors is folded into a Folded Reed-
Solomon code with m = 2. Now consider the error pattern in Figure 16.5.

f (1) f (γ) f (γ
2) f (γ
3) · · · f (γ
n−2) f (γ
n−1)
⇓

f (1) f (γ
2) · · · f (γ
n−2)

f (γ) f (γ
3) f (γ
n−1)

Figure 16.5: An error pattern after folding. The pink cells denotes the location of errors

The error pattern for Reed-Solomon code has 1
2 fraction of errors, so any list decoding al-
gorithm must be able to list-decode from this error pattern. However, for the Folded Reed-
Solomon code the error pattern has 1 fraction of errors which is too high for the code to list-
decode from. Thus, this “folded" error pattern case can be discarded from the ones that a list
decoding algorithm for folded Reed-Solomon code needs to consider. This is of course one
example– however, it turns out that this folding operation actually rules out a lot of error pat-
terns that a list decoding algorithm for folded Reed-Solomon code needs to handle (even be-
yond the current best 1 − p
R bound for Reed-Solomon codes). Put another way, an algorithm
for folded Reed-Solomon codes has to solve the list decoding problem for the Reed-Solomon
codes where the error patterns are “bunched" together (technically they’re called bursty er-
rors). Of course, converting this intuition into a theorem takes more work and is the subject
of this chapter.

Wait a second... The above argument has a potential hole– what if we take the argument to
the extreme and "cheat" by setting m = n where any error pattern for the Reed-Solomon code
will result in an error pattern with 100% errors for the Folded Reed-Solomon code: thus, we
will only need to solve the problem of error detection for Reed-Solomon codes (which we can
easily solve for any linear code and in particular for Reed-Solomon codes)? It is a valid concern
but we will “close the loophole" by only using a constant m as the folding parameter. This
will still keep q to be polynomially large in n and thus, we would still be on track to answer
Question 16.0.1. Further, if we insist on smaller list size (e.g. one independent of n), then we can
use code concatenation to achieve capacity achieving results for codes over smaller alphabets.
(See Section 16.4 for more.)

General Codes. We would like to point out that the folding argument used above is not speciﬁc
to Reed-Solomon codes. In particular, the argument for the reduction in the number of error
patterns holds for any code. In fact, one can prove that for general random codes, with high

274

probability, folding does strictly improve the list decoding capabilities of the original code. (The
proof is left as an exercise.)

16.2 List Decoding Folded Reed-Solomon Codes: I

We begin with an algorithm for list decoding folded Reed-Solomon codes that works with agree-
ment t ∼ mR N . Note that this is a factor m larger than the R N agreement we ultimately want.
In the next section, we will see how to knock off the factor of m.
Before we state the algorithm, we formally (re)state the problem we want to solve:

• Input: An agreement parameter 0 ≤ t ≤ N and the received word:

y =
 



 y0 ym · · · yn−m
... ... ...
ym−1 y2m−1 yn−1
 


 ∈ Fm×N
q , N = n
m

• Output: Return all polynomials f (X ) ∈ Fq [X ] of degree at most k − 1 such that for at
least t values of 0 ≤ i < N
 



 f (
γ
mi )

...
f (
γ
m(i +1)−1)
 


 =
 



 ymi
...
ym(i +1)−1
 


 (16.1)

The algorithm that we will study is a generalization of the Welch-Berlekamp algorithm (Al-
gorithm 21). However unlike the previous list decoding algorithms for Reed-Solomon codes
(Algorithms 22, 23 and 24), this new algorithm has more similarities with the Welch-Berlekamp
algorithm. In particular, for m = 1, the new algorithm is exactly the Welch-Berlekamp algo-
rithm. Here are the new ideas in the algorithm for the two-step framework that we have seen in
the previous chapter:

• Step 1: We interpolate using (m +1)-variate polynomial, Q(X , Y1, . . . , Ym), where degree of
each variable Yi is exactly one. In particular, for m = 1, this interpolation polynomial is
exactly the one used in the Welch-Berlekamp algorithm.

• Step 2: As we have done so far, in this step, we output all "roots" of Q. Two remarks are in
order. First, unlike Algorithms 22, 23 and 24, the roots f (X ) are no longer simpler linear
factors Y − f (X ), so one cannot use a factorization algorithm to factorize Q(X , Y1, . . . , Ym).
Second, the new insight in this algorithm, is to show that all the roots form an (afﬁne)
subspace,1 which we can use to compute the roots.

1An afﬁne subspace of Fk
q is a set {v + u|u ∈ S}, where S ⊆ Fk
q is a linear subspace and v ∈ Fk
q .

275

Algorithm 26 has the details.

Algorithm 26 The First List Decoding Algorithm for Folded Reed-Solomon Codes
INPUT: An agreement parameter 0 ≤ t ≤ N , parameter D ≥ 1 and the received word:

y =
 



 y0 ym · · · yn−m
... ... ...
ym−1 y2m−1 yn−1
 


 ∈ Fm×N
q , N = n
m

OUTPUT: All polynomials f (X ) ∈ Fq [X ] of degree at most k − 1 such that for at least t values of
0 ≤ i < N
 



 f (
γ
mi )

...
f (
γ
m(i +1)−1)
 


 =
 



 ymi
...
ym(i +1)−1
 


 (16.2)

1: Compute a non-zero Q(X , Y1, . . . , Ym) where

Q(X , Y1, . . . , Ym) = A0(X ) + A1(X )Y1 + A2(X )Y2 + · · · + Am(X )Ym

with deg(A0) ≤ D + k − 1 and deg(A j ) ≤ D for 1 ≤ j ≤ m such that

Q(γ
mi , ymi , · · · , ym(i +1)−1) = 0, ∀0 ≤ i < N (16.3)

2: L ← ;

3: FOR every f (X ) ∈ Fq [X ] such that Q(X , f (X ), f (γX ), f (γ
2X ), . . . , f (γ
m−1X )) = 0 DO

4: IF deg( f ) ≤ k − 1 and f (X ) satisﬁes (16.2) for at least t values of i THEN

5: Add f (X ) to L.

6: RETURN L

Correctness of Algorithm 26. In this section, we will only concentrate on the correctness of
the algorithm and analyze its error correction capabilities. We will defer the analysis of the
algorithm (and in particular, proving a bound on the number of polynomials that are output by
Step 6) till the next section.
We ﬁrst begin with the claim that there always exists a non-zero choice for Q in Step 1 using
the same arguments that we have used to prove the correctness of Algorithms 23 and 24:

Claim 16.2.1. If (m + 1) (D + 1) + k − 1 > N , then there exists a non-zero Q (X , Y1, ...Ym) that satis-
ﬁes the required properties of Step 1.

Proof. As in the proof of correctness of Algorithms 22, 23 and 24, we will think of the constraints
in (16.3) as linear equations. The variables are the coefﬁcients of Ai (X ) for 0 ≤ i ≤ m. With the

276

stipulated degree constraints on the Ai (X )’s, note that the number of variables participating in
(16.3) is D + k + m(D + 1) = (m + 1) (D + 1) + k − 1.

The number of equations is N . Thus, the condition in the claim implies that we have strictly
more variables then equations and thus, there exists a non-zero Q with the required properties.

Next, we argue that the root ﬁnding step works (again using an argument very similar to
those that we have seen for Algorithms 22, 23 and 24):

Claim 16.2.2. If t > D +k −1, then all polynomial f (X ) ∈ Fq [X ] of degree at most k −1 that agree
with the received word in at least t positions is returned by Step 6.

Proof. Deﬁne the univariate polynomial

R (X ) = Q (X , f (X ) , f (γX ) , ..... f (
γ
m−1X )) .

Note that due to the degree constraints on the Ai (X )’s and f (X ), we have

deg (R) ≤ D + k − 1,

since deg( f (γ
i X )) = deg( f (X )). On the other hand, for every 0 ≤ i < N where (16.1) is satisﬁed
we have R (
γ
mi ) = Q (γ
mi , ymi , . . . , ym(i +1)−1) = 0,

where the ﬁrst equality follows from (16.1), while the second equality follows from (16.3). Thus
R(X ) has at least t roots. Thus, the condition in the claim implies that R(X ) has more roots then
its degree and thus, by the degree mantra (Proposition 5.2.3) R(X ) ≡ 0, as desired.

Note that Claims 16.2.1 and 16.2.2 prove the correctness of the algorithm. Next we analyze
the fraction of errors the algorithm can correct. Note that the condition in Claim 16.2.1 is satis-
ﬁed if we pick
 D = ⌊ N − k + 1
m + 1
 ⌋ .

This in turn implies that the condition in Claim 16.2.2 is satisﬁed if

t > N − k + 1
m + 1 + k − 1 = N + m(k − 1)
m + 1 .

Thus, the above would be satisﬁed if

t ≥ N
m + 1 + mk
m + 1 = N ( 1
m + 1 + mR ( m
m + 1
 )) ,

where the equality follows from the fact that k = mR N .
Note that when m = 1, the above bound exactly recovers the bound for the Welch-Berlekamp
algorithm (Theorem 15.1.4). Thus, we have shown that

277

 0

 0.2

 0.4

 0.6

 0.8

 1
  0  0.2  0.4  0.6  0.8  1R
δ
 m=1
m=2
m=2
m=4
Johnson bound

Figure 16.6: The tradeoff between rate R and the fraction of errors that can be corrected by
Algorithm 26 for folding parameter m = 1, 2, 3 and 4. The Johnson bound is also plotted for
comparison. Also note that the bound for m = 1 is the Unique decoding bound achieved by
Algorithm 21.

Theorem 16.2.3. Algorithm 26 can list decode folded Reed-Solomon code with folding parameter
m ≥ 1 and rate R up to m
m+1 (1 − mR) fraction of errors.

See Figure 16.2 for an illustration of the tradeoff for m = 1, 2, 3, 4.
Note that if we can replace the mR factor in the bound from Theorem 16.2.3 by just R then
we can approach the list decoding capacity bound of 1 − R. (In particular, we would be able
to correct 1 − R − ε fraction of errors if we pick m = O(1/ε).) Further, we need to analyze the
number of polynomials output by the root ﬁnding step of the algorithm (and then analyze the
runtime of the algorithm). In the next section, we show how we can “knock-off" the extra factor
m (and we will also bound the list size).

16.3 List Decoding Folded Reed-Solomon Codes: II

In this section, we will present the ﬁnal version of the algorithm that will allow us to answer
Question 16.0.1 in the afﬁrmative. We start off with the new idea that allows us to knock off the
factor of m. (It would be helpful to keep the proof of Claim 16.2.2 in mind.)
To illustrate the idea let us consider the folding parameter to be m = 3. Let f (X ) be a poly-
nomial of degree at most k − 1 that needs to be output and let 0 ≤ i < N be a position where it
agrees with the received word. (See Figure 16.7 for an illustration.)

278

f (γ
3i ) f (γ
3i +1) f (γ
3i +2)

y3i y3i +1 y3i +2

Figure 16.7: An agreement in position i .

The idea is to “exploit" this agreement over one F3
q symbol and convert it into two agree-
ments over Fq 2. (See Figure 16.8 for an illustration.)

f (γ
3i ) f (γ
3i +1) f (γ
3i +1) f (γ
3i +2)

y3i y3i +1 y3i +1 y3i +2

Figure 16.8: More agreement with a sliding window of size 2.

Thus, in the proof of Claim 16.2.2, for each agreement we can now get two roots for the
polynomial R(X ). In general for an agreement over one Fq m symbols translates into m − s + 1
agreement over Fs
q for any 1 ≤ s ≤ m (by “sliding a window" of size s over the m symbols from
Fq ). Thus, in this new idea the agreement is m − s + 1 times more than before which leads to the
mR term in Theorem 16.2.3 going down to mR
m−s+1 . Then making s smaller than m but still large
enough we can get down the relative agreement to R + ε, as desired. There is another change
that needs to be done to make the argument go through: the interpolation polynomial Q now
has to be (s + 1)-variate instead of the earlier (m + 1)-variate polynomial. Algorithm 27 has the
details.

Correctness of Algorithm 27. Next, we analyze the correctness of Algorithm 27 as well as com-
pute its list decoding error bound. We begin with the result showing that there exists a Q with
the required properties for Step 1.

Lemma 16.3.1. If D ≥ ⌊ N (m−s+1)−k+1
s+1
 ⌋
, then there exists a non-zero polynomial Q(X , Y1, ..., Ys)
that satisﬁes Step 1 of the above algorithm.

Proof. Let us consider all coefﬁcients of all polynomials Ai as variables. Then the number of
variables will be D + k + s(D + 1) = (s + 1)(D + 1) + k − 1.

On the other hand, the number of constraints in (16.5), i.e. the number of equations when
all coefﬁcients of all polynomials Ai are considered variables) will be N (m − s + 1).
Note that if we have more variables than equations, then there exists a non-zero Q that
satisﬁes the required properties of Step 1. Thus, we would be done if we have:

(s + 1)(D + 1) + k − 1 > N (m − s + 1),

which is equivalent to:
 D > N (m − s + 1) − k + 1
s + 1 − 1.

279

Algorithm 27 The Second List Decoding Algorithm for Folded Reed-Solomon Codes
INPUT: An agreement parameter 0 ≤ t ≤ N , parameter D ≥ 1 and the received word:

y =
 



 y0 ym · · · yn−m
... ... ...
ym−1 y2m−1 yn−1
 


 ∈ Fm×N
q , N = n
m

OUTPUT: All polynomials f (X ) ∈ Fq [X ] of degree at most k − 1 such that for at least t values of
0 ≤ i < N
 



 f (
γ
mi )

...
f (
γ
m(i +1)−1)
 


 =
 



 ymi
...
ym(i +1)−1
 


 (16.4)

1: Compute non-zero polynomial Q(X , Y1, .., Ys) as follows:

Q(X , Y1, .., Ys) = A0(X ) + A1(X )Y1 + A2(X )Y2 + .. + As(X )Ys,

with deg[A0] ≤ D + k − 1 and deg[Ai ] ≤ D for every 1 ≤ i ≤ s such that for all 0 ≤ i < N and
0 ≤ j ≤ m − s, we have Q(γ
i m+ j , yi m+ j , ..., yi m+ j +s−1) = 0. (16.5)

2: L ← ;

3: FOR every f (X ) ∈ Fq [X ] such that

Q (X , f (X ), f (
γX ) , f (
γ
2X ) , . . . , f (
γs−1X )) ≡ 0 (16.6)

DO

4: IF deg( f ) ≤ k − 1 and f (X ) satisﬁes (16.2) for at least t values of i THEN

5: Add f (X ) to L.

6: RETURN L

The choice of D in the statement of the claim satisﬁes the condition above, which complete the
proof.

Next we argue that the root ﬁnding step works.

Lemma 16.3.2. If t > D+k−1
m−s+1 , then every polynomial f (X ) that needs to be output satisﬁes (16.6).

Proof. Consider the polynomial R(X ) = Q (X , f (X ), f (
γX ) , ..., f (
γs−1X ))
. Because the degree of
f (γ
ℓX ) (for every 0 ≤ ℓ ≤ s − 1) is at most k − 1,

deg(R) ≤ D + k − 1. (16.7)

280

Let f(X) be one of the polynomials of degree at most k − 1 that needs to be output, and f (X )
agrees with the received word at column i for some 0 ≤ i < N , that is:











 f (
γ
mi )

f (
γ
mi +1)

·
·
·
f (γ
m(i +1)−1)
 









 =
 









 ymi
ymi +1
·
·
·
ym(i +1)−1
 









 ,

then for all 0 ≤ j ≤ m − s, we have:

R (γ
mi + j ) = Q (γ
mi + j , f (γ
mi + j ) , f (
γ
mi +1+ j ) , ..., f (γ
mi +s−1+ j ))

= Q (γ
mi + j , ymi + j , ymi +1+ j , ..., ymi +s−1+ j ) = 0.

In the above, the ﬁrst equality follows as f (X ) agrees with y in column i while the second equal-
ity follows from (16.5). Thus, the number of roots of R(X ) is at least

t (m − s + 1) > D + k − 1 ≥ deg(R),

where the ﬁrst inequality follows from the assumption in the claim and the second inequality
follows from (16.7). Hence, by the degree mantra R(X ) ≡ 0, which shows that f (X ) satisﬁes
(16.6), as desired.

16.3.1 Error Correction Capability

Now we analyze the the fraction of errors the algorithm above can handle. (We will come back
to the thorny issue of proving a bound on the output list size for the root ﬁnding step in Sec-
tion 16.3.2.)
The argument for the fraction of errors follows the by now standard route. To satisfy the
constraint in Lemma 16.3.1, we pick

D = ⌊ N (m − s + 1) − k + 1
s + 1
 ⌋ .

This along with the constraint in Lemma 16.3.2, implies that the algorithm works as long as

t > ⌊ D + k − 1
m − s + 1
 ⌋ .

The above is satisﬁed if we choose

t >
 N (m−s+1)−k+1
s+1 + k − 1

m − s + 1 = N (m − s + 1) − k + 1 + (k − 1)(s + 1)
(m − s + 1)(s + 1) = N (m − s + 1) + s(k − 1)
(s + 1)(m − s + 1) .

281

Thus, we would be ﬁne if we pick

t > N
s + 1 + s
s + 1 · k
m − s + 1 = N ( 1
s + 1 + ( s
s + 1
 ) ( m
m − s + 1
 ) · R) ,

where the equality follows from the fact that k = mR N . This implies the following result:

Theorem 16.3.3. Algorithm 27 can list decode folded Reed-Solomon code with folding parameter
m ≥ 1 and rate R up to s
s+1 (1 − mR/(m − s + 1)) fraction of errors.

See Figure 16.3.1 for an illustration of the bound above.

 0

 0.2

 0.4

 0.6

 0.8

 1
  0  0.2  0.4  0.6  0.8  1R
δ
 m=6,s=6
m=9, s=6
m=12, s=6
m=15, s=6
Johnson bound

Figure 16.9: The tradeoff between rate R and the fraction of errors that can be corrected by
Algorithm 27 for s = 6 and folding parameter m = 6, 9, 12 and 15. The Johnson bound is also
plotted for comparison.

16.3.2 Bounding the Output List Size

We ﬁnally address the question of bounding the output list size in the root ﬁnding step of the
algorithm. We will present a proof that will immediately lead to an algorithm to implement the
root ﬁnding step. We will show that there are at most q s−1 possible solutions for the root ﬁnding
step.
The main idea is the following: think of the coefﬁcients of the output polynomial f (X ) as
variables. Then the constraint (16.6) implies D +k linear equations on these k variables. It turns
out that if one picks only k out of these D +k constraints, then the corresponding constraint ma-
trix has rank at least k − s + 1, which leads to the claimed bound. Finally, the claim on the rank

282

of the constraint matrix follows by observing (and this is the crucial insight) that the constraint
matrix is upper triangular. Further, the diagonal elements are evaluation of a non-zero polyno-
mial of degree at most s − 1 in k distinct elements. By the degree mantra (Proposition 5.2.3),
this polynomial can have at most s − 1 roots, which implies that at least k − s + 1 elements of the
diagonal are non-zero, which then implies the claim. See Figure 16.10 for an illustration of the
upper triangular system of linear equations.
 =

B (1)
B (γ)
B (γ2)
B (γ3)
 B (γk−2)
B (γk−1)

0
 ×
 f0
f1

fk−1

fk−2

fk−3

fk−4
 −a0,k−1
−a0,k−2

−a0,3
−a0,2
−a0,1
−a0,0

Figure 16.10: The system of linear equations with the variables f0, . . . , fk−1 forming the coefﬁ-
cients of the polynomial f (X ) = ∑k−1
i =0 fi X i that we want to output. The constants a j ,0 are ob-
tained from the interpolating polynomial from Step 1. B (X ) is a non-zero polynomial of degree
at most s − 1.

Next, we present the argument above in full detail. (Note that the constraint on (16.8) is the
same as the one in (16.6) because of the constraint on the structure of Q imposed by Step 1.)

Lemma 16.3.4. There are at most q s−1 solutions to f0, f1, .., fk−1 (where f (X ) = f0 + f1X + ... +
fk−1X k−1) to the equations

A0(X ) + A1(X ) f (X ) + A2(X ) f (
γX ) + ... + As(X ) f (
γs−1X ) ≡ 0 (16.8)

Proof. First we assume that X does not divide all of the polynomials A0, A1, ..., As. Then it im-
plies that there exists i ∗ > 0 such that the constant term of the polynomial Ai ∗(X ) is not zero.
(Because otherwise, since X |A1(X ), ..., As(X ), by (16.8), we have X divides A0(X ) and hence X
divide all the Ai (X ) polynomials, which contradicts the assumption.)
To facilitate the proof, we deﬁne few auxiliary variables ai j such that

Ai (X ) = D+k−1∑

j =0 ai j X j for every 0 ≤ i ≤ s,

and deﬁne the following univariate polynomial:

B (X ) = a1,0 + a2,0X + a3,0X 2 + ... + as,0X s−1. (16.9)

283

Notice that ai ∗,0 ̸= 0, so B (X ) is non-zero polynomial. And because degree of B (X ) is at most
s − 1, by the degree mantra (Proposition 5.2.3), B (X ) has at most s − 1 roots. Next, we claim the
following:

Claim 16.3.5. For every 0 ≤ j ≤ k − 1:

• If B (γ j ) ̸= 0, then f j is uniquely determined by f j −1, f j −2, . . . , f0.

• If B (γ j ) = 0, then f j is unconstrained, i.e. f j can take any of the q values in Fq .

We defer the proof of the claim above for now. Suppose that the above claim is correct. Then
as γ is a generator of Fq , 1, γ, γ
2, ..., γ
k−1 are distinct (since k − 1 ≤ q − 2). Further, by the degree
mantra (Proposition 5.2.3) at most s − 1 of these elements are roots of the polynomial B (X ).
Therefore by Claim 16.3.5, the number of solutions to f0, f1, ..., fk−1 is at most q s−1. 2

We are almost done except we need to remove our earlier assumption that X does not divide
every Ai . Towards this end, we essentially just factor out the largest common power of X from
all of the Ai ’s, and proceed with the reduced polynomial. Let l ≥ 0 be the largest l such that
Ai (X ) = X l A′
i (X ) for 0 ≤ i ≤ s; then X does not divide all of A′
i (X ) and we have:

X l (A′
0(X ) + A′
1(X ) f (X ) + · · · + A′
s(X ) f (γs−1X )) ≡ 0.

Thus we can do the entire argument above by replacing Ai (X ) with A′
i (X ) since the above con-
straint implies that A′
i (X )’s also satisfy (16.8).

Next we prove Claim 16.3.5.

Proof of Claim 16.3.5. Recall that we can assume that X does not divide all of {A0(X ), . . . , As(X )}.
Let C (X ) = A0(X )+ A1(X ) f (X )+· · ·+ As f (
γs−1X )
. Recall that we have C (X ) ≡ 0. If we expand
out each polynomial multiplication, we have:

C (X ) =a0,0 + a0,1X + · · · + a0,D+k−1X D+k−1

+ (a1,0 + a1,1X + · · · + a1,D+k−1X D+k−1) ( f0 + f1X + f2X 2 + · · · + fk−1X k−1)

+ (a2,0 + a2,1X + · · · + a2,D+k−1X D+k−1) ( f0 + f1γX + f2γ
2X 2 + · · · + fk−1γ
k−1X k−1)

...

+ (as,0 + as,1X + · · · + as,D+k−1X D+k−1) ( f0 + f1γs−1X + f2γ
2(s−1)X 2 + · · · + fk−1γ
(k−1)(s−1)X k−1)

(16.10)

Now if we collect terms of the same degree, we will have a polynomial of the form:

C (X ) = c0 + c1X + c2X 2 + · · · + cD+k−1X D+k−1.

2Build a “decision tree" with f0 as the root and f j in the j th level: each edge is labeled by the assigned value to
the parent node variable. For any internal node in the j th level, if B (γ j ) ̸= 0, then the node has a single child with
the edge taking the unique value promised by Claim 16.3.5. Otherwise the node has q children with q different
labels from Fq . By Claim 16.3.5, the number of solutions to f (X ) is upper bounded by the number of nodes in the
kth level in the decision tree, which by the fact that B has at most s − 1 roots is upper bounded by q s−1.

284

So we have D +k linear equations in variables f0, . . . , fk−1, and we are seeking those solutions
such that c j = 0 for every 0 ≤ j ≤ D + k − 1. We will only consider the 0 ≤ j ≤ k − 1 equations. We

ﬁrst look at the equation for j = 0: c0 = 0. This implies the following equalities:

0 = a0,0 + f0a1,0 + f0a2,0 + · · · + f0as,0 (16.11)

0 = a0,0 + f0 (a1,0 + a2,0 + · · · + as,0) (16.12)

0 = a0,0 + f0B (1). (16.13)

In the above (16.11) follows from (16.10), (16.12) follows by simple manipulation while (16.13)
follows from the deﬁnition of B (X ) in (16.9).
Now, we have two possible cases:

• Case 1: B (1) ̸= 0. In this case, (16.13) implies that f0 = −a0,0
B (1) . In particular, f0 is ﬁxed.

• Case 2: B (1) = 0. In this case f0 has no constraint (and hence can take on any of the q
values in Fq ).

Now consider the equation for j = 1: c1 = 0. Using the same argument as we did for j = 0,
we obtain the following sequence of equalities:

0 = a0,1 + f1a1,0 + f0a1,1 + f1a2,0γ + f0a2,1 + · · · + f1as,0γs−1 + f0as,1

0 = a0,1 + f1 (a1,0 + a2,0γ + · · · + as,0γs−1) + f0
 ( s∑

l =1 al ,1
)

0 = a0,1 + f1B (γ) + f0b(1)
0 (16.14)

where b(1)
0 = ∑s
l =1 al ,1 is a constant. We have two possible cases:

• Case 1: B (γ) ̸= 0. In this case, by (16.14), we have f1 = −a0,1− f0b(1)
0
B (γ) and there is a unique
choice for f1 given ﬁxed f0.

• Case 2: B (γ) = 0. In this case, f1 is unconstrained.

Now consider the case of arbitrary j : c j = 0. Again using similar arguments as above, we get:

0 = a0, j + f j (a1,0 + a2,0γ j + a3,0γ
2 j + · · · + as,0γ j (s−1))

+ f j −1(a1,1 + a2,1γ j −1 + a3,1γ
2( j −1) + · · · + as,1γ
( j −1)(s−1))
...

+ f1(a1, j −1 + a2, j −1γ + a3, j −1γ
2 + · · · + as, j −1γs−1)

+ f0(a1, j + a2, j + a3, j + · · · + as, j )

0 = a0, j + f j B (γ j ) +
 j −1∑

l =0 fl b( j )
l (16.15)

where b( j )
l = ∑s
ι=1 aι, j −l · γ
l (ι−1) are constants for 0 ≤ j ≤ k − 1.
We have two possible cases:
 285

• Case 1: B (γ j ) ̸= 0. In this case, by (16.15), we have

f j = −a0, j − ∑ j −1
l =0 fl b( j )
l
B (γ j ) (16.16)

and there is a unique choice for f j given ﬁxed f0, . . . , f j −1.

• Case 2: B (γ j ) = 0. In this case f j is unconstrained.

This completes the proof.

We now revisit the proof above and make some algorithmic observations. First, we note that
to compute all the tuples ( f0, . . . , fk−1) that satisfy (16.8) one needs to solve the linear equations
(16.15) for j = 0, . . . , k − 1. One can state this system of linear equation as (see also Figure 16.10)

C ·
 



 f0
...
fk−1
 


 =
 



 −a0,k−1
...
−a0,0
 


 ,

where C is a k × k upper triangular matrix. Further each entry in C is either a 0 or B (γ j ) or b( j )
l –
each of which can be computed in O(s log s) operations over Fq . Thus, we can setup this system
of equations in O (s log sk 2) operations over Fq .
Next, we make the observation that all the solutions to (16.8) form an afﬁne subspace. Let
0 ≤ d ≤ s − 1 denote the number of roots of B (X ) in {1, γ, . . . , γ
k−1}. Then since there will be
d unconstrained variables among f0, . . . , fk−1 (one of every j such that B (γ j ) = 0), it is not too

hard to see that all the solutions will be in the set {M · x + z|x ∈ Fd
q }, for some k ×d matrix M and

some z ∈ Fk
q . Indeed every x ∈ Fd
q corresponds to an assignment to the d unconstrained variables
among f0, . . . , f j . The matrix M and the vector z are determined by the equations in (16.16).
Further, since C is upper triangular, both M and z can be computed with O (k 2) operations over
Fq . The discussion above implies the following:

Corollary 16.3.6. The set of solutions to (16.8) are contained in an afﬁne subspace {M · x + z|x ∈ Fd
q }

for some 0 ≤ d ≤ s −1 and M ∈ Fk×d
q and z ∈ Fk
q . Further, M and z can be computed from the poly-
nomials A0(X ), . . . , As(X ) with O(s log sk 2) operations over Fq .

16.3.3 Algorithm Implementation and Runtime Analysis

In this sub-section, we discuss how both the interpolation and root ﬁnding steps of the algo-
rithm can be implemented and analyze the run time of each step.
Step 1 involves solving N m linear equation in O(N m) variables and can e.g. be solved by
Gaussian elimination in O((N m)3) operations over Fq . This is similar to what we have seen for
Algorithms 22, 23 and 24. However, the fact that the interpolation polynomial has total degree

286

of one in the variables Y1, . . . , Ys implies a much faster algorithm. In particular, one can perform
the interpolation in O(N m log
2(N m) log log(N m)) operations over Fq .
The root ﬁnding step involves computing all the “roots" of Q. The proof of Lemma 16.3.4
actually suggests Algorithm 28.

Algorithm 28 The Root Finding Algorithm for Algorithm 27
INPUT: A0(X ), . . . , As(X )
OUTPUT: All polynomials f (X ) of degree at most k − 1 that satisfy (16.8)

1: Compute ℓ such that X ℓ is the largest common power of X among A0(X ), . . . , As(X ).

2: FOR every 0 ≤ i ≤ s DO

3: Ai (X ) ← Ai (X )
X ℓ .

4: Compute B (X ) according to (16.9)

5: Compute d , z and M such that the solutions to the k linear system of equations in (16.15)

lie in the set {M · x + z|x ∈ Fd
q }.

6: L ← ;

7: FOR every x ∈ Fd
q DO

8: ( f0, . . . , fk−1) ← M · x + z.

9: f (X ) ← ∑k−1
i =0 fi · X i .

10: IF f (X ) satisﬁes (16.8) THEN

11: Add f (X ) to L.

12: RETURN L

Next, we analyze the run time of the algorithm. Throughout, we will assume that all polyno-
mials are represented in their standard coefﬁcient form.
Step 1 just involves ﬁguring out the smallest power of X in each Ai (X ) that has a non-zero
coefﬁcient from which one can compute the value of ℓ. This can be done with O(D + k + s(D +
1)) = O(N m) operations over Fq . Further, given the value of ℓ one just needs to “shift" all the
coefﬁcients in each of the Ai (X )’s to the right by ℓ, which again can be done with O(N m) oper-
ations over Fq .
Now we move to the root ﬁnding step. The run time actually depends on what it means to
“solve" the linear system. If one is happy with a succinct description of a set of possible solution
that contains the actual output then one can halt Algorithm 28 after Step 5 and Corollary 16.3.6
implies that this step can be implemented in O (s log sk 2) = O (s log s(N m)2) operations over
Fq . However, if one wants the actual set of polynomials that need to be output, then the only
known option so far is to check all the q s−1 potential solutions as in Steps 7-11. (However, we’ll
see a twist in Section 16.4.) The latter would imply a total of O(s log s(N m)2) + O(q s−1 · (N m)2)
operations over Fq .
Thus, we have the following result:

Lemma 16.3.7. With O(s log s(N m)2) operations over Fq , the algorithm above can return an
afﬁne subspace of dimension s − 1 that contains all the polynomials of degree at most k − 1

287

that need to be output. Further, the exact set of solution can be computed in with additional
O(q s−1 · (N m)2) operations over Fq .

16.3.4 Wrapping Up

By Theorem 16.3.3, we know that we can list decode a folded Reed-Solomon code with folding
parameter m ≥ 1 up to s
s + 1 · (1 − m
m − s + 1 · R) (16.17)

fraction of errors for any 1 ≤ s ≤ m.
To obtain our desired bound 1 − R − ε fraction of errors, we instantiate the parameter s and
m such that s
s + 1 ≥ 1 − ε and m
m − s + 1 ≤ 1 + ε. (16.18)

It is easy to check that one can choose

s = Θ(1/ε) and m = Θ(1/ε2)

such that the bounds in (16.18) are satisﬁed. Using the bounds from (16.18) in (16.17) implies
that the algorithm can handle at least

(1 − ε)(1 − (1 + ε)R) = 1 − ε − R + ε2R > 1 − R − ε

fraction of errors, as desired.
We are almost done since Lemma 16.3.7 shows that the run time of the algorithm is qO(s).
The only thing we need to choose is q: for the ﬁnal result we pick q to be the smallest power
of 2 that is larger than N m + 1. Then the discussion above along with Lemma 16.3.7 implies
the following result (the claim on strong explicitness follows from the fact that Reed-Solomon
codes are strongly explicit):

Theorem 16.3.8. There exist strongly explicit folded Reed-Solomon codes of rate R that for large
enough block length N can be list decoded from 1 − R − ε fraction of errors (for any small enough

ε > 0) in time ( N
ε )O(1/ε). The worst-case list size is ( N
ε )O(1/ε) and the alphabet size is ( N
ε )O(1/ε2).

16.4 Bibliographic Notes and Discussion

There was no improvement to the Guruswami-Sudan result (Theorem 15.2.6) for about seven
years till Parvaresh and Vardy showed that “Correlated" Reed-Solomon codes can be list-decoded
up to 1−(mR) 1
m+1 fraction of errors for m ≥ 1 [77]. Note that for m = 1, correlated Reed-Solomon
codes are equivalent to Reed-Solomon codes and the result of Parvaresh and Vardy recovers
Theorem 15.2.6. Immediately, after that Guruswami and Rudra [44] showed that Folded Reed-
Solomon codes can achieve the list-decoding capacity of 1 − R − ε and hence, answer Ques-
tion 16.0.1 in the afﬁrmative. Guruswami [39] reproved this result but with a much simpler

288

proof. In this chapter, we studied the proof due to Guruswami. Guruswami in [39] credits
Salil Vadhan for the the interpolation step. An algorithm presented in Brander’s thesis [10]
shows that for the special interpolation in Algorithm 27, one can perform the interpolation in
O(N m log
2(N m) log log(N m)) operations over Fq . The idea of using the “sliding window" for list
decoding Folded Reed-Solomon codes is originally due to Guruswami and Rudra [43].
The bound of q s−1 on the list size for folded Reed-Solomon codes was ﬁrst proven in [43] by
roughly the following argument. One reduced the problem of ﬁnding roots to ﬁnding roots of a
univariate polynomial related to Q over Fq k . (Note that each polynomial in Fq [X ] of degree at
most k −1 has a one to one correspondence with elements of Fq k – see e.g. Theorem 12.2.1.) The
list size bound follows from the fact that this new univariate polynomial had degree q s−1. Thus,
implementing the algorithm entails running a root ﬁnding algorithm over a big extension ﬁeld,
which in practice has terrible performance.

Discussion. For constant ε, Theorem 16.3.8 answers Question 16.0.1 in the afﬁrmative. How-
ever, from a practical point of view, there are three issues with the result: alphabet, list size and
run time. Below we tackle each of these issues.

Large Alphabet. Recall that one only needs an alphabet of size 2
O(1/ε) to be able to list de-
code from 1 − R − ε fraction of errors, which is independent of N . It turns out that combining
Theorem 16.3.8 along with code concatenation and expanders allows us to construct codes over
alphabets of size roughly 2
O(1/ε4) [43]. (The idea of using expanders and code concatenation was
not new to [43]: the connection was exploited in earlier work by Guruswami and Indyk [42].)
The above however, does not answer the question of achieving list decoding capacity for
ﬁxed q, say e.g. q = 2. We know that there exists binary code of rate R that are (H −1(1 − R −
ε),O(1/ε))-list decodable codes (see Theorem 7.4.1). The best known explicit codes with efﬁ-
cient list decoding algorithms are those achieved by concatenating folded Reed-Solomon codes
with suitable inner codes achieve the so called Blokh-Zyablov bound [45]. However, the tradeoff
is far from the list decoding capacity. As one sample point, consider the case when we want to
list decode from 1
2 − ε fraction of errors. Then the result of [45] gives codes of rate Θ(ε3) while
the codes on list decoding capacity has rate Ω(ε2). The following fundamental question is still
very much wide open:

Open Question 16.4.1. Do there exist explicit binary codes with rate R that can be list de-
coded from H −1(1 − R − ε) fraction of errors with polynomial list decoding algorithms?

The above question is open even if we drop the requirement on efﬁcient list decoding al-
gorithm or we only ask for a code that can list decode from 1/2 − ε fraction of errors with rate
Ω(εa) for some a < 3. It is known (combinatorially) that concatenated codes can achieve the list
decoding capacity but the result is via a souped up random coding argument and does not give
much information about an efﬁcient decoding algorithm [46].

289

List Size. It is natural to wonder if the bound on the list size in Lemma 16.3.4 above can be
improved as that would show that folded Reed-Solomon codes can be list decoded up to the list
decoding capacity but with a smaller output list size than Theorem 16.3.8. Guruswami showed
that in its full generality the bound cannot be improved [39]. In particular, he exhibits explicit
polynomials A0(X ), . . . , As(X ) such that there are at least q s−2 solutions for f (X ) that satisfy
(16.8). However, these Ai (X )’s are not known to be the output for an actual interpolation in-
stance. In other words, the following question is still open:

Open Question 16.4.2. Can folded Reed-Solomon codes of rate R be list decoded from 1 −
R −ε fraction of errors with list size f (1/ε)·N c for some increasing function f (·) and absolute
constant c?

Even the question above with N (1/ε)o(1) is still open.
However, if one is willing to consider codes other than folded Reed-Solomon codes in or-
der to answer to achieve list decoding capacity with smaller list size (perhaps with one only
dependent on ε), then there is good news. Guruswami in the same paper that presented the
algorithm in this chapter also present a randomized construction of codes of rate R that are
(1 − R − ε,O(1/ε2))-list decodable codes [39]. This is of course worse than what we know from
the probabilistic method. However, the good thing about the construction of Guruswami comes
with an O(N /ε)
O(1/ε)-list decoding algorithm.
Next we brieﬂy mention the key ingredient in the result above. To see the potential for im-
provement consider Corollary 16.3.6. The main observation is that all the potential solutions
lie in an afﬁne subspace of dimension s − 1. The key idea in [39] was use the folded Reed-
Solomon encoding for a special subset of the message space Fk
q . Call a subspace S ⊆ Fk
q to be a
(q, k, ε, ℓ, L)-subspace evasive subset if

1. |S| ≥ q k(1−ε); and

2. For any (afﬁne) subspace T ⊆ Fk
q of dimension ℓ, we have |S ∩ T | ≤ L.

The code in [39], applies the folded Reed-Solomon encoding on a (q, k, s,O (s2))
-subspace eva-
sive subset (such a subset can be shown to exist via the probabilistic method). The reason why
this sub-code of folded Reed-Solomon code works is as follows: Condition (1) ensures that the
new code has rate at least R(1−ε), where R is the rate of the original folded Reed-Solomon code
and condition (2) ensures that the number of output polynomial in the root ﬁnding step of the
algorithm we considered in the last section is at most L. (This is because by Corollary 16.3.6 the
output message space is an afﬁne subspace of dimension s − 1 in Fk
Q . However, in the new code

by condition 2, there can be at most O (s2) output solutions.)
The result above however, has two shortcomings: (i) the code is no longer explicit and (ii)

even though the worst case list size is O ( 1
ε2 )
, it was not know how to obtain this output without

listing all the q s−1 possibilities and pruning them against S. The latter meant that the decoding
runtime did not improve over the one achieved in Theorem 16.3.8.

290

Large Runtime. We ﬁnally address the question of the high run time of all the list decoding
algorithms so far. Dvir and Lovett [25], presented a construction of an explicit (q, k, ε, s, sO(s))-
subspace evasive subset S∗. More interestingly, given any afﬁne subspace T of dimension at
most s, it can compute S ∩T in time proportional to the output size. Thus, this result along with
the discussion above implies the following result:

Theorem 16.4.1. There exist strongly explicit codes of rate R that for large enough block length N

can be list decoded from 1−R −ε fraction of errors (for any small enough ε > 0) in time O (( N
ε2 )2)+
( 1
ε )O(1/ε). The worst-case list size is ( 1
ε )O(1/ε) and the alphabet size is ( N
ε )O(1/ε2).

The above answers Question 16.0.1 pretty satisfactorily. However, to obtain a completely
satisfactory answer one would have to solve the following open question:

Open Question 16.4.3. Are there explicit codes of rate R > 0 that are (1 − R − ε, (1/ε)
O(1))
-list
decodable that can be list-decoded in time poly(N , 1/ε) over alphabet of size q ≤ pol y(n)?

The above question, without the requirement of explicitness, has been answered by Gu-
ruswami and Xing [51].
 291292

Part V

The Applications

293

Chapter 17

Cutting Data Down to Size: Hashing

In this chapter, we will study hashing, which is a method to compute a small digest of data
that can be used as a surrogate to later perform quick checks on the data. We begin with brief
descriptions of three practical applications where hashing is useful. We then formally state
the deﬁnition of hash functions that are needed in these applications (the so called “universal"
hash functions). Next, we will show how in some sense good hashing functions and good codes
are equivalent. Finally, we will see how hashing can solve a problem motivated by outsourced
storage in the “cloud."

17.1 Why Should You Care About Hashing?

Hashing is one of the most widely used objects in computer science. In this section, we outline
three practical applications that heavily use hashing. While describing the applications, we will
also highlight the properties of hash functions that these applications need.
Before we delve into the applications, let us ﬁrst formally deﬁne a hash function.

Deﬁnition 17.1.1 (Hash Function). Given a domain D and a range Σ, (typically, with |Σ| < |D|),
a hash function is a map h : D → Σ.

Of course, the deﬁnition above is too general and we will later specify properties that will
make the deﬁnition more interesting.

Integrity Checks on Routers. Routers on the Internet process a lot of packets in a very small
amount of time. Among other tasks, router has to perform an “integrity check" on the packet
to make sure that the packet it is processing is not corrupted. Since the packet has well deﬁned
ﬁelds, the router could check if all the ﬁeld have valid entries. However, it is possible that one of
the valid entry could be turned into another valid entry. However, the packet as a whole could
still be invalid.
If you have progressed so far in the book, you will recognize that the above is the error detec-
tion problem and we know how to do error detection (see e.g., Proposition 2.3.3). However, the

295

algorithms that we have seen in this book are too slow to implement in routers. Hence, Internet
protocols use a hash function on a domain D that encodes all the information that needs to go
into a packet. Thus, given an x ∈ D, the packet is the pair (x, h(x)). The sender sends the packet
(x, h(x)) and the receiver gets (x′, y). In order to check if any errors occurred during transmis-
sion, the receiver checks if h(x′) = y. If the check fails, the receiver asks for a re-transmission
otherwise it assumes there were no errors during transmission. There are two requirements
from the hash function: (i) It should be super efﬁcient to compute h(x) given x and (ii) h should
avoid “collisions," i.e. if x ̸= x′, then h(x) ̸= h(x′).1

Integrity Checks in Cloud Storage. Say, you (as a client) have data x ∈ D that you want to
outsource x to a cloud storage provider. Of course once you “ship" off x to the cloud, you do not
want to store it locally. However, you do not quite trust the cloud either. If you do not audit the
cloud storage server in any way, then nothing stops the storage provider from throwing away
x and send you some other data x′ when you ask for x. The problem of designing an auditing
protocol that can verify whether the server has the data x is called the data possession problem.
We consider two scenarios. In the ﬁrst scenario, you access the data pretty frequently during
“normal" operation. In such cases, here is a simple check you can perform. When you ship off
x to the cloud, compute z = h(x) and store it. Later when you access x and the storage provider
send you x′, you compute h(x′) and check if it is the same as the stored h(x). This is exactly the
same solution as the one for packet veriﬁcation mentioned above.
Now consider the scenario, where the cloud is used as an archival storage. In such a case,
one needs an “auditing" process to ensure that the server is indeed storing x (or is storing some
massaged version from which it can compute x– e.g. the storage provider can compress x). One
can always ask the storage provider to send back x and then use the scheme above. However,
if x is meant to be archived in the cloud, it would be better to resolve the following question:

Question 17.1.1. Is there an auditing protocol with small client-server communication
a,
which if the server passes then the client should be able to certain (with some high conﬁdence)
that the server is indeed storing x?

aIn particular, we rule out solutions where the server sends x to the client.

We will see later how this problem can be solved using hashing.

Fast Table Lookup. One of the most common operations on databases is the following. As-
sume there is a table with entries from D. One would like to decide on a data structure to store

1Note that in the above example, one could have x ̸= x′ and h(x) ̸= h(x′) but it is still possible that y = h(x′) and
hence the corrupted packet (x′, y) would pass the check above. Our understanding is that such occurrences are
rare.
 296

the table so that later on given an element x ∈ D, one would quickly like to decide whether x is
in the table or now.
Let us formalize the problem a bit: assume that the table needs to store N values a1, . . . , aN ∈
D. Then later given x ∈ D one needs to decide if x = ai for some i . Here is one simple solution:
sort the n elements in an array T and given x ∈ D use binary search to check if x is in T or not.
This solution uses Θ(N ) amounts of storage and searching for x takes Θ(log N ) time. Further,
the pre-processing time (i.e. time taken to build the array T ) is Θ(N log N ). The space usage of
this scheme is of course optimal but one would like the lookup to be faster: ideally we should
be able to perform the search in O(1) time. Also it would be nice to get the pre-processing time
closer to the optimal O(N ). Further, this scheme is very bad for dynamic data: inserting an item
to and deleting an item from T takes Θ(N ) time in the worst-case.
Now consider the following solution: build a boolean array B with one entry for each z ∈ D
and set B [ai ] = 1 for every i ∈ [N ] (and every other entry is 0).2 Then searching for x is easy: just
lookup B [x] and check if B [x] ̸= 0. Further, this data structure can easily handle addition and
deletion of elements (by incrementing and decrementing the corresponding entry of B respec-
tively). However, the amount of storage and pre-processing time are both Θ (|D|), which can be
much much bigger than the optimal O(N ). This is deﬁnitely true for tables stored in real life
databases. This leads to the following question:

Question 17.1.2. Is there a data structure that supports searching, insertion and deletion in
O(1) time but only needs O(N ) space and O(N ) pre-processing time?

We will see later how to solve this problem with hashing.

17.2 Avoiding Hash Collisions

One of the properties that we needed in the applications outlined in the previous section was
that the hash function h : D → Σ should avoid collisions. That is, given x ̸= y ∈ D, we want
h(x) ̸= h(y). However, since we have assumed that |Σ| < |D|, this is clearly impossible. A simple
counting argument shows that there will exist an x ̸= y ∈ D such that h(x) = h(y). There are two
ways to overcome this hurdle.
The ﬁrst is to deﬁne a cryptographic collision resistant hash function h, i.e. even though
there exists collisions for the hash function h, it is computationally hard for an adversary to
compute x ̸= y such that h(x) = h(y).3 This approach is out of the scope of this book and hence,
we will not pursue this solution.

2If one wants to handle duplicates, one could store the number of occurrences of y in B [y].
3This is a very informal deﬁnition. Typically, an adversary is modeled as a randomized polynomial time algo-
rithm and there are different variants on whether the adversary is given h(x) or x (or both). Also there are variants
where one assumes a distribution on x. Finally, there are no unconditionally collision resistant hash function but
there exists provably collision resistant hash function under standard cryptographic assumptions: e.g. factoring is
hard.
 297

The second workaround is to deﬁne a family of hash functions and then argue that the prob-
ability of collision is small for a hash function chosen randomly from the family. More formally,
we deﬁne a hash family:

Deﬁnition 17.2.1 (Hash Family). Given D, Σ and an integer m ≥ 1, a hash family H is a set
{h1, . . . , hm} such that for each i ∈ [m], hi : D → Σ.

Next we deﬁne the notion of (almost) universal hash function (family).

Deﬁnition 17.2.2 (Almost Universal Hash Family). A hash family H = {h1, . . . , hm} deﬁned over
the domain D and range Σ is said to be ε-almost universal hash function (family) for some 0 <
ε ≤ 1 if for every x ̸= y ∈ D, Pr
i
 [
hi (x) = hi (y)] ≤ ε,

where in the above i is chosen uniformly at random from [m].

We will show in the next section that ε-almost universal hash functions are equivalent to
codes with (large enough) distance. In the rest of the section, we outline how these hash families
provides satisfactory solutions to the problems considered in the previous section.

Integrity Checks. For the integrity check problem, one pick random i ∈ [m] and chooses hi ∈
H , where H is an ε-almost universal hash function. Thus, for any x ̸= y, we’re guaranteed
with probability at least 1 − ε (over the random choice of i ) that hi (x) ̸= hi (y). Thus, this gives a
randomized solution to the integrity checking problem in routers and cloud storage (where we
consider the ﬁrst scenario in which the cloud is asked to return the original data in its entirety).
It is not clear whether such hash functions can present a protocol that answers Question 17.1.1.
There is a very natural protocol to consider though. When the client ships off data x to the cloud,
it picks a random hash function hi ∈ H , where again H is an ε-universal hash function, and
computes hi (x). Then it stores hi (x) and ships off x to the cloud. Later on, when the client wants
to audit, it asks the cloud to send hi (x) back to it. Then if the cloud returns with z, the client
checks if z = hi (x). If so, it assumes that the storage provider is indeed storing x and otherwise
it concludes that the cloud is not storing x.
Note that it is crucial that the hash function be chosen randomly: if the client picks a de-
terministic hash function h, then the cloud can store h(x) and throw away x because it knows
that the client is only going to ask for h(x). Intuitively, the above protocol might work since the
random index i ∈ [m] is not known to the cloud till the client asks for hi (x), it seems “unlikely"
that the cloud can compute hi (x) without storing x. We will see later how the coding view of
almost universal hash functions can make this intuition rigorous.

Fast Table Lookup. We now return to Question 17.1.2. The basic idea is simple: we will mod-
ify the earlier solution that maintained an entry for each element in the domain D. The new
solution will be to keep an entry for all possible hash values (instead of all entries in D).

298

More formally, let H = {h1, . . . , hm} be an ε-almost hash family with domain D and range
Σ. Next we build an array of link list with one entry in the array for each value v ∈ Σ. We pick a
random hash function hi ∈ H . Then for each a j ( j ∈ [N ]) we add it to the link list corresponding
to hi (a j ). Now to determine whether x = a j for some j , we scan the link list corresponding to
hi (x) and check if x is in the list or not. Before we analyze the space and time complexity of
this data structure, we point out that insertion and deletion are fairly easy. For inserting an
element x, we compute hi (x) and add x to the link list corresponding to hi (x). For deletion, we
ﬁrst perform the search algorithm and then remove x from the list corresponding to hi (x), if it
is present. It is easy to check that the algorithms are correct.
Next we analyze the space complexity. Note that for a table with N elements, we will use
up O(N ) space in the linked lists and the array is of size O(|Σ|). That is, the total space usage is
O(N + |Σ|). Thus, if we can pick |Σ| = O(N ), then we would match the optimal O(N ) bound for
space.
Now we analyze the time complexity of the various operations. We ﬁrst note that insertion is
O(1) time (assuming computing the hash value takes O(1) time). Note that this also implies that
the pre-processing time is O(N + |Σ|), which matches the optimal O(N ) bound for |Σ| ≤ O(N ).
Second, for deletion, the time taken after performing the search algorithm is O(1), assuming
the lists as stored as doubly linked lists. (Recall that deleting an item from a doubly linked list if
one has a pointer to the entry can be done in O(1) time.)
Finally, we consider the search algorithm. Again assuming that computing a hash value
takes O(1) time, the time complexity of the algorithm to search for x is dominated by size of the
list corresponding to hi (x). In other words, the time complexity is determined by the number
of a j that collide with x, i.e., hi (x) = hi (a j ). We bound this size by the following simple observa-
tion.

Claim 17.2.1. Let H = {h1, . . . , hm} with domain D and range Σ be an ε-almost universal hash
family. Then the following is true for any (distinct) x, a1, a2, . . . , aN ∈ D:

Ei [
|{a j |hi (x) = hi (a j )}|] ≤ ε · N ,

where the expectation is taken over a uniformly random choice of i ∈ [m].

Proof. Fix a j ∈ [N ]. Then by deﬁnition of an ε-almost universal hash family, we have that

Pr
i [hi (x) = hi (a j )] ≤ ε.

Note that we want to bound E [∑N
j =1 1hi (a j )=hi (x)]. The probability bound above along with the
linearity of expectation (Proposition 3.1.2) and Lemma 3.1.1 completes the proof.

The above discussion then implies the following:

Proposition 17.2.2. Given an O ( 1
N )
-almost universal hash family with domain D and range Σ
such that |Σ| = O(N ), there exists a randomized data structure that given N elements a1, . . . , aN ∈
D, supports searching, insertion and deletion in expected O(1) time while using O(N ) space in the
worst-case.
 299

Thus, Proposition 17.2.2 answers Question 17.1.2 in the afﬁrmative if we can answer the
following question in the afﬁrmative:

Question 17.2.1. Given a domain D and an integer N ≥ 1, does there exist an O ( 1
N )
-almost
universal hash function with domain D and a range Σ such that |Σ| = O(N )?

We will answer the question above (spoiler alert!) in the afﬁrmative in the next section.

17.3 Almost Universal Hash Function Families and Codes

In this section, we will present a very strong connection between almost universal hash families
and codes with good distance: in fact, we will show that they are in fact equivalent.
We ﬁrst begin by noting that any hash family has a very natural code associated with it and
that every code has a very natural hash family associated with it.

Deﬁnition 17.3.1. Given a hash family H = {h1, . . . , hn} where for each i ∈ [n], hi : D → Σ, con-
sider the following associated code CH : D → Σn,

where for any x ∈ D, we have
 CH (x) = (h1(x), h2(x), . . . , hn(x)) .

The connection also goes the other way. That is, given an (n, k)Σ code C , we call the associated
hash family HC = {h1, . . . , hn), where for every i ∈ [n],

hi : Σk → Σ

such that for every x ∈ Σk and i ∈ [n],
 hi (x) = C (x)i .

Next we show that an ε-almost universal hash family is equivalent to a code with good dis-
tance.

Proposition 17.3.1. Let H = {h1, . . . , hn} be an ε-almost universal hash function, then the code
CH has distance at least (1 − ε)n. On the other hand if C is an (n, k, δn)-code, then HC is a
(1 − δ)-almost universal hash function.

Proof. We will only prove the ﬁrst claim. The proof of the second claim is essentially identical
and is left as an exercise.
Let H = {h1, . . . , hn} be an ε-almost universal hash function. Now ﬁx arbitrary x ̸= y ∈ D.
Then by deﬁnition of CH , we have

{i |hi (x) = hi (y)} = {i |CH (x)i = CH (y)i }.

300

This implies that

Pr
i
 [hi (x) = hi (y)] = |{i |hi (x) = hi (y)}|
n = n − ∆(CH (x),CH (y))
n = 1 − ∆(CH (x),CH (y))
n ,

where the second equality follows from the deﬁnition of the Hamming distance. By the deﬁ-
nition of ε-almost universal hash family the above probability is upper bounded by ε, which
implies that ∆(CH (x),CH (y)) ≥ n(1 − ε).

Since the choice of x and y was arbitrary, this implies that CH has distance at least n(1 − ε) as
desired.

17.3.1 The Polynomial Hash Function

We now consider the hash family corresponding to a Reed-Solomon code. In particular, let C
be a [q, k, q − k + 1]q Reed-Solomon code. By Proposition 17.3.1, the hash family HC is an k−1
q -
almost universal hash family– this hash family in the literature is called the polynomial hash.
Thus, if we pick q to be the smallest power of 2 larger than N and pick k = O(1), then this leads
to an O(1/N )-universal hash family that satisﬁes all the required properties in Question 17.2.1.
Note that the above implies that |D| = N O(1). One might wonder if we can get an O(1/N )-
almost universal hash family with the domain size being N ω(1). We leave the resolution of this
question as an exercise.

17.4 Data Possession Problem

In this section, we return to Question 17.1.1. Next we formalize the protocol for the data pos-
session problem that we outlined in Section 17.2. Algorithm 29 presents the pre-processing
step.

Algorithm 29 Pre-Processing for Data Possession Veriﬁcation
INPUT: Data x ∈ D, hash family H = {h1, . . . , hm} over domain D

1: Client computes an index i for x.

2: Client picks a random j ∈ [m].

3: Client computes z ← h j (x) and stores (i , j , z).

4: Client sends x to the server.

Algorithm 30 formally states the veriﬁcation protocol. Note that if the server has stored x
(or is able to re-compute x from what it had stored), then it can pass the protocol by returning
a ← h j (x). Thus, for the remainder of the section, we will consider the case when the server
tries to cheat. We will show that if the server is able to pass the protocol in Algorithm 30 with
high enough probability, then the server indeed has stored x.

301

Algorithm 30 Veriﬁcation for Data Possession Veriﬁcation
INPUT: Index i of data x ∈ D
OUTPUT: 1 if Server has x and 0 otherwise

1: Client sends a challenge (i , j ) to the server.

2: Client receives an answer a.

3: IF a = z THEN

4: RETURN 1

5: ELSE

6: RETURN 0

Before we formally prove the result, we state our assumptions on what the server can and
cannot do. We assume that the server follows the following general protocol. First, when the
server receives x, it does performs some computation (that terminates) on x to produce y and
then it stores y. (E.g., the server could store y = x or y could be a compressed version of x.)
Then when it receives the challenge (i , j ) for x, it uses another algorithm A and returns the
answers a ← A (y, j ). We assume that A always terminates on any input.4 Note that the server
is allowed to use arbitrary (but ﬁnite) amount of time to compute its answer. Next, we will prove
that under these assumptions, the server cannot cheat with too high a probability.

Theorem 17.4.1. Assume that the hash family H is an ε-almost universal hash family. Then if
the server passes the protocol in Algorithm 30 with probability > 1
2 + ε
2 , then the server has enough
information to recreate x.

Proof. To prove the claim, we present an algorithm that can compute x from y. (Note that we do
not need this algorithm to be efﬁcient: it just needs to terminate with x.) In particular, consider
Algorithm 31.

Algorithm 31 Decompression Algorithm
INPUT: A , y
OUTPUT: x′

1: z ← (
A (y, j ))
 j ∈[m].

2: Run the MLD algorithm (Algorithm 2) for CH on z and let CH (x′) be its output.

3: RETURN x′

To complete the proof, we will show that x′ = x. Towards this end we claim that ∆(z,CH (x)) <
m
2 · (1 − ε). Assuming this is true, we complete the proof. Note that Proposition 17.3.1 implies
that CH has distance at least m(1 − ε). Thus, Proposition 1.4.1 (in particular, its proof) implies
that Algorithm 2 will return CH (x) and thus, x′ = x, as desired.

4We have stated the algorithm to be independent of y and j but that need not be the case. However later in the
section, we will need the assumption that A is independent of y and j , so we will keep it that way.

302

Finally, we argue that ∆(z,CH (x)) < m(1 − ε)/2. To see this note that if the server passes

the protocol in Algorithm 30 (i.e. the client outputs 1), then it has to be the case that z j def
=
A (y, j ) = h j (x). Recall that by deﬁnition of CH , h j (x) = CH (x) j and that the server passes the
protocol with probability > 1/2+ε/2. Since j is chosen uniformly from [m], this implies that for
> m(1/2 + ε/2) positions j , z j = CH (x) j , which then implies the claim.

17.4.1 Driving Down the Cheating Probability

One of the unsatisfying aspects of Theorem 17.4.1 is that the probability of catching a “cheating"
server is strictly less than 50%.5 It is of course desirable to drive this up as close to 100% as possi-
ble. One way to obtain this would be to “repeat" the protocol: i.e. the client can choose multiple
random hashes and store the corresponding values (in Algorithm 29) and (in Algorithm 30) asks
the server to send back all the hash values and accepts if and only if all the returned answers
match with the stored hash values. This however, comes at a cost: the client has to store more
hash values (and also the communication cost between the client and the server goes up ac-
cordingly.)
Next we argue using list decoding that the protocol in Algorithm 29 and 30 (without any
modiﬁcation) gives a more powerful guarantee than the one in Theorem 17.4.1. To see why list
decoding might buy us something, let us look back at Algorithm 31. In particular, consider Step
2: since we run MLD, we can only guarantee unique decoding up to half the (relative) distance
of CH . This in turn leads to the bound of 1/2 + ε/2 in Theorem 17.4.1. We have seen that list
decoding allows us to go beyond half the distance number of errors. So maybe, running a list
decoding algorithm instead of MLD in Step 2 of Algorithms 31 would help us get better results.
There are two potential issues that we’ll need to tackle:

• We will need a general bound that shows that list decoding (arbitrarily) close to 100% is
possible for any CH for an ε-almost universal hash family; and

• Even if the above is possible, what will we do when a list decoding algorithm returns a list
of possible data?

We will get around the ﬁrst concern by using the Johnson bound 7.3.1. To get around the second
issue we will indirectly use “side information" (like we mentioned in Section 7.2). For the latter,
we will need the notion of Kolmogorov complexity, which captures the amount of information
content in any given string. For our purposes, the following informal description is enough:

Deﬁnition 17.4.1. Given a string x, its Kolmogorov complexity, denoted by K (x) is the mini-
mum of |y|+|D|, where D is a decompression algorithm that on input y outputs x (where |x| and
|D| are the length of x and (a description of) D in bits).

Informally, K (x) is the amount of information that can be obtained algorithmically from x.
Kolmogorov complexity is a fascinating topic that it outside the scope of this book. Here we will

5Note that Theorem 17.4.1 states that a server that cannot recreate x can pass the test with probablity at most
1/2 + ε/2. In other words, the probability that such a server is caught is at most 1/2 − ε/2 < 1/2.

303

only need to use the deﬁnition of K (x). We are now ready to prove the following list decoding
counterpart of Theorem 17.4.1:

Theorem 17.4.2. Assume that the hash family H is an ε-almost universal hash family. Then if
the server passes the protocol in Algorithm 30 with probability > p
ε, then the amount of infor-
mation server has stored for x is at least K (x) − O(log |x|).

We note that the above is not a strict generalization of Theorem 17.4.1, as even though
probability of catching a cheating server has gone up our guarantee is weaker. Unlike Theo-
rem 17.4.1, where we can guarantee that the server can re-create x, here we can only guarantee
“storage enforceability"– i.e. we can only force a server to store close to K (x) amounts of mem-
ory.

Proof of Theorem 17.4.2. Here is the main idea of the proof. We ﬁrst assume for the sake of
contradiction that |y| < K (x)−O(log(|x|)). Then using we construct a decompression algorithm
D that on given input y and O(log(|x|)) extra information (or “advice"), outputs x. Then we will
show this overall contradicts the deﬁnition of K (x) (as this gives an overall smaller description
of x).
Before we state the decompression algorithm, we recall some facts. First note that CH by
Proposition 17.3.1 is a q-ary code (with |Σ| = q) with distance m(1 − ε). Further, by the Johnson
bound (Theorem 7.3.1), CH is a (1 − pε, L)-list decodable, where

L ≤ qm2. (17.1)

Next, in Algorithm 32, we present a decompression algorithm that can compute x from y
and an advice string a ∈ [L]. (As before, we do not need this algorithm to be efﬁcient: it just
needs to terminate with x.)

Algorithm 32 Decompression Algorithm Using List Decoding
INPUT: A , y, a
OUTPUT: x

1: z ← (
A (y, j ))
 j ∈[m].

2: L ← ;.

3: FOR x′ ∈ D DO

4: IF ∆(CH (x′), z) ≤ (1 − p
ε)m THEN

5: Add x′ to L

6: RETURN The ath element in L

To complete the proof, we claim that there exists a choice of a ∈ [L] such that Algorithm 32
outputs x. Note that this implies that (y, a) along with Algorithm 32 gives a complete description
of x. Now note that Algorithm 32 can be described in O(1) bits. This implies that the size of this
description is |y| + log L + O(1), which by Deﬁnition 17.4.1 has to be at least K (x). This implies
that |y| ≥ K (x) − |a| − O(1) = K (x) − log L − O(1) ≥ K (x) − O(log |x|),

304

where the last inequality follows from (17.1).
Next, we argue the existence of an appropriate a ∈ [L]. Towards this end we claim that
∆(z,CH (x)) < m(1 − p
ε). Note that this implies that x ∈ L . Since |L | ≤ L, then we can just
assign a to be the index of x in L . Finally, we argue that ∆(z,CH (x)) < m(1 − p
ε). To see this
note that if the server passes the protocol in Algorithm 30 (i.e. the client outputs 1), then it has

to be the case that z j def
= A (y, j ) = h j (x). Recall that by deﬁnition of CH , h j (x) = CH (x) j and
that the server passes the protocol with probability > pε. Since j is chosen uniformly from [m],
this implies that for > mp
ε positions j , z j = CH (x) j , which then implies the claim.

17.5 Bibliographic Notes

Universal hash functions were deﬁned in the seminal paper of Carter and Wegman [12]. Almost
universal hash function family was deﬁned by Stinson [95].
Kolmogorov complexity was deﬁned by Kolmogorov [63]. For a thorough treatment see the
textbook by Li and Vitányi [68].
 305306

Chapter 18

Securing Your Fingerprints: Fuzzy Vaults

String-based passwords are the dominant mode of authentication in today’s information-reliant
world. Indeed, all of us use passwords on a regular basis to authenticate ourselves in almost
any online activity. Strings, a primitive data type, have become widespread due to several nice
mathematical properties. First, matching two strings (that is, checking if two strings are exactly
the same) is computationally very fast (and easy). Second, and more importantly, there exist se-
cure hash functions that map a string x to another string h(x) such that, given h(x), determining
x is hard. Furthermore, since h(x) is itself a string, we can check if a claimed password y is the
same as the original string x by comparing h(y) and h(x), which (as we just observed) is easy to
do. This implies that the server performing the authentication only needs to store the hashes
h(x) of the original passwords. Hence, even if the list of hashed passwords were compromised,
the passwords themselves would remain secure.
The above scheme is perfect as long as the passwords x are “random enough," and this can
be achieved if the passwords were generated randomly by some automated process. However,
in real life passwords are generated by humans and are not really random. (One of the most
quoted facts is that the most commonly used password is the string “password" itself.) Further,
we tend to forget passwords, which has lead to the near ubiquity of “Forgot passwords" links in
places where we need to login.
One alternative that has been gaining traction in the last decade or so is to use a user’s ﬁnger-
print (and more generally their biometrics: e.g. their face) as their password. The big advantage
is that it is hard to “forget" one’s ﬁngerprint. In this chapter, we will look at the issues in using
ﬁngerprints as passwords and see how Reed-Solomon codes can help.

18.1 Some quick background on ﬁngerprints

First we give a very short (and necessarily incomplete) description of how a ﬁngerprint (im-
age/sensor reading) is converted in to a string f . The standard way to store a ﬁngerprint (see
Figure 18.1 for images of two ﬁngerprints) is as a collection of triples, called minutia. Each
minutia point is located where one ridge
1 splits into two, or where one ridge ends. The i th

1In Figure 18.1, the ridges are the lines.
 307

minutia is the triple (xi , yi , θi ), where xi and yi are the x and y coordinates of a point on the
ﬁnger, and θi indicates the direction of the ridge that created the minutia point relative to the
plane.
Given that we now have a string representation of a ﬁngerprint, we have the following naive
solution for designing a hash function for the ﬁngerprint f :

Naive Solution. Use any off-the-shelf hash function h for strings and then store h( f ) instead
of f .
To see the issues with the naive solution, we ﬁrst need to know a little bit about how ﬁnger-
prints are stored.
The main issue with our naive solution is that two ﬁngerprint readings will never be exactly
the same, even if the same ﬁnger is used. For any two ﬁngerprint readings, the following issues
may produce errors:

1. Translation and rotation, even when using the same ﬁnger.

2. Varying pressure.

3. Each reading may not completely overlap with the ideal ﬁngerprint region (i.e., the ﬁnger
may be slightly tilted).

4. The minutiae are not ordered, so they form a set instead of a vector. Of course one can
sort the set by the lexicographic order to produce a string. But the earlier issue (especially
points 1 and 2) imply that the speciﬁc values of (xi , yi , θi ) are not that important individu-
ally. Furthermore, the fact that any two readings might not have complete overlap means
that we are interested in matching readings that have signiﬁcant overlap, so it turns out
that the set notation is ideal to theoretically deal with these issues.

We can now see that the naive solution is inadequate. Even if we could somehow correct
the ﬁrst three issues, existing hash functions for strings require a vector, not a set, so our naive
solution will fail.

Remark 18.1.1. The four problems that came up in our naive solution will come up in any so-
lution we propose. Technology has not yet developed to the point where we can securely elimi-
nate these issues, which is why there are no prevalent secure commercial systems that safeguard
secrets using ﬁngerprints. (The reason government agencies, such as the police or FBI, use ﬁn-
gerprinting is because there is an inherent trust that the government will keep your data secure,
even when it does not apply a good hash function to it.)

Thus, we need secure hash functions designed to handle the additional challenges posed by
ﬁngerprints. We would like to mention that for ﬁngerprints to replace strings as passwords, the
hash function needs to satisfy both of these properties simultaneously: (i) we should be able to
match hashes from the “same" ﬁngerprint and (ii) an adversary should not be able to “break"
the hash function.
 308

Figure 18.1: The minutiae are unordered and form a set, not a vector.

18.2 The Fuzzy Vault Problem

We begin with the fuzzy vault problem, which is slightly different from the one we have been
studying so far. Say you have a secret string s, and you want to store it in a secure way. Instead
of using a password, you want to use your ﬁngerprint, f , to “lock" the secret s. You want the
locked version of your secret to have two properties:

1. You should be able to “unlock" the locked version of s

2. No one else should be able to “unlock" s

We claim that if we can solve the above problem, then we can solve the problem of designing a
secure hash function for ﬁngerprints. We leave the details as an exercise. (Hint: pick s at random
and then in addition to the locked version of s also store h(s), where h is an off-the-shelf secure
hash function for strings.)
We will now formalize the fuzzy vault problem.

18.2.1 Formal Problem Statement

The ﬁrst thing we need to do is quantize the measurements of the minutiae. We cannot be
inﬁnitely precise in our measurements anyways, so let us assume that all quantized minutiae,
(xi , yi , θi ), can be embedded into Fq for some large enough prime power q. Theoretically, this
can also help to correct the ﬁrst two issues from our naive solution. We could go through all
possible values in Fq to get rid of translation and rotation errors (e.g., for every (∆x, ∆y, ∆z) ∈ Fq ,
we rotate and translate each minutia (xi , yi , zi ) to (xi + ∆x, yi + ∆y, zi + ∆z)). 2 We could also

2To be more precise we ﬁrst perform the translation and rotation over the reals and then quantize and map to
the appropriate Fq value.
 309

do some local error correction to a quantized value to mitigate the effect of varying pressure.
Going over all possible shifts is not a practical solution, but theoretically this can still lead to a
polynomial-time solution.
We now formally deﬁne our problem, which primarily captures issues 3 and 4. (Below for
any integers t ≥ 1, (Fq
t ) denotes the set of all subsets of Fq of size exactly t .) The following are the
components of the problem:

• Integers k ≥ 1, n ≥ t ≥ 1

• Secret s ∈ Fk
q

• Fingerprint f ∈
 (Fq
t
 )

• LOCK : Fk
q ×
 (
Fq
t
 )
 →
 (
Fq
n
 )

• UNLOCK :
 (
Fq
t
 )
 ×
 (
Fq
n
 )
 → Fk
q

The goal of the problem is to deﬁne the functions LOCK and UNLOCK such that they satisfy
these two properties (for some c < t ):

1. (c-completeness.) For any f , f ′ ∈ (Fq
t ) such that | f − f ′| ≤ c, the following should hold:

UNLOCK (LOCK(s, f ), f ′) = s.

2. (Soundness.) It should be “hard" for an adversary to get s from LOCK(s, f ). (The notion of
“hard" will be more formally deﬁned later.)

Note that the completeness property corresponds to the matching property we need from
our hash function, while the soundness property corresponds to the security property of the
hash function.

18.2.2 Two Futile Attempts

We begin with two attempts at designing the LOCK and UNLOCK functions, which will not work.
However, later we will see how we can combine both to get our ﬁnal solution.
For this section, unless mentioned otherwise, we will assume that the original ﬁngerprint f
is given by the set {α1, . . . , αt }.
 310

Attempt 1. We begin with a scheme that focuses on the soundness property. A very simple
idea, which is what we will start off with, would be to just add n − t random values to f to
get our vault. The intuition, which can be made precise, is that an adversary just looking at the
vault will just see random points and will not be able to recover f from the random set of points.
The catch of course that this scheme has terrible completeness. In particular, if we get a match
between a value in the second ﬁngerprint f ′ and the vault, we have no way to know whether
the match is to one of the original values in f or if the match is with one of the random “chaff"
points there were added earlier.

Attempt 2. Next, we specify a scheme that has good completeness (but has pretty bad sound-
ness).
We begin with the LOCK function:

LOCK2(s, f ) = {(α1, Ps(α1)), . . . , (αt , Ps(αt ))},

where Ps(X ) = ∑k−1
i =0 s·X i and recall f = {α1, . . . , αt }. (Note that we have n = t .)
The main intuition behind LOCK2 is the following. Given another ﬁngerprint f ′ = {β1, . . . , βt }
such that it is close enough to f , i.e. | f \ f ′| ≤ c, for every value in f ∩ f ′, we will know the
corresponding Ps value and thus, we can use the fact that we can decode Reed-Solomon codes
from erasures to recover the secret s. We formally present UNLOCK2 as Algorithm 33.

Algorithm 33 UNLOCK2
INPUT: Vault {(α1, y1), . . . , (αt , yt )} = LOCK(s, f ) and another ﬁngerprint f ′ = {β1, . . . , βt }
OUTPUT: s if | f \ f ′| ≤ c

1: FOR i = 1, . . . , t DO

2: IF there exists a j ∈ [t ] such that αi = β j THEN

3: z j ← yi
4: ELSE

5: z j ←?

6: z ← (z1, . . . , zt )

7: Run Algorithm from Theorem 12.2.1 to correct z from erasures for RS codes with evaluation
points {β1, . . . , βt } and output resulting message as s.

The following result is fairly simple to argue.

Lemma 18.2.1. The pair (LOCK2, UNLOCK2) of functions is (t − k)-complete. Further, both func-
tions can be implemented in polynomial time.

Proof. Let us assume | f \ f ′| ≤ t −k. Now as both f and f ′ have exactly t values, this means that
z has at most t − k erasures. Thus, by Theorem 12.2.1, Step 6 will output s and UNLOCK2 can
be implemented in polynomial time. Further, the claim on the polynomial run time of LOCK2
follows from the fact that one can do encoding of Reed-Solomon code in polynomial time.

311

Unfortunately, (LOCK2, UNLOCK2) pair has terrible soundness. This is because the vault {(α1, y1), . . . , (αt , yt )}
has f in the ﬁrst component in each pair. This an adversary can just read off those values and
present f ′ = {α1, . . . , αt }, which would imply that UNLOCK2(LOCK2(s, f ), f ′) = s, which means
that the vault would be “broken."

18.3 The Final Fuzzy Vault

So far we have seen two attempts: one that (intuitively) has very good soundness but no com-
pleteness and another which has good completeness but terrible soundness. It is natural to
consider if we can combine both of these attempts and get the best of both worlds. Indeed, it
turns we can easily combine both of our previous attempts to get the ﬁnal fuzzy vault.
Algorithm 34 presents the new LOCK3 function.

Algorithm 34 LOCK3
INPUT: Fingerprint f = {α1, . . . , αt } and secret s = (s0, . . . , sk−1) ∈ Fk
q
OUTPUT: Vault with f locking s

1: R, T ← ;

2: Ps(X ) ← ∑k−1
i =0 si · X i

3: FOR i = 1, . . . , t DO

4: T ← T ∪ {αi }

5: FOR i = t + 1, . . . , n DO

6: αi be a random element from Fq \ T

7: T ← T ∪ {αi }

8: FOR every α ∈ T DO

9: γ be a random element from Fq \ Ps(α)

10: R ← R ∪ {(α, γ)}

11: Randomly permute R

12: RETURN R

Algorithm 35 presents the new UNLOCK3 function.
The following result is a simple generalization of Lemma 18.2.1.

Lemma 18.3.1. The pair (LOCK3, UNLOCK3) of functions is (t −k)/2-complete. Further, both func-
tions can be implemented in polynomial time.

Proof. Let us assume | f \ f ′| ≤ (t − k)/2. Now as both f and f ′ have exactly t values, it implies
that | f ∩ f ′| ≥ (t + k)/2. Further for each j ∈ [t ] such that β j ∈ f ∩ f ′, we have that z j = Ps(β j ).
In other words, this means that z has at most (t − k)/2 errors.3 Thus, by Theorem 12.2.2, Step 6
will output s and UNLOCK3 can be implemented in polynomial time. Further, the claim on the
polynomial run time of LOCK3 follows from the fact that one can do encoding of Reed-Solomon
code in polynomial time.

3To be more precise if z has e errors and s erasures w.r.t. the codeword corresponding to s, then 2e + s ≤ t − k.

312

Algorithm 35 UNLOCK2
INPUT: Vault {(α1, y1), . . . , (αn, yn)} = LOCK(s, f ) and another ﬁngerprint f ′ = {β1, . . . , βt }
OUTPUT: s if | f \ f ′| ≤ c

1: FOR i = 1, . . . , t DO

2: IF there exists a j ∈ [n] such that αi = β j THEN

3: z j ← yi
4: ELSE

5: z j ←?

6: z ← (z1, . . . , zt )

7: Run Algorithm from Theorem 12.2.2 to correct z from errors and erasures for RS codes with
evaluation points {β1, . . . , βt } and output resulting message as s.

18.3.1 Soundness

To avoid getting into too much technical details, we will present a high level argument for why
the proposed fuzzy vault scheme has good soundness. Given a vault {(α1, y1), . . . , (αn, yn)} =

LOCK3(s, f ), we know that there are exactly t values (i.e. those α j ∈ f ) such that the polynomial
Ps(X ) agrees with the vault on exactly those t points. Thus, an intuitive way to argue the sound-
ness of the vault would be to argue that there exists a lot other secrets s′ ∈ Fk
q such that Ps′(X )
also agrees with the vault in exactly t positions. (One can formalize this intuition and argue that
the vault satisﬁes a more formal deﬁnition of soundness but we will skip those details.)
We will formalize the above argument by proving a slightly different result (and we will leave
the ﬁnal proof as an exercise).

Lemma 18.3.2. Let V = {(x1, y1), . . . , (xn, yn) be n independent random points from Fq ×Fq . Then,

in expectation, there are at least 1
3 · q k · ( n
q t
 )t polynomials P (X ) of degree at most k − 1 such that
for exactly t values of j ∈ [n], we have P (x j ) = y j .

Proof. Consider a ﬁxed polynomial P (X ) and a j ∈ [n]. Then for any x j ∈ Fq , the probability that
for a random y j ∈ Fq , P (x j ) = y j is exactly 1/q. Further, these probabilities are all independent.
This implies that the probability that P (X ) agrees with V in exactly t positions is given by
(n
t
 )
 · ( 1
q
 )t · (1 − 1
q
 )n−t ≥ 1
3
 ( n
q t
 )t .

Since there are q k such polynomials, the claimed result follows.

We note that there are two aspects of the above lemma that are not satisfactory. (i) The result
above is for a vault V with completely random points whereas we would like to prove a similar
result but with V = LOCK3(s, f ) and (ii) Instead of a bound in expectation, we would like to prove
a similar exponential lower bound but with high probability. We leave the proof that these can
be done as an exercise. (Hint: Use the “Inverse Markov Inequality.")

313

18.4 Bibliographic Notes

The fuzzy vault presented in this chapter is due to Juels and Sudan [57]. The “inverse Markov
inequality" ﬁrst appeared in Dumer et al. [24].

314

Chapter 19

Finding Defectives: Group Testing

Consider the following situation that arises very frequently in biological screens. Say there are N
individuals and the objective of the study is to identify the individuals with a certain “biomarker"
that could e.g. indicate that the individual has some speciﬁc disease or is at risk for a certain
health condition. The naive way to do this would be to test each person individually, that is:

1. Draw sample (e.g. a blood or DNA sample) from a given individual,

2. Perform required tests, then

3. Determine presence or absence of the biomarker.

This method of one test per person will gives us a total of N tests for a total of N individuals.
Say we had more than 70 − 75% of the population infected. At such large numbers, the use of
the method of individual testing is reasonable. However, our goal is to achieve effective testing
in the more likely scenario where it doesn’t make sense to test 100, 000 people to get just (say)
10 positives.
The feasibility of a more effective testing scheme hinges on the following property. We can
combine blood samples and test a combined sample together to check if at least one individual
has the biomarker.
The main question in group testing is the following: If we have a very large number of items
to test, and we know that only certain few will turn out positive, what is a nice and efﬁcient way
of performing the tests?

19.1 Formalization of the problem

We now formalize the group testing problem. The input to the problem consists of the follow-
ing:
• The total number of individuals: N .

• An upper bound on the number of infected individuals d .

315

• The input can be described as a vector x = (x1, x2, ..., xn) where xi = 1 if individual i has
the biomarker, else xi = 0.

Note that w t (x) ≤ d . More importantly, notice that the vector x is an implicit input since we
do not know the positions of 1s in the input. The only way to ﬁnd out is to run the tests. Now,
we will formalize the notion of a test.
A query/test S is a subset of [N ]. The answer to the query S ⊆ [N ] is deﬁned as follows:

A(S) =
 { 1 if ∑

i ∈S xi ≥ 1;

0 otherwise.

Note that the answer to the S is the logical-OR of all bits in S, i.e. A(S) = ⋁i ∈S xi .
The goal of the problem is to compute x and minimize the number of tests required to de-
termine x.

Testing methods. There is another aspect of the problem that we need specify. In particular,
we might need to restrict how the tests interact with each other. Below are two commons ways
to carry out tests:

1. Adaptive group testing is where we test a given subset of items, get the answer and base
our further tests on the outcome of the previous set of tests and their answers.

2. Non-Adaptive group testing on the other hand is when all our tests are set even before we
perform our ﬁrst test. That is, all our tests are decided a priori.

Non-adaptive group testing is crucial for many applications. This is because the individuals
could be geographically spread pretty far out. Due to this, adaptive group testing will require
a very high degree of co-ordination between the different groups. This might actually increase
the cost of the process.

Notation. We will also need notation to denote the minimum number of tests needed in group
testing. Towards this end, we present the following two deﬁnitions.

Deﬁnition 19.1.1 (t (d , N )). Given a subset of N items with d defects represented as x ∈ {0, 1}N ,
the minimum number of non-adaptive tests that one would have to make is deﬁned as t (d , N ).

Deﬁnition 19.1.2. t a(d , N ) : Given a set of N items with d defects, t a(d , N ) is deﬁned as the
number of adaptive tests that one would have to make to detect all the defective items.

The obvious questions are to prove bounds on t (d , N ) and t a(d , N ):

Question 19.1.1. Prove asymptotically tight bounds on t (d , N ).

316

Question 19.1.2. Prove asymptotically tight bounds on t a(d , N ).

We begin with some simple bounds:

Proposition 19.1.1. For every 1 ≤ d ≤ N , we have

1 ≤ t a(d , N ) ≤ t (d , N ) ≤ N .

Proof. The last inequality follows from the naive scheme of testing all individuals with singleton
tests while the ﬁrst inequality is trivial. The reason for t a(d , N ) ≤ t (d , N ) is due to the fact that
any non-adaptive test can be performed by an adaptive test by running all of the tests in the
ﬁrst step of the adaptive test. Adaptive tests can be faster than non-adaptive tests since the test
can be changed after certain things are discovered.

Representing the set of tests as a matrix. It turns out that is is useful to represent a non-
adaptive group testing scheme as a matrix. Next, we outline the natural such representation.
For, S ⊆ [N ], deﬁne χS ∈ {0, 1}N such that i ∈ S if and only if χS(i ) = 1. Consider a non-adaptive
group testing scheme with t test S1, . . . , St . The corresponding matrix M is a t × N matrix where
the i th row is χSi . (Note that the trivial solution of testing each individual as a singleton set
would just be the N × N identity matrix.) In other words, M = {Mi j }i ∈[t ], j ∈[N ] such that Mi j = 1
if j ∈ Si and Mi j = 0 otherwise.
If we assume that multiplication is logical AND (⋀
) and addition is logical OR (⋁
), then we
have M × x = r where r ∈ {0, 1}t is the vector of the answers to the t tests. We will denote this
operation as M ⊙x. To think of this in terms of testing, it is helpful to visualize the matrix-vector
multiplication. Here, r will have a 1 in position i if and only if there was a 1 in that position in
both M and x i.e. if that person was tested with that particular group and if he tested out to be
positive.
Thus, our goal is to get to compute x from M ⊙ x with as small a t as possible.

19.2 Bounds on t a(d , N )

In this section, we will explore lower and upper bounds on t a(d , N ) with the ultimate objective
of answering Question 19.1.2.
We begin with a lower bound that follows from a simple counting argument.

Proposition 19.2.1. For every 1 ≤ d ≤ N ,

t a(d , N ) ≥ d log N
d .

Proof. Fix any valid adaptive group testing scheme with t tests. Observe that if x ̸= y ∈ {0, 1}N ,
with w t (x), w t (y) ≤ d then r(x) ̸= r(y), where r(x) denotes the result vector for running the tests

317

on x and similarly for r(y). The reason for this is because two valid inputs cannot give the same
result. If this were the case and the results of the tests gave r(x) = r(y) then it would not be
possible to distinguish between x and y.
The above observation implies that total number of distinct test results is the number dis-
tinct binary vectors with Hamming weight at most d , i.e. V ol2(d , N ). On the other hand, the
number of possible distinct t -bit vectors is at most 2t , which with the previous argument im-
plies that 2t ≥ V ol2(d , N )

and hence, it implies that t ≥ logV ol2(d , N ).

Recall that
 V ol2(d , N ) ≥
 (N
d
 )
 ≥ ( N
d
 )d ,

where the ﬁrst inequality follows from (3.23) and the second inequality follows from Lemma B.1.1.
So t ≥ d log(N /d ), as desired.

It turns out that t a(d , N ) is also O (d log ( N
d )). (See Exercise 19.1.) This along with Propo-
sition 19.2.1 implies that t a(d , N ) = Θ (
d log ( N
d ))
, which answers Question 19.1.2. The upper
bound on t a(d , N ) follows from an adaptive group testing scheme and hence does not say
anything meaningful for Question 19.1.1. (Indeed, we will see later that t (d , N ) cannot be
O(d log(N /d )).) Next, we switch gears to talk about non-adaptive group testing.

19.3 Bounds on t (d , N )

We begin with the simplest case of d = 1. In this case it is instructive to recall our goal. We want
to deﬁne a matrix M such that given any x with w t (x) ≤ 1, we should be able to compute x from
M ⊙ x. In particular, let us consider the case when x = ei for some i ∈ [N ]. Note that in this
case M ⊙ x = M i , where M i is the i th column of M . Hence we should design M such that M i

uniquely deﬁned i . We have already encountered a similar situation before in Section 2.6 when
trying to decode the Hamming code. It turns out that is sufﬁces to pick M as the parity check
matrix of a Hamming code. In particular, we can prove the following result:

Proposition 19.3.1. t (1, N ) ≤ ⌈log(N + 1)⌉ + 1

Proof. We prove the upper bound by exhibiting a matrix that can handle non adaptive group
testing for d = 1. The group test matrix M is the parity check matrix for [2m − 1, 2m − m − 1, 3]2,
i.e. Hm where the i -th column is the binary representation of i (recall Section 2.4). This works
because when performing Hm ⊙x = r, if w t (v) ≤ 1 then r will correspond to the binary represen-
tation of i . Further, note that if w t (x) = 0, then r = 0, which is exactly x. Hence, M ⊙ x uniquely
identiﬁes x when w t (x) ≤ 1, as desired.
If N ̸= 2m − 1 for any m, the matrix Hm corresponding to the m such that 2m−1 − 1 < N <
2m − 1 can be used by adding 0s to the end of x. By doing this, decoding is "trivial" for both

318

cases since the binary representation is given for the location. So the number of tests is at most
⌈log(N + 1)⌉ + 1, which completes the proof.

Note that Propositions 19.1.1 and 19.2.1 imply that t (d , N ) ≥ log N , which with the above
result implies that t (1, N ) = Θ(log N ). This answers Question 19.1.1 for the case of d = 1. We will
see later that such a tight answer is not known for larger d . However, at the very least we should
try and extend Proposition 19.3.1 for larger values of d . In particular,

Question 19.3.1. Prove asymptotic upper bounds on t (d , N ) that hold for every 1 < d ≤ N .

We would like to point out something that was implicitly used in the proof of Proposi-
tion 19.3.1. In particular, we used the implicitly understanding that a non-adaptive group test-
ing matrix M should have the property that given any x ∈ {0, 1}N such that w t (x) ≤ d , the result
vector M ⊙ x should uniquely determine x. This notion is formally captured in the following
deﬁnition of non-adaptive group testing matrix:

Deﬁnition 19.3.1. A t ×N matrix M is d -separable if and only if for every S1 ̸= S2 ⊆ [N ] such that
|S1|, |S2| ≤ d , we have
 ⋃

j ∈S1 M j ̸= ⋃

i ∈S2 M i .

In the above we think of a columns M i ∈ {0, 1}t as a subset of [t ] and for the rest of this
chapter we will use both views of the columns of a group testing matrix. Finally, note that the
above deﬁnition is indeed equivalent to our earlier informal deﬁnition since for any x ∈ {0, 1}N

with w t (x) ≤ d , the vector M ⊙ x when thought of as its equivalent subset of [t ] is exactly the set
∪i ∈S M i , where S is the support of x, i.e. S = {i |xi = 1}.
Like in the coding setting, where we cared about the run time of the decoding algorithm,
we also care about the time complexity of the decoding problem (given M ⊙ x compute x) for
group testing. We will now look at the obvious decoding algorithm for d -separable matrices:
just check all possible sets that could form the support of x. Algorithm 36 has the details.
The correctness of Algorithm 36 follows from Deﬁnition 19.3.1. Further, it is easy to check
that this algorithm will run in N Θ(d ) time, which is not efﬁcient for even moderately large d .
This naturally leads to the following question:

Question 19.3.2. Do there exists d -separable matrices that can be efﬁcient decoded?

We would like to remark here that the matrices that we seek in the answer to Question 19.3.2
should have small number of tests (as otherwise the identity matrix answers the question in the
afﬁrmative).
 319

Algorithm 36 Decoder for Separable Matrices
INPUT: Result vector r and d -separable matrix M
OUTPUT: x if r = M ⊙ x else Fail

1: R ← {i |ri = 1}.

2: FOR Every T ⊆ [N ] such that |T | ≤ d DO

3: ST ← ∪i ∈T M i

4: IF R = ST THEN

5: x ← (x1, . . . , xN ) ∈ {0, 1}N such that xi = 1 if and only i ∈ T .

6: RETURN x

7: RETURN Fail

19.3.1 Disjunct Matrices

We now deﬁne a stronger notion of group testing matrices that have a more efﬁcient decoding
algorithm than d -separable matrices.

Deﬁnition 19.3.2. A t × N matrix M is d -disjunct if and only if for every S ⊂ [N ] with |S| ≤ d and
for every j ∉ S, there exist an i ∈ [t ] such that Mi j = 1 but for all k ∈ S, Mi k = 0. Or equivalently

M j ̸⊆ ⋃

k∈S M k .

For an illustration of the deﬁnition, see Figure 19.3.2.

j

i
 S

1 0 0 0 0 0 0 0 0 0 0 0 0 0 0

Figure 19.1: Pick a subset S (not necessarily contiguous). Then pick a column j that is not
present in S. There will always be i such that row i has a 1 in column j and all zeros in S.

Next we argue that disjunctness is a sufﬁcient condition for separability.

Lemma 19.3.2. Any d -disjunct matrix is also d -separable.

320

Proof. For contradiction, assume M is d -disjunct but not d -separable. Since M is not d -separable,
then union of two subset S ̸= T ⊂ [N ] of size at most d each are the same; i.e.

⋃

k∈S M k = ⋃

k∈T M k .

Since S ̸= T , there exists j ∈ T \ S. But we have

M j ⊆ ⋃

k∈T M k = ⋃

k∈S M k ,

where the last equality follows from the previous equality. However, since by deﬁnition j ̸∈ S,
the above contradicts the fact that M is d -disjunct.

In fact, it turns out that disjunctness is also almost a necessary condition: see Exercise 19.2.
Next, we show the real gain of moving to the notion of disjunctness from the notion of sep-
arability.

Lemma 19.3.3. There exists a O(tN) time decoding algorithm for any t × N matrix that is d -
disjunct.

Proof. The proof follows from the following two observations.
First, say we have a matrix M and a vector x and r = M ⊙ x such that ri = 1. Then there exists
a column j in matrix that made it possible i.e. if ri = 1, then there exists a j such that Mi j = 1
and x j = 1.
Second, let T be a subset and j be a column not in T where T = {ℓ | xℓ = 1} and |T | ≤ d .
Consider the i th row such that T has all zeros in the i th row, then ri = 0. Conversely, if ri = 0,
then for every j ∈ [N ] such that Mi j = 1, it has to be the case that x j = 0. This naturally leads to
the decoding algorithm in Algorithm 37.
The correctness of Algorithm 37 follows from the above observation and it can be checked
that the algorithm runs in time O(t N )– see Exercise 19.3.

Modulo the task of exhibiting the existence of d -disjunct matrices, Lemmas 19.3.3 and 19.3.2
answer Question 19.3.2 in the afﬁrmative. Next, we will tackle the following question:

Question 19.3.3. Design d -disjunct matrices with few rows.

As we will see shortly answering the above question will make connection to coding theory
becomes even more explicit.
 321

Algorithm 37 Naive Decoder for Disjunct Matrices
INPUT: Result vector r and d -disjunct matrix M
OUTPUT: x if M ⊙ x = r else Fail

1: Initialize x ∈ {0, 1}N to be the all ones vector

2: FOR every i ∈ [t ] DO

3: IF ri = 0 THEN

4: FOR Every j ∈ [N ] DO

5: IF Mi j = 1 THEN

6: x j ← 0

7: IF M ⊙ x = r THEN

8: RETURN x

9: ELSE

10: RETURN Fail

19.4 Coding Theory and Disjunct Matrices

In this section, we present the connection between coding theory and disjunct matrices with
the ﬁnal goal of answering Question 19.3.3. First, we present a sufﬁcient condition for a matrix
to be d -disjunct.

Lemma 19.4.1. Let 1 ≤ d ≤ N be an integer and M be a t × N matrix, such that

(i) For every j ∈ [N ], the j th column has at least wmin ones in it, i.e. ∣M j ∣ ≥ wmin and

(ii) For every i ̸= j ∈ [N ], the i and j ’th columns have at most amax ones in common, i.e.∣M i ∩ M j ∣ ≤ amax

for some integers amax ≤ wmin ≤ t . Then M is a ⌊ wmin−1

amax
 ⌋
-disjunct.

Proof. For notational convenience, deﬁne d = ⌊ wmin−1
amax
 ⌋
. Fix an arbitrary S ⊂ [N ] such that |S| ≤
d and a j ̸∈ S. Note we have to show that
M j ̸⊆ ∪i ∈S M i ,

or equivalently
 M j ̸⊆ ∪i ∈S (M i ∩ M j ) .

We will prove the above by showing that

∣M j \ ∪i ∈S (M i ∩ M j )∣ > 0.

322

Indeed, consider the following sequence of relationships:

∣M j \ ∪i ∈S (M i ∩ M j )∣ = ∣M j ∣ − ∣∪i ∈S (M i ∩ M j )∣

≥ ∣M j ∣ − ∑

i ∈S
 ∣(M i ∩ M j )∣ (19.1)

≥ wmin − |S| · amax (19.2)

≥ wmin − d · amax (19.3)

≥ wmin − wmin − 1

amax · amax (19.4)

= 1.

In the above, (19.1) follows from the fact that size of the union of sets is at most the sum of
their sizes. (19.2) follows from the deﬁnitions of wmin and amax. (19.3) follows from the fact that
|S| ≤ d while (19.4) follows from the deﬁnition of d . The proof is complete.

Next, we present a simple way to convert a code into a matrix. Let C ⊆ [q]t be a code such
that C = {c1, . . . , cN }. Then consider the matrix MC whose i ’th column is ci , i.e.

MC =
 

 ↑ ↑ ↑
c1 c2 · · · cn
↓ ↓ ↓
 

 .

Thus, by Lemma 19.4.1, to construct an ⌊ wmin−1
amax
 ⌋
-disjunct matrix, it is enough to design a

binary code C ∗ ⊆ {0, 1}t such that (i) for every c ∈ C ∗, w t (c) ≥ wmin and (ii) for every c1 ̸= c2 ∈ C ∗,
we have |{i |c 1
i = c 2
i = 1}| ≤ amax. Next, we look at the construction of such a code.

19.4.1 Kautz-Singleton Construction

In this section, we will prove the following result:

Theorem 19.4.2. For every integer d ≥ 1 and large enough N ≥ d , there exists a t × N matrix is

d -disjunct where t = O (d 2 (
logd N )2).

Note that the above result answers Question 19.3.3. It turns out that one can do a bit better:
see Exercise 19.4.
Towards this end, we will now study a construction of C ∗ as in the previous section due to
Kautz and Singleton. As we have already seen in Chapter 10, concatenated codes are a way
to design binary codes. For our construction of C ∗, we will also use code concatenation. In
particular, we will pick C ∗ = Cout ◦ Cin, where Cout is a [q, k, q − k + 1]q Reed-Solomon code (see
Chapter 5) while the inner code Cin : Fq → {0, 1}q is deﬁned as follows. For any i ∈ Fq , deﬁne
Cin(i ) = ei . Note that MCin is the identity matrix and that N = q k and t = q 2.

323

Example 19.4.3. Let k = 1 and q = 3. Note that by our choice of [3, 1]3 Reed-Solomon codes, we
have Cout = {(0, 0, 0), (1, 1, 1), (2, 2, 2)}. In other words,

MCout =
 


0 1 2
0 1 2
0 1 2


 .

Then the construction of MC ∗ can be visualized as in Figure 19.4.3.




0 1 2
0 1 2
0 1 2




MCout
 ◦
 


0 0 1
0 1 0
1 0 0




MCin
 →
 
















0 0 1
0 1 0
1 0 0
0 0 1
0 1 0
1 0 0
0 0 1
0 1 0
1 0 0

















MC ∗

Figure 19.2: Construction of the ﬁnal matrix MC ∗ from MCout and MCin from Example 19.4.3.
The rows in MC ∗ that correspond to the same row in MCout have the same color.

Next, we instantiate parameters in the Kautz-Singleton construction to prove Theorem 19.4.2.

Proof of Theorem 19.4.2. We ﬁrst analyze the construction to determine the parameters wmin
and amax. Then we pick the parameters q and k in terms of d to complete the proof.
Recall that N = q k and t = q 2. It is easy to check that every column of MC ∗ has exactly q
ones in it. In other words, wmin = q. Next, we estimate amax.
Divide the rows into q sized chunks, and index the t = q 2 rows by pairs in [q] × [q]. Recall
that each column in MC ∗ corresponds to a codeword in C ∗. For notational convenience, we
will use M for MC ∗. Note that for any row (i , j ) ∈ [q] × [q] and a column index ℓ ∈ [N ], we have
M(i , j ),ℓ = 1 if and only if cℓ( j ) = j (where we use some ﬁxed bijection between Fq and [q] and
cℓ is the ℓ’th codeword in Cout). In other words, the number of rows where the ℓ1th and ℓ2th
columns both have a one is exactly the number of positions where cℓ1 and cℓ2 agree, which is
exactly q − ∆(cℓ1, cℓ2). Since Cout is a [q, k, q − k + 1]q code, the number of rows where any two
columns agree is at most k − 1. In other words, amax = k − 1.1

Lemma 19.4.1 implies that MC ∗ is d -disjunct if we pick

d = ⌊ q − 1
k − 1
 ⌋ .

1The equality is obtained due to columns that corresponds to codewords that agree in exactly k − 1 positions.

324

Thus, we pick q and k such that the above is satisﬁed. Note that we have q = O(kd ). Further,
since we have N = q k , we have k = logq N .

This implies that q = O(d · logq N ), or q log q = O(d log N ). In other words we have

q = O(d logd N ).

Recalling that t = q 2 completes the proof.

An inspection of the proof of Theorem 19.4.2 shows that we only used the distance of the
Reed-Solomon code and in particular, any Cout with large enough distance sufﬁces. In particu-
lar, if we pick Cout to be a random code over an appropriate sized alphabet then one can obtain
t = O(d 2 log N ). (See Exercise 19.5 for more on this.) Note that this bound is incomparable to
the bound in Theorem 19.4.2. It turns out that these two are the best known upper bounds on
t (d , N ). In particular,

Open Question 19.4.1. Can we beat the upper bound of O (d 2 · min (
log(N /d ), log
2 N )) on
t (d , N )?

It turns out that the quadratic dependence on d in the upper bounds is tight. In fact it is
known that t (d , N ) ≥ Ω(d 2 logd N ). (See Exercises 19.7 and 19.8.)
Next, we present an application of group testing in the ﬁeld of data stream algorithms, which
in turn will bring out another facet of the connection between coding theory and group testing.

19.5 An Application in Data Stream Algorithms

Let us consider the problem of tracking updates on stock trades. Given a set of trades (i1, u1), · · · ,
(im, um), where i j is the stock id for the j t h trade, u j is the amount of the stocks in the j t h trade.
The problem is to keep track of the top d stocks. Such a problem is also called hot items/ heavy
hitters problem.
Let N be the total number of stocks in the market. This problem could be solved in O(m) +
O(N log N ) ≈ O(m) time and O(N ) space by setting a O(N ) size buffer to record the total number
of trading for each stock and then sort the buffer later. However, m could be of the order of
millions for one minute’s trading, e.g. in the ﬁrst minute of April 19, 2010, there are 8077600
stocks were traded. Taking the huge amount of trades into consideration, such an algorithm is
not practical.
A more practical model of efﬁcient algorithms in this context is one of data stream algo-
rithm, which is deﬁned as follows.

Deﬁnition 19.5.1. A data stream algorithm has four requirements listed below:

1. The algorithm should make one sequential pass over the input.

325

2. The algorithm should use poly-log space. (In particular, it cannot store the entire input.)

3. The algorithm should have poly-log update time, i.e. whenever a new item appears, the
algorithm should be able to update its internal state in poly-log time.

4. The algorithm should have poly-log reporting time, i.e. at any point of time the algorithm
should be able to return the required answers in poly-log time.

Thus, ideally we would like to design a data stream algorithm to solve the hot items problem
that we discussed earlier. Next, we formally deﬁne the hot items problem. We begin with the
deﬁnition of frequencies of each stock:

Deﬁnition 19.5.2. Let fℓ denote the total count for the stock id ℓ. Initially fℓ = 0, given (ℓ, uℓ), fℓ ←
fℓ + uℓ.

Next, we deﬁne the hot items problem.

Deﬁnition 19.5.3 (Hot Items Problem). Given N different items, for m input pairs of data (iℓ, uℓ)
for 1 ≤ ℓ ≤ m, where iℓ ∈ [N ] indicates the item index and uℓ indicates corresponding count.
The problem requires updating the count fℓ(1 ≤ ℓ ≤ m) for each item, and to output all item

indices j such that f j >
 ∑N
ℓ=1 uℓ
d . (Any such item is called a hot item.)

Note that there can be at most d hot items. In this chapter, we will mostly think of d as
O(log N ). Hot items problem is also called heavy hitters problems. We state the result below
without proof:

Theorem 19.5.1. Computing hot items exactly by a deterministic one pass algorithm needs Ω(n)
space (even with exponential time).

This theorem means that we cannot solve the hot items problem in poly-log space as we
want. However, we could try to ﬁnd solutions for problems around this. The ﬁrst one is to
output an approximate solution, which will output a set that contains all hot items and some
non-hot items. For this solution, we want to make sure that the size of the output set is not too
large (e.g. outputting [N ] is not a sensible solution).
Another solution is to make some assumptions on the input. For example, we can assume
Zipf-like distribution of the input data, which means only a few items appear frequently. More
speciﬁcally, we can assume heavy-tail distribution on the input data, i.e.:

∑

ℓ:not hot fℓ ≤ m
d . (19.5)

This is reasonable for many applications, such as hot stock ﬁnding, where only a few of them
have large frequency. Next, we will explore the connection between group testing and hot items
problem based on this assumption.
 326

19.5.1 Connection to Group Testing

Let us recall the naive solution that does not lead to a data stream algorithm: for each item
j ∈ [N ], we maintain the actual count of number of trades for stock j . In other words, at any
point of time, if C j is the count for stock j , we have C j = f j . Another way to represent this is if
M is the N × N identity matrix, then we maintain the vector of counts via M · f, where f is the
vector of the frequencies of the items. Paralleling the story in group testing where we replace
the identity matrix with a matrix with fewer rows, a natural idea here would be to replace M
by matrix with fewer rows that utilizes the fact that there can be at most d hot items. Next, we
show that this idea works if the heavy tail distribution holds. In particular, we will reduce the
hot items problem to the group testing problem.
We now show how we solve the hot items problem from Deﬁnition 19.5.3. Let M be an t × N
matrix that is d -disjunct. We maintain counters C1, . . . ,Ct , where each Ci is the total count of
any item that is present in the i th row. We also maintain the total number of items m seen so far.
Algorithm 38 and Algorithm 39 present the initialization and update algorithms. The reporting
algorithm then needs to solve the following problem: at any point of time, given the counts
C1, . . . ,Ct and m output the at most d hot items.

Algorithm 38 Initialization
OUTPUT: Initialize the counters

1: m ← 0

2: FOR every j ∈ [t ] DO

3: C j ← 0

Algorithm 39 Update
INPUT: Input pair (i , u), i ∈ [N ] and u ∈ Z
OUTPUT: Update the Counters

1: m ← m + 1,

2: FOR every j ∈ [t ] DO

3: IF Mi j = 1 THEN

4: C j ← C j + u

Next, we reduce the problem of reporting hot items to the decoding problem of group test-
ing. The reduction essentially follows from the following observations.

Observation 19.5.2. If j is a hot item and Mi j = 1, then Ci > m
d .

327

Proof. Let i ∈ [t ] be such that Mi j = 1. Then note that at any point of time,

Ci = ∑

k:Mi k =1 fk ≥ f j .2

Since j is a hot item, we have f j > m
d , which completes the proof.

Observation 19.5.3. For any 1 ≤ i ≤ t , if all j with Mi j = 1 are not hot items, then we have Ci ≤ m
d .

Proof. Fix an ∈ [t ] such that every j ∈ [N ] such that Mi j = 1 is not a hot item. Then by the same
argument as in proof of Observation 19.5.2, we have

Ci = ∑

k:Mi k =1 fk .

The proof then follows by the choice of i and (19.5).

Armed with these observations, we now present the reduction. Deﬁne x = (x1, x2, . . . , xN ) ∈
{0, 1}N with x j = 1 if and only if j is a hot item, and r = (r1, r2, . . . , rt ) ∈ {0, 1}t with ri = 1 if and
only if Ci > m
d , we will have ri = ∨ j :Mi j =1x j . The latter claim follows from Observations 19.5.2
and 19.5.3 above. This means we have:
 M ⊙ x = r. (19.6)

Note that by deﬁnition, w t (x) < d . Thus reporting the hot items is the same as decoding to
compute x given M and r, which successfully changes the hot items problem into group testing
problem. Algorithm 40 has the formal speciﬁcation of this algorithm.

Algorithm 40 Report Heavy Items
INPUT: Counters m and C1, . . . ,Ct
OUTPUT: Output the heavy items

1: FOR every j ∈ [t ] DO

2: IF Ct > m
d THEN

3: r j ← 1

4: ELSE

5: r j ← 0

6: Let x be the result of decoding (for group testing) r

7: RETURN {i |xi = 1}

Next, we will design and analyze the algorithm above and check if the conditions in Deﬁni-
tion 19.5.1 are met.

2The equality follows e.g. by applying induction on Algorithm 39.

328

Analysis of the Algorithm

In this part, we will review the requirements on data stream algorithm one by one and check
if the algorithm for the hot items problem based on group testing satisﬁes them. In particular,
we will need to pick M and the decoding algorithm. We will pick M to be the d -disjunct matrix
from Theorem 19.4.2.

1. One-pass requirement
If we use non-adaptive group testing, the algorithm for the hot items problem above can
be implemented in one pass, which means each input is visited only once. (If adaptive
group testing is used, the algorithm is no longer one pass, therefore we choose non-
adaptive group testing.) We note that by deﬁnition, our choice of M satisﬁes this con-
dition.

2. Poly-log space requirement
In the algorithm, we have to maintain the counters Ci and m. The maximum value for
them is mN , thus we can represent each counter in O(log N + log m) bits. This means
we need O((log N +log m)t )bits to maintain the counters. Theorem 19.4.2 implies that t =
O(d 2 log2 N ). Thus, the total space we need to maintain the counters is O(d 2 log2 N (log N +
log m)).

On the other hand, if we need to store the matrix M , we will need Ω(t N ) space. Therefore,
poly-log space requirement can be achieved only if matrix M is not stored directly. (We
will tackle this issues in the next point.)

3. Poly-log update time
As mentioned in the previous part, we cannot store the matrix M directly in order to have
poly-log space. Since RS code is strongly explicit (see Exercise
 6.9), we do not need to
explicitly store M (we just need to store the parameters of the code Cout and Cin, which can
be done in poly-log space). In the following, we will argue that the runtime of Algorithm 39
is O(t × poly log t ). It is easy to check the claimed time bound is correct as long as we can
perform the check in Step 3 in poly log(t ) time. In particular, we would be done if given
j ∈ [N ], we can compute the column M j in O(t × poly log t ) time. Next, we argue that the
latter claim is correct.

Recall that M = MC ∗, with C ∗ = Cout ◦ Cin, where Cout is a [q, k, q − k + 1]
q RS code and
Cin chosen such that MCin is the q × q identity matrix. Recall that codewords of C ∗ are
columns of the matrix M , and we have n = q k , t = q 2.

Since every column of M corresponds to a codeword of C ∗, we can think of j equiva-
lently as a message m ∈ Fq k . In particular, M j then corresponds to the codeword Cout(m).
On the other hand, the column M j can be partitioned into q chunks, each chunk is of
length q. Notice that (Cout(m))i1 = i2 if and only if the i1th chunk has 1 on its i2th po-
sition and 0 on other positions (recall the deﬁnition of Cin). Therefore, we can compute
M j by computing Cout(m). Because Cout is a linear code, Cout(m) can be computed in

329

O(q 2×poly log q) time,3 implies that M j can be computed in O(q 2×poly log q) time. Since
we have t = q 2, the update process can be ﬁnished with O(t × poly log t ) time. (We do not
need Cout to be strongly explicit: as long as Cout is linear the arguments so far work just as
well.)

4. Reporting time
It is easy to check that the run time of Algorithm 40 is dominated by Step 6. So far, the only
decoding algorithm for M that we have seen is Algorithm 37, which runs in time Ω(t N ),
which does not satisfy the required reporting time requirement. In Exercise 19.11, we
show that using the fact that Cout is the Reed-Solomon code, one can solve the decoding
problem in poly(t ).

Thus, we have argued that

Theorem 19.5.4. There exists a data streaming algorithm that computes d hot items with one
pass, O(t log N ) space for t = O(d 2 log
2 N ), O(t poly log t ) update time and poly(t ) reporting time.

19.6 Summary of best known bounds

We conclude the chapter by collecting the best known bounds on both adaptive and non-
adaptive group testing. First, we know the correct bound on the best possible number of adap-
tive tests:

Theorem 19.6.1. t a(d , N ) = Θ (
d log(N /d )) .

The upper bound follows from Exercise 19.1 while the lower bound follows from Proposi-
tion 19.2.1.
There is a gap between the best known upper and lower bound on the number of non-
adaptive tests:

Theorem 19.6.2.
 Ω (
d 2 logd N ) ≤ t (d , N ) ≤ O (d 2 min (
log(N /d ), log
2 N )) .

The upper bounds follow from Theorem 19.4.2 and Exercise 19.5 while the lower bound
follows from Exercise 19.8.
Finally, note that Theorem 19.6.1 and 19.6.2 imply that there is a gap between the minimum
number of tests needed for adaptive and non-adaptive group testing:

Corollary 19.6.3. t (d , N )
t a(d , N ) ≥ Ω ( d
log d
 ) .

3This follows from Proposition 2.3.2 and the fact that Cout is strongly explicit

330

19.7 Exercises

Exercise 19.1 (Upper bound on t a(d , N )). In this problem we will show that t a(d , N ) = O(d log(N /d )).
We begin by trying to prove a weaker bound of O(d log N ):

• Show that one can identify at least one i such that xi = 1 (or report none exist) with
O(log N ) adaptive tests.

(Hint: Use binary search.)

• Using the scheme above argue that one can compute x with O(w t (x)·log N ) adaptive tests.
Conclude that t a(d , N ) ≤ O(d log N ).

Next we argue that we can tighten the bound to the optimal bound of O(d log(N /d )):

• Argue that any scheme that computes x ∈ {0, 1}N with O(w t (x) · log N ) adaptive tests can
be used to compute x with O(d log(N /d )) adaptive tests where w t (x) ≤ d .

• Conclude that t a(d , N ) ≤ O(d log(N /d )).

Exercise 19.2. Show that every d -separable matrix is also (d − 1)-disjunct.

Exercise 19.3. Prove that Algorithm 37 is correct and runs in time O(t N ).

Exercise 19.4. For every integer d ≥ 1 and large enough integer N ≥ d show that there exists a
d -disjunct matrix with O(d 2 log(N /d )) rows.

(Hint: Use the probabilistic method. It might help to pick each of t N bits in the matrix inde-
pendently at random with the same probability.)

Exercise 19.5. We ﬁrst begin by generalizing the argument of Theorem 19.4.2:

• Let Cout be an (n, k, D)q code. Let Cin be deﬁned such that MCin is the q ×q identity matrix.
Let MCout◦Cin be a t × N matrix that is d -disjunct. Derive the parameters d , t and N .

Next argue that it is enough to pick an outer random code to obtain a d -disjunct matrix with
the same parameters obtained in Exercise 19.4:

• Pick q = Θ(d ). Then using the previous part or otherwise show that if Cout is a random
[n, k, D]q code, then the resulting t × N matrix MCout◦Cin is d -disjunct with t = O(d 2 log N )
for large enough N .

(Hint: Use Theorem 4.2.1 and Proposition 3.3.5.)

Exercise 19.6. For every integer d ≥ 1 and large enough N ≥ d , construct a d -disjunct matrix
with O(d 2 log N ) rows in (deterministic) time poly(N ).

Hint: Recall Exercise 4.7.

Exercise 19.7 (Lower Bound on t (d , N ) due to Bassalygo). In this problem we will show that

t (d , N ) ≥ min {(d +2
2 )
, N }
. In what follows let M be a t × N matrix that is d -disjunct.

331

(a) Argue that if w t (M j ) < d then M j has a private row i.e. there exists a row i ∈ [t ] such that
Mi j = 1 but Mi j ′ = 0 for every j ′ ̸= j .

(b) Using part (a) or otherwise, argue that if all columns of M have Hamming weight at most
d − 1, then t ≥ N .

(c) Let M − j for j ∈ [N ] be the matrix M with M j as well as all rows i ∈ [t ] such that Mi j = 1
removed. Then argue that M − j is (d − 1)-disjunct.

(d) Argue that t (1, N ) ≥ min {3, N }.

(e) Using induction with parts (b)-(d) or otherwise, argue that t ≥ min {(d +2
2 ), N }
.

Exercise 19.8 (Lower Bound on t (d , N ) due to Ruszinkó and Alon-Asodi). In this problem, we
will show that t (d , N ) ≥ Ω (min {d 2 logd N , N }) . (19.7)

In what follows let M be a t × N matrix that is d -disjunct.

(a) Argue that any j ∈ [N ] such that w t (M j ) < 2t
d has a private subset of size ⌈4t /d 2⌉, i.e. there
exists a subset S ⊆ [N ] with |S| = ⌈4t /d 2⌉ such that M j has ones in all i ∈ S but for every
j ̸= j ′, M j ′ has at least one row i ′ ∈ S such that Mi ′ j ′ = 0.

(b) Using part (a) or otherwise, argue:
 N − d
2 ≤
 ( t
⌈4t /d 2⌉
)

.

(c) Using Exercise 19.7 and part (b) or otherwise argue (19.7).

Exercise 19.9. In this exercise and the ones that follow it, we will consider the following equiv-
alent version of the decoding problem: given r = M ⊙ x with w t (x) ≤ d , output {i |xi = 1}. Now
consider the following easier version of the problem. In addition to r and M assume that one is
also given a set S such that {i |xi = 1} ⊆ S. Modify Algorithm 37 to design a decoding algorithm
that computes {i |xi = 1} in time O(t · |S|).

Exercise 19.10. A t × N matrix M is called (d , L)-list disjunct if and only if the following holds for
every disjoint subsets S, T ⊂ [N ] such that |S| = d and |T | = L − d , there is a row in M where all
columns in S have a 0 but at least one column in T has a 1.

• What is a (d , d + 1)-list disjunct matrix?

• Let Cout be an (n, k)q code that is (0, d , L)-list recoverable code (recall Deﬁnition 15.3.2).
Let Cin be the inner code such that MCin is the q × q identity matrix. Argue that MCout◦Cin
is (d , L) list disjunct.

Exercise 19.11. Using Exercises 19.9 and 19.10 or otherwise prove the following. Let MC ∗ be
the Kautz-Singleton matrix from Section 19.4.1. Then given MC ∗ ⊙ x with w t (x) ≤ d , one can
compute {i |xi = 1} in poly(t ) time.
(Hint: Theorem 15.3.2 could be useful.)
 332

19.8 Bibliographic Notes

Robert Dorfman’s paper in 1943 [22] introduced the ﬁeld of (Combinatorial) Group Testing. It
must be noted that though this book covers group testing as an application of coding theory, it
took off long before coding theory itself.
The original motivation arose during the Second World War when the United States Public
Health service and the Selective Service embarked upon a large scale project. The objective was
to weed out all syphilitic men called up for induction. [22].
The connection between group testing and hot items problem considered in Section 19.5
was established by Cormode and Muthukrishnan [20]. More details on data stream algorithms
can be bound in the survey by Muthukrishnan [76].

333334

Bibliography

[1] Manindra Agrawal, Neeraj Kayal, and Nitin Saxena. PRIMES Is in P. Annals of Mathemat-
ics, 160(2):781–793, 2004.

[2] M. Alekhnovich. Linear diophantine equations over polynomials and soft decoding of
reed-solomon codes. In The 43rd Annual IEEE Symposium on Foundations of Computer
Science, 2002. Proceedings., pages 439–448, Nov 2002.

[3] Noga Alon and Joel Spencer. The Probabilistic Method. John Wiley, 1992.

[4] Erdal Arıkan. Channel polarization: A method for constructing capacity-achieving codes
for symmetric binary-input memoryless channels. IEEE Transactions on Information
Theory, pages 3051–3073, July 2009.

[5] Jarosław Bł asiok, Venkatesan Guruswami, Preetum Nakkiran, Atri Rudra, and Madhu Su-
dan. General strong polarization. In Proceedings of the 50th Annual ACM Symposium on
Theory of Computing, pages 485–492, 2018.

[6] P.G.H. Bachmann. Die analytische Zahlentheorie. Number v. 2 in Zahlentheorie. Ver-
such einer Gesammtdarstellung dieser Wissenschaft in ihren Haupttheilen. 2. th. Teub-
ner, 1894.

[7] Donald Beaver and Joan Feigenbaum. Hiding instances in multioracle queries. In Chof-
frut and Lengauer [17], pages 37–48.

[8] Eli Ben-Sasson, Swastik Kopparty, and Jaikumar Radhakrishnan. Subspace polynomi-
als and limits to list decoding of reed-solomon codes. IEEE Trans. Information Theory,
56(1):113–120, 2010.

[9] E. R. Berlekamp. Factoring polynomials over large ﬁnite ﬁelds. Mathematics of Compu-
tation, 24:713–735, 1970.

[10] Kristian Brander. Interpolation and list decoding of algebraic codes. PhD thesis, Technical
University of Denmark, 2010.

[11] P.S. Bullen. Handbook of Means and Their Inequalities. Mathematics and Its Applications.
Springer Netherlands, 2010.
 335

[12] Larry Carter and Mark N. Wegman. Universal classes of hash functions. J. Comput. Syst.
Sci., 18(2):143–154, 1979.

[13] Donald G. Chandler, Eric P. Batterman, and Govind Shah. Hexagonal, information en-
coding article, process and system. US Patent Number 4,874,936, October 1989.

[14] C. L. Chen and M. Y. Hsiao. Error-correcting codes for semiconductor memory applica-
tions: A state-of-the-art review. IBM Journal of Research and Development, 28(2):124–134,
1984.

[15] Peter M. Chen, Edward K. Lee, Garth A. Gibson, Randy H. Katz, and David A. Patter-
son. RAID: High-performance, reliable secondary storage. ACM Computing Surveys,
26(2):145–185, 1994.

[16] Q. Cheng and D. Wan. On the list and bounded distance decodability of reedâ ˘A¸Ssolomon
codes. SIAM Journal on Computing, 37(1):195–209, 2007.

[17] Christian Choffrut and Thomas Lengauer, editors. STACS 90, 7th Annual Symposium on
Theoretical Aspects of Computer Science, Rouen, France, February 22-24, 1990, Proceed-
ings, volume 415 of Lecture Notes in Computer Science. Springer, 1990.

[18] Alan Cobham. The Intrinsic Computational Difﬁculty of Functions. In Y. Bar-Hillel, edi-
tor, Logic, Methodology and Philosophy of Science, proceedings of the second International
Congress, held in Jerusalem, 1964, Amsterdam, 1965. North-Holland.

[19] Stephen A. Cook. The complexity of theorem-proving procedures. In Proceedings of the
3rd Annual ACM Symposium on Theory of Computing (STOC), pages 151–158, 1971.

[20] Graham Cormode and S. Muthukrishnan. What’s hot and what’s not: tracking most fre-
quent items dynamically. ACM Trans. Database Syst., 30(1):249–278, 2005.

[21] Eren ¸Sa¸so˘glu. Polarization and polar codes. Foundations and Trends in Communications
and Information Theory, 8(4):259–381, 2012.

[22] Robert Dorfman. The detection of defective members of large populations. The Annals
of Mathematical Statistics, 14(4):436–440, December 1943.

[23] Devdatt P. Dubhashi and Alessandro Panconesi. Concentration of Measure for the Analysis
of Randomized Algorithms. Cambridge University Press, 2009.

[24] Ilya Dumer, Daniele Micciancio, and Madhu Sudan. Hardness of approximating the min-
imum distance of a linear code. IEEE Transactions on Information Theory, 49(1):22–37,
2003.

[25] Zeev Dvir and Shachar Lovett. Subspace evasive sets. Electronic Colloquium on Compu-
tational Complexity (ECCC), 18:139, 2011.

336

[26] Jack Edmonds. Paths, trees, and ﬂowers. In Ira Gessel and Gian-Carlo Rota, editors, Clas-
sic Papers in Combinatorics, Modern BirkhÃd’user Classics, pages 361–379. BirkhÃd’user
Boston, 1987.

[27] Peter Elias. Error-free coding. IEEE Transactions on Information Theory, 4(4):29–37, 1954.

[28] Peter Elias. List decoding for noisy channels. Technical Report 335, Research Laboratory
of Electronics, MIT, 1957.

[29] P. Erdös. On extremal problems of graphs and generalized graphs. Israel Journal of Math-
ematics, 2(3):183–190, 1964.

[30] G. David Forney. Concatenated Codes. MIT Press, Cambridge, MA, 1966.

[31] G. David Forney. Generalized Minimum Distance decoding. IEEE Transactions on Infor-
mation Theory, 12:125–131, 1966.

[32] Peter Gemmell, Richard J. Lipton, Ronitt Rubinfeld, Madhu Sudan, and Avi Wigderson.
Self-testing/correcting for polynomials and for approximate functions. In Cris Kout-
sougeras and Jeffrey Scott Vitter, editors, Proceedings of the 23rd Annual ACM Symposium
on Theory of Computing, May 5-8, 1991, New Orleans, Louisiana, USA, pages 32–42. ACM,
1991.

[33] Peter Gemmell and Madhu Sudan. Highly resilient correctors for multivariate polynomi-
als. Information Processing Letters, 43(4):169–174, 1992.

[34] Peter Gemmell and Madhu Sudan. Highly resilient correctors for polynomials. Inf. Pro-
cess. Lett., 43(4):169–174, 1992.

[35] E. N. Gilbert. A comparison of signalling alphabets. Bell System Technical Journal, 31:504–
522, 1952.

[36] M. J. E. Golay. Notes on digital coding. Proceedings of the IRE, 37:657, 1949.

[37] Venkatesan Guruswami. Limits to list decodability of linear codes. In Proceedings of the
34th ACM Symposium on Theory of Computing (STOC), pages 802–811, 2002.

[38] Venkatesan Guruswami. List decoding of error-correcting codes. Number 3282 in Lecture
Notes in Computer Science. Springer, 2004. (Winning Thesis of the 2002 ACM Doctoral
Dissertation Competition).

[39] Venkatesan Guruswami. Linear-algebraic list decoding of folded reed-solomon codes.
In Proceedings of the 26th Annual IEEE Conference on Computational Complexity (CCC),
pages 77–85, 2011.

[40] Venkatesan Guruswami, Johan Håstad, and Swastik Kopparty. On the list-decodability of
random linear codes. IEEE Transactions on Information Theory, 57(2):718–725, 2011.

337

[41] Venkatesan Guruswami, Johan Håstad, Madhu Sudan, and David Zuckerman. Combi-
natorial bounds for list decoding. IEEE Transactions on Information Theory, 48(5):1021–
1035, 2002.

[42] Venkatesan Guruswami and Piotr Indyk. Linear-time encodable/decodable codes with
near-optimal rate. IEEE Transactions on Information Theory, 51(10):3393–3400, 2005.

[43] Venkatesan Guruswami and Atri Rudra. Limits to list decoding reed-solomon codes. IEEE
Transactions on Information Theory, 52(8):3642–3649, August 2006.

[44] Venkatesan Guruswami and Atri Rudra. Explicit codes achieving list decoding capac-
ity: Error-correction with optimal redundancy. IEEE Transactions on Information Theory,
54(1):135–150, 2008.

[45] Venkatesan Guruswami and Atri Rudra. Better binary list decodable codes via multilevel
concatenation. IEEE Transactions on Information Theory, 55(1):19–26, 2009.

[46] Venkatesan Guruswami and Atri Rudra. The existence of concatenated codes list-
decodable up to the hamming bound. IEEE Transactions on Information Theory,
56(10):5195–5206, 2010.

[47] Venkatesan Guruswami and Igor Shparlinski. Unconditional proof of tightness of john-
son bound. In Proceedgins of the Fourteenth Annual ACM-SIAM Symposium on Discrete
Algorithms (SODA), pages 754–755, 2003.

[48] Venkatesan Guruswami and Madhu Sudan. Improved decoding of Reed-Solomon and
algebraic-geometry codes. IEEE Transactions on Information Theory, 45(6):1757–1767,
1999.

[49] Venkatesan Guruswami and Ameya Velingker. An entropy sumset inequality and poly-
nomially fast convergence to Shannon capacity over all alphabets. In Proceedings of 30th
Conference on Computational Complexity, pages 42–57, 2015.

[50] Venkatesan Guruswami and Patrick Xia. Polar codes: Speed of polarization and poly-
nomial gap to capacity. IEEE Trans. Information Theory, 61(1):3–16, 2015. Preliminary
version in Proc. of FOCS 2013.

[51] Venkatesan Guruswami and Chaoping Xing. Folded codes from function ﬁeld towers and
improved optimal rate list decoding. Electronic Colloquium on Computational Complex-
ity (ECCC), 19:36, 2012.

[52] Richard W. Hamming. Error Detecting and Error Correcting Codes. Bell System Technical
Journal, 29:147–160, April 1950.

[53] G.H. Hardy and J.E. Littlewood. Some problems of diophantine approximation. Acta
Mathematica, 37(1):193–239, 1914.
 338

[54] Seyed Hamed Hassani, Kasra Alishahi, and Rüdiger L. Urbanke. Finite-length scaling for
polar codes. IEEE Trans. Information Theory, 60(10):5875–5898, 2014.

[55] Johan Håstad, Steven Phillips, and Shmuel Safra. A well-characterized approximation
problem. Inf. Process. Lett., 47(6):301–305, 1993.

[56] Tom Høholdt, J. H. van Lint, and Ruud Pellikaan. Algebraic geometry codes. In W. C. Huf-
famn V. S. Pless and R. A.Brualdi, editors, Handbook of Coding Theory. North Holland,
1998.

[57] Ari Juels and Madhu Sudan. A fuzzy vault scheme. Des. Codes Cryptography, 38(2):237–
257, 2006.

[58] J. Justesen. Class of constructive asymptotically good algebraic codes. IEEE Trans. Inform.
Theory, pages 652–656, Sep 1972.

[59] Erich Kaltofen. Polynomial-time reductions from multivariate to bi- and univariate inte-
gral polynomial factorization. SIAM J. Comput., 14(2):469–489, 1985.

[60] Richard M. Karp. Reducibility among combinatorial problems. In Complexity of Com-
puter Computations, pages 85–103, 1972.

[61] John Y. Kim and Swastik Kopparty. Decoding reed-muller codes over product sets. Theory
of Computing, 13(1):1–38, 2017.

[62] Donald E. Knuth. Big omicron and big omega and big theta. SIGACT News, 8(2):18–24,
April 1976.

[63] Andrei N. Kolmogorov. Three Approaches to the Quantitative Deﬁnition of Information.
Problems of Information Transmission, 1(1):1–7, 1965.

[64] Satish Babu Korada, Eren Sasoglu, and Rüdiger L. Urbanke. Polar codes: Characteriza-
tion of exponent, bounds, and constructions. IEEE Transactions on Information Theory,
56(12):6253–6264, 2010.

[65] E. Landau. Handbuch der lehre von der verteilung der primzahlen. Number v. 1 in Hand-
buch der lehre von der verteilung der primzahlen. B. G. Teubner, 1909.

[66] Amos Lapidoth and P. Narayan. Reliable communication under channel uncertainty.
IEEE Transactions on Information Theory, 44(6):2148–2177, 1998.

[67] Leonid A Levin. Universal sequential search problems. Problemy Peredachi Informatsii,
9(3):115–116, 1973.

[68] Ming Li and Paul M. B. Vitányi. An Introduction to Kolmogorov Complexity and Its Appli-
cations. Graduate Texts in Computer Science. Springer, New York, NY, USA, third edition,
2008.
 339

[69] Rudolf Lidl and Harald Niederreiter. Introduction to Finite Fields and their applications.
Cambridge University Press, Cambridge, MA, 1986.

[70] Richard J. Lipton. Efﬁcient checking of computations. In Choffrut and Lengauer [17],
pages 207–215.

[71] Michael Luby, Michael Mitzenmacher, Mohammad Amin Shokrollahi, and Daniel A.
Spielman. Efﬁcient erasure correcting codes. IEEE Transactions on Information Theory,
47(2):569–584, 2001.

[72] Robert J. McEliece. On the average list size for the Guruswami-Sudan decoder. In 7th In-
ternational Symposium on Communications Theory and Applications (ISCTA), July 2003.

[73] Robert J. McEliece, Eugene R. Rodemich, Howard Rumsey Jr., and Lloyd R. Welch. New
upper bounds on the rate of a code via the Delsarte-Macwilliams inequalities. IEEE Trans-
actions on Information Theory, 23:157–166, 1977.

[74] Ryuhei Mori and Toshiyuki Tanaka. Source and channel polarization over ﬁnite ﬁelds and
Reed-Solomon matrices. IEEE Trans. Information Theory, 60(5):2720–2736, 2014.

[75] David E. Muller. Application of boolean algebra to switching circuit design and to error
detection. Trans. I.R.E. Prof. Group on Electronic Computers, 3(3):6–12, 1954.

[76] S. Muthukrishnan. Data streams: Algorithms and applications. Foundations and Trends
in Theoretical Computer Science, 1(2), 2005.

[77] Farzad Parvaresh and Alexander Vardy. Correcting errors beyond the guruswami-sudan
radius in polynomial time. In Proceedings of the 46th Annual IEEE Symposium on Foun-
dations of Computer Science (FOCS), pages 285–294, 2005.

[78] Ruud Pellikaan and Xin-Wen Wu. List decoding of q-ary reed-muller codes. IEEE Trans.
Information Theory, 50(4):679–682, 2004.

[79] Larry L. Peterson and Bruce S. Davis. Computer Networks: A Systems Approach. Morgan
Kaufmann Publishers, San Francisco, 1996.

[80] W. Wesley Peterson. Encoding and error-correction procedures for Bose-Chaudhuri
codes. IEEE Transactions on Information Theory, 6:459–470, 1960.

[81] Michael O. Rabin. Probailistic algorithms. In J. F. Traub, editor, Algorithms and Complex-
ity, Recent Results and New Directions, pages 21–39, 1976.

[82] I. Reed, R. Scholtz, , and L. Welch. The fast decoding of reed-solomon codes using fermat
theoretic transforms and continued fractions. IEEE Transactions on Information Theory,
24(1):100–106, January 1978.

[83] Irving S. Reed. A class of multiple-error-correcting codes and the decoding scheme.
Trans. of the IRE Professional Group on Information Theory (TIT), 4:38–49, 1954.

340

[84] Irving S. Reed and Gustav Solomon. Polynomial codes over certain ﬁnite ﬁelds. SIAM
Journal on Applied Mathematics, 8(2):300–304, 1960.

[85] Herbert Robbins. A remark on Stirling’s formula. Amer. Math. Monthly, 62:26–29, 1955.

[86] Atri Rudra and Steve Uurtamo. Two theorems on list decoding. In Proceedings of the 14th
Intl. Workshop on Randomization and Computation (RANDOM), pages 696–709, 2010.

[87] Atri Rudra and Mary Wootters. Every list-decodable code for high noise has abundant
near-optimal rate puncturings. In Symposium on Theory of Computing, STOC 2014, New
York, NY, USA, May 31 - June 03, 2014, pages 764–773, 2014.

[88] E. Sasoglu, E. Telatar, and E. Arikan. Polarization for arbitrary discrete memoryless chan-
nels. In 2009 IEEE Information Theory Workshop, pages 144–148, Oct 2009.

[89] Claude E. Shannon. A mathematical theory of communication. Bell System Technical
Journal, 27:379–423, 623–656, 1948.

[90] Victor Shoup. New algorithms for ﬁnding irreducible polynomials over ﬁnite ﬁelds. Math.
Comp., 54:435–447, 1990.

[91] Victor Shoup. A computational introduction to number theory and algebra. Cambridge
University Press, 2006.

[92] R. Singleton. Maximum distance q -nary codes. Information Theory, IEEE Transactions
on, 10(2):116 – 118, apr 1964.

[93] Michael Sipser. The history and status of the p versus np question. In Proceedings of the
Twenty-fourth Annual ACM Symposium on Theory of Computing, STOC ’92, pages 603–
618, New York, NY, USA, 1992. ACM.

[94] Daniel A. Spielman. Linear-time encodable and decodable error-correcting codes. IEEE
Transactions on Information Theory, 42(6):1723–1731, 1996.

[95] Douglas R. Stinson. Universal hashing and authentication codes. Des. Codes Cryptogra-
phy, 4(4):369–380, 1994.

[96] Madhu Sudan. Decoding of Reed Solomon codes beyond the error-correction bound. J.
Complexity, 13(1):180–193, 1997.

[97] Madhu Sudan. List decoding: Algorithms and applications. SIGACT News, 31:16–27, 2000.

[98] Ido Tal and Alexander Vardy. How to construct polar codes. IEEE Trans. Information
Theory, 59(10):6562–6582, 2013.

[99] Robert Endre Tarjan. Algorithmic design. Commun. ACM, 30(3):204–212, 1987.

341

[100] Aimo Tietavainen. On the nonexistence theorems for perfect error-correcting codes.
SIAM Journal of Applied Mathematics, 24(1):88–96, 1973.

[101] Jacobus H. van Lint. Nonexistence theorems for perfect error-correcting codes. In Pro-
ceedings of the Symposium on Computers in Algebra and Number Theory, pages 89–95,
1970.

[102] R. R. Varshamov. Estimate of the number of signals in error correcting codes. Doklady
Akadamii Nauk, 117:739–741, 1957.

[103] Joachim von zur Gathen and Jürgen Gerhard. Modern Computer Algebra. Cambridge
University Press, 3 edition, 2013.

[104] Lloyd R. Welch and Elwyn R. Berlekamp. Error correction of algebraic block codes. US
Patent Number 4,633,470, December 1986.

[105] John M. Wozencraft. List Decoding. Quarterly Progress Report, Research Laboratory of
Electronics, MIT, 48:90–95, 1958.
 342

Appendix A

Notation Table

R The set of real numbers
Z The set of integers
¬E Negation of the event E
log x Logarithm to the base 2
Σm Vectors of length m with symbols from Σ
v A vector
0 The all zero vector
ei The i th standard vector, i.e. 1 in position i and 0 everywhere else
vS Vector v projected down to indices in S
〈u, v〉 Inner-product of vectors u and v
[a, b] {x ∈ R|a ≤ x ≤ b}
[x] The set {1, . . . , x} Section
n Block length of a code Deﬁnition
Σ Alphabet of a code Deﬁnition
q q = |Σ| Deﬁnition
k Dimension of a code Deﬁnition
R Rate of a code Deﬁnition
∆(u, v) Hamming distance between u and v Deﬁnition
d Minimum distance of a code Deﬁnition
w t (v) Hamming weight of v Deﬁnition
B (x, r ) Hamming ball of radius r centered on x Deﬁnition
V olq (r, n) Volume Hamming ball of radius r Deﬁnition
(n, k, d )Σ A code with block length n, dimension k, distance d and alphabet Σ Deﬁnition
(n, k, d )q A code with block length n, dimension k, distance d and alphabet size q Deﬁnition
[n, k, d ]q A linear (n, k, d )q code Deﬁnition
Fq The ﬁnite ﬁeld with q elements (q is a prime power) Section
F∗ The set of non-zero elements in the ﬁeld F
Fm×N
q The set of all m × N matrices where each entry is from Fq
Fq [X1, . . . , Xm] The set of all m-variate polynomials with coefﬁcients from Fq

343

R(C ) Rate of a code family C Deﬁnition
δ(C ) Relative distance of a code family C Deﬁnition
U The uniform distribution Deﬁnition
E[V ] Expectation of a random variable V Deﬁnition
1E Indicator variable for event E Section
Hq (x) x logq (q − 1) − x logq x − (1 − x) logq (1 − x) Deﬁnition
H −1
q (y) Unique x ∈ [0, 1 − 1/q] such that Hq (x) = y Section
deg(P ) Degree of polynomial P (X ) Deﬁnition
Fq [X ] The set of all univariate polynomials in X over Fq Section
Jq (x) (1 − 1/q)(1 − √
1 − q x/(q − 1)) Theor
(S
t ) {T ⊆ S||T | = t }
M ⊙ x Binary matrix-vector multiplication where multiplication is AND and addition is OR

344

Appendix B

Some Useful Facts

B.1 Some Useful Inequalities

Recall that the binomial coefﬁcient for integers a ≤ b, deﬁned as
(b
a
)
 = b!
a!(b − a)! .

We begin with a simple lower bound on the binomial coefﬁcient:

Lemma B.1.1. For every integers 1 ≤ a ≤ b, we have
(b
a
)
 ≥ ( b
a
 )a .

Proof. The following sequence of relations completes the proof:
(a
b
)
 = a−1∏

i =0
 b − i
a − i ≥ a−1∏

i =0
 b
a = ( b
a
 )a .

In the above, the ﬁrst equality follows from deﬁnition and the inequality is true since b ≥ a and
i ≥ 0.

We state the next set of inequalities without proof (see [85] for a proof):

Lemma B.1.2 (Stirling’s Approximation). For every integer n ≥ 1, we have

p2πn ( n
e
 )n eλ1(n) < n! < p2πn ( n
e
 )n eλ2(n),

where
 λ1(n) = 1
12n + 1 and λ2(n) = 1
12n .

We prove another inequality involving Binomial coefﬁcient.

345

Lemma B.1.3. For every integers 1 ≤ a ≤ b, we have

(b
a
)
 ≤ ( eb
a
 )a .

Proof. First note that (a
b
)
 = a(a − 1) · · · (a − b + 1)
b! ≤ ab

b! .

The ﬁnal bound follows from the fact that
 b! > ( b
e
 )b ,

which in turns follows from the lower bound in Lemma B.1.2.

We next state Bernoulli’s inequality:

Lemma B.1.4 (Bernoulli’s Inequality). For every real numbers k ≥ 1 and x ≥ −1, we have

(1 + x)k ≥ 1 + kx.

Proof Sketch. We only present the proof for integer k. For the full proof see e.g. [11].
For the base case of k = 1, the inequality holds trivially. Assume that the inequality holds
for some integer k ≥ 1 and to complete the proof, we will prove it for k + 1. Now consider the
following inequalities:
 (1 + x)k+1 = (1 + x) · (1 + x)k

≥ (1 + x) · (1 + kx)

= 1 + (k + 1)x + kx2

≥ 1 + (k + 1)x,

as desired. In the above, the ﬁrst inequality follows from the inductive hypothesis and the sec-
ond inequality follows from the fact that k ≥ 1.

Lemma B.1.5. For |X |l e1, p1 + x ≤ 1 + x
2 − x2

16 .

Proof. Squaring the RHS we get

(
1 + x
2 − x2

16
 )2 = 1 + x2

4 + x4

256 + x − x2

16 − x3

32 = 1 + x + 3x2

16 − x3

32 + x4

256 ≥ 1 + x,

as desried.
 346

B.2 Some Useful Identities and Bounds

We start off with an equivalence between two inequalities.

Lemma B.2.1. Let a, b, c, d > 0. Then a
b ≤ c
d if and only if a
a+b ≤ c
c+d .

Proof. Note that a
b ≤ c
d if and only if b
a ≥ d
c .

The above is true if and only if b
a + 1 ≥ d
c + 1,

which is same as a
a+b ≤ c
c+d .

Next, we state some inﬁnite sums that are identical to certain logarithms (the proofs are
standard and are omitted).

Lemma B.2.2. For |x| < 1,
 ln(1 + x) = x − x2

2! + x3

3! − · · · .

We can use the above to prove some bounds on ln(1 + x) (we omit the proof):

Lemma B.2.3. For 0 ≤ x < 1, we have

x − x2/2 ≤ ln(1 + x) ≤ x,

and for 0 ≤ x ≤ 1/2, we have −x − x2 ≤ ln(1 − x) ≤ −x.

We can use the above bounds to further prove boounds on the (binary) entropy function:

Lemma B.2.4. For x ≤ 1/4, we have

1 − 5x2 ≤ H (1/2 − x) ≤ 1 − x2.

Proof. By deﬁnition H (1/2 − x) = 1 − 1/2 log(1 − 4x2) + x log(1 − 2x)/(1 + 2x), and using the ap-
proximations for ln(1 + x) from Lemma B.2.3, we have, for x < 1/4,

H (1/2 − x) ≤ 1 + 1
2 ln 2 · (4x2 + 16x4) + 1
ln 2 · (−2x2) − 1
ln 2 · (2x2 − 2x3)

= 1 − 2
ln 2 · x2 + 2
ln 2 · x3 + 8
ln 2 · x4

≤ 1 − x2

ln 2 (B.1)

≤ 1 − x2.

In the above, (B.1) follows by using our assumption that x ≤ 1/4.

347

Using the other sides of the approximations we also have:

H (1/2 − x) ≥ 1 + 1
2 ln 2 · (4x2) + 1
ln 2 · (−2x2 − 4x3) − 1
ln 2 · (2x2)

≥ 1 − 3x2

ln 2
≥ 1 − 5x2,

where the second inequality uses our assumption that x ≤ 1/4.

The following fact follows from the well-known fact that limx→∞(1 + 1/x)x = e:

Lemma B.2.5. For every real x > 0, (
1 + 1
x
 )x ≤ e.

348

Appendix C

Background on Asymptotic notation,
Algorithms and Complexity

In this chapter, we collect relevant background on algorithms and their analysis (as well as their
limitations). We begin with notation that we will use to bound various quantities when we do
not pay close attention to the constants.

C.1 Asymptotic Notation

Throughout the book, we will encounter situations where we would be interested in how a func-
tion f (N ) grows as the input parameter N grows. (We will assume that the real valued function
f is monotone.) The most common such situation is when we would like to bound the run-
time of an algorithm we are analyzing– we will consider this situation in some detail shortly. In
particular, we will interested in bounds on f (N ) that are “oblivious" to constants. E.g. given
that an algorithm takes 24N 2 + 100N steps to terminate, we would be interested in the fact that
the dominating term is the N 2 (for large enough N ). Technically, speaking we are interested in
the asymptotic growth of f (N ). Throughout this chapter, we will assume that all functions are
monotone.
The ﬁrst deﬁnition is when we are interested in an upper bound on the function f (N ). When
talking about numbers, we say b is an upper bound on a if a ≤ b. We will consider a similar
deﬁnition for functions that in some sense ignores constants.

Deﬁnition C.1.1. We say f (N ) is O(g (N )) (to be read as f (N ) is “Big-Oh" of g (N )) if there exists
constants c, N0 ≥ 0 that are independent of N such that for every large enough N ≥ N0:

f (N ) ≤ c · g (N ).

Alternatively f (N ) is O(g (N )) if and only if

lim
N →∞ f (N )
g (N ) ≤ C ,

349

for some absolute constant C . (See Exercise C.1.) So for example both 24N 2+100N and N 2/2−N
are O(N 2) as well as O(N 3). However, neither of them are O(N ) or O(N 3/2).
The second deﬁnition is when we are interested in a lower bound on the function f (N ).
When talking about numbers, we say b is a lower bound on a if a ≥ b. We will consider a similar
deﬁnition for functions that in some sense ignores constants.

Deﬁnition C.1.2. We say f (N ) is Ω(g (N )) (to be read as f (N ) is “Big-Omega" of g (N )) if there
exists constants ε, N0 ≥ 0 that are independent of n such that for every large enough N ≥ N0:

f (N ) ≥ ε · g (N ).

Alternatively f (N ) is Ω(g (N )) if and only if

lim
N →∞ f (N )
g (N ) ≥ C ,

for some absolute constant C . (See Exercise C.2.) So for example both 24N 2+100N and N 2/2−N
are Ω(N 2) as well as Ω(N 3/2). However, neither of them are Ω(N 3) or Ω(N 5/2).
The third deﬁnition is when we are interested in a tight bound on the function f (N ). When
talking about numbers, we say b is same as a if a = b. We will consider a similar deﬁnition for
functions that in some sense ignores constants.

Deﬁnition C.1.3. We say f (N ) is Θ(g (N )) (to be read as f (N ) is “Theta" of g (N )) if and only if
f (N ) is O(g (N )) and is also Ω(g (N )).

Alternatively f (N ) is Θ(g (N )) if and only if

lim
N →∞ f (N )
g (N ) = C ,

for some absolute constant C . (See Exercise C.3.) So for example both 24N 2+100N and N 2/2−N
are Θ(N 2). However, neither of them are Θ(N 3) or Θ(N ).
The fourth deﬁnition is when we are interested in a strict upper bound on the function f (N ).
When talking about numbers, we say b is a strict upper bound on a if a < b. We will consider a
similar deﬁnition for functions that in some sense ignores constants.

Deﬁnition C.1.4. We say f (N ) is o(g (N )) (to be read as f (N ) is “little-oh" of g (N )) if f (N ) is
O(g (N )) but f (N ) is not Ω(g (N )).

Alternatively f (N ) is o(g (N )) if and only if

lim
N →∞ f (N )
g (N ) = 0.

(See Exercise C.4.) So for example both 24N 2 + 100N and N 2/2 − N are o(N 3) as well as o(N 5/2).
However, neither of them are o(N 2) or o(N 3/2).
The ﬁnal deﬁnition is when we are interested in a strict lower bound on the function f (N ).
When talking about numbers, we say b is a strict lower bound on a if a > b. We will consider a
similar deﬁnition for functions that in some sense ignores constants.

350

Deﬁnition C.1.5. We say f (N ) is ω(g (N )) (to be read as f (N ) is “little-omega" of g (N )) if f (N )
is Ω(g (N )) but f (N ) is not O(g (N )).

Alternatively f (N ) is ω(g (N )) if and only if

lim
N →∞ f (N )
g (N ) = ∞.

(See Exercise C.5.) So for example both 24N 2 + 100N and N 2/2 − N are ω(N ) as well as ω(N 3/2).
However, neither of them are ω(N 2) or ω(N 5/2).

C.1.1 Some Properties

We now collect some properties of asymptotic notation that we will be useful in this book.
First all the notations are transitive:

Lemma C.1.1. Let α ∈ {O, Ω, Θ, o, ω}. Then if f (N ) is α(g (N )) and g (N ) is α(h(N )), then f (N ) is
α(h(N )).

Second, all the notations are additive:

Lemma C.1.2. Let α ∈ {O, Ω, Θ, o, ω}. Then if f (N ) is α(h(N )) and g (N ) is α(h(N )), then f (N ) +
g (N ) is α(h(N )).

Finally, all the notations are multiplicative:

Lemma C.1.3. Let α ∈ {O, Ω, Θ, o, ω}. Then if f (N ) is α(h1(N )) and g (N ) is α(h2(N )), then f (N ) ·
g (N ) is α(h1(N ) · h2(N )).

The proofs of the above properties are left as an exercise (see Exercise C.6).

C.2 Bounding Algorithm run time

Let A be the algorithm we are trying to analyze. Then we will deﬁne T (N ) to be the worst-case
run-time of A over all inputs of size N . Slightly more formally, let tA (x) be the number of steps
taken by the algorithm A on input x. Then

T (N ) = max
x:x is of size N tA (x). (C.1)

In this section, we present two useful strategies to prove statements like T (N ) is O(g (N ))
or T (N ) is Ω(h(N )). Then we will analyze the run time of a very simple algorithm. However,
before that we digress to clarify the following: (i) For most of the book, we will be interested in
deterministic algorithms (i.e. algorithm whose execution is ﬁxed given the input). However, we
will consider randomized algorithms (see Section C.3 for more on this). (ii) One needs to clarify
what constitutes a “step" in the deﬁnition of T (N ) above. We do so next.

351

C.2.1 RAM model

In this book, unless speciﬁed otherwise we will assume that the algorithms run on the RAM
model. Informally, this computation model is deﬁned as follows. For an input with n items, the
memory consists of registers with O(log n) bits. For simplicity, we can assume that the input and
output have separate dedicated registers. Note that the input will have n dedicated registers.
Any (atomic) step an algorithm can take are essentially any basic operations on constant
such registers which can be implemented in O(log n) bit operations. In particular, the following
operations are considered to take one step: loading O(log n) from a register or storing O(log n)
bits in a register, initializing the contents of a register, bit-wise operations among registers, e.g.
taking bit-wise XOR of the bits of two registers, adding numbers stored in two registers, incre-
menting the value stored in a register, comparing the values stored in two registers. Some exam-
ples of operations that are not single step operations: multiplying numbers or exponentiation
(where the operands ﬁt into one register each).

C.2.2 Proving T (N ) is O( f (N ))

We start off with an analogy. Say you wanted prove that given m numbers a1, . . . , am, maxi ai ≤
U . Then how would you go about doing so? One way is to argue that the maximum value
is attained at i ∗ and then show that ai ∗ ≤ U . Now this is a perfectly valid way to prove the
inequality we are after but note that you will also have to prove that the maximum value is
attained at i ∗. Generally, this is a non-trivial task. However, consider the following strategy:

Show that for every 1 ≤ i ≤ m, ai ≤ U . Then conclude that maxi ai ≤ U .

Let us consider an example to illustrate the two strategies above. Let us say for whatever rea-
son we are interested in showing that the age of the oldest person in your coding theory lectures
is at most 100. Assume there are 98 students registered and the instructor is always present in
class. This implies that there are at most m = 99 folks in the class. Let us order them somehow
and let ai denote the age of the i ’th person. Then we want to show that max{a1, . . . , a99} ≤ 100
(i.e. U = 100). The ﬁrst strategy above would be to ﬁrst ﬁgure out who is the oldest person in
room: say that is the i ∗’th person (where 1 ≤ i ∗ ≤ 99) and then check if ai ∗ ≤ 100. However, this
strategy is somewhat invasive: e.g. the oldest person might not want to reveal that he or she
is the oldest person in the room. This is where the second strategy works better: we ask every
person in the room if their age is ≤ 100: i.e. we check if for every 1 ≤ i ≤ 99, ai ≤ 100. If everyone
says yes, then we have proved that maxi ai ≤ 100 (without necessarily revealing the identity of
the oldest person).
Mathematically the above two strategies are the same. However, in "practice," using the
second strategy turns out to be much easier. (E.g. this was true in the age example above.)
Thus, here is the strategy to prove that T (N ) is O( f (N )):

For every large enough N , show that for every input x of size N , tA (x) is O( f (N )).
Then conclude that T (N ) is O( f (N )).
 352

C.2.3 Proving T (N ) is Ω( f (N ))

We start off with the same analogy as in the previous section. Say you wanted prove that given
m numbers a1, . . . , am, maxi ai ≥ L. Then how would you go about doing so? Again, one way
is to argue that the maximum value is attained at i ∗ and then show that ai ∗ ≥ L. Now this is a
perfectly valid way to prove the inequality we are after but note that you will also have to prove
that the maximum value is attained at i ∗. Generally, this is a non-trivial task. However, consider
the following strategy:

Show that there exists an 1 ≤ i ≤ m, such that ai ≥ L. Then conclude that maxi ai ≥
L.

Let us go back to the class room example. Now let us say we are interesting in proving that
the oldest person in the room is at least 25 years old. (So a1, . . . , am is as in Section C.2.2 but now
L = 25.) Again, the ﬁrst strategy would be to ﬁrst ﬁgure out the oldest person, say i ∗ and check
if ai ∗ ≥ 25. However, as we saw in Section C.2.2, this strategy is somewhat invasive. However,
consider the the following implementation of the second strategy above. Say for the sake of
mathematics, the instructor comes forward and volunteers the information that her age is at
least 25. Since the oldest person’s age has to be at least the instructor’s age, this proves that
maxi ai ≥ 25, as desired.
Mathematically the above two strategies are the same. However, in "practice," using the
strategy second turns out to be much easier. (E.g., this was true in the age example above.)
Thus, here is the strategy to prove that T (N ) is Ω( f (N )):

For every large enough N , show that there exists an input x of size N , tA (x) is
Ω( f (N )). Then conclude that T (N ) is Ω( f (N )).

C.2.4 An Example

Now let us use all the strategies from Section C.2.2 and Section C.2.3 to asymptotically bound
the run-time of a simple algorithm. Consider the following simple problem: given n+1 numbers
a1, . . . , an; v, we should output 1 ≤ i ≤ n if ai = v (if there are multiple such i ’s then output any
one of them) else output −1. Below is a simple algorithm to solve this problem.

Algorithm 41 Simple Search
INPUT: a1, . . . , an; v
OUTPUT: i if ai = v; −1 otherwise

1: FOR every 1 ≤ i ≤ n DO

2: IF ai = v THEN RETURN i

3: RETURN −1

We will show the following:

Theorem C.2.1. The Simple Search algorithm 41 has a run time of Θ(n).

353

We will prove Theorem C.2.1 by proving Lemmas C.2.2 and C.2.3.

Lemma C.2.2. T (n) for Algorithm 41 is O(n).

Proof. We will use the strategy outlined in Section C.2.2. Let a1, . . . , an; v be an arbitrary input.
Then ﬁrst note that there are at most n iterations of the for loop in Step 1. Further, each iteration
of the for loop (i.e. Step 2) can be implemented in O(1) time (since it involves one comparison
and a potential return of the output value). Thus, by Lemma C.1.3, the total times taken overall
in Steps 1 and 2 is given by T12 ≤ O(n · 1) = O(n).

Further, since Step 3 is a simple return statement, it takes time T3 = O(1) time. Thus, we have
that tAlgorithm 41(a1, . . . , an; v) = T12 + T3 ≤ O(n) + O(1) ≤ O(n),

where the last inequality follows from Lemma C.1.2 and the fact that O(1) is also O(n). Since the
choice of a1, . . . , an; v was arbitrary, the proof is complete.

Lemma C.2.3. T (n) for Algorithm 41 is Ω(n).

Proof. We will follow the strategy laid out in Section C.2.3. For every n ≥ 1, consider the speciﬁc
input a′
i = n+1−i (for every 1 ≤ i ≤ n) and v ′ = 1. For this speciﬁc input, it can be easily checked
that the condition in Step 2 is only satisﬁed when i = n. In other words, the for loop runs at least
(actually exactly) n times. Further, each iteration of this loop (i.e. Step 2) has to perform at least
one comparison, which means that this step takes Ω(1) time. Since n is Ω(n), by Lemma C.1.3
(using notation from the proof of Lemma C.2.2), we have

T12 ≥ Ω(n · 1) = Ω(n).

Thus, we have tAlgorithm 41(a′
1, . . . , a′
n; v ′) ≥ T12 ≥ Ω(n).

Since we have shown the existence of one input for each n ≥ 1 for which the run-time is Ω(n),
the proof is complete.

A quick remark on the proof of Lemma C.2.3. Since by Section C.2.3, we only need to exhibit
only one input with runtime Ω(n), the input instance in the proof of Lemma C.2.3 is only one
possibility. One can choose other instances: e.g. we can choose an instance where the output
has to be −1 (as a speciﬁc instance consider ai = i and v = 0). For this instance one can make a
similar argument as in the proof of Lemma C.2.3 to show that T (n) ≥ Ω(n).

C.2.5 The Best-Case Input “Trap"

We now brieﬂy talk about a common mistake that is made when one starts trying to prove Ω(·)
on T (N ). Note that in Section C.2.3, it says that one can prove that T (N ) to be Ω( f (N )) for
every large enough N , one only needs to pick one input of size N for which the algorithm takes
Ω( f (N )) steps.
 354

The confusing part about the strategy in Section C.2.3 is how does one get a hand on that
special input that will prove the Ω( f (N )) bound. There is no mechanical way of ﬁnding this
input. Generally, speaking you have to look at the algorithm and get a feel for what input might
force the algorithm to spend a lot of time. Sometimes, the analysis of the O(·) bound itself gives
gives us a clue.
However, one way of picking the “special" input that almost always never works in practice
is to consider (for every large enough N ), the “best-case input," i.e. an input of size N on which
the algorithm runs very fast. Now such an input will give you a valid lower bound but it would
almost never give you a tight lower bound.
So for example, let us try to prove Lemma C.2.3 using the best case input. Here is one best
case input: ai = i for every i ∈ [n] and v = 1. Note that in this case the algorithm ﬁnds a match
in the ﬁrst iteration and this terminates in constant many steps. Thus, this will prove an Ω(1)
lower bound but that is not tight/good enough.
Another common mistake is to make an argument for a ﬁxed value of N (say N = 1). How-
ever, note that in this case one can never prove a bound better than Ω(1) and again, this trick
never works in proving any meaningful lower bound.

C.3 Randomized Algorithms

So far the algorithms we have considered are deterministic, i.e. these are algorithm whose be-
havior is completely determined once the input is ﬁxed. We now consider a generalization of
such algorithms to algorithms that have access to random bits. In particular, even when the
input is ﬁxed, the behavior of the algorithm might change depending on the actual value of the
random bits.1 For the machine model, it is easy to modify the RAM model from Section C.2.1
to handle randomized algorithms: we can always load a register with independent and uniform
random bits in one step.
Typically one considers randomized algorithms due to the following reasons:

• For some problems, it is easier to think of a randomized algorithm. Once one has de-
signed a randomized algorithm, one could then attempt to “derandomize" the random-
ized algorithm to construct deterministic algorithms.

• In addition to conceptual simplicity, a randomized algorithm might run faster than all
corresponding known deterministic algorithms.

• For certain problems, it might be provably impossible to design deterministic algorithms
with certain guarantees but it is possible to design randomized algorithms with such guar-
antees. This is a common situation when we might be interested in algorithms that run
in sub-linear time.

1There are many fundamental and interesting questions regarding how truly random these random bits are and
how many such bits can an algorithm access. We will consider the ideal case, where an algorithm has access to as
many uniform and independent random bits as it wants.

355

In this section, we will consider a problem where the third scenario above is applicable. For
examples of the ﬁrst and second scenarios, see Sections 12.3 and D.6 respectively.
Before delving into an example problem, we would like to clarify how we determine the
run time and correctness of a randomized algorithm. There are multiple natural deﬁnitions
but we will consider the following ones. The run time of a randomized algorithm will again
be the worst-case run time as we deﬁned for deterministic algorithms in Section C.2 for every
possible choice of internal random bits that the algorithm might use (with the modiﬁcation to
the RAM model as discussed above). For correctness, the deﬁnition for deterministic algorithm
was obvious so we did not explicitly state it: for every input, a deterministic algorithm must
return the correct output. We call a randomized algorithm correct if on all its inputs, it returns
the correct answer with probability bounded away from a 1/2– to be precise let us say it has to
return the correct output with probability at least 2/3.2

We would like to remark on a subtle point in the deﬁnition above. In the deﬁnition of the
correctness of a randomized algorithm above, the probability is taken over the random coin
tosses that the algorithm might make. However, note that the guarantee is of the worst-case
ﬂavor in the sense that the algorithm has to be correct with high probability for every input.
This should be contrasted with a scenario where the input might itself be random in which case
we might be happy with an average case guarantee where the algorithm is supposed to return
the correct output with high probability (over the distribution over the input). In particular, the
algorithm is allowed to err on certain inputs as long as the total probability mass on the inputs
on which it is incorrect is small: see Chapter 6 where this deﬁnition of correctness makes perfect
sense. In such situations one can always assume that the algorithm itself is deterministic (see
Exercise C.9).

C.3.1 An example problem

In the rest of the section, we will consider the following problem and will attempt to design
(deterministic and randomized) algorithms with an eye to illustrate various points that were
raised when we deﬁned randomized algorithms.

Given a vector x ∈ {0, 1}n determine whether w t (x) ≤ n
3 or w t (x) ≥ 2n
3 . For the cases
where w t (x) ∈ (n/2, 2n/3) the algorithm can have arbitrary behavior.3

We will refer to the above as the GAPHAMMING problem.
It is easy to design an O(n) time deterministic algorithm to solve GAPHAMMING: In O(n)
one can compute w t (x) and then in O(1) time one can verify if w t (x) ≤ n/3 or w t (x) ≥ 2n/3. In
addition one can show that any correct deterministic algorithm will need a run time of Ω(n):
see Exercise C.10.
We will now design a randomized algorithm that solves GAPHAMMING problem. Recall that
we only need to determine if w t (x) ≤ n/3 or w t (x) ≥ 2n/3 (note that we assumed we do not get

2The choice of 2/3 was arbitrary: see Exercise C.8.
3Or equivalently one can assume that the algorithm is given the promise that it will never encounter an input x
with w t (x) ∈ (n/3, 2n/3).
 356

inputs with Hamming weight in (n/3, 2n/2)) with high probability. We will present what is called
a sampling algorithm for this task. To gain intuition, pick a random index i ∈ [n]. Note that then
xi is a random bit. Further, if w t (x) ≤ n/3, then Pri [xi = 1] ≤ 1/3. On the other hand, if w t (x) ≥
2n/3, then the probability is at least 2/3. Thus, if we take s samples, with high probability in the
ﬁrst case we expect to see less than s/3 ones and in the second case we expect to see at least
2s/3 ones. To get a constant probability of success we will invoke Chernoff bound to bound
the probability of seeing more ones in the ﬁrst case than the second case. Algorithm 42 for the
details.

Algorithm 42 Sampling algorithm for GAPHAMMING
INPUT: x ∈ {0, 1}n

OUTPUT: 0 if w t (x) ≤ n/3 and 1 if w t (x) ≥ 2n/3 with probability at least 1 − ε

1: s ← 98 · ln(1/ε)

2: C ← 0

3: FOR j ∈ [s] DO

4: Pick i to be a random index from [n] ⊲ The choice of i is independent for each j

5: C ← C + xi

6: IF C < s/2 THEN

7: RETURN 0

8: RETURN 1

It can be checked that Algorithm 42 runs in time O(log(1/ε)): see Exercise C.11. Next we
argue that the algorithm is correct with probability at least 1 − ε.

Lemma C.3.1. Algorithm 42 outputs the correct answer with probability at least 1 − ε for every x
(such that w t (x) ̸∈ (n/3, 2n/3)).

Proof. We will prove the lemma for the case when w t (x) ≤ n/3 and leave the other case to Exer-
cise C.12.
Fix an arbitrary input x such that w t (x) ≤ n/3. We will argue that at Step 6, we have

Pr [
C ≥ s
3 + s
7
 ] ≤ ε. (C.2)

Note that the above is enough to prove that the algorithm will output 0, as desired.
Towards that end for every j ∈ [s], let Y j be the random bit xi that is picked. Note that C =
∑s
j =1 Y j . Since each of the Y j ’s are independent binary random variables, the additive Chernoff
bound (Theorem 3.1.6) implies that

Pr [
C > E[C ] + s
7
 ] ≤ e− s
72·2 ≤ ε,

where the last inequality follows from our choice of s. As observed earlier for any j , Pr[Y j = 1] ≤
1/3, which implies that E[C ] ≤ s/3, which with the above bound implies (C.2), as desired.

357

Finally, we consider the average-case version of the GAPHAMMING problem. Our goal is
to illustrate the difference between randomized algorithms and average-case algorithms that
was alluded to earlier in this section. Recall that in the GAPHAMMING problem, we are trying to
distinguish between two classes of inputs: one with Hamming weight at most n/3 and the other
with Hamming weight at least 2n/3. We now consider the following natural version where the
inputs themselves comes from two distributions and our goal is to distinguish between the two
cases.
Let Dp denote the distribution on {0, 1}n, where each bit is picked independently
with probability 0 ≤ p ≤ 1. Given an x ∈ {0, 1}n sampled from either D 1
3 or D 2
3 , we
need to ﬁgure out which distribution x is sampled from.

The intuition for an algorithm that is correct with high probability (over the corresponding
distributions) is same as Algorithm 42, so we directly present the the algorithm for the new
version of the problem above.

Algorithm 43 An average-case algorithm for GAPHAMMING
INPUT: x ∈ {0, 1}n sampled from either D 1
3 or D 2
3
OUTPUT: 0 if x was sampled from D 1
3 and 1 otherwise with probability at least 1 − ε

1: s ← 98 · ln(1/ε)

2: C ← 0

3: FOR j ∈ [s] DO

4: C ← C + x j

5: IF C < s/2 THEN

6: RETURN 0

7: RETURN 1

Note that unlike Algorithm 42, Algorithm 43 is a deterministic algorithm and the algorithm
might make an incorrect decision on certain speciﬁc inputs x that it receives.
Using pretty much the same analysis as in the proof of Lemma C.3.1, one can argue that:

Lemma C.3.2. Let x be a random sample from D 1
3 (D 2
3 resp.). Then with probability at least 1 − ε
(over the choice of x), Algorithm 43 outputs 0 (1 resp.)

(See Exercise C.13 for a proof.)

C.4 Efﬁcient Algorithms

A major focus of this book is to design algorithms that are efﬁcient. A somewhat smaller focus is
to argue that for certain problems efﬁcient algorithms do not exists (maybe with a well accepted
assumption that certain computational tasks are hard to accomplish efﬁciently). In this section,
we ﬁrst begin with the notion of efﬁcient algorithms that will be standard for this book and then

358

present a peek into how one might argue that a computational task is hard. To illustrate various
concepts we will focus on the following problem:

Given n linear equations over k variables (all over F2: i.e. all the variables are in {0, 1}
and all arithmetic operations are over the binary ﬁeld 4 F2) and an integer 0 ≤ s ≤ n,
we want to ﬁnd a solution to the systems of equations that satisﬁes at least s out
of the n equations. We will denote this problem as MAXLINEAREQ(k, n, s). We will
drop the arguments when we want to talk about the problem in general.

We choose the non-standard notation of k for number of variables and n for number of equa-
tions as they correspond better to problems in coding theory that we would be interested in.
An overwhelming majority of the algorithmic problems considered in this book will have
the following property: there are exponentially many possible solutions and we are interested
in a solution (or solutions) that satisfy a certain objective. For example, in the MAXLINEAREQ
problem, there are 2k possible solutions and we are interested in a solution that satisﬁes at least
s many linear equations. Note that such problems have a very natural exponential time algo-
rithm: generate all (the exponentially many) potential solutions and check if the current poten-
tial solution satisfy the objective. If it does, then the algorithm stops. Otherwise the algorithm
continues to the next solution. For example, Algorithm 44 instantiates this general algorithm
for the MAXLINEAREQ problem.

Algorithm 44 Exponential time algorithm for MAXLINEAREQ
INPUT: n linear equations over k variables and an integer 0 ≤ s ≤ n
OUTPUT: A solution in {0, 1}k that satisﬁes at least s of the equations or fail if none exists

1: FOR every x ∈ {0, 1}k DO

2: Let t be the number of equations the solution x satisﬁes

3: IF t ≥ s THEN

4: RETURN x

5: RETURN fail

It is not too hard to argue that Algorithm 44 runs in time O (kn2k ) (see Exercise C.14). We
point out two things that will expand into more detailed discussion on what is an efﬁcient algo-
rithm (and what is not):

1. A run time of Ω(2k ) is not efﬁcient for even moderate values of k: indeed for k = 100, the
number of steps of the algorithm exceeds the number of particles in the universe.

2. In the generic exponential time algorithm mentioned earlier, we made the implicit as-
sumption that given a potential solution we can “quickly" verify if the potential solution
satisﬁes the objective or not.

4In other words, addition is XOR and multiplication is AND.

359

Notwithstanding the fact that an exponential run time can become infeasible for moderate
input size, one might think that one cannot do better than Algorithm 44 to solve the MAXLIN-

EAREQ problem. In particular, the lack of any extra information other than the fact that we have
a system of linear equations on our hands seems to make the possibility of coming up with a
faster algorithm slim. However, looks can sometimes be deceptive, as we will see shortly.
Consider the special case of the MAXLINEAREQ problem: MAXLINEAREQ(k, n, n). In other
words, we want to see if there exists a solution x ∈ {0, 1}n that satisﬁes all the equations. Not
only is this is an interesting special case but it is also relevant to this book since this setting
corresponds to the error detection problem (Deﬁnition 1.3.4) for linear codes (Chapter 2)– see
Exercise C.15. It turns out this special setting of parameters makes the problem easy: one can
use Gaussian elimination to solve this problem in time O(kn2) (see Exercise C.16). For the case
of k = Θ(n) (which would be the most important parameter regime for this book), this cubic
run time is much faster than the exponential time Algorithm 44. In particular, any run time
of the form O(nc ) for some ﬁxed constant c would be much faster than the 2Ω(n) run time of
Algorithm 44 (for large enough n). Note that the appealing aspect of a run time of the form
O(nc ) is that when the input size doubles, the run time only increases by a constant (though
clearly we might be pushing the boundary of a practical deﬁnition of a constant for moderately
large values of c) as opposed to the exponential run time, where the run time on the new input
size is quadratic in the old run time.
In theoretical computer science, the notion of an efﬁcient algorithm is one that runs in time
O(N c ) on inputs of size N for some ﬁxed constant c ≥ 0: such algorithms are said to have poly-
nomial run time. In particular, a problem is said to be in the complexity class P if it admits
a polynomial time algorithm5. While one might debate the deﬁnition of P as capturing algo-
rithms that are efﬁcient in practice, it clearly seems to capture the difference between problems
that “need" exponential time algorithms and problems that have some inherent structure that
allows much faster algorithmic solutions (in this case polynomial time algorithm).

C.4.1 Computational Intractability

So far we have talked mainly about problems that admit efﬁcient algorithms. We now consider
the issue of how we talk about a problem being hard: e.g. can we somehow formally argue that
a certain problem cannot admit efﬁcient solutions? In particular, are there problems where the
generic exponential time algorithm discussed earlier is the best possible? To be more precise,
let us consider problems where given a potential solution one can in polynomial time deter-
mine whether the solution satisﬁes the objective or not. We call the class of such problems as
NP.6 For example, MAXLINEAREQ(k, n, s) is such a problem because given a potential solution
x, one can in time O(kn) verify whether it satisﬁes at least s out of the n solutions– see Exer-
cise C.17 and hence MAXLINEAREQ ∈ NP. Like the earlier special case of MAXLINEAREQ(k, n, n),

5The technical deﬁnition of P is a bit more nuanced: in particular it only considers problems with a binary
output but we will ignore this technical issue in this book.
6Again for the technical deﬁnition we need to only consider problems with binary output but we will ignore this
technicality.
 360

the more general problem MAXLINEAREQ(k, n, s) for s < n is also interesting from a coding the-
ory perspective: see Exercise C.18.
Thus, the question of whether there exists a problem where the earlier exponential time
algorithm is the best possible is essentially the same as showing P ̸= NP (see Exercise C.19).
While we are nowhere close to answer this fundamental question, we do know a way to identify
the “core" of hard problems in NP. Such problems (called NP-complete problems) have the
property that if any of them do not have a polynomial time algorithms then none of them do.
(Conversely if any of them do have a polynomial time algorithm then P = NP.) Note that this
implies if one assumes that P ̸= NP, then these NP-complete problems are hard problems since
they are not in P (which we consider to be the class of “easy" problems).
At ﬁrst blush, one might wonder how one would go about proving that such problems exist.
Proving the existence of such a problem is out of the scope of the book. However, we do want to
give an overview of how given one such speciﬁc problem that is NP-complete one might argue
that another problem is also NP-complete. The way to show such a result is to reduce the known
NP-complete problem (let us call this problem P1) to the other problem (let us call this problem
P2). Without going into the technical deﬁnition of a reduction, we present an informal deﬁni-
tion, which would be sufﬁcient for our purposes. A reduction is a polynomial time algorithm
(let us call it A1) that given an arbitrary instance x1 of P1 can produce in polynomial time an-
other instance x2 but this time for the problem P2 such that given the answer for problem P2 on
x2, one can in polynomial time exactly determine the answer of P1 on x1 (by another algorithm,
which let us call A2). There are two (equivalent) ways to think about such a reduction:

1. A reduction implies that to solve P1 in polynomial time, it is enough to “only" solve some
subset of instances for problem P2 (in particular, those inputs for P2 that are generated by
A1 on all possible input instances of P1). In other words, P2 is “harder" to solve than P1.
Since the problem P1 is a hard problem, P2 is also a hard problem.

2. Let us for the sake of contradiction assume that there exists a polynomial time algorithm
A3 that solves P2 on all instances (i.e. P2 is easy). Then one can construct a polynomial
time algorithm to solve P1 as follows. Given an arbitrary input x1 for P1, ﬁrst use A1 to
generate an input x2 for P2. Then use A3 to solve P2 on x2 and then convert the answer of
P2 on x2 to the answer of P1 on x1 by using A2. Note that this is a polynomial time algo-
rithm and is a correct algorithm. Thus, we have proved that P1 is easy, which contradicts
our assumption that P1 is hard.

To make the concept of reduction a bit less abstract we outline a reduction from a known
NP-complete problem to our MAXLINEAREQ problem.7 In particular, the following problem is
known to be NP-complete

Given a graph G = (V, E ) with |V | = k and |E | = n and an integer 0 ≤ s ≤ n, does there
exist a cut of size at least s. In other words, does there exist a subset S ⊂ V such that
the number of edges with one end point in S and the other in V \ is at least s? We
will call this the MAXCUT(k, n, s) problem.

7We assume that the reader is familiar with the mathematical concept of graphs, where we do not mean graphs
in the sense of plots.
 361

Algorithm 45 is the algorithm A1 of the reduction from MAXCUT(k, n, s) to MAXLINEAREQ(k, n, s).

Algorithm 45 Reduction from MAXCUT to MAXLINEAREQ
INPUT: An instance for MAXCUT(k, n, s): a graph G and an integer s
OUTPUT: An instance of MAXLINEAREQ(k ′, n′, s′)

1: k ′ ← k, n′ ← n, s′ ← s

2: FOR every vertex i ∈ V DO

3: Add a variable xi to the set of variables

4: FOR every edge (i , j ) ∈ E DO

5: Add a linear equation xi + x j = 1 to the system of equation

Further, the algorithm A2 is simple: given a solution (x1, . . . , xk ) to the instance for MAXLINEAREQ(k, n, s)
problem, consider the cut S = {i ∈ V |xi = 1}. It can be checked that this algorithm and Algo-
rithm 45 forms a valid reduction. (See Exercise C.20.)

C.5 Exercises

Exercise C.1. Prove that f (N ) is O(g (N )) (as per Deﬁnition C.1.1) if and only if

lim
N →∞ f (N )
g (N ) ≤ C ,

for some absolute constant C .

Exercise C.2. Prove that f (N ) is Ω(g (N )) (as per Deﬁnition C.1.2) if and only if

lim
N →∞ f (N )
g (N ) ≥ C ,

for some absolute constant C .

Exercise C.3. Prove that f (N ) is Θ(g (N )) (as per Deﬁnition C.1.3) if and only if

lim
N →∞ f (N )
g (N ) = C ,

for some absolute constant C .

Exercise C.4. Prove that f (N ) is o(g (N )) (as per Deﬁnition C.1.4) if and only if

lim
N →∞ f (N )
g (N ) = 0.

Exercise C.5. Prove that f (N ) is ω(g (N )) (as per Deﬁnition C.1.5) if and only if

lim
N →∞ f (N )
g (N ) = ∞.

362

Exercise C.6. Prove Lemmas C.1.1, C.1.2 and C.1.3.

Exercise C.7. Prove or disprove the following for every α ∈ {O, Ω, Θ, o, ω}:

Let f (N ) be α(h(N )) and g (N ) be α(h(N )). Then f (N ) · g (N ) is α(h(N )).

Exercise C.8. Say there exists a randomized algorithm A that is correct with probability 1
2 +δ for
some δ > 0 with runtime T (N ). Then show that for every ε > 0, there exists another randomized

algorithm that is correct with probability 1 − ε with runtime O ( log(1/ε)
δ · T (N ))
.

Hint: Repeat A multiple times and pick one among the multiple outputs. For analysis use the Chernoff bound

(Theorem 3.1.6).

Exercise C.9. Assume that there is a randomized algorithm A , which one when provided with
an input from a distribution D, is correct with probability p (where the probability is taken over
both D and internal randomness of A ). Then show that there exists a deterministic algorithm
that is correct with probability at least p (where the probability is now only taken over D) with
the same run time as A .

Exercise C.10. Argue that any correct deterministic algorithm that solves the GAPHAMMING
problem needs a run time of Ω(n).

Hint: Argue that any correct deterministic algorithm needs to read Ω(n) bits of the input.

Exercise C.11. Argue that Algorithm 42 runs in time O(log(1/ε)).

Exercise C.12. Prove that for every x ∈ {0, 1}n such that w t (x) ≥ 2n/3, Algorithm 42 outputs 1
with probability at least 1 − ε.

Exercise C.13. Prove Lemma C.3.2 and that Algorithm 43 runs in time O(log(1/ε)).

Exercise C.14. Argue that Algorithm 44 runs in time O (kn2k ). Conclude that the algorithm runs
in time 2
O(n).

Exercise C.15. Show that if any MAXLINEAREQ(k, n, n) problem can be solved in time T (k, n),
then the error detection for any [n, k]2 code can be solved in T (k, n) time.

Hint: The two problems are in fact equivalent.

Exercise C.16. Argue that the problem MAXLINEAREQ(k, n, n) can be solved in time O(kn2).

Exercise C.17. Show that given a system of n linear equation on k variables over F2, there exists a
O(kn) time algorithm that given a vector x ∈ {0, 1}n can compute the exact number of equations
x satisﬁes.

Exercise C.18. Consider the following problem called the BOUNDED DISTANCE DECODING prob-
lem. Given a code C ⊆ {0, 1}n, a vector y ∈ {0, 1}n and an integer 0 ≤ e ≤ n (called the error radius),
output any codeword c ∈ C such that ∆(c, y) ≤ e (or state that no such codeword exists).
Prove that if any MAXLINEAREQ(k, n, s) problem can be solved in time T (k, n, s), then one
can solve the BOUNDED DISTANCE DECODING problem for any [k, n]2 linear code with error
radius n − s.
 363

Exercise C.19. Argue that showing P ̸= NP is equivalent to showing that NP \ P ̸= ;.

Exercise C.20. Argue that Algorithm 45 and the algorithm A2 deﬁned just below it are correct
and run in polynomial time.

C.6 Bibliographic Notes

The full suite of asymptotic notation in Section C.1 was advocated for analysis of algorithms by
Knuth [62]. The Big-Oh notation is credited to Bachmann [6] form a work in 1894 and the little-
oh notation was ﬁrst used by Landau [65] in 1909. A variant of the Big-Omega notation was
deﬁned by Hardy and Littlewood [53] in 1914 though the exact deﬁnition in Section C.1 seems
to be from [62]. The Theta and little omega notation seem to have been deﬁned by Knuth [62]
in 1976: Knuth credits Tarjan and Paterson for suggesting the Theta notation to him.
The choice to use worst-case run time as measure of computational efﬁciency in the RAM
model as well as only considering the asymptotic run time (as opposed to more ﬁne grained
analysis as advocated by Knuth) seem to have been advocated by Hopcroft and Tarjan: see
Tarjan’s Turing award lecture for more on this [99].
Cobham [18] and Edmonds [26] are generally credited with making the ﬁrst forceful case
for using P as the notion of efﬁciently solvable problems. Somewhat interestingly, Peterson’s
paper on decoding of Reed-Solomon codes [80] that predates these two work explicitly talks
about why a polynomial time algorithm is better than an exponential time algorithm (though
it does not explicitly deﬁne the class P). The notion of NP (along with a proof of the existence
of an NP-complete problem) was deﬁned independently by Cook [19] and Levin [67]. This no-
tion really took off when Karp showed that 21 natural problems where NP-complete (including
the MAXCUT problem) [60]. For more historical context on P and NP including some relevant
historical comments, see the survey by Sipser [93].
The ﬁrst randomized algorithms is generally credited to Rabin [81]. However, an earlier
work of Berlekamp on factoring polynomials presents a randomized algorithm (though it is not
stated explicitly as such) [9].
This chapter gave a very brief overview of topics that generally span multiple classes. For
further readings, please consult standard textbooks on the subjects of (introductory) algorithms
and computational complexity as well as randomized algorithms.

364

Appendix D

Basic Algebraic Algorithms

D.1 Executive Summary

In this appendix we include some basic facts about abstract algebra that were used throughout
the book. Readers who are comfortable with their background in algebra should feel free to skip
it entirely. However, this background should include both aspects introduced by ﬁniteness —
most ﬁelds we work with are ﬁnite, and so are the vector spaces deﬁned over them — and com-
putation — the mere existence of a nice algebraic structure is not good enough for us, we need
to know how to carry out basic, and not so basic operations over these structures efﬁciently. If
you are not very comfortable with these settings you will ﬁnd the appropriate sections of this
appendix more useful. The opening paragraph of each section summarizes the main aspects
covered in the section and the reader may use them to decide if they wish to read further.
Some of the material in this appendix appears earlier in the book (e.g. Sections 2.1, 2.2
and 5.1). Finally, this coverage of algebra in this appendix is not exhaustive and the reader is
referred to the book by Lidl and Niederreiter [69] for more matetrial (and proofs) on ﬁnite ﬁelds
and the book by Shoup for more details on the basic algebraic algorithms [91].

D.2 Groups, Rings, Fields

The title of this section says it all. We cover, very tersely, the deﬁnition of a group, a ring, and a
ﬁeld.
We begin with some terminology. We consider binary operations over some set of elements.
Given a set X such a binary operator would be a function ◦ : X × X → X , and we usually use
a ◦ b to denote ◦(a, b), for a, b ∈ X . We say the operator ◦ is associative if a ◦ (b ◦ c) = (a ◦ b) ◦ c,
for every a, b, c ∈ X . For associative operations it is customary to drop the parenthesis. We say
the operator ◦ is commutative if a ◦ b = b ◦ a for every a, b ∈ X . We say an element e ∈ X is an
identity for ◦ if a ◦ e = e ◦ a = a for every a ∈ X . Identities are, by deﬁnition, unique if they exist,
since if e1, e2 ∈ X were identities, we would have e1 = e1 ◦ e2 = e2. Given a ∈ X and operator ◦
with inverse e we say that a is is invertible with respect to ◦ if there exists an element a−1 ∈ X
such that a ◦ a−1 = a−1 ◦ a = e. Often ◦ will be clear from context in which case we will refer to a

365

as simply invertible.

Deﬁnition D.2.1 (Group). Given a set G and a binary operation ◦ over G, we say that (G, ◦) is a
group if ◦ is associative, has an identity, and every element of G is invertible. A group (G, ◦) is
said to be an abelian group if ◦ is also commutative.

Examples of groups include the integers with addition, the non-zero rationals with multi-
plication and the set of permutations (one-to-one functions) on any ﬁnite set under the com-
position operation.

Deﬁnition D.2.2 (Ring). A ﬁnite set R with two binary operations + and · are said to form a ring
if (1) (R, +) form an abelian group, (2) · is associative and has an identity and (3) · distributes over
+, i.e., for every a, b, c ∈ R we have a · (b + c) = (a · b) + (a · c) and have (b + c) · a = (b · a) + (c · a).
The ring (R, +, ·) is said to be a commutative ring if · is commutative.

Examples include the integers over addition and multiplication (a commutative ring) and
the set of k × k integer matrices (for any positive integer k) under matrix addition and matrix
multiplication (which forms a non-commutative ring for k ≥ 2).

Deﬁnition D.2.3 (Field). A set F with operations + and · forms a ﬁeld if (F, +, ·) is a commutative
ring, and (F \ {0}, ·) is a group where 0 denotes the identity for +.

Examples of ﬁelds include the rationals, the reals, the complexes (all under addition and
multiplication) and (more interestingly to us) the integers modulo any prime number p (see
Lemma 2.1.2 for the latter).
It is customary in rings and ﬁelds to let 0 denote the additive identity, 1 the multplicative
identity and to let −a denote the additive inverse of a and a−1 the multiplicative inverse of a. It
is also customary to abbreviate a + (−b) to a − b.

D.3 Polynomials

In this section we will introduce polynomial rings, mention when they satisfy the unique factor-
ization property, describe the ‘remainder algorithm’, and describe the evaluation map and the
polynomial distance property (where the latter is a re-statement of the degree mantra (Propo-
sition 5.2.3)).

Deﬁnition D.3.1 (Formal Polynomials). Let (R, +, ·) be a commutative ring with identity 0. The
set of formal polynomials over R in indeterminate X , denoted R[X ], is given by ﬁnite formal
sums R[X ] = {∑d
i =0 fi X i | f0, . . . , fd ∈ R; d ∈ Z≥0}, under the equivalence ∑d
i =0 fi X i = ∑d −1
i =0 fi X i

if fd = 0. (The term formal refers to the fact that the summation, and the terms X i are just
formal symbols and do not have operational meaning, yet. So really polynomials are just ﬁnite
sequences of elements from R under the equivalence ( f0, . . . , fd , 0) ∼= ( f0, . . . , fd ).)

Basic terminology The elements fi are referred to as the coefﬁcients of f , the symbols X i as
the monomials of f and the product fi X i as the terms of f . For f = ∑d
i =0 fi X i , its degree,
denoted degX ( f ) or simply deg( f ), is the largest integer e such that fe ̸= 0.

366

Addition The sum of two polynomials f = ∑d
i =0 fi X i and g = ∑d
i =0 gi X i , denoted f + g , is the
polynomial ∑d
i =0( fi + gi )X i . (Note that by padding the coefﬁcients of f and g with zeroes
we can always arrange it so that they have the same number of terms.)

Multiplication Finally, the product of f = ∑d
i =0 fi X i g = ∑e
i =0 gi X i , denoted f · g (or sometimes

simply f g ), is given by ∑d +e
i =0
 (∑e
j =0 fi − j · g j ) X i .

The following proposition follows immediately from the deﬁnitions above.

Proposition D.3.1. For every commutative ring R, R[X ] is a commutative ring under the sum
and product of polynomials.

In fact R inherits many properties of R and in particular the notion of “unique factorization”
which we describe next.

Deﬁnition D.3.2 (Unique Factorization Domains). Let R be a commutative ring. An element
u ∈ R is said to be a unit if it has a multiplicative inverse in R. Elements a and b are said to be
associates if there exists a unit u such that a = b · u. (Note that being associates is an equivlence
relationship.) Element a ∈ R is said to be irreducible if a = b · c implies either b or c is a unit.
A factorization of a ∈ R is a sequence b1, . . . , bk such that a = b1 · b2 · · · bk and none of the bi ’s
are units. The bi are referred to as the factors of a in this factorization. Ring R is a factorization
domain if for non-zero every a ∈ R that is not a unit, there is a ﬁnite bound ka such that every
factorization of a has at most ka factors. A factorization domain R is a unique factorization
domain (UFD) if every non-zero, non-unit element has a unique irreducible factorization, upto
associates. I.e., if a = b1 · · · bk = c1 · · · cℓ and the bi ’s and c j ’s are irreducible, then k = ℓ and there
exists a bijection π : [k] → [ℓ] such that bi and cπ(i ) are associates, for every i ∈ [k].

Since every non-zero element of a ﬁeld is a unit, every ﬁeld is a UFD.

Proposition D.3.2. Every ﬁeld is a UFD.

A central result in basic commutative algebra is the following lemma of Gauss.

Lemma D.3.3 (Gauss). If R is a UFD, then so is R[X ].

We omit the proof of the above lemma here, but point out its implications. It allows us to
build many interesting rings from a simple base case, namely a ﬁeld. Given a ﬁeld F, F[X ] is
a UFD. So is (F[X ])[Y ]. Now we could have gone in the other direction and created the ring
(F[Y ])[X ] and this would be a UFD too. However if X and Y commute (so X Y = Y X ) then the
rings (F[X ])[Y ] and (F[Y ])[X ] are isomorphic under the isomorphism that preserves F and sends
X → X and Y → Y . So we tend to compress the notation and refer to this ring as F[X , Y ], the
ring of “bivariate” polynomials over F. Rings of univariate and mutlivariate polynomials play a
central role in algebraic coding theory.
We now turn to the notion of polynomial division with remainder that lead us to some im-
portant notions associated with polynomials.
Let f ∈ R[X ] and let f = ∑d
i =0 fi X i with fd ̸= 0. f is said to be monic if fd is a unit in R.

367

Proposition D.3.4. Given a monic polynomial f , and general polynomial p there exists a unique
pair of polynomials q (for quotient) and r (for remainder) such that p = q · f + r and deg(r ) <
deg( f ).

See Exercise D.1 for a proof.
The function p 7→ f (q, r ) described is often referred to as the ‘division algorithm’ (since it is
the outcome of long division). A special case that is of great interest to us is when f = X − α for
α ∈ R. In this case the remainder is polynomial of degree at most 0, and so can be associated
with an element of R. Denote this element p(α) (since it depends only on p and α) and we
get the “evaluation” map which maps elements of R[X ] × R to R. The remainder p(α) can be
worked out explicitly and is given by the simple form below (where the uniqueness follows from
Proposition D.3.4).

Proposition D.3.5. Given p = ∑d
i =0 pi X i ∈ R[X ] and α ∈ R, let p(α) = ∑d
i =0 pi α
i . Then there
exists a unique q ∈ R[X ] such that p = q · (X − α) + p(α). It follows that p(α) = 0 if and only if
X − α divides p(X ).

Finally using Proposition D.3.5 and the fact that F[X ] is a UFD, we get the following the
following central fact about univariate polynomials.

Lemma D.3.6 (Polynomial Distance Lemma). Let f ̸= g ∈ F[X ] be polynomials of degree at most
d . Then there exist at most d elements α ∈ F such that f (α) = g (α).

Proof. Let h = f − g . We have h is non-zero and of degree at most d . Let S = {α| f (α) = g (α)}.
Then we have (X − α) divides h for every α ∈ S. Furthermore, by the unique factorization prop-
erty we have ˜h = ∏
α∈S(X −α) divides h. But if ˜h divides h, then deg( ˜h) ≤ deg(h) and deg( ˜h) = |S|.
We conclude |S| ≤ d .

D.4 Vector Spaces

In this section we introduce vector spaces over ﬁelds and describe two basic views of describing
a ﬁnite dimensional vector space: ﬁrst via its generators (and the generator matrix) and next via
constraints on the vector space (and its parity check matrix). We ﬁrst start with a quick overview
of matrices and the corresponding notation and then move on to vector spaces.

D.4.1 Matrices and Vectors

In this book, a vector of length n over the ﬁeld F (i.e. x ∈ Fn) is a row vector
1. E.g., we have
x = (
0 1 3 4 0) ∈ F4
5. Given two vectors u, v ∈ Fn, their inner product is deﬁned as

〈u, v〉 = n∑

i =1 ui · vi ,

1We acknowledge that this is different from the usual assumption in linear algebra that all vectors are column
vectors. We are assuming row vectors to be consistent with how message vectors are assumed to be row vectors in
coding theory.
 368

where the multiplication and addition are over F.
A matrix M ∈ Fk×n is a two-dimensional array/vector, where we refer to the (i , j )’th entry
(for (i , j ) ∈ [k] × [n]) as Mi , j (or Mi j if the two indices are clear without being separated by a
comma). We will use Mi ,· as the i ’th row and M·, j as the j th column of M respectively.
So e.g. consider G ∈ F2×3
3 as follows:
 G = (
1 0 1
0 2 1
) .

In the above G1,2 = 2, G1,· = (
1 0 1) and G·,2 = (
0
2
)
.

The transpose of a matrix M ∈ Fk×n, denoted by M T is an n × k matrix over F such that for
any ( j , i ) ∈ [n] × [k], we have M T
j ,i = Mi j .

Note that if k = 1, then the above says that for a row vector x ∈ Fn, its transpose xT is a column
vector.
The product of two matrices A ∈ Fk×n and B ∈ Fn×m is a matrix C ∈ Fk×m such that for any
(i , j ) ∈ [k] × [m], we have Ci , j = 〈Ai ,·, B·, j 〉 .

D.4.2 Deﬁnition and Properties of Vector Spaces

This section will repeat some of the material from Section 2.2. We begin with the deﬁnition of a
vector space:

Deﬁnition D.4.1 (Vector Space). Over a ﬁeld F, a vector space is given by a triple (V, +, ·) where
(V, +) is a commutative group and · : F × V → V distributes over addition, so that α · (u + v) =
α · u + α · v for every α ∈ F and u, v ∈ V . It is customary to denote the identity of the group (V, +)
by 0 and to refer to V as an F-vector space.

The simplest example of an F-vector space is Fn, whose elements are sequences of n ele-
ments of F. The sum is coordinate-wise summation and product is “scalar” product, so if u =
(u1, . . . , un), v = (v1, . . . , vn) and α ∈ F then u+v = (u1 +v1, . . . , un +vn) and α·u = (α·u1, . . . , α·un).
Essentially these are the only vector spaces (as we will make precise soon), but representations
of the vectors is important to us, and will make a difference.

Deﬁnition D.4.2 (Dimension of a vector space). A sequence of vectors v1, . . . , vk ∈ V are said to
be linearly independent if ∑k
i =1 βi · vi = 0 implies that β1 = · · · = βk = 0. v1, . . . , vk ∈ V are said to
linearly dependent otherwise.
V is said to be ﬁnite dimensional of dimension k if every sequence of k +1 vectors from V is
linearly dependent and there exists a sequence of length k that is linearly independent.
A linearly independent set v1, . . . , vk ∈ V is said to form a basis for V if V has dimension k.

Every F-vector space of dimension k is isomorphic to Fk as described by the following propo-
sition.
 369

Proposition D.4.1. If v1, . . . , vk for a basis for an F-vector space V , then V = {∑k
i =a βi ·vi |β1, . . . , βk ∈
F} and the map (β1, . . . , βk ) 7→ ∑k
i =1 βi · vi is an isomorphism from Fk to V .

The point we wish to stress now is that even though all vector spaces are isomorphic, dif-
ferent spaces do lead to different codes with different error-correction properties, and these
properties are not preserved by such isomorphisms. So not all k-dimensional vector spaces
are identical for our purposes. We will specially be interested in k-dimensional vector spaces
contained in Fn, and how these can be represented succinctly in matrix form.

Deﬁnition D.4.3 (Generator Matrix, Parity Check Matrix). A matrix G ∈ Fk×n is said to be a gen-
erator matrix of an F-vector space V ⊆ Fn if the rows of G are linearly independent in Fn and
V = {x · G|x ∈ Fk }. The rows of G form a basis of V . A matrix H ∈ Fn×(n−k) is said to be a par-
ity check matrix of an F-vector space V ⊆ Fn if the columns of H are linearly independent and
V = {y ∈ Fn|H · y
T = 0}. Given a vector space V with parity check matrix H , its dual space, de-
noted V ⊥, is the vector space generated by the transpose of H , i.e., V ⊥ = {x · H T |x ∈ Fn−k }.

Our goal below is to show that every space has a generator matrix and a parity check matrix.
The former is obvious from deﬁnitions. If V ⊆ Fn is a k-dimensional vector space, then it has
a basis v1, . . . , vk and if we build a matrix G with these vectors as its rows, then G satisﬁes the
conditions of the generator matrix.
We sketch the idea for construction of a parity check matrix. We say that a k × k matrix R
forms a row operation if Ri i = 1, and Ri j = 0 for all must at most one pair i ̸= j ∈ [k]. We say that
˜G is obtained from G by row operations, denoted G ❀ ˜G, if ˜G = Rm ·Rm−1 · · · R1 ·G where the Ri ’s
are row operations. Note that if G is a generator matrix for V then so is ˜G. Gaussian elimina-
tion allows us to “simplify” G till its columns are special, and in particular after permuting the
columns ˜G would look like [Ik |A] where Ik denotes the k × k identity matrix. Assume for sim-
plicity that ˜G = [Ik |A] (without permuting columns). Now let H be given by H T = [−AT |In−k ].
It can be veriﬁed that ˜G · H = 0 and so G · H = 0. Furthermore all columns of H are linearly in-
dependent and so H satisﬁes the conditions of the parity check matrix of V . We conclude with
the following.

Proposition D.4.2. If V ⊆ Fn is a k-dimensional vector space then it has a generator matrix G ∈
Fk×n and a parity check matrix H ∈ Fn×(n−k). Furthermore its dual V ⊥ is generated by H T , has
dimension n − k, and has G T as its parity check matrix. Finally (V ⊥)⊥ = V .

Before concluding we mention one important difference from the case of orthoganility of
real vectors. For vector spaces over ﬁnite ﬁelds it is possible that there are non-zero vectors in
V ∩ V ⊥ and indeed even have V = V ⊥. (See Exercise 2.29 for more on this.)

D.5 Finite Fields

In this section we describe the existence and uniqueness of ﬁnite ﬁelds. We also describe the
basic maps going from prime ﬁelds to extensions and vice versa. Parts of this section will repeat
material from Section 2.1 and 5.1.
 370

D.5.1 Prime Fields

We start by describing a ﬁeld of size p, for any prime number p. Let Zp be the set of integers
{0, . . . , p − 1}. For integer a and postive integer b, let a mod b denote the unique integer c in
Zp such that b divides a − c. Let +p be the binary operation on Zp that maps a and b to (a + b)
mod p. Let ·p map a and b to (ab) mod p. We have the following (see Section 2.1 for a proof).

Proposition D.5.1. (Zp , +p , ·p ) form a ﬁeld of cardinality p.

Given a ﬁnite ﬁeld F, its characteristic, denoted char(F), is the smallest positive integer p
such that p · 1 = 1 + 1 + · · · + 1 = 0. (See Exercise D.2 for why such a ﬁnite characteristic exists.)

Proposition D.5.2. For every ﬁnite ﬁeld F, char(F) is a prime. Furthermore, F is a Zp -vector space,
where p = char(F). Thus F has cardinality p n for prime p and integer n.

Proof. Let p = char(F). We ﬁrst note that p is the smallest integer such that p · a = 0 for any
non-zero element of F. This is so since p ·a = p ·1·a = 0, and if p ·a = 0 then so is p ·a ·a−1 = p ·1.
Next we note that if p = qr then for the element w = q ·1 ∈ F, we have w ·r = 0 which contradicts
the minimality of p.
Next we note that (F, +, ◦) satisfy the conditions of a Zp -vector space where i ◦a = (a +· · ·+a)
(i times), for i ∈ Zp and a ∈ F. We conclude that |F| = p n where n is the dimension of the vector
space (F, +, ◦) and p = char(F).

We conclude now by claiming that Zp is the unique ﬁeld of cardinality p.

Proposition D.5.3. For any prime p, there is a unique ﬁeld of cardinality p upto isomorphism.

Proof. Let F be a ﬁeld of cardinality p. By Proposition D.5.2 we have that char(F) = p. It can be
veriﬁed that the map 1F → 1 extends to an isomorphism (see Exercise D.3).

The uniqueness of the ﬁeld of cardinality p allows us to call it Fp in the future.

D.5.2 Extension ﬁelds and subﬁelds

We now move towards determining when non-prime ﬁelds exists. While the answer is simple
(they exist for every number of the form p n for prime p and positive integer n), proving when
they exist requires some structural understanding of how ﬁelds behave.
We will ﬁrst present a basic property of all ﬁnite ﬁelds that is crucial when working with
ﬁelds.
We recall a basic result about ﬁnite groups (see Exercise D.4 for a proof for the abelian case).

Proposition D.5.4. If (G, ·) is a ﬁnite group with identity 1, then for every a ∈ G, we have a|G| = 1.

Proposition D.5.5. Let F be a ﬁeld of cardinality q. The every element α ∈ F is a root of the
polynomial X q − X and so X q − X = ∏
α∈F(X − α).

371

Proof. If α = 0, then it is trivial to see that is a root of X q − X . If α ̸= 0, then it is a member of
a group (F \ {0}, ·) and so by Proposition D.5.4, satisﬁes α
|F\{0}| = 1. Thus, αq−1 = 1, and ﬁnally
αq = α, as desired.

Let K be a ﬁeld and F ⊆ K be a set that is closed under addition and multiplication. Then
F is itself a ﬁeld and we denote if F ✁ K to denote that it is a subﬁeld of K . We say K ✄ F to
denote that K extends F.

Proposition D.5.6. If K ✄F then K is an F-vector space and so |K | = |F|n where n is the dimen-
sion of K as an F-vector space. Furthermore there is a unique copy of F in K .

Proof. The fact that K is a vector space follows from the deﬁnitions, and thus the claim about
its cardinality. The fact that there is a unique copy of F follows from the fact that the elements
of F satisfy X q − X = 0, where q = |F| and there can be at most q roots of this polynomial.

D.5.3 Existence of Finite Fields

In what follows we will rely heavily on the modular reduction of polynomials. Following the
notation of previous sections, for ﬁeld F and f , g ∈ F[X ], we let f mod g be the remainder when
f is divided by g - so deg( f mod g ) < deg(g ) and g divides f − ( f mod g ). Let f +g h = ( f + h)
mod g and let f ·g h = ( f h) mod g . Recall that an irreducible polynomial in Fq [X ] is one that
does not have any non-trivial factor (recall Deﬁnition 5.1.4).

Proposition D.5.7. Let F be a ﬁnite ﬁeld of cardinality q and let g ∈ F[X ] be an irreducible poly-
nomial of degree n. Then (F[X ]/g , +g , ·g ) form a ﬁeld of cardinality q n.

Essentially all ﬁelds can be obtained in the above manner, but to prove this fact, we need to
prove that there is an irreducible polynomial of degree n over Fp for every p and unfortunately
this proof is not much simpler than proving the existence of a ﬁeld of cardinality p n. So we
prove the existence directly, or rather sketch a proof of this fact.
The rough idea of the proof is as follows: First we establish that every polynomial f ∈ F[X ]
splits completely (into linear factors) over some extension K of F. To do this we work slowly,
working away at one irreducible factor of f at a time. If g is such an irreducible factor, we
consider the ﬁeld2 L = F[Z ]/g (Z ) and note that Z is a root of g ,3 and hence of f , in L and so f
splits more in L. We continue this process till f splits completely in some ﬁeld K .
Now we work with a very special polynomial f , namely f (X ) = X pn − X in the ring Fp [X ] and
let K be a ﬁeld in which f splits completely. Now let S ⊆ K be the set S = {α ∈ K | f (α) = 0}.
We note that this set, miraculously, is closed under addition and multiplication. The latter is
easy: f (α) = 0 if and only if αpn = α. So if f (α) = f (β) = 0 then αpn = α and βpn = β and so
(αβ)pn = αpn βpn = αβ and so αβ ∈ S. For the former we explicitly highlight another crucial fact
in ﬁnite ﬁelds.

2Recall Theorem 5.1.1.
3This is because g (Z ) ≡ 0 in L.
 372

Proposition D.5.8. Let K be a ﬁeld of characteristic p and let A, B ∈ K [X , Y ]. Then for all
positive integers n we have (A + B )pn = Apn + B pn .

The proof of the lemma above follows immediately from the fact that (p
i ) mod p is 0 unless
p divides i (see Exercise D.5). And while the lemma is stated for very general A and B , we only
need it for A, B ∈ K itself. However we state it generally since it is fundamental to working over
extension ﬁelds and indeed we will see a few applications later.
Returning to our quest to prove that S is closed under addition, let us apply the above propo-
sition to α, β ∈ S. We get that (α + β)pn = αpn + βpn = α + β and so S is closed under addition as
well. What we will show next is that S has exactly p n elements and so is a ﬁeld of size p n (it is
closed under addition and multiplication and the rest of the properties follow from the fact that
S is a subseteq of a ﬁeld K ).
First note that S has all roots of f . We note further that f has no multiple roots. In general
this is proved by looking at derivatives etc., but in this case we can do it by inspection. We wish
to show that (X − α)2 does not divide X pn − X , but this is the same as showing that Z 2 does not
divide (Z +α)pn −(Z +α) = Z pn −Z +αpn −α, but the latter polynomial has a coefﬁcient of −1 ̸= 0
for Z and so is not divisible by Z 2. We conclude that since S has all roots of X pn − X and this
polynomial has p n distinct roots, and so |S| ≥ p n. On the other hand since every element of S
is a root of X pn − X and this polynomial has at most p n roots, we conclude that |S| = p n and so
there exists a ﬁeld of cardinality p n. Thus we get the following theorem (the ﬁrst part follows
from Proposition D.5.2 and the second part follows from Proposition D.5.7).

Theorem D.5.9. If F is a ﬁnite ﬁeld, then it has charatestic p for some prime p and its cardinality
is p n for positive integer n. Conversely, for every prime p and positive integer n, there is a ﬁeld of
cardinality p n.

D.5.4 Uniqueness of ﬁnite ﬁelds

We start by proving that every ﬁnite ﬁeld has a multiplicative generator. To do so we need to
understand cyclic groups a bit better.
The cyclic group of order n is the group Zn = {0, . . . , n − 1} with addition modulo n being
the binary operation. This group clearly has an element of order n (namely the number 1). Let
N =(G, m) denote the number of elements of order exactly m in G and let N (G, m) denote the
number of elements of order dividing m in G. We have N (G.m) = ∑
k|m N =(G, k). For the cyclic
group, we have for every k|n, N (Zn, k) = k and N =(Zn, k) ≥ 0. (The latter is trivial and for the
former see Exercise D.6.)
We now turn to understanding (F∗, ·) the group of non-zero elements of F under multiplica-
tion.

Lemma D.5.10. Let q = |F| and n = q − 1. We claim that for every k dividing n, N (F∗, k) =
N (Zn, k) and N =(F∗, k) = N =(Zn, k).

Proof. The claim is straightforward for N (F∗, k). We have that every α ∈ F∗ is a root of of the

373

polynomial X n − 1 and since X k − 1 divides4 X n − 1, k elements of F∗ must be roots of this
polynomial also. We thus have N (F∗, k) = k = N (Zn, k).
For the claim about N =(F∗, k), we use induction and the inductive formula. We have ∑ℓ|k N =(F∗, ℓ) =
N (F∗, k) = k = N (Zn, k) = ∑ℓ|k N =(Zn, ℓ). But since by induction we have N =(F∗, ℓ) = N =(Zn, ℓ)
for ℓ < k, we may conclude that the remaining term N =(F∗, k) = N =(Zn, k).

We say that an element ω ∈ F is primitive if ωi ̸= 1 for i < |F|−1 and ω|F|−1 = 1. Since N =(F∗, n)
counts the number of primitive elements, Lemma D.5.10 implies that the number of primi-
tive elements is at least one. Indeed, if p is the smallest prime divisor of n, then we have that
N =(F∗, n) = N (F∗, n) − N (F∗, n/p) − N (F∗, p) = n − n/p − p > 0, assuming p < n/p. Otherwise if
n = p 2, then we have N =(F∗, n) = N (F∗, n) − N (F∗, p) = n − p > 0. If n itself is a prime then we
have N =(F∗, n) = N (F∗, n) = n > 0.

Proposition D.5.11. Every ﬁnite ﬁeld F has a primitive element. Consequently the multiplicative
group is cyclic.

We now describe a weaker form of special element in F. Let K extend F. We say that α ∈ K
is an F-generator for K if for every element β ∈ K there is a polynomial p ∈ F[X ] such that
β = p(α).

Proposition D.5.12. Let K be a ﬁnite ﬁeld and let ω be a primitive element in K . Then for every
subﬁeld F ✁ K we have that ω is an F-generator of K . As a consequence, for every K ✄ F there is
an F-generator in K .

Proof. Consider the lowest degree polynomial p ∈ F[X ] such that p(ω) = 0. Let |F| = q and
|K | = q n.
We claim that deg(p) = n. If deg(p) > n, we have that 1, ω, ω2, . . . , ωn are linearly indepen-
dent over F and so K has size strictly larger than q n. Now if deg(p) < n, then consider the
polynomials X , X 2, X 3, . . . , X q n −1 modulo p ∈ F[X ]. Since we have only q deg(p) options for the
residues, two of these must be equal modulo p and so there exist i ̸= j and f ∈ F[X ] such that
X i = X j + p · f . Substituting X = ω yields ωi = ω j + p(ω) f (ω) = ω j . But this contradicts the
assumption that ω is a primitive element.
Finally, note that any element β ∈ K can be written as the polynomial q j mod p(X ) evalu-
ated at X = ω for some 0 ≤ j < q n.

Generators are useful in that they show that the only way to construct ﬁeld extensions is via
irreducible polynomials.

Proposition D.5.13. Let K ✄ F and let α be an F-generator of K . Then, if p is the minimal
polynomial in F[X ] such that p(α) = 0, we have p is irreducible and K is isomorphic to F[X ]/p.

Proof. Irreducibility of p follows from its minimality (see Exercise D.8). The isomorphism is
obtained by ﬁxing F ✁ K and letting α 7→ X . We leave it to the reader to verify that this extends
to an isomorphism (uniquely)– see Exercise D.9.

4See Exercise D.7.
 374

We are almost ready to prove uniqueness of ﬁnite ﬁelds. We need one more fact about irre-
ducible polynomials to do so.

Proposition D.5.14. If f ∈ Fp [X ] is irreducible of degree n, then f divides X pn − X .

Proof. Consider the ﬁeld K = Fp [X ]/( f ). This is a ﬁeld of cardinality p n and so every element
α ∈ K satisﬁes αpn = α. In particular X ∈ K also satisﬁes this, implying that X pn − X = 0(
mod f ) and so f divides X pn − X .

We now turn to proving uniqueness of ﬁnite ﬁelds.

Theorem D.5.15. For every prime p and integer n, there is a unique ﬁeld of cardinality p n up to
isomorphism.

Proof. Suppose K , L are both ﬁelds of cardinality p n. Both ﬁelds contain a unique copy of Fp ,
and by mapping 1K to 1L and extending additively, we get a partial isomorphism between these
copies of Fp . Now we show how to extend it. Let α ∈ K be a Fp -generator and let f ∈ Fp [X ]
be its minimal polynomial. Since f is irreducible of degree n, we have that f (X ) divides the
polynomial X pn − X (see Proposition D.5.14).
Using the fact that X pn − X = ∏
β∈L(X − β), we conclude that L contains a root β of f . We
assert (see Exercise D.10) that the map that sends α 7→ β is an isomorphism from K to L.

D.5.5 The Trace and Norm maps

We conclude this section with two basic polynomials that have some very nice regularity prop-
erty when dealing with ﬁnite ﬁelds and their extensions.

Deﬁnition D.5.1. Let F = Fq and let K = Fq n . Then the Trace function Tr = TrK →F is the func-

tion obtained by the evaluation of the polynomial Tr(X ) = X + X q + X q 2 + · · · + X q n−1. The Norm
function is obtained by evaluation of N (X ) = X 1+q+q 2+···+q n−1.

The Norm and Trace functions are important because they map elements of K to the sub-
ﬁeld F and they do so in a nice uniform way. We mention some properties below.

Proposition D.5.16. 1. Trace is a F-linear map, i.e., for every α ∈ F and β, γ ∈ K , we have
Tr(α · β + γ) = α · Tr(β) + Tr(γ).

2. Norm is multiplicative, i.e., N (β · γ) = N (β)N (γ)

3. Trace is a q n−1-to-one map from K to F.

4. Norm is a (q n − 1)/(q − 1)-to-one map from K ∗ to F∗.

Proof. 1. The F-linearity follows from the facts that (αβ + γ)q i = αq i βq i + γq i and αq i = α.

2. The multiplicativity is obvious from deﬁnition.

375

3. For β ∈ K we have Tr(β)q = βq + · · · βq n = βq + · · · + βq n−1 + 1 = Tr(β) and so the range of Tr
is F. Since Tr is a polynomial of degree q n−1 is can take on any value in the range at most
q n−1 times. But it has a domain of size q n and range of size q, so it must take on every
value exactly q n−1 times.

4. The is similar to Part (3) above. By Exercise D.11, we have that N (β)q = N (β) and further-
more note that by deﬁnition, N (β) is non-zero iff β ̸= 0. We then use the degree of N and
counting to determine that it is a regular function on non-zero values.

The Trace function from K → F is especially important since it captures all F-linear maps
from K → F, as explained below.

Proposition D.5.17. A function L : K → F is F-linear if and only if there exists λ ∈ K such that
L(β) = Tr(λβ) for every β ∈ K .

Proof. First note that f (β) = Tr(λβ) is obviously F-linear since

f (αβ + γ) = Tr(λ(αβ + γ)) = Tr(λαβ) + Tr(λγ) = α Tr(λβ) + Tr(λγ) = α f (β) + f (γ)

for every α ∈ F and β, γ ∈ K (where in the above we used Propositon D.5.16). This concludes
one direction of the proposition.
To see the converse we employ a counting argument. First note that if λ ̸= 0 then the func-
tion fλ(β) = Tr(λβ) is not identically zero. (To see this, note that fλ(Z ), viewed as a polynomial
in Z has degree |K |/|F| and it is a non-zero polynomial since the coefﬁcient of Z is non-zero.)
By linearity this implies that fλ ̸= fτ if λ ̸= τ since fλ − fτ = fλ−τ ̸= 0. So, including λ = 0, we
have at least |K | distinct linear functions of the form fλ(·). We now note there are also at
most |K | such functions. To see this let β1, . . . , βn ∈ K be F-linearly independent elements
of K (i.e., ∑n
i =1 αi βi ̸= 0 if (α1, . . . , αn) ∈ Fn \ {0}). Since K is a degree n extension of F we know
such a sequence exists and furthermore the βi ’s generate K in that for every β ∈ K there exist
α1, . . . , αn ∈ F such that β = ∑
i αi βi . We note that a linear function L : K → F is completely
determined by its values at β1, . . . , βn, since for every β = ∑
i αi βi ∈ K with α1, . . . , αn ∈ F, we
have L(β) = L(∑i αi βi ) = ∑
i αi L(βi ). Thus the number of linear functions is upper bounded by
|{(L(β1), . . . , L(βn)) ∈ Fn}| ≤ |F|n = |K |. We conclude that these are exactly |K | functions that are
F-linear from K → F, and these are exactly the Trace functions.

D.6 Algorithmic aspects of Finite Fields

In this section we show how ﬁnite ﬁelds may be represented and ﬁeld operations computed
efﬁciently.
Let q = p t for prime p and positive integer t . We consider how to work with Fq — the ﬁeld
on q elements.
We start by noticing that if O(q 2) space is not imposing, then four tables — one for addition,
and one for multiplication, and one each for additive and multiplicative inverses would sufﬁce

376

for working with ﬁelds, with each ﬁeld operation now requiring a single table look up. In what
follows we give more succinct descriptions that still allow moderately fast (some polynomial in
log q) operations.

D.6.1 Prime Fields

We start with the case of t = 1. Here there is not much to do. The most natural representa-
tion of the ﬁeld is by specifying the prime p which takes log2 p + 1 = log q + 1 bits to specify.
The most complex part of addition and multiplication is the computation of the remainder of
the operation modulo p, and this takes at most O((log p)2) steps by the naive method. More
sophisiticated algorithms can bring this compexity down to O((log p)(log log p)2).

D.6.2 General ﬁelds as vectors

For general ﬁelds, we can adopt one of two approaches. The ﬁrst of these uses less of the
knowledge that we have about ﬁnite ﬁelds, but helps abstract away many issues. In this view
we use the isomorphism between Fp t and Ft
p to represent elements of the former as vectors
in Ft
p . This, thus represents elements of Fq by O(log q) bits which is nice. This also tells us
how to add in Fq since it is simply coordinatewise Fp -addition. However this representation
by itself is not sufﬁcient to do Fq -multiplication. To multiply elements we enhance this repre-
sentation by maintaining t 2 vectors wi j ∈ Ft
p with wi j = ei · e j where the ei ’s are the unit vec-
tors (so ei = (0, . . . , 0, 1, 0, . . . , 0) is 1 in the i th coordinate and zero elsewhere). Now given u =
(u1, . . . , ut ) and v = (v1, . . . , vt ) we can compute u · v = ∑t
i =1 ∑t
j =1 ui v j wi j . This leads to a roughly

O(t 3(log p)2) = O((log q)3) time algorithm for multiplying in Fq while requiring O(t 3 log p) bits
to store p and the vectors wi j . While not the most efﬁcient representation, this may afford a
clean representation that may be sufﬁcient in several settings.

D.6.3 General ﬁelds as polynomial rings

Our ﬁnal representation uses the fact that the ﬁeld Fp t is isomorphic to Fp [X ]/(g ) for any ir-
reducible polynomial g of degree t . Here, a ﬁeld element is simply a polynomial in Fp [X ]
of degree strictly less than t which is maintained as a vector of coefﬁcients. Addition is just
coordinate-wise addition, whereas multiplication is polynomial multiplication followed by a
remainder computation modulo g . Thus addition takes time O(t (log p)2) while mutliplication
naively takes time O(t 2(log p)2). The only ingredients that need to be remembered to do ﬁeld
operations are the integer p and the polynomial g ∈ Fp [X ], all of which take O(t log p) bits. So
this representation deﬁnitely outperforms the generic representation via vector spaces in al-
most all senses (though we might ﬁnd the vector space view helpful when discussing certain
operations with codes).
 377

D.6.4 Finding primes and irreducible polynomials

The ﬁnal question that remains to be discussed is how hard is to ﬁnd the ingredients that de-
scribe a ﬁeld. Of course, this depends on how the ﬁeld is described, and the most natural one
may be by giving the cardinality q of the ﬁeld.
Given q = p t , it is straightforward to enumerate all candidate (p, t ) pairs such that q = p t

— there are only log q possible values of t and thus log q such integers. Only one of these, the
one with the largest t could correspond to prime p. Testing if an integer is prime can be done
efﬁciently with randomization, and thanks to a recent breakthrough [1] even deterministically
in time polynomial in log q.
When t = 1 no further works needs to be done. If t > 1 one needs to ﬁnd an irreducible
polynomial g of degree t and this can be a challenge. There are several possible solutions here:

Randomized It is known (and can actually be proved with a little effort, given the ingredients
of this chapter) that a random polynomial g ∈ Fp [X ] of degree t is irreducible with prob-
ability at least 1/t . Furthermore, irreducibility can be tested (see next section) in time
poly(log q). Thus repeatedly sampling random polynomials till an irreducible polynomial
is found takes expected time poly(log q). (See Algorithm 8.)

Deterministic Shoup [90] gave an algorithm to deterministically ﬁnd an irreducible polyno-
mial of degree t in Fp [X ] in time poly(t , p). Notice that this dependence is slower than
one may hope for in terms of p, but works well when p is small (say, smaller than t ).

Explicit In some rare cases, i.e., a few choices of p and t , explicit polynomials are known that
are irreducible. These may be used when the ﬁeld size seems appropriate. One such
family of irreducible polynomials is given in the following proposition.

Proposition D.6.1 ([69]). Let p = 2 and t = 2 · 3ℓ for any non-negative integer ℓ. Then the
polynomial X t + X t /2 + 1 is irreducble in F2[X ].

D.7 Algorithmic aspects of Polynomials

In this section we review basic facts about algorithmic aspects of manipulating polynomials. We
start with basic tasks and move to more complex tasks ending with factoring and root-ﬁnding.

D.7.1 Adding, Multiplying, Dividing

Given two polynomials f , g ∈ Fq [X ] of degree at most n, they can be added with O(n) operations
in Fq and no more needs to be said. f and g can also be multiplied with O(n2) operations by the
standard long multiplication. Similarly the quotient and remainder obtained when dividing f
by g can be computed wih O(n2) operations using the long division algorithm. More efﬁcient
algorithms do exist for both these tasks making O(n(log n)c ) ﬁeld operations, for some constant
c. (See [103] for this and other references for this section.)

378

D.7.2 Greatest Common Divisor

Perhaps the most surprising algorithm in algebra is that of ﬁnding greatest common divisors
(of integers or polynomials), and would be even more so, if it were not for over 2000 years of
exposure. To explain, let us look at the deﬁnition of the problem.

Deﬁnition D.7.1 (Greatest Common Divisor). Given polynomials f , g ∈ F[X ], their greatest com-
mon divisor, denoted gcd( f , g ), is the maximal degree polynomial h(X ) with leading coefﬁcient
being 1 such that h divides f and g .

The natural algorithm for ﬁnding gcd( f , g ) would be to factor f and g into irreducible fac-
tors, and then to take all common factors (with multiplicity) and take their product to get h.
Unfortunately this reduces gcd to factoring which goes in the wrong direction. (As we will see
below, factoring can also be solved efﬁciently for polynomials, but by reduction to gcd compu-
tation.)
But fortunately, we can employ Euclid’s algorithm which uses the following algorithmic re-
duction: If deg(g ) < deg( f ) and g does not divide f , then gcd( f , g ) = gcd(g , r ) where f = q · g +r
with deg(r ) < deg(g ) is as given by the division algorithm. This simple fact turns out to be al-
gorithmically effective reducing the (sum of the) degree of the polynomials in a single step of
polynomial division, and thus leading to a polynomial time algorithm for ﬁnding the greatest
common divisor.
Once again the steps of this algorithm can be combined in clever ways to get an implemen-
tation in O(n(log n)c ) time.

D.7.3 Factoring and Root-Finding

Finally, one of the most striking tasks related to polynomials that turns out to have a polynomial
time algorithm is the factorization of polynomials. Polynomials, even multivariate ones, can be
factored extremely efﬁciently with randomization and this is a consequence of many years of
research in algebraic computing. We won’t give the strongest results here, since even stating the
result is non-trivial. For our purposes it will sufﬁce to know that polynomials in Fq [X ] of degree
n can be factored in time poly(n, log q). We state this general result, and prove a very special
case of it, which will sufﬁce for the algorithms in this book.

Theorem D.7.1. There exists a constant c and a randomized algorithm running in expected time
O((n log q)c ) that factors polynomials of degree n in Fq [X ]. Furthermore, if q = p t for prime t ,
then there is a deterministic algorithm with running time O((npt )c ) for factoring.

To give an idea behind this powerful algorithm, we consider a simple special case of root-
ﬁnding.

Deﬁnition D.7.2 (Root-Finding Problem). The input to the root ﬁnding problem is a polynomial
f ∈ Fq [X ] of degree at most n (given as a list of coefﬁcients f0, . . . , fn ∈ Fq ). The task is to ﬁnd all
α ∈ Fq that are roots of f , i.e., to output the set {α ∈ Fq | f (α) = 0}.

379

We now turn towards the root-ﬁnding algorithm. The algorithm relies crucially on the al-
gorithm for computing greatest common divisors (mentioned in the previous section) and two
additional facts. First we use the fact X q − X = ∏α∈Fq (X −α) to algorithmic advantage as follows.

Lemma D.7.2. A polynomial f ∈ Fq [X ] has a root in Fq if and only if gcd( f , X q − X ) ̸= 1.

Proof. The proof is immediate. If f has a root α, then X − α divides gcd( f , X q − X ) and so their
gcd can’t be trivial. Conversely a factor of X q − X is of the form ∏
α∈S(X − α) for some S ⊆ Fq ,
and so gcd( f , X q − X ) must be of this form. If the gcd is non-trivial, then S must be non-empty
implying that for every α ∈ S we have X − α divides f and thus f has a root in S ⊆ Fq .

The step above is almost algorithmic, but to verify this, we need to stress that the gcd of
f and X q − X can be computed in time polynomial in deg( f ) and log q. We explain how this
can be done in the next few paragraphs, taking a detour on sparse polynomials. But assuming
this can be done, this provides a natural starting point for a root ﬁnding algorithm. Given f
we compute g = gcd( f , X q − X ). If g ̸= 1, then we take the set S1 of roots of g and the set S2 of
roots of f /g and output S1 ∪ S2. The set S2 can be computed recursively (since f /g has smaller
degree than f ), but for S1 we need some new ideas to determine how to compute the roots of
g , when g splits into linear and distinct factors over Fq . To get to this point we will use the fact
that X q − X splits into some high-degree sparse factors and this will turn out to be crucial to
ﬁnding S. Indeed the sparsity of X q − X and its factors are heavily used concepts and we now
take a detour to explain these effects.

Sparse high degree polynomials

We start with some terminology. We say that a polynomial h ∈ F[X ] is t -sparse if at most t of its
coefﬁcients are non-zero. Every polynomial h is thus (deg(h) + 1)-sparse, but often the sparsity
can be smaller, and this will be useful. One sparse polynomial that is already motivated by the
earlier discussion is X q − X , which is 2-sparse. We will see a few more below.

Lemma D.7.3. Let f ∈ F[X ] be a polynomial of degree n and let h ∈ F [X ] be a t -sparse polynomial
of degree D. Then h mod f and gcd( f , h) can be computed in time poly(n, t , log D).

Proof. It obviously sufﬁces to compute h mod f in time poly(n, t , log D) and then one can use
Euclid’s algorithm to compute gcd( f , h) = gcd( f , h mod f ) in time poly(n). In turns out that
if h = ∑t
i =1 hi X di and we can compute hi X di mod f in time poly(n, log di ) for every i , then
we can add the results in time poly(n, t ) to get h mod f . Finally, we note that X d mod f can
be computed by repeated squaring. Let d = ∑log2 d
j =0 d j 2 j . We can ﬁrst compute the sequence

of polynomials g j = X 2 j mod f = g 2
j −1 mod f by repeatedly squaring the output of the previ-

ous step. Then we can compute X d mod f = ∏log2 d
j =0 (g j )d j by using log d more multiplications,
yielding the desired result.

The lemma above shows that sparse polynomials can be used effectively. The following
lemma shows that the central sparse polynomial also has sparse factorizations, and this will be
useful later.
 380

Proposition D.7.4. 1. Let Fq be a ﬁeld of odd characteristic (and so q is odd). Then X q − X =
X ·(X (q−1)/2 −1)·(X (q−1)/2 +1). In particular X q − X factors into three 2-sparse polynomials
of degree at most q/2.

2. Let q = 2t for integer t ≥ 2. Then (X q − X ) = Tr(X ) · (Tr(X ) − 1) where Tr(X ) = TrFq →F2(X ) =

X + X 2 + X 4 + · · · + X 2r −1 is the Trace map from Fq to F2. In particular X q − X factors into
two (2 + log2 q)-sparse polynomials of degree q/2.

Proof. The case of odd q is obvious by inspection. Only aspect to be stressed is that (q − 1)/2 is
an integer.
For the case of even q, we use the fact that the trace map is a map from Fq to F2. So every
α ∈ Fq satisﬁes Tr(α) = 0 or Tr(α) = 1. It follows that X − α divides Tr(X ) · (Tr(X ) − 1) for every
α. Consequently X q − X divides Tr(X ) · (Tr(X ) − 1). The identity X q − X = Tr(X ) · (Tr(X ) − 1) now
follows from the fact that both polynomials have the same degree and have leading coefﬁcient
1.
 The existence of such sparse polynomials with many roots is one of the remarkable aspects
of ﬁnite ﬁelds and leads to many algorithmic effects. We demonstrate this by showing how this
is utilized in root-ﬁnding.

Root ﬁnding algorithm

We now complete the root-ﬁnding algorithm. Recall that by letting g = gcd( f , X q − X ) we can
reduce to the case of polynomials that split into distinct linear factors in Fq . We now focus on
this case. We will also focus on the case of odd q for simplicity, though all we will use is the fact
that X q − X splits into sparse factors of degree at most q/2.
If we were lucky, then g would have two roots α and β with X − α dividing (X (q−1)/2 − 1) and
X − β not dividing it. Then we would have that g1 = gcd(g , X (q−1)/2 − 1) would be a non-trivial
factor of g and we could recurse on g1 and g2 = g /g1. The key to the randomized root-ﬁnding
is that by an appropriate afﬁne change of variables, we can try to arrange to be “lucky”.
Speciﬁcally, ﬁx a ∈ F∗
q and b ∈ Fq and let g a,b(X ) = g ((X − a)/b). We have the following
proposition.

Proposition D.7.5. Let g ∈ Fq [X ] have α ̸= β as its roots. Then we have:

1. The coefﬁcients of g a,b can be computed efﬁciently given a, b and the coefﬁcients of g .

2. g a,b has aα + b and aβ + b as its roots.

3. If a ∈ F∗
q and b ∈ Fq are chosen uniformly at random independently, then the probability
that exactly one of aα + b and aβ + b is a root of X (q−1)/2−1 is at least 1/2.

Proof. Parts (1) and (2) are straightforward to verify. For part (3) we note that for any pair of
distinct elements γ, δ ∈ Fq there is exactly one pair a ∈ F∗
q and b ∈ Fq such that aα + b = γ and
aβ + b = δ. Since the fraction of distinct pairs γ, δ ∈ Fq such that exacty one of them comes

381

from a set of size (q − 1)/2 (the set of roots of X (q−1)/2 − 1) is at least 1/2 (the exact formula
is 1/2 + 1/(2q)) we have that the probability that exactly one of aα + b and aβ + b is a root of
X (q−1)/2−1 is at least 1/2.

We conclude by giving the full root-ﬁnding algorithm and summary of analysis of its run-
time.

Algorithm 46 ROOT-FIND(Fq , f )
INPUT: Fq , f (X ) ∈ Fq [X ]
OUTPUT: Fq roots of f (X )

1: g ← gcd( f , X q − X )

2: IF g = 1 THEN

3: RETURN ;

4: RETURN LINEAR-ROOT-FIND(Fq , g ) ∪ ROOT-FIND(Fq , ( f /g ))

Algorithm 47 LINEAR-ROOT-FIND(Fq , g )
INPUT: Fq , g (X ) ∈ Fq (X )
OUTPUT: Fq roots of g (X ) if g (X ) divides X q − X

1: IF deg(g ) = 1 THEN

2: RETURN {α} where g = X − α

3: REPEAT

4: Pick a ∈ F∗
q and b ∈ Fq uniformly independently

5: g a,b ← g ((X − b)/a)

6: h1 ← gcd(g a,b, X (q−1)/2−1)

7: g1 ← h1(a X + b)

8: UNTIL 0 < deg(g1) < deg(g )

9: RETURN LINEAR-ROOT-FIND(Fq , g1) ∪ LINEAR-ROOT-FIND(Fq , (g /g1))

Lemma D.7.6. ROOT-FIND(Fq , f ) outputs the multiset of roots of f in expected time poly(n, log q).

Proof. Let n = deg( f ). It is straightforward to see that ROOT-FIND makes at most n calls to
LINEAR-ROOT-FIND. (This is a very weak estimate, but we leave out optimizations here, in favor
of simplicity.) By Proposition D.7.5, Part (3), we have that the loop in LINEAR-ROOT-FIND will be
executed an expected constant number of times before a non-trivial split is found. Finally, the
degrees of the polynomials in the two recursive calls add up to deg(g ) and so this leads to a tree
of recurvie calls of size at most n with each internal node and leaf performing poly(n, log q) work
(to compute the various gcds, and the transformation of variables). Thus the overall expected
running time is poly(n, log q).
 382

D.8 Exercises

Exercise D.1. Let R be a commutative ring. Then prove the following:

1. If a is a unit in R, then b · a = 0 if and only if b = 0.

2. Using the previous part or otherwise, prove Proposition D.3.4.

Exercise D.2. Argue that every ﬁnite ﬁeld F has a ﬁnite characteristic char(F).

Exercise D.3. Let F be a ﬁeld with p elements for prime p. Argue that the map 1F → 1 can be
extended to an isomorphism between F and Zp .

Exercise D.4. Let G be an abelian group with identity 1 and let a ∈ G.

1. Argue that the map x → a · x for x ∈ G is a bijection.

2. Argue that ∏

x∈G x = an · ∏

x∈G x.

3. Using the previous part or otherwise prove Proposition D.5.4 for abelian groups.

Exercise D.5. Let p be a prime and let 0 ≤ i ≤ p. The show that

(p
i
 )
 mod p =
 {
1 if i = p or i = 0

0 otherwise .

Exercise D.6. In this exercise we will argue that for every k that divides n, we have N (Zn, k) = k,
i.e. show that the number of elements of Zn that have an order that divides k is exactly k.
Consider the following:

1. Prove that Sk = {a · n
k |0 ≤ a < k}

is a sub-group of Zn.

2. Argue that any b ∈ Zn that has an order that divides k satisﬁes, k · b mod n = 0.

3. Argue that any b ∈ Zn \ Sk it must be the case that k · b mod n ̸= 0.

4. Argue that any b ∈ Sk has an order that divides k.

5. Using the above parts or otherwise, argue that Sk contains all elements of Zn with an order
that divides k. Conclude that N (Zn, k) = k.

Exercise D.7. If k divides n, then show that X k − 1 divides X n − 1.

Exercise D.8. Let K ✄ F and let α be an F-generator of K . Let p be the minimal polynomial in
F[X ] such that p(α) = 0. Argue that have p is irreducible.

383

Exercise D.9. Let K ✄ F and let α be an F-generator of K . Let p be the minimal polynomial in
F[X ] such that p(α) = 0. Argue that there is an isomorphism between K and F[x]/p obtained
by ﬁxing F ✁ K and letting α 7→ X , which can be extended to all other elements.

Exercise D.10. Using notation in proof of Theorem D.5.15, prove that the map α 7→ β can be
extended to an isomorphism between K and L.

Exercise D.11. Argue that for any β ∈ Fq n , the norm function satisﬁes N (β)q = N (β).

384

Appendix E

Some Information Theory Essentials

We used the notions of Shannon entropy and conditional entropy in Chapter 6. This appendix
collects some basic facts relating to entropy and mutual information as a quick refresher. It is
very elementary and can be skipped by readers with basic familiarity with information theory.

E.1 Entropy

Let X be a discrete random variable, say,
 X ∼
 



a 2
3
b 1
6
c 1
6

and deﬁne H (X ) to be the entropy of the random variable X . We’d like the entropy to measure
the amount of information conveyed by the value of the random variable X , where the amount
of information is, roughly speaking, the amount of surprise we get from this random variable.
Suppose we had such a function S : [0, 1] → R
+ that takes a probability and maps it to a
non-negative real. Let’s think about some natural properties of S.
Suppose we told you that X is a, b, or c. Are you surprised? No—because this occurs with
probability 1 and we already know this. So therefore we’d like S(1) = 0: ﬂipping a two-headed
coin doesn’t give us any surprise.
Now suppose we told you that X = a. This is a little bit surprising, but X = b is more surpris-
ing because this is a rarer event. So we’d like S to satisfy S(p) > S(q) if p < q.
We’d also like S(x) to be a continuous function of x, because we’d like the surprise to not
exhibit jumps (if we had instead
 X ∼
 



a 2
3 + 10−6

b 1
6 − 10−6

c 1
6

our impression of the “surprise” of a should not be much different than the original X ).

385

Now suppose X1 and X2 are two independent instantiations of X . It’s natural for our surprise
from X1 = a and X2 = b to be additive (as each event “adds” to our surprise):

S ( 2
3 · 1
3
 ) = S ( 2
3
 ) + S ( 1
3
 )

which means we must have S(pq) = S(p) + S(q).

Exercise E.1.1. The only S that satisﬁes the above requirements is S(p) = c log2 ( 1
p
 ) , c > 0. A con-
venient normalization constant is that we are unit surprised by a fair coin ﬂip (S(1/2) = 1), which
sets c = 1.

Deﬁnition E.1.1 (Entropy). The entropy of a discrete random variable X , denoted H (X ), is the
average surprise for an outcome of X :

Ex
 (
log2 1
P (x = x)
 ) = ∑

x∈supp(()X ) p(x) log2 1
p(x) ,

where we deﬁne 0 log2 1
0 = 0.

We have the following obvious facts:

1. H (X ) ≥ 0; H (X ) = 0 if and only if X is deterministic.

2. Let X be uniform on {a1, . . . , an}. Then H (X ) = log2 n.

Lemma E.1.2. |supp(()X )| = n implies that H (X ) ≤ log2 n.

Proof. We use Jensen’s inequality: for convex functions f , we have E[ f (x)] ≤ f (E[x]) (this im-
plies E[X 2] ≥ E[X ]
2 and E[
pX ] ≤ p
E[X ].) Since we have

H (X ) = Ex←X
 [
log 1
p(x)
 ]

≤ log (Ex←X 1
p(x)
 ) = log n

where we have applied Jensen’s inequality to the expression with f (x) = log x while using the
random variable Z ∼ 1/p(x) w.p. p(x):

H (X ) = EZ [
log Z ] .

Communication. Let’s see if we can derive the binary entropy function in a different set-
ting. Suppose X ← Bernoulli(1/2), then H (X ) = 1. And if X ← Bernoulli(1), then H (X ) = 0. Now
suppose X ← Bernoulli(p), and we have X1, X2, . . . , Xn iid samples from this distribution, repre-
sented as a bitstring {0, 1}n. A way to communicate this in an efﬁcient way is that we ﬁrst send

386

k, the number of 1 bits in the string, and then use ⌈log2 (n
k)
⌉ bits to reveal which subset those 1s
go in. The expected number of bits communicated with this scheme is

E(number of bits) = ⌈log2 n⌉
︸ ︷︷ ︸
sending k
 + n∑

k=0
 (n
k
 )
p k (1 − p)n−k ⌈
log2
 (n
k
 )⌉

︸ ︷︷ ︸
number of bits required for each k
 .

What we are interested is the average fraction of bits we need as the number of bits as n grows
large: limn→∞ 1
n E(number of bits). Dividing our expression by n, we can omit the ﬁrst term
(log n/n → 0 as n → ∞) and we can use Stirling’s approximation (or the intuitive concept that if
k is far from pn the term in the sum is close to zero) to obtain that

lim
n→∞ 1
n E(number of bits) = h(p) = p log2 1
p + (1 − p) log2 1
1 − p ,

which tells us that we can take H (Bernoulli(p)) bits, on average, to communicate a Bernoulli(p)
random variable.
Non-binary random variable. We can extend this deﬁnition of entropy in the communi-
cations context to non-binary random variables. Suppose X ← {a1, . . . , an}. Suppose we have
related variables
 Z1 =
 {
1 X = a1
0 else

and
 Z2 =
 



a2 p2
1−p1
...

an pn
1−p1
 .

We can break H (X ) = H (Z1) + Pr(Z1 = 0)H (Z2),

as we need to communicate Z1 and then, if Z1 is 0, we need to communicate Z2. Since we
know how to compute H (Z1) from the binary case, we can recursively use this to obtain H (X ) =
∑n
i =1 pi log 1/pi , which is the same expression as we got before.

E.2 Joint and conditional entropy

Deﬁnition E.2.1 (Joint entropy). Let X and Y be two possibly correlated random variables. The
joint entropy of X and Y , denoted H (X , Y ), is

H (X , Y ) = ∑

x,y p(x, y) log 1
p(x, y) ,

where p(x, y) is deﬁned to be Pr(X = x ∧ Y = y).

387

If X and Y are independent, p(x, y) = p(x)p(y) and

H (X , Y ) = ∑

x,y p(x)p(y) (
log 1
p(x) + log 1
p(y)
 ) = H (X ) + H (Y ).

In general,
 H (X , Y ) = ∑

x,y p(x, y) log 1
p(x)p(y|x) ,

where p(y|x) = Pr(Y = y|X = x).
We can then do the following calculation:

H (X , Y ) = ∑

x,y p(x, y) log 1
p(x)p(y|x)

= ∑

x,y p(x, y) log 1
p(x) + ∑

x,y p(x, y) log 1
p(y|x)

= ∑

x p(x) log 1
p(x) + ∑

x p(x) ∑

y p(y|x) log 1
p(y|x)

= H (X ) + ∑

x p(x)H (Y |X = x)

= H (X ) + Ex[H (Y |X = x)].

This motivates the deﬁnition of conditional entropy:

Deﬁnition E.2.2 (Conditional entropy). The conditional entropy of Y given X is

H (Y |X ) = Ex[H (Y |X = x)].

Our calculation then shows this lemma:

Lemma E.2.1. H (X , Y ) = H (X ) + H (Y |X ).

Intuitively, this says that how surprised we are by drawing from the joint distribution of X
and Y is how surprised we are by X plus how surprised we are by Y given that we know X
already.
Note that if X and Y are independent, H (Y |X ) = H (Y ) and H (X , Y ) = H (X ) + H (Y ).
Recall the chain rule for probability: p(x, y) = p(x)p(y|x), or, more generally,

p(x1, . . . , xn) = p(x1)p(x2|x1) . . . p(xn|x1, . . . , xn).

There is a similar chain rule for entropy:

Theorem E.2.2 (Chain rule). For random variables X , Y , and Z ,

H (X , Y , Z ) = H (X ) + H (Y |X ) + H (Z |X , Y ).

For n random variables X1, . . . , Xn,

H (X1, X2, . . . , Xn) = H (X1) + H (X2|X1) + · · · + H (Xn|X1, X2, . . . , Xn−1).

388

The log in the deﬁnition of entropy changes the multiplication in the probability chain rule
to addition. Also, the order of the random variables does not matter. For example, it also holds
that H (X , Y ) = H (Y ) + H (X |Y ).

Note that H (X |X ) = 0.

Example E.2.3. Let X be a random variable that is uniform on {0, 1, 2, 3}. Let Y = X mod 2.
Clearly, H (X ) = 2.
H (Y ) = 1 since Y is uniform on {0, 1}.
H (X |Y ) = 1 because knowing Y tells us if X is odd or even.
H (Y |X ) = 0 since knowing X tell us the exact value of Y .
H (X , Y ) = 2 because X tells us everything about X and Y .

Intuitively, it seems like conditioning should never increase entropy: knowing more should
never increase our surprise. This is indeed the case:

Lemma E.2.4 (Conditioning cannot increase entropy). H (Y |X ) ≤ H (Y ).

Proof. First, we have that

H (Y |X ) − H (Y ) = H (X , Y ) − H (X ) − H (Y )

= ∑

x,y p(x, y) log 1
p(x, y) − ∑

x p(x) log 1
p(x) − ∑

y p(y) log 1
p(y) .

Since p(x) = ∑y p(x, y) and p(y) = ∑x p(x, y),

H (Y |X ) − H (Y ) = ∑

x,y p(x, y) log p(x)p(y)
p(x, y) .

We now deﬁne Z to be a random variable taking value p(x)p(y)
p(x,y) with probability p(x, y), so

H (Y |X ) − H (Y ) = Ex,y [log Z ]

≤ log E[Z ] by Jensen’s Inequality

= log
 (∑

x,y p(x, y) p(x)p(y)
p(x, y)
 )

= log
 ((
∑

x p(x)) (∑

y p(y)
))

= log 1

= 0.

As a corollary, we have a statement similar to the union bound:

389

Corollary E.2.5. For random variables X and Y ,

H (X , Y ) ≤ H (X ) + H (Y ).

More generally, for random variables X1, . . . , Xn,

H (X1, . . . , Xn) ≤ n∑

i =1 H (Xi ).

Exercise E.2.6. For a random variable X with support size n, we can think of entropy as a func-
tion from [0, 1]
n to R≥0. If X takes on n different values with probabilities p1, · · · , pn, then for
p = (p1, · · · , pn), H (p) = ∑n
i =1 pi log 1
pi . Show that H (p) is a concave function, i.e., show

H (λp + (1 − λ)q) ≥ λH (p) + (1 − λ)H (q)

for all λ ∈ [0, 1], p, q ∈ [0, 1]
n.

E.3 Mutual information

Deﬁnition E.3.1 (Mutual information). The mutual information between random variables X
and Y , denoted I (X ; Y ), is I (X ; Y ) = H (X ) − H (X |Y ).

Intuitively, mutual information is the reduction in the uncertainty of X that comes from
knowing Y .
We can write I (X ; Y ) in several other equivalent ways:

I (X ; Y ) = H (X ) − H (X |Y )

= H (X ) − (H (X , Y ) − H (Y ))

= H (X ) + H (Y ) − H (X , Y )

= H (Y ) − H (Y |X )

= I (X ; Y )

Note that I (X ; Y ) = I (Y ; X ).
The next lemma follows from the fact that conditioning cannot increase entropy.

Lemma E.3.1. I (X ; Y ) ≥ 0.

Also, if X and Y are independent, I (X ; Y ) = 0.

Example E.3.2. Consider X and Y as deﬁned in Example E.2.3. Then

I (X ; Y ) = H (X ) − H (X |Y ) = 2 − 1 = 1.

Example E.3.3. Let the Zi ’s be i.i.d. random variables that are uniform over {0, 1}. Let X =
Z1Z2Z3Z4Z5 and Y = Z4Z5Z6Z7. Then I (X ; Y ) = 2 since X and Y have 2 bits in common.

390

Figure E.1: Relationship between entropy, joint entropy, conditional entropy, and mutual infor-
mation for two random variables.

We show the relationship between entropy, joint entropy, conditional entropy, and mutual
information for two random variables X and Y in Figure 5.1.
We can also deﬁne a conditional version of mutual information.

Deﬁnition E.3.2 (Conditional mutual information). The conditional mutual information be-
tween X and Y given Z is
 I (X ; Y |Z ) = H (X |Z ) − H (X |Y , Z )

= H (Y |Z ) − H (Y |X , Z ).

Exercise E.3.4. Prove the chain rule for mutual information:

I (X1, X2, . . . , Xn; Y ) = n∑

i =1 I (Xi ; Y |X1, X2, . . . , Xi −1).

Note that the order of the Xi ’s does not matter.

Exercise E.3.5. It is not true that conditioning never inreases mutual information. Give an ex-
ampleof random variables X , Y , X where I (X ; Y |Z ) > I (X ; Y ).

391
