from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = 'Token Telegram'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
chat_id = 'Chat_ID'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Received data: {data}")

    if 'Type' in data:
        if data['Type'] == 'queue.created' and 'Queues' in data and len(data['Queues']) > 0:
            queue = data['Queues'][0]
            queue_id = queue.get('Id', 'Unknown ID')
            queue_name = queue.get('Name', 'Unknown Name')
            queue_description = queue.get('Description', 'No description')

            message = f"Queue Created:\nID: {queue_id}\nName: {queue_name}\nDescription: {queue_description}"

        elif data['Type'] == 'queue.deleted' and 'Queues' in data and len(data['Queues']) > 0:
            queue = data['Queues'][0]
            queue_id = queue.get('Id', 'Unknown ID')
            queue_name = queue.get('Name', 'Unknown Name')
            queue_description = queue.get('Description', 'No description')

            message = f"Queue Deleted:\nID: {queue_id}\nName: {queue_name}\nDescription: {queue_description}"

        elif data['Type'] == 'queue.updated' and 'Queues' in data and len(data['Queues']) > 0:
            queue = data['Queues'][0]
            queue_id = queue.get('Id', 'Unknown ID')
            queue_name = queue.get('Name', 'Unknown Name')
            queue_description = queue.get('Description', 'No description')

            message = f"Queue Updated:\nID: {queue_id}\nName: {queue_name}\nDescription: {queue_description}"

        elif data['Type'] == 'queueItem.added' and 'Queue' in data and 'QueueItems' in data and len(data['QueueItems']) > 0:
            queue = data['Queue']
            queue_item = data['QueueItems'][0]
            queue_id = queue.get('Id', 'Unknown ID')
            queue_name = queue.get('Name', 'Unknown Name')
            queue_description = queue.get('Description', 'No description')
            item_id = queue_item.get('Id', 'Unknown Item ID')
            item_key = queue_item.get('Key', 'Unknown Key')
            item_status = queue_item.get('Status', 'Unknown Status')

            message = f"Queue Item Added:\nQueue ID: {queue_id}\nQueue Name: {queue_name}\nQueue Description: {queue_description}\nItem ID: {item_id}\nItem Key: {item_key}\nItem Status: {item_status}"

        else:
            return jsonify({"status": "error", "message": "Unsupported event type or missing data"}), 400

        
        
        payload = {
            'chat_id': chat_id,
            'text': message
        }
        response = requests.post(TELEGRAM_API_URL, params=payload)
        
        print(f"Telegram API response status_code: {response.status_code}")
        print(f"Telegram API response text: {response.text}")

        if response.status_code == 200:
            return jsonify({"status": "success", "message": "Mensagem enviada"}), 200
        else:
            return jsonify({"status": "error", "message": f"Erro ao enviar Mensagem: {response.text}"}), 500

    return jsonify({"status": "error", "message": "Não configurado"}), 400

if __name__ == '__main__':
    app.run(debug=True)
