from typing import Any, List, Text, Dict
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionBookTicket(Action):
    def name(self) -> Text:
        return "action_book_ticket"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        category = tracker.get_slot('category')
        if category:
            # Implement your ticket booking logic here
            dispatcher.utter_message(text=f"Booking ticket for {category} category.")
            return []
        else:
            dispatcher.utter_message(text="Please provide a category to book the ticket.")
            return []

class ActionCancelTicket(Action):
    def name(self) -> Text:
        return "action_cancel_ticket"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Implement your ticket cancelation logic here
        dispatcher.utter_message(text="Canceling your ticket.")
        return []
