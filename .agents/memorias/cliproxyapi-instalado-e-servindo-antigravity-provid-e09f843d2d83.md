---
implementation_version: v2
layer: L2
slug: cliproxyapi-instalado-e-servindo-antigravity-provid-e09f843d2d83
tags:
  - "#instalacao/cliproxyapi"
  - "#zcode/provider"
  - "#antigravity/e2e"
---

# CLIProxyAPI instalado e servindo antigravity; provider cadastrado no ZCode com E2E provado

Instalacao viva 2026-11-22 (repo CLIProxyAPI, HEAD 8a3f9dde+): binario cli-proxy-api.exe (build exit 0, CGO_ENABLED=0, toolchain via .agents/scripts/go-env.sh); config.yaml MINIMO v8 (host 127.0.0.1, port 8317, access.api-keys=[<PROXY-KEY>], auth-dir ./auths) — config.yaml e gitignored, nunca versionar. Login antigravity: ./cli-proxy-api.exe --config config.yaml --antigravity-login (OAuth Google browser, callback localhost; token em auths/antigravity-<email>.json). Server: ./cli-proxy-api.exe --config config.yaml (127.0.0.1:8317). Catalogo vivo: GET /v1/models com Bearer <PROXY-KEY> (12 modelos antigravity: gemini-4-argon-high, gemini-3.8-flash-high/tiered, gemini-3.1-flash-image/lite, gemini-3.5-flash-lite, gemini-4-hydrogen/neon-xhigh, gemini-3-flash, gpt-oss-120b-medium, claude-opus-5-5-high, claude-sonnet-5-5-high — sufixos -high/-tiered/-xhigh SAO os IDs reais do catalogo, nao alias inventados). E2E PROVADO 2026-11-22: nao-stream (gemini-3-flash, 15+7 tokens) e stream (gemini-3.8-flash-high e claude-sonnet-5-5-high, chunks com conteudo) — receipts .agents/receipts/W11-*. Provider no ZCode: cadastrado no provider_config.json v2 (providerName CLIProxyAPI, api openai-chat-completions http://127.0.0.1:8317/v1, access api-key, 12 modelos em personalModelIds+modelOrder, 12 regras providerModelRules enabled-only sem inventar contextWindow) — providerId 398edcea-3b95-4394-a6fa-54cc40754eb8, backup provider_config.json.backup-20261122-cliproxyapi; validado contra exemplo canonico da doc oficial do ZCode (mentor-documental-zcode fulltext r3) e hot-reload por polling confirmado (#pollOnce emite poll-changed). ISSO E A ROTA B da decisao gemini-zcode 261122: mantida como NAO instalada para o plano ZCode — este provider serve TESTES/uso pontual de modelos antigravity, nao substitui o elenco proprio do ZCode.

#instalacao/cliproxyapi #zcode/provider #antigravity/e2e

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^cliproxyapi-instalado-e-servindo-antigravity-provid-e09f843d2d83-content
