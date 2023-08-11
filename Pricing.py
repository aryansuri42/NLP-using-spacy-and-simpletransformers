import spacy
from DataCleaning import *
from QueryTesting import *
from Ticket import * 
from TimeRestriction import *


nlp = spacy.load("en_core_web_lg")

def country_cancellelation(filename, country):
    rules_temp = FileCleaning(filename)
    doc_temp = nlp(rules_temp.filtering()[0])
    for token in doc_temp:
        if str(token) == country :
            return 1
        else:
            continue
    return 0

class ChangePricing:
    def __init__(self, filename, uid, after_hours, before_hours):
        self.filename = filename
        self.uid = uid
        self.before_hours = before_hours
        self.after_hours = after_hours
        
    def charges(self, query):
        rules = FileCleaning(self.filename)
        ticket = FindTicket(self.uid)
        query_find = QueryMatch(query, self.filename)
        query_index = query_find.changematch()
        hrs_detail = HourCalc(self.after_hours, self.before_hours, self.filename)
        price = hrs_detail.change_hours(query_index)
        if price == 0.0:
            print("NO CHANGES PERMITTED")
            return
        new_base_price = int(input("New Base Price: "))
        base_price = float(ticket.ticketbaseprice())
        existing_extra = float(ticket.extraprice())
        if new_base_price > base_price:
            charges = price + (new_base_price-base_price) + existing_extra
            update = UpdatePrices(self.uid, charges)
            update.extra()
        else:
            charges = price + existing_extra
            update = UpdatePrices(self.uid, charges)
            update.extra()
            
    def cancelcharges(self, country, query=0):
        rules = FileCleaning(self.filename)
        ticket = FindTicket(self.uid)
        hrs_detail = HourCalc(self.after_hours, self.before_hours, self.filename)
        price = hrs_detail.cancel_hours()
        check_country = country_cancellelation(filename=self.filename, country=country)
        update = UpdatePrices(self.uid, charges=price)
        if self.before_hours==0:
            hrs_detail = HourCalc(self.after_hours, self.before_hours, self.filename)
            price = hrs_detail.cancel_hours()
            update.noshow()
        elif check_country==1:
            update.country_refundable(country=country)
        elif query==1:
            statement = input("ENTER THE CASE: ")
            query = QueryMatch(statement, self.filename)
            query_res = query.cancelmatch()
            if query_res[0]==2 or statement=="DEATH":
                update.fullrefund()
            elif query_res[0]==1:
                hrs_detail = HourCalc(self.after_hours, self.before_hours, self.filename)
                price = hrs_detail.cancel_hours(query_res[1])
                update.regular_refund()

        else:
            update.regular_refund()
    
    # def charges_according_to_time(self, rule_list, index, time_index,time, before_hours):
    #     rule = nlp(str(rule_list[index]))
    #     print(rule)
    #     if before_hours < time:
    #         for token in range(time_index+1,len(rule)):
    #             if rule[token].pos_=='NUM' and rule[token].is_alpha==False:
    #                 return(float(rule[token].text))
                
    #     elif before_hours > time:
    #         for token in range(time_index-1,-1,-1):
    #             if rule[token].pos_=='NUM' and rule[token].is_alpha==False:
    #                 return(float(rule[token].text))
            
                
    # def change_timings(self):
    #     rules = FileCleaning(self.filename)
    #     rule_list = rules.changes_split()
    #     for rule in range(0, len(rule_list)):
    #         doc = nlp(str(rule_list[rule]))
    #         for token in range(0,len(doc)):
    #             if doc[token].pos_=="NUM" and doc[token].ent_type_=="TIME" and doc[token].is_alpha==False:
    #                 time = int(doc[token].text)
    #                 find_charge = self.charges_according_to_time(rule_list, rule, token, time, self.before_hours)
    #                 if find_charge==None:
    #                     find_charge=0.0
    #                 return [find_charge, time]
                
            
        
        
# extracharges = ChangePricing("YYZCOK-RULE-K.txt", "dac5518c-b63e-4539-815c-71fd3f555e70",25, 0)
# extracharges.cancelcharges(country='INDIA')    
                    
