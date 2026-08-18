# Sequence survey final

Fresh tool_builder computation verified exactly:

- c1(k)=1+floor(k*(3-sqrt(5))/2)=1+floor(k/phi^2), for every 1<=k<=10000. First possible falsifier k=10001. OEIS lookup matches A189663 (shifted indexing).
- Lmin(k)=k+F-1, where F is least Fibonacci strictly greater than k, for every 1<=k<=10000 via independent substring oracle. First possible falsifier k=10001.
- No constant-coefficient recurrence of order <=12 was found for Psi prefix (25 terms), c1 (400 terms), or ext_recurrence final column (40 terms).
- No new exact regularity was found for Psi itself or vr_runvals.

Memory tools were unavailable during this cycle, so this remains a workspace record rather than durable memory.