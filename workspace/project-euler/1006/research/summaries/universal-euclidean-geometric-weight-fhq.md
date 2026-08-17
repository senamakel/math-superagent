> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/universal-euclidean-geometric-weight-fhq.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://www.cnblogs.com/dixiao/p/15719155.html | converted from HTML -->

## What is in it

- [fhq_treap][2]
  - 很多时候你要够努力，你要做的是往前走，去100分的位置，而不是在0分位置就此停止
- [[学习笔记]万能欧几里得][6]
    - 问题形式
    - 解决该问题
      - 合并
      - 翻转
      - 合并
    - 实现
      - [【模板】类欧几里得算法][7]
    - 一些特定的问题
    - 公告


## What it claims

所以我们考虑 \(q \leq p\) ，则每个 \(R\) 前都有 \(\lfloor\frac{p}{q}\rfloor\) 个连续 \(U\),我们将其合并，那么每个 \(R\) 前的数还有
\(\lfloor\frac{px + r}{q}\rfloor - x\lfloor\frac{p}{q}\rfloor = \lfloor\frac{px - px + (p\ mod\ q)x + r}{q}\rfloor = \lfloor\frac{(p\ mod\ q)x + r}{q}\rfloor\)

于是有 \(sol(p,q,r,n,U,R) = sol(p\ mod\ q,q,r,n,U,U^{\lfloor\frac{p}{q}\rfloor}R)\)

*[digest of a 4581 character source; every section, statement, and proof in full at `research/sources/universal-euclidean-geometric-weight-fhq.full.md`]*
