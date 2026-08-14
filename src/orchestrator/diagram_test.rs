//! Deterministic tests for the rendered solution loop.
#![allow(clippy::expect_used, clippy::panic)]

use super::*;

/// The diagram renders the graph the engine runs, so the only thing left to
/// check is that every node it draws is one the graph actually has. A name here
/// for a node that no longer exists would render nothing and say nothing.
#[test]
fn every_shortened_name_belongs_to_a_real_node() {
    let graph = solution_loop();
    for (id, _) in NODES {
        assert!(
            graph.nodes.iter().any(|node| node.id.as_str() == id),
            "`{id}` is named for the diagram but is not in the loop"
        );
    }
}

/// The renderer truncates on character count, not width, so a longer name does
/// not get cut off — it runs out of its box and over the next one.
#[test]
fn node_names_fit_the_box_the_renderer_draws() {
    for node in solution_loop().nodes {
        assert!(
            node.name.len() <= 13,
            "`{}` is named `{}`, which will overflow its box",
            node.id,
            node.name
        );
        assert!(
            node.name.is_ascii(),
            "`{}` is named `{}`; the 8x8 font has no glyph for it",
            node.id,
            node.name
        );
    }
}

/// Nothing leaves the terminal node. A picture showing an exit from it would be
/// describing a loop that cannot stop.
#[test]
fn nothing_leaves_the_terminal_node() {
    let graph = solution_loop();
    assert!(graph.nodes.iter().any(|node| node.id.as_str() == "report"));
    assert!(
        !graph
            .edges
            .iter()
            .any(|edge| edge.from_node.as_str() == "report")
    );
}

#[test]
fn an_unsupported_extension_is_refused_by_name() {
    let error = render_solution_loop("loop.svg").expect_err("svg is not a raster format");
    assert!(error.to_string().contains("loop.svg"), "{error}");
}

/// Every flow is drawable, and the checks that matter for the loop matter for
/// each of them: a name too long runs out of its box and over the next one, and
/// the 8x8 font has no glyph outside ASCII.
#[test]
fn every_flow_is_named_for_the_renderer() {
    for (stem, graph) in flows() {
        assert!(
            !graph.nodes.is_empty(),
            "the `{stem}` flow has no nodes to draw"
        );
        for node in &graph.nodes {
            assert!(
                node.name.len() <= 13,
                "`{stem}`: `{}` is named `{}`, which will overflow its box",
                node.id,
                node.name
            );
            assert!(
                node.name.is_ascii(),
                "`{stem}`: `{}` is named `{}`; the 8x8 font has no glyph for it",
                node.id,
                node.name
            );
        }
    }
}

/// The flows are distinct files. Two graphs sharing a stem would render as one,
/// with whichever came last silently overwriting the other.
#[test]
fn no_two_flows_share_a_file_name() {
    let mut stems: Vec<&str> = flows().iter().map(|(stem, _)| *stem).collect();
    stems.sort_unstable();
    let count = stems.len();
    stems.dedup();
    assert_eq!(count, stems.len(), "two flows would render to one file");
}

/// Every child graph the loop embeds is drawn. A `sub_workflow` node whose child
/// is not in `flows` is a flow that runs and that nobody can look at.
#[test]
fn every_embedded_child_is_a_flow() {
    let drawn: Vec<String> = flows()
        .iter()
        .map(|(_, graph)| graph.name.clone())
        .collect();
    for node in solution_loop().nodes {
        let Some(child) = node.config.get("workflow") else {
            continue;
        };
        let name = child
            .get("name")
            .and_then(serde_json::Value::as_str)
            .unwrap_or_default()
            .to_string();
        assert!(
            drawn.contains(&name),
            "`{}` embeds the `{name}` graph, which no flow draws",
            node.id
        );
    }
}
