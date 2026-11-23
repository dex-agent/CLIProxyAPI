---
dex_contract: spt
version: 3
status: 'RASCUNHO'
owner: 'sessao-zcode-dex (GO do dono 2026-11-23: apagou dex-agent/CLIProxyAPI e autorizou recriar); comandante $chato'
date: '2026-11-23'
workspace: 'C:\CodexProjetos\CLIProxyAPI'
abertura:
  contexto: "O fork publico dex-agent/CLIProxyAPI foi apagado pelo dono em 2026-11-23 porque o primeiro push levou e-mail do dono e corpos de requisicao (ficha RECEIPTS-NAO-VERSIONADOS, PENDENTES fork-dados-pessoais, memoria host repo-publico-antes-do-push). Medido antes de agir: gh devolve repositorio inexistente; conta autenticada dex-agent (User) com escopo repo; main local com 14 commits sobre 6eb8554f e arvore limpa; nenhum commit do intervalo toca .agents/receipts (controle positivo: 3 tocam GATILHOS-VIVOS); os refs fork/* apontam para o repositorio morto e nao tem commit unico (fork/dev e ancestral de origin/main); os 6 ramos de rastreamento fork/* mostram que o primeiro era fork verdadeiro. Achado novo do gate: a chave de acesso local do proxy esta fixa em 8 arquivos versionados, em 15 blobs desde o commit de instalacao."
  ferramentas: "sanitizar-scan.py da skill dex-sanitizar-dados-pessoais (inventario read-only; tinha NameError no validador de CNPJ, corrigido nesta sessao nas 2 copias com harness RED->GREEN); W18-export-new-blobs-scan.py (hoje .agents/scripts/push_gate_scan.py: exporta os blobs novos do intervalo, roda o scanner e tria com saida mascarada) e .agents/scripts/push_gate_credentials.py (credenciais do runtime local em 0 blobs); git filter-repo a40bce548d2c com --refs 6eb8554f..main (modo parcial: reescreve so os commits da casa e preserva a ancestridade com o upstream, provado em clone descartavel); gh (criar o fork e conferir); spt-kit/preflight.mjs (validacao local deste Trilho; spt_validate MCP ausente nesta sessao); dex-audio-motor, dex-memoria v2 e validate-memory-batch.py no fechamento."
  mentor: "mentor-documental-git para duvida de filtro e refs; o comportamento do filter-repo foi medido em clone descartavel e nao presumido da documentacao."
origin: "GO do dono 2026-11-23: apagou dex-agent/CLIProxyAPI e escreveu que pode criar novamente, sob o workflow base PPIRTV com $chato como comandante."
goal:
  id: recriar-fork-limpo-261123
  title: 'Recriar o fork publico dex-agent/CLIProxyAPI sem dado pessoal e sem credencial'
  objective: "O repositorio publico dex-agent/CLIProxyAPI volta a existir com os commits da casa sobre o upstream 6eb8554f, sem e-mail do dono, sem corpo de requisicao, sem a chave local do proxy e sem ponteiro para o historico antigo, e o alcance desse historico no GitHub fica medido com a remocao encaminhada ao dono."
context: "O repositorio remoto nao existe mais, então a reescrita do historico local custa um comando e nao deixa objeto solto em lugar nenhum. Depois do primeiro push qualquer reescrita volta a exigir force-push. O gate de sanitizacao roda antes de cada push."
problem: "O fork publico nao existe; o historico local ainda carrega a chave de acesso local do proxy em texto fixo e um ponteiro para o commit antigo; e o historico antigo continua acessivel no GitHub pelo namespace do upstream mesmo com o fork apagado."
decision: "Reescrever so os commits da casa trocando a chave e o ponteiro do commit antigo por marcadores, corrigir os 4 scripts que fixavam a chave para lerem o config.yaml, rodar o gate, recriar como fork verdadeiro do upstream (como era o primeiro) e publicar main. Medido em 2026-11-23 antes de recriar: apagar o fork nao removeu o historico antigo, que segue servido pelo namespace do upstream porque a rede de forks compartilha o armazem de objetos; a remocao depende de pedido ao suporte do GitHub, que so o dono consegue abrir."
scope:
  include:
    - 'historico local de main no intervalo 6eb8554f..main'
    - '.agents/scripts/start-proxy.ps1, stop-proxy.ps1, free_aggregator.py, register_zcode_provider.py e register_xai_provider.py'
    - '.agents/PLAN-TASKS, ACTIVE.md, HANDOFF.md e PENDENTES.md'
    - 'repositorio GitHub dex-agent/CLIProxyAPI'
  exclude:
    - 'mesclar os 51 commits novos do upstream (bloco proprio)'
    - 'trocar o valor da chave do proxy no config.yaml e nos providers do ZCode (so vale em 127.0.0.1; fica como recomendacao)'
    - 'limpar os scripts de sessao versionados em .agents/scripts (decisao do dono sobre o que o fork carrega)'
    - 'apagar as copias locais do historico antigo (decisao do dono)'
requirements:
  - id: REQ-01
    statement: 'O historico a publicar nao carrega credencial nem dado pessoal.'
    criteria:
      - id: C-01
        statement: 'A busca pela chave local do proxy em main devolve 0 arquivos.'
      - id: C-02
        statement: 'A busca pela chave local do proxy no ramo de seguranca devolve mais de 0 arquivos.'
      - id: C-03
        statement: 'O relatorio do scanner registra mail_like_count=0.'
      - id: C-04
        statement: 'O relatorio do scanner registra head_files_not_covered=0.'
      - id: C-05
        statement: 'Nenhum commit do intervalo toca .agents/receipts.'
  - id: REQ-02
    statement: 'A ancestridade com o upstream esta preservada.'
    criteria:
      - id: C-06
        statement: 'git merge-base main origin/main devolve 6eb8554f0ede597b2aa3e508ffb3f111d3c2b9e6.'
      - id: C-07
        statement: 'A contagem total de commits do historico e igual a do ramo de seguranca somada aos commits novos.'
  - id: REQ-03
    statement: 'Os scripts leem a chave do proxy a partir do config.yaml.'
    criteria:
      - id: C-08
        statement: 'start-proxy.ps1 responde JA_ATIVO com http=200.'
      - id: C-09
        statement: 'Um pedido a /v1/models com chave errada responde 401.'
      - id: C-10
        statement: 'register_zcode_provider.py imprime JA_EXISTE.'
  - id: REQ-04
    statement: 'O repositorio publico existe com o historico novo.'
    criteria:
      - id: C-11
        statement: 'git ls-remote fork refs/heads/main devolve o SHA de HEAD local.'
      - id: C-12
        statement: 'gh repo view devolve visibility PUBLIC.'
  - id: REQ-05
    statement: 'O alcance do historico antigo no GitHub esta medido e a remocao tem rota registrada.'
    criteria:
      - id: C-13
        statement: 'Nenhum arquivo de main cita o SHA de um commit do historico antigo.'
      - id: C-14
        statement: 'PENDENTES.md registra o pedido de remocao dos objetos antigos ao suporte do GitHub.'
  - id: REQ-06
    statement: 'O estado vivo registra o desfecho.'
    criteria:
      - id: C-15
        statement: 'PENDENTES.md marca fork-dados-pessoais como concluida.'
      - id: C-16
        statement: 'HANDOFF.md tem a secao W18.'
  - id: REQ-07
    statement: 'O proxy pode ser ligado e desligado por script.'
    criteria:
      - id: C-17
        statement: 'stop-proxy.ps1 encerra o proxy deste repositorio.'
      - id: C-18
        statement: 'stop-proxy.ps1 com o proxy ja parado responde JA_PARADO.'
plan:
  - 'P1: Trilho + preflight verde'
  - 'P2: reescrita parcial do historico com ramo de seguranca'
  - 'P3: scripts leem a chave do config.yaml + stop-proxy.ps1 + testes'
  - 'P4: gate de sanitizacao + recriar o fork + push'
  - 'P5: medida de onde o historico antigo ainda responde e rota de remocao'
  - 'P6: estado vivo, memorias e fechamento'
tasks:
  - id: A-01
    action: 'Reescrever os commits da casa trocando a chave por marcador, com ramo de seguranca'
    covers: [REQ-01, REQ-02]
    done_when: [C-01, C-02, C-06, C-07]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'git grep -l -F -f .agents/receipts/W18-proxy-key-pattern.txt main'
        expectation:
          kind: command_exit
          expected_exit_code: 1
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'git grep -l -F -f .agents/receipts/W18-proxy-key-pattern.txt pre-scrub-main'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-03
        proves: [C-06]
        method: command
        procedure: 'git merge-base main origin/main | grep -c 6eb8554f0ede597b2aa3e508ffb3f111d3c2b9e6'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-04
        proves: [C-07]
        method: command
        procedure: 'test "$(git rev-list --count main)" -eq "$(( $(git rev-list --count pre-scrub-main) + 0 ))"'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-02
    action: 'Fazer os 4 scripts lerem a chave do proxy do config.yaml, criar stop-proxy.ps1 e testar'
    covers: [REQ-03, REQ-07]
    done_when: [C-08, C-09, C-10, C-17, C-18]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-05
        proves: [C-08]
        method: command
        procedure: 'powershell -NoProfile -ExecutionPolicy Bypass -File .agents/scripts/start-proxy.ps1 | grep -c "^JA_ATIVO http=200"'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-06
        proves: [C-09]
        method: command
        procedure: 'curl -s -o /dev/null -w "%{http_code}" -H "Authorization: Bearer wrong-key" http://127.0.0.1:8317/v1/models | grep -c "^401$"'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-07
        proves: [C-10]
        method: command
        procedure: 'python -I -X utf8 .agents/scripts/register_zcode_provider.py | grep -c "^JA_EXISTE"'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-16
        proves: [C-17]
        method: command
        procedure: 'powershell -NoProfile -ExecutionPolicy Bypass -File .agents/scripts/stop-proxy.ps1 | grep -c "^PARADO"'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-17
        proves: [C-18]
        method: command
        procedure: 'powershell -NoProfile -ExecutionPolicy Bypass -File .agents/scripts/stop-proxy.ps1 | grep -c "^JA_PARADO"'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Rodar o gate de sanitizacao, recriar o fork e publicar main'
    covers: [REQ-01, REQ-04]
    done_when: [C-01, C-03, C-04, C-05, C-11, C-12]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-08
        proves: [C-01, C-05]
        method: command
        procedure: 'git grep -l -F -f .agents/receipts/W18-proxy-key-pattern.txt main; git log --oneline 6eb8554f..main -- .agents/receipts'
        expectation:
          kind: command_exit
          expected_exit_code: 1
      - id: ER-09
        proves: [C-03, C-04]
        method: command
        procedure: 'python -I -B -X utf8 .agents/scripts/push_gate_scan.py C:/CodexProjetos/CLIProxyAPI 6eb8554f..main C:/CodexProjetos/CLIProxyAPI-receipts-local-20261123 | grep -c -e "mail_like_count=0" -e "head_files_not_covered=0 \\[\\]"'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-10
        proves: [C-11]
        method: command
        procedure: 'git ls-remote fork refs/heads/main | grep -c "$(git rev-parse HEAD)"'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-11
        proves: [C-12]
        method: command
        procedure: 'gh repo view dex-agent/CLIProxyAPI --json visibility | grep -c PUBLIC'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-04
    action: 'Medir onde o historico antigo ainda responde e registrar a rota de remocao'
    covers: [REQ-05]
    done_when: [C-13, C-14]
    depends_on: [A-03]
    evidence_requirements:
      - id: ER-12
        proves: [C-13]
        method: command
        procedure: 'git grep -l -F -f .agents/receipts/W18-old-sha-patterns.txt main'
        expectation:
          kind: command_exit
          expected_exit_code: 1
      - id: ER-13
        proves: [C-14]
        method: command
        procedure: 'grep -c "suporte do GitHub" .agents/PENDENTES.md'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-05
    action: 'Atualizar estado vivo, gravar memorias e fechar o bloco'
    covers: [REQ-06]
    done_when: [C-15, C-16]
    depends_on: [A-04]
    evidence_requirements:
      - id: ER-14
        proves: [C-15]
        method: command
        procedure: 'grep -c "\"id\": \"fork-dados-pessoais\", \"status\": \"concluida\"" .agents/PENDENTES.md'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-15
        proves: [C-16]
        method: command
        procedure: 'grep -c "^## W18" .agents/HANDOFF.md'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'gate de sanitizacao verde antes de cada push (ficha RECEIPTS-NAO-VERSIONADOS)'
  - 'memorias do bloco gravadas por dex-memoria e validadas'
  - 'HANDOFF, ACTIVE e PENDENTES atualizados e publicados'
risks:
  - 'filter-repo em modo integral reescreve o upstream e rompe a ancestridade: usar so --refs 6eb8554f..main e conferir o merge-base'
  - 'o ramo de seguranca guarda os commits antigos com a chave em texto: e local, nunca e publicado, e sai no fechamento depois do garimpo'
  - 'MEDIDO: o historico antigo sobrevive ao apagar o fork e segue acessivel pelo namespace do upstream (API, pagina e raw responderam 200 sem login em 2026-11-23); so o suporte do GitHub remove, e o repositorio novo nao pode carregar o ponteiro'
  - 'stop-proxy.ps1 encerra o proxy: sessoes do ZCode que estejam usando um provider via proxy perdem a conexao ate o start seguinte'
uncertainties:
  - 'ressalva residual: o fork novo entra na mesma rede do upstream, entao o commit antigo tambem pode responder pelo namespace do fork novo; medir depois da recriacao e informar o dono'
  - 'ressalva residual: o numero de commits publicados cresce com os commits de estado do fechamento, entao a conferencia de ancestridade usa o merge-base e nao uma contagem fixa'
gates:
  - 'preflight.mjs devolve achados=0 antes de executar (spt_validate MCP ausente nesta sessao: validador local com evidencia registrada).'
validation:
  - 'node C:/CodexProjetos/dex-PPIRTV/spt-kit/preflight.mjs .agents/PLAN-TASKS/2026-11-23-recriar-fork-limpo.md'
  - 'procedures dos ER-01 a ER-15, cada uma com o exit esperado'
execution_prompt: |
  /GOAL
  Executar o trilho 2026-11-23-recriar-fork-limpo.md no workspace C:\CodexProjetos\CLIProxyAPI: reescrever so os commits da casa, tirar a chave fixa dos scripts, rodar o gate de sanitizacao, recriar o fork publico dex-agent/CLIProxyAPI, provar que o historico antigo sumiu e fechar o estado vivo.
---

# Recriar o fork público dex-agent/CLIProxyAPI limpo

Detalhes no frontmatter. Checklist visual:

- [x] A-01 reescrita parcial do histórico com ramo de segurança — 14 commits, 0 de 14 com mudança fora da chave e do ponteiro; base `6eb8554f`
- [x] A-02 scripts leem a chave do config.yaml, stop-proxy.ps1 e testes — JA_ATIVO, 401 com chave errada, JA_EXISTE, PARADO/JA_PARADO
- [x] A-03 gate + recriar o fork + push — 129 blobs verdes; compare da API 16 à frente, 0 atrás
- [x] A-04 medida de onde o histórico antigo ainda responde e rota de remoção — 9 de 10 commits servidos em cada namespace; pedido ao suporte redigido
- [ ] A-05 estado vivo, memórias e fechamento
