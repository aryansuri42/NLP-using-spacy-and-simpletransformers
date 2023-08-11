import spacy
import os
# dir_path = r'C:\Users\ARYAN SURI\Desktop\Rules NLP'
# train = []
# res = []
# for file in os.listdir(dir_path):
#     if file.endswith('.txt'):
#         res.append(file)
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
                changes.append("")
            elif line=="CANCELLATIONS":
                current = "cancel"
                cancel.append("")
            if current == "changes":
                changes.append(line)
            elif current == "cancel":
                cancel.append(line)
            else:
                continue
        cancel = '\n'.join(cancel).replace('HR', 'HOURS')
        changes = '\n'.join(changes).replace('HR', 'HOURS')
        return [cancel,changes]
    
    def cancellation_split(self):
        file_rules = self.filtering()[0]
        rules = file_rules.split("\n\n")
        return rules
        
    def changes_split(self):
        file_rules = self.filtering()[1]
        rules = file_rules.split("\n\n")
        return rules
    
    def change_time_splits(self):
        file_rules = self.filtering()[1].split("\n")
        first_split = "ANY TIME"
        second_split = "AFTER DEPARTURE"
        third_split = "BEFORE DEPARTURE"
        anytime_split = []
        after_split = []
        before_split = []
        current = ""
        for line in file_rules:
            if line==first_split:
                current = first_split
            elif line==second_split:
                current = second_split
            elif line==third_split:
                current = third_split
            if current==first_split:
                anytime_split.append(line)
            elif current==second_split:
                after_split.append(line)
            elif current==third_split:
                before_split.append(line)
        anytime_rules = '\n'.join(anytime_split)
        after_rules = '\n'.join(after_split)
        before_rules = '\n'.join(before_split)    
        anytime_rules = anytime_rules.split('\n\n')
        after_rules = after_rules.split('\n\n')
        before_rules = before_rules.split('\n\n')
        return [anytime_rules, after_rules, before_rules]
    
    def cancellation_time_splits(self):
        file_rules = self.filtering()[0].split("\n")
        first_split = "ANY TIME"
        second_split = "AFTER DEPARTURE"
        third_split = "BEFORE DEPARTURE"
        anytime_split = []
        after_split = []
        before_split = []
        current = ""
        for line in file_rules:
            if line==first_split:
                current = first_split
            elif line==second_split:
                current = second_split
            elif line==third_split:
                current = third_split
            if current==first_split:
                anytime_split.append(line)
            elif current==second_split:
                after_split.append(line)
            elif current==third_split:
                before_split.append(line)
        anytime_rules = '\n'.join(anytime_split)
        after_rules = '\n'.join(after_split)
        before_rules = '\n'.join(before_split)
        anytime_rules = anytime_rules.split('\n\n')
        after_rules = after_rules.split('\n\n')
        before_rules = before_rules.split('\n\n')
        return [anytime_rules, after_rules, before_rules]
    
    # def decision_making_cancellation(self):
    #     decision_1 = nlp("REFUNDABLE")
    #     decision_2 = nlp("NON REFUNDABLE")
    #     decision_rules = self.cancellation_split()
    #     result = nlp(str(decision_rules[0]))
    #     if decision_1.similarity(result) > decision_2.similarity(result):
    #         return 1
    #     else:
    #         return 0
        
    # def decide_cancel(self, index):
    #     decision_1 = nlp("REFUNDABLE")
    #     decision_2 = nlp("NON REFUNDABLE")
    #     decision_rules = self.cancellation_split()
    #     result = nlp(str(decision_rules[index]))
    #     if decision_1.similarity(result) > decision_2.similarity(result):
    #         return 1
    #     else:
    #         return 0
    
    
    def timings(self):
        rules = self.change_time_splits()
        if rules[0] == [""] and rules[1] == [""] and rules[2] == [""]:
            finres = self.change_prices()
            return finres
        else:
            finres = self.change_time_prices()
            return finres
        
    def timings_cancel(self):
        rules = self.cancellation_time_splits()
        if rules[0] == [""] and rules[1] == [""] and rules[2] == [""]:
            finres = self.cancel_prices()
            return finres
        else:
            finres = self.cancel_time_prices()
            return finres
    
    
        
    def change_prices(self):
        set = self.cancellation_split()
        doc = nlp(set[0])
        ent = []
        for token in doc:
            if token.pos_=="NUM" and token.ent_type_=="TIME" and token.is_alpha==False:
                ent.append("hrs")
            if token.pos_=="NUM" and token.ent_type_!="TIME" and token.is_alpha==False:
                ent.append("money")
        if "hrs" in ent and "money" in ent:
            target = set[0]
            return target
        ent = []
        index = []
        string = []
        for rule in range(0,len(set)):
            for token in nlp(set[rule]):
                if token.pos_=="NUM" and token.ent_type_=="TIME" and token.is_alpha==False:
                    ent.append("hrs")
                if token.pos_=="NUM" and token.ent_type_!="TIME" and token.is_alpha==False:
                    ent.append("money")
                    
            if "hrs" in ent and "money" in ent:
                target = set[rule]
                return target
            ent = []
        return set[0]
        
                
    def change_time_prices(self):
        set = self.change_time_splits()
        depart_type = ["ANY TIME", "AFTER DEPARTURE", "BEFORE DEPARTURE"]
        count = 0
        rule_acc_time = []
        index = []
        ent = []
        string = []
        for rule in set:
            rules = rule #list (iterate the list into the rules thazt will be converted into a nlp string for tokenization)
            for times in range(0,len(rules)):
                for token in nlp(rules[times]):
                    if token.pos_=="NUM" and token.ent_type_!="TIME" and token.is_alpha==False:
                        ent.append("money")
                    
                if "money" in ent:
                    index.append(times)
                    ent = []
                    for i in index:
                        string.append(rules[i].strip())
                    target = '\n'.join(string).strip("")
                    string = []
                    rule_acc_time.append(target)
                    target = []
                    break
            if len(index)>0:
                index = []
            else:
                rule_acc_time.append("")
        return rule_acc_time
    
    def cancel_prices(self):
        set = self.cancellation_split()
        doc = nlp(set[0])
        ent = []
        for token in doc:
            if token.pos_=="NUM" and token.ent_type_=="TIME" and token.is_alpha==False:
                ent.append("hrs")
            if token.pos_=="NUM" and token.ent_type_!="TIME" and token.is_alpha==False:
                ent.append("money")
        if "hrs" in ent and "money" in ent:
            target = set[0]
            return target
        ent = []
        index = []
        string = []
        for rule in range(0,len(set)):
            for token in nlp(set[rule]):
                if token.pos_=="NUM" and token.ent_type_=="TIME" and token.is_alpha==False:
                    ent.append("hrs")
                if token.pos_=="NUM" and token.ent_type_!="TIME" and token.is_alpha==False:
                    ent.append("money")
                    
            if "hrs" in ent and "money" in ent:
                target = set[rule]
                return target
            ent = []
        return set[0]
        
                
    def cancel_time_prices(self):
        set = self.cancellation_time_splits()
        depart_type = ["ANY TIME", "AFTER DEPARTURE", "BEFORE DEPARTURE"]
        count = 0
        rule_acc_time = []
        index = []
        ent = []
        string = []
        for rule in set:
            rules = rule #list (iterate the list into the rules thazt will be converted into a nlp string for tokenization)
            for times in range(0,len(rules)):
                for token in nlp(rules[times]):
                    if token.pos_=="NUM" and token.ent_type_!="TIME" and token.is_alpha==False:
                        ent.append("money")
                    
                if "money" in ent:
                    index.append(times)
                    ent = []
                    for i in index:
                        string.append(rules[i].strip())
                    target = '\n'.join(string).strip("")
                    string = []
                    rule_acc_time.append(target)
                    target = []
                    break
            if len(index)>0:
                index = []
            else:
                rule_acc_time.append("")
        return rule_acc_time
    
                
# for i in res:
#     print(i)
#     print("---------------")
#     filerules = FileCleaning(i)
#     fin = filerules.timings_cancel()
#     if type(fin) == str:
#         print(fin)
#     else:
#         for i in fin:
#             print(i)
#     print('-----------------')