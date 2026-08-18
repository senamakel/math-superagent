import Mathlib

/--
The provenance fact recorded in the source summary: the downloaded file is
identified by its title and arXiv identifier as Mureddu's power-grid paper,
not as a Llibre--Zhang Liénard survey.  The propositions below deliberately
formalise only the checkable metadata claim; they do not attempt to formalise
semantic document contents.
-/
def sourceTitle : String :=
  "Representation of the German transmission grid for Renewable Energy Sources impact analysis"

def sourceAuthor : String := "Mario Mureddu"
def sourceArxiv : String := "1612.05532"
def sourceSubject : String := "Physics and Society"

def isMuredduPowerGridRecord : Prop :=
  sourceTitle =
      "Representation of the German transmission grid for Renewable Energy Sources impact analysis" ∧
    sourceAuthor = "Mario Mureddu" ∧
    sourceArxiv = "1612.05532" ∧
    sourceSubject = "Physics and Society"

def isLlibreZhangLienardSurveyRecord : Prop :=
  sourceTitle = "Limit cycles of the Liénard equation" ∧
    sourceAuthor = "Llibre and Zhang"

theorem source_is_mureddu_not_llibrez :
    isMuredduPowerGridRecord ∧ ¬ isLlibreZhangLienardSurveyRecord := by
  simp [isMuredduPowerGridRecord, isLlibreZhangLienardSurveyRecord,
    sourceTitle, sourceAuthor, sourceArxiv, sourceSubject]

#print axioms source_is_mureddu_not_llibrez
