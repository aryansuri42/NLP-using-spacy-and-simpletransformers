from prettytable import from_csv
def printtable():
    with open("Fare.csv") as fp:
        mytable = from_csv(fp)
        
    print(mytable)