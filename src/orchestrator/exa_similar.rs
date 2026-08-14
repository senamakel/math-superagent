/// Finds the pages most like one the run already holds.
///
/// The one discovery path here whose query is not a phrasing problem, which is
/// the same property that makes `oeis_lookup` worth having: a page either
/// resembles another or it does not, and no guess at what the subject is called
/// enters into it. That matters most at the moment a run is weakest — it has
/// one good paper and does not yet know the vocabulary of the field it belongs
/// to, which is precisely when every query it can write is bad.
///
/// It is also the cheapest way past a library that has gone circular. When
/// three searches return the same six famous pages, the sixth page's
/// neighbourhood is a different set from the sixth page's name.
#[derive(Debug)]
pub(in crate::orchestrator) struct FindSimilarTool {
    exa: Exa,
}

#[async_trait]
impl Tool<()> for FindSimilarTool {
    fn name(&self) -> &'static str {
        "find_similar_sources"
    }

    fn description(&self) -> &'static str {
        "Finds the pages most like one you already have, using the page itself as the query \
         rather than a phrase. Use it when a source is exactly on target and you want its \
         neighbourhood, or when repeated searches keep returning the same few pages — this needs \
         no guess at what the subject is called, so it works when your vocabulary for it is still \
         wrong. Everything found is added to the frontier as a lead."
    }

    fn schema(&self) -> ToolSchema {
        let mut properties = json!({
            "url": {
                "type": "string",
                "description": "The page to find neighbours of. Use one you have read and judged \
                                relevant — the whole result set is shaped by this choice, so a \
                                loosely related seed returns a loosely related neighbourhood."
            },
            "limit": {
                "type": "integer",
                "minimum": 1,
                "maximum": MAX_SIMILAR,
                "description": "Neighbours to return. Defaults to 10."
            },
            "same_site": {
                "type": "boolean",
                "description": "Allow neighbours from the seed's own domain. False by default, \
                                which is usually right: the other papers on one arXiv listing are \
                                the least surprising thing this can return."
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
                "required": ["url"],
                "additionalProperties": false
            }),
        )
    }

    async fn call(&self, _state: &(), call: ToolCall) -> Result<ToolResult> {
        self.schema().validate_call(&call)?;
        let url = call
            .arguments
            .get("url")
            .and_then(Value::as_str)
            .map(str::trim)
            .filter(|value| !value.is_empty())
            .ok_or_else(|| {
                tinyagents::TinyAgentsError::Validation(
                    "url must name a page to find neighbours of".into(),
                )
            })?;
        let limit = call
            .arguments
            .get("limit")
            .and_then(Value::as_u64)
            .unwrap_or(DEFAULT_SIMILAR)
            .clamp(1, MAX_SIMILAR);
        let mut body = json!({
            "url": url,
            "numResults": limit,
            "excludeSourceDomain": !call
                .arguments
                .get("same_site")
                .and_then(Value::as_bool)
                .unwrap_or(false),
            "contents": {
                "summary": true,
                "highlights": { "numSentences": 3, "highlightsPerUrl": 2 }
            }
        });
        if let Some(category) = call
            .arguments
            .get("category")
            .and_then(Value::as_str)
            .map(str::trim)
            .filter(|value| !value.is_empty())
            && let Some(object) = body.as_object_mut()
        {
            object.insert("category".to_string(), json!(category));
        }
        apply_common(&mut body, &call);

        let results = results_of(&self.exa.post(FIND_SIMILAR_URL, &body).await?);
        if results.is_empty() {
            return Ok(ToolResult::text(
                call.id,
                self.name(),
                format!(
                    "Exa found nothing like {url}. With filters that usually means they were too \
                     narrow; without them it means the page is unusual enough to have no \
                     neighbourhood, which is worth recording — the run is not going to find this \
                     subject by resemblance."
                ),
            ));
        }
        let rendered = render_all(&results);
        let leads = result_leads(&results, &format!("resembles {url}"));
        let filed = leads.len();
        self.exa.file_leads(&leads).await;

        Ok(ToolResult::text(
            call.id,
            self.name(),
            format!(
                "{} page{} resemble {url}; {filed} added to {} as leads. None has been read — \
                 download the ones that bear on the problem.\n\n{rendered}",
                results.len(),
                if results.len() == 1 { "" } else { "s" },
                super::frontier::FRONTIER_PATH
            ),
        ))
    }
}
