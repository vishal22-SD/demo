#Arithematic operator
#WAP to calculate x raised to the power n (xn). Accept the value of x and n from the user.
x=int(input("Enter value of x:"))
n=int(input("Enter value of n:"))
print("X power of n is:",x**n)

# WAP to calculate average of three numbers.Accept numbers  from user
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter third number:"))
avg=(num1+num2+num3)/3
print("Average of three number is:",round(avg,2))

#Write a Python program to convert degree to radian.
degree=int(input("enter degree:"))
pi=3.14
convert=degree*(pi/180)
print("Degree convert into radian is:",round(convert,2))

#Write a Python program to convert radian to degree.
radian=int(input("enter radian:"))
pi=3.14
convert=radian*(180/pi)
print("Radian convert into degree is:",round(convert,2))

#Write a Python program to calculate the area of a trapezoid.
Base1=int(input("enter shorter base:"))
Base2=int(input("enter longer base:"))
Height=int(input("enter height:"))
area=((Base1+Base2)/2)*Height
print("Area of trapezoid is:",round(area,2))

# Write a Python program to calculate the area of a parallelogram.
base=int(input("enter base of parallelogram:"))
height=int(input("enter height of Parallelogram"))
print("Area of parallelogram is:",base*height)

#Write a Python program to calculate surface area and volume of a cylinder.
radius=int(input("enter radius:"))
height=int(input("enter height"))
pi=3.14
Area=(2*pi*radius*height)+(2*pi*(radius**2))
volume=pi*(radius**2)*height
print("Surface area of cylinder is:",Area)
print("Volume of cylinder is:",volume)

#Write a Python program to calculate surface area and volume of a sphere.
radius=int(input("enter radius:"))
pi=3.14
spArea=4*pi*(radius**2)
spvolume=(4/3)*pi*(radius**3)
print("Surface area of sphere is:",spArea)
print("Volume of sphere is:",spvolume)
