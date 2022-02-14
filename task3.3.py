#variables
#WAP to check type of data accepted using input() function

val=input()
print(type(val))

#WAP to accept name from user and display
#Hello Username
name=input()
print("Hello {}".format(name))

# Accept first name middle name and surname from user (Use 3 input() ).Display the user input as
#Surname Firstname Middlename
firstname=input()
middlename=input()
sirname=input()
print("{} {} {}".format(firstname,middlename,sirname))

#Accept name,age and address from user and display it as ( You are allowed to use only 1 print())
#Name:Username
#Age:Userage
#Address:UserAddress
name=input()
age=int(input())
address=input()
print('Name:{}\nAge:{}\nAddress:{}'.format(name,age,address))

#Accept Student Details-Rollno,Name,percent and display as (Use 2 print())
	#Rollno		Name		Percentage
	#UserRoll	Username	UserPercent

rollno=int(input())
name=input()
percentage=float(input())
print("Rollno Name  Percentage")
print("{}  {}  {}".format(rollno,name,percentage))

