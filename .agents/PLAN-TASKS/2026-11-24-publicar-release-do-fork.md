---
dex_contract: spt
version: 3
status: 'CONCLUÍDO'
owner: 'sessao zcode (Chato comandando)'
date: '2026-11-24'
workspace: 'C:\CodexProjetos\CLIProxyAPI'
abertura:
  contexto: 'Fork dex-agent/CLIProxyAPI sem release e sem tags (git ls-remote --tags fork = 0 linhas). Historico reescrito: nenhuma tag do upstream e ancestral do HEAD. Conteudo do fork corresponde a v8.1.1 (pareamento por data e titulo). Actions habilitado no fork com 0 runs. 0 segredos configurados.'
  ferramentas: 'dex-git-fechamento (fechar-git.ps1 -Status e -DryRun), range_gate.py da skill dex-sanitizar-dados-pessoais, gh cli, chama-o-vigia para o workflow em background.'
  mentor: 'mentor-documental-github-actions se algum job do workflow falhar; mentor-documental-git se o push da tag falhar.'
origin: 'Pedido do dono em 2026-11-24: "faz o deploy", precedido de "antes faz a revisao do github padrao".'
goal:
  id: 'publicar-release-do-fork-2026-11-24'
  title: 'Publicar a primeira release do fork dex-agent/CLIProxyAPI'
  objective: 'Publicar a tag v8.1.1-dex.1 no fork com os binarios gerados pelo workflow release.yaml e a nota da release enxuta.'
context: 'Todo push de tag dispara .github/workflows/release.yaml (tags: *) com permissao de escrita; docker-image.yml tambem dispara em tags v* e falha por falta dos segredos do Docker Hub.'
problem: 'As outras maquinas precisam de um binario pronto para instalar o fork, e o fork nao tem release.'
decision: 'Publicar a tag v8.1.1-dex.1 sobre o HEAD de fork/main, so depois da confirmacao do dono.'
scope:
  include:
    - 'Completar o .gitignore padrao antes do commit'
    - 'Criar e enviar a tag anotada para o remoto fork'
    - 'Acompanhar o workflow release.yaml'
    - 'Substituir a nota da release por um texto curto'
    - 'Rodar o gate de faixa na faixa da tag'
  exclude:
    - 'Publicar imagem Docker'
    - 'Push para o remoto origin (upstream)'
    - 'Alterar os workflows do repositorio'
requirements:
  - id: REQ-01
    statement: 'O repositorio fecha limpo antes da tag'
    criteria:
      - id: C-01
        statement: 'git status --short lista zero arquivos depois do commit'
      - id: C-02
        statement: 'git check-ignore cobre o caminho .env.local'
  - id: REQ-02
    statement: 'A tag chega ao fork so depois da confirmacao do dono'
    criteria:
      - id: C-03
        statement: 'git ls-remote --tags fork lista a tag v8.1.1-dex.1'
      - id: C-04
        statement: 'A tag aponta para o mesmo commit de fork/main'
  - id: REQ-03
    statement: 'A release publica tem binarios e nota curta'
    criteria:
      - id: C-05
        statement: 'gh release view lista o arquivo CLIProxyAPI_8.1.1-dex.1_windows_amd64.zip'
      - id: C-06
        statement: 'gh release view lista o arquivo CLIProxyAPI_8.1.1-dex.1_linux_amd64.tar.gz'
      - id: C-07
        statement: 'gh release view lista o arquivo checksums.txt'
      - id: C-08
        statement: 'A nota da release tem menos de 60 linhas'
      - id: C-09
        statement: 'O gate de faixa devolve exit 0 na faixa da tag'
plan:
  - 'Completar o .gitignore e commitar as mudancas pendentes por caminho explicito'
  - 'Pedir a confirmacao do dono e criar a tag anotada'
  - 'Enviar a tag para o remoto fork e vigiar o workflow'
  - 'Substituir a nota da release e rodar o gate de faixa'
tasks:
  - id: A-01
    action: 'Completar o .gitignore com as 8 entradas padrao e commitar com fechar-git.ps1 por caminhos explicitos'
    covers: [REQ-01]
    done_when: [C-01, C-02]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'git status --short (saida vazia)'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'git check-ignore -q --no-index .env.local (exit 0)'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-02
    action: 'Criar a tag anotada v8.1.1-dex.1 sobre fork/main depois da confirmacao do dono'
    covers: [REQ-02]
    done_when: [C-03, C-04]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'git ls-remote --tags fork | grep v8.1.1-dex.1 (uma linha ou mais)'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-04
        proves: [C-04]
        method: command
        procedure: 'git rev-parse v8.1.1-dex.1^{} fork/main (dois shas iguais)'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Enviar a tag para o remoto fork e vigiar o workflow release.yaml em background'
    covers: [REQ-02]
    done_when: [C-03]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-05
        proves: [C-03]
        method: command
        procedure: 'gh run list --repo dex-agent/CLIProxyAPI --workflow release.yaml --limit 1 (status concluded)'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Substituir a nota da release por texto curto e rodar o gate de faixa'
    covers: [REQ-03]
    done_when: [C-05, C-06, C-07, C-08, C-09]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-06
        proves: [C-05, C-06, C-07]
        method: command
        procedure: 'gh release view v8.1.1-dex.1 --repo dex-agent/CLIProxyAPI --json assets --jq ".assets[].name" (lista os 3 arquivos)'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-07
        proves: [C-08]
        method: command
        procedure: 'gh release view v8.1.1-dex.1 --repo dex-agent/CLIProxyAPI --json body --jq .body | wc -l (menos de 60)'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-08
        proves: [C-09]
        method: command
        procedure: 'python range_gate.py . v8.1.1-dex.1 --secrets-only --gh-token (exit 0)'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'Item 0066 do tracker do registry ja integrado; atualizar o HANDOFF com a release publicada.'
risks:
  - 'A primeira tag do fork deixa a faixa do changelog sem tag anterior e a nota nasce com milhares de linhas; mitigacao: substituir a nota depois do workflow.'
  - 'docker-image.yml falha no fork por falta dos segredos do Docker Hub; mitigacao: run vermelho esperado e declarado, fora do escopo.'
  - 'O painel de gerenciamento consulta a ultima release do upstream; mitigacao: avisar que a versao do fork aparece diferente da do upstream.'
uncertainties:
  - 'O passo generate-notes da primeira tag pode falhar no fork sem tag anterior; nao medido porque o workflow nunca rodou neste fork.'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - 'git status --short'
  - 'gh release view v8.1.1-dex.1 --repo dex-agent/CLIProxyAPI'
execution_prompt: |
  /GOAL
  Execute o Trilho .agents/PLAN-TASKS/2026-11-24-publicar-release-do-fork.md no workspace C:\CodexProjetos\CLIProxyAPI. Pare antes da task A-02 para a confirmacao do dono.
---

# Publicar a primeira release do fork

Checklist (atualizado pela sessao):

- [x] A-01 .gitignore padrao + commit por caminho explicito (`d0d1ed08d`)
- [x] A-02 tag anotada v8.1.1-dex.1 (apos confirmacao do dono; objeto `ec55e2b8d`, alvo `ec7670aa0`)
- [x] A-03 push da tag para fork + workflow vigiado (run 45491486971, attempt 2)
- [x] A-04 nota curta (29 linhas) + gate de faixa (exit 0; recibo local `W21-range-gate-tag.txt`)

Veredito: PRONTO COM RESSALVA. 9 de 9 criterios verdes; o pacote `darwin-arm64` nao foi gerado.

Ocorrencias do bloco (medidas):

- **Revisao do dex-git-fechamento**: 8 entradas padrao faltavam no `.gitignore` (`.env.local` e `*.log` nao ignorados). Corrigidas em `d0d1ed08d`.
- **A skill recusou o `git add`** de `.agents/lembranca.md` (exit 1). Causa na regra do repo, nao na ferramenta: `.agents` e `.agents/*` ignoravam a pasta inteira com 94 arquivos versionados. Corrigido em `ec7670aa0` (ver abaixo).
- **Recorte do `.agents` com a dex-ignore**: removida a regra nua `.agents`; `.agents/*` segue como padrao; re-inclusos so os arquivos da raiz, `ESTACIONAMENTO`, `LIXEIRA`, `PLAN-TASKS`, `memorias` e `.dex-memoria`. `scripts`, `receipts`, `TEMP` e os grafos seguem ignorados: 7 dos 12 scripts nao versionados trazem caminho local ou linha com cara de credencial. Prova: `git add -- .agents/lembranca.md` exit 0 sem `-f`.
- **O primeiro push da tag nao disparou o Actions** (0 runs; o check suite do CodeRabbit foi criado, o do Actions nao). Causa nao identificada. A permissao de Actions foi reaplicada com os mesmos valores e a tag foi reenviada sob aprovacao do dono; o segundo push disparou em 30s. Nao ha prova de que a permissao tenha sido a causa.
- **`prepare-release` caiu com HTTP 422** (`body is too long`, limite de 125000 caracteres): sem tag anterior no fork, o changelog tinha 4969 entradas e 402975 caracteres.
- **Cura aprovada pelo dono**: tag de base `upstream-v8.1.1` (`a6126416d`, alvo `6eb8554f0`) e re-execucao dos jobs que falharam. O changelog caiu para 27 entradas e 2905 caracteres. O run proprio da tag de base falhou com o mesmo 422, como previsto.
- **`build darwin-arm64` cancelado 2 vezes** (exatos 15 minutos na fila, zero passos executados): o runner `macos-15` nao foi entregue. O runner `macos-15-intel` funcionou. Limite declarado; nao tentar de novo sem decisao do dono.
- **`docker-image`**: vermelho, como previsto (fork sem os segredos do Docker Hub).

Revisao do dex-git-fechamento (2026-11-24, -Status e -DryRun):

- identidade ok (dex-agent); branch `main` envia para o remoto `fork`; hooks em `tools/hooks`.
- 8 entradas padrao faltantes no `.gitignore`; `.env.local`, `*.log`, `*.tmp` e `__pycache__/` nao ignorados.
- pendente: `.agents/lembranca.md` modificado (linha de gatilho da memoria de release).
