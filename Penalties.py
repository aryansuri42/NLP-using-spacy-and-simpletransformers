import csv
import pandas as pd
import uuid

# with open("Penalties.csv",'w',newline='') as f:
#     header = ['PENALTY ID', 'ID', 'RULES','AFTER HOURS', 'BEFORE HOURS', 'CASE', 'SUB CASE', 'PENALTIES']
#     writer = csv.writer(f)
#     writer.writerow(header)


class Penalties:
    
    def __init__(self, uid, rules, after_hours, before_hours, case, sub_case):
        self.penalty_id = uuid.uuid4()
        self.uid = uid
        self.rules = rules
        self.after_hours = after_hours
        self.before_hours = before_hours
        self.case = case
        self.sub_case = sub_case
        self.penalty = 0
    def updatefile(self):
        row = [self.penalty_id,self.uid,self.rules,self.after_hours,self.before_hours,self.case,self.sub_case,self.penalty]
        with open("Penalties.csv",'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(row)
            
    def penaltyamount(self, price=0):
        df = pd.read_csv("Penalties.csv", index_col="ID")
        df.loc[self.penalty_id, 'PENALTIES'] += price
        df.to_csv("Fare.csv", index_label="ID")
        print("File Updated")
        