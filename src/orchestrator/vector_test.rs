    use serde_json::json;

    use super::{
        CHUNK_SEARCH, DEFAULT_LIMIT, EXTENDED_GRAPH_SEARCH, GRAPH_SEARCH, MAX_LIMIT,
        SCOPE_SAFE_SEARCH_TYPES, TRIPLET_SEARCH, durable_node_sets, library_node_set,
        limit_argument, limit_property, point_id, render_result, scratch_node_set,
        session_node_set, slug, source_file_name, source_mime, visible_datasets,
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
        let rendered = render_result(&json!({"text": "context", "score": 0.9}));
        assert!(rendered.contains("context"));
        assert!(rendered.contains("0.9"));
    }

    /// This project's library, named the way `VectorStore::from_env` names it.
    const LIBRARY: &str = "math_agent_library__project_euler_903";

    #[test]
    fn session_recall_is_limited_to_the_current_project_run() {
        let datasets = json!([
            {"name": "math_agent_brain"},
            {"name": LIBRARY},
            {"name": "math_agent_sessions__project_euler_903__current"},
            {"name": "math_agent_sessions__project_euler_904__other"}
        ]);
        assert_eq!(
            visible_datasets(
                &datasets,
                "math_agent_sessions__project_euler_903__current",
                LIBRARY
            ),
            vec![
                "math_agent_brain",
                LIBRARY,
                "math_agent_sessions__project_euler_903__current"
            ]
        );
        assert_eq!(slug("project-euler/903"), "project_euler_903");
        assert_eq!(slug("---"), "default");
    }

    #[test]
    fn an_unrecognised_dataset_is_not_this_run_s_to_read() {
        // A live server carried `project_euler_903_L0` — thirty-six sources an
        // earlier build ingested — and the old denylist passed it, so every
        // run on the box searched another problem's literature. Anything this
        // runtime does not name belongs to another project or an older build.
        let datasets = json!([
            {"name": "math_agent_brain"},
            {"name": "project_euler_903_L0"},
            {"name": "math_agent_library__project_euler_763"},
            {"name": "something_a_person_uploaded"},
            {"name": "math_agent_library__project_euler_185"},
            {"name": "math_agent_sessions__project_euler_185"}
        ]);
        assert_eq!(
            visible_datasets(
                &datasets,
                "math_agent_sessions__project_euler_185",
                "math_agent_library__project_euler_185"
            ),
            vec![
                "math_agent_brain",
                "math_agent_library__project_euler_185",
                "math_agent_sessions__project_euler_185"
            ]
        );
    }

    #[test]
    fn a_rerun_of_the_same_problem_reuses_its_dataset_and_reaches_earlier_runs() {
        // The dataset used to carry the run id — nanoseconds and a pid — so
        // every restart opened a new one and could see only itself. One problem
        // restarted eight times left eight datasets, seven unreachable. The
        // name is now the project, and the per-run datasets an older build
        // stranded underneath it are readable again.
        let ours = "math_agent_sessions__project_euler_185";
        let datasets = json!([
            {"name": "math_agent_brain"},
            {"name": "math_agent_sessions__project_euler_185"},
            {"name": "math_agent_sessions__project_euler_185__s18cb030630d9e2be-1"},
            {"name": "math_agent_sessions__project_euler_185__s18cb0306ffffffff-9"},
            {"name": "math_agent_sessions__project_euler_763"}
        ]);
        let visible = visible_datasets(&datasets, ours, "math_agent_library__project_euler_185");
        assert!(visible.contains(&ours.to_string()));
        assert!(visible.contains(&"math_agent_brain".to_string()));
        assert!(
            visible.contains(&format!("{ours}__s18cb030630d9e2be-1")),
            "a run must reach the session memory of earlier runs on the same problem"
        );
        assert!(
            !visible.contains(&"math_agent_sessions__project_euler_763".to_string()),
            "another problem's session memory must stay out"
        );
    }

    #[test]
    fn provisional_work_never_reaches_durable_recall() {
        // The scratch replaces SCRATCHPAD.md, and the file was withheld from
        // reflection on purpose: unsettled arithmetic is not evidence of
        // progress, and a loop that reads it as such keeps retrying. Durable
        // recall must therefore not reach the scratch even for this project —
        // `recall_scratch` is the only way in.
        let ours = "math_agent_sessions__project_euler_185";
        let datasets = json!([
            {"name": "math_agent_brain"},
            {"name": "math_agent_sessions__project_euler_185"},
            {"name": "math_agent_scratch__project_euler_185"},
            {"name": "math_agent_scratch__project_euler_763"}
        ]);
        let visible = visible_datasets(&datasets, ours, "math_agent_library__project_euler_185");
        assert_eq!(
            visible,
            vec!["math_agent_brain", "math_agent_sessions__project_euler_185"]
        );
    }

    #[test]
    fn a_shorter_project_name_does_not_swallow_a_longer_one() {
        // `euler_18` is a prefix of `euler_185`, so the ownership test has to
        // require the `__` separator or one problem reads another's memory.
        let datasets = json!([
            {"name": "math_agent_sessions__euler_18"},
            {"name": "math_agent_sessions__euler_185"},
            {"name": "math_agent_sessions__euler_18__s1-2"}
        ]);
        let visible = visible_datasets(
            &datasets,
            "math_agent_sessions__euler_18",
            "math_agent_library__euler_18",
        );
        assert!(visible.contains(&"math_agent_sessions__euler_18".to_string()));
        assert!(visible.contains(&"math_agent_sessions__euler_18__s1-2".to_string()));
        assert!(
            !visible.contains(&"math_agent_sessions__euler_185".to_string()),
            "euler_18 must not read euler_185's memory"
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
        // The separation the three stores rest on. It used to hold because
        // `visible_datasets` omitted the scratch dataset; the server does not
        // apply the dataset filter, so it holds here or nowhere.
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
    /// `node_name` is the only filter this deployment applies — dataset
    /// filtering needs `ENABLE_BACKEND_ACCESS_CONTROL`, which the memory
    /// compose file turns off — so a retriever that ignores it searches every
    /// problem on the box. That is the leak `visible_datasets` closed, and
    /// naming a different search type is the way back into it.
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
        for used in [
            CHUNK_SEARCH,
            TRIPLET_SEARCH,
            GRAPH_SEARCH,
            EXTENDED_GRAPH_SEARCH,
        ] {
            assert!(SCOPE_SAFE_SEARCH_TYPES.contains(&used), "{used} is unreachable");
        }
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
        // The same failure `visible_datasets` guards against, one layer down:
        // node-set matching is exact, so a prefix cannot widen the scope.
        assert_ne!(session_node_set("euler_18"), session_node_set("euler_185"));
        assert!(!durable_node_sets("euler_18").contains(&session_node_set("euler_185")));
    }
