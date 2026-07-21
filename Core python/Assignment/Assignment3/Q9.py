m1=float(input("subject 1 marks:"))
m2=float(input("subject 2 marks:"))
m3=float(input("subject 3 marks:"))
m4=float(input("subject 4 marks:"))
m5=float(input("subject 5 marks:"))



percentage=(m1+m2+m3+m4+m5)

if percentage>=75:
    print("grade:Distination")
elif percentage>=60:
    print("grade: first class")
elif percentage>=50:
    print("grade: second class")
elif percentage>=35:
    print("grade:pass class")
else:
    print("grade:fail")