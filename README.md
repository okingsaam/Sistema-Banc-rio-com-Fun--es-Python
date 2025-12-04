# Sistema Bancário Simples (Python)

Este repositório contém uma aplicação de linha de comando que simula operações bancárias básicas: criar conta, depositar, sacar, transferir e ver extrato.

Status: pronto para executar (menu interativo disponível em `main.py`) — configuração do VS Code incluída.

Requisitos
- Python 3.8 ou superior (testado com Python 3.13)

Instalação (opcional)
1. Recomendo criar um ambiente virtual:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. (Opcional) Instalar dependências — este projeto não usa dependências externas no momento.

Como executar

- Pelo terminal (PowerShell) — no diretório raiz do projeto:

```powershell
py -3 main.py
# ou
python main.py
```

- Se você encontrar erro de import relacionado a `src`, rode com `PYTHONPATH` apontando para a pasta `src`:

```powershell
$env:PYTHONPATH = "src"
py -3 main.py
```

- Via VS Code (com um clique / F5):
  1. Abra a pasta do projeto no VS Code.
  2. Selecione o interpretador Python correto (canto inferior direito).
  3. Abra a aba "Executar e Depurar" (Ctrl+Shift+D).
  4. Escolha a configuração **Run main.py (integratedTerminal)**.
  5. Pressione F5 ou clique no botão verde para executar — o menu aparecerá no terminal integrado.

Demo (execução automática)
- Para testar rapidamente sem interação, execute o demo que cria duas contas e realiza operações:

```powershell
py -3 scripts/demo.py
```

Isso irá gerar/atualizar `data/banco_db.json` com as contas e transações criadas.

Estrutura do projeto
- `main.py` — ponto de entrada que inicia o menu interativo.
- `scripts/demo.py` — script não interativo para demonstração e testes rápidos.
- `src/Bank.py` — lógica do banco (criar conta, depositar, sacar, transferir).
- `src/Models.py` — modelos de dados `Account` e `Transaction`.
- `src/Storage.py` — serialização / desserialização (JSON) em `data/banco_db.json`.
- `src/Menu.py` — interface de linha de comando (menu interativo).
- `.vscode/launch.json` — configuração para executar `main.py` no VS Code.
- `.vscode/settings.json` — configuração do analisador (Pylance) para encontrar `src`.

Sobre avisos/erros no VS Code (Pylance)
- Se você abrir o projeto no VS Code e ver muitos problemas na aba "Problemas", provavelmente são avisos do Pylance relacionados a imports não resolvidos ou checagem de tipos.
- As configurações fornecidas em `.vscode/settings.json` adicionam `src` ao `python.analysis.extraPaths` e desativam a checagem estrita de tipos, reduzindo falsos-positivos. Caso ainda veja avisos, recarregue a janela do VS Code (Ctrl+Shift+P → "Developer: Reload Window").

Contribuição e testes
- Sinta-se à vontade para abrir issues ou pull requests. Para testes rápidos você pode adicionar testes em `tests/`.

Contato
- Autor: okingsaam

----
Se quiser, eu posso:
- Rodar uma sessão interativa aqui e copiar a saída para você, ou
- Padronizar imports para um estilo absoluto (ex.: `from src.Bank import Bank`) ou transformar `src` em um pacote instalável.
