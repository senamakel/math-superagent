# Directives

What an operator asked this run to do, and what the run did about it. Written by the runtime; edit the queue, not this file.

## 1 — from steer

download_document cannot reach publisher or preprint hosts on this run: the network boundary permits only the search and data APIs, so arxiv.org, doi.org, sciencedirect.com and springer.com will fail every time regardless of the URL. Stop retrying them. Use read_sources and deep_research instead, which fetch server-side and return the text. This is a property of the run's environment, not of the sources, and it is not a finding about the mathematics.

I read the workspace first. The directive is an environment fact, not a research finding, so I carried it into the three places that decide what roles do with it:

- **`TASKS.md`** — replaced the placeholder with the full phase order from the run directive, and wrote the fetch rule into phase 1: use `read_sources`/`deep_research` for the blocked hosts, do not retry `download_document` on arxiv.org/doi.org/sciencedirect.com/springer.com, and do not file it as a mathematical finding.
- **`CONTEXT.md`** — added a short **Environment** section so every role is told the host restriction on every call; it stays well inside budget.
- **`prompts/librarian.md`** — folded the host warning into the "failed download" guidance, keeping the original "try another source, record what failed" advice.

I made no other changes: the directive names no research gap (so no `request_research`), starts no direction of attack (no new thread), and abandons none. `research/ROOT.md` already notes the sources were obtained via `read_sources`, so the plan on disk is consistent with the directive.
