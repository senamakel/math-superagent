# Context — what the library establishes

The bit-deletion game reduces to counting. The board is a **disjunctive sum** of
one subgame per number ([[disjsum]], [[cgt]]); each number with a 1-bits, b 0-bits
is the integer **a−b** ([[surreal]]), so the no-skip value of the whole board is
**A−B** (A = total 1-bits, B = total 0-bits). The game is strictly partisan, so
Sprague–Grundy does not apply ([[partisan]]); normal play, unable-to-move loses,
A−B>0 ⇒ One wins without skips ([[normalplay]]). The skip is a zugzwang/pass
self-loop, a 1-cycle in the loopy game, resolved as a DP fixpoint; a stopper ⇒
finite S(n) ([[zugzwang]], [[loopy]]). Pass theory is primary: [[pass_waiting]]
(Larsson–Nowakowski–Santos 2015) and [[mfl_pass]] (MFL 2011) show a pass can
dramatically change game structure, so **S(n) ≠ A−B and comes from the (A,B)
minimax DP, not any CGT closed form**; [[siegel_zugzwang]] (Siegel 2009) supplies
the theorem-level loopy/zugzwang frame (Li's theorem, stoppers).

Arithmetic engine — **polylog**, not iterating to n, which n=10⁵ demands:
- A(n)=Σ k·popcount(k) via A000788 ([[bitcount]]); B(n)=Σ k·zerocount(k) via
  A059015 = A083652 − A000788 ([[zerocount]], [[a083652]]).
- Trollope–Delange structure (main term + 1-periodic fluctuation) proven from
  [[trollopedelange]] (Girgensohn 2011), which also gives the O(log n)
  recurrences; [[verify_trollopedelange]] is the numeric check-list.
- **Weighted digit sums keep this structure** (first-moment closed forms) — now
  from two openly-held primary texts, [[flajolet_weighted_digitalsums]]
  (arXiv:1003.0150) and [[minabutdinov_qweighted]] (arXiv:1801.03120,
  Takagi–Landsberg limits), upgrading the abstract-only [[weightedmom]].
- S(n) ∉ OEIS ([[weightedsearch]]) — no lookup shortcut.

**Caveat (open):** counting is a *surrogate* — its (A,B) One-move (A−1,B),
Zero-move (A,B−1) ignore that deleting a leading 1 can also drop 0-bits
("100"→0). Given S(2)=2, S(5)=17, S(10)=64 are reproduced; real-vs-counting S(n)
agreement for all n is checked empirically by brute.py vs counting.py
([[disjsum]] records the caveat; see MEMORY.md, which also records the refuted
single-aggregate skip-readings).
