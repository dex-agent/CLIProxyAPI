---
implementation_version: v2
layer: L2
slug: antigravity-suspenso-por-tos-violation-e-o-painel-d-c39b5e48e305
tags:
  - "#cliproxyapi/antigravity"
  - "#cliproxyapi/proxy"
  - "#cliproxyapi/painel"
---

# Antigravity suspenso por TOS_VIOLATION e o painel de gerenciamento embutido

CAUSA RAIZ (medida em 2026-11-25): em 2026-11-23 as 18:30:03 o Google respondeu TOS_VIOLATION e o executor do proxy suspendeu a credencial Antigravity (auths/logs/main.log, antigravity_executor_credits.go:537). O codigo trata TOS_VIOLATION como terminal: desativa a credencial de forma duradoura e grava tos_appeal_url e tos_appeal_url_text=Submit Appeal no arquivo de credencial.

SINTOMAS: a credencial em auths/ fica com disabled: true; o token continua sendo renovado a cada 30 minutos (o login e valido, a conta e que esta suspensa); GET /v1/models do proxy deixa de listar qualquer modelo Antigravity (em 25/11: 35 modelos, so openrouter-free, xai e opencode-go). Reiniciar o proxy NAO resolve.

COMO DIAGNOSTICAR (sem imprimir segredo): ler o campo disabled e a presenca de tos_appeal_url no JSON de auths/; grep 'suspended for TOS' em auths/logs/main.log; GET /v1/models e agrupar por owned_by.

SAIDAS: (1) enviar o recurso pelo link gravado na credencial e aguardar o Google; (2) fazer login com outra conta Google: cli-proxy-api -antigravity-login -no-browser. Nao basta colocar disabled: false.

PAINEL: o proxy ja serve o Management Center oficial embutido em http://127.0.0.1:8317/management.html (titulo CLI Proxy API Management Center, cerca de 4 MB). Mas a API de gerenciamento devolve 404 quando config.yaml nao tem management.secret-key: sem chave a Management API fica inteiramente desligada (config.example.yaml: a chave em texto puro e convertida em hash no inicio). Para o painel funcionar e preciso criar o bloco management: com secret-key e reiniciar o proxy (stop-proxy.ps1 e depois start-proxy.ps1).

O README lista paineis de terceiros (CPA-Manager-Plus, Oh-My-CPA, panel4cliproxyapi, CPA-Tray-Powershell para Windows), mas o painel embutido basta para ver credenciais e estado.

ACHADO VIZINHO: free-or-dots-studio-dots-3-note-preview foi aposentado pelo OpenRouter (404 no longer available em 25/11) e segue no grupo Gratis (todos).

#cliproxyapi/antigravity #cliproxyapi/proxy #cliproxyapi/painel

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^antigravity-suspenso-por-tos-violation-e-o-painel-d-c39b5e48e305-content
