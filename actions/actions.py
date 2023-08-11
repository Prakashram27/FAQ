import requests
from bs4 import BeautifulSoup

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCases(Action):
    def name(self) -> Text:
        return "action_corona_cases"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        url = 'https://covid19.who.int/'  # Replace with the actual URL

        response = requests.get(url)
        content = response.content

        soup = BeautifulSoup(content, 'html.parser')

        # Find all span tags with class "sc-fznLxA"
        span_elements = soup.find_all('span', class_='sc-fznLxA')

        # Define the order of the extracted elements
        element_order = ['Globally', '1:56pm CEST, 2 August 2023', '768,983,095 confirmed cases', '6,953,743 deaths', '5 August 2023', '13,492,225,267 vaccine doses']

        # Initialize an empty dictionary to store the extracted elements
        extracted_elements = {}

        # Populate the dictionary with the extracted elements
        for i, span in enumerate(span_elements):
            extracted_elements[element_order[i]] = span.text

        # Construct the final output sentence
        final_output = (
            f"{extracted_elements['Globally']}, as of {extracted_elements['1:56pm CEST, 2 August 2023']}, there have been "
            f"{extracted_elements['768,983,095 confirmed cases']} of COVID-19, "
            f"including {extracted_elements['6,953,743 deaths']}, reported to WHO. As of "
            f"{extracted_elements['5 August 2023']}, a total of "
            f"{extracted_elements['13,492,225,267 vaccine doses']} have been administered."
        )

        print(final_output)
        dispatcher.utter_message(final_output)

        return []
    
class ActionSessionId(Action):
    def name(self) -> Text:
        return "action_session_id" 

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        conversation_id = tracker.sender_id
        
        # print("1>>>>>>>>>>>>>.",tracker.sender_id)
        # print("2>>>>>>>>>>>>>>>>",Tracker['sender_id'])

  
        dispatcher.utter_message(f"The session ID assigned to this conversation is: {conversation_id}")

        return []



# class ActionSaveConversation(Action):
#     def name(self) -> Text:
#         return "action_save_conversation"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         goodbye_intent = "goodbye"
        
#         # Initialize or retrieve the goodbye counter from tracker slots
#         goodbye_counter = tracker.get_slot("goodbye_counter") or 0
        
#         # Check if the latest user message's intent is a "goodbye" intent
#         if tracker.latest_message.get("intent", {}).get("name") == goodbye_intent:
#             goodbye_counter += 1
#         else:
#             goodbye_counter = max(0, goodbye_counter - 1)  # Decrement counter
            
#         # Update the counter in tracker slots
#         tracker.slots["goodbye_counter"] = goodbye_counter
        
#         # Check if the threshold is reached to save the conversation
#         save_threshold = 2  # Adjust as needed
#         if goodbye_counter >= save_threshold:
#             conversation_data = tracker.export_stories()
#             self.save_conversation(conversation_data)
#             goodbye_counter = 0  # Reset counter after saving
            
#         return []

#     def save_conversation(self, conversation_data: List[Dict[Text, Any]]) -> None:
#         # Specify the CSV file path
#         csv_file_path = "conversation_data.csv"
        
#         # Open the CSV file in append mode and write the conversation data
#         with open(csv_file_path, mode="a", newline="") as csv_file:
#             csv_writer = csv.DictWriter(csv_file, fieldnames=conversation_data[0].keys())
#             if csv_file.tell() == 0:  # Write header if the file is empty
#                 csv_writer.writeheader()
#             csv_writer.writerows(conversation_data)

# class ActionProvideInfoWithButtons(Action):
#     def name(self) -> Text:
#         return "action_provide_info_with_buttons"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         response = "Did this information help you?"
#         buttons = [
#             {"payload": "/affirm", "title": "Yes"},
#             {"payload": "/deny", "title": "No"}
#         ]
#         dispatcher.utter_message(text=response, buttons=buttons)
#         return []