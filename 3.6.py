#decision and control flow
#WAP to determine input number is even or odd
num=int(input("enter number:"))
if(num%2==0):
    print("number is even")
else:
    print("number is odd")

# Find out if a given year is a leap year or not.
year=int(input("enter year:"))
if (year % 400 == 0) and (year % 100 == 0):
    print("leap year")
elif (year % 4 ==0) and (year % 100 != 0):
    print("{} is leap year".format(year))
else:
    print("{} is Not a leap year".format(year))

#Write a program to check if a triangle is valid or not.(Input-3 angles of triangle).
a=int(input("enter 1st side of triangle:"))
b=int(input("enter 2nd side of triangle:"))
c=int(input("enter 3rd side of triangle:"))
if(a+b>=c)and (b+c>=a)and(c+a>=b):
    print("yes valid triangle")
else:
    print("Not valid triangle")

#WAP to determine if the seller has made profit or loss.
# Display amount of profit/loss.(Input: Cost price and selling price).
cp=int(input("enter cost price:"))
sp=int(input("enter selling price:"))
profit=abs(sp-cp)
loss=abs(cp-sp)
if(cp<sp):
    print("Profit is:",profit)
else:
    print("Loss is:",loss)

#WAP to determine if the given number is the Armstrong number or not (153 is the Armstrong number as 1³+5³+3³=153).
num=int(input("enter number:"))
val=num
length=len(str(num))
rev=0
while(num!=0):
   rem=num%10
   rev=rev+(rem**length)
   num=num//10
if(rev==val):
    print("yes number is amstrong")
else:
    print("No")


#Determine if the input number is positive or negative.
num=int(input("enter number:"))
if(num>0):
    print("number is positive")
else:
    print("number is negative")

#. WAP to check if a candidate is eligible for voting or not.
num=int(input("enter the age:"))
if(num<18):
    print("not eligible")
else:
    print("eligible")

#WAP to find the largest among 3 numbers.
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))
if(a>b) and (a>c):
    print("{} is largest".format(a))
elif(b>a)and(b>c):
    print("{} is largest".format(b))
else:
    print("{} is largest".format(c))

#Categorize the person depending on the height.
#a. <150	Dwarf
#b. =150 	Average heighted
#c. >=165	Tall

num=int(input("enter height:"))
if(num<150):
    print("Dwarf")
elif(num==150):
    print("Average heighted")
else:
    print("Tall")

#WAP to accept coordinates of a point and determine in which Quadrant it lies.
point1=int(input("Enter coordinate point1:"))
point2=int(input("Enter coordinate point2:"))
if(point1>0 and point2>0):
    print("point lies in first quadrant")
elif(point1>0 and point2<0):
    print("point lies in Second quadrant")
elif(point1<0 and point2<0):
    print("point lies in Third quadrant")
else:
    print("point lies in Fourth quadrant")

#WAP to check if the alphabet is a vowel or consonant.
alphabet=input("enter alphabet:")
vovwel=['a','e','i','o','u','A','E','I','O','U']
if(alphabet in vovwel):
    print("Alphabet is vowel")
else:
    print("Alphabet is consonant")

# Accept the month number and print its name and number of days in it.
month=int(input("Enter month"))
if(month==1):
    print("January 31")
elif(month==2):
    print("February 29")
elif(month==3):
    print("March 31")
elif (month ==4):
    print("April 30")
elif(month==5):
    print("May 31")
elif (month ==6):
    print("June 30")
elif(month==7):
    print("July 31")
elif(month==8):
    print("August 31")
elif(month==9):
    print("September 30")
elif(month==10):
    print("October 31")
elif(month==11):
    print("November 30")
elif(month==12):
    print("December 31")
else:
    print("Invalid")

# Accept Marital status  and print Miss or Mrs in front of name.
name=input()
status=input()
if(status=="yes"):
    print("Mrs.{}".format(name))
else:
    print("Miss.{}".format(name))

#Write a Menu driven program for following
#Area of circle (pi*r²)
#Area of Rectangle (l*b)
#Area of triangle (b*h/2)
#Area of Square (a²)
def circle(r,pi):
    carea=pi*(r**2)
    return carea
def Rectangle(l,b):
    rarea=l*b
    return rarea
def Triangle(b,h):
    tarea=(1/2)*b*h
    return tarea
def square(a):
    sarea=a*a
    return sarea
pi=3.14
while(True):
    print("1.Area of Circle:")
    print("2.Area of Rectangle:")
    print("3.Area of Triangle:")
    print("4.Area of Square:")
    print("5.Exit:")
    num=int(input("Enter a number:"))
    if(num==1):
        r=int(input("Enter radius of circle:"))
        print("Area of circle is:",circle(r,pi))
    if (num == 2):
        l = int(input("Enter length of rectangle:"))
        b=int(input("Enter bredth of rectangle:"))
        print("Area of rectangle is:",Rectangle(l, b))
    if (num == 3):
        b = int(input("Enter bredth of rectangle:"))
        h=int(input("Enter height of rectangle:"))
        print("Area of triangle is:",Triangle(b, h))
    if (num ==4):
        a = int(input("Enter length of square:"))
        print("Area of square is:",square(a))
    if (num == 5):
        break
