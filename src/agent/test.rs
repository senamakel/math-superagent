//! Unit tests for the embedded `OpenHuman` runtime configuration.

use super::domains;

#[test]
fn excludes_memory_channels_and_web3() {
    let domains = domains();

    assert!(domains.agent);
    assert!(domains.inference);
    assert!(!domains.memory);
    assert!(!domains.channels);
    assert!(!domains.web3);
}
