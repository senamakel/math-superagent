# Run 1 — live observations

Recorded while the run was going, so the reasoning behind each change is here
rather than reconstructed afterwards.

## The headline finding, at 04:00 elapsed

**The model recognised the problem and recalled the answer in its first two
searches, before doing any work at all.**

```
query 1: "Hadwiger-Nelson problem chromatic number of the plane
          lower bound 4 upper bound 7"
query 2: "de Grey chromatic number of the plane at least 5
          unit distance graph 1581 vertices"
```

The seed never uses the words "Hadwiger", "Nelson", "de Grey", or the number
1581. All four came from the model's weights. The screen denied both queries —
which is the screen working exactly as designed — but the denial came *after*
the recall, and no control can be placed earlier than that.

This is the confound `GROUND_TRUTH.md` predicted, observed directly on the first
run, and it is the strongest available evidence for the de-naming assessment
recorded there: **weak** for this problem, because the statement is
self-identifying. Any claim this run makes about "discovering" `χ ≥ 5` has to be
read against a trace in which `1581` appears at search number two.

What the run can still measure honestly:

- whether it builds the exact-arithmetic machinery and the SAT oracle (M1),
  which recall does not supply;
- whether it searches structurally (M2);
- whether it can produce the vertex set, which is the part recall genuinely
  cannot hand over.

## Screen behaviour, at 04:00

13 decisions, all `denied`, all on `exa_search`: 5 at `arguments`, 8 at
`result`. No false negatives visible — the two recall queries above are among
the argument denials.

## Two defects to fix before the next run

The policy is read at startup, so neither can be applied to a run already
going. Batched deliberately rather than restarting and losing the trajectory.

### 1. `Moser spindle` is over-blocked

It is in `[block]`, so the run cannot research **spindling**, which is a
legitimate pre-2018 construction technique that the seed's own leads section
points at. Blocking the name of a technique the seed asks the run to use is
over-blocking: it degrades the research capability being measured rather than
withholding the answer.

Move it to `[flag]`, where the adjudicator can allow a source about the
construction and deny one that announces `χ ≥ 5`. `Hadwiger Nelson` stays in
`[block]` — that one is the problem's name and leads straight to the result.

### 2. A proxy-blocked host surfaces as an opaque transport error

```
download_document ... error: document download failed:
  error sending request for url (https://doi.org/10.4230/...)
```

`doi.org` is not on the proxy allowlist, so the request dies at the network
boundary after a 5–12 second timeout, and the model is told only that a request
failed. It has no way to learn that the host class is unreachable, so it can
keep trying — spending budget on calls that cannot succeed, and turning the
measurement into "does the harness notice downloads do not work" rather than
into mathematics.

The tool screen already refuses a *denied* host immediately with a clear
message. It should do the same for a host that is simply not on the
allowlist: fail fast, and say that the source has to come through
`read_sources` instead. The allowlist has to reach the compiled policy for
that, and it is plaintext — API hostnames reveal nothing about the answer.

## Not a defect

- `recall_memory` returning `404 NoDataError` on a fresh Cognee stack. Expected
  while the library is empty.
- `download_document` failing on publisher hosts generally. That is the strict
  allowlist the operator chose, working as intended: the container talks to
  APIs, and content arrives through Exa's server-side fetches, which the screen
  reads in plaintext.
