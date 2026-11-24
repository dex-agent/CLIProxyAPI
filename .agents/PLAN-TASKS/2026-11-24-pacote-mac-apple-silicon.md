---
dex_contract: spt
version: 3
status: 'CONCLUÍDO'
owner: 'sessao zcode (Chato comandando)'
date: '2026-11-24'
workspace: 'C:\CodexProjetos\CLIProxyAPI'
abertura:
  contexto: 'Release v8.1.1-dex.1 publicada com 9 pacotes; o job build darwin-arm64 foi cancelado 2 vezes com exatos 15 minutos na fila e zero passos executados (run 45491486971, attempts 2 e 3). O runner macos-15-intel do job darwin-amd64 comecou em 2 segundos e terminou em 4 minutos.'
  ferramentas: '.github/workflows/release.yaml (so a linha do runner e uma guarda de arquitetura), chama-o-vigia, push_gate.py (gate de pre-push), spt-kit/preflight.mjs.'
  mentor: 'mentor-documental-github-actions se o build cruzado falhar ou a guarda de arquitetura rejeitar o binario.'
origin: 'GO do dono em 2026-11-24 ao proximo passo recomendado: publicar o pacote de Mac Apple Silicon.'
goal:
  id: 'pacote-mac-apple-silicon-2026-11-24'
  title: 'Publicar o pacote de Mac Apple Silicon do fork'
  objective: 'Publicar uma release do fork que contenha o pacote CLIProxyAPI_<versao>_darwin_aarch64.tar.gz com binario arm64.'
context: 'O fork nao altera nenhum arquivo Go sobre a v8.1.1; o job compila com CGO_ENABLED=1 e GOARCH definido pelo job.'
problem: 'Mac Apple Silicon e a unica plataforma dos 11 alvos do workflow sem pacote na release.'
decision: 'Compilar o alvo darwin-arm64 no runner macos-15-intel, que o fork recebe, com uma guarda que falha o job se o binario nao for arm64.'
scope:
  include:
    - 'Trocar o runner do job darwin-arm64 para macos-15-intel'
    - 'Adicionar guarda de arquitetura no passo de build dos alvos macOS'
    - 'Criar a tag v8.1.1-dex.2 depois da confirmacao do dono'
    - 'Conferir o pacote publicado: cabecalho Mach-O arm64'
  exclude:
    - 'Apagar ou mover a tag v8.1.1-dex.1'
    - 'Publicar imagem Docker'
    - 'Alterar outros jobs do workflow'
requirements:
  - id: REQ-01
    statement: 'O workflow compila o alvo darwin-arm64 num runner que o fork recebe'
    criteria:
      - id: C-01
        statement: 'A linha runner do alvo darwin-arm64 no release.yaml e macos-15-intel'
      - id: C-02
        statement: 'O passo de build dos alvos macOS falha se o binario nao tiver a arquitetura do GOARCH'
  - id: REQ-02
    statement: 'O pacote de Mac Apple Silicon chega a release'
    criteria:
      - id: C-03
        statement: 'gh release view lista o arquivo CLIProxyAPI_8.1.1-dex.2_darwin_aarch64.tar.gz'
      - id: C-04
        statement: 'O cabecalho Mach-O do binario dentro do pacote declara arm64'
      - id: C-05
        statement: 'O sha256 do pacote confere com a linha do checksums.txt'
plan:
  - 'Editar o runner e adicionar a guarda de arquitetura'
  - 'Pedir a confirmacao do dono e criar a tag v8.1.1-dex.2'
  - 'Vigiar o workflow e conferir o pacote'
tasks:
  - id: A-01
    action: 'Trocar o runner do alvo darwin-arm64 e adicionar a guarda de arquitetura no build'
    covers: [REQ-01]
    done_when: [C-01, C-02]
    depends_on: []
    evidence_requirements:
      - id: ER-01
        proves: [C-01]
        method: command
        procedure: 'git show HEAD:.github/workflows/release.yaml | grep -A1 "target: darwin-arm64" (mostra runner: macos-15-intel)'
        expectation:
          kind: command_exit
          expected_exit_code: 0
      - id: ER-02
        proves: [C-02]
        method: command
        procedure: 'git show HEAD:.github/workflows/release.yaml | grep -c "Mach-O 64-bit executable" (maior ou igual a 1)'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-02
    action: 'Criar a tag anotada v8.1.1-dex.2 sobre fork/main depois da confirmacao do dono e envia-la ao fork'
    covers: [REQ-02]
    done_when: [C-03]
    depends_on: [A-01]
    evidence_requirements:
      - id: ER-03
        proves: [C-03]
        method: command
        procedure: 'gh release view v8.1.1-dex.2 --repo dex-agent/CLIProxyAPI --json assets --jq ".assets[].name" | grep darwin_aarch64 (uma linha)'
        expectation:
          kind: command_exit
          expected_exit_code: 0
  - id: A-03
    action: 'Baixar o pacote, conferir o checksum e ler o cabecalho Mach-O'
    covers: [REQ-02]
    done_when: [C-04, C-05]
    depends_on: [A-02]
    evidence_requirements:
      - id: ER-04
        proves: [C-04, C-05]
        method: command
        procedure: 'python: sha256 do pacote igual ao checksums.txt e cputype do cabecalho Mach-O igual a 0x0100000c'
        expectation:
          kind: command_exit
          expected_exit_code: 0
closure_gates:
  - 'Publicar a nota curta na release e atualizar o arquivo do prompt de instalacao com o nome da tag.'
risks:
  - 'O clang do Mac Intel pode nao produzir um arm64 executavel mesmo com a guarda passando no cabecalho; mitigacao: a guarda confirma a arquitetura e a release nota diz que o pacote nao foi executado em Mac.'
  - 'A tag nova regenera os outros 10 pacotes; mitigacao: mesmo codigo, checksums novos publicados junto.'
uncertainties:
  - 'Nenhum Mac Apple Silicon esta disponivel nesta maquina para executar o binario; a prova e o cabecalho Mach-O.'
gates:
  - 'spt_validate retorna valid=true e contract_version=3 antes de goal_start.'
validation:
  - 'gh release view v8.1.1-dex.2 --repo dex-agent/CLIProxyAPI --json assets'
execution_prompt: |
  /GOAL
  Execute o Trilho .agents/PLAN-TASKS/2026-11-24-pacote-mac-apple-silicon.md no workspace C:\CodexProjetos\CLIProxyAPI. Pare antes da task A-02 para a confirmacao do dono.
---

# Publicar o pacote de Mac Apple Silicon

Checklist (atualizado pela sessao):

- [x] A-01 runner do alvo darwin-arm64 + guarda de arquitetura (`ba8f8c3b`)
- [x] A-02 tag v8.1.1-dex.2 (apos confirmacao do dono; objeto `5914ffaca`, alvo `c1d3add94`; run 45506695907, 12 de 12 jobs verdes)
- [x] A-03 pacote conferido: sha256 igual ao checksums.txt; cabecalho Mach-O 64 com cputype arm64 (recibo local `W30-dex2/`)

Veredito: PRONTO. 5 de 5 criterios verdes. Release https://github.com/dex-agent/CLIProxyAPI/releases/tag/v8.1.1-dex.2 com 10 pacotes + checksums.txt e nota curta. Limite declarado: o binario arm64 nao foi executado num Mac Apple Silicon.
