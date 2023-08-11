from DataCleaning import *
string = """CHANGES                                                       
    ANY TIME                                                    
      CHARGE CAD 300.00 FOR REISSUE/REVALIDATION.               
      WAIVED FOR DEATH OF PASSENGER OR FAMILY MEMBER.           
         NOTE -                                                 
          FOR ALL CHANGES WITHIN 96 HOURS BEFORE DEPARTURE      
          OF A FLIGHT A CHARGE OF 330 CAD MUST BE COLLECTED     
          FOR CHANGE OF RESERVATION."""
print(string.find("300.00"))