import math
a=float(input("Enter a number"))
b=input("Enter operation ")
if b=='+':
    c=float(input("Enter a number"))
    ans=a+c
elif b=='-':
    c=float(input("Enter a number"))
    ans=a-c
elif b=='*':
    c=float(input("Enter a number"))
    ans=a*c
elif b=='/':
    c=float(input("Enter a number"))
    ans=a/c
elif b=='^':
    c=float(input("Enter a number"))
    ans=a**c
elif b=='sqrt':
    ans=math.sqrt(a)
elif b=="sin":
    ans=math.sin(a)
elif b=="cos":
    ans=math.cos(a)
elif b=="tan":
    ans=math.tan(a)
elif b=="asin":
    ans=math.asin(a)
elif b=="acos":
    ans=math.acos(a)
elif b=="atana":
    ans=math.atan(a)
print(ans)