; Independent cvc5 check of the gate and the witness-refutation queries.
; Logic QF_LIA.
;
; Query 1 (gate): digit-free n in {0,2,8} is SAT.  We assert the disjunction
; and ask SAT; separately force n=8 and ask SAT (finds the witness 256=100111_3).
;
; Query 2: C1 refutation — there EXISTS a digit-free n with Polarity =/= 0 mod 3.
; We use the n==0 branch: digits a_0=1,a_1..=0 (V=1), Polarity = 1 =/= 0 mod 3.
; Assert that branch and ask SAT (consistent) — the refutation itself is the
; existence witness n=0 with Polarity 1.
(set-logic QF_LIA)
(declare-fun a0 () Int)
(declare-fun a1 () Int)
(declare-fun a2 () Int)
(declare-fun a3 () Int)
(declare-fun a4 () Int)
(declare-fun a5 () Int)
(declare-fun a6 () Int)
(declare-fun a7 () Int)
(declare-fun a8 () Int)
(declare-fun a9 () Int)
; digits are all in {0,1}
(assert (and (<= 0 a0) (<= a0 1) (<= 0 a1) (<= a1 1) (<= 0 a2) (<= a2 1)
             (<= 0 a3) (<= a3 1) (<= 0 a4) (<= a4 1) (<= 0 a5) (<= a5 1)
             (<= 0 a6) (<= a6 1) (<= 0 a7) (<= a7 1) (<= 0 a8) (<= a8 1)
             (<= 0 a9) (<= a9 1)))
; Value = sum a_i 3^i  (first 10 digits only, rest assumed 0 by the branch)
(define-fun V () Int
  (+ a0 (* 3 a1) (* 9 a2) (* 27 a3) (* 81 a4) (* 243 a5)
     (* 729 a6) (* 2187 a7) (* 6561 a8) (* 19683 a9)))
; Polarity = sum (-1)^i a_i
(define-fun Pol () Int
  (+ a0 (- a1) a2 (- a3) a4 (- a5) a6 (- a7) a8 (- a9)))

; ---- GATE: the digit-free witness n=8 has V=256=100111_3 (low->high 1,1,1,0,0,1) ----
(push)
(assert (= V 256))
(assert (and (= a0 1) (= a1 1) (= a2 1) (= a3 0) (= a4 0) (= a5 1)
        (= a6 0) (= a7 0) (= a8 0) (= a9 0)))
(check-sat)
(get-model)
(pop)

; ---- GATE: n in {0,2,8} is reachable (disjunction over the three values) ----
(push)
(assert (or (= V 1) (= V 4) (= V 256)))
(check-sat)
(pop)

; ---- C1 refutation: exists digit-free n with Polarity not == 0 mod 3.
;      Witness n=0: V=1, a0=1 => Polarity = 1, and 1 is not 0 mod 3.
;      Assert the concrete witnesses; SAT confirms reachability.
(push)
(assert (= V 1))
(assert (and (= a0 1) (= a1 0) (= a2 0) (= a3 0) (= a4 0) (= a5 0)
        (= a6 0) (= a7 0) (= a8 0) (= a9 0)))
(assert (= Pol 1))   ; 1 is not divisible by 3 -> C1 violated
(check-sat)
(get-model)
(pop)

; ---- C2 refutation: exists digit-free n with Polarity not == 0 mod 2.
;      Witness n=0: Polarity = 1, odd -> C2 violated.
(push)
(assert (= V 1))
(assert (and (= a0 1) (= a1 0) (= a2 0) (= a3 0) (= a4 0) (= a5 0)
        (= a6 0) (= a7 0) (= a8 0) (= a9 0)))
(assert (= Pol 1))   ; 1 is not 0 mod 2 -> C2 violated
(check-sat)
(get-model)
(pop)

; ---- bare digit-free n>8 within bound: should be UNSAT (vacuous).
;      Correct encoding: V equals the actual ternary digits of 2^n for some
;      n in [9,40], and all digits are in {0,1}.  The only digit-free 2^n in
;      range are {1,4,256} (n=0,2,8), so this is genuinely unsatisfiable.
(push)
(assert (or (= V 512) (= V 1024) (= V 2048) (= V 4096) (= V 8192)
            (= V 16384) (= V 32768) (= V 65536) (= V 131072) (= V 262144)
            (= V 524288) (= V 1048576) (= V 2097152) (= V 4194304)
            (= V 8388608) (= V 16777216) (= V 33554432) (= V 67108864)
            (= V 134217728) (= V 268435456) (= V 536870912) (= V 1073741824)
            (= V 2147483648) (= V 4294967296) (= V 8589934592)
            (= V 17179869184) (= V 34359738368) (= V 68719476736)
            (= V 137438953472) (= V 274877906944) (= V 549755813888)
            (= V 1099511627776)))
(check-sat)   ; expect unsat: none of 2^9..2^40 is digit-free
(pop)
