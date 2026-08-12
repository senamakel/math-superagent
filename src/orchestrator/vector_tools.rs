impl RememberMemoryTool {
    pub(super) fn new(store: VectorStore) -> Self {
        Self { store }
    }
}

#[async_trait]
impl Tool<()> for RememberMemoryTool {
    fn name(&self) -> &'static str {
        "remember_memory"
    }

    fn description(&self) -> &'static str {
        "Stores a concise durable finding, lesson, decision, or failed approach in Cognee."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "A self-contained memory worth reusing across agents and runs."
                    },
                    "source": {
                        "type": "string",
                        "description": "A source URL, agent name, or short provenance label."
                    }
                },
                "required": ["text", "source"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let text = string_argument(&call, "text")?;
        let source = string_argument(&call, "source")?;
        let id = self.store.remember(&text, &source).await?;
        Ok(ToolResult::text(
            call.id,
            self.name(),
            format!("stored research note {id} from {source}"),
        ))
    }
}

#[derive(Debug)]
pub(super) struct RecallMemoryTool {
    store: VectorStore,
}

impl RecallMemoryTool {
    pub(super) fn new(store: VectorStore) -> Self {
        Self { store }
    }
}

#[async_trait]
impl Tool<()> for RecallMemoryTool {
    fn name(&self) -> &'static str {
        "recall_memory"
    }

    fn description(&self) -> &'static str {
        "Recalls shared durable findings and research plus session memory from this project/run only."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "query": { "type": "string" },
                    "limit": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 10,
                        "default": 5
                    }
                },
                "required": ["query"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let query = string_argument(&call, "query")?;
        let limit = limit_argument(&call);
        let rendered = self.store.search(&query, CHUNK_SEARCH, limit).await?;
        Ok(ToolResult::text(
            call.id,
            self.name(),
            rendered.unwrap_or_else(|| "no related research notes found".to_string()),
        ))
    }
}

/// Asks the memory what its entities are connected to, rather than which
/// passages mention them.
///
/// This is the one thing a graph memory can answer that a vector store cannot.
/// `recall_memory` returns the chunks most similar to a phrase, which is a
/// better index than a filename and no more; `relate_memory` returns the edges
/// the graph actually holds, so "what does this run connect the Moore bound to"
/// has an answer that nobody wrote down in those words. A run that only ever
/// recalls chunks is paying for a graph store and using it as a search box.
#[derive(Debug)]
pub(super) struct RelateMemoryTool {
    store: VectorStore,
}

impl RelateMemoryTool {
    pub(super) fn new(store: VectorStore) -> Self {
        Self { store }
    }
}

#[async_trait]
impl Tool<()> for RelateMemoryTool {
    fn name(&self) -> &'static str {
        "relate_memory"
    }

    fn description(&self) -> &'static str {
        "Returns what this project's memory connects a subject to — the relationships between \
         entities rather than the passages mentioning them. Use it to find a link the run \
         established but never stated in one place; use recall_memory when you want the text."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "query": { "type": "string" },
                    "limit": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 10,
                        "default": 5
                    }
                },
                "required": ["query"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let query = string_argument(&call, "query")?;
        let limit = limit_argument(&call);
        let rendered = self.store.search(&query, GRAPH_SEARCH, limit).await?;
        Ok(ToolResult::text(
            call.id,
            self.name(),
            rendered.unwrap_or_else(|| {
                "the memory holds no connections for that subject yet".to_string()
            }),
        ))
    }
}

/// Writes one provisional note where `SCRATCHPAD.md` used to be written.
///
/// The file was in three roles' system prompts, so every model call in each of
/// them paid for every number anyone had jotted down, whether or not the turn
/// was about it — and it was re-read whole to add a line. A note is written
/// once and read back by wording, which is the same trade `remember_memory`
/// makes for durable findings.
///
/// It is a separate tool rather than a flag on `remember_memory` because the
/// distinction is the one the method policy rests on. A durable memory is
/// something the run checked; a scratch note is something it has not. Sharing a
/// tool between them would leave which store a statement landed in decided by
/// an argument, mid-derivation, by the role least able to judge it.
#[derive(Debug)]
pub(super) struct NoteScratchTool {
    store: VectorStore,
}

impl NoteScratchTool {
    pub(super) fn new(store: VectorStore) -> Self {
        Self { store }
    }
}

#[async_trait]
impl Tool<()> for NoteScratchTool {
    fn name(&self) -> &'static str {
        "note_scratch"
    }

    fn description(&self) -> &'static str {
        "Records provisional work — a partial derivation, an intermediate number, a hypothesis \
         not yet checked — in this project's scratch. Nothing here is evidence: once a finding \
         survives a check, store it with remember_memory instead."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "The provisional work, self-contained enough to be read back later."
                    },
                    "topic": {
                        "type": "string",
                        "description": "A few words naming what the note is about, so it can be recalled."
                    }
                },
                "required": ["text", "topic"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let text = string_argument(&call, "text")?;
        let topic = string_argument(&call, "topic")?;
        let id = self.store.note_scratch(&text, &topic).await?;
        Ok(ToolResult::text(
            call.id,
            self.name(),
            format!("noted provisional work {id} on {topic}"),
        ))
    }
}

/// Reads the run's provisional work back, and nothing else.
#[derive(Debug)]
pub(super) struct RecallScratchTool {
    store: VectorStore,
}

impl RecallScratchTool {
    pub(super) fn new(store: VectorStore) -> Self {
        Self { store }
    }
}

#[async_trait]
impl Tool<()> for RecallScratchTool {
    fn name(&self) -> &'static str {
        "recall_scratch"
    }

    fn description(&self) -> &'static str {
        "Returns this project's provisional notes nearest a phrase — unfinished work, not \
         established results. Use recall_memory for what the run has actually checked."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "query": { "type": "string" },
                    "limit": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 10,
                        "default": 5
                    }
                },
                "required": ["query"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        let query = string_argument(&call, "query")?;
        let limit = limit_argument(&call);
        let rendered = self.store.recall_scratch(&query, limit).await?;
        Ok(ToolResult::text(
            call.id,
            self.name(),
            rendered.unwrap_or_else(|| "no provisional notes on that yet".to_string()),
        ))
    }
}
