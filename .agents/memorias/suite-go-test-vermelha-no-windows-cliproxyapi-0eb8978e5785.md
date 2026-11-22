---
implementation_version: v2
layer: L2
slug: suite-go-test-vermelha-no-windows-cliproxyapi-0eb8978e5785
tags:
  - "#build/go-tests"
  - "#plataforma/windows"
---

# Suite go test ./... vermelha no Windows (CLIProxyAPI)

Em 2026-11-22 (HEAD 6eb8554f): 9 falhas em 6 pacotes. 8 sao ambiente-Windows: file-lock de cleanup TempDir (bolt/shadow: internal/home x2, internal/kvstore x1, internal/pluginhost x1), TUI/TTY com timeout 30s (cmd/server main_exit_test.go:122 x2), links POSIX git_workspace_test.go:166 e :444 (internal/store). 1 e drift REAL de golden: TestToolSearchDisabledMatchesDevGolden. Nao re-abrir sem ler .agents/receipts/W6-build-test.json. Build VERDE (exit 0).

#build/go-tests #plataforma/windows

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^suite-go-test-vermelha-no-windows-cliproxyapi-0eb8978e5785-content
