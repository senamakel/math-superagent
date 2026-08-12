"""State the falsifier for the NO4 growth law and the avoidsC4 dead ends clearly."""
NO4 = {17: 34758006}
# If a_n/a_{n-1} ~ 3(n-10) holds, predict NO4(18):
n = 18
pred = 3*(n-10)*NO4[17]
print(f"NO4 growth law predicts NO4(18) ~ 3*(18-10)*{NO4[17]} = {pred:.0f}")
print(f"Falsifier: NO4(18) far from ~834M (law violated). n=17 enumeration took ~25 min "
      f"and counts grow ~x24 per step, so n=18 (~10 hr) is the next test if budget allows.")

# avoidsC4: the 4th-order rational fit is already refuted by integrality (next term non-integer).
# No OEIS match, no low-order recurrence (find_linear_recurrence order<=6: none).
print("avoidsC4 [1,1,2,5,15,50,202,807]: no OEIS match, no order<=6 recurrence; "
      "4th-order rational fit refuted by integrality. Closed direction.")
