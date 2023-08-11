import spacy
from DataCleaning import * 

nlp = spacy.load("en_core_web_lg")

class PreSale:
    
    def __init__(self, filename):
        self.filename = filename
        
    def cancellation_presale(self):
        file_rules = FileCleaning(self.filename)
        cancel = nlp(str(file_rules.cancellation_split()[0]))
        price = 0
        hours = 0
        hours_list = []
        prices_list = []
        prices = []
        no_change_index = []
        when_index = []
        no_charge_exist = 1               
        for token in range(0, len(cancel)):
            if cancel[token].pos_=="NUM" and cancel[token].ent_type_!="TIME" and cancel[token].is_alpha==False and cancel[token].text not in hours_list and cancel[token].text not in prices_list:
                price = cancel[token].text
                for index in range(token+1, len(cancel)):                    
                    if cancel[index].pos_=="NUM" and cancel[index].ent_type_=="TIME" and cancel[index].is_alpha==False and cancel[index].text not in hours_list :
                        hours = cancel[index].text
                        for no_charge_index in range(index-1, -1, -1):
                            if no_charge_index not in no_change_index and cancel[no_charge_index].text=='CHARGE' and cancel[no_charge_index-1].text=='NO':
                                print(hours, " NO CHARGES")
                                no_change_index.append(no_charge_index)
                                hours_list.append(hours)
                                hours = 0
                                break                                                                                            
                            elif no_charge_index not in when_index and cancel[no_charge_index].text=='WHEN':
                                for amp in range(no_charge_index+1, len(cancel)):
                                    if cancel[amp].pos_=="NUM" and cancel[amp].ent_type_!="TIME" and cancel[amp].is_alpha==False and cancel[amp].text not in hours_list and cancel[amp].text not in prices_list:
                                        newprice = cancel[amp].text
                                        when_index.append(no_charge_index)
                                        hours_list.append(hours)
                                        prices_list.append(newprice)
                                        print(hours, " ", newprice)
                                        break
                                for i in range(no_charge_index+1, len(cancel)):
                                    if cancel[i].pos_=="NUM" and cancel[i].ent_type_=="TIME" and cancel[i].is_alpha==False and cancel[i].text not in hours_list :
                                        hours = cancel[i].text
                                        hours_list.append(hours)
                                        prices_list.append(price)
                                        print(hours, " ", price) 
                                        hours = 0
                                        break                            
                            no_charge_exist = 0                                                                                                                    
                        if no_charge_exist==0 and cancel[index].text not in hours_list:
                            hours_list.append(hours)            
                            prices_list.append(price)
                            print(hours, " ", price)
                            hours = 0
                            price = 0
                            break                        
                if hours==0 and price!=0:
                    hours_list.append(hours)            
                    prices_list.append(price)
                    print(hours, " ", price)
                    hours = 0                                  
        print(hours_list, prices_list)
                
        
    
    
    def new_cancel_presale(self):
        file_rules = FileCleaning(self.filename)
        change = nlp(str(file_rules.changes_split()[0]))
        price = 0
        hours = 0
        hours_list = []
        prices_list = []
        prices = []
        no_change_index = []
        when_index = []
        no_charge_exist = 1               
        for token in range(0, len(change)):
            if change[token].pos_=="NUM" and change[token].ent_type_!="TIME" and change[token].is_alpha==False and change[token].text not in hours_list and change[token].text not in prices_list:
                price = change[token].text
                for index in range(token+1, len(change)):                    
                    if change[index].pos_=="NUM" and change[index].ent_type_=="TIME" and change[index].is_alpha==False and change[index].text not in hours_list :
                        hours = change[index].text
                        for no_charge_index in range(index-1, -1, -1):
                            if no_charge_index not in no_change_index and change[no_charge_index].text=='CHARGE' and change[no_charge_index-1].text=='NO':
                                print(hours, " NO CHARGES")
                                no_change_index.append(no_charge_index)
                                hours_list.append(hours)
                                hours = 0
                                break                                                                                            
                            elif no_charge_index not in when_index and change[no_charge_index].text=='WHEN':
                                for amp in range(no_charge_index+1, len(change)):
                                    if change[amp].pos_=="NUM" and change[amp].ent_type_!="TIME" and change[amp].is_alpha==False and change[amp].text not in hours_list and change[amp].text not in prices_list:
                                        price = change[amp].text
                                        when_index.append(no_charge_index)
                                        hours_list.append(hours)
                                        print(hours, " ", price)
                                        prices_list.append(price)
                                        price = 0
                                        hours = 0
                                        break                                
                            no_charge_exist = 0                                                                                                                    
                        if no_charge_exist==0 and change[index].text not in hours_list:
                            hours_list.append(hours)            
                            prices_list.append(price)
                            print(hours, " ", price)
                            hours = 0
                            price = 0
                            break                        
                if hours==0 and price!=0:
                    hours_list.append(hours)            
                    prices_list.append(price)
                    print(hours, " ", price)
                    hours = 0                                  
        print(hours_list, prices_list)
        
test = PreSale("DELBOM-AI-INR.txt")
test.cancellation_presale()
# "DELBOM-AI-INR.txt"