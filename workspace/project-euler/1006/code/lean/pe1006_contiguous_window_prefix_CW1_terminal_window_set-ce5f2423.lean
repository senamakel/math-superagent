import Mathlib

namespace PE1006CW1

abbrev Word := List Bool

def windows (w : Word) (k : Nat) : Set Word :=
  {u | ∃ r, r + k ≤ w.length ∧ u = (w.drop r).take k}

def fibWord : Nat → Word
  | 0 => [false]
  | 1 => [false, true]
  | n + 2 => fibWord (n + 1) ++ fibWord n

def fibLen : Nat → Nat
  | 0 => 1
  | 1 => 2
  | n + 2 => fibLen (n + 1) + fibLen n

def terminalWindows (q : Word) (k : Nat) : Set Word :=
  {u | ∃ r, fibLen 0 ≤ r ∧ r ≤ q.length - 1 ∧
    ((q ++ q).drop r).take k = u}

/--
`cw1_terminal_window_set` formalises the requested terminal-window claim.
The Fibonacci factor set is represented here by `factors`; the standard word
and its length are explicit parameters, so the missing mathematical bridge is
isolated rather than hidden in notation.
-/
def factors (k : Nat) : Set Word :=
  {u | ∃ n, u ∈ windows (fibWord n) k}

/- gap
id: cw1-factor-stabilisation
lemma: ∀ k t, 1 ≤ k → k < fibLen t → factors k = windows (fibWord t ++ fibWord t) k
status: open
next: prove stabilization of length-k factors in the doubled standard word, using the Fibonacci factor-location theorem
-/

/- gap
id: cw1-terminal-index-cover
lemma: ∀ k t, 1 ≤ k → k < fibLen t → windows (fibWord t ++ fibWord t) k = terminalWindows (fibWord t) k
status: open
next: prove the terminal-window index lemma by splitting windows at the concatenation boundary and using the standard-word conjugacy classification
-/

/- gap
id: cw1-terminal-uniqueness
lemma: ∀ k t, 1 ≤ k → k < fibLen t → Set.ncard (terminalWindows (fibWord t) k) = k + 1
status: open
next: establish injectivity of terminal indices via primitivity/least-period facts, then count the interval of indices
-/

theorem cw1_terminal_window_set
    (k t : Nat) (hk : 1 ≤ k) (hkt : k < fibLen t)
    (h₁ : factors k = windows (fibWord t ++ fibWord t) k)
    (h₂ : windows (fibWord t ++ fibWord t) k = terminalWindows (fibWord t) k)
    (h₃ : Set.ncard (terminalWindows (fibWord t) k) = k + 1) :
    factors k = terminalWindows (fibWord t) k := by
  exact h₁.trans (h₂.trans (by rfl))

#print axioms cw1_terminal_window_set
end PE1006CW1
