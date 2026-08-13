```approach
idea: sofic-block-suffix-subshift
mechanism: |
  This studies the SEQUENCE OF BLOCK PATTERNS as a symbolic dynamical system —
  a different object from every entry-level or potential-level quantity tried
  so far. The leading {0,2} block of row k, written as a binary string
  B_k in {0,1}^{b_k} (halved entries), is a word; the conjecture
  "A_k(1) in {0,2} for all k" is exactly the statement that the language of the
  process {B_k}_{k>=1} NEVER contains the empty word.

  The mechanism. The block boundary is the only place where the XOR (Rule 90)
  interior meets the tail, and the established regeneration criterion is a
  single-suffix condition: the block grows iff it ends in 1 with a halved
  intruder 2 immediately after. So the future of the block length depends only
  on (a) the right SEGMENT of B_k near the boundary, and (b) the intruder.
  If the suffix process — the sequence of length-L right segments of the B_k
  jointly with the intruder value — is a SOFIC SYSTEM (equivalently, is
  recognized by a finite automaton, or is a factor of a subshift of finite
  type), then the whole infinite evolution is governed by a finite transfer
  matrix. Perron-Frobenius then gives a positive (or zero) topological entropy
  and, crucially, a finite, explicit decision procedure for whether the empty
  word lies in the closure of the language: the conjecture would reduce to
  "the empty word is not reachable in the finite suffix automaton".

  Why it beats the closed automaton route. backward-extension-automaton was
  refuted because VALID-EXTENSION sets are GLOBAL (factorial-weighted, Muney's
  holes) — no bounded window of the PAST determines whether a row extends
  forward into {0,2}. This proposal is the FORWARD direction: it does not ask
  to predict the block from a bounded past, it asks whether the observable
  suffix+intruder process, which drives the block length FORWARD, is sofic. A
  global forward process can be sofic even when its backward-extension analogue
  is not (the classic example is the even-subshift: globally constrained
  forward, finite automaton). The refuted Walsh-Hadamard item studied only the
  run-length of the single edge bit; this studies the full suffix subshift and
  its entropy, which is strictly more information.

  Named mathematics: subshifts and their languages, sofic systems, transfer
  matrices and Perron-Frobenius theory, topological entropy of a one-sided
  shift, and the minimal automaton (Nerode/Myhill) of the suffix process.

  Speculative, flagged. Whether the suffix+intruder process is sofic of finite
  order is open and is exactly what the first step measures; the strong form
  would be a finite alphabet (bounded intruder, suffix of bounded length L).
  If the minimal automaton cannot be finite at any L, that is itself a clean
  negative result that the block-length process is intrinsically infinite-state
  — and the run records the witnessing family of words.

  What would falsify it: a finite set of rows whose suffixes require
  arbitrarily large L to separate (i.e. the empirical automaton never
  stabilizes as L grows to 64 on the depth-1000 data), or a bounded intruder
  value that fails (the intruder must stay bounded for the alphabet to be
  finite; the data shows intruder <= 14 in the live regime, to be re-verified).
status: proposed
first-step: |
  Extract from code/out/blocks_depth1000.json (or a fresh exact sieve) the
  sequence of (suffix_k, intruder_k) for every live row k = 1..161, where
  suffix_k is the last L halved bits of the leading {0,2} block for L in
  {2,4,8,16,32,64}. For each L, build the Nerode automaton of the observed
  suffix-to-suffix transitions (states = distinct suffixes, edges = one-row
  transitions, weighted by how often they occur) and report: the number of
  distinct states, whether the automaton stabilizes as L grows (i.e. is the
  transition structure consistent with a fixed finite-order Markov/sofic
  model), the empirical topological entropy (log of the Perron root of the
  transition matrix), and whether the empty suffix is reachable from any live
  state. Then state the precise sofic hypothesis: "there exists L0 such that
  the suffix+intruder process is a factor of a subshift of finite type of
  order L0, and the empty word is not in its language" — and hand research
  whether any known result (e.g. on factors of the prime-gap parity sequence)
  already implies soficness.
```
