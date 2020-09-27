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

class DrugForm(FormAction):


    def name(self):
         return "drug_form"
    @staticmethod
    def required_slots(tracker):
        return [
            "question_23",
            "question_24",
            "question_25",
            "question_26",
            "question_27",
            "question_28",
            "question_29",
            "question_30",
            "question_31",
            "question_32",
            "question_33",
            "question_34",
            "question_35",
            "question_36",
            "question_37",
            "question_38",
            "question_39",
            "question_40",
            "question_41",
            "question_42",
            "question_43",
            "question_44",
            "question_45",
            "question_46",
            "question_47",
            "question_48",
            "question_49",
            "question_50"
            ]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        
        question_23  = int(tracker.get_slot("question_23"))
        question_24 =  int(tracker.get_slot("question_24"))
        question_25  = int(tracker.get_slot("question_25"))
        question_26  = int(tracker.get_slot("question_26"))
        question_27  = int(tracker.get_slot("question_27"))
        question_28  = int(tracker.get_slot("question_28"))
        question_29  = int(tracker.get_slot("question_29"))
        question_30  = int(tracker.get_slot("question_30"))
        question_31  = int(tracker.get_slot("question_31"))
        question_32  = int(tracker.get_slot("question_32"))
        question_33  = int(tracker.get_slot("question_33"))
        question_34 =  int(tracker.get_slot("question_34"))
        question_35  = int(tracker.get_slot("question_35"))
        question_36  = int(tracker.get_slot("question_36"))
        question_37  = int(tracker.get_slot("question_37"))
        question_38  = int(tracker.get_slot("question_38"))
        question_39  = int(tracker.get_slot("question_39"))
        question_40  = int(tracker.get_slot("question_40"))
        question_41  = int(tracker.get_slot("question_41"))
        question_42  = int(tracker.get_slot("question_42"))
        question_43  = int(tracker.get_slot("question_43"))
        question_44  = int(tracker.get_slot("question_44"))
        question_45  = int(tracker.get_slot("question_45"))
        question_46  = int(tracker.get_slot("question_46"))
        question_47  = int(tracker.get_slot("question_47"))
        question_48  = int(tracker.get_slot("question_48"))
        question_49  = int(tracker.get_slot("question_49"))
        question_50  = int(tracker.get_slot("question_50"))
        
        sum2 = question_23+ question_24+ question_25+ question_26+ question_27+ question_28+ question_29+ question_30+ question_31+ question_32+ question_33+ question_34+ question_35+ question_36+ question_37+ question_38+ question_39+ question_40+ question_41+ question_42+ question_43+ question_44+ question_45+ question_46+ question_47+ question_48+ question_49+ question_50
        sum2 = int(sum2)
        if(sum2 < 6):
            message = "You do not possess traits of drug addiction. Although if you continue facing the problems kindly visit a doctor.  Caution: These results are not to be trusted fully.."
            dispatcher.utter_message(message)
        elif(sum2 >= 6 and sum2 < 12):
            message = "You do possess moderate traits of drug addiction. You should see a psychologist or counsellor.  Caution: These results are not to be trusted fully.."
            dispatcher.utter_message(message)
        elif(sum2 >= 12):
            message = "You possess high traits of drug addiction. You should see a psychologist or counsellor on immediate basis.  Caution: These results are not to be trusted fully.."
            dispatcher.utter_message(message)
        return [AllSlotsReset()]

class OCDForm(FormAction):


    def name(self):
         return "OCD_form"
    @staticmethod
    def required_slots(tracker):
        return [
            "question_51",
            "question_52",
            "question_53",
            "question_54",
            "question_55",
            "question_56",
            "question_57",
            "question_58",
            "question_59",
            "question_60",
            "question_61",
            "question_62",
            "question_63",
            "question_64",
            "question_65",
            "question_66",
            "question_67",
            "question_68",
            "question_69",
            "question_70"      
            ]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        
        question_51  = int(tracker.get_slot("question_51"))
        question_52 =  int(tracker.get_slot("question_52"))
        question_53  = int(tracker.get_slot("question_53"))
        question_54  = int(tracker.get_slot("question_54"))
        question_55  = int(tracker.get_slot("question_55"))
        question_56  = int(tracker.get_slot("question_56"))
        question_57  = int(tracker.get_slot("question_57"))
        question_58  = int(tracker.get_slot("question_58"))
        question_59  = int(tracker.get_slot("question_59"))
        question_60  = int(tracker.get_slot("question_60"))
        question_61  = int(tracker.get_slot("question_61"))
        question_62  = int(tracker.get_slot("question_62"))
        question_63  = int(tracker.get_slot("question_63"))
        question_64  = int(tracker.get_slot("question_64"))
        question_65  = int(tracker.get_slot("question_65"))
        question_66  = int(tracker.get_slot("question_66"))
        question_67  = int(tracker.get_slot("question_67"))
        question_68  = int(tracker.get_slot("question_68"))
        question_69  = int(tracker.get_slot("question_69"))
        question_70  = int(tracker.get_slot("question_70"))

        
        sum8 = question_51+ question_52+ question_53+ question_54+ question_55+ question_56+ question_57+ question_58+ question_59+ question_60+ question_61+ question_62+ question_63+ question_64+ question_65+ question_66+ question_67+ question_68+ question_69+ question_70
        sum8 = int(sum8)
        if(sum8 <= 5):
            message = "You do not possess traits of obsessive compulsive disorder. Although if you continue facing the problems kindly visit a doctor.  Caution: These results are not to be trusted fully."
            dispatcher.utter_message(message)
        elif(sum8 >= 6 and sum8 < 10):
            message = "You do possess moderate traits of obsessive compulsive disorder. You should see a psychologist or counsellor.  Caution: These results are not to be trusted fully."
            dispatcher.utter_message(message)
        elif(sum8 >= 10):
            message = "You possess high traits of obsessive compulsive disorder. You should see a psychologist or counsellor on immediate basis.  Caution: These results are not to be trusted fully."
            dispatcher.utter_message(message)
        return [AllSlotsReset()]