# Integração UiPath e Telegram

Este projeto fornece uma API que escuta eventos do UiPath e envia mensagens para um bot do Telegram com base nesses eventos. Ele é útil para notificar ou acionar ações automaticamente em resposta a eventos específicos gerados pelo UiPath Orchestrator.

## Visão Geral

A API expõe um endpoint que recebe notificações de eventos do UiPath Orchestrator e, com base no tipo de evento, envia uma mensagem para um bot do Telegram. Este sistema é projetado para funcionar com o UiPath Orchestrator e o Telegram Bot API.

## Recursos

- **Recepção de eventos do UiPath**: Escuta e processa notificações de eventos do UiPath Orchestrator.
- **Integração com Telegram**: Envia mensagens para um bot do Telegram com base em eventos recebidos.

## Requisitos

- Node.js (ou outro ambiente de execução para o código de backend)
- Conta no UiPath Orchestrator
- Conta no Telegram e criação de um bot
- [ngrok](https://ngrok.com/) para expor localmente o endpoint para a internet

## Documentação

- [Eventos do UiPath](https://docs.uipath.com/pt-BR/orchestrator/standalone/2023.10/user-guide/types-of-events#job-events): Detalhes sobre os tipos de eventos que podem ser recebidos do UiPath Orchestrator.
- [Telegram Bot API](https://core.telegram.org/bots/api): Documentação oficial da API do Telegram Bot.

## Configuração

1. **Criar um Bot no Telegram**

   - Acesse [BotFather](https://t.me/botfather) no Telegram e crie um novo bot.
   - Copie o token do bot fornecido.

2. **Configurar o UiPath Orchestrator**

   - Configure o UiPath Orchestrator para enviar eventos para o endpoint desta API.

3. **Instalação e Configuração**

   - Clone o repositório:

     ```bash
     git clone https://github.com/claytonoliver/Notifications_Uipath
     ```

   - Instale as dependências:

     ```bash
     npm install Flask
     npm install Requests
     ```

   - Substitua as variaveis com base nas suas informações

     ```env
     TELEGRAM_BOT_TOKEN = Token Telegram
     chat_id = 'Chat_ID'
     ```

   - Substitua `Token Telegram` pelo token do seu bot e `Chat_ID` pelo ID do chat do Telegram onde as mensagens serão enviadas.

4. **Executar o Servidor**

   - Inicie o servidor:

     ```bash
     npm start
     ```

5. **Configurar ngrok**

   - Baixe e instale o [ngrok](https://ngrok.com/).
   - Exponha a porta do seu servidor local (por exemplo, a porta 3000) usando ngrok. No terminal, execute:

     ```bash
     ngrok http 3000
     ```

   - O ngrok fornecerá uma URL pública que pode ser usada para acessar o seu servidor local. A URL terá a aparência de `https://abcdef1234.ngrok.io`.

6. **Atualizar Configuração do UiPath Orchestrator**

   - Adicione uma webhook no orchestrador para enviar eventos para a URL pública fornecida pelo ngrok, por exemplo:

     ```
     https://abcdef1234.ngrok.io/webhook
     ```

## Endpoints

- **POST /webhook**

  Recebe eventos do UiPath Orchestrator. O corpo da requisição deve ser um JSON conforme especificado pela documentação oficial do uipath.

  Exemplo de payload:

  ```json
  {
  "Type": "queue.created",
  "EventId": "d20b0839229443e8ab36c8fbb7cc8953",
  "Timestamp": "2018-11-26T14:31:14.4357176Z",
  "Queues": [
    {
      "Id": 40079,
      "Name": "new-queue-definition-name",
      "Description": "This the description of the queue.",
      "MaxNumberOfRetries": 3,
      "AcceptAutomaticallyRetry": true,
      "EnforceUniqueReference": true
      "SlaInMinutes": 1500,
      "RiskSlaInMinutes": 1140
    }
  ],
  "TenantId": 1,
  "UserId": 2
}
