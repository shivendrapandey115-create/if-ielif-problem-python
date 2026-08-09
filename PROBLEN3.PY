#  a spam comment is defined as a text coantaining
#  following keywords: "make a lot of money","buy now".
# "subscribe this", "click this".write a program to detect 
# these spam
P1 = "make a lot of money"
P2 = "buy now"
P3 = "subscribe this"
P4 = "click this"
message = input("enter a message:")

if((P1 in message) or (P2 in message) or (P3 in message) or
   (P4 in message)):
    print("this is a spam message")