    use serde_json::json;

    use super::{
        DEFAULT_LIMIT, Lookup, MAX_LIMIT, VectorStore, limit_argument, limit_property, point_id,
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

    /// Every question a tool can ask has an answer in both engines.
    ///
    /// The point of [`Lookup`] is that a tool can no longer name a retriever,
    /// so the set of questions is closed and each engine has to answer all of
    /// it. This walks the set rather than trusting that it was walked: adding a
    /// variant without teaching both engines what it means is the failure, and
    /// the two `match`es on it are exhaustive so the compiler catches that —
    /// this catches the other half, a variant added and mapped to nothing
    /// meaningful.
    #[test]
    fn every_lookup_is_answered_by_both_engines() {
        for lookup in [
            Lookup::Passages,
            Lookup::Connections,
            Lookup::ConnectionsExtended,
        ] {
            assert!(
                !super::cognee::search_type(lookup).is_empty(),
                "Cognee names no retriever for {lookup:?}"
            );
            assert!(
                !super::cortex::layers(lookup).is_empty(),
                "CortexDB reads no layer for {lookup:?}"
            );
        }
        // The two connection reaches must differ, or `relate_memory`'s
        // `extended` is a slower spelling of `direct` and the option is a lie
        // told in a tool schema.
        assert_ne!(
            super::cognee::search_type(Lookup::Connections),
            super::cognee::search_type(Lookup::ConnectionsExtended)
        );
        assert_ne!(
            super::cortex::layers(Lookup::Connections),
            super::cortex::layers(Lookup::ConnectionsExtended)
        );
    }

    /// An unset `MATH_AGENT_MEMORY` is `CortexDB`, and a name neither engine
    /// answers to is a startup failure rather than a silent default.
    ///
    /// The failure this guards is the quiet one: a typo falling back to an
    /// engine holding none of what the run wrote looks exactly like a memory
    /// that has nothing in it, which is a whole afternoon of `docs/memory.md`.
    #[test]
    fn an_unknown_engine_is_refused_rather_than_defaulted() {
        // `from_env` is driven by process-wide state, so this asserts the
        // decision rather than the construction: the selection is a `match` on
        // a lowercased name with an explicit error arm, and the arm is what a
        // misspelling reaches.
        let refused = VectorStore::from_env_named("cognie");
        assert!(
            refused.is_err(),
            "a misspelled engine name has to fail loudly"
        );
        let message = refused.err().map(|error| error.to_string()).unwrap_or_default();
        assert!(
            message.contains("cognie") && message.contains("cortex"),
            "the refusal has to name what was asked for and what is available: {message}"
        );
    }

    /// Durable recall reads three named stores and never the scratch.
    ///
    /// The list is the control rather than a convenience: `view: "descend"` was
    /// tried first and returned nothing on a live workspace whose brain held
    /// nineteen events, so what durable recall reaches is now a literal. A
    /// scratch scope appearing in it would put unchecked arithmetic into
    /// `recall_memory`, which is the one thing the four-store split exists to
    /// prevent — and it would do so silently.
    #[test]
    fn durable_recall_names_three_stores_and_never_the_scratch() {
        let stores = super::cortex::DURABLE_STORES;
        assert_eq!(stores.len(), 3, "the three durable stores, and only those");
        for store in stores {
            assert!(
                store.starts_with("store:"),
                "{store} is not one of the project's durable stores"
            );
            assert!(
                !store.contains("scratch"),
                "the scratch must not be reachable from durable recall"
            );
        }
        // The brain is read first, because it holds what survived checking and
        // the reader sees it before a session transcript.
        assert_eq!(stores[0], "store:brain");
    }

    /// A small `limit` narrows every store rather than silencing two of them.
    ///
    /// The failure guarded is invisible: a split that floored to zero would
    /// stop reading the library and the sessions below some limit, and a recall
    /// that quietly covers less than it says it does is worse than a thin one.
    #[test]
    fn every_store_keeps_a_share_of_the_recall_budget() {
        for limit in [1, 2, 3, 8, MAX_LIMIT] {
            let budgets = super::cortex::store_budgets(limit);
            assert!(
                budgets.iter().all(|share| *share >= 1),
                "limit {limit} silenced a store: {budgets:?}"
            );
            // The brain takes the largest share at any limit worth splitting.
            assert!(
                budgets[0] >= budgets[1] && budgets[0] >= budgets[2],
                "limit {limit} did not favour the brain: {budgets:?}"
            );
        }
    }
