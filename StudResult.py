str=input("Enter Student Name:")
clas=input("Enter the Class:")
RNo=input("Enter the RollNo:")
Sub_list =[]
mark_list = []
n=int(input("Enter how many subjects:"))
total=0
per=0
av=0
for i in range(n):
    print("Enter subjects ",i+1,":")
    Sub=input()
    print("Enter marks of Subject",i+1,":")
    mark=int(input())
    Sub_list.append(Sub)
    mark_list.append(mark)
print()
print()
print()
print("Name:",str)
print("-------------------------------------------------------------")
print("Class:",clas)
print("-------------------------------------------------------------")
print("RollNumber:",RNo)
print("-------------------------------------------------------------")
print("Subjects                      marks")
print("-------------------------------------------------------------")
for j in range(n):
    total=total+mark_list[j]
    print(Sub_list[j],"             ",mark_list[j])
    print("-----------------------------------------------------------")
av=total/2.5

if av<=100 and av>=80:
     grade='A'
elif av<30 and av>60:
     grade='B'
elif av<=60 and av>44:
     grade='C'
elif av<45 and av>=35:
     grade='D'
else:
     grade='E'
if grade=='A' or grade=='B' or grade=='C'  or grade=='D':
     result='Pass'
else:
     result='Fail'

print("Total : ",total,"    ","Percentage:",av)
print("-------------------------------------------------")
print("GRADE: ",grade,"                ","Result:",result)
print("--------------------------------------------------")
