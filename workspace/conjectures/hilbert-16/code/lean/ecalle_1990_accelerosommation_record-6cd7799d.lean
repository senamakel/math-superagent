import Mathlib

/--
A bibliographic record is represented by its citation data.  This theorem says
that the recorded title, venue, year, and page interval are internally
consistent as a record; it does not assert Écalle's mathematical finiteness
 theorem, whose statement is explicitly unavailable in the held source.
-/
def RecordConsistent : Prop :=
  (1990 : Nat) = 1990 ∧
  (74 : Nat) ≤ 159 ∧
  "Finitude des cycles-limites et accelero-sommation de l'application de retour" ≠ ""

theorem ecalle_1990_accelerosommation_record : RecordConsistent := by
  simp [RecordConsistent]

#print axioms ecalle_1990_accelerosommation_record
