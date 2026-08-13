//! Deterministic tests for the rendered solution loop.
#![allow(clippy::expect_used)]

use super::*;

/// The renderer lays out from edges, so an edge naming a node that is not in
/// [`NODES`] draws as a dangling reference rather than failing. That is the
/// mistake this catches: a route added to the loop whose destination nobody
/// added to the picture.
#[test]
fn every_edge_endpoint_is_a_declared_node() {
    let graph = solution_loop();
    let declared: Vec<&str> = NODES.iter().map(|(id, _)| *id).collect();
    for edge in &graph.edges {
        assert!(
            declared.contains(&edge.from_node.as_str()),
            "edge source `{}` is not a declared node",
            edge.from_node
        );
        assert!(
            declared.contains(&edge.to_node.as_str()),
            "edge target `{}` is not a declared node",
            edge.to_node
        );
    }
}

#[test]
fn the_picture_carries_every_route_the_loop_wires() {
    let graph = solution_loop();
    // One edge per table row, and nothing invented: the whole point of sharing
    // the tables is that these two counts cannot drift apart.
    assert_eq!(
        graph.edges.len(),
        DIRECT_EDGES.len() + JUDGE_ROUTES.len() + REFLECT_ROUTES.len()
    );

    for (verdict, target) in REFLECT_ROUTES {
        assert!(
            graph.edges.iter().any(|edge| edge.from_node.as_str() == "reflect"
                && edge.to_node.as_str() == target
                && edge.from_port == verdict.to_string()),
            "no rendered edge for reflect/{verdict} -> {target}"
        );
    }
    for (verdict, target) in JUDGE_ROUTES {
        assert!(
            graph.edges.iter().any(|edge| edge.from_node.as_str() == "judge"
                && edge.to_node.as_str() == target
                && edge.from_port == verdict.to_string()),
            "no rendered edge for judge/{verdict} -> {target}"
        );
    }
}

#[test]
fn the_entry_and_finish_nodes_are_drawn() {
    let graph = solution_loop();
    assert!(graph.nodes.iter().any(|node| node.id.as_str() == ENTRY));
    assert!(graph.nodes.iter().any(|node| node.id.as_str() == FINISH));
    // Nothing leaves the terminal node; a picture showing an exit from it
    // would be describing a loop that cannot stop.
    assert!(
        !graph
            .edges
            .iter()
            .any(|edge| edge.from_node.as_str() == FINISH)
    );
}

#[test]
fn node_names_fit_the_box_the_renderer_draws() {
    // The renderer truncates on character count, not width, so a longer name
    // does not get cut off — it runs out of the node and over the next one.
    for (id, name) in NODES {
        assert!(
            name.len() <= 13,
            "`{id}` is named `{name}`, which will overflow its box"
        );
        assert!(
            name.is_ascii(),
            "`{id}` is named `{name}`; the 8x8 font has no glyph for it"
        );
    }
}

#[test]
fn an_unsupported_extension_is_refused_by_name() {
    let error = render_solution_loop("loop.svg").expect_err("svg is not a raster format");
    let rendered = error.to_string();
    assert!(rendered.contains("loop.svg"), "{rendered}");
}
