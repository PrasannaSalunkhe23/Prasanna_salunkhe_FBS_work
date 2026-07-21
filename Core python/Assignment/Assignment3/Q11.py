ag1=int(input("Enter the age of first person="))
tkprice1=float(input("Enter the Ticket price of first person="))

totalprice=0

if ag1<12:
    totalprice=totalprice+(tkprice1*0.30)
elif ag1>59:
    totalprice=totalprice+(tkprice1*0.50)
else:
    totalprice=totalprice+tkprice1
    #first person ends here...



ag2=int(input("Enter the age of second person="))
tkprice2=float(input("Enter the Ticket price of second person="))
if ag2<12:
    totalprice=totalprice+(tkprice2*0.30)
elif ag2>59:
    totalprice=totalprice+(tkprice2*0.50)
else:
    totalprice=totalprice+tkprice1
    #second person ends here...





ag3=int(input("Enter the age of third person="))
tkprice3=float(input("Enter the Ticket price of third person="))

if ag3<12:
    totalprice=totalprice+(tkprice3*0.30)
elif ag3>59:
    totalprice=totalprice+(tkprice3*0.50)
else:
    totalprice=totalprice+tkprice1
    #third person ends here...




ag4=int(input("Enter the age of fourth person="))
tkprice4=float(input("Enter the Ticket price of fourth person="))


if ag4<12:
    totalprice=totalprice+(tkprice4*0.30)
elif ag4>59:
    totalprice=totalprice+(tkprice4*0.50)
else:
    totalprice=totalprice+tkprice1
    #fourth person ends here...

    
    
    
ag5=int(input("Enter the age of five person="))
tkprice5=float(input("Enter the Ticket price of five person="))



if ag5<12:
    totalprice=totalprice+(tkprice5*0.30)
elif ag5>59:
    totalprice=totalprice+(tkprice5*0.50)
else:
    totalprice=totalprice+tkprice1
    #five person ends here...



    print(f"total amount:,total")