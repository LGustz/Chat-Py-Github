# 💬 Chat em Tempo Real com Flask-SocketIO

Aplicação web de mensagens em tempo real desenvolvida com **Python, Flask e Flask-SocketIO**, permitindo a comunicação instantânea entre diferentes usuários conectados ao servidor.

O projeto utiliza eventos Socket.IO para enviar e distribuir mensagens sem a necessidade de atualizar a página.

## 🚀 Funcionalidades

- Envio e recebimento de mensagens em tempo real.
- Comunicação entre vários clientes conectados.
- Identificação das mensagens por nome.
- Interface web responsiva e simples.
- Indicador de conexão com o servidor.
- Reconexão automática após desconexões.
- Limite de caracteres para nomes e mensagens.
- Suporte para execução local e hospedagem na internet.

## 🛠️ Tecnologias utilizadas

- **Python** — lógica e execução do servidor.
- **Flask** — framework para aplicação web.
- **Flask-SocketIO** — comunicação em tempo real.
- **JavaScript** — interação com o servidor.
- **HTML5 e CSS3** — estrutura e interface.
- **Gunicorn** — servidor de aplicação para hospedagem.
- **simple-websocket** — suporte ao transporte WebSocket.

## 📂 Estrutura do projeto

```text
meu-chat-websocket/
├── app.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

## ⚙️ Requisitos

- Python 3.10 ou superior.
- Pip.
- Navegador atualizado.
- Conexão com a internet para carregar a biblioteca Socket.IO pelo CDN.

## 💻 Executando localmente

### 1. Clone o repositório

```bash
git clone https://github.com/LGustz/Chat-Py-Github.git
```

### 2. Acesse a pasta

```bash
cd meu-chat-websocket
```

### 3. Instale as dependências

```bash
py -m pip install -r requirements.txt
```

### 4. Inicie o servidor

```bash
py app.py
```

### 5. Acesse a aplicação

Abra o navegador e entre em:

```text
http://127.0.0.1:5000
```

Para testar a comunicação em tempo real, abra o endereço em duas abas ou navegadores diferentes.

## 🌐 Publicação no Render

A aplicação pode ser hospedada no Render utilizando o repositório do GitHub.

**Configurações de implantação:**

| Configuração | Valor |
|---|---|
| Language | Python 3 |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn --worker-class gthread --workers 1 --threads 100 app:app` |

### Variáveis de ambiente

Configure a seguinte variável no painel do Render:

| Variável | Descrição |
|---|---|
| `SECRET_KEY` | Chave secreta da aplicação |
| `PORT` | Porta fornecida automaticamente pelo ambiente, quando aplicável |

A variável `PORT` é lida pelo código Python na execução direta. No comando Gunicorn acima, o servidor utiliza a porta configurada pelo ambiente de hospedagem.

Após concluir a implantação, acesse a URL pública gerada pelo Render.

> **Observação:** o plano gratuito pode apresentar suspensão por inatividade, reinicializações e limitações de recursos. Consulte os planos e limites atuais do provedor.

## 🔄 Como funciona

1. O usuário informa seu nome e digita uma mensagem.
2. O JavaScript envia os dados ao servidor por meio do evento `mensagem`.
3. O Flask-SocketIO recebe os dados e verifica se o nome e a mensagem são válidos.
4. O servidor distribui a mensagem para os clientes conectados.
5. Os navegadores recebem o evento e atualizam a interface automaticamente.

### Fluxo de comunicação

```text
Navegador A
     |
     | socket.emit("mensagem")
     v
Servidor Flask-SocketIO
     |
     | socketio.emit("mensagem")
     v
Navegador A + Navegador B + outros clientes
```

## 📡 Eventos Socket.IO

| Evento | Função |
|---|---|
| `connect` | Detecta a conexão de um cliente |
| `disconnect` | Detecta a desconexão no navegador |
| `mensagem` | Recebe e distribui mensagens |

O servidor utiliza `socketio.emit()` para enviar as mensagens a todos os clientes conectados.

## ⚠️ Limitações conhecidas

- As mensagens não são armazenadas em banco de dados.
- Não existe histórico persistente.
- Não há autenticação ou cadastro de usuários.
- Os nomes são escolhidos livremente pelos participantes.
- Não há conversas privadas nem salas.
- O servidor precisa estar ativo para permitir a comunicação.

**Segurança:** esta versão é destinada a aprendizado e experimentação. Antes de disponibilizá-la para uso público, implemente autenticação, validação adicional, limitação de frequência de mensagens e proteção contra abuso. Configure HTTPS/WSS e uma `SECRET_KEY` forte, armazenada fora do código-fonte.

## 🔮 Melhorias futuras

- [ ] Sistema de cadastro e login.
- [ ] Histórico de mensagens com SQLite ou MySQL.
- [ ] Salas de conversa.
- [ ] Conversas privadas.
- [ ] Lista de usuários online.
- [ ] Indicador de digitação.
- [ ] Envio de imagens e arquivos.
- [ ] Interface aprimorada para dispositivos móveis.
- [ ] Notificações de mensagens.
- [ ] Controles de segurança e moderação.

## 🎯 Objetivo do projeto

Projeto educacional desenvolvido para aprender os fundamentos de comunicação em tempo real, programação backend com Python e integração entre navegadores e servidores por meio de Socket.IO.

