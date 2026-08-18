> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/shallit-shan-fibonacci-representations-2023.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2309.02765 | converted from PDF -->

## What it claims

Zs. Gazdag, Sz. Iván, G. Kovásznai (Eds.): 16th International
Conference on Automata and Formal Languages (AFL 2023)
EPTCS 386, 2023, pp. 228–242, doi:10.4204/EPTCS.386.18
 © J. Shallit and S. L. Shan
This work is licensed under the
Creative Commons Attribution License.

A General Approach to Proving Properties of Fibonacci
Representations via Automata Theory

Jeffrey Shallit* and Sonja Linghui Shan

School of Computer Science, University of Waterloo, Waterloo, ON N2L 3G1, Canada

shallit@uwaterloo.ca, slshan@uwaterloo.ca

We provide a method, based on automata theory, to mechanically prove the correctness of many nu-
meration systems based on Fibonacci numbers. With it, long case-based and induction-based proofs
of correctness can be replaced by simply constructing a regular expression (or finite automaton)
specifying the rules for valid representations, followed by a short computation. Examples of the
systems that can be handled using our technique include Brown’s lazy representation (1965), the far-
difference representation developed by Alpert (2009), and three representations…

## Statements it makes

Theorem 1. There is a decision procedure that, given a first-order logical formula F involving natural
numbers, comparisons, automata, and addition, and no free variables, will decide the truth or falsity of
F. Furthermore, if F has free variables, the procedure constructs a DFA accepting those values of the
free variables (in Fibonacci representation) that make F evaluate to TRUE.

Proposition 2. We can convert a binary string x to a Zeckendorf representation y for the same number
using the following algorithm: first append a 0 on the front, if necessary. Then scan the string from left
to right, replacing each occurrence of “ 011" successively with “ 100".

Theorem 3. There is an algorithm that, given rules that specify which representations are valid (in the
form of a regular language L of all valid representations), will decide if the corresponding numeration
system based on the Fibonacci numbers is complete and unambiguous for N.

Theorem 4. Suppose L is a regular language. If L is complete, we can find a representation for an
integer n in O(log n) time.

Theorem 7. The set of largest Fibonacci representations in dictionary order forms a regular language.

Lemma 8. The lengths of two Fibonacci-based representation strings for the same natural number differ
by one at most (not counting leading zeros).

Theorem 9. Let L = 0∗(ε|1|10(ε|0|1)1∗(01+)∗(ε|0)). Then L is complete and unambiguous.

Theorem 10. Let L be the language accepted by the DFA Z. Then L is complete and unambiguous.

*[digest of a 38227 character source; every section, statement, and proof in full at `research/sources/shallit-shan-fibonacci-representations-2023.full.md`]*
