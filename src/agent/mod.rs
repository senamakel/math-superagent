//! Embedded `OpenHuman` runtime configuration.
//!
//! This facade embeds the complete `OpenHuman` Rust core while selecting only
//! the domain families needed to run agents. Persistent memory, external
//! channels, and Web3 are disabled in the returned [`DomainSet`].

pub use openhuman_core::{
    CoreBuilder, CoreRuntime, DomainSet, HostKind, ServiceSet, TokenSource,
};

/// Returns the `OpenHuman` domains used by this embedded agent runtime.
///
/// Agent execution, inference, configuration, security, threads, and native
/// runtimes are available. Memory, channels, Web3, and unrelated product
/// surfaces remain disabled.
#[must_use]
pub fn domains() -> DomainSet {
    DomainSet {
        agent: true,
        memory: false,
        threads: true,
        config: true,
        security: true,
        flows: false,
        skills: false,
        mcp: false,
        meet: false,
        channels: false,
        web3: false,
        voice: false,
        media: false,
        medulla: false,
        inference: true,
        integrations: false,
        automation: false,
        runtimes: true,
        desktop: false,
        hosted: false,
        relay: false,
        platform: false,
    }
}

/// Creates an embedded `OpenHuman` core builder with no network transport or
/// background services.
#[must_use]
pub fn builder(host_kind: HostKind) -> CoreBuilder {
    CoreBuilder::new(host_kind)
        .services(ServiceSet::none())
        .domains(domains())
}

#[cfg(test)]
mod test;
