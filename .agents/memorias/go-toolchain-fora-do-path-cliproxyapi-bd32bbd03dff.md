---
implementation_version: v2
layer: L2
slug: go-toolchain-fora-do-path-cliproxyapi-bd32bbd03dff
tags:
  - "#toolchain/go"
  - "#build/windows"
---

# Go toolchain fora do PATH (CLIProxyAPI)

O binario go NAO esta no PATH desta maquina (nem no Git Bash nem no PowerShell). Toolchain 1.26.10 (exata do go.mod) vive no module cache: %USERPROFILE%/go/pkg/mod/golang.org/toolchain@v0.0.1-go1.26.10.windows-amd64/bin/go.exe. Rota: source .agents/scripts/go-env.sh (repo CLIProxyAPI) e usar $GO com CGO_ENABLED=0. Acha-se de novo via telemetria AppData/Roaming/go/telemetry se o cache mudar.

#toolchain/go #build/windows

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^go-toolchain-fora-do-path-cliproxyapi-bd32bbd03dff-content
