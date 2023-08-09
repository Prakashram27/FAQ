# from flask import Flask, render_template, request
# import speech_recognition as sr
# import requests
# import pyttsx3

# app = Flask(__name__)

# def recognize_speech():
#     recognizer = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Say something...")
#         audio = recognizer.listen(source)

#     try:
#         recognized_text = recognizer.recognize_google(audio, language='en')
#         print("You said:", recognized_text)
#         return recognized_text
#     except sr.UnknownValueError:
#         print("Sorry, I could not understand what you said.")
#     except sr.RequestError as e:
#         print("Error fetching results:", e)

# def send_text_to_rasa(user_text):
#     url = "http://192.168.0.111:5005/webhooks/rest/webhook"  # Replace with your Rasa server URL
#     data = {
#         "sender": "user",
#         "message": user_text
#     }
#     response = requests.post(url, json=data)
#     print(response.json())
#     return response.json()

# def text_to_speech(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()
# @app.route("/hello")
# def testRoute():
#     return "world"

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     print(request.json['text'])
#     # return "haha"
#     user_input = request.json['text']
#     if user_input:
#         rasa_response = send_text_to_rasa(user_input)
#         if rasa_response and len(rasa_response) > 0:
#             bot_responses = []
#             for i in rasa_response:
#                 bot_message = i['text']
#                 bot_responses.append(bot_message)
#                 text_to_speech(bot_message)
#             return {'bot_responses': bot_responses}
#     return {'bot_responses': []}

# if __name__ == '__main__':
#     app.run(host='192.168.0.111', port=5000,debug=True)



from flask import Flask, render_template, request, jsonify
import os,sys,requests, json
from random import randint
app = Flask(__name__)
@app.route('/')
def home():
  return render_template('index.html')
@app.route('/parse',methods=['POST', 'GET'] )
def extract():
  text=str(request.form.get('value1'))
  payload = json.dumps({"sender": "Rasa","message": text})
  headers = {'Content-type': 'application/json'}
  response = requests.request("POST",   url="http://localhost:5005/webhooks/rest/webhook", headers=headers, data=payload)
  response=response.json()
  resp=[]
  for i in range(len(response)):
    try:
      resp.append(response[i]['text'])
    except:
      continue
  result=resp
  print(result)
  return result
if __name__ == "__main__":
  app.run(debug=True)