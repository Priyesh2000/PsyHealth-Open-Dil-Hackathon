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

class EatForm(FormAction):


    def name(self):
         return "eat_form"
    @staticmethod
    def required_slots(tracker):
        return [
            "question_71",
            "question_72",
            "question_73",
            "question_74",
            "question_75",
            "question_76",
            "question_77",
            "question_78",
            "question_79",
            "question_80",
            "question_81",
            "question_82",
            "question_83",
            "question_84",
            "question_85"   
            ]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        
        question_71  = int(tracker.get_slot("question_71"))
        question_72 =  int(tracker.get_slot("question_72"))
        question_73  = int(tracker.get_slot("question_73"))
        question_74  = int(tracker.get_slot("question_74"))
        question_75  = int(tracker.get_slot("question_75"))
        question_76  = int(tracker.get_slot("question_76"))
        question_77  = int(tracker.get_slot("question_77"))
        question_78  = int(tracker.get_slot("question_78"))
        question_79  = int(tracker.get_slot("question_79"))
        question_80  = int(tracker.get_slot("question_80"))
        question_81  = int(tracker.get_slot("question_81"))
        question_82  = int(tracker.get_slot("question_82"))
        question_83  = int(tracker.get_slot("question_83"))
        question_84  = int(tracker.get_slot("question_84"))
        question_85  = int(tracker.get_slot("question_85"))
        
        sum9 = question_71+ question_72+ question_73+ question_74+ question_75+ question_76+ question_77+ question_78+ question_79+ question_80+ question_81+ question_82+ question_83+ question_84+ question_85  
        sum9 = int(sum9)
        if(sum9 < 16):
            message = "You do not possess traits of eating disorder. Although if you continue facing the problems kindly visit a doctor. Caution: These results are not to be trusted fully."
            dispatcher.utter_message(message)
        elif(sum9 >= 16 and sum9 < 30):
            message = "You do possess moderate traits of eating disorder. You should see a psychologist or counsellor.  Caution: These results are not to be trusted fully."
            dispatcher.utter_message(message)
        elif(sum9 >= 30):
            message = "You possess high traits of eating disorder. You should see a psychologist or counsellor on immediate basis.  Caution: These results are not to be trusted fully."
            dispatcher.utter_message(message)
        return [AllSlotsReset()]

class SleepForm(FormAction):


    def name(self):
         return "sleep_form"
    @staticmethod
    def required_slots(tracker):
        return [
            "question_86",
            "question_87",
            "question_88",
            "question_89",
            "question_90",
            "question_91",
            "question_92",
            "question_93",
            "question_94",
            "question_95",
            "question_96",
            "question_97",
            "question_98",
            "question_99",
            "question_100",
            "question_101",
            "question_102",
            "question_103",
            "question_104",
            "question_105",
            "question_106",
            "question_107",
            "question_108",
            "question_109",
            "question_110",
            "question_111",
            "question_112",
            "question_113",
            "question_114",
            "question_115",
            "question_116",
            "question_117",
            "question_118",
            "question_119"
            ]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        
        question_86   = int(tracker.get_slot("question_86"))
        question_87   = int(tracker.get_slot("question_87"))
        question_88   = int(tracker.get_slot("question_88"))
        question_89   = int(tracker.get_slot("question_89"))
        question_90   = int(tracker.get_slot("question_90"))
        question_91   = int(tracker.get_slot("question_91"))
        question_92   = int(tracker.get_slot("question_92"))
        question_93   = int(tracker.get_slot("question_93"))
        question_94   = int(tracker.get_slot("question_94"))
        question_95   = int(tracker.get_slot("question_95"))
        question_96   = int(tracker.get_slot("question_96"))
        question_97   = int(tracker.get_slot("question_97"))
        
        question_98   = int(tracker.get_slot("question_98"))
        question_99   = int(tracker.get_slot("question_99"))
        question_100  = int(tracker.get_slot("question_100"))
        question_101  = int(tracker.get_slot("question_101"))
        question_102  = int(tracker.get_slot("question_102"))
        question_103  = int(tracker.get_slot("question_103"))
        question_104  = int(tracker.get_slot("question_104"))
        
        question_105  = int(tracker.get_slot("question_105"))
        question_106  = int(tracker.get_slot("question_106"))
        question_107  = int(tracker.get_slot("question_107"))
        question_108  = int(tracker.get_slot("question_108"))
        question_109  = int(tracker.get_slot("question_109"))
        question_110  = int(tracker.get_slot("question_110"))
        question_111  = int(tracker.get_slot("question_111"))
        question_112  = int(tracker.get_slot("question_112"))
        
        question_113  = int(tracker.get_slot("question_113"))
        question_114  = int(tracker.get_slot("question_114"))
        question_115  = int(tracker.get_slot("question_115"))
        question_116  = int(tracker.get_slot("question_116"))
        question_117  = int(tracker.get_slot("question_117"))
        question_118  = int(tracker.get_slot("question_118"))
        question_119  = int(tracker.get_slot("question_119"))
        
        sum3 = question_86+ question_87+ question_88+ question_89+ question_90+ question_91+ question_92+ question_93+ question_94+ question_95+ question_96+ question_97 
        sum4 = question_98+ question_99+ question_100+ question_101+ question_102+ question_103+ question_104 
        sum5 = question_105+ question_106+ question_107+ question_108+ question_109+ question_110+ question_111+ question_112
        sum6 = + question_113+ + question_114+ question_115+ question_116+ question_117+ question_118+ question_119
        sum3 = int(sum3)
        sum4 = int(sum4)
        sum5 = int(sum5)
        sum6 = int(sum6)
        sum7 = sum3+sum4+sum5+sum6
        if(sum3 > 3):
            message = "You do possess traits of sleep apnea. You should see a psychologist or counsellor.  Caution: These results are not to be trusted fully.."
            dispatcher.utter_message(message)
        if(sum4 > 3):
            message = "You do possess traits of insomnia. You should see a psychologist or counsellor.  Caution: These results are not to be trusted fully.."
            dispatcher.utter_message(message)
        if(sum5 > 3):
            message = "You possess traits of narcolepsy. You should see a psychologist or counsellor.  Caution: These results are not to be trusted fully.."
            dispatcher.utter_message(message)
        if(sum6 > 3):
            message = "You possess traits of restless leg syndrome. You should see a psychologist or counsellor.  Caution: These results are not to be trusted fully.."
            dispatcher.utter_message(message)
        elif(sum7 < 10):
            message = "You do not possess traits of sleeping disorders. Although if you continue facing the problems kindly visit a doctor.  Caution: These results are not to be trusted fully.."
            dispatcher.utter_message(message)
        elif(sum7 > 10):
            message = "You do possess traits of sleeping disorders. You should see a psychologist or counsellor.  Caution: These results are not to be trusted fully.."
            dispatcher.utter_message(message)


        return [AllSlotsReset()]

