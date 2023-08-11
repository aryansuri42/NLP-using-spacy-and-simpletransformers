from Pricing import *
from Ticket import *
from file_print import *

# from Penalities import *
print("1. TICKET BOOKING")
print("2. CANCELLATION")
print("3. CHANGES")
print("4. PRE-SALE MODE")
print("5. PRINT ENTRIES")
loop=True
while loop:
    x = int(input("ENTER: "))
    if x==1:
        flightrules = input("Rules: ")
        base_fare = int(input("Base Fare: "))
        taxes = int(input('TAXES: '))
        fuel_surcharge = int(input('FUEL CHARGES: '))
        airport_charges = int(input('AIRPORT CHARGES: '))
        ticket = FlightTicket(rules=flightrules, base_fare=base_fare, taxes=taxes,fuel_surcharge=fuel_surcharge, airport_charges=airport_charges)
        ticket.dumpticket()
        
    elif x==2:
        ticket_id = input("Ticket ID ")
        df = pd.read_csv("Fare.csv", index_col="ID")
        rules = df.loc[ticket_id, 'RULES']
        after_hours = int(input('TIME SPENT AFTER BOOKING OF TICKET: '))
        before_hours = int(input("TIME BEFORE DEPARTURE"))
        country = input("COUNTRY: ")
        case1 = print("REGULAR")
        case2 = print('NO SHOW')
        case3 = print("OTHER")
        y = int(input("CHOICE: "))
        if y==1:
            # penalty = Penalties(uid=ticket_id, rules=rules, after_hours=after_hours, before_hours=before_hours, case='CANCELLATION', sub_case='REGULAR')
            # penalty.updatefile()
            cancellation_charges = ChangePricing(rules, ticket_id, after_hours, before_hours)
            cancellation_charges.cancelcharges(country=country)
        elif y==2:
            # penalty = Penalties(uid=ticket_id, rules=rules, after_hours=after_hours, before_hours=before_hours,case='CANCELLATION', sub_case='NO SHOW')
            # penalty.updatefile()
            cancellation_charges = ChangePricing(rules, ticket_id, after_hours, 0)
            cancellation_charges.cancelcharges(country=country)
        elif y==3:
            # penalty = Penalties(uid=ticket_id, rules=rules, after_hours=after_hours, before_hours=before_hours, case='CANCELLATION', sub_case="")
            # penalty.updatefile()
            cancellation_charges = ChangePricing(rules, ticket_id, after_hours, before_hours)
            cancellation_charges.cancelcharges(country=country, query=1)
            
        
    elif x==3:
        ticket_id = input("Ticket ID ")
        df = pd.read_csv("Fare.csv", index_col="ID")
        rules = df.loc[ticket_id, 'RULES']
        after_hours = int(input('TIME SPENT AFTER BOOKING OF TICKET: '))
        before_hours = int(input("TIME BEFORE DEPARTURE: "))
        query = input("CASE: ")
        extracharges = ChangePricing(rules, ticket_id, after_hours, before_hours)
        extracharges.charges(query = query)
        # penalty = Penalties(uid=ticket_id, rules=rules, after_hours=after_hours, before_hours=before_hours, case='CHANGES', sub_case=query)
        # penalty.updatefile()
        
    elif x==4:
        loop2 = True
        while loop2:
            print("1. CANCELLATION")
            print("2. CHANGES")
            sub_choice = int(input("ENTER: "))
            if sub_choice==1:
                pass
            elif sub_choice==2:
                pass
            else:
                loop2=False
        
    elif x==5:
        printtable()
        
    else:
        loop=False