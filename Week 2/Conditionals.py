# Q 1
# a=int(input("Enter number:"));
# if(a>=0):
#     print("Positive.");
# else:
#     print("Negetive.");

# Q 2
# num=int(input("Enter marks:"))
# if(num>=90):
#     print("Your grade is 'A'.");
# elif(num>=75):
#     print("Your grade is 'B'.");
# elif(num>=60):
#     print("Your grade is 'C'.");
# elif(num>=40):
#     print("Your grade is 'D'.");
# else:
#     print("You are fail.");

# Q 3
# m=int(input("Enter month number:"));
# if(m<5):
#     print("This is first season.");
# elif(m>=5 and m<9):
#     print("This is second season.");
# else:
#     print("This is last season.");

# Q 4
# a=int(input("Enter 1st side of triangle:"));
# b=int(input("Enter 2nd side of triangle:"));
# c=int(input("Enter 3rd side of triangle:"));
# if(a+b>c):
#     if(a==b==c):
#         print("Equilateral Triangle.");
#     elif((a==b and a!=c) or (b==c and b!=a) or (a==c and a!=b)):
#          print("Isoceles Triangle.");
#     else:
#         print("Scalene Triangle.");
# else:
#     print("Not a Triangle.");

# Q 5
# y=int(input("Enter Year:"));
# if(y%400==0):
#     print("Entered year is leap year.");
# elif(y%100==0):
#     print("Enter year is not a leap year.");
# elif(y%4==0):
#     print("Enter year is leap year.");
# else:
#     print("Enter year is not a leap year.");

# Q 6
r1=float(input("Enter minimun value of range:"));
r2=float(input("Enter maximum value of range:"));
n=float(input("Enter number:"));
if(r1<n<r2):
    print("Enter number is within the range.");
else:
    print("Enter number is not in range.");