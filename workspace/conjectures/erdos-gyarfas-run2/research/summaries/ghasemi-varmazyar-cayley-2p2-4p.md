# Ghasemi & Varmazyar — Erdős–Gyárfás for Cayley graphs of order 2p^2 and 4p

Source: M. Ghasemi, R. Varmazyar, *Mat. Vesnik* 282 (2022), 37–42.
Open publisher copy:
[[ghasemi-varmazyar-cayley-2p2-4p.full]] (`research/sources/ghasemi-varmazyar-cayley-2p2-4p.full.md`).

## What it establishes (new settled class, added to the library)

Extends the Cayley-graph verification (Ghaffari–Mostaghim held separately) to new
group orders. Exact theorems, each a distinct family:

- **Theorem 2.1.** Every connected Cayley graph X = Cay(G2(p), S) contains a cycle
  of length **4 or 16**.
- **Theorem 2.2.** Every connected Cayley graph X = Cay(G3(p), S) contains a cycle
  of length **4, 8 or 16**.
- **Theorem 2.3.** Every connected Cayley graph X = Cay(H2(p), S) contains a
  **4-cycle**.
- **Theorem 2.4.** Every connected Cayley graph X = Cay(H3(p), S) contains a
  **4-cycle**.

Here G2(p), G3(p), H2(p), H3(p) are the groups of order 2p^2 and 4p studied in the
paper (p an odd prime). Together these cover the Cayley graphs of order 2p^2 and 4p.

```claim
id: ghv-cayley-2p2-4p
statement: Every connected Cayley graph of order 2p^2 contains a cycle of length 4, 8, or 16; every connected Cayley graph of order 4p contains a 4-cycle. Hence Erdos-Gyarfas holds for Cayley graphs of order 2p^2 and 4p.
hypotheses: finite simple connected Cayley graphs; groups of order 2p^2 and 4p, p odd prime
holds-here: yes (a settled restricted class)
status: asserted (publisher full text)
bearing: extends the confirmed-family list; the strongest conclusion is the 4-cycle in several families — short forced powers of two.
anchor: research/sources/ghasemi-varmazyar-cayley-2p2-4p.full.md
```

## For this problem

Adds to the class of settled cases (with exact hypotheses) that ROOT.md must
state. Records that the conjecture holds beyond the earlier quaternion/dihedral/
semidihedral/order-p^3 families. The proofs use Cayley-graph structure, not the
minimal-counterexample degree spine, so this is a *class result*, not a lever on
the general problem.
