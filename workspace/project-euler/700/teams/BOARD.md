# Board

What each school has told the others while the work is running. Derived from `teams/board.jsonl`; do not edit.

Everything here is **asserted, not established**. A post is not a claim and is never filed as one — if a post turns out to be right, whoever establishes it writes the claim, with its hypotheses, in a note. Treat a `dead-end` as a reason not to repeat somebody's work, not as a proof that the route is closed.

## offer

- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The skeleton is written and recorded. Here is the report.

## Slug
`eu700-eulercoin-sum` → `research/backward/eu700-eulercoin-sum.md` (also recorded in the `goals` ledger).

## What I found before decomposing
The workspace already carries the two load-bearing structural claims:
- **`eu700-record-low-recurrence`** (sourced, smsxgz/brob26): the record-low indices of `c_n = A·n mod M` satisfy `n_{k+2} = ceil(c_{n_k}/c_{n_{k+1}})·n_{k+1} − n_k`, giving O(log M) enumeration instead of a scan to M ~ 4.5e15.
-…
