# Instalação em outra máquina — prompt mantido

Este arquivo é o prompt de instalação do fork. Quem publica uma release ou muda a instalação atualiza este arquivo no mesmo bloco. Para usar: copie o bloco abaixo e cole no agente da máquina nova.

O prompt pede sempre a release mais recente do fork, então ele não precisa mudar a cada tag.

```text
Instale o CLIProxyAPI (fork dex-agent) nesta máquina.

FONTE
- Repositório: https://github.com/dex-agent/CLIProxyAPI.git
- Releases: https://github.com/dex-agent/CLIProxyAPI/releases (use a mais recente).
- Não use o repositório upstream (router-for-me) como origem da instalação.
- O fork não tem imagem Docker própria. Não use o docker-compose.yml do repositório.

REGRAS
- Leia o AGENTS.md do repositório depois de clonar. Siga as regras dele.
- Leia a mensagem de erro inteira antes de formar uma hipótese.
- Antes de criar qualquer script, procure um que já exista no repositório.
- Não imprima chaves, tokens nem o conteúdo do config.yaml na saída.
- Nunca faça push para este repositório durante a instalação.
- Se um passo falhar, corrija a causa e continue. Pare só se precisar de uma decisão minha.

PASSOS
1. Descubra o sistema e a arquitetura desta máquina.
2. Descubra a release mais recente do fork:
   gh release list --repo dex-agent/CLIProxyAPI --limit 1
   (ou leia a página de releases, se o gh não estiver instalado).
3. Baixe o pacote da release para o seu sistema e o arquivo checksums.txt.
   Nomes: linux_amd64, linux_aarch64, windows_amd64, windows_aarch64,
   darwin_amd64, darwin_aarch64, freebsd_amd64.
   No Linux, prefira o pacote sem sufixo. Use o sufixo _no-plugin só em musl ou sistema antigo.
4. Confira o sha256 do pacote contra o checksums.txt antes de extrair.
5. Extraia em uma pasta de instalação. O pacote traz o binário, LICENSE, os README e o config.example.yaml.
   Se não houver pacote para o seu sistema: clone o repositório e compile com Go 1.26 ou superior:
   go build -o cli-proxy-api ./cmd/server
6. Prepare a configuração:
   - Pegue config.example.fork.yaml no repositório como base para ZCode e Antigravity.
   - Copie para config.yaml, se config.yaml ainda não existir.
   - Substitua cada CHANGE_ME por um valor gerado localmente.
   - Confirme que config.yaml está no .gitignore.
   - Confirme que o servidor escuta em 127.0.0.1 em uma porta livre.
7. Crie um script de inicialização adequado ao sistema desta máquina (Windows, Linux ou macOS).
   Ele deve subir o servidor a partir da pasta de instalação e gravar log em arquivo.
8. Suba o servidor. Confirme a porta com uma chamada simples e local. Apague o processo de teste.
9. Liste os providers disponíveis a partir da fonte, não de memória:
   - rg -n "flag\.(Bool|String)Var" cmd/server/main.go
   - rg -n "case \".*-login" cmd/server/main.go
   - seção de providers em config.example.yaml
10. Faça a pergunta final (ver PERGUNTA FINAL).
11. Para cada provider que eu escolher:
   - rode o comando de login documentado na fonte;
   - para provider por chave de API, adicione a chave no config.yaml sem imprimi-la;
   - confirme que a pasta auths/ recebeu o arquivo de credencial (só o nome do arquivo);
   - reinicie o servidor e faça uma chamada de teste com o modelo mais barato do provider.
12. Ao terminar, mostre:
   - pasta de instalação;
   - comando para iniciar e para parar;
   - endereço local e porta;
   - lista dos providers instalados com o status de cada um (funcionou ou falhou, com o motivo);
   - qual release e qual pacote foram instalados.

PERGUNTA FINAL (obrigatória, com AskUserQuestion)
Depois do passo 9, antes de qualquer login, pergunte quais providers eu quero instalar.

Formato da pergunta:
- Pergunta: "Quais providers você quer instalar?"
- Header: "Providers"
- multiSelect: true
- Uma opção por provider encontrado no passo 9.
- Cada opção com nome claro e descrição de uma linha: o que é e o tipo de acesso
  (login OAuth, chave de API ou chave de serviço).
- Se houver mais de 4 opções, divida em duas perguntas na mesma chamada:
  "Providers por login OAuth" e "Providers por chave".
- Coloque primeiro a opção recomendada por mim: Antigravity (Google).
- Não deixe eu seguir sem escolher. Não escolha por mim.

Lista de referência (conferir com o passo 9 e corrigir se a fonte divergir):
- Antigravity: -antigravity-login (OAuth, Google)
- Codex / OpenAI: -codex-login (OAuth)
- Claude: -claude-login (OAuth)
- Kimi: -kimi-login (OAuth)
- xAI / Grok: -xai-login (OAuth)
- GitHub Copilot: -copilot-login (OAuth)
- Devin: -devin-login (OAuth)
- Meta: -meta-login (OAuth)
- Vertex AI: -vertex-import <arquivo.json> (conta de serviço)
- Providers por chave de API: ler a seção de api-keys do config.example.yaml

Flags úteis:
- -no-browser: não abre o navegador no OAuth (use em servidor sem interface).
- -oauth-callback-port <porta>: troca a porta de callback do OAuth.
- -local-model: usa os catálogos de modelo embutidos, sem busca remota.
- -tui: sobe com a interface de terminal.
- -config <caminho>: aponta outro arquivo de configuração.

Não faça a pergunta de providers antes de o servidor estar rodando.
```

## Estado da instalação (atualizar junto com a release)

- Última release: `v8.1.1-dex.2` (2026-11-24). Tem 10 pacotes + `checksums.txt`, incluindo `darwin_aarch64` (Mac Apple Silicon). A `v8.1.1-dex.1` ficou sem o pacote de Mac Apple Silicon.
- O pacote de Mac Apple Silicon foi compilado num runner Intel e conferido pelo cabeçalho do binário. Não foi executado num Mac Apple Silicon.
- O binário do fork é o mesmo do upstream v8.1.1: o fork não altera nenhum arquivo Go.
- O painel de gerenciamento compara a versão com a última release do upstream e mostra aviso de atualização.
