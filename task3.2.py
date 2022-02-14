#Type and Typecasting
#1. Assign three different values to three different variables and print them.
val1=23
val2=34
val3=12
print(val1,val2,val3)

#2. Write a program to demonstrate single and multiple assignment of values to a variables
a=5
print(a)
a=b=c=5
print(a,b,c)
a,b,c=2,3,4
print(a,b,c)

#3. Write a program to swap two variables.
a=5
b=4
temp=a
a=b
b=temp
print(a,b)

#Write a program to demonstrate that a single variable can store different type of values at different instance of time
a=5
print(a)
a=4.5
print(a)
a='tom'
print(a)

#Write a program to concatenate two strings.
str1="Hello"
str2="Welcome!"
print(str1+' '+str2)

#WAP to assign different type of values to one variable at different instance of and print its type each time
val1=5
print(type(val1))
val2=3.4
print(type(val2))
val3="Jhon"
print(type(val3))
val4=True
print(type(val4))

#Write a program to calculate simple interest.Accept values from user.(si=pnr/100)

p=int(input("enter value of principle:"))
n=int(input("enter value of time:"))
r=int(input("enter value of rate:"))
si=(p*n*r)/100
print("simple interest =",si)

#