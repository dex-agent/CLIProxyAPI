---
implementation_version: v2
layer: L2
slug: ci-do-cliproxyapi-roda-apenas-build-sem-testes-2e98af5340cd
tags:
  - "#ci/gaps"
  - "#build/go"
---

# CI do CLIProxyAPI roda apenas build (sem testes)

.github/workflows/pr-test-build.yml (branch main) executa go build e rm do binario - NAO roda go test. CI verde nao pega regressao de teste; a suite so roda local (go test ./...). Peca: job de teste no CI ou vigia local. Evidencia: transcricao do workflow em .agents/receipts/, achado W1.

#ci/gaps #build/go

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^ci-do-cliproxyapi-roda-apenas-build-sem-testes-2e98af5340cd-content
