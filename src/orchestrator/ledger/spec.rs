//! What a ledger *is*, as data rather than as a Rust module.
//!
//! The nine derived ledgers are each a module: a source to walk, a block to
//! parse, statuses to fold, sections to render. That is right for the ones that
//! reason — `closure` computes a transitive closure, `blueprint` finds cycles —
//! and it is overhead for the ones that do not. `threads`, `approaches`,
//! `backward` and `weakened` are the same shape four times: read one file per
//! item, parse a fenced block, group by status, render a bounded table and some
//! bounded lists.
//!
//! The cost of that is not duplication, which is tolerable. It is that **a run
//! cannot make one**. When a live workspace needed an axis nobody had
//! anticipated it built the axis by hand and badly: `docs/ledgers.md` records a
//! `research/folds/` folder that nobody designed, holding `game-core.md`,
//! `passes.md`, `counting-arithmetic.md` and `deadends.md` — a run needing
//! topic-shaped notes so badly it invented them outside the schema. `threads`
//! was written in response, months later. That will happen again, and the
//! answer should not be another Rust module each time.
//!
//! So a ledger is a [`LedgerSpec`]: a declaration the runtime compiles in for
//! the ones it ships with, and reads from `config/ledgers/` for the ones a run
//! writes. The engine renders both the same way.
//!
//! # What a declaration deliberately cannot do
//!
//! - **It cannot reason.** [`Check`] is a closed set covering the faults the
//!   built-ins already report — a thread resting on a claim id nobody wrote, a
//!   closed approach with no reason. There is no expression language, and there
//!   should not be: `closure`'s fixed point and `blueprint`'s cycle detection
//!   are arguments about mathematics, not configuration.
//! - **It cannot raise a bound.** Every cap is clamped against
//!   [`super::budget`] when the spec is read, so a run cannot declare its way
//!   back to an 86 KB file.
//! - **It cannot reach a system prompt.** Those are assembled once at container
//!   start, so a ledger created mid-run could not reach one even if the engine
//!   tried. Nothing tries. The way in is `list_ledgers`, then `read_ledger`.

use serde_json::Value;

use crate::agent::Result;

/// Where a ledger's entries live.
#[derive(Clone, Debug, PartialEq, Eq)]
pub(in crate::orchestrator) enum Source {
    /// An append-only JSONL file, one complete line per event.
    ///
    /// The construction [`super::super::board`] and [`crate::directives`] both
    /// use, for the reason they both give: one `write_all` of one whole line on
    /// a handle opened for append, so concurrent writers interleave whole lines
    /// and never halves of one, and no lock is needed.
    ///
    /// Events fold into current state rather than replacing it, which is what
    /// makes *what was done and why* survivable. `TASKS.md` was rewritten
    /// wholesale forty-eight times on one workspace — 1,647 lines written to
    /// reach a net 165 — and every rewrite silently deleted the finished items.
    Queue { path: String },
    /// A directory holding one file per entry, each carrying a fenced block.
    ///
    /// What `threads`, `approaches`, `backward` and `weakened` already are. Two
    /// writers never conflict on content because they write different files;
    /// they conflict only on the render, which `worklock` serialises.
    Items { dir: String, block: String },
    /// A file some other module derives, readable but not writable here.
    ///
    /// The nine keep their own modules — they carry checks a declaration cannot
    /// express — and are registered anyway so `list_ledgers` and `read_ledger`
    /// reach every ledger uniformly rather than reaching eight of them.
    Derived,
}

/// What a field is for, which is what the engine needs to know about it.
///
/// A name alone would make the engine guess which field is the identity and
/// which is prose to truncate, and guessing wrong is how a ledger renders its
/// id truncated and its essay whole.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(in crate::orchestrator) enum Role {
    /// The entry's identity. Exactly one per spec.
    Id,
    /// The one-line summary a table row and an index line carry.
    Title,
    /// Which of [`LedgerSpec::statuses`] the entry is in.
    Status,
    /// Long text: truncated in every rendered section, whole through
    /// `read_ledger`.
    Prose,
    /// Ids or paths this entry points at, comma separated.
    Refs,
}

/// One field of an entry.
#[derive(Clone, Debug)]
pub(in crate::orchestrator) struct Field {
    pub(in crate::orchestrator) name: String,
    pub(in crate::orchestrator) role: Role,
    /// Whether an entry missing this field is a reported fault.
    pub(in crate::orchestrator) required: bool,
}

/// One status an entry may be in.
#[derive(Clone, Debug)]
pub(in crate::orchestrator) struct StatusSpec {
    pub(in crate::orchestrator) name: String,
    /// Whether this status ends the entry's life.
    ///
    /// A closed entry is kept and rendered, never deleted — the dead-thread
    /// argument, which is the same one everywhere in this runtime: a known dead
    /// end is a result, and the reason it closed is the only thing that stops
    /// the next role paying for it again.
    pub(in crate::orchestrator) closed: bool,
    /// Whether closing into this status demands a reason.
    pub(in crate::orchestrator) needs_reason: bool,
}

/// The order a section lists its rows in.
///
/// Two values, and it must stay two. The reason is the same one that keeps
/// [`Check`] a closed set: a section that could declare a sort *expression*
/// would be configuration deciding what a role works on next, which is a
/// question about the run rather than about layout.
#[derive(Clone, Copy, Debug, Default, PartialEq, Eq)]
pub(in crate::orchestrator) enum Order {
    /// First-seen order: the order ids arrived in the source.
    ///
    /// The default, so a ledger that says nothing renders exactly as it did
    /// before this existed.
    #[default]
    Recorded,
    /// Most-recently-touched first: by the position of the entry's *last*
    /// event, not the first.
    ///
    /// A live conjecture run is why. A human directive reached the `director`,
    /// which filed the new work correctly and then reported that it had no way
    /// to put it where a reader would see it — the fresh, higher-priority task
    /// rendered *below* a stale one under a blurb reading "In order. Work the
    /// first one you can." `docs/ledgers.md` has the quote.
    ///
    /// Last-event rather than newest-created, deliberately: because
    /// `record_entry` merges into an existing id, an old task that is still the
    /// most important is re-prioritised by recording an event against it, with
    /// a tool every writing role already holds. Newest-created would fix the
    /// arriving task and permanently bury that one.
    Recent,
}

/// The order names a spec and `read_ledger` both accept.
///
/// One list, so the message a bad `sort` returns and the message a bad `order`
/// returns cannot drift apart.
pub(in crate::orchestrator) const ORDERS: [&str; 2] = ["recorded", "recent"];

/// Reads an order name, or says which ones exist.
///
/// The discovery path the `ledger` argument already uses: a caller that guessed
/// learns the real names from the failure, in one turn.
///
/// # Errors
///
/// Returns an error when `name` is not one of [`ORDERS`]. Never falls back
/// silently — a mistyped order would otherwise render a section in an order
/// nobody asked for and nothing would say so.
pub(in crate::orchestrator) fn order(name: &str) -> Result<Order> {
    match name.trim() {
        "recorded" => Ok(Order::Recorded),
        "recent" => Ok(Order::Recent),
        other => Err(invalid(&format!(
            "`{other}` is not an order; use {}",
            ORDERS
                .iter()
                .map(|name| format!("`{name}`"))
                .collect::<Vec<_>>()
                .join(" or ")
        ))),
    }
}

/// One rendered section of the derived file.
#[derive(Clone, Debug)]
pub(in crate::orchestrator) struct Section {
    pub(in crate::orchestrator) heading: String,
    /// The sentence under the heading saying what the section is for.
    pub(in crate::orchestrator) blurb: String,
    /// Statuses whose entries appear here. Empty means every status.
    pub(in crate::orchestrator) statuses: Vec<String>,
    /// Rows this section renders, already clamped against [`super::budget`].
    pub(in crate::orchestrator) cap: usize,
    /// The order those rows appear in. See [`Order`].
    pub(in crate::orchestrator) order: Order,
}

/// A fault the engine checks for, from a closed set.
#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub(in crate::orchestrator) enum Check {
    /// An entry missing a field marked required.
    RequiredField,
    /// An entry whose status is not one the spec declares.
    KnownStatus,
    /// An entry closed into a `needs_reason` status with no reason given.
    ClosedNeedsReason,
}

/// A ledger, declared.
#[derive(Clone, Debug)]
pub(in crate::orchestrator) struct LedgerSpec {
    pub(in crate::orchestrator) slug: String,
    pub(in crate::orchestrator) title: String,
    pub(in crate::orchestrator) purpose: String,
    pub(in crate::orchestrator) source: Source,
    /// The rendered file. Runtime-written: no agent may edit it.
    pub(in crate::orchestrator) derived: String,
    pub(in crate::orchestrator) fields: Vec<Field>,
    pub(in crate::orchestrator) statuses: Vec<StatusSpec>,
    pub(in crate::orchestrator) sections: Vec<Section>,
    pub(in crate::orchestrator) checks: Vec<Check>,
    /// Roles that may write. Empty means every role holding the tool.
    pub(in crate::orchestrator) writers: Vec<String>,
    /// How this ledger is actually written, in a sentence.
    ///
    /// The write guard refuses an edit to a derived file and has to say what to
    /// do instead, and *what to do instead is not the same for every ledger*.
    /// A `queue` or `items` ledger takes `record_entry`; a [`Source::Derived`]
    /// one does not, and telling its caller otherwise sends them to a tool that
    /// refuses them a second time.
    ///
    /// That is not hypothetical. A live run had the librarian try to write
    /// `teams/BOARD.md`; the guard correctly refused and told it to use
    /// `record_entry` with `ledger: "board"` — which would also have been
    /// refused, because the board is rendered by its own module and is written
    /// with `post_board`. One wasted call that time, because the role did not
    /// retry. A role that believed the message would have spent two.
    ///
    /// So the answer travels with the declaration rather than being assumed at
    /// the point of refusal.
    pub(in crate::orchestrator) written_by: String,
    /// Whether the runtime ships this one.
    ///
    /// A built-in may not be retired and its slug may not be shadowed, so that
    /// a run cannot redefine `tasks` into something that is not a task list and
    /// leave every prompt mentioning it wrong.
    pub(in crate::orchestrator) builtin: bool,
}

impl LedgerSpec {
    /// The field carrying the entry's identity, if the spec declares one.
    pub(in crate::orchestrator) fn id_field(&self) -> Option<&Field> {
        self.fields.iter().find(|field| field.role == Role::Id)
    }

    /// The field carrying the one-line summary, if the spec declares one.
    pub(in crate::orchestrator) fn title_field(&self) -> Option<&Field> {
        self.fields.iter().find(|field| field.role == Role::Title)
    }

    /// The field carrying the status, if the spec declares one.
    pub(in crate::orchestrator) fn status_field(&self) -> Option<&Field> {
        self.fields.iter().find(|field| field.role == Role::Status)
    }

    /// The order `read_ledger` uses when the call does not name one.
    ///
    /// The first section's, because that is the ledger's own answer to what a
    /// reader arriving at it wants first — for `tasks`, "Do next". A per-call
    /// `sort` overrides it; a ledger declaring no sections gets
    /// [`Order::Recorded`], which is what every ledger did before ordering
    /// existed.
    pub(in crate::orchestrator) fn default_order(&self) -> Order {
        self.sections.first().map_or(Order::default(), |section| section.order)
    }

    /// Whether `status` is one this spec declares.
    pub(in crate::orchestrator) fn knows_status(&self, status: &str) -> bool {
        self.statuses
            .iter()
            .any(|declared| declared.name.eq_ignore_ascii_case(status))
    }

    /// The declaration for `status`, if there is one.
    pub(in crate::orchestrator) fn status(&self, status: &str) -> Option<&StatusSpec> {
        self.statuses
            .iter()
            .find(|declared| declared.name.eq_ignore_ascii_case(status))
    }

    /// Whether `role` may write to this ledger.
    ///
    /// Checked in the tool rather than at registration, because the set of
    /// ledgers is not fixed when the tools are registered — a run may define
    /// one afterwards. Granting `record_entry` is therefore not the same as
    /// granting write access to everything, which is the distinction that keeps
    /// the reflection role from filing tasks and the director from filing
    /// claims.
    pub(in crate::orchestrator) fn writable_by(&self, role: &str) -> bool {
        self.writers.is_empty() || self.writers.iter().any(|writer| writer == role)
    }
}

/// Reads a declaration from JSON, clamping every bound and refusing nonsense.
///
/// Hand-written rather than derived because this crate has no direct `serde`
/// dependency — the reason [`super::super::authoring`] gives for the same
/// choice. It also means every field is validated on the way in rather than
/// deserialized and checked afterwards, which is where a `cap` of four billion
/// would otherwise get through.
///
/// # Errors
///
/// Returns an error when a required key is missing or empty, when the source is
/// not one of the three kinds, when no field carries an id, or when a section
/// names a status the spec does not declare. Each of those would produce a
/// ledger that renders but says nothing, which is worse than one that refuses.
pub(in crate::orchestrator) fn parse(document: &Value, builtin: bool) -> Result<LedgerSpec> {
    let slug = required_slug(document, "slug")?;
    let source = parse_source(document)?;
    let fields = parse_fields(document)?;
    if !fields.iter().any(|field| field.role == Role::Id) {
        return Err(invalid(
            "a ledger needs one field with role `id`; without it nothing can name an entry to \
             close it",
        ));
    }
    let statuses = parse_statuses(document)?;
    let sections = parse_sections(document, &statuses)?;
    Ok(LedgerSpec {
        title: string(document, "title").unwrap_or_else(|| slug.clone()),
        purpose: string(document, "purpose").unwrap_or_default(),
        derived: string(document, "derived")
            .ok_or_else(|| invalid("a ledger needs a `derived` path to render into"))?,
        slug,
        source,
        fields,
        statuses,
        sections,
        checks: parse_checks(document),
        writers: strings(document, "writers"),
        // A declared ledger is always `queue` or `items` — `parse_source`
        // accepts `derived` but `registry::rejected` refuses it from a run — so
        // the default is the one that is right for everything a run can
        // declare, and only the built-ins ever need to override it.
        written_by: string(document, "written_by").unwrap_or_else(|| {
            "`record_entry` to add or amend a row, `close_entry` to close one".to_string()
        }),
        builtin,
    })
}

fn invalid(message: &str) -> tinyagents::TinyAgentsError {
    tinyagents::TinyAgentsError::Validation(message.to_string())
}

fn string(document: &Value, key: &str) -> Option<String> {
    document
        .get(key)
        .and_then(Value::as_str)
        .map(str::trim)
        .filter(|value| !value.is_empty())
        .map(ToOwned::to_owned)
}

fn strings(document: &Value, key: &str) -> Vec<String> {
    document
        .get(key)
        .and_then(Value::as_array)
        .map(|items| {
            items
                .iter()
                .filter_map(Value::as_str)
                .map(str::trim)
                .filter(|value| !value.is_empty())
                .map(ToOwned::to_owned)
                .collect()
        })
        .unwrap_or_default()
}

/// Reads a slug and holds it to what a filename and a tool argument can carry.
///
/// Lowercase, digits and hyphens. A slug reaches the filesystem as
/// `config/ledgers/<slug>.json`, so anything else is a traversal question
/// nobody should have to think about again.
fn required_slug(document: &Value, key: &str) -> Result<String> {
    let value = string(document, key).ok_or_else(|| invalid("a ledger needs a `slug`"))?;
    if value.len() > 48
        || !value
            .chars()
            .all(|character| character.is_ascii_lowercase() || character.is_ascii_digit() || character == '-')
    {
        return Err(invalid(
            "a ledger slug is lowercase letters, digits and hyphens, up to 48 characters",
        ));
    }
    Ok(value)
}

fn parse_source(document: &Value) -> Result<Source> {
    match string(document, "source").as_deref() {
        Some("queue") => Ok(Source::Queue {
            path: string(document, "path")
                .ok_or_else(|| invalid("a queue ledger needs a `path` to append to"))?,
        }),
        Some("items") => Ok(Source::Items {
            dir: string(document, "dir")
                .ok_or_else(|| invalid("an items ledger needs a `dir` holding one file per entry"))?,
            block: string(document, "block")
                .ok_or_else(|| invalid("an items ledger needs a `block` naming its fenced block"))?,
        }),
        Some("derived") => Ok(Source::Derived),
        _ => Err(invalid(
            "a ledger `source` is `queue` (an append-only jsonl), `items` (one file per entry), \
             or `derived` (rendered by its own module)",
        )),
    }
}

fn parse_fields(document: &Value) -> Result<Vec<Field>> {
    let Some(items) = document.get("fields").and_then(Value::as_array) else {
        return Err(invalid("a ledger needs a `fields` list"));
    };
    items
        .iter()
        .map(|item| {
            let name = string(item, "name").ok_or_else(|| invalid("every field needs a `name`"))?;
            let role = match string(item, "role").as_deref() {
                Some("id") => Role::Id,
                Some("title") => Role::Title,
                Some("status") => Role::Status,
                Some("refs") => Role::Refs,
                Some("prose") | None => Role::Prose,
                Some(other) => {
                    return Err(invalid(&format!(
                        "`{other}` is not a field role; use id, title, status, prose or refs"
                    )));
                }
            };
            Ok(Field {
                name,
                role,
                required: item
                    .get("required")
                    .and_then(Value::as_bool)
                    .unwrap_or(false),
            })
        })
        .collect()
}

fn parse_statuses(document: &Value) -> Result<Vec<StatusSpec>> {
    let items = document
        .get("statuses")
        .and_then(Value::as_array)
        .ok_or_else(|| invalid("a ledger needs a `statuses` list"))?;
    let statuses: Vec<StatusSpec> = items
        .iter()
        .filter_map(|item| {
            Some(StatusSpec {
                name: string(item, "name")?,
                closed: item.get("closed").and_then(Value::as_bool).unwrap_or(false),
                needs_reason: item
                    .get("needs_reason")
                    .and_then(Value::as_bool)
                    .unwrap_or(false),
            })
        })
        .collect();
    if statuses.is_empty() {
        return Err(invalid("a ledger needs at least one status"));
    }
    Ok(statuses)
}

fn parse_sections(document: &Value, statuses: &[StatusSpec]) -> Result<Vec<Section>> {
    let Some(items) = document.get("sections").and_then(Value::as_array) else {
        return Ok(Vec::new());
    };
    items
        .iter()
        .map(|item| {
            let named = strings(item, "statuses");
            if let Some(unknown) = named
                .iter()
                .find(|name| !statuses.iter().any(|status| &&status.name == name))
            {
                return Err(invalid(&format!(
                    "section `{}` filters on status `{unknown}`, which this ledger does not \
                     declare — the section would always be empty",
                    string(item, "heading").unwrap_or_default()
                )));
            }
            Ok(Section {
                heading: string(item, "heading")
                    .ok_or_else(|| invalid("every section needs a `heading`"))?,
                blurb: string(item, "blurb").unwrap_or_default(),
                statuses: named,
                // Clamped, not trusted. A declaration that could raise its own
                // bound would be a second route back to the file this whole
                // module exists to prevent.
                cap: item
                    .get("cap")
                    .and_then(Value::as_u64)
                    .and_then(|cap| usize::try_from(cap).ok())
                    .unwrap_or(super::budget::MAX_LISTED)
                    .min(super::budget::MAX_LISTED),
                // Parsed and reported like every other spec fault, never
                // defaulted past: a section silently rendering in an order
                // nobody declared is the failure this option exists to fix,
                // arrived at from the other direction.
                order: match item.get("order") {
                    Some(value) => order(value.as_str().unwrap_or_default())?,
                    None => Order::default(),
                },
            })
        })
        .collect()
}

fn parse_checks(document: &Value) -> Vec<Check> {
    strings(document, "checks")
        .iter()
        .filter_map(|name| match name.as_str() {
            "required-field" => Some(Check::RequiredField),
            "known-status" => Some(Check::KnownStatus),
            "closed-needs-reason" => Some(Check::ClosedNeedsReason),
            _ => None,
        })
        .collect()
}

#[cfg(test)]
#[path = "spec_test.rs"]
mod test;
