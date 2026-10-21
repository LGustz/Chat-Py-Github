# 💬 Meu Chat WebSocket

Chat em tempo real desenvolvido com **Python, Flask e Flask-SocketIO**, permitindo que vários usuários conectados recebam mensagens instantaneamente, sem precisar atualizar a página.

O projeto foi criado com o objetivo de aprender os fundamentos da comunicação em tempo real entre clientes e servidores usando eventos e conexões persistentes.

## 🚀 Funcionalidades

- Envio e recebimento de mensagens em tempo real.
- Comunicação entre vários navegadores conectados.
- Identificação das mensagens pelo nome do usuário.
- Interface web simples e responsiva.
- Reconexão automática do cliente após desconexões.
- Limite de caracteres para nomes e mensagens.
- Execução local no próprio computador.
- Possibilidade de publicação em uma hospedagem compatível com Python.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Lógica e servidor da aplicação |
| Flask | Criação da aplicação web |
| Flask-SocketIO | Comunicação em tempo real |
| JavaScript | Envio e recebimento de mensagens |
| HTML5 | Estrutura da interface |
| CSS3 | Estilização da página |
| Gunicorn | Servidor de aplicação para publicação |

## 📁 Estrutura do projeto

```text
meu-chat-websocket/
├── app.py
├── requirements.txt
└── templates/
    └── index.html
```

## ⚙️ Requisitos

- Python 3.10 ou superior.
- Pip instalado.
- Navegador atualizado.
- Conexão com a internet para carregar a biblioteca Socket.IO pelo CDN utilizado na interface.

## 📥 Instalação

**1. Clone o repositório**

```bash
git clone https://github.com/SEU-USUARIO/meu-chat-websocket.git
```

Substitua `SEU-USUARIO` pelo seu nome de usuário do GitHub.

**2. Entre na pasta**

```bash
cd meu-chat-websocket
```

**3. Instale as dependências**

```bash
py -m pip install -r requirements.txt
```

**4. Execute o servidor**

```bash
py app.py
```

**5. Acesse a aplicação**

Abra o navegador e entre em:

```text
http://127.0.0.1:5000
```

## 🌐 Acesso por outros dispositivos

Para permitir que outros dispositivos da mesma rede local acessem o chat:

1. Execute `ipconfig` no PowerShell.
2. Localize o IPv4 do computador que está executando o servidor.
3. No outro dispositivo, abra `http://IP-DO-SERVIDOR:5000`.

Exemplo:

```text
http://192.168.1.100:5000
```

O endereço acima é apenas ilustrativo. Utilize o IP real do computador servidor.

O firewall do Windows precisa permitir conexões de entrada na porta TCP 5000 pela rede privada.

Para acesso externo pela internet, são necessárias configurações adicionais de rede e segurança.

## 🔄 Como funciona a comunicação

1. O usuário digita uma mensagem na interface.
2. O JavaScript envia os dados ao servidor por meio do evento `mensagem`.
3. O Flask-SocketIO recebe e valida os dados.
4. O servidor distribui a mensagem aos clientes conectados.
5. Os navegadores recebem o evento e atualizam a interface sem recarregar a página.

### Fluxo de comunicação

```text
Cliente A
   |
   | socket.emit("mensagem")
   v
Servidor Python
   |
   | socketio.emit("mensagem")
   v
Clientes conectados
```

## ⚠️ Limitações atuais

- As mensagens não são armazenadas em banco de dados.
- Não há cadastro, autenticação ou gerenciamento de usuários.
- Os nomes são informados livremente pelos participantes.
- As mensagens não possuem histórico persistente.
- O servidor precisa estar em execução para que o chat funcione.
- O acesso público exige configurações adicionais de segurança.

Esta versão é destinada ao aprendizado e a testes. Não deve ser exposta diretamente à internet sem medidas de proteção apropriadas.

## 🔮 Melhorias futuras

- [ ] Cadastro e login de usuários.
- [ ] Histórico de mensagens com SQLite ou MySQL.
- [ ] Conversas privadas.
- [ ] Salas de bate-papo.
- [ ] Lista de usuários online.
- [ ] Indicador de digitação.
- [ ] Envio de imagens e arquivos.
- [ ] Interface aprimorada para dispositivos móveis.
- [ ] Criptografia HTTPS/WSS e controles de segurança.
- [ ] Notificações de novas mensagens.

## 🎯 Objetivo educacional

Este projeto demonstra os fundamentos de aplicações web em tempo real e serve como ponto de partida para estudos de WebSockets, desenvolvimento backend, comunicação cliente-servidor e sistemas de mensagens.

## 📄 Licença

Este projeto pode ser disponibilizado sob a licença MIT. Para isso, adicione um arquivo `LICENSE` com o texto oficial da licença MIT.

---

Desenvolvido como projeto de estudo de **Python e comunicação em tempo real**.
