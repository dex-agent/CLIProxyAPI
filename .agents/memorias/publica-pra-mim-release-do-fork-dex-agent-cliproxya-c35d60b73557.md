---
implementation_version: v2
layer: L2
slug: publica-pra-mim-release-do-fork-dex-agent-cliproxya-c35d60b73557
tags:
  - "#cliproxyapi/release"
  - "#cliproxyapi/push-gate"
---

# Publica pra mim = release do fork dex-agent/CLIProxyAPI

Executar os passos combinados em 2026-11-24:
1. Descobrir a versao do upstream em que o fork esta baseado.
2. Preparar a tag anotada v<versao>-dex.N para o HEAD de fork/main (N = proximo numero livre).
3. Conferir antes do push: o workflow .github/release.yaml do gatilho ate os artefatos; se aceita sufixo no nome da tag; se injeta caminho local ou dado pessoal nos binarios; se os Actions estao habilitados no fork.
4. Mostrar o resultado da conferencia e pedir confirmacao do dono antes de criar a tag.
5. Depois do push, acompanhar o workflow em background.
6. Ao terminar: conferir a pagina da release, listar os binarios por sistema, rodar o gate de faixa (range_gate.py da skill dex-sanitizar-dados-pessoais) na faixa da tag e atualizar o prompt de instalacao para baixar o binario em vez de compilar.

Por que: o fork e publico e todo push de tag dispara o release.yaml (tags '*', permissao de escrita), por isso a confirmacao antes da tag.

Fatos medidos em 2026-11-24, re-conferir antes de citar: o fork tinha zero releases; docker-image.yml empurra para eceasy/cli-proxy-api no Docker Hub com segredos que o fork nao deve ter; docker-compose.yml aponta para a imagem do upstream. Docker fica fora do pedido, a menos que o dono peca. O trabalho nasce de um Trilho (3 ou mais passos).

#cliproxyapi/release #cliproxyapi/push-gate

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^publica-pra-mim-release-do-fork-dex-agent-cliproxya-c35d60b73557-content
