---
implementation_version: v2
layer: L2
slug: apagar-um-fork-nao-remove-o-historico-antigo-a-rede-d4b87d5bc57a
tags:
  - "#cliproxyapi/fork-publico"
  - "#git/historico-exposto"
  - "#github/rede-de-forks"
---

# Apagar um fork nao remove o historico antigo: a rede de forks compartilha o armazem de objetos

Apagar um fork no GitHub NAO remove os objetos inalcancaveis. Medido em 2026-11-23 no fork dex-agent/CLIProxyAPI (upstream router-for-me/CLIProxyAPI): com o fork recem-apagado pelo dono, o commit antigo com dado pessoal ainda respondia 200 SEM LOGIN pela API, pela pagina e pelo raw na namespace do upstream, e a pasta de recibos antiga ainda listava 147 arquivos; com o fork recriado (fork verdadeiro = mesma rede) voltou a responder tambem pela namespace do fork. A rede de forks compartilha o armazem de objetos com o upstream. UNICA ROTA DE REMOCAO: pedido ao suporte do GitHub, aberto pelo dono da conta (texto pronto no recibo local W18-support-ticket.txt). A afirmacao anterior, de que apagar seria a remocao completa, estava errada: foi dita sem medir a namespace do upstream. O repositorio novo nunca pode citar o SHA de um commit do historico antigo, porque e o atalho para o conteudo exposto. GATE ANTES DE CADA PUSH (W18): (1) exportar os blobs novos do intervalo e rodar o scanner da casa sobre eles (.agents/scripts/push_gate_scan.py), com controle positivo em toda busca vazia; (2) conferir que nenhuma credencial do runtime local aparece (.agents/scripts/push_gate_credentials.py: chave do proxy, token do OpenCode, token do GitHub); (3) nenhum SHA antigo citado. Com esse gate a chave de acesso local do proxy foi achada em 15 blobs (o scanner de e-mail e caminho nao acusa valor de chave fixo em codigo) e removida do historico. REESCRITA SO DOS COMMITS DA CASA: git filter-repo --force --refs <base>..main --replace-text <arquivo>. O --refs implica modo parcial: reescreve so o intervalo e preserva a ancestridade e os SHAs do upstream (conferir com merge-base e com a compare da API). O modo integral reescreve tudo e rompe o parentesco. MEDIR SEMPRE: commit conhecido responde 200; SHA inventado responde 422 na API e 404 na pagina; corpo descartado, nunca lido. Armadilha de medida: o historico antigo tinha outra base, entao um 'git log tip ^base' com a base errada listou o projeto inteiro (5066 commits) e o laco de consultas na API quase consumiu a cota; conferir a contagem antes de laquear chamadas.

#cliproxyapi/fork-publico #git/historico-exposto #github/rede-de-forks

[Voltar às lembranças](../lembranca.md) [[lembranca|Lembranças]]

^apagar-um-fork-nao-remove-o-historico-antigo-a-rede-d4b87d5bc57a-content
