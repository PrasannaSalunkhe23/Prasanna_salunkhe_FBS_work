#1. Write a program to prompt user to enter userid and password. If Id and  password is incorrect 
# give him chance to re-enter the credentials. Let him try 3  times. After that program to terminate.  


User_id='Prasanna'
Password='2309'
attempt=1
while(attempt<=3):
    userid=input("Enter the User_id:")
    password=input("Enter the Password:")
    if(User_id==userid and Password==password):
        print("Login Successfully")
        break
    else:
        print("invalid User_id & Password")
        attempt=attempt+1
    if attempt==4:
        print("Program Terminate")    
        

