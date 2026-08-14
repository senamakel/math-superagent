/// Joins the labelled sections that have content into one briefing.
///
/// Empty sections are dropped rather than rendered as a heading with nothing
/// under it: a child asked to act on "Research:\n\n" reasonably concludes the
/// research found nothing, which is a different claim from its not having run.
fn merge_context(sections: &[(&str, &str)]) -> String {
    let mut merged = String::new();
    for (label, body) in sections {
        if body.trim().is_empty() {
            continue;
        }
        if !merged.is_empty() {
            merged.push_str("\n\n");
        }
        let _ = write!(merged, "{label}:\n{}", body.trim());
    }
    merged
}

/// Where something working outside the loop leaves text for a later attempt.
///
/// The pattern agent used to be awaited beside the reflection, and that made
/// it a gate on the whole loop: a live run sat 33 minutes unable to start its
/// next attempt because the pattern agent it had already collected a verdict
/// beside was still working. Nothing bounds a pattern run against the loop —
/// it has its own budget of hundreds of model calls — so the gate had no
/// ceiling.
///
/// Detaching it is safe precisely because nothing in the routing decision
/// reads it: `route` turns on the reflection's verdict alone. So the run is
/// spawned, the loop proceeds on the reflection, and whatever the pattern
/// agent finds is posted here and picked up by the next attempt that asks. A
/// structural observation is worth as much one attempt later; a stalled loop
/// is not.
///
/// Human direction arrives the same way and for a stronger version of the same
/// reason. A person is slower than any support agent, so a loop that waited on
/// one would be that 33-minute gate with no bound at all. Two mailboxes are
/// therefore built from this one type — one carrying what the pattern team
/// found, one carrying what an operator asked for — and they differ only in
/// the heading their contents are rendered under.
#[derive(Clone, Default)]
pub(super) struct Mailbox(Arc<std::sync::Mutex<Vec<String>>>);

impl Mailbox {
    /// Leaves a finished report for the next attempt.
    pub(super) fn post(&self, report: String) {
        if report.trim().is_empty() {
            return;
        }
        if let Ok(mut slot) = self.0.lock() {
            slot.push(report);
        }
    }

    /// Takes every report that has arrived since the last collection.
    ///
    /// More than one can be waiting when a pattern run outlives the attempt
    /// that started it, which is the normal case now that they are detached.
    pub(super) fn collect(&self) -> String {
        let Ok(mut slot) = self.0.lock() else {
            return String::new();
        };
        let reports = std::mem::take(&mut *slot);
        reports.join("\n\n")
    }
}

/// What the loop is handed by the work running beside it.
///
/// Grouped rather than passed as two more parameters, because they are one
/// idea: everything that reaches an attempt without the loop having asked for
/// it arrives through a mailbox, and a third one — a second kind of team, an
/// operator channel that is not text — belongs in here rather than in `run`'s
/// signature.
#[derive(Clone)]
pub(super) struct Mailboxes {
    /// What the standing teams and the detached literature sweep found,
    /// drained by the attempt.
    ///
    /// The reflection drained it too until the pattern agent moved onto the
    /// evaluation fan-out, where it is awaited rather than posted. What is left
    /// here is what genuinely arrives on its own schedule, and the attempt is
    /// the only thing that should read that.
    pub(super) patterns: Mailbox,
    /// What a person asked for, drained by the attempt alone.
    pub(super) directives: Mailbox,
    /// The lemmas that would suffice to prove the goal, drained by the attempt
    /// alone.
    ///
    /// The third one this struct's own doc anticipated. It carries open gaps
    /// rather than prose, and it is separate from `patterns` for the reason
    /// `directives` is: a target and a piece of gathered material are different
    /// kinds of thing, and one mailbox cannot render both under the right
    /// heading.
    pub(super) skeletons: Mailbox,
}






/// Pulls the `LESSON:` line out of a reflection, falling back to the whole text.
fn extract_lesson(reflection: &str) -> String {
    for line in reflection.lines() {
        let trimmed = line.trim();
        if let Some(rest) = trimmed
            .strip_prefix("LESSON:")
            .or_else(|| trimmed.strip_prefix("lesson:"))
        {
            let lesson = rest.trim();
            if !lesson.is_empty() {
                return lesson.to_string();
            }
        }
    }
    let condensed = reflection.trim();
    if condensed.is_empty() {
        "The reflection step returned nothing usable.".to_string()
    } else {
        condensed.chars().take(400).collect()
    }
}
