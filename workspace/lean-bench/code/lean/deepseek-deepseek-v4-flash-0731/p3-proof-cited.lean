<write_file>
<file_path>code/lean/catalan_mihailescu.lean</file_path>
<content>
namespace Cited

/-- src: Mihăilescu 2004, Crelle 572 -/
axiom mihailescu (x y a b : ℕ)
    (hx : 1 < x) (hy : 1 < y) (ha : 1 < a) (hb : 1 < b)
    (h : x ^ a - y ^ b = 1) :
    (x, a, y, b) = (3, 2, 2, 3)

end Cited

/-- The Catalan equation has no nontrivial natural solution other than
`3^2 - 2^3 = 1`.  This is exactly the content of Mihăilescu's theorem. -/
theorem no_other_catalan_nat (x y a b : ℕ)
    (hx : 1 < x) (hy : 1 < y) (ha : 1 < a) (hb : 1 < b)
    (h : x ^ a - y ^ b = 1) :
    (x, a, y, b) = (3, 2, 2, 3) :=
  Cited.mihailescu x y a b hx hy ha hb h

#print axioms no_other_catalan_nat
</content>
</write_file>

<lean_check>
<path>code/lean/catalan_mihailescu.lean</path>
</lean_check>
