---
implementation_version: v2
layer: L2
slug: encoding-do-repo-cliproxyapi-working-crlf-loja-lf-s-5cb3c3050391
tags:
  - "#encoding/repo"
  - "#git/windows"
---

# Encoding do repo CLIProxyAPI: working CRLF / loja LF sem pin

Censo W2 (2405 fontes): working tree 100% CRLF, loja git 2583 arquivos i/lf LIMPOS, core.autocrlf=true (system config), SEM .gitattributes. 0 BOM; 125 arquivos UTF-8 valido nao-ASCII (mandarim em internal/tui/i18n.go, box-drawing em comentarios; validados por iconv exit 0). Risco: contribuidor com autocrlf=false colapsaria a loja para CRLF. Proposta de pin *.go text eol=lf registrada - decisao do upstream.

#encoding/repo #git/windows

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^encoding-do-repo-cliproxyapi-working-crlf-loja-lf-s-5cb3c3050391-content
