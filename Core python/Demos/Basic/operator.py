#Arithmetic operator
x=10
y=20
a='xyz'
b='abc'

#1.Addition
res=x+y

#sub
res=x-y

#mul
res=x*y

#div
res=x/y
res=x//y
print(res)

#module
res=x%y  #find remainder

#expointial
res=x**y




#Assignment operator

#1.=
x=10
x+=20
x-=5
x*=6
x/=2
x//=4
x%=10
x**=9
print(x)



#Relational operator
x=10
y=20
a='abc'

#Relational/comparison operator
#1.==   #exact equal to
print(x==y)
print(x==20)

#2.Not equal to
print(x!='10')

#3.greater than
print(x>10)

#4.greater than equal to
print(x>=10)

#5.less than
print(x<5)

#6.less  than equal to 
print(x<=10)



#Logical operator
#1. and :If both condition are true then true otherwise false
print(True and True)

#2.OR : If both condition are false then false otherwise true
print(False or True)

#3.not: opposite of condition
print(not True)



# membership operator
#1. in
print('f' in 'Firstbit')

#2. not in
print('f' not in 'Firstbit')




# Identity operator
x=10
y=20
z=30

li1=[10,20]
li2=[10,20]

#1. is
print(X is Y)
print(id(x))
print(id(y))
print(id(z))
print(li1 is li2)

