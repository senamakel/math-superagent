# Mourtada Théorème 0 conclusion truncated in ar5iv conversion — PDF needed for exact N, L

## Finding

The ar5iv HTML conversion of Mourtada (arXiv:0912.1560) renders **Théorème 0's
conclusion as empty**: after "il existe des entiers N N et L L et des voisinages
Γ_k ⊂ U ⊂ U_0 et V ∈ (ℝ^q,0) tels que" the statement cuts off. The conversion
drops the displayed-equation content of that conclusion (the bound on the number
of limit cycles of X_ν in U and their multiplicity). The theorem's *existence*
claim — integers N, L and neighborhoods making the count uniform — is clear from
the surrounding prose ("Les cycles limites de X_ν correspondent aux intersections
isolées… Le théorème 0 est alors une conséquence simple du théorème IVC1: la
propriété (i) est équivalente à la χ-régularité de f, et la propriété (ii) est une
conséquence de la noethérianité ou la locale noethérianité de l'idéal différentiel
I_{χ,f}"). But the **numerical content is not in the library**.

## Why it matters

Lu (arXiv:2607.13785) cites Mourtada [3] for the QRH theorem applied to
all-hyperbolic words. The run's `lu-h14-3-verification` thread verifies Lu's
claim independently. If that verification ever needs Mourtada's actual N, L (or
the exact uniformity statement of Théorème 0), the ar5iv copy is insufficient —
the **arXiv PDF (0912.1560v1)** is the authoritative copy and its displayed
equations must be read. The library holds the abstract page and the ar5iv text,
not the PDF body with its displayed equations intact.

## Action if the numbers are ever needed

1. Fetch https://arxiv.org/pdf/0912.1560 and read Théorème 0's conclusion from
   the PDF (the `download_document` converter may recover the equation; the ar5iv
   HTML route is confirmed lossy on this statement).
2. Record the recovered N, L statement as an `asserted-by-source` claim with
   `anchors` pointing at the PDF.

## Not affected

The *structural* content of Théorème IVC1 ("QRH^{k,.} est localement χ-finie")
and of the three principaux theorems (II1, IIIA1, IIIB1) IS recoverable from the
held text; the double-inclusion formula and the reduced derivation normal form
χ_ℓ = ρ ∂/∂ρ − Σ s_j u_j ∂/∂u_j are both displayed correctly. Only Théorème 0's
conclusion is truncated.
