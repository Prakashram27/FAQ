import requests

url = "http://192.168.0.115:5005//webhooks/rest/webhook"
data = {
    "sender": "user",
    "message": "Hello, chatbot!"
}

response = requests.post(url, json=data)
bot_responses = response.json()
for bot_response in bot_responses:
    print("Bot:", bot_response["text"])