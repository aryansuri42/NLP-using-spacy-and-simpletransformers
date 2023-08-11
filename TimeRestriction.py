import spacy
from DataCleaning import * 
from QueryTesting import *
from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_lg")

class HourCalc:
    
    def __init__(self, after_hours, before_hours, rules):
        self.after_hours = after_hours
        self.before_hours = before_hours
        self.rules = rules
        
        
    def change_hours(self, query_index):
        files_rules = FileCleaning(self.rules)
        changes = files_rules.changes_split()
        price = 0
        hours = 0
        if self.before_hours==0:
            price = 0
            query = QueryMatch('NO SHOW', self.rules)
            query_index = query.changematch()
            for sentence in range(query_index,-1,-1):
                doc_sent = nlp(str(changes[sentence]))
                for token in range(0,len(doc_sent)):
                    if doc_sent[token].pos_=='NUM' and doc_sent[token].is_alpha==False:
                        price = doc_sent[token].text
                        return(float(price))
        else:
            for sentence in range(query_index,-1,-1):
                doc_sent = nlp(str(changes[sentence]))
                for token in range(0,len(doc_sent)):
                    if doc_sent[token].ent_type_=='TIME' and doc_sent[token].pos_=="NUM" and doc_sent[token].text!='24':
                        hours = doc_sent[token].text
                        break
                if hours!=0:
                    break
            if self.after_hours <= 24 and self.before_hours>=168:
                price = 0
                return price
            if self.before_hours >= int(hours):
                for token in range(token-1, -1, -1):
                    if doc_sent[token].pos_=="NUM":
                        price = doc_sent[token].text
            else:
                for token in range(token+1, len(doc_sent)):
                    if doc_sent[token].pos_=="NUM":
                        price = doc_sent[token].text
            print(price)
            return float(price)
        
        
    def cancel_hours(self, query_index=0):
        files_rules = FileCleaning(self.rules)
        changes = files_rules.cancellation_split()
        price = 0
        hours = 0
        if self.before_hours==0:
            price = 0
            query = QueryMatch('NO SHOW', self.rules)
            query_index = query.cancelmatch()[1]
            for sentence in range(query_index,-1,-1):
                doc_sent = nlp(str(changes[sentence]))
                for token in range(0,len(doc_sent)):
                    if doc_sent[token].pos_=='NUM' and doc_sent[token].is_alpha==False:
                        price = doc_sent[token].text
                        return(float(price))
        else:
            for sentence in range(query_index,-1,-1):
                doc_sent = nlp(str(changes[sentence]))
                for token in range(0,len(doc_sent)):
                    if doc_sent[token].ent_type_=='TIME' and doc_sent[token].pos_=="NUM" and doc_sent[token].text!='24':
                        hours = doc_sent[token].text
                        break
                if hours!=0:
                    break
            if self.after_hours <= 24 and self.before_hours>=168:
                price = 0
                return price
            if self.before_hours >= int(hours):
                for token in range(token-1, -1, -1):
                    if doc_sent[token].pos_=="NUM":
                        price = doc_sent[token].text
            else:
                for token in range(token+1, len(doc_sent)):
                    if doc_sent[token].pos_=="NUM":
                        price = doc_sent[token].text
            print(price)
            return float(price)