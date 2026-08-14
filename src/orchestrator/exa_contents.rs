/// Reads up to twenty candidate pages in one request, and stores none of them.
///
/// This is triage, and it exists because the run's only way to find out what a
/// page said was `download_document`, which converts it, digests it, archives
/// the original bytes, files it in durable memory, indexes it, and adds a row
/// to the folder index. That is the right amount of work for a source the run
/// is going to *use*, and it is paid twenty times over to discover that
/// seventeen were not the right paper. The library then carries seventeen
/// documents nobody will read, which is the state the scholar's brief describes
/// as a library that has cost the run context and taught it nothing.
///
/// So the two are different questions and stay different tools. This one asks
/// *which of these is worth having*; `download_document` asks for the one that
/// is. Nothing here reaches the workspace, and the tool says so, because a
/// model that believes a page is filed will cite it later from a summary it no
/// longer holds.
///
/// One thing does survive: what the pages linked to. A triage read that kept
/// only the verdict would throw away every reference each page carried, which
/// is most of what a page was worth in the case the verdict was no.
#[derive(Debug)]
pub(in crate::orchestrator) struct SourceContentsTool {
    exa: Exa,
}

#[async_trait]
impl Tool<()> for SourceContentsTool {
    fn name(&self) -> &'static str {
        "read_sources"
    }

    fn description(&self) -> &'static str {
        "Reads up to twenty web pages in one request and returns a summary of each, without \
         storing anything. This is triage: use it to decide which candidates are worth a real \
         download, instead of downloading twenty papers to find the three that matter. Pass \
         `question` to have each page summarised against what you actually want to know. Nothing \
         is filed in the workspace — download_document is still how a source enters the library — \
         but every link these pages carry is added to the frontier."
    }

    fn schema(&self) -> ToolSchema {
        ToolSchema::new(
            self.name(),
            self.description(),
            json!({
                "type": "object",
                "properties": {
                    "urls": {
                        "type": "array",
                        "items": { "type": "string" },
                        "minItems": 1,
                        "maxItems": MAX_CONTENTS_URLS,
                        "description": "The candidate pages, from search results, the frontier, \
                                        or a source you already hold. Never an address you have \
                                        not seen — an invented URL fails here rather than \
                                        silently returning the wrong paper, but it still costs \
                                        the call."
                    },
                    "question": {
                        "type": "string",
                        "description": "What you want to know. Each page is summarised against \
                                        this rather than in general, which is the difference \
                                        between `a paper about cycle lengths` and `it proves the \
                                        bound only for triangle-free graphs`."
                    },
                    "include_text": {
                        "type": "boolean",
                        "description": "Return an excerpt of each page's text as well as its \
                                        summary. Off by default: twenty excerpts is a large \
                                        reply, and the summary is what a triage decision needs."
                    },
                    "subpages": {
                        "type": "integer",
                        "minimum": 0,
                        "maximum": 5,
                        "description": "Also read this many linked subpages of each URL. Use it \
                                        on a survey's or a course's index page, where the \
                                        landing page is a table of contents and the mathematics \
                                        is one level down."
                    },
                    "subpage_target": {
                        "type": "string",
                        "description": "Which subpages to prefer, e.g. `references` or \
                                        `theorem`. Only meaningful with `subpages`."
                    }
                },
                "required": ["urls"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        self.schema().validate_call(&call)?;
        let urls: Vec<&str> = call
            .arguments
            .get("urls")
            .and_then(Value::as_array)
            .into_iter()
            .flatten()
            .filter_map(Value::as_str)
            .map(str::trim)
            .filter(|url| !url.is_empty())
            .take(MAX_CONTENTS_URLS)
            .collect();
        if urls.is_empty() {
            return Err(tinyagents::TinyAgentsError::Validation(
                "urls must name at least one page to read".into(),
            ));
        }
        let question = call
            .arguments
            .get("question")
            .and_then(Value::as_str)
            .map(str::trim)
            .filter(|value| !value.is_empty());

        let mut summary = json!({});
        if let (Some(object), Some(question)) = (summary.as_object_mut(), question) {
            object.insert("query".to_string(), json!(question));
        }
        let mut body = json!({
            "urls": urls,
            "summary": summary,
            // The links are the point of doing this rather than reading a
            // search snippet: they outlive the triage decision.
            "extras": { "links": MAX_LINKS_PER_PAGE }
        });
        if let Some(object) = body.as_object_mut() {
            if call
                .arguments
                .get("include_text")
                .and_then(Value::as_bool)
                .unwrap_or(false)
            {
                object.insert(
                    "text".to_string(),
                    json!({ "maxCharacters": MAX_TEXT_CHARS }),
                );
            }
            if let Some(question) = question {
                object.insert(
                    "highlights".to_string(),
                    json!({ "query": question, "maxCharacters": MAX_TEXT_CHARS }),
                );
            }
            let subpages = call
                .arguments
                .get("subpages")
                .and_then(Value::as_u64)
                .unwrap_or(0)
                .min(5);
            if subpages > 0 {
                object.insert("subpages".to_string(), json!(subpages));
                if let Some(target) = call
                    .arguments
                    .get("subpage_target")
                    .and_then(Value::as_str)
                    .map(str::trim)
                    .filter(|value| !value.is_empty())
                {
                    object.insert("subpageTarget".to_string(), json!(target));
                }
            }
        }

        let reply = self.exa.post(CONTENTS_URL, &body).await?;
        let results = results_of(&reply);
        if results.is_empty() {
            return Ok(ToolResult::text(
                call.id,
                self.name(),
                "Exa returned none of those pages. Check the addresses came from a search \
                 result, the frontier, or a source you hold, rather than being constructed."
                    .to_string(),
            ));
        }
        let rendered = render_all(&results);
        let failures = failed(&reply);
        let leads = extracted_leads(&results);
        let filed = leads.len();
        // Every page contributes its own links, so the frontier is told which
        // page they came from — the first URL stands for the batch only in the
        // ledger's "this source was consulted" sense.
        self.exa.file_leads(urls[0], &leads).await;

        Ok(ToolResult::text(
            call.id,
            self.name(),
            format!(
                "Read {} of {} page{}{failures}. {filed} link{} they carry added to {}. Nothing \
                 was stored in the workspace — use download_document on the ones worth \
                 keeping.\n\n{rendered}",
                results.len(),
                urls.len(),
                if urls.len() == 1 { "" } else { "s" },
                if filed == 1 { "" } else { "s" },
                super::frontier::FRONTIER_PATH
            ),
        ))
    }
}

/// Names the pages the request could not reach.
///
/// Reported rather than dropped, because a triage over twenty URLs that
/// silently returns eleven reads as eleven candidates rather than as nine
/// unanswered questions, and the nine are where a paywalled or moved primary
/// source hides.
fn failed(reply: &Value) -> String {
    let broken: Vec<String> = reply
        .get("statuses")
        .and_then(Value::as_array)
        .into_iter()
        .flatten()
        .filter(|status| {
            status
                .get("status")
                .and_then(Value::as_str)
                .is_some_and(|value| value != "success")
        })
        .filter_map(|status| status.get("id").and_then(Value::as_str))
        .map(ToOwned::to_owned)
        .collect();
    if broken.is_empty() {
        return String::new();
    }
    format!(
        " ({} could not be reached: {})",
        broken.len(),
        clip(&broken.join(", "), RESULT_CHARS)
    )
}
