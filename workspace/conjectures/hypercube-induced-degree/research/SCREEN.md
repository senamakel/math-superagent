# Screen ledger

Every decision the evidence screen made this run. This workspace is a
**calibration** workspace: the problem in `problem.md` is stated as open, and
sources that would hand the run a published solution are withheld in code.

A row here is not a fault. It records that a source was reached for and not
delivered, which is information about how the run was working — and a run with
no rows is as informative as a run with many.

The matched term is deliberately not recorded. Naming it here would put the
withheld name into this workspace, which is the one thing the screen exists to
prevent.

| when | tool | stage | decision | detail |
| --- | --- | --- | --- | --- |
| 1786745792 | `exa_search` | result | denied | term matched in 12208 characters |
| 1786745796 | `exa_search` | result | denied | term matched in 12172 characters |
| 1786745849 | `download_document` | arguments | unreachable-host | host `arxiv.org` is not on the egress allowlist |
| 1786745849 | `download_document` | arguments | unreachable-host | host `arxiv.org` is not on the egress allowlist |
| 1786745852 | `exa_search` | result | denied | term matched in 12163 characters |
| 1786745874 | `exa_search` | result | denied | term matched in 12101 characters |
| 1786745892 | `download_document` | arguments | unreachable-host | host `arxiv.org` is not on the egress allowlist |
| 1786745896 | `download_document` | arguments | unreachable-host | host `citeseerx.ist.psu.edu` is not on the egress allowlist |
| 1786745896 | `download_document` | arguments | unreachable-host | host `arxiv.org` is not on the egress allowlist |
| 1786745896 | `download_document` | arguments | unreachable-host | host `arxiv.org` is not on the egress allowlist |
| 1786745896 | `download_document` | arguments | unreachable-host | host `arxiv.org` is not on the egress allowlist |
| 1786745995 | `exa_search` | result | allowed-by-adjudicator | flagged, then allowed (12086 characters) |
| 1786746029 | `read_sources` | arguments | denied | term matched |
| 1786746036 | `read_sources` | arguments | denied | term matched |
| 1786746040 | `exa_search` | arguments | denied | term matched |
| 1786746095 | `read_sources` | result | allowed-by-adjudicator | flagged, then allowed (3984 characters) |
| 1786746123 | `exa_search` | arguments | denied | term matched |
| 1786746299 | `read_sources` | result | denied-by-adjudicator | adjudicator reply was neither ALLOW nor DENY; failing closed |
| 1786746577 | `exa_search` | arguments | denied | term matched |
| 1786746577 | `exa_search` | arguments | denied | term matched |
