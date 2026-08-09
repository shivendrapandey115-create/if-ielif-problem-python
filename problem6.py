# write a program to calculate the grade of a student from his marks from the 
# following scheme
# 90-100 => Ex
# 80-90 => A
# 70-80 => B
# 60-70 =>C
N = int(input("enter a number "))
if(N<=100 and N>=90 ):
    print("EX")
elif(N<=90 and N>=80):
    print("A")
elif(N<=80 and N>=70 ):
    print("B")
elif(N<=70 and N>=60 ):
    print("C")
else:
    print("fail")