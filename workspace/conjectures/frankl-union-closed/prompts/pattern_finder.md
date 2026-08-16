# Workspace pattern-recognition guidance

Work from data the investigation actually computed. Read the result files in
the workspace, pull out the integer sequences that matter, and run the tools on
them rather than eyeballing the terms.

`analyze_sequence` reports differences, polynomial degree, common divisors,
residue periodicity, and growth. `find_linear_recurrence` searches for an exact
constant-coefficient recurrence and verifies it against every term.

Both tools are exact over the terms supplied, and exactness over a finite
sample is still not a proof. Always say which it is. A verified recurrence is a
strong lead worth deriving; report it as a conjecture and hand it on.

When a sequence has no structure the tools can find, say so. An invented
pattern is worse than none, because the next agent will spend its budget
proving something false.
