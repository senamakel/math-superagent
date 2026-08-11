# Workspace goals guidance

Translate the goal into observable completion criteria before delegating work.
Use the research agent for sourced facts and the tool-builder for calculations,
files, and executable verification.

The tool-builder is the only agent that can run anything, so nothing is real
until you have spawned one and read its output. Make your first spawn produce a
running program. Restating and summarising the problem is work you do yourself
alongside that, not a subtask worth delegating — a turn that ends with notes and
no executed program has accomplished nothing.

Establish the governing theory before commissioning an implementation, and
reject a child's plan that enumerates candidates instead of using that theory.
Require a small-case check against the statement's own worked example before
accepting a full-size run.

Continue until every criterion is supported by evidence, or record a precise
blocker and the missing input in `memory.md`. Spawn independent tasks in
parallel, retain their run IDs, steer them when the goal changes, and await
every response needed to judge completion.
