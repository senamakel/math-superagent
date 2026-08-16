> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/abdesselam-chipalkatti-hilbert-covariants.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/1010.2358 | converted from PDF -->

## What it claims

Given a directed acyclic graph with labeled vertices, we consider the problem
of ﬁnding the most common label sequences (“traces”) among all paths in the
graph (of some maximum length m). Since the number of paths can be huge, we
propose novel algorithms whose time complexity depends only on the size of the
graph, and on the frequency ε of the most frequent traces. In addition, we apply
techniques from streaming algorithms to achieve space usage that depends only on
ε, and not on the number of distinct traces.
The abstract problem considered models a variety of tasks concerning ﬁnding
frequent patterns in event sequences. Our motivation comes from working with a
data set of 2 million RFID readings from baggage trolleys at Copenhagen Airport.
The question of ﬁnding frequent passenger movement patterns is mapped to the
above problem. We report on experimental ﬁndings for this data set.

Keywords: algorithms; graphs; sampling; data mining; patterns discovery.

1 Introduction

Sequential pattern mining has attracted a lot of interest in recent years. However, some
of the probabilistic…

## Statements it makes

Theorem 1 We can generate a random sample of Sm in expected time O(|V |+|E|m+
log(1/δ)/ε) such that any trace with frequency ε or more has frequency at least ε/2 in
the random sample with probability 1 − δ. ◦

Theorem 3 Given a stream of elements representing the set of samples of traces pro-
duced by SAMPLETRACES, the space needed in order to output the traces with fre-
quency at least ε/2, without producing any trace with frequency less than ε/2, is
O(1/ε) words. ◦

*[digest of a 29571 character source; every section, statement, and proof in full at `research/sources/abdesselam-chipalkatti-hilbert-covariants.full.md`]*
