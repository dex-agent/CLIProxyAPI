# INDEX — CLIProxyAPI (mapa de retomada)

Proxy multi-provider em Go 1.26+ (OpenAI/Gemini/Claude/Codex compatíveis, OAuth, round-robin). HEAD: `6eb8554f`.

## Árvore do repo (sem sub-INDEX próprios — repo upstream pré-convenção)
- [docs/](docs/) — API de gerência, schema de configuração e notas de release.
- [sdk/](sdk/) — SDK embutível (handlers HTTP, cliproxy, auth, translator, pluginapi).
- [internal/](internal/) — núcleo do servidor (api, runtime/executor, translator, registry, store, pluginhost, tui…).
- [examples/](examples/) — exemplos de uso e plugins C/Rust/Go.
- [test/](test/) — testes de integração cross-módulo.
- [.agents/INDEX.md](.agents/INDEX.md) — estado vivo da arqueologia (receipts, scripts, gatilhos, handoff).

## Retomada rápida
1. `AGENTS.md` → contratos de build/convenções (upstream-governado, não tocar em PR).
2. `.agents/GATILHOS-VIVOS.md` → gatilhos quentes (toolchain Go no cache, CRG, testes).
3. `.agents/HANDOFF.md` → estado da última sessão.
4. `DEPENDENCIES.md` → grafo interno + 3rd-party.
