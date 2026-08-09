# write a program to find a greates of four numbers entered by
# a user 
A = int(input("enter a number A:"))
B= int(input("enter a number B:"))
C = int(input("enter a number C:"))
D = int(input("enter a number D:"))
if(A>B and A>C and A>D):
    print("A is the greatest number")
if(B>A and B>C and B>D):
    print("B is the greatest number")
if(C>A and C>B and C>D):
    print("C is the greatest number")
if(D>A and D>B and D>C):
    print("D is the greatest number")
