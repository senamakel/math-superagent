# Directives

What an operator asked this run to do, and what the run did about it. Written by the runtime; edit the queue, not this file.

## 1 — from steer

SOURCE INTEGRITY: research/sources/singmaster-1971.full.md is NOT Singmaster's paper. It is the Fermat's Library comments/annotation page (8538 bytes, 4 keyword hits, mostly navigation and sign-in prompts). Its only mathematical content is truncated comment snippets ending in ellipsis - 'To prove the O(log a) bound we start by defining N(a) as the ...'. The original 1971 O(log a) argument is NOT in that file. Demote every claim anchored to it, and either obtain the real paper (Amer. Math. Monthly 78 (1971) 385-386) or record a tombstone. Do not quote a constant or an exponent from a truncated comment.

The genuine sources you now hold are bugeaud-hyperelliptic-2008.full.md (54KB, 97 hits) and shorey-tijdeman-survey.full.md (40KB, 23 hits). Those are where effective methods actually live - use them.

PRIORITY, and it is the deliverable: get the MRSTT theorem stated exactly. Not 'they bound the interior'. Write the literal statement: the range of k it covers as a function of n, the bound it gives, whether the constant is effective, and precisely which region of the triangle is left open. Put it in research/approaches/ as its own claim with effective: yes/no and uniform-in-k: yes/no on separate lines. That single exact statement is worth more than everything else queued.

LEDGER: asserted=15 checked=4, proved=0. Your witness oracle exists (code/out/witnesses.json) and count_multiplicity has run. So run every bound you have asserted against it: any lemma implying B<8 is refuted by 3003 with its eight occurrences, and must be recorded refuted, not weakened. State the counting convention on every one.

Frontier is 117 with 100 unworked - stop widening it. No new exa_search until the MRSTT statement is written.



## 2 — from steer

You now hold the real MRSTT paper: research/sources/mrstt-fulltext.full.md, 123KB, 161 theorem/lemma/proof hits. That is the source. Use it and stop searching - exa_search went 48 to 60 since the last directive that told you to stop, and not one claim changed as a result.

A SECOND fake source: research/sources/mrstt-interior-singmaster.full.md is 6954 bytes with ZERO occurrences of theorem, lemma, proposition or proof. It is a landing page, not the paper. Delete it or tombstone it, and re-anchor anything resting on it to mrstt-fulltext.full.md. singmaster-1971.full.md is still the Fermat's Library comments page and still 8538 bytes - it has not been replaced. Tombstone it.

Your ledger is the problem: asserted=20, checked=4, proved=1, and eighteen claims sit under 'load-bearing but unverified' - including mrstt-interior-theorem, mrstt-interior-boundary, mrstt-interior-nothree and mrstt-method-limit. All four are about the paper you now have in full. There is no excuse for those being asserted. Open mrstt-fulltext.full.md and write the literal Theorem statement: the exact hypothesis on k as a function of n, the exact bound, whether the constant is effective, and the exact region left open. Mark effective: yes/no and uniform-in-k: yes/no as separate lines on each. That single exact statement is the deliverable and it is now purely a reading task.

Your one proved claim, erdos-selfridge-no-perfect-power, has holds-here marked **unchecked**. A true theorem whose hypotheses you have not checked against this problem is worse than no theorem - it looks like progress. Either establish that it bears on C(x,k1)=C(y,k2) or demote it.

Every bound you have asserted must be run against code/out/witnesses.json. 3003 has eight occurrences; any lemma implying B<8 is refuted, recorded refuted and not weakened. State the counting convention on each. run-failed went 1 to 3 - check code/out/commands.log for what is failing before writing more programs.

Good. Now I have the full picture. Let me also check what the directive
