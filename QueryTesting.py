import spacy
from DataCleaning import *

nlp = spacy.load("en_core_web_lg")
class QueryMatch:
    def __init__(self,query, filename):
        self.filename = filename
        self.query = query
        
    def cancelmatch(self):
        rules = FileCleaning(self.filename)
        cancels = rules.cancellation_split()
        doc_query = nlp(self.query)
        count_similarity = 0
        max_similarity = 0
        
        for line in range(0,len(cancels)):
            doc2 = nlp(str(cancels[line]))
            if doc_query.similarity(doc2) > max_similarity:
                max_similarity = doc2.similarity(doc_query)
                count_similarity = line
            else:
                continue
        doc_sim = nlp(str(doc[count_similarity]))   
        doc_check1 = nlp('REFUND PERMITTED')
        doc_check2 = nlp('REFUND NOT PERMITTED')
        doc_check3 = nlp('FULL REFUND')
        
        check1 = doc_check1.similarity(doc_sim)
        check2 = doc_check2.similarity(doc_sim)
        check3 = doc_check3.similarity(doc_sim)
        
        maximum = max(check1, check2, check3)
        if check1==maximum:
            return [1, count_similarity]
        elif check2==maximum:
            return [0, count_similarity]
        elif check3==maximum:
            return [2, count_similarity]
        
        
    def changematch(self):
        rules = FileCleaning(self.filename)
        changes = rules.changes_split()
        doc_query = nlp(self.query)
        count_similarity = 0
        max_similarity = 0
        for line in range(0,len(changes)):
            doc2 = nlp(str(changes[line]))
            if doc_query.similarity(doc2) > max_similarity:
                max_similarity = doc2.similarity(doc_query)
                count_similarity = line
            else:
                continue
        return count_similarity
        
# query = QueryMatch('TICKET FORFEIT', "YYZCOK-RULE.txt")
# print(query.country_cancellelation("NORWAY"))