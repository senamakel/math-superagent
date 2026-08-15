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
attribution. Its strength differs sharply by problem, and `GROUND_TRUTH.md`
records the assessment for each:

| slug | de-naming | why |
| --- | --- | --- |
| `hypercube-induced-degree` | **strong** | a self-contained extremal question about induced subgraphs of the cube; recognising it as the famous conjecture requires an equivalence that is not obvious |
| `unit-distance-plane-chromatic` | **weak** | "χ of the unit-distance graph on `R²`" is self-identifying |
| `consecutive-perfect-powers` | **weak** | `x^p − y^q = 1` is self-identifying, and "8 and 9" in the first paragraph settles it |

Where de-naming is weak, the **ordering** in `config/trace.jsonl` carries the
attribution instead: a term the run derived appears after the work that derived
it, and a term the model recalled appears before any such work.
`scripts/eval-report` reports first-occurrence positions for exactly this
reason.

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
