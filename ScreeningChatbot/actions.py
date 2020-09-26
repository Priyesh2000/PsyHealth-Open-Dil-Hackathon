from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.forms import FormAction
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.events import AllSlotsReset, SlotSet
import pandas as pd
from rasa.core.slots import Slot
import json

class DepressionForm(FormAction):

   

    def name(self):
        return "depression_form"
    @staticmethod
    def required_slots(tracker):
        return [
            "question_0",
            "question_1",
            "question_2",
            "question_3",
            "question_4",
            "question_5",
            "question_6",
            "question_7",
            "question_8",
            "question_9",
            "question_10",
            "question_11",
            "question_12",
            ]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        
        question_0   = int(tracker.get_slot("question_0"))
        question_1   = int(tracker.get_slot("question_1"))
        question_2   = int(tracker.get_slot("question_2"))
        question_3   = int(tracker.get_slot("question_3"))
        question_4   = int(tracker.get_slot("question_4"))
        question_5   = int(tracker.get_slot("question_5"))
        question_6   = int(tracker.get_slot("question_6"))
        question_7   = int(tracker.get_slot("question_7"))
        question_8   = int(tracker.get_slot("question_8"))
        question_9   = int(tracker.get_slot("question_9"))
        question_10  = int(tracker.get_slot("question_10"))
        question_11  = int(tracker.get_slot("question_11"))
        question_12  = int(tracker.get_slot("question_12"))
        sum0 = question_0 + question_1+ question_2+ question_3+ question_4+ question_5+ question_6+ question_7+ question_8+ question_9+ question_10+ question_11+ question_12
        sum0 = int(sum0)
        print(sum0)
        if(sum0 < 13):
            message = "You do not possess traits of depression or anxiety. Although if you continue facing the problems kindly visit a doctor.  Caution: These results are not to be trusted fully.."
            dispatcher.utter_message(message)
        elif(sum0 >= 13 and sum0 < 26):
            message = "You do possess moderate traits of depression and anxiety. You should see a psychologist or counsellor.  Caution: These results are not to be trusted fully.."
            dispatcher.utter_message(message)
        elif(sum0 >= 26):
            message = "You possess high traits of depression and anxiety. You should see a psychologist or counsellor on immediate basis.  Caution: These results are not to be trusted fully.."
            dispatcher.utter_message(message)
        return [AllSlotsReset()]

class TraumaForm(FormAction):


    def name(self):
         return "trauma_form"
    @staticmethod
    def required_slots(tracker):
        return [
            "question_13",
            "question_14",
            "question_15",
            "question_16",
            "question_17",
            "question_18",
            "question_19",
            "question_20",
            "question_21",
            "question_22"    
            ]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        
        question_13  = int(tracker.get_slot("question_13"))
        question_14 =  int(tracker.get_slot("question_14"))
        question_15  = int(tracker.get_slot("question_15"))
        question_16  = int(tracker.get_slot("question_16"))
        question_17  = int(tracker.get_slot("question_17"))
        question_18  = int(tracker.get_slot("question_18"))
        question_19  = int(tracker.get_slot("question_19"))
        question_20  = int(tracker.get_slot("question_20"))
        question_21  = int(tracker.get_slot("question_21"))
        question_22  = int(tracker.get_slot("question_22"))
        
        sum1 = question_13+ question_14+ question_15+ question_16+ question_17+ question_18+ question_19+ question_20+ question_21+ question_22
        sum1 = int(sum1)
        if(sum1 < 3):
            message = "You do not possess traits of trauma. Although if you continue facing the problems kindly visit a doctor.  Caution: These results are not to be trusted fully.."
            dispatcher.utter_message(message)
        elif(sum1 >= 3 and sum1 < 6):
            message = "You do possess moderate traits of trauma. You should see a psychologist or counsellor.  Caution: These results are not to be trusted fully.."
            dispatcher.utter_message(message)
        elif(sum1 >= 6):
            message = "You possess high traits of trauma. You should see a psychologist or counsellor on immediate basis.  Caution: These results are not to be trusted fully.."
            dispatcher.utter_message(message)
        return [AllSlotsReset()]
