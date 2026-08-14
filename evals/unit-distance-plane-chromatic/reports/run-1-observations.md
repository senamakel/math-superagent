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

## At 12:00 — the strict allowlist starved the librarian

`download_document`: **16 attempts, 16 failures.** Every one blocked at the
network boundary — `arxiv.org` (6), `export.arxiv.org` (3), `doi.org` (3),
`sciencedirect.com`, `link.springer.com`. The librarian was spending 54% of the
run's model calls with a zero success rate on its main tool, and the transport
error told it nothing that would let it stop.

Handled two ways:

1. **Immediately, by steering.** `./steer` reaches a live run at the next
   boundary and creates no container, so the run did not have to be restarted.
2. **Properly, in code**, for runs 2 and 3 — the policy is read at startup, so
   a code change cannot reach a run already going.

Both changes are committed as `668ac253`.

### What the directive did, and why it is a good sign

The `director` carried it into `TASKS.md`, `CONTEXT.md` and
`prompts/librarian.md` — the three places that change what roles are told — and
then said explicitly that it filed no claim, opened no thread and requested no
research, because the directive names an environment fact rather than a
mathematical one.

That is precisely the behaviour the design intends: a directive is asserted, not
established, and the `director` is denied `research/CLAIMS.md` for exactly this
reason. The rule held under a live test.

## At 12:00 — trajectory

- 103 model calls across 7 roles; `tool_builder` active (9 calls).
- Attempt 1 open, no judge verdict yet.
- 6 sources, 2 summaries — all via `read_sources`, none via download.
- `code/brute.py` written (8.8 kB). **0 claims filed**, which is the thing to
  watch: `GOAL.md` requires the oracle to be calibrated against the 7-vertex
  graph before anything measured with it is trusted, and a run with code but no
  claims has not yet established anything.

## At 16:00 — the documented phase-1 trap, reproduced exactly

| | |
| --- | --- |
| sources | 14 |
| `research/ROOT.md` | 97 lines |
| claim blocks filed | **0** |
| `CONTEXT.md` Established | **empty placeholder** |
| `code/brute.py` | written, **never executed** |
| `code/out/` | empty |
| librarian share of model calls | 58.5%, still climbing |

`AGENTS.md` already records this failure, from a previous run: *"a live run spent
twenty-seven uninterrupted minutes there, reached fifty-three sources and a rich
ROOT.md, and never wrote a single belief into the brief every role reads — it
had read everything and concluded nothing."*

The conjecture task prompt anticipates it in as many words — *"You are behind if
research/ has content and CONTEXT.md's Established section is empty"* — and the
run did it anyway, at 16 minutes, against a 30-minute attempt budget.

### The framework finding

**This is the repository's own principle failing on its own terms: a prompt
instruction is not a control.**

Phase 1's exit condition is written into the task prompt and enforced by
nothing. There is no counter, no threshold, and no routing arm that notices
`sources > 0 && claims == 0`. The loop's thresholds — `STUCK_THRESHOLD`,
`COMPUTATIONAL_THRESHOLD`, `UNVERIFIED_THRESHOLD` — all measure what happens
*after* an attempt is judged, and this run has not produced a judge verdict yet,
so none of them can fire. The run can spend its entire attempt budget in
gathering and the graph has no way to see it.

Candidate remedies, for the supervision document rather than for now:

1. A **derived counter** on the extraction ratio — sources filed versus claim
   blocks written — with a routing arm that forces extraction when it diverges.
   It is a cheap, exactly-measurable quantity and it is already on disk.
2. A **budget on the librarian's share** of model calls within one attempt.
   58.5% with zero claims is the signature, and it is visible to `./diagnose`
   from outside, so the runtime can see it too.
3. Failing both, make the phase-1 exit test a **tool** the run has to call, so
   that not exiting is something a reader can see it never did.

Steered as directive 2, which is the operator remedy the design already
provides. That it *needed* an operator is the finding.

## Final state at 82:30, when the run was stopped

Stopped by the operator. The workspace survives with its own checkpoint history,
so `./calibrate unit-distance-plane-chromatic` continues from what is on disk.

| | |
| --- | --- |
| model calls | 651, across 12 roles |
| attempts / verdicts | 1 / 0 |
| sources | 36 |
| captured output files | 23 |
| **claim blocks filed** | **0** |
| **`CONTEXT.md` Established** | **still the empty placeholder** |
| screen decisions | 118 |

Role spend: librarian 38.2%, pattern_finder 20.4%, tool_builder 14.1%,
scholar 12.9%, then nine others under 4% each.

The one loop line recorded: `verdict unsolved, progress no (computational,
1 consecutive scaling), next retry`.

### What the run did do

Real computation, and a lot of it: 23 captured output files including a spindle
census, a `k11` extension, and an edge-fit analysis. `tool_builder` and
`pattern_finder` together took 34.5% of the calls. This is not a run that only
talked.

### What it never did, in 82 minutes and after being told twice

**File a single claim, or write one belief into `CONTEXT.md`.**

Directive 2 asked for exactly this, in as many words, and the run acknowledged
it and still did not do it. That upgrades the finding: the phase-1 extraction
gap is not a matter of the run not having been *told*. It was told by the task
prompt, and then told again by an operator directive, and the ledger the whole
design routes through stayed empty.

So the remedy cannot be a better instruction. It has to be a control — a derived
counter on the extraction ratio, a cap on the librarian's share, or a tool the
run must call to leave the phase. The three candidates in the section above
stand, and the second directive is the evidence that the prompt-level fix has
already been tried and failed.

### The screen, over a full run

```
denied                   92
denied-host               6
allowed-by-adjudicator   19
denied-by-adjudicator     1
```

by tool: `exa_search` 86, `read_sources` 16, `citation_graph` 7,
`find_similar_sources` 4, `download_document` 4, `deep_research` 1.
by stage: 47 arguments, 71 result.

Two things worth keeping from this. The adjudicator is **discriminating rather
than rubber-stamping** — 19 allows against 1 deny, on text the deterministic
stage had already flagged, which is the ratio a useful second stage should show.
And the screen reached **every** research tool, not just `exa_search`: the
`citation_graph`, `find_similar_sources` and `deep_research` counts are the
evidence that wrapping at construction covered the whole surface.
