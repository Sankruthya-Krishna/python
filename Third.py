# #*********LISTS*********lists are mutable(change)strings are immutable in python
# marks=[5,6.7,4,8,0,4]
# print(type(marks))
# print(len(marks))
# # print(marks[2])
# # marks[2]="honey"

# #*****LIST SLICING*****
# # print(marks[1:4])
# #******List methods*****
# marks.append(2)#added element in end of the list
# print(marks)
# print(marks.sort())#ascending order
# print(marks)
# print(marks.sort(reverse=True))#descending order
# print(marks)
# print(marks.reverse())# reverse the list
# print(marks)
# marks.insert(2,'oil')#inserted oil as a element at ind2
# print(marks)
# marks.remove(4)# remove element 4 where it occured for the first time
# print(marks)
# marks.pop(2)# removed index 2 element
# print(marks)
# #******Tuples*****
# tup=(5,6,7,8,6,9)
# print(type(tup))
# tup2=(1,)
# print(type(tup2))# gives as tuple as we declared , in declaration....if there is no , then int type will be printed.
# #*********TUPLE SLICING**********
# print(tup[1:4])
# #*********TUPLE METHODS**********
# # print(tup.append(10))#tuple is immutable so we cant use append method
# print(tup.index(6))#takes index of first occurence of element'6'
# print(tup.count(6))#counts the number of times 6 occured in the tuple
# print(tup)
#...........QUESTIONS..........
m1=input("enter first movie: ")
m2=input("enter second movie: ")
m3=input("enter THIRD movie: ")
list=[m1,m2,m3]
print(type(list))
print(list)
pal=[1,2,0]
r=pal.copy()
r.reverse()
if(pal==r):
    print("palindrome")
else:
    print("not palindrome")
grade=("C","D","A","A","B","B","A")
print(type(grade))
print(grade.count("A"))#counts the number of times a occured in the tuple
grade1=["C","D","A","A","B","B","A"]
grade1.sort()
print(grade1)
