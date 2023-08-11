from DataCleaning import * 
from QueryTesting import *
import pandas as pd
import uuid
import csv

# with open("Fare.csv",'w',newline='') as f:
#     header = ['ID', 'RULES', 'BASE', 'TAX', 'FUEL CHARGE', 'AIRPORT CHARGES', 'CANCELLATION CHARGES', 'EXTRA CHARGES','NO OF CHANGES', 'TOTAL']
#     writer = csv.writer(f)
#     writer.writerow(header)
    

class FindTicket:
    def __init__(self, uid):
        self.uid = uid
        
    def ticketbaseprice(self):
        df = pd.read_csv("Fare.csv", index_col="ID")
        return df.loc[self.uid, "BASE"]
                
    def extraprice(self):
        df = pd.read_csv("Fare.csv", index_col="ID")
        return df.loc[self.uid, "EXTRA CHARGES"]
                
                
class FlightTicket:
    
    def __init__(self, rules, base_fare, taxes,fuel_surcharge, airport_charges):
        self.base_fare = base_fare
        self.taxes = taxes
        self.uid = uuid.uuid4()
        self.rules = rules
        self.fuel_surcharge = fuel_surcharge
        self.airport_charges = airport_charges
        self.cancellation = 0
        self.extra = 0
        self.no_changes = 0
        
    def dumpticket(self):
        list_content = [self.uid, self.rules, self.base_fare, self.taxes, self.fuel_surcharge, self.airport_charges,self.cancellation, self.extra, self.no_changes]
        with open("Fare.csv",'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(list_content)
        df = pd.read_csv("Fare.csv")
        df['TOTAL'] = df['BASE'] + df['TAX'] + df['AIRPORT CHARGES'] + df['EXTRA CHARGES']
        df.to_csv("Fare.csv", index = False)
        
        
class UpdatePrices:
    def __init__(self, uid, charges):
        self.uid = uid
        self.charges = charges
        
    def extra(self):
        df = pd.read_csv("Fare.csv", index_col="ID")
        df.loc[self.uid, 'EXTRA CHARGES'] = self.charges
        df['TOTAL'] = df['BASE'] + df['TAX'] + df['EXTRA CHARGES']
        df.loc[self.uid, 'NO OF CHANGES'] += 1
        df.to_csv("Fare.csv", index_label="ID")
        print("File Updated")
        
    def country_refundable(self):
        df = pd.read_csv("Fare.csv", index_col="ID")
        refundable = df['FUEL CHARGE'] + df['TAX'] - self.charges
        if refundable<=0:
            df.loc[self.uid, 'REFUNDABLE'] = 0
        else:
            df.loc[self.uid, 'REFUNDABLE'] = refundable
        df.loc[self.uid, 'CANCELLATION CHARGES'] = self.charges
        df.to_csv("Fare.csv", index_label="ID")
        print("File Updated")
        
    def regular_refund(self):
        df = pd.read_csv("Fare.csv", index_col="ID")
        refundable = df.loc[self.uid, 'TOTAL'] - self.charges
        if refundable<=0:
            df.loc[self.uid, 'REFUNDABLE'] = 0
        else:
            df.loc[self.uid, 'REFUNDABLE'] = refundable
        df.loc[self.uid, 'CANCELLATION CHARGES'] = self.charges
        df.to_csv("Fare.csv", index_label="ID")
        print("File Updated")
        
    def noshow(self):
        df = pd.read_csv("Fare.csv", index_col="ID")
        refundable = df.loc[self.uid, 'TAX'] - self.charges
        if refundable<=0:
            df.loc[self.uid, 'REFUNDABLE'] = 0
            df.loc[self.uid, 'REFUNDABLE'] = refundable
        else:
            df.loc[self.uid, 'REFUNDABLE'] = refundable
        df.loc[self.uid, 'CANCELLATION CHARGES'] = self.charges
        df.to_csv("Fare.csv", index_label="ID")
        print("File Updated")
        
    def fullrefund(self):
        df = pd.read_csv("Fare.csv", index_col="ID")
        df.loc[self.uid, 'REFUNDABLE'] = df.loc[self.uid, 'TOTAL']
        df.to_csv("Fare.csv", index_label="ID")
        print("File Updated")

# ticket = FlightTicket(rules="UK-CORP-RULE.txt", base_fare=12000, taxes=3000,fuel_surcharge=1000, airport_charges=800)
# ticket.dumpticket()
# myticket=FindTicket("bb667c61-e76f-40d1-832f-b6aa91ce01e3")
# myticket.ticketbaseprice()