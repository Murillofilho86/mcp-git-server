Passo 7 — Conectar ao Claude Code

Agora o momento de verdade. Sai do Inspector (Ctrl+C) e roda:


claude mcp add git-server -- uv run --directory /caminho/absoluto/para/mcp-git-server server.py

Substitui /caminho/absoluto/para/mcp-git-server pelo path real.

Confirma que o server foi registrado:
- claude mcp list

Usar no Claude Code
- claude
Dentro da sessão, pede algo que deveria usar a tool:
Use git-server para ver o status do repositório em ~/projetos/mcp-git-server


uv --version responde
uv run mcp dev server.py sobe o Inspector
git_status funciona no Inspector contra um repo real
claude mcp list mostra git-server