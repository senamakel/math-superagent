# Calibration: measuring the harness against solved conjectures

The rules are in [`AGENTS.md`](../AGENTS.md#calibration-runs). This file is the
evidence behind them — what each control was written to stop, what it cost to
learn, and what it deliberately does not do.

## The problem this exists to solve

The harness runs against open conjectures. It produces a research tree, six
derived ledgers, programs, captured output and a reflection archive. All of that
is legible, and none of it answers the only question that matters: **is this
working?**

An open conjecture has no known trajectory. A run that spends four hours
building a library, writing an oracle and stating three lemmas looks exactly
like a run that spends four hours generating plausible mathematical activity,
because on an unsolved problem *both* end without a proof. So every change to
the routing ladder, the role registry, the thresholds or the prompts has been
made without a way to tell whether it helped.

A conjecture that has **already been solved**, stated as open, supplies the
missing reference. The destination is known, the intermediate steps are known,
and a milestone ladder can be written in advance. Then a framework change is
judged by whether it moves runs up that ladder.

## Three things have to be true, and only two are achievable

**1. The answer must not be reachable.** This is achievable and is what the
screen does.

**2. The answer must not already be known.** This is *not* achievable. The model
weights hold these results. De-naming the statements helps — see below — and the
leakage audit measures the residue, but no control removes recall. Any report
that treats a calibration result as though retrieval were the only channel is
overclaiming.

**3. Ground truth must be outside the mount.** Achievable and cheap: only
`workspace/conjectures/<slug>/` is bind-mounted, so `evals/` at the repository
root is unreachable from a run by construction rather than by instruction.

## What was actually open

Three egress paths existed, and the obvious one was the least important.

- `exa_search` and the four discovery tools. Gated by `MATH_AGENT_RESEARCH`,
  and the path everybody thinks of.
- `download_document`. Granted to fifteen of the nineteen roles and **not**
  gated by `MATH_AGENT_RESEARCH` at all. It fetches an arbitrary URL. This is
  the path a reader of the registry would miss.
- `execute_command`. Runs Python in the container, and the container had
  unrestricted network. Three lines of `urllib` reach any paper on the web
  without passing a single screened tool.

The third one decides the design. A screen at the tool layer alone is a filter
on the *intended* research path and nothing more — it would have satisfied a
code review and failed the first run that decided to fetch a PDF with a script.

Worth recording precisely: `compose.yaml` and `docs/runtime.md` both referred to
"the runtime container's egress rules", in a comment explaining that Cognee's
own fetches bypass them. **There were no such rules.** The comment described a
control that had never existed, which is the exact failure this repository keeps
writing down — a document is not a control either.

## The two layers, and why the split falls where it does

**The proxy** (`compose.eval.yaml`, `Dockerfile.proxy`). The agent container is
joined to an internal network with no default route; all egress goes through
`screen-proxy`, which holds a host allowlist and refuses everything else.

An HTTPS request arrives at a proxy as `CONNECT host:443` and carries no path
and no body. So this layer can only ever decide **which hosts are reachable**.
That is exactly the decision it is good at, and it is the one that closes
`execute_command`.

**The Rust screen** (`orchestrator::screen`). Wraps every research tool and
`download_document` at construction. It sees plaintext — including PDF text,
which `readable` extracts before a tool returns — so it is the only layer that
can decide **whether an allowed source reveals the answer**.

Wrapping happens at *construction* rather than at registration because the same
`Arc<dyn Tool<()>>` values are handed to `caps::tools::WorkspaceTools` for the
workflow path, which has no harness and no middleware stack in between.
Middleware would have covered the agent path and silently missed the other one.

### Verified, not assumed

From inside the agent image, on the eval network:

```
--- direct, no proxy: the execute_command escape hatch ---
  https://arxiv.org/abs/1804.02385     BLOCKED  Temporary failure in name resolution
  https://openrouter.ai/               BLOCKED  Temporary failure in name resolution
--- through the proxy ---
  https://openrouter.ai/               REACHED  HTTP 200
  https://oeis.org/A000045             REACHED  HTTP 200
  https://arxiv.org/abs/1804.02385     BLOCKED  Tunnel connection failed: 403 Filtered
  https://en.wikipedia.org/wiki/...    BLOCKED  Tunnel connection failed: 403 Filtered
```

Two things this cost to learn:

- **Filter rules must be anchored.** tinyproxy matches with `regexec`, which is
  unanchored, so a bare `oeis\.org` also allows `oeis.org.attacker.example` —
  the allowlist leaks by suffix. Confirmed by trying it.
- **Network attachment order decides the default route.** With the internal
  network attached first, the proxy itself has no gateway and every *allowed*
  host fails with a tunnel error, which reads exactly like a broken allowlist.
  `priority: 100` on `egress` is load-bearing.

## Why the compiled blocklist is hashed

`screen.json` is mounted into the container so the Rust screen can read it, and
`execute_command` runs as the same user. A plaintext blocklist there would be
the leak: the file would name every author, title and identifier the run is not
supposed to encounter.

So terms travel as `sha256(salt || normalised n-gram)`, and matching hashes the
candidate text the same way. Hosts stay plaintext in the proxy's `proxy.deny`,
because the proxy is a container the agent cannot read.

The adjudicator needs no secret at all. It is asked whether a text reveals a
solution to *the de-named statement the run already has*, so no answer key
crosses the boundary.

**Normalisation is the fragile part**, because a divergence between the Python
compiler and the Rust matcher fails silently — no error, no ledger entry, just a
blocklist that never fires. Two bugs found by writing the tests rather than by
running the system:

- splitting only on the ASCII hyphen welds `Hadwiger–Nelson` (en dash, which is
  how mathematics actually writes it) into one token;
- dropping punctuation *inside* a token welds `arXiv:1804.02385` into
  `arxiv180402385`, matching nothing.

Both are fixed by the same rule — every non-alphanumeric character separates,
and combining marks are dropped rather than treated as separators — and
`terms_test.rs` pins digests generated by the compiler itself.

## The threat model, stated plainly

The run is **not adversarial**. It is trying to solve a mathematics problem, not
to defeat a filter. The controls close every path a normally-behaving run would
take, including the `execute_command` one that the tool layer alone would miss.

They do not claim to withstand a run that sets out to exfiltrate. Hashing bounds
what such a run could learn from the policy file, and that is the extent of it.

One gap is recorded rather than hidden: Cognee runs with
`ALLOW_HTTP_REQUESTS: true` and fetches from inside the Docker network, where
the agent's egress rules do not apply. Do not hand the memory server a URL to
fetch during a calibration run.

## De-naming, and how much it is worth

Every statement is restated in neutral notation with no names, dates or
attribution. Before round 1 the strength was assessed per problem, and the
assessment was wrong for the one it mattered most for:

| slug | predicted | measured in round 1 |
| --- | --- | --- |
| `hypercube-induced-degree` | **strong** — recognising it requires a non-obvious equivalence | **failed**: the run named `Huang`, `1907.00847` and the paper's title, and wrote `code/lib/huang.py` |
| `unit-distance-plane-chromatic` | weak — self-identifying | **failed**: `Aubrey de Grey`, `Hadwiger Nelson`, `1804.02385` |
| `consecutive-perfect-powers` | weak — `x^p − y^q = 1` is self-identifying | **failed**: `Mihăilescu`, `Catalan's conjecture`, the paper's title |

**De-naming does not work.** Not weakly, not for two of three — it failed on all
three, and it failed on the problem whose whole value depended on it. No search
was involved in any of these: the controls held, and the model simply knew.

The consequence is specific. `hypercube-induced-degree`'s **M3b** — which its own
`RUBRIC.md` calls *"the hinge of this entire calibration exercise"* and *"the
single most valuable datum any of the three runs will yield"* — measures whether
the harness can invent the signed-matrix step. It cannot be measured on a run
that already remembers it, so that datum is unobtainable as the problem is
currently written.

The runs were not deceptive about it. `research/notes/huang-lead.md` is headed
*"The recalled theorem"* and carries an integrity section; the note recording the
computed values says plainly that the computation "does NOT prove the theorem".
Concealment is not the failure mode. Contamination is.

### What replaces it

Two things, and the second is the one that works.

**Ordering**, as before: a term the run derived appears after the work that
derived it, and a recalled term appears before any such work.
`scripts/eval-report` reports first-occurrence positions for this reason. It is
necessary and it is not sufficient — round 1 shows recall arriving first and the
derivation being done anyway, which the ordering records but does not prevent.

**Recall-proof targets**, which is the real answer. A target is recall-proof when
remembering the published result does not supply it:

- extending an exact table (`f(6)`, `f(7)` on the cube) — nobody memorises those
  values and no proof hands them to you;
- a construction with a large explicit witness — knowing that a 1581-vertex
  5-chromatic unit-distance graph exists is worth nothing without the vertex set;
- a proved barrier against a named technique, checked against the run's own
  search.

All three appear in the rubrics already, under *"alternative ladders that score
equally"*. Round 1 says they should be the **main** ladder.

## The board is an unscreened channel, and it carries the answer

The strongest finding of round 1, and it is a consequence of a fix rather than
of a gap.

Schools share one board. On `hypercube-induced-degree`, `rising-sea` recalled the
proof and posted the entire mechanism to it — the block recursion
`A_n = [[A_{n-1}, I], [I, −A_{n-1}]]`, `A_n² = nI`, Cauchy interlacing, the whole
chain — and then posted again telling the other schools to stop:

> Any school still treating the lower bound as open should stop … Do not spend
> effort re-proving `f(n) ≥ √n` as if new.

`orchestrator::screen` wraps the tools that reach the web. `teams/BOARD.md` is
workspace-local, so **nothing screens it**, and one school's recall reaches every
other school complete and instantly.

That breaks the comparison the schools exist to support. `chisel` runs as the
control because an alternative school is only evidence when today's runtime ran
beside it — and two schools sharing a board are not two independent runs. A
calibration that draws conclusions about a school from a shared-board run is
reading a single contaminated trajectory twice.

The tension is real rather than an oversight to patch away: the board is
valuable *because* it moves what one school knows to another, and that is
exactly what makes it a contamination channel. Screening it would also destroy
its main observed use (below). The honest options are to run schools on separate
workspaces when the comparison is the point, or to accept that a shared-board
run measures the *ensemble* and never a school.

## What the board was actually used for

46 posts with bodies across three thirty-minute runs. Nine were the loop's own
structural offers; **37 were written by models through `post_board`**.

The dominant use was not idea-sharing. **18 of 46 posts (39%) correct or refute
something**, frequently the run's own earlier work:

- `REFUTED G-threshold-shadow`
- *"The attempt in `delsarte_lp_finding.md` overclaims, and two of its 'findings'
  predate it"*
- *"Claim `exp2-fixed23-proved-thue` is BANKED but over-claimed"*
- *"The flat-torus separation graph F is built on a BUG that manufactures false
  6-colourings"*
- *"Correction to my own hunch about approach (3)"*

`adversarial` posted most (19 of 46), which is what that school is for — and the
board is what let it attack *another school's* claims rather than only its own.
That is the strongest argument for schools this repository has produced, and
`src/prompts/board.md` does not ask for it. The brief asks for dead ends,
lessons, hunches, offers and asks; what the board became is peer review.

## The seed is falsifiable, and the runs falsified it

A calibration seed states the art as of the year before the solution. Round 1
shows the subject can check that:

> `problem.md`'s central premise — "the gap … has not moved in thirty years" — is
> stale and checkable-false

The unit-distance board says the same of its own seed. Both runs worked out they
were being handed a time capsule and told the other schools.

This is not fixable by writing the seed more carefully. A statement that the
literature has not moved is a claim about the present, the model knows the
present, and so the claim is checkable from weights alone with no search. A seed
should either avoid claiming the state of the art is current, or a problem should
be chosen whose current state the model does not know.

## What is deliberately not blocked

`arxiv.org` and the scholarly indexes are not denied at the tool layer, and
`oeis.org` stays reachable so `oeis_lookup` keeps working. The paper carrying
the answer is withheld by its **content**, not its venue, so the pre-solution
literature around it stays available.

Withholding the venue would be easier and would test a different, less
interesting harness — one with no research capability at all.

The proxy allowlist is narrower than that, and the consequence is accepted
deliberately: under the overlay `download_document` reaches only the API hosts,
and general content arrives through Exa, which performs its fetches server-side
and returns text the Rust screen reads in plaintext. The container talks to
APIs; content comes through tools that can be screened.

## What a good calibration run looks like

Not a solved conjecture. Each `RUBRIC.md` weights the ladder so that building
the right instrument, calibrating it before trusting it, and searching
structurally score above a claimed result — and on
`consecutive-perfect-powers` the scoring is deliberately inverted, because a
confident proof there is almost certainly fluent nonsense and a precise
statement of where the argument stops is the real outcome.

The single most valuable datum any of these runs can produce is **which role
proposed the key idea, at which attempt, and from what context**. That is what
no amount of computation or literature reading produces, and it is what a
framework change should be trying to make more likely.

Round 1 could not produce it, on any of the three problems, and the reason is
the subject of the next several sections: the key idea was recalled rather than
proposed, so there is no role, attempt or context to record. Everything below is
what round 1 found instead, and most of it is about this file's own instrument
rather than about the harness.

## The rubrics were built wrong

Every ladder in round 1 put a famous published theorem at **M4**: de Grey's
1581-vertex graph, Huang's theorem, Mihăilescu's theorem. Each took an expert
years. That makes the top rung unreachable by construction and leaves nothing
between *"did competent work"* (M2/M3) and *"matched a career mathematician"*
(M4).

A rubric whose top rung cannot be reached teaches nothing when it is missed. The
top rung has to be something a strong run could plausibly hit — for
`hypercube-induced-degree` that is pushing `f_exact` to `n = 7` or `8`, which is
genuinely hard, entirely recall-proof, and a real addition to a small table.

## Round 1: what the runs achieved

Three problems, run concurrently on 2026-08-14, stopped by the operator at
roughly thirty minutes. None completed an attempt cycle; all three showed
`verdicts 0`. Everything here is the first thirty minutes of a run.

None of it is new mathematics. All of it is recall-proof, verified and honest.

| slug | milestone | result |
| --- | --- | --- |
| `consecutive-perfect-powers` | **M3** | Case B closed; a proved barrier |
| `hypercube-induced-degree` | **M0** | `f(5) = 3`, verified three ways |
| `unit-distance-plane-chromatic` | **M2-equivalent** | every unit-distance graph on ≤ 11 vertices is 4-colourable |

**`consecutive-perfect-powers`** derived the Case B reduction itself
(`x = c²+1`, `y = cm`, `m² = ((c²+1)^p − 1)/c²`), proved a mod-8 classification
narrowing to one residual class, showed *no fixed modulus closes that class* — a
proved barrier, one of the four M3 routes its rubric names — then closed the
slice with Nagell–Ljunggren, excluding both of that theorem's exceptional
solutions individually. This rediscovers Ko Chao's 1965 theorem and leans on a
classical result it did not prove, and it says so. Its `h⁻(Q(ζ_p))` values for
`p ≤ 43` are correct, computed by two independent implementations and matched
against OEIS A000927 to `p ≤ 97`. It was the only run given all three schools,
and it was the problem predicted to go nowhere.

**`hypercube-induced-degree`** posed `f_exact` as an ILP decision problem rather
than enumerating subsets, cross-checked HiGHS against CP-SAT, and validated the
ILP against the exhaustive oracle on every `(n, d)` pair for `n ≤ 4` *before*
trusting it at `n = 5`. Verified on the host by a third, solver-free route.

**`unit-distance-plane-chromatic`** enumerated ~185M graphs with `nauty-geng`
across 28 CPUs in 28 residue classes, filtered to 228 kernel members, and
4-coloured each by two independent routes. The structural facts it used are the
right ones: a unit-distance graph is `K₄`-free, `K_{2,3}`-free (two unit circles
meet in at most two points), and every neighbourhood has maximum degree ≤ 2.
Sound, and modest — the smallest known 5-chromatic unit-distance graph has 509
vertices.

Two behaviours are worth more than the results. The unit-distance run caught its
own refutation tool returning a false positive, decoded the model, and recorded
the false positive rather than the refutation. It also established that the
fractional-chromatic LP certifies `χ ≥ 5` on *none* of its calibration graphs — a
dead end found, priced and written down.

The phase-1 trap did **not** reproduce. The previous round went 82 minutes with
36 sources and 0 claims; round 1 had programs running and claims filed inside
twenty minutes on all three problems.

## What round 1 changed in the runtime

**A decomposition posts to the board without a model having to comply.**
`post_board` is granted to three roles, and a live three-school hour on Euler
1006 called it zero times. The diagnosis then was that no prompt mentioned the
board, and `src/prompts/board.md` was written. Twenty minutes into a calibration
run with that brief in place, `goals` had taken forty-six turns and posted
nothing.

So `LoopSteps::offer_decomposition` posts the decomposition report itself, as an
`Offer`. `reduce_arm`'s second return value was dead; it now carries the report
to the one caller holding the school slug and the workspace.

The honest reading is narrower than it first appeared. By the end of the run
models had posted 37 times themselves, so the brief does work once the roles
run — two of the three holders only run after a verdict, and there were none in
the window first measured. The structural post guarantees a **floor**; it did not
rescue a dead capability.

The truncation is a separate, tested function, because it is the part that would
silently restore the original failure: `board::post` refuses a body over 2000
characters, two sub-agents routinely write past that between them, and no post
looks exactly like choosing not to post.

## What round 1 changed in the instrument

Three of these were silently corrupting results.

- **The screen contradicted itself.** Reachability was checked on every
  URL-taking tool, but only `download_document` dials its own URL —
  `read_sources`, `deep_research`, `find_similar_sources` and `citation_graph`
  post the URL to `api.exa.ai` or `api.openalex.org`, which fetch server-side.
  The proxy never sees the publisher host on those calls and could not block
  them. Meanwhile `UNREACHABLE_HOST` tells the caller to fetch the same material
  with `read_sources` — and `read_sources` then refused the same host, eleven
  times in twenty minutes. An instruction the runtime immediately contradicts is
  worse than no instruction.
- **The leakage audit was lying.** It reported *"No withheld term appears in
  anything the run wrote"* while `code/lib/huang.py` sat in the workspace. It
  audited `[block]` terms only, and every blocked phrase pairs the surname with
  another word (`Hao Huang sensitivity`), so none matched. The `[flag]` list —
  `signed adjacency`, `Cauchy interlacing`, `sensitivity` — was ignored
  entirely, and that is precisely the class the audit exists for: a flagged term
  is legitimate *when derived* and damning when it arrives first. It now audits
  flagged terms separately, and looks for the run **describing its own recall**
  (*"the recalled Huang lower bound"*), which is a stronger signal than any term
  because no blocklist has to have guessed the word.
- **Parallel runs could not share a Compose project.** Two runs in one project
  fight over one `screen-proxy` and one `agent-egress` network: the second `up`
  recreates services underneath the first's live container, and both proxies
  answer to one name. Each problem now gets its own `calibrate-<slug>` project;
  the cost is one extra proxy, five megabytes, per run.
- **Health timeouts were sized for one stack.** Back when a run started its own
  Cognee, three starting together loaded the box enough that a healthy server
  failed a five-second probe —
  the health log read `Health check exceeded timeout (5s)` while the server's own
  log showed a normal startup. The probe is now 20s and the launcher waits 420s.
  This is why `hypercube-induced-degree` failed to start on the first attempt.
- **`evals/<slug>/schools`** carries which schools attack a problem and the
  argument for the pairing, and `./calibrate` refuses a set without `chisel`: an
  alternative school is evidence only when today's runtime ran beside it.
- **`scripts/calibrate-watch`** reports the four things `./diagnose` cannot —
  school divergence, board use, adjudicator discrimination, and sources against
  claims — scoped to the live container, so *"did that change work"* is
  answerable at all across a restart.

A note on container naming, which cost real time: the Compose project name comes
from the checkout directory, so a run started from a worktree is called
`<worktree>-agent-run-<id>` and the documented `grep riemann-agent-run` finds
nothing while a container is live. Resolve a collision by **mount**, never by
name.

## Measured, not yet acted on

- **Concurrency is ~6× against a cap of 50.** 240 model calls, 7,199s of model
  time, 1,200s of wall clock. The harness uses an eighth of the parallelism it
  has, and the constraint is latency inside sequential role turns rather than
  semaphore contention.
- **p90 per model call is 76s; the worst observed was 358s.** One six-minute
  call stalls everything downstream of it.
- **An attempt takes 13–20 minutes.** At `MAX_ATTEMPTS = 8` and a four-hour
  ceiling a run gets roughly sixteen attempts across all schools. Cycle time is
  therefore the binding constraint on how many ideas a run tries, and it is the
  reason none of the three reached a verdict in thirty minutes.

## What to do next, in order

1. **Replace the calibration set, or move every top rung to a recall-proof
   target.** Round 1 cannot measure invention, and no control fixes that.
2. **Cut the attempt cycle time.** It bounds how many ideas a run gets to try,
   and nothing else here matters as much.
3. **Raise effective concurrency toward the cap that already exists.**
4. **Decide what a shared board means for the school comparison** — separate
   workspaces when the comparison is the point, or accept that a shared-board run
   measures the ensemble and never a school.
5. **Re-run to completion** and score against a ladder whose top rung is
   reachable.
