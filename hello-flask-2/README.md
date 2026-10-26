# Hello-Flask 2.0

Protótipo web com comunicação assíncrona entre Front-end (JavaScript `fetch` com `async/await`) e Back-end (Flask rota `/api/hello` retornando JSON).

## Estrutura
- `app.py`: Servidor Flask com as rotas `/` e `/api/hello`.
- `templates/index.html`: Interface HTML com campo de entrada e botão.
- `static/style.css`: Estilização da página.
- `static/script.js`: Requisição assíncrona via `fetch("/api/hello")` e atualização do DOM.
- `documentacao/diagrama-sequencia.puml`: Diagrama de sequência PlantUML.