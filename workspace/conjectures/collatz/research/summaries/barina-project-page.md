<!-- source: https://pcbarina.fit.vutbr.cz | converted from HTML -->

```claim
id: barina-2075-2p60
answers: current-record-bound-c386
statement: The convergence of all numbers below 2075 × 2^60 (≈ 2^71.02) has been verified under the Collatz map (every such orbit reaches 1).
hypotheses: positive integers n < 2075 × 2^60 ≈ 2.39 × 10^21.
holds-here: true — this is the current computational record for the verification bound.
evidence: Barina project page (pcbarina.fit.vutbr.cz), snapshot 2026-08-18; milestone log 2^71 verified 2025-01-15; journal paper Barina, J Supercomput 81, 810 (2025), DOI 10.1007/s11227-025-07337-0.
status: verified-numerically
falsifies: a counterexample below 2075×2^60 (an orbit not reaching 1), or a primary source reporting a verified bound above it.
```

```claim
id: barina-method
statement: The verification method uses the accelerated/Syracuse form with 3^k sieves, GPU/CPU acceleration, work unit 2^40 numbers, ~5s per unit on modern GPUs, distributed across European supercomputers.
hypotheses: none — method description.
holds-here: true — describes how the record was obtained.
evidence: Barina project page; Barina 2025 paper Section 3 (algorithms).
status: asserted-by-source
falsifies: a primary source describing a materially different method for the same bound.
```

```claim
id: barina-milestones
statement: Milestones: 2^68 verified 2020-05-07, 2^69 2021-12-10, 2^70 2023-07-09, 1.5×2^70 2023-11-03, 2^71 2025-01-15; four new path records found during the convergence test.
hypotheses: none.
holds-here: true — timeline of the record.
evidence: Barina project page and Barina 2025 paper abstract.
status: verified-numerically
falsifies: a primary source reporting a different bound or date for a milestone.
```

Convergence verification of the Collatz problem

# Convergence verification of the Collatz problem

The convergence of all numbers below 2075 × 2 60 (&asymp; 2 71.02) has been verified. The work unit is 2 40 numbers. On modern GPUs, verification of one work unit takes 5 seconds on average. All source codes are available on [this GitHub repository][1].

## Progress towards verifying all numbers below 2076 × 2 60

Lowest incomplete: `17.1991 % `(work unit `2175975546 × 2 40`, all work units below are verified)
Lowest unassigned: `17.1991 % `(work unit `2175975546 × 2 40`, all work units below are assigned or even verified)

## Results

- [Table][2] with found path records.

## Project log

- 2019-09-04 started the project
- 2020-05-07 the convergence of [all numbers below 2 68 is verified][3]
- 2021-12-10 the convergence of all numbers below 2 69 is verified
- 2023-07-09 the convergence of all numbers below 2 70 is verified
- 2023-11-03 the convergence of all numbers below 1.5 × 2 70 is verified
- 2025-01-15 the convergence of all numbers below 2 71 is verified

## Contact

[David Barina][4] < [ibarina@fit.vutbr.cz][5] >

## References

- Barina, D. Convergence verification of the Collatz problem. *J Supercomput*77, 2681–2688 (2021). [https://doi.org/10.1007/s11227-020-03368-x][6]
- Barina, D. Improved verification limit for the convergence of the Collatz conjecture. *J Supercomput*81, 810 (2025). [https://doi.org/10.1007/s11227-025-07337-0][7]

---

Generated: Tue, 18 Aug 2026 11:53:11 +0200


## Links

[1]: https://github.com/xbarin02/collatz/
[2]: path-records.htm
[3]: news.htm
[4]: https://www.fit.vut.cz/person/ibarina/
[5]: mailto:ibarina@fit.vutbr.cz
[6]: https://doi.org/10.1007/s11227-020-03368-x
[7]: https://doi.org/10.1007/s11227-025-07337-0
