//! The six tools every ledger shares.
//!
//! # Six tools, not six per ledger
//!
//! The tool set is fixed for the duration of a run —
//! `tinyagents::harness::agent_loop::run_loop` builds the schema vec once,
//! with a regression test keeping it that way — so a ledger a run defines
//! halfway through cannot get a tool of its own, and cannot appear in an `enum`
//! inside anybody else's schema either. Both would be invisible until the next
//! container.
//!
//! That constraint is the design rather than an obstacle to it. `ledger` is a
//! plain string, validated against the registry at call time, and a slug that
//! does not exist comes back as an error listing the ones that do. So the tool
//! surface does not change when a ledger is added — only what the tools accept
//! — and a run can define an axis and record into it in the same turn.
//!
//! # What the tools do not decide
//!
//! Write authority is the *spec's*, checked here, not the registry's. Holding
//! `record_entry` is not permission to write every ledger: the acting role is
//! baked into the tool at construction — never an argument, on `post_board`'s
//! reasoning — and each spec names the roles that may write it. That is what
//! keeps the judge out of the task list without needing a tool per ledger.

use std::sync::Arc;

use async_trait::async_trait;
use serde_json::{Map, Value, json};

use super::{engine, registry};
use crate::agent::{Result, Tool, ToolCall, ToolResult, ToolSchema};
use crate::orchestrator::documents::WorkspaceDocuments;

/// Which of the six a tool instance is.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(crate) enum Kind {
    List,
    Read,
    Record,
    Close,
    Define,
    Retire,
}

/// One of the ledger tools, bound to a workspace and an acting role.
#[derive(Debug)]
pub(crate) struct LedgerTool {
    kind: Kind,
    documents: WorkspaceDocuments,
    /// The role this instance acts as. See the module documentation.
    role: String,
}

impl LedgerTool {
    /// The read-only pair, granted with the document tools to every role.
    ///
    /// Reading what the run already recorded is how a role avoids recording it
    /// again, which is the argument `docs/roles.md` makes for granting recall
    /// broadly rather than narrowly.
    pub(in crate::orchestrator) fn readers(
        documents: &WorkspaceDocuments,
        role: &str,
    ) -> Vec<Arc<dyn Tool<()>>> {
        [Kind::List, Kind::Read]
            .into_iter()
            .map(|kind| Self::one(kind, documents, role))
            .collect()
    }

    /// The writing tools, granted to the roles that decide what the run does.
    pub(in crate::orchestrator) fn writers(
        documents: &WorkspaceDocuments,
        role: &str,
    ) -> Vec<Arc<dyn Tool<()>>> {
        [Kind::Record, Kind::Close]
            .into_iter()
            .map(|kind| Self::one(kind, documents, role))
            .collect()
    }

    /// The two that change the registry itself.
    ///
    /// Narrower than the writing tools on purpose. Recording into an axis is
    /// ordinary work; deciding the run needs a new axis is a planning decision,
    /// and a runtime where every role can add one grows an axis per attempt.
    pub(in crate::orchestrator) fn keepers(
        documents: &WorkspaceDocuments,
        role: &str,
    ) -> Vec<Arc<dyn Tool<()>>> {
        [Kind::Define, Kind::Retire]
            .into_iter()
            .map(|kind| Self::one(kind, documents, role))
            .collect()
    }

    fn one(kind: Kind, documents: &WorkspaceDocuments, role: &str) -> Arc<dyn Tool<()>> {
        Arc::new(Self {
            kind,
            documents: documents.clone(),
            role: role.to_string(),
        })
    }

    /// Resolves a slug, or reports what the workspace actually has.
    ///
    /// The error is the discovery path. A model that guessed `todos` learns the
    /// ledger is called `tasks` from the failure, in one turn, rather than
    /// calling `list_ledgers` it may not have thought to call.
    fn spec(&self, slug: &str) -> Result<super::spec::LedgerSpec> {
        let root = self.documents.root();
        registry::find(root, slug).ok_or_else(|| {
            let available: Vec<String> = registry::all(root)
                .0
                .into_iter()
                .map(|spec| spec.slug)
                .collect();
            tinyagents::TinyAgentsError::Validation(format!(
                "there is no ledger called `{slug}`. This workspace has: {}",
                available.join(", ")
            ))
        })
    }

    /// Re-renders a ledger's derived file after a write.
    ///
    /// Beside the write rather than at a call site, for the reason
    /// `super::super::board` records: a second posting path that forgot to
    /// render left `teams/BOARD.md` never written at all while the queue held
    /// both posts, so the board every school was told to read did not exist.
    ///
    /// Best effort, like every ledger refresh: a file that will not render must
    /// not fail the write that succeeded.
    async fn rerender(&self, spec: &super::spec::LedgerSpec) -> String {
        if matches!(spec.source, super::spec::Source::Derived) {
            return String::new();
        }
        let entries = engine::collect(self.documents.root(), spec);
        let rendered = engine::render(spec, &entries);
        if self
            .documents
            .write_runtime(&spec.derived, &rendered)
            .await
            .is_err()
        {
            return format!(" (`{}` could not be re-rendered)", spec.derived);
        }
        let faults = if entries.faults.is_empty() {
            String::new()
        } else {
            format!(
                ", with {} entr{} reported as faulty in it",
                entries.faults.len(),
                if entries.faults.len() == 1 { "y" } else { "ies" }
            )
        };
        format!(" and re-derived `{}`{faults}", spec.derived)
    }

    /// Refuses a write the acting role is not allowed to make.
    fn permitted(&self, spec: &super::spec::LedgerSpec) -> Result<()> {
        if spec.writable_by(&self.role) {
            return Ok(());
        }
        Err(tinyagents::TinyAgentsError::Validation(format!(
            "`{}` may be written by {}, and this is the `{}` role",
            spec.slug,
            spec.writers.join(", "),
            self.role
        )))
    }
}

#[async_trait]
impl Tool<()> for LedgerTool {
    fn name(&self) -> &'static str {
        match self.kind {
            Kind::List => "list_ledgers",
            Kind::Read => "read_ledger",
            Kind::Record => "record_entry",
            Kind::Close => "close_entry",
            Kind::Define => "define_ledger",
            Kind::Retire => "retire_ledger",
        }
    }

    fn description(&self) -> &'static str {
        match self.kind {
            Kind::List => {
                "Lists every ledger this workspace keeps — what each one holds, what it is called, \
                 and which file it renders into. Call it when you do not know where something \
                 belongs, before writing a note that duplicates a ledger the run already has."
            }
            Kind::Read => {
                "Reads entries out of one ledger, in full and unabridged. The rendered files in \
                 your prompt are shortened; this is where the whole reason an approach was \
                 refuted, or the whole statement of a claim, actually lives. Filter by status or \
                 by id, or search the text."
            }
            Kind::Record => {
                "Records or updates one entry in a ledger — a task to do, a sub-goal, a row in an \
                 axis this run defined. Fields you do not mention are left alone, so changing one \
                 thing costs one field rather than a rewrite of the file. Use this instead of \
                 editing the rendered file, which is derived and will overwrite your edit."
            }
            Kind::Close => {
                "Closes one entry, with the reason it closed. Say what came of it: a finished \
                 task whose outcome nobody recorded, or a route abandoned without saying why, is \
                 work this run will pay for a second time. Closed entries are kept and stay \
                 readable — that is the point of closing rather than deleting."
            }
            Kind::Define => {
                "Declares a new ledger, when this investigation needs an axis none of the existing \
                 ones carries. Prefer an existing ledger: a second place to put something is a \
                 second place to look for it. Define one when you find yourself writing the same \
                 shape of note over and over into a folder nobody designed."
            }
            Kind::Retire => {
                "Retires a ledger this run defined. The entries stay on disk — only the \
                 declaration goes, so nothing recorded is lost."
            }
        }
    }

    fn schema(&self) -> ToolSchema {
        // `ledger` is a string rather than an enum of slugs, and must stay one:
        // the schema is built once per run, so an enum could not name a ledger
        // defined after the container started. See the module documentation.
        let ledger = json!({
            "type": "string",
            "description": "The ledger's slug, as `list_ledgers` reports it — for example `tasks`, \
                            `goals`, or `approaches`."
        });
        let parameters = match self.kind {
            Kind::List => json!({
                "type": "object",
                "properties": {},
                "additionalProperties": false
            }),
            Kind::Read => json!({
                "type": "object",
                "properties": {
                    "ledger": ledger,
                    "status": {
                        "type": "string",
                        "description": "Only entries in this status. Optional."
                    },
                    "id": {
                        "type": "string",
                        "description": "One entry, by id. Optional."
                    },
                    "query": {
                        "type": "string",
                        "description": "Only entries whose text contains this. Optional."
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Entries to return. Optional; bounded whatever you ask for."
                    }
                },
                "required": ["ledger"],
                "additionalProperties": false
            }),
            Kind::Record => json!({
                "type": "object",
                "properties": {
                    "ledger": ledger,
                    "id": {
                        "type": "string",
                        "description": "The entry's id. Reuse an existing one to update it; a new \
                                        one creates the entry. Lowercase words joined by hyphens, \
                                        naming what the entry is about."
                    },
                    "fields": {
                        "type": "object",
                        "description": "The fields to set, as a flat object of strings. Only what \
                                        you name changes; everything else is left as it was. Use \
                                        the field names `list_ledgers` reports for that ledger."
                    }
                },
                "required": ["ledger", "id", "fields"],
                "additionalProperties": false
            }),
            Kind::Close => json!({
                "type": "object",
                "properties": {
                    "ledger": ledger,
                    "id": { "type": "string", "description": "The entry to close." },
                    "status": {
                        "type": "string",
                        "description": "The closing status this ledger declares — for a task, \
                                        `done` when it was carried out and `dropped` when it will \
                                        not be."
                    },
                    "reason": {
                        "type": "string",
                        "description": "What came of it, in a sentence or two. For a finished \
                                        task, what it established and where the evidence is. For \
                                        an abandoned one, what killed it — 'it needs f to be \
                                        D-finite and it is not' saves an attempt, 'did not work' \
                                        saves nothing."
                    }
                },
                "required": ["ledger", "id", "status", "reason"],
                "additionalProperties": false
            }),
            Kind::Define => json!({
                "type": "object",
                "properties": {
                    "slug": {
                        "type": "string",
                        "description": "Lowercase letters, digits and hyphens. How every tool will \
                                        name this ledger."
                    },
                    "title": { "type": "string", "description": "The rendered file's heading." },
                    "purpose": {
                        "type": "string",
                        "description": "What this axis holds that no existing ledger does, in a \
                                        sentence. A reader who is not you decides from this \
                                        whether an entry belongs here."
                    },
                    "source": {
                        "type": "string",
                        "enum": ["queue", "items"],
                        "description": "`queue` for many small rows that change status — a task \
                                        list. `items` for one file per entry with working notes \
                                        around it — a thread, a decomposition."
                    },
                    "path": {
                        "type": "string",
                        "description": "For `queue`: the jsonl to append to, under `config/`."
                    },
                    "dir": {
                        "type": "string",
                        "description": "For `items`: the folder of one file per entry."
                    },
                    "block": {
                        "type": "string",
                        "description": "For `items`: the fenced block each file carries."
                    },
                    "derived": {
                        "type": "string",
                        "description": "The Markdown file to render into. It becomes \
                                        runtime-written: nothing may edit it by hand."
                    },
                    "fields": {
                        "type": "array",
                        "description": "The fields an entry carries. Exactly one must have role \
                                        `id`. Roles: id, title, status, prose, refs.",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": { "type": "string" },
                                "role": {
                                    "type": "string",
                                    "enum": ["id", "title", "status", "prose", "refs"]
                                },
                                "required": { "type": "boolean" }
                            },
                            "required": ["name"],
                            "additionalProperties": false
                        }
                    },
                    "statuses": {
                        "type": "array",
                        "description": "The statuses an entry may be in. Mark the ones that end \
                                        an entry's life `closed`, and the ones that must say why \
                                        `needs_reason`.",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": { "type": "string" },
                                "closed": { "type": "boolean" },
                                "needs_reason": { "type": "boolean" }
                            },
                            "required": ["name"],
                            "additionalProperties": false
                        }
                    },
                    "sections": {
                        "type": "array",
                        "description": "How the rendered file is laid out. Each section shows the \
                                        entries in the statuses it names.",
                        "items": {
                            "type": "object",
                            "properties": {
                                "heading": { "type": "string" },
                                "blurb": { "type": "string" },
                                "statuses": { "type": "array", "items": { "type": "string" } },
                                "cap": { "type": "integer" }
                            },
                            "required": ["heading"],
                            "additionalProperties": false
                        }
                    },
                    "checks": {
                        "type": "array",
                        "description": "Faults to report: `required-field`, `known-status`, \
                                        `closed-needs-reason`.",
                        "items": {
                            "type": "string",
                            "enum": ["required-field", "known-status", "closed-needs-reason"]
                        }
                    },
                    "writers": {
                        "type": "array",
                        "description": "Roles allowed to write it. Omit or leave empty for any \
                                        role holding `record_entry`.",
                        "items": { "type": "string" }
                    }
                },
                "required": ["slug", "source", "derived", "fields", "statuses"],
                "additionalProperties": false
            }),
            Kind::Retire => json!({
                "type": "object",
                "properties": {
                    "ledger": ledger
                },
                "required": ["ledger"],
                "additionalProperties": false
            }),
        };
        ToolSchema::new(self.name(), self.description(), parameters)
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        self.schema().validate_call(&call)?;
        let output = match self.kind {
            Kind::List => self.list(),
            Kind::Read => self.read(&call.arguments)?,
            Kind::Record => self.record(&call.arguments).await?,
            Kind::Close => self.close(&call.arguments).await?,
            Kind::Define => self.define(&call.arguments).await?,
            Kind::Retire => self.retire(&call.arguments)?,
        };
        Ok(ToolResult::text(call.id, self.name(), output))
    }
}

/// Entries one `read_ledger` returns, whatever it asks for.
///
/// Generous, because this is the *pull* side: the rendered file in a prompt is
/// already bounded, and the whole reason to call this is that the bounded copy
/// was not enough. Bounding it as tightly would leave nowhere to read the full
/// text from, which is the point of the split.
const MAX_READ: usize = 20;

impl LedgerTool {
    fn list(&self) -> String {
        let root = self.documents.root();
        let (specs, faults) = registry::all(root);
        let mut out = String::from(
            "# Ledgers\n\nEvery ledger this workspace keeps. Read one with `read_ledger`, record \
             into it with `record_entry`. The rendered file is derived — never edit it by hand.\n",
        );
        for spec in specs {
            let entries = engine::collect(root, &spec);
            let count = match spec.source {
                super::spec::Source::Derived => "rendered by the runtime".to_string(),
                _ => format!("{} entr{}", entries.entries.len(), if entries.entries.len() == 1 { "y" } else { "ies" }),
            };
            let fields: Vec<&str> = spec.fields.iter().map(|field| field.name.as_str()).collect();
            let statuses: Vec<&str> = spec.statuses.iter().map(|status| status.name.as_str()).collect();
            out.push_str(&format!(
                "\n## `{}`{}\n\n{}\n\n- renders: `{}`\n- {count}\n- fields: {}\n- statuses: {}\n",
                spec.slug,
                if spec.builtin { "" } else { " (defined by this run)" },
                spec.purpose,
                spec.derived,
                fields.join(", "),
                statuses.join(", "),
            ));
        }
        for fault in faults {
            out.push_str(&format!("\n_{fault}_\n"));
        }
        out
    }

    fn read(&self, arguments: &Value) -> Result<String> {
        let slug = text(arguments, "ledger");
        let spec = self.spec(&slug)?;
        // A ledger rendered by its own module has no entries this engine can
        // read, so the honest answer is the file itself rather than an empty
        // list that reads as "the run recorded nothing".
        if matches!(spec.source, super::spec::Source::Derived) {
            let path = self.documents.root().join(&spec.derived);
            return Ok(std::fs::read_to_string(path).unwrap_or_else(|_| {
                format!(
                    "`{}` has not been rendered yet — nothing has been written to it.",
                    spec.derived
                )
            }));
        }
        let entries = engine::collect(self.documents.root(), &spec);
        let wanted_status = text(arguments, "status").to_ascii_lowercase();
        let wanted_id = text(arguments, "id");
        let query = text(arguments, "query").to_ascii_lowercase();
        let limit = arguments
            .get("limit")
            .and_then(Value::as_u64)
            .and_then(|value| usize::try_from(value).ok())
            .unwrap_or(MAX_READ)
            .clamp(1, MAX_READ);

        let matching: Vec<&engine::Entry> = entries
            .entries
            .iter()
            .filter(|entry| wanted_id.is_empty() || entry.id == wanted_id)
            .filter(|entry| wanted_status.is_empty() || entry.status(&spec) == wanted_status)
            .filter(|entry| {
                query.is_empty()
                    || entry.id.to_ascii_lowercase().contains(&query)
                    || entry
                        .fields
                        .values()
                        .any(|value| value.to_ascii_lowercase().contains(&query))
            })
            .collect();

        if matching.is_empty() {
            return Ok(format!(
                "`{slug}` holds {} entr{}, and none of them match. Statuses it uses: {}.",
                entries.entries.len(),
                if entries.entries.len() == 1 { "y" } else { "ies" },
                spec.statuses
                    .iter()
                    .map(|status| status.name.as_str())
                    .collect::<Vec<_>>()
                    .join(", ")
            ));
        }
        let shown = matching.len().min(limit);
        let mut out = format!(
            "# `{slug}` — {} of {} entr{} shown, in full\n",
            shown,
            matching.len(),
            if matching.len() == 1 { "y" } else { "ies" }
        );
        for entry in matching.iter().take(limit) {
            out.push('\n');
            out.push_str(&entry.full());
        }
        if matching.len() > shown {
            out.push_str(&format!(
                "\n_{} more match. Narrow with `status`, `id` or `query`, or raise `limit`._\n",
                matching.len() - shown
            ));
        }
        Ok(out)
    }

    async fn record(&self, arguments: &Value) -> Result<String> {
        let slug = text(arguments, "ledger");
        let spec = self.spec(&slug)?;
        self.permitted(&spec)?;
        let id = slugify(&text(arguments, "id"))?;
        let fields = flatten(arguments.get("fields"))?;
        if fields.is_empty() {
            return Err(tinyagents::TinyAgentsError::Validation(
                "`fields` is empty, so this call would record nothing".into(),
            ));
        }
        // Held across the write and the re-derivation that follows it, at the
        // tool-call boundary and never below one — `super::super::worklock`.
        let _guard = crate::orchestrator::worklock::writes().await;
        let where_written = match &spec.source {
            super::spec::Source::Queue { path } => {
                engine::append(self.documents.root(), &spec, &self.role, &id, &fields)?;
                path.clone()
            }
            super::spec::Source::Items { .. } => {
                engine::merge(self.documents.root(), &spec, &id, &fields)?
            }
            super::spec::Source::Derived => {
                return Err(tinyagents::TinyAgentsError::Validation(format!(
                    "`{slug}` is rendered from files this runtime derives, so it is not written \
                     through this tool. Write the note or the block it derives from instead."
                )));
            }
        };
        Ok(format!(
            "recorded `{id}` in `{slug}` ({where_written}){}",
            self.rerender(&spec).await
        ))
    }

    async fn close(&self, arguments: &Value) -> Result<String> {
        let slug = text(arguments, "ledger");
        let spec = self.spec(&slug)?;
        self.permitted(&spec)?;
        let id = slugify(&text(arguments, "id"))?;
        let status = text(arguments, "status");
        let reason = text(arguments, "reason");

        let Some(declared) = spec.status(&status) else {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "`{slug}` has no status `{status}`. It declares: {}",
                spec.statuses
                    .iter()
                    .map(|status| status.name.as_str())
                    .collect::<Vec<_>>()
                    .join(", ")
            )));
        };
        if !declared.closed {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "`{status}` does not close an entry in `{slug}`. Use `record_entry` to move an \
                 entry to a status it stays open in; the closing ones are: {}",
                spec.statuses
                    .iter()
                    .filter(|status| status.closed)
                    .map(|status| status.name.as_str())
                    .collect::<Vec<_>>()
                    .join(", ")
            )));
        }
        if reason.trim().is_empty() {
            return Err(tinyagents::TinyAgentsError::Validation(
                "closing an entry needs a reason. A row that does not say what came of it is \
                 worth nothing to whoever reads it next, which is the whole reason closed entries \
                 are kept."
                    .into(),
            ));
        }
        let status_field = spec.status_field().map(|field| field.name.clone());
        let Some(status_field) = status_field else {
            return Err(tinyagents::TinyAgentsError::Validation(format!(
                "`{slug}` declares no status field, so nothing on it can be closed"
            )));
        };
        let mut fields = Map::new();
        fields.insert(status_field, json!(status));
        fields.insert(engine::REASON.to_string(), json!(reason));

        let _guard = crate::orchestrator::worklock::writes().await;
        match &spec.source {
            super::spec::Source::Queue { .. } => {
                engine::append(self.documents.root(), &spec, &self.role, &id, &fields)?;
            }
            super::spec::Source::Items { .. } => {
                engine::merge(self.documents.root(), &spec, &id, &fields)?;
            }
            super::spec::Source::Derived => {
                return Err(tinyagents::TinyAgentsError::Validation(format!(
                    "`{slug}` is rendered by this runtime and is not closed through this tool"
                )));
            }
        }
        Ok(format!(
            "closed `{id}` in `{slug}` as `{status}`; it stays on the ledger with its reason{}",
            self.rerender(&spec).await
        ))
    }

    async fn define(&self, arguments: &Value) -> Result<String> {
        let _guard = crate::orchestrator::worklock::writes().await;
        let spec = registry::define(self.documents.root(), arguments)?;
        let rendered = self.rerender(&spec).await;
        Ok(format!(
            "defined the `{}` ledger, declared in `{}/{}.json`{rendered}. Record into it with \
             `record_entry` naming `{}`.",
            spec.slug,
            registry::SPEC_DIR,
            spec.slug,
            spec.slug
        ))
    }

    fn retire(&self, arguments: &Value) -> Result<String> {
        let slug = text(arguments, "ledger");
        let left = registry::retire(self.documents.root(), &slug)?;
        Ok(format!(
            "retired the `{slug}` ledger. Its entries are untouched, in `{left}`."
        ))
    }
}

/// Reads a string argument, trimmed, or the empty string.
fn text(arguments: &Value, name: &str) -> String {
    arguments
        .get(name)
        .and_then(Value::as_str)
        .unwrap_or_default()
        .trim()
        .to_string()
}

/// Holds an id to what a filename and a queue key can carry.
///
/// An items ledger writes `<dir>/<id>.md`, so this is a traversal boundary as
/// well as a tidiness one. Spaces and capitals are folded rather than refused —
/// a model that wrote `Fix The Audit` meant `fix-the-audit`, and failing the
/// call over it costs a turn to learn nothing.
fn slugify(raw: &str) -> Result<String> {
    let mut out = String::new();
    let mut last_hyphen = true;
    for character in raw.trim().chars() {
        if character.is_ascii_alphanumeric() {
            out.push(character.to_ascii_lowercase());
            last_hyphen = false;
        } else if !last_hyphen {
            out.push('-');
            last_hyphen = true;
        }
    }
    let out = out.trim_matches('-').chars().take(72).collect::<String>();
    let out = out.trim_matches('-').to_string();
    if out.is_empty() {
        return Err(tinyagents::TinyAgentsError::Validation(
            "an entry needs an id with at least one letter or digit in it".into(),
        ));
    }
    Ok(out)
}

/// Reads the `fields` object, refusing anything that is not a flat map.
///
/// A nested object would round-trip through the queue as a JSON blob and render
/// as one, which reads as data loss even though nothing is lost. Refusing says
/// so at the call, where the model can fix it.
fn flatten(value: Option<&Value>) -> Result<Map<String, Value>> {
    let Some(Value::Object(fields)) = value else {
        return Err(tinyagents::TinyAgentsError::Validation(
            "`fields` must be an object of field names to values".into(),
        ));
    };
    let mut out = Map::new();
    for (name, value) in fields {
        match value {
            Value::Null => {
                out.insert(name.clone(), Value::Null);
            }
            Value::String(text) => {
                out.insert(name.clone(), json!(text.trim()));
            }
            Value::Bool(_) | Value::Number(_) => {
                out.insert(name.clone(), json!(value.to_string()));
            }
            Value::Array(items) => {
                let joined: Vec<String> = items
                    .iter()
                    .map(|item| item.as_str().map_or_else(|| item.to_string(), ToOwned::to_owned))
                    .collect();
                out.insert(name.clone(), json!(joined.join(", ")));
            }
            Value::Object(_) => {
                return Err(tinyagents::TinyAgentsError::Validation(format!(
                    "field `{name}` is an object; a ledger field holds text, so write it out as a \
                     sentence"
                )));
            }
        }
    }
    Ok(out)
}

#[cfg(test)]
#[path = "tool_test.rs"]
mod test;
