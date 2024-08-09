# Student Details

Name=input("Enter the Student Name : ")
Roll_No=input("Enter the Student Roll_Number : ")

# Student Mark Details

sub1=input("Enter the Subject 1 : ")
sub2=input("Enter the Subject 2 : ")
sub3=input("Enter the Subject 3 : ")
sub4=input("Enter the Subject 4 : ")
sub5=input("Enter the Subject 5 : ")
sub6=input("Enter the Subject 6 : ")

subject1=input("Enter the " +sub1+ " Subject Marks : ")
subject2=input("Enter the " +sub2+ " Subject Marks : ")
subject3=input("Enter the " +sub3+ " Subject Marks : ")
subject4=input("Enter the " +sub4+ " Subject Marks : ")
subject5=input("Enter the " +sub5+ " Subject Marks : ")
subject6=input("Enter the " +sub6+ " Subject Marks : ")

# Sum

total=subject1+subject2+subject3+subject4+subject5+subject6

#Average

avg=(total/1200)*100

# Output

print("\n\n*~*~*~*~*~*~*~*~*~* OUTPUT *~*~*~*~*~*~*~*~*~")

print("\nStudent Name :", Name)
print("Student Roll_Number :", Roll_No)

print("\nTotal Marks : ",total)
print("Average Marks : ",avg)

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
