# Erdős (1950), "Az 1/x1 + ... + 1/xn = a/b egyenlet egész számú megoldásairól"

Source: https://www.renyi.hu/~p_erdos/1950-02.pdf (Mat. Lapok 1 (1950) 192–210,
in Hungarian). The PDF conversion is OCR-imperfect (Hungarian diacritics
garbled).
Full text: `research/sources/erdos-1950-original.full.md`

## What it establishes (sourced, primary)

The 1950 original Erdős paper on the integer solutions of
`1/x1 + ... + 1/xn = a/b`. Introduces the "unit fraction" (törzstört)
terminology, frames the problem (the "optical equation" n=2 case which is the
lens equation), and discusses Nakayama's earlier work on distinct-denominator
solutions and the function N(a,b). The conjecture itself is stated as posed to
Straus (per the standard attribution, this paper is the reference the
"Erdős–Straus conjecture" name hangs on, though the specific 4/n form is
usually attributed to the 1948 conversation; Obláth's 1950 paper is the first
published statement of the 4/n form per erdosproblems #242).

## Consequence

This is the historical root of the subject. It fixes the attribution (Erdős
1950; Obláth 1950 for the explicit 4/n form) and the framing (unit fractions,
sums of reciprocals). It does not contain the modular-identity results; those
are Mordell/Rosati/Yamamoto era. Held as context; not load-bearing for the
construction, but now in the library so nobody re-derives the attribution.

```claim
id: erdos-1950-original
statement: Erdős 1950 (Mat. Lapok 1, 192–210) studies integer solutions of 1/x1+...+1/xn = a/b (unit fractions), defines N(a,b) for distinct-denominator minimal length, and discusses Nakayama's results; it is the founding reference for the unit-fraction-sum problem (with Obláth 1950 as the first published statement of the 4/n form).
hypotheses: none (historical attribution).
holds-here: true — the run's problem is the n=3, a=4, b=n case of this equation.
status: sourced (original PDF, Hungarian; OCR-imperfect conversion).
bearing: attribution and framing only; construction results come from Mordell/Yamamoto/Salez/Schinzel.
anchor: research/sources/erdos-1950-original.full.md
```