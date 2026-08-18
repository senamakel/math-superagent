import Mathlib

open List

namespace PE1006Probe

def fibWord : ℕ → List Bool
  | 0   => [false]
  | 1   => [false, true]
  | n+2 => fibWord (n+1) ++ fibWord n

def decVal : List Bool → ℕ
  | []     => 0
  | b :: bs => (if b then 1 else 0) * 10 ^ bs.length + decVal bs

-- Distinct length-k windows of a single finite word, as a Finset (computable).
def windowsFinset (w : List Bool) (k : ℕ) : Finset (List Bool) :=
  (Finset.range (w.length + 1)).image (fun i => (w.drop i).take k)

-- 1. fibWord 5 must equal S_5 = S_4 S_3 = 01001010 01001 = 0100101001001
-- (as digits: 0 1 0 0 1 0 1 0 0 1 0 0 1)
#eval fibWord 5 = [false, true, false, false, true, false, true, false, false, true, false, false, true]

-- 2. distinct length-3 windows of S_5 must be exactly {001,010,100,101}
#eval (windowsFinset (fibWord 5) 3) =
  { [false, false, true], [false, true, false], [true, false, false], [true, false, true] }

-- 3. cardinality is 4 = k+1
#eval (windowsFinset (fibWord 5) 3).card = 4

-- 4. Ψ(3) = 1² + 10² + 100² + 101² = 20302
#eval (windowsFinset (fibWord 5) 3).sum (fun x => (decVal x) ^ 2) = 20302

-- 5. Ψ(10) mod M = 10699667 (windows of S_13, which is long enough: |S_13| = F_15 = 610 > 2·10)
#eval ((windowsFinset (fibWord 13) 10).sum (fun x => (decVal x) ^ 2)) % 101001001 = 10699667

end PE1006Probe
