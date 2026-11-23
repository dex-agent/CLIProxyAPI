# Estacionamento

> Índice derivado dos itens. Não edite linhas manualmente; reconstrua com
> `parking-directory.py rebuild-index`.

## Itens

| Localizador | Status | Tipo | Nome | Owner | Quando | Destino | Origem |
|---|---|---|---|---|---|---|---|
| [EST-CLIPROXY-PROXY-SOBREVIVE-RESTART-ZCODE](./itens/EST-CLIPROXY-PROXY-SOBREVIVE-RESTART-ZCODE.md) | active | risk | Proxy via WMI ainda nao provado contra restart do ZCode | sessao-do-projeto | no primeiro uso depois do proximo restart do ZCode | dex-frontmatter-finder-padrao | zcode:sess_a0645205-1434-4eb5-a371-5a727fc31ebb |
| [EST-CLIPROXY-REGISTRO-PROVIDER-DUPLICADO](./itens/EST-CLIPROXY-REGISTRO-PROVIDER-DUPLICADO.md) | active | debt | Registro de provider no ZCode duplicado em seis scripts | sessao-do-projeto | no proximo cadastro ou alteracao de provider no provider_config.json do ZCode | dex-frontmatter-finder-padrao | zcode:sess_a0645205-1434-4eb5-a371-5a727fc31ebb |
| [EST-CLIPROXY-RESSYNC-GRATIS-TODOS](./itens/EST-CLIPROXY-RESSYNC-GRATIS-TODOS.md) | active | risk | Grupo Gratis (todos) nao se ressincroniza sozinho | sessao-do-projeto | quando um alias free-or-* ou free-oc-* devolver 404; depois de cada sync dos free do OpenRouter | dex-frontmatter-finder-padrao | zcode:sess_a0645205-1434-4eb5-a371-5a727fc31ebb |
| [EST-CLIPROXY-SUITE-MINIMA-MERGE-CHECK](./itens/EST-CLIPROXY-SUITE-MINIMA-MERGE-CHECK.md) | active | risk | Gate de merge com SUITE vazia: avisa e nao bloqueia | sessao-do-projeto | quando o dono quiser o gate de merge bloqueando de verdade | dex-frontmatter-finder-padrao | zcode:sess_a0645205-1434-4eb5-a371-5a727fc31ebb |
| [EST-CLIPROXY-TEMPLATE-FORK-SEM-GRATIS](./itens/EST-CLIPROXY-TEMPLATE-FORK-SEM-GRATIS.md) | active | debt | config.example.fork.yaml nao descreve o bloco gratis-todos | sessao-do-projeto | quando o fork publico for limpo ou recriado | dex-frontmatter-finder-padrao | zcode:sess_a0645205-1434-4eb5-a371-5a727fc31ebb |

## Gatilhos de retomada

- [EST-CLIPROXY-PROXY-SOBREVIVE-RESTART-ZCODE] Proxy via WMI ainda nao provado contra restart do ZCode #cliproxyapi/proxy #windows/processo-desacoplado -> [[itens/EST-CLIPROXY-PROXY-SOBREVIVE-RESTART-ZCODE|Proxy via WMI ainda nao provado contra restart do ZCode]] ^est-cliproxy-proxy-sobrevive-restart-zcode
- [EST-CLIPROXY-REGISTRO-PROVIDER-DUPLICADO] Registro de provider no ZCode duplicado em seis scripts #cliproxyapi/registro-provider #zcode/duplicacao -> [[itens/EST-CLIPROXY-REGISTRO-PROVIDER-DUPLICADO|Registro de provider no ZCode duplicado em seis scripts]] ^est-cliproxy-registro-provider-duplicado
- [EST-CLIPROXY-RESSYNC-GRATIS-TODOS] Grupo Gratis (todos) nao se ressincroniza sozinho #cliproxyapi/gratis-todos #openrouter/free -> [[itens/EST-CLIPROXY-RESSYNC-GRATIS-TODOS|Grupo Gratis (todos) nao se ressincroniza sozinho]] ^est-cliproxy-ressync-gratis-todos
- [EST-CLIPROXY-SUITE-MINIMA-MERGE-CHECK] Gate de merge com SUITE vazia: avisa e nao bloqueia #cliproxyapi/merge-gate -> [[itens/EST-CLIPROXY-SUITE-MINIMA-MERGE-CHECK|Gate de merge com SUITE vazia: avisa e nao bloqueia]] ^est-cliproxy-suite-minima-merge-check
- [EST-CLIPROXY-TEMPLATE-FORK-SEM-GRATIS] config.example.fork.yaml nao descreve o bloco gratis-todos #cliproxyapi/fork #cliproxyapi/gratis-todos -> [[itens/EST-CLIPROXY-TEMPLATE-FORK-SEM-GRATIS|config.example.fork.yaml nao descreve o bloco gratis-todos]] ^est-cliproxy-template-fork-sem-gratis

## Compatibilidade

A fila histórica pode continuar em [`../ESTACIONAMENTO.md`](../ESTACIONAMENTO.md)
até uma migração comprovar paridade de identidade e conteúdo.
