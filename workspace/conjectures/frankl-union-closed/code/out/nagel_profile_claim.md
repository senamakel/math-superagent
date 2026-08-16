# Nagel / Das–Wu kth-most-frequent abundance-profile equality — exact verification

<!-- regenerator-trigger -->

**Statement verified (exact integer arithmetic, oracle `lib.uc`).** For the
near-k-cube union-closed family on ground set `[k]`:

```
F = 2^[k-1] ∪ { [k-1] ∪ {k} }        |F| = 2^{k-1} + 1
```

the sorted-descending abundance profile is

```
[ 2^{k-2}+1  repeated k-1 times,  1 ]
```

So the **kth-most-frequent element** (the rare one, `k`) has exact frequency

```
1  =  |F| / (2^{k-1} + 1)
```

i.e. the Nagel lower bound `kth-most-frequent ≥ |F|/(2^{k-1}+1)` (Das–Wu,
arXiv:2412.03862, Thm 1.4) is **attained with equality** on the near-k-cube.

**The sequence of denominators.** `2^{k-1}+1` for `k = 2..8` is `3, 5, 9, 17,
33, 65, 129 = 2^n+1`, the OEIS **A000051** sequence, whose closed form is
`a(n) = 2^n + 1`. This is the Nagel constant for the kth-most-frequent element.

This is a **computational verification of a sourced theorem's equality case**,
done with exact integers (never floats), for k = 2..8. It is not a new
conjecture: the bound and its equality characterisation are Das–Wu Theorem 1.4
(sourced, `research/sources/das-wu-frequent-elements-2024.full.md`).

**Falsifier tested.** The structure would be falsified by a union-closed family
with `|∪F| ≥ k` whose kth-most-frequent element has frequency strictly below
`|F|/(2^{k-1}+1)`. Das–Wu Thm 1.4 rules this out generally; here the equality
case was confirmed term by term for k = 2..8 (all `|F|/(2^{k-1}+1)` attained).

```claim
id: nagel-profile-equality
statement: On the near-k-cube (F = 2^[k-1] ∪ { [k-1] ∪ {k} }, |F|=2^{k-1}+1), the exact sorted-descending abundance profile is [2^{k-2}+1 repeated k-1 times, 1]; hence the kth-most-frequent element has frequency exactly 1 = |F|/(2^{k-1}+1), and the denominators 2^{k-1}+1 are the sequence 2^n+1 (OEIS A000051).
hypotheses: F the near-k-cube, ground set [k], k >= 2
holds-here: yes
status: checked (exact integer computation via lib.uc oracle, k=2..8)
bearing: confirms the extremal object behind Nagel's kth-most-frequent bound attains equality exactly; a clean abundance-profile structure. The abundance profile is the in-scope quantity (unlike the enumeration counts 3,13,121,...).
anchor: code/out/nagel_profile.py
answers: <none>
```

*Command:* `python code/out/nagel_profile.py`
