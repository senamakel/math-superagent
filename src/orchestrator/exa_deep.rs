/// Hands one question to Exa's own research agent, which searches many ways
/// and reasons across what it finds.
///
/// The tier above a search rather than a better one. An ordinary `exa_search`
/// returns ten pages ranked against one phrasing and leaves the synthesis to
/// the caller; this runs its own query variations, reads across the results,
/// and returns prose with the sources it used. It costs twelve to forty seconds
/// and real money for that, which is why it is a distinct tool: a run should be
/// seen to have chosen the expensive call, and a trace where the cheap and the
/// expensive call look identical cannot show that.
///
/// # What it is not
///
/// It is not evidence, and the tool result says so in the words the run's own
/// method policy uses. What comes back is a model's synthesis of pages it read
/// and the run did not — which is exactly the shape of the failure the
/// librarian's brief was written against, a run reasoning from what a model
/// remembers rather than from what it can read. So its sources go to the
/// frontier, its prose goes in the reply, and neither is a claim until somebody
/// downloads a source and checks it. Used that way it is the best query
/// generator the run has: it names the theorems, the authors, and the
/// vocabulary that the next ordinary search and the next `citation_graph` call
/// need.
#[derive(Debug)]
pub(in crate::orchestrator) struct DeepResearchTool {
    exa: Exa,
}

#[async_trait]
impl Tool<()> for DeepResearchTool {
    fn name(&self) -> &'static str {
        "deep_research"
    }

    fn description(&self) -> &'static str {
        "Hands one hard question to Exa's research agent, which runs many searches, reads across \
         the results, and returns a synthesis with its sources. Slower and more expensive than \
         exa_search — use it for a question you cannot decompose into queries yourself, such as \
         `what is known about the smallest case nobody has settled`, not for a lookup. What comes \
         back is a synthesis of pages you have not read, so it is a lead and never a claim: its \
         sources go to the frontier, and it is at its most useful for the names, theorems, and \
         vocabulary that make your next ordinary search a good one."
    }

    fn schema(&self) -> ToolSchema {
        let mut properties = json!({
            "question": {
                "type": "string",
                "description": "The question, stated as fully as the run can state it. Include \
                                what has already been ruled out — this reads the question rather \
                                than matching it, so context narrows the answer instead of \
                                diluting the query."
            },
            "also_search": {
                "type": "array",
                "items": { "type": "string" },
                "maxItems": 5,
                "description": "Extra phrasings to search alongside the question: the named \
                                theorem, the objects involved, the classification. Use them when \
                                the subject goes by more than one name."
            },
            "category": {
                "type": "string",
                "enum": ["research paper", "pdf", "news", "company", "github"],
                "description": "Narrows to one kind of source. For a mathematical question \
                                `research paper` is usually what you want."
            }
        });
        if let (Some(object), Some(common)) = (
            properties.as_object_mut(),
            common_properties().as_object(),
        ) {
            for (key, value) in common {
                object.insert(key.clone(), value.clone());
            }
        }
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": properties,
                "required": ["question"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        self.schema().validate_call(&call)?;
        let question = call
            .arguments
            .get("question")
            .and_then(Value::as_str)
            .map(str::trim)
            .filter(|value| !value.is_empty())
            .ok_or_else(|| {
                tinyagents::TinyAgentsError::Validation("question must be a non-empty string".into())
            })?;
        let mut body = json!({
            "query": question,
            "type": DEEP_TYPE,
            "contents": {
                "summary": true,
                "highlights": { "numSentences": 3, "highlightsPerUrl": 2 }
            }
        });
        if let Some(object) = body.as_object_mut() {
            let extra: Vec<&str> = call
                .arguments
                .get("also_search")
                .and_then(Value::as_array)
                .into_iter()
                .flatten()
                .filter_map(Value::as_str)
                .map(str::trim)
                .filter(|value| !value.is_empty())
                .take(5)
                .collect();
            if !extra.is_empty() {
                object.insert("additionalQueries".to_string(), json!(extra));
            }
            if let Some(category) = call
                .arguments
                .get("category")
                .and_then(Value::as_str)
                .map(str::trim)
                .filter(|value| !value.is_empty())
            {
                object.insert("category".to_string(), json!(category));
            }
        }
        apply_common(&mut body, &call);

        let reply = self.exa.post(SEARCH_URL, &body).await?;
        let synthesis = synthesis(&reply);
        let results = results_of(&reply);
        let leads = result_leads(&results, &format!("found researching: {}", clip(question, 160)));
        let filed = leads.len();
        self.exa.file_leads(&leads).await;

        if synthesis.is_empty() && results.is_empty() {
            return Ok(ToolResult::text(
                call.id,
                self.name(),
                "The research agent returned neither a synthesis nor any sources. Narrow the \
                 question, or fall back to exa_search on the individual phrasings."
                    .to_string(),
            ));
        }
        Ok(ToolResult::text(
            call.id,
            self.name(),
            format!(
                "{}\n\n---\n\n{filed} source{} added to {}. Nothing above has been read by this \
                 run: it is a synthesis of pages you do not hold, so treat it as the vocabulary \
                 for your next search and download a source before recording anything as \
                 established.\n\n{}",
                if synthesis.is_empty() {
                    "The research agent returned sources but no synthesis.".to_string()
                } else {
                    clip(&synthesis, TOTAL_CHARS)
                },
                if filed == 1 { "" } else { "s" },
                super::frontier::FRONTIER_PATH,
                render_all(&results)
            ),
        ))
    }
}

/// Reads the synthesised answer out of a deep reply.
///
/// The field has moved between `output.content`, a bare `answer`, and a
/// `content` string across the endpoint's revisions, and a reply carrying prose
/// this cannot find is indistinguishable from one carrying none — the run would
/// silently pay for a deep search and get a list. Reading all three is cheaper
/// than pinning a version.
fn synthesis(reply: &Value) -> String {
    for path in [
        vec!["output", "content"],
        vec!["answer"],
        vec!["content"],
        vec!["output", "text"],
    ] {
        let mut node = Some(reply);
        for key in path {
            node = node.and_then(|value| value.get(key));
        }
        let Some(node) = node else {
            continue;
        };
        let text = match node {
            Value::String(text) => text.clone(),
            other => serde_json::to_string_pretty(other).unwrap_or_default(),
        };
        if !text.trim().is_empty() {
            return text.trim().to_string();
        }
    }
    String::new()
}
