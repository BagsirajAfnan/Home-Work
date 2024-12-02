
# to check the number is positive or negative
# a=20
# if a>0:
#     print("The Number is Positive")
# elif a==0:
#     print("The Number is Zero")
# else:
#     print("The Number is Negative")
    
    
    
# to find the number is even or odd

# a=20
# if a%2==0:
#     print("The number is Even")
# else:
#     print("The Number is Odd")
    
    

# to check the grade based on percentage
 
# a=int(input("enter a your percentage"))
# if a>=90 and a<=100:
#     print("Grade, A")
# elif a>=70 and 85<=89:
#     print("Grade, B")
# elif a>=50 and a<=69:
#     print("Grade, C")
# else :
#     print("Grade, F")


# to check number is divisible by 3,5,or both

# a=3
# if a%5==0 and a%3==0:
#     print("The Number is Divisible By Both")
# elif a%3==0:
#     print("The Number is Divible By 3")
# elif a%5==0:
#     print("The Number is Divible By 5")


# to find minimum

# a=110
# b=20
# if a<b:
#     print(a)
# else:
#     print(b)


# to find largest number 

# a=10 
# b=20
# c=30
# if a>b and a>c:
#     print(a)
# else:
#     if b>c and b>a:
#         print(b)
#     else:
#         print(c)


# check leap year

# a=2010
# if a%4==0 or a%400==0:
#     print("The given year is Leap year")
# else:
#     print("The year is not a leap year")
    

# Temperature checking 
# a=15
# if a<15:
#     print("Cold")
# else:
#     if a>=15 and a<=30:
#         print("warm")
#     else:
#         print("Hot")

# to check vowel or consonant
# a,e,i,o,u

# z='b'

# if z=='a'=='e' or z=='i' or z=='0' or z=='u or z':
#     print("The character is vowel")
# else:
#     print("The given character is consonent")


# driving  eligibility
# a=16
# licence=True
# if a>=18:
#     print("The person is Eligilble to drive a car")
#     if licence==True:
#         print(" licence is Valid ")
#     else:
#         print("licence is Not  Valid")
# else:
#     print("The persin is Not Eligilble to drive a car")
   
   
 
 
#tax based

# a=5000000
# if a<=50000:
#     b = a*5/100
#     print(b)
#     print("5% tax is compulsory")
# elif a>=500001 and a<=1000000:
#      b = a*5/100
#      print(b)
#      print("10% tax is compulsory")
# else:
#     b = a*5/100
#     print(b)
#     print("20% tax is compulsory")



# age categorize

# a=50
# if a>=0 and a<=12:
#     print("Child")
# elif a>=13 and a<=19:
#     print("Teen")
# elif a>=20 and a<=59:
#     print("Adult")
# else:
#     print("Senior")
    
# logical and 

# a=5
# if a>10 and a%2==0:
#     print("The Number is Greater than 10 and divisble by 2")
# else:
#     print("The Number is not  Greater than 10 and not divisble by 2")


# logical or 
# a=21
# if a==5 or a>20:
#     print("The Number is greater than 20")
# else:
#     print("The Number is less than 5")



# electricity unit 
# u=250
# if u<=100:
#     c=5*u
#     print(c)
# elif u>=101 and u<=200:
#     c=10*u
#     print(c)
# else:
#     c=15*u
#     print(c)


# # type checker

# char='@'
# if isinstance(char,str) and len(char)==1:
#     print("Alphabet")
# elif not char.isalnum():
#     print("special character")
# elif type(char)==int:
#     print("Integer")

char = 1

if isinstance(char, str):
    if char.isalpha():  # Check if it's an alphabet
        print("Alphabet")
    elif not char.isalnum():  #Check if it's a special character
        print("Special Character")
elif type(char)==int:
    print("Integer")
else:
    print("Other Type")
    
# season finder

# w = ["December","January","Febaury"]
# s=["March","April","May"]
# summer=["June","July","August"]
# Autumn=["September","October","November"]

# b="August"
# if b in w:
#     print("winter")
# elif b in s:
#     print("spring")
# elif b in summer:
#     print("summer")
# else:
#     print("autumn")




# body weight

# a=16
# if a<=18.5:
#     print("Under Weight")
# elif a>=18.5 and a<=24.9:
#     print("Normal")
# elif a>=25 and a<=29.9:
#     print("over wieght")
# else:
#     print("obese")


# password checker
# a="afnan@g"
# if  len(a)<=8 and "@" in a:
#     print("condition matched")
# else:
#     print("does not meet the conditons")


# triangle 
# a=10
# b=4
# c=5
# if a+b>c and a+c>b and b+c>a:
#     print("True")
# else:
#     print("False")
