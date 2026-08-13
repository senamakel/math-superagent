//! Deterministic tests for the deliberately absent execution path.
#![allow(clippy::expect_used)]

use super::*;

/// The control this refusal protects is the complexity declaration on
/// `execute_command`. A runner that quietly returned nothing would let a
/// workflow believe it had computed something.
#[tokio::test]
async fn a_code_node_is_refused_and_pointed_at_the_supported_path() {
    for language in [CodeLanguage::Python, CodeLanguage::JavaScript] {
        let error = RefusingCodeRunner
            .run(language, "print(1)", Value::Null)
            .await
            .expect_err("this host does not run code from a `code` node");
        let rendered = error.to_string();
        assert!(rendered.contains("execute_command"), "{rendered}");
        assert!(rendered.contains("complexity"), "{rendered}");
    }
}
