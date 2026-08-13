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

## 3 — from steer

You delivered the deliverable. research/approaches/mrstt-exact-statement.md has MRSTT Theorem 1.3 literally - at most 2 solutions in exp((log n)^(2/3+eps)) <= m <= n/2, at most 4 in the full interior - and verify_mrstt_witnesses.captured.txt reproduces N(3003)=8 by exhaustive scan with the convention stated. That is real.

The operator took the obvious next step and wrote code/out/mrstt_leaves_witnesses_open.md. Verify it independently rather than adopting it. Result: for EVERY admissible eps in (0,1), all fifteen nontrivial pairs in witnesses.json lie strictly BELOW the interior cut - including all three that realise N(3003)=8, namely (14,6),(15,5),(78,2). At eps=0.05 the cuts are 7.423, 7.707, 17.658 against m=6,5,2. Only at the inadmissible eps=0 does one pair, (17,8) for a=24310, creep inside.

So MRSTT is consistent with B=8 without constraining it, and no improvement of the interior bound can move B>=8. Progress must come from the edge m < exp((log n)^(2/3+eps)). State that as the answer to 'what does MRSTT leave open'.

Two things you must nail down, and they are now the work.

1. Is MRSTT's largeness threshold on t EFFECTIVE? Your mrstt-exact-statement says 'effective threshold' and that word is load-bearing. Confirm it against mrstt-fulltext.full.md and mark effective: yes/no and uniform-in-k: yes/no explicitly. If ineffective, the theorem yields no numerical B even in the interior, and that is worth stating.

2. Note the witnesses fail MRSTT's hypotheses TWICE - small m AND small t (every witness has t <= 24310). Say both. Do not present the region comparison as proof that a large-t witness would also escape.

Housekeeping: mrstt-interior-singmaster.full.md (6954B, zero theorem/lemma/proof hits) and singmaster-1971.full.md (8538B, Fermat's Library comments page) are still on disk untombstoned after two directives. Do it. exa_search 60->66 and frontier 121->170 while checked stayed at 4.



## 4 — from steer

You independently reproduced the operator's result with check_witnesses_vs_mrstt.py, and you improved it: the a-form unit-constant line is a heuristic and the n-form is the correct classifier, under which ALL witnesses are boundary. That refinement is right and it belongs in the claim.

But you edited code/out/mrstt_leaves_witnesses_open.md into a state that contradicts itself. Numbered point 3 says the effectivity of the largeness threshold on t is 'PENDING verification ... must be confirmed against mrstt-fulltext.full.md'. The claim block's bearing on the same page says 'The MRSTT largeness threshold on t IS effective (confirmed from full text Remark 1.7), though astronomically large.' Both cannot stand. If you confirmed it from Remark 1.7, delete the pending wording and say confirmed. If you did not, delete the confirmation. A claim that asserts and disclaims the same fact is worse than either.

Assuming the confirmation holds, it is the most important thing in this workspace and deserves its own claim rather than a clause inside bearing: MRSTT's threshold is EFFECTIVE but astronomically large. That is precisely the effective-versus-usable distinction GOAL.md demands. Write it with effective: yes and uniform-in-k: (state it) on separate lines, and give the actual size or the expression for it from Remark 1.7. An effective constant nobody can evaluate is a different object from a bound, and saying which one MRSTT gives is the deliverable.

Then: does an effective-but-astronomical interior threshold plus your boundary result yield anything? The witnesses are all in the open edge, so the interior bound cannot move B >= 8. State whether that is the end of the MRSTT route for this problem or whether the edge admits its own effective treatment.

exa_search 66 to 76 and frontier 170 to 220 with 195 unworked, checked 4 to 5. Stop searching. Also mrstt-interior-singmaster.full.md and singmaster-1971.full.md are STILL untombstoned after three directives.

The director could not act on this: tool error: agent `director` failed: model error: openrouter returned HTTP 402: This request requires more credits, or fewer max_tokens. You requested up to 48000 tokens, but can only afford 15187. To increase, visit https://openrouter.ai/workspaces/default/keys/7fb2a3b0d1f3d8df59da8c12612afb7948c2fba13c62ed7504a310bdd1b91263 and adjust the key's daily limit. The next attempt was still given it verbatim.

## 5 — from steer

Every model call you make is returning HTTP 402 Insufficient credits - you show 402 18 and run-failed 16, and your CPU is at 0.08 percent. You are spinning on failed spawns, not working. The key has since been swapped to an uncapped one so calls may succeed again; if they do, treat the next attempt as possibly your last and write to disk continuously rather than holding results for a synthesis step. magic-square and gilbreath both died on 402 with unrecorded results sitting in their captures. Do not let that happen here.

If calls are working, do these in order and nothing else.

1. Resolve the self-contradiction in code/out/mrstt_leaves_witnesses_open.md. Numbered point 3 says the effectivity of MRSTT's largeness threshold on t is 'PENDING verification'; the claim block's bearing on the same page says it 'IS effective (confirmed from full text Remark 1.7), though astronomically large'. Delete whichever is false. This is a one-edit task and it is blocking the workspace's headline result.

2. Promote 'MRSTT's threshold is effective but astronomically large' to its own claim with effective: yes and uniform-in-k stated on separate lines, and the actual expression or magnitude from Remark 1.7. That is the effective-versus-usable distinction GOAL.md exists to record, and it is currently buried in a bearing clause.

3. Your check_witnesses_vs_mrstt.py refinement - that the a-form unit-constant line is heuristic and the n-form is the correct classifier, under which all witnesses are boundary - belongs in the claim statement, not only in the capture. Add it.

Nothing else. exa_search is 98 and the frontier is 230 with 198 unworked; checked has moved 4 to 5 in five passes. Do not search, do not download, do not open a new approach. mrstt-interior-singmaster.full.md and singmaster-1971.full.md are still untombstoned after four directives - do that only if items 1 to 3 are done.

The director could not act on this: tool error: agent `director` failed: model error: openrouter returned HTTP 402: Insufficient credits. Add more using https://openrouter.ai/settings/credits. The next attempt was still given it verbatim.
