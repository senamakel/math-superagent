//! Writes each agent's assembled system prompt to its own file.
//!
//! The prompts are the most consequential text in the runtime and were the
//! least reviewable part of it: assembled at startup from a built-in policy,
//! a role prompt, and whichever workspace files that role is entitled to, then
//! visible only in a provider trace after a run had already started. This
//! renders the same assembly on the host, without a container, an API key, or
//! spending anything.
//!
//! ```sh
//! cargo run --example dump_prompts -- workspace/conjectures/gilbreath
//! cargo run --example dump_prompts -- workspace/template --stdout | less
//! ```
//!
//! One file per agent, under that project's folder:
//!
//! ```text
//! reports/conjectures/gilbreath/prompts/SUMMARY.md
//! reports/conjectures/gilbreath/prompts/orchestrator.md
//! reports/conjectures/gilbreath/prompts/goals.md
//! …
//! ```
//!
//! A file per agent rather than one document, because the questions asked of
//! this are per-agent — *what does the judge actually see*, *did the searcher's
//! prompt grow* — and a third of a megabyte of concatenated prompts answers
//! them by scrolling. It also makes the useful diff possible: the same role
//! across two workspaces, or across two commits, is two paths.
//!
//! `SUMMARY.md` is what the single document was actually read for. It is
//! written first and lists every role with what it costs, so the overview
//! survives the split rather than being something a reader has to rebuild by
//! opening twenty-four files.
//!
//! `/reports/` is gitignored. `--stdout` prints the whole thing instead, for
//! piping.

mod common;

use std::fmt::Write as _;

/// What one role's prompt is of the whole sweep, as a percentage.
///
/// Integer arithmetic, in tenths of a percent, because the alternative is a
/// float cast lint on a number that only ever gets one decimal place printed.
fn share_of(tokens: u64, total: u64) -> String {
    if total == 0 {
        return "0.0".to_string();
    }
    let tenths = tokens.saturating_mul(1000) / total;
    format!("{}.{}", tenths / 10, tenths % 10)
}

/// What a role may call, or why the report cannot say.
///
/// A prompt never lists a role's tools: they are sent as function schemas on
/// every request, so writing them into the text would pay for them twice and
/// leave two lists to disagree. That is right for the run and unhelpful for a
/// review, which is what this section is for — what a role is told, beside what
/// it can do.
fn tools_of(report: &math_agent::PromptReport) -> String {
    if report.tools.is_empty() {
        return "_Registered directly onto this role's harness rather than declared, so the \
                registry has no list to read. See `build_planner_harness`._"
            .to_string();
    }
    report
        .tools
        .iter()
        .map(|tool| format!("- `{tool}`"))
        .collect::<Vec<_>>()
        .join("\n")
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let options = common::options("workspace/template")?;
    let path = std::path::Path::new(&options.workspace);
    if !path.is_dir() {
        return Err(format!("workspace `{}` is not a directory", options.workspace).into());
    }

    if options.to_stdout {
        println!("{}", math_agent::prompt_report(path)?);
        return Ok(());
    }

    let reports = math_agent::prompt_reports(path)?;
    let directory = common::project_dir(path)?.join("prompts");
    let total: u64 = reports.iter().map(|report| report.tokens).sum();

    let mut summary = format!(
        "# Assembled agent prompts\n\nworkspace: {}\n\n\
         Each prompt is the shared method policy, then the role's built-in prompt, then the \
         workspace files that role receives. One file per agent, beside this one.\n\n\
         | Role | Chars | ~Tokens | Share |\n| --- | ---: | ---: | ---: |\n",
        path.display()
    );
    let mut ordered: Vec<&math_agent::PromptReport> = reports.iter().collect();
    ordered.sort_by_key(|report| std::cmp::Reverse(report.tokens));
    for report in &ordered {
        let share = share_of(report.tokens, total);
        let _ = writeln!(
            summary,
            "| [`{role}`]({role}.md) | {chars} | {tokens} | {share}% |",
            role = report.role,
            chars = report.prompt.len(),
            tokens = report.tokens,
        );
    }
    let _ = write!(
        summary,
        "\n~{total} tokens across {} roles. The shared method policy is ~{} of them, repeated in \
         every one.\n",
        reports.len(),
        math_agent::shared_policy_tokens()
    );
    common::write(&directory.join("SUMMARY.md"), &summary)?;

    for report in &reports {
        let body = format!(
            "# {}\n\nworkspace: {}\n\n_{} chars, ~{} tokens_\n\n## Tools\n\n{}\n\n\
             ## Prompt\n\n```text\n{}\n```\n",
            report.role,
            path.display(),
            report.prompt.len(),
            report.tokens,
            tools_of(report),
            report.prompt
        );
        common::write(&directory.join(format!("{}.md", report.role)), &body)?;
    }

    println!("{}", directory.display());
    println!(
        "{} agent prompts, ~{total} tokens; largest {} at ~{}",
        reports.len(),
        ordered.first().map_or("none", |report| &report.role),
        ordered.first().map_or(0, |report| report.tokens),
    );
    Ok(())
}
