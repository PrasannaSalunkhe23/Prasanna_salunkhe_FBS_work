feet=float(input("enter feet:"))
inches=float(input("enter inches:"))

#calculate total_inches
total_inches = (feet *12) +inches



#convert inches into meter
meter = total_inches * 0.0254

#convert meter into cm
cm = meter * 100




print("meters=",meter)
print("centimeters=",cm)