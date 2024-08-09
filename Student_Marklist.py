# Student Details

Name=input("Enter the Student Name : ")
Roll_No=input("Enter the Student Roll_Number : ")

# Student Mark Details

sub1=input("Enter the Subject 1 Marks : ")
sub2=input("Enter the Subject 2 Marks : ")
sub3=input("Enter the Subject 3 Marks : ")
sub4=input("Enter the Subject 4 Marks : ")
sub5=input("Enter the Subject 5 Marks : ")
sub6=input("Enter the Subject 6 Marks : ")

# Sum

total=sub1+sub2+sub3+sub4+sub5+sub6

#Average

avg=total*100

# Output

print("\n\n*~*~*~*~*~*~*~*~*~* OUTPUT *~*~*~*~*~*~*~*~*~")

print("\nStudent Name :", Name)
print("Student Roll_Number :", Roll_No)

print("\nPlease Enter", sub1 ,"Marks")
print("Please Enter", sub2 ,"Marks")
print("Please Enter", sub3 ,"Marks")
print("Please Enter", sub4 ,"Marks")
print("Please Enter", sub5 ,"Marks")
print("Please Enter", sub6 ,"Marks")

print("\nTotal Marks : ")
print("Average Marks : ")

#Functions

if avg>=91 and avg<=100:
    print("\nYour Grade is : A+ ")
elif avg>=81 and avg<=90:
    print("Your Grade is : A")
elif avg>=71 and avg<=80:
    print("Your Grade is : B+")
elif avg>=61 and avg<=70:
    print("Your Grade is : B")
elif avg>=51 and avg<=60:
    print("Your Grade is : C+")
elif avg>=41 and avg<=50:
    print("Your Grade is : C")
elif avg>=35 and avg<=40:
    print("Your Grade is : D")
else:
    print("Fail")

print("\n\n~*~*~*~*~*~*~*~*~*~ ENTER TO THE EXIT ~*~*~*~*~*~*~*~*~*~")
