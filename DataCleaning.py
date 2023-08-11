import spacy
nlp = spacy.load("en_core_web_lg")
class FileCleaning:
    def __init__(self,filename):
        self.filename = filename
    
    def filtering(self):
        with open(self.filename) as f:
            lines = f.readlines()
        for line in range(0,len(lines)):
            lines[line] = lines[line].strip().strip("-")
        cancel = []
        changes = []
        current = ""
        for line in lines:
            if line=="CHANGES":
                current = "changes"
            elif line=="CANCELLATIONS":
                current = "cancel"
            if current == "changes":
                changes.append(line)
            elif current == "cancel":
                cancel.append(line)
            else:
                continue
        cancel = '\n'.join(cancel).replace('HR', 'HOURS')
        cancel = cancel.replace('HRS', "HOURS")
        changes = '\n'.join(changes).replace('HR', 'HOURS')
        changes = changes.replace('HRS', "HOURS")
        return [cancel,changes]
    
    def cancellation_split(self):
        file_rules = self.filtering()[0]
        rules = file_rules.split("\n\n")
        return rules
        
    def changes_split(self):
        file_rules = self.filtering()[1]
        rules = file_rules.split("\n\n")
        return rules
    
    def decision_making_cancellation(self):
        decision_1 = nlp("REFUNDABLE")
        decision_2 = nlp("NON REFUNDABLE")
        decision_rules = self.cancellation_split()
        result = nlp(str(decision_rules[0]))
        if decision_1.similarity(result) > decision_2.similarity(result):
            return 1
        else:
            return 0
                
    def decision_making_changes(self):
        decision_1 = nlp("CHANGES PERMITTED")
        decision_2 = nlp("CHNAGES NOT PERMITTED")
        decision_rules = self.changes_split()
        for rule in decision_rules:
            doc = nlp(str(rule))
            if decision_1.similarity(doc) < decision_2.similarity(doc):
                print(doc, " => ", "CHNAGES PERMITTED\n\n")
                
            else:
                print(doc, " => ", "NO CHNAGES PERMITTED\n\n")
                
        
            
# filerules = FileCleaning("DELBOM-AI-INR.txt")
# rules = filerules.changes_split()[0]
# print(rules)