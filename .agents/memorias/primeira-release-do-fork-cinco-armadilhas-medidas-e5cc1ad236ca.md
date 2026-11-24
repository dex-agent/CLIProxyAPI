---
implementation_version: v2
layer: L2
slug: primeira-release-do-fork-cinco-armadilhas-medidas-e5cc1ad236ca
tags:
  - "#cliproxyapi/release"
  - "#cliproxyapi/gitignore"
---

# Primeira release do fork: cinco armadilhas medidas

Medido em 2026-11-24 ao publicar v8.1.1-dex.1 (Trilho .agents/PLAN-TASKS/2026-11-24-publicar-release-do-fork.md; detalhe no HANDOFF W21).

1. A tag de base upstream-v8.1.1 (alvo 6eb8554f0) nao deve ser apagada. Sem tag anterior no fork, o release.yaml monta o changelog de todo o historico (4969 entradas, 402975 caracteres) e a criacao da release cai com HTTP 422 body is too long (limite 125000). Com a tag de base: 27 entradas.
2. O primeiro push de uma tag pode nao disparar o Actions no fork (0 runs, embora o GitHub tenha recebido o push). Causa nao identificada. Saida usada: reaplicar a permissao de Actions e reenviar a tag, com aprovacao do dono. Conferir com gh run list antes de concluir que o workflow quebrou.
3. O job darwin-arm64 (runner macos-15) fica 15 minutos na fila e e cancelado sem executar passo. Medido 2 vezes. macos-15-intel funciona. Mac Apple Silicon instala compilando do clone.
4. docker-image fica vermelho em toda tag v* (fork sem os segredos do Docker Hub). Esperado.
5. O .gitignore do upstream ignorava .agents inteira com 94 arquivos versionados. O recorte vigente: .agents/* como padrao e re-inclusao so do estado vivo. scripts, receipts e TEMP seguem ignorados; 7 dos 12 scripts nao versionados trazem caminho local ou linha com cara de credencial.

O fork nao altera nenhum arquivo Go sobre a v8.1.1: o binario da release e o do upstream.

#cliproxyapi/release #cliproxyapi/gitignore

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^primeira-release-do-fork-cinco-armadilhas-medidas-e5cc1ad236ca-content
