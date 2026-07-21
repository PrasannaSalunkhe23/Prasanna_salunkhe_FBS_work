gender=input("Enter gender(m/f):")
age=int(input("Enter the age:"))

if(gender=="f"):
    if(age>=18):
        print("girls is eligible for marriage")

    else:
        print("pehle padai kar lo")

else:
    if (age > 21):
        print("Boy is eligible for marriage.")
    else:
        print("Pehle kama lo.")
        