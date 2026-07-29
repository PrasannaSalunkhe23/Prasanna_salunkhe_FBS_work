#3. Accept no. of passengers from user and per ticket cost. Then accept age of each  passenger 
# and then calculate total amount to ticket to travel for all of them based on  following 
# condition :  a. Children below 12 = 30% discount  b. Senior citizen (above 59) = 50% discount  
# c. Others need to pay full.


n=int(input("Enter the passenger:"))
i=1
Total_Ticket=0
while(i<=n):
    Age=int(input("Enter the age{i} person"))
    Ticket=int(input(f"Enter the Ticket {i}"))
    if(Age<12):
        Total_Ticket=Total_Ticket+Ticket-Ticket*0.3
    elif(Age>59):
        Total_Ticket=Total_Ticket+Ticket-Ticket*0.5 
    else:
        Total_Ticket=Total_Ticket+Ticket
    i=i+1
    print(f'Total Ticket Amount{Total_Ticket}')    
               