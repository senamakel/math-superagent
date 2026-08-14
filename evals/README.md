# `evals/` — the calibration set

This tree holds conjectures that **have** been solved, presented to the harness
as open, so that a run has a known destination and its trajectory can be scored.

Nothing here is mounted into a container. Only `workspace/conjectures/<slug>/`
is bind-mounted at `/workspace`, so the answer keys, the rubrics and the
plaintext blocklists in this tree are unreachable from a run by construction
rather than by instruction.

## Why this exists

The harness runs against open conjectures, and nothing measures whether it is
working. A run produces notes, code and ledgers, but with no known-good
trajectory to compare against there is no way to distinguish a harness closing
in on a proof from one generating plausible mathematical activity. Every
architecture change is therefore made blind.

A solved conjecture, with its solution withheld by a control, gives the missing
reference: a milestone ladder the run either climbs or does not, and a change to
the framework can be judged by whether it moves runs up that ladder.

## Layout

```
evals/
  README.md                      this file
  screen.baseline.terms          blocklist merged into every problem
  <slug>/
    GROUND_TRUTH.md              the real name, the actual solution, the year
    RUBRIC.md                    milestone ladder and negative markers
    screen.terms                 the per-problem blocklist, plaintext
    seed/                        problem.md, GOAL.md, METHOD.md — de-named
    reports/                     one eval-report per run
  .build/<slug>/                 generated, gitignored
    screen.json                  hashed terms + policy, mounted into the agent
    proxy.deny                   plaintext hosts, mounted into the proxy only
```

## The three problems

| slug | de-named as | really is | what it tests |
|---|---|---|---|
| `unit-distance-plane-chromatic` | `chi` of the unit-distance graph on `R^2` | Hadwiger–Nelson; de Grey 2018 | construction, exact arithmetic, SAT — machine-checkable, recall useless |
| `hypercube-induced-degree` | max degree of induced subgraphs of `Q_n` on `2^(n-1)+1` vertices | Sensitivity Conjecture; Huang 2019 | invention: one idea, no scale, no literature |
| `consecutive-perfect-powers` | `x^p - y^q = 1` | Catalan; Mihăilescu 2002 | depth, and whether the harness knows it is out of its depth |

Each `seed/problem.md` is a **time capsule**: the state of the art as of the
year before the solution, stated honestly, including the obstruction and the
leads that were genuinely available then. It is not a puzzle with the hints
removed — a dishonest seed measures nothing. Where a seed's own hinting is
substantial, `GROUND_TRUTH.md` records exactly how much, so the score can
account for it.

## The screen

Three layers, only the first two of which are controls.

1. **The proxy.** Under `compose.eval.yaml` the agent container is joined to an
   `internal: true` network and has no default route out. All egress goes
   through a proxy holding a host allowlist plus this tree's `proxy.deny`. This
   is what closes `execute_command`, which otherwise runs Python with
   unrestricted network and would make the rest decorative. HTTPS `CONNECT`
   shows the proxy only `host:port`, so the proxy decides *which hosts are
   reachable* and nothing more.

2. **The Rust screen** (`src/orchestrator/screen/`). Wraps every research tool
   and `download_document` at construction, so both the harness path and the
   workflow path inherit it. It sees plaintext — including PDF text, which is
   extracted before the tool returns — and so it is the only layer that can
   decide *whether an allowed source reveals the answer*. Deterministic term
   matching first, then a fail-closed adjudicator for anything flagged. Every
   decision lands in `config/screen.jsonl` and `research/SCREEN.md`.

3. **The leakage audit**, host-side, after the run. Not a control: it catches
   what the first two missed, and — more importantly — it catches **recall**,
   which no control can stop, by checking the *order* of events in
   `config/trace.jsonl` against the answer key.

### Why the compiled terms are hashed

`screen.json` is mounted into the agent container so the Rust screen can use it,
and `execute_command` can read any file the runtime can. A plaintext blocklist
would therefore hand the run exactly the names it is meant to withhold. So
`scripts/compile-screen` emits every term as `sha256(salt || normalised term)`
over token n-grams; matching hashes the candidate text the same way. Structural
policy — size bounds, adjudicator settings — stays plaintext, because it reveals
nothing.

Hosts stay plaintext in `proxy.deny`, because the proxy container is a separate
container the agent cannot read.

The adjudicator needs no secret at all. It is asked whether a text reveals a
solution to *the de-named statement the run already has*, so no answer key ever
crosses into the container.

### What the screen deliberately does not block

`arxiv.org` and the scholarly indexes stay reachable, and so does `oeis.org`.
The paper carrying the answer is withheld by its **content**, not by its venue,
so the pre-solution literature around it stays available. Blocking the venue
would be easier and would test a different, less interesting harness — one with
no research capability at all.

## The threat model, stated plainly

The run is **not adversarial**. It is trying to solve a mathematics problem, not
to defeat a filter. The controls are built to the standard `CLAUDE.md` sets —
enforced in code, not by prompt instruction — and they close every path a
normally-behaving run would take, including the one through `execute_command`
that the tool layer alone would miss.

They are not built to withstand a run that actively sets out to exfiltrate. A
sufficiently determined agent inside the container could observe that a screen
exists, and the hashed terms bound what it could learn from that, but the design
does not claim to stop it. What it claims is that **no accidental ingestion path
remains**, which is what the calibration needs.

One known gap, recorded rather than hidden: `cognee` runs with
`ALLOW_HTTP_REQUESTS: true` and performs fetches from inside the Docker network,
where the agent's egress rules do not apply. Do not hand the memory server a URL
to fetch during a calibration run.

## Running one

```sh
./calibrate unit-distance-plane-chromatic
./diagnose --workspace conjectures/unit-distance-plane-chromatic
./euler-tui --workspace conjectures/unit-distance-plane-chromatic
scripts/eval-report unit-distance-plane-chromatic
```

`./calibrate` refuses to start if a container is already mounted on that
workspace — resolved by mount, not by name, because two runs on one workspace is
silent and interleaves two investigations in one checkpoint history.
