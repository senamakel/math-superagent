    use serde_json::json;

    use super::{
        CHUNK_SEARCH, DEFAULT_LIMIT, EXTENDED_GRAPH_SEARCH, GRAPH_SEARCH, IngestHealth, MAX_LIMIT,
        PROJECT_DATASET_PREFIX, SCOPE_SAFE_SEARCH_TYPES, UNSUPPORTED_TRIPLET_SEARCH,
        authenticated_client, durable_node_sets, indexing_health, library_node_set, limit_argument,
        limit_property, point_id, render_result, scratch_node_set, session_node_set, slug,
        source_file_name, source_mime,
    };

    #[test]
    fn an_uploaded_source_is_named_for_the_bytes_rather_than_the_workspace_path() {
        // The workspace path is always `.md` — it names the *conversion*. A PDF
        // uploaded under that name invites Cognee to chunk a binary as text.
        assert_eq!(
            source_file_name("research/summaries/pell.md", Some("application/pdf")),
            "source-research_summaries_pell.pdf"
        );
        assert_eq!(
            source_file_name(
                "research/summaries/pell.md",
                Some("text/html; charset=utf-8")
            ),
            "source-research_summaries_pell.html"
        );
        // An unknown or absent type is text rather than a guess.
        assert_eq!(
            source_file_name("research/summaries/pell.md", None),
            "source-research_summaries_pell.txt"
        );
    }

    #[test]
    fn a_mislabelled_pdf_is_still_uploaded_as_a_pdf() {
        // Servers mislabel routinely; the download path already prefers magic
        // bytes for that reason, and the upload has to make the same choice or
        // the extraction is spent on the wrong parser.
        assert_eq!(
            source_mime(b"%PDF-1.7\n1 0 obj", Some("text/html")),
            "application/pdf"
        );
        assert_eq!(source_mime(b"<html>", Some("text/html")), "text/html");
        // Parameters are dropped, so the type is one Cognee can match on.
        assert_eq!(
            source_mime(b"# note", Some("text/markdown; charset=utf-8")),
            "text/markdown"
        );
        // Nothing declared and nothing recognisable stays deliberately opaque.
        assert_eq!(source_mime(b"\x00\x01", None), "application/octet-stream");
    }

    #[test]
    fn point_ids_are_deterministic() {
        assert_eq!(point_id("same note"), point_id("same note"));
        assert_ne!(point_id("same note"), point_id("different note"));
    }

    #[test]
    fn cognee_results_render_strings_and_structured_context() {
        assert_eq!(render_result(&json!("plain context")), "plain context");
        // A result object is rendered as its passage, not as the object: the
        // server sends the text twice — `text` and `raw.value` — beside null
        // scores, empty metadata and a dataset UUID, and a live recall spent
        // more of its clip on that scaffolding than on the answer.
        let rendered = render_result(&json!({
            "kind": "chunk",
            "text": "the smallest open degree is 20",
            "score": null,
            "metadata": {},
            "dataset_name": "math_agent_brain",
            "raw": {"value": "the smallest open degree is 20"}
        }));
        assert_eq!(
            rendered,
            "the smallest open degree is 20\n\n(from math_agent_brain)"
        );
        // A shape with nothing readable still arrives whole, because guessing
        // would lose the answer where verbosity only costs tokens.
        let opaque = render_result(&json!({"score": 0.9}));
        assert!(opaque.contains("0.9"), "{opaque}");
    }

    /// This project's dataset, named the way `VectorStore::from_env` names it.
    fn project_dataset(project: &str) -> String {
        format!("{PROJECT_DATASET_PREFIX}{project}")
    }

    #[test]
    fn a_project_owns_exactly_one_dataset() {
        // Four datasets became one when the memory server became shared, and
        // the reason is the server's storage model: under access control a
        // dataset *is* a graph database, so a library and the sessions that
        // read it would land in graphs with no edge possible between them.
        // The four stores are separated by node set inside this one name.
        assert_eq!(
            project_dataset(&slug("project-euler/903")),
            "math_agent__project_euler_903"
        );
        assert_eq!(slug("project-euler/903"), "project_euler_903");
        assert_eq!(slug("---"), "default");
    }

    #[test]
    fn a_shorter_project_name_does_not_swallow_a_longer_one() {
        // `euler_18` is a prefix of `euler_185`. Nothing tests a prefix any
        // more — a tenant is shown its own datasets and no others, so the
        // question is only whether two problems can be handed the same name.
        assert_ne!(project_dataset("euler_18"), project_dataset("euler_185"));
        assert_ne!(session_node_set("euler_18"), session_node_set("euler_185"));
    }

    #[test]
    fn every_request_carries_the_tenant_key() {
        // The boundary between one problem's memory and another's is this
        // header: the server holds every problem's datasets and decides which
        // tenant is asking. A client built without it would be answered `401`
        // by a server that has the run's whole memory, which reads as a store
        // that is simply empty.
        assert!(authenticated_client("a-tenant-key").is_ok());
        assert!(
            authenticated_client("   ").is_err(),
            "an empty key is a misconfiguration, not an anonymous run"
        );
        assert!(
            authenticated_client("bad\nvalue").is_err(),
            "a key that cannot be sent as a header must fail at construction"
        );
    }

    #[test]
    fn durable_recall_reads_the_brain_and_this_project_only() {
        let ours = durable_node_sets("project_euler_185");
        assert!(ours.contains(&"math_agent_brain".to_string()));
        assert!(ours.contains(&session_node_set("project_euler_185")));
        assert!(ours.contains(&library_node_set("project_euler_185")));
        assert!(
            !ours.contains(&session_node_set("project_euler_763")),
            "one problem must not read another's sessions"
        );
    }

    #[test]
    fn durable_recall_never_reaches_the_scratch() {
        // The scratch replaces SCRATCHPAD.md, and the file was withheld from
        // reflection on purpose: unsettled arithmetic is not evidence of
        // progress, and a loop that reads it as such keeps retrying. It shares
        // a dataset with everything else this project stores now, so the whole
        // of the separation is the node set — `recall_scratch` names it, and
        // `durable_node_sets` must not.
        let project = "project_euler_185";
        assert!(
            !durable_node_sets(project).contains(&scratch_node_set(project)),
            "provisional arithmetic must not come back as durable knowledge"
        );
    }

    #[test]
    fn a_writer_and_a_reader_spell_each_scope_the_same_way() {
        // A leak nothing would report: documents filed under a node set recall
        // never names are simply unreachable, and the store reads as empty.
        let project = "conjectures_erdos_gyarfas";
        assert_eq!(session_node_set(project), format!("project:{project}"));
        assert_eq!(scratch_node_set(project), format!("scratch:{project}"));
        assert_eq!(library_node_set(project), format!("library:{project}"));
    }

    /// Every search type the runtime can ask for is one the server will
    /// actually scope.
    ///
    /// `node_name` is what separates this project's four stores from each
    /// other, and they share one dataset, so a retriever that ignores it
    /// returns the scratch as durable recall. The cross-problem boundary is
    /// the server's — one tenant per problem — but this one is only ever the
    /// filter, and naming a different search type is the way around it.
    #[test]
    fn no_search_type_the_server_cannot_scope_is_reachable() {
        for unscoped in [
            // Takes `top_k` and a session id, and no node filter at all.
            "SUMMARIES",
            // BM25, and takes `top_k` alone. The exact-identifier search this
            // costs us is covered on disk by `search_documents` instead.
            "CHUNKS_LEXICAL",
            // Run against the whole graph by construction.
            "CYPHER",
            "NATURAL_LANGUAGE",
            "CODE",
            "CODING_RULES",
        ] {
            assert!(
                !SCOPE_SAFE_SEARCH_TYPES.contains(&unscoped),
                "{unscoped} does not honour node_name and must stay unreachable"
            );
        }
        // And everything the tools do reach is on the list, so the guard in
        // `search_in` cannot refuse a call a tool is able to make.
        for used in [CHUNK_SEARCH, GRAPH_SEARCH, EXTENDED_GRAPH_SEARCH] {
            assert!(SCOPE_SAFE_SEARCH_TYPES.contains(&used), "{used} is unreachable");
        }
    }

    /// The retriever this server cannot run is one no call can name.
    ///
    /// It was the graph half of every fused recall and answered none of them:
    /// the server needs a `create_triplet_embeddings` memify pass this runtime
    /// never runs, so it replies `404 … [NoDataError]`. 122 of 136 recalls in
    /// one live run came back passages-only for that reason. The guard in
    /// `search_in` is what stops it being asked for again.
    #[test]
    fn the_triplet_retriever_this_server_cannot_run_is_unreachable() {
        assert!(
            !SCOPE_SAFE_SEARCH_TYPES.contains(&UNSUPPORTED_TRIPLET_SEARCH),
            "a retriever the server refuses must not be reachable from a tool"
        );
        // And the graph half of a fused recall is one the server answers, which
        // is the whole of the correction: a fused recall that silently loses
        // half of itself is a search box wearing a graph store's description.
        assert!(SCOPE_SAFE_SEARCH_TYPES.contains(&GRAPH_SEARCH));
    }

    /// A server that says it cannot index is refused a write, in its own words.
    ///
    /// The report below is verbatim from a live `conjectures/casas-alvero`
    /// memory server whose model endpoint was answering `403 Key limit
    /// exceeded`. A sentinel posted to it returned `200 {"status":"running"}`
    /// and never appeared in the dataset or in the server's file storage.
    #[test]
    fn a_server_that_cannot_index_is_not_told_it_stored_anything() {
        let degraded = json!({
            "status": "degraded",
            "components": {
                "relational_db": {"status": "healthy", "details": "Connection successful"},
                "llm_provider": {
                    "status": "degraded",
                    "details": "API check failed: LLM connection test timed out after 30s."
                },
                "embedding_service": {"status": "healthy", "details": "Embedding generation working"}
            }
        });
        let detail = match indexing_health(&degraded) {
            IngestHealth::Refusing(detail) => detail,
            IngestHealth::Ready => String::new(),
        };
        assert!(
            detail.contains("llm_provider"),
            "a degraded ingest path must refuse the write that would be dropped, and say what is \
             degraded; got `{detail}`"
        );
        assert!(detail.contains("connection test timed out"), "{detail}");

        // Healthy is healthy, including when the server reports components this
        // runtime has never seen: refusing on an unfamiliar shape would stop a
        // memory that works.
        let healthy = json!({
            "status": "healthy",
            "components": {
                "graph_db": {"status": "healthy", "details": "Schema validated"},
                "something_new": {"status": "healthy"}
            }
        });
        assert_eq!(indexing_health(&healthy), IngestHealth::Ready);
        // And a report with nothing this runtime recognises is not a refusal.
        assert_eq!(indexing_health(&json!({"status": "ok"})), IngestHealth::Ready);
    }

    /// The advertised bounds and the enforced ones are the same numbers,
    /// because a schema promising more than the clamp allows is a limit the
    /// model is invited to exceed and never told it did.
    #[test]
    fn the_recall_limit_is_advertised_exactly_as_it_is_enforced() {
        let property = limit_property();
        assert_eq!(property["maximum"], json!(MAX_LIMIT));
        assert_eq!(property["minimum"], json!(1));
        assert_eq!(property["default"], json!(DEFAULT_LIMIT));

        let read = |arguments| {
            limit_argument(&crate::agent::ToolCall {
                id: "call-1".into(),
                name: "recall_memory".into(),
                invalid: None,
                arguments,
            })
        };
        assert_eq!(read(json!({})), DEFAULT_LIMIT);
        assert_eq!(read(json!({ "limit": 25 })), 25);
        // Out of range in either direction is clamped rather than refused: a
        // recall is not worth failing over an argument nobody has to get right.
        assert_eq!(read(json!({ "limit": 500 })), MAX_LIMIT);
        assert_eq!(read(json!({ "limit": 0 })), 1);
    }

    #[test]
    fn a_shorter_project_name_does_not_swallow_a_longer_one_in_node_sets() {
        // The same failure the node-set scoping guards against, one layer down:
        // node-set matching is exact, so a prefix cannot widen the scope.
        assert_ne!(session_node_set("euler_18"), session_node_set("euler_185"));
        assert!(!durable_node_sets("euler_18").contains(&session_node_set("euler_185")));
    }
