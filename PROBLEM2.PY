# write a program to find out whether a student has passed 
# or failed if it requires a total of 40% and at least 33%
# in each subject to pass . Assume 3 subject and take marks 
# as an input from the user
NAME = input("enter student name: ")
SUBJECT1 = int(input("enter a number of subject :"))
SUBJECT2 = int (input("enter a number of subject :"))
SUBJECT3 = int(input("enter a nuber of subject :"))
RESULT =((SUBJECT1 + SUBJECT2 +SUBJECT3)/300)*100
print("RESULT:",RESULT)
if(RESULT>=40 ):
    print("student has passed")
else:
    print("student has failed")