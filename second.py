#*********STRING METHODS************
# #string concatination
# str1="Devi"
# str2="sankruthya"
# print(str1+ " "+str2)  # Output: Devi sankruthya
# #length of string
# print(len(str1))  # Output: 5
# #indexing 
# print(str2[3])  # Output: k
# #slicing
# print(str2[1:4])  # Output: ank
# print(str2[0:])
# print(str1[:4])
# print(str1[-3:-1])#negative slicing(backward counting)
#  #String functions
# #  print(str1.upper())  # Output: DEVI
# #  print(str1.lower())  # Output: devi
# #  print(str1.capitalize())  # Output: Devi
# #  print(str1.title())  # Output: Devi Sankruthya
# str = "iam honeya"
# print(str.endswith("ey"))#return true as it ends with ey
# print(str.endswith("ep"))#return false as it not ends with ep
# print(str.capitalize()) #return capital letter at begining
# print(str.replace("a","j"))#replacing a in a string with j
# print(str.find("e"))#return index number of first occurence,if letter not exists in string then return -1.
# print(str.count("m"))#return no of times m present in string
#*******QUESTIONS********
# a=str(input("enter a string"))
# print(len(a))
# print(a.count("$"))
# #******* CONDITIONAL STATEMENTS********
# age= int(input("enter your age:"))
# if age>=18:
#     print("you are eligible to vote and apply for license \n")
#     print("can drive")#if condition is true then print this statement
# else:
#         print("you are not eligible to vote")#if condition is false then print this statement

# light=str(input("enter traffic light color:"))
# if(light=='green'):
#    print("go")
# elif(light=='red'):
#    print("stop")
# elif(light=='yellow'):
#    print("caution")
# else:
#     print("no light entered")
    #***grading system****
    
# marks = int(input("enter your marks:"))
# if(marks>=90):
#         print("grade A")
# elif(marks>=80 and marks<90):
#         print("grade B")
# elif(marks>=70 and marks<80):
#         print("grade C")
# elif(marks>=60 and marks<70):
#         print("grade D")
# else:
#         grade="fail"
#         print("grade of a student is:",grade)
#******NESTING*******
# age=7
# if(age>=18):
#     print("can drive")
# if(age>=60):
#     print("can drive with license")
# else:
#     print("can't drive")
#********QUESTIONS*********
a=int(input("enter a number"))
if(a%2==0):
    print("number is even")
else:
    print("number is odd")
b=int(input("enter first number"))
c=int(input("enter second number"))
d=int(input("enter third number"))
f=int(input("enter fourth number"))
if(b>=c and b>=d):
   print(b," is greatest")
elif(c>=d and c>=f):
    print(c,"is greatest")
elif(d>=f):
    print(d,"is greatest")
# elif(d>=b and d>=c):
#     print(d ,"is greater than b and c")
else:
    print(f," is greater")
e=int(input("enter a number to check multiple of 7: "))
if(e%7==0):
    print(e,"is a multiple of 7")
else:
    print(e,"is not a multiple of 7")

