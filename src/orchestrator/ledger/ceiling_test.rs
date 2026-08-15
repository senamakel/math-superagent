//! What every derived ledger may cost a system prompt, asserted rather than
//! intended.
//!
//! Each of these renders a deliberately pathological workspace — far more
//! entries than a run would produce, each carrying far more prose than anybody
//! would write — and asserts the rendered file stays under a stated ceiling.
//!
//! The ceilings are the point, and so is the fixture being absurd. Every one of
//! these ledgers already had a `MAX_ROWS` and a `FIELD_CHARS` when
//! `research/APPROACHES.md` reached 86 KB on a live workspace, because those
//! two bounds governed the *table* and the list sections underneath it were
//! written later, by hand, with no bound at all. Nothing failed; the file just
//! grew, and it was a third of a 63,833-token system prompt before anybody
//! counted. A bound that is not asserted is a bound that drifts back, so this
//! is the control rather than the intention.
//!
//! A ceiling here is deliberately generous — roughly what the bounds in
//! [`super::budget`] permit, with slack for headers and blurbs. It is not a
//! target. It exists to catch a section that has escaped its bound entirely,
//! which is the failure that actually happened.

use std::fmt::Write as _;
use std::path::{Path, PathBuf};

use super::super::{approaches, backward, claims, threads, weakened};

/// Entries a fixture writes. Far past any ledger's row bound, so the caps are
/// what decides the size rather than the input.
const ENTRIES: usize = 60;

/// Characters of prose per field. A live `killed-by` reached about 5,000.
const PROSE: usize = 6_000;

fn prose(what: &str) -> String {
    format!("{what} ").repeat(PROSE / (what.len() + 1))
}

fn workspace(name: &str) -> std::io::Result<PathBuf> {
    let root = std::env::temp_dir().join(format!("math-agent-ceiling-{name}"));
    let _ = std::fs::remove_dir_all(&root);
    std::fs::create_dir_all(&root)?;
    Ok(root)
}

/// Asserts `rendered` is under `ceiling`, reporting by how much when it is not.
fn under(label: &str, rendered: &str, ceiling: usize) {
    let chars = rendered.chars().count();
    assert!(
        chars <= ceiling,
        "{label} rendered {chars} characters (~{} tokens) against a {ceiling}-character ceiling. \
         A section has escaped its bound — check that every `append_*` in that module goes \
         through `ledger::budget::listed` and truncates its prose fields.",
        chars / 4
    );
}

/// The one that actually happened: sixty closed approaches, each with a
/// refutation nobody bounded.
#[test]
fn the_approach_ledger_stays_under_its_ceiling() -> std::io::Result<()> {
    let root = workspace("approaches")?;
    std::fs::create_dir_all(root.join(approaches::APPROACHES_DIR))?;
    for index in 0..ENTRIES {
        let mut block = String::new();
        let _ = write!(
            block,
            "idea: {}\nmechanism: {}\nstatus: {}\nprecedent: \nfirst-step: {}\nkilled-by: {}",
            prose("an idea"),
            prose("a mechanism"),
            // Half closed, half open, so the closed list and the unchecked list
            // are both exercised in one render.
            if index % 2 == 0 { "refuted" } else { "proposed" },
            prose("a first step"),
            prose("the reason it died"),
        );
        std::fs::write(
            root.join(format!("{}/approach-{index}.md", approaches::APPROACHES_DIR)),
            format!("# approach-{index}\n\n```approach\n{block}\n```\n"),
        )?;
    }
    under(
        approaches::APPROACHES_PATH,
        &approaches::collect(&root).render(),
        58_000,
    );
    Ok(())
}

/// Sixty skeletons, each with open, discharged and broken gaps.
#[test]
fn the_backward_ledger_stays_under_its_ceiling() -> std::io::Result<()> {
    let root = workspace("backward")?;
    std::fs::create_dir_all(root.join(backward::BACKWARD_DIR))?;
    for index in 0..ENTRIES {
        let mut file = String::new();
        let _ = write!(
            file,
            "# skeleton-{index}\n\n```skeleton\ngoal: {}\nimplies: {}\nstatus: {}\nrests-on: \
             nothing-recorded-{index}\nkilled-by: {}\n```\n",
            prose("a goal"),
            prose("an inference"),
            if index % 3 == 0 { "broken" } else { "live" },
            prose("what broke it"),
        );
        for gap in 0..3 {
            let _ = write!(
                file,
                "\n```gap\nid: gap-{index}-{gap}\nlemma: {}\nstatus: {}\ndischarged-by: \
                 claim-{index}\nthread: \nnext: {}\n```\n",
                prose("a lemma"),
                if gap == 0 { "discharged" } else { "open" },
                prose("a first move"),
            );
        }
        std::fs::write(
            root.join(format!("{}/skeleton-{index}.md", backward::BACKWARD_DIR)),
            file,
        )?;
    }
    let ledger = claims::collect(&root);
    under(
        backward::BACKWARD_PATH,
        &backward::collect(&root).render(&ledger),
        125_000,
    );
    Ok(())
}

/// Sixty ladders, each with settled, failed and open rungs.
#[test]
fn the_weakened_ledger_stays_under_its_ceiling() -> std::io::Result<()> {
    let root = workspace("weakened")?;
    std::fs::create_dir_all(root.join(weakened::WEAKENED_DIR))?;
    for index in 0..ENTRIES {
        let mut file = String::new();
        let _ = write!(
            file,
            "# ladder-{index}\n\n```ladder\ngoal: {}\ndifficulties: alpha, beta\nstatus: open\n```\n",
            prose("a goal"),
        );
        for (rung, status) in ["settled", "failed", "open"].iter().enumerate() {
            let _ = write!(
                file,
                "\n```rung\nid: rung-{index}-{rung}\nstatement: {}\noff: alpha\nstatus: \
                 {status}\nmerge: {}\nsettled-by: claim-{index}\nfailed-by: {}\n```\n",
                prose("a weakened statement"),
                prose("how to climb off it"),
                prose("what went wrong"),
            );
        }
        std::fs::write(
            root.join(format!("{}/ladder-{index}.md", weakened::WEAKENED_DIR)),
            file,
        )?;
    }
    under(
        weakened::WEAKENED_PATH,
        &weakened::collect(&root).render(),
        168_000,
    );
    Ok(())
}

/// Two hundred claim blocks, contradicting each other and unverified.
#[test]
fn the_claim_ledger_stays_under_its_ceiling() -> std::io::Result<()> {
    let root = workspace("claims")?;
    let notes = root.join("research/notes");
    std::fs::create_dir_all(&notes)?;
    for index in 0..ENTRIES {
        let mut file = format!("# note-{index}\n");
        for claim in 0..4 {
            let _ = write!(
                file,
                "\n```claim\nid: claim-{index}-{claim}\nstatement: {}\nhypotheses: {}\n\
                 holds-here: yes\nstatus: {}\ncontradicts: claim-{index}-0\nanchor: note-{index}\n```\n",
                prose("a statement"),
                prose("its hypotheses"),
                if claim % 2 == 0 {
                    "asserted"
                } else {
                    "catalogued"
                },
            );
        }
        std::fs::write(notes.join(format!("note-{index}.md")), file)?;
    }
    under(
        claims::CLAIMS_PATH,
        &claims::collect(&root).render(),
        37_000,
    );
    Ok(())
}

/// Sixty threads, every one of them resting on a claim that is not on disk.
#[test]
fn the_thread_ledger_stays_under_its_ceiling() -> std::io::Result<()> {
    let root = workspace("threads")?;
    std::fs::create_dir_all(root.join(threads::THREADS_DIR))?;
    for index in 0..ENTRIES {
        std::fs::write(
            root.join(format!("{}/thread-{index}.md", threads::THREADS_DIR)),
            format!(
                "# thread-{index}\n\n```thread\nquestion: {}\nstatus: blocked\nrests-on: \
                 missing-{index}\nblocked-by: \nnext: {}\n```\n",
                prose("a question"),
                prose("a next move"),
            ),
        )?;
    }
    let ledger = claims::collect(&root);
    under(
        threads::THREADS_PATH,
        &threads::collect(&root).render(&ledger),
        26_000,
    );
    Ok(())
}

/// The bounds are what keeps the size flat, so trebling the input must not
/// treble the output.
///
/// A ceiling alone cannot catch a section that grows slowly — it passes until
/// one day it does not. This asserts the shape instead: past the row bound,
/// adding entries stops adding characters. Only the counts in the elision lines
/// may move, which is a few characters rather than a few thousand.
#[test]
fn past_the_bound_more_entries_do_not_grow_the_file() -> std::io::Result<()> {
    fn render_with(count: usize, name: &str) -> std::io::Result<usize> {
        let root = workspace(name)?;
        std::fs::create_dir_all(root.join(approaches::APPROACHES_DIR))?;
        for index in 0..count {
            std::fs::write(
                root.join(format!("{}/approach-{index}.md", approaches::APPROACHES_DIR)),
                format!(
                    "# approach-{index}\n\n```approach\nidea: {}\nstatus: refuted\nkilled-by: \
                     {}\n```\n",
                    prose("an idea"),
                    prose("the reason it died"),
                ),
            )?;
        }
        Ok(approaches::collect(&root).render().chars().count())
    }

    let small = render_with(60, "growth-60")?;
    let large = render_with(180, "growth-180")?;
    let growth = large.saturating_sub(small);
    assert!(
        growth < 200,
        "tripling the entries from 60 to 180 grew the render by {growth} characters \
         ({small} -> {large}). Past the row bound only the elided counts should move; a section \
         is still rendering every entry."
    );
    Ok(())
}
