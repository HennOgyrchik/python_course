import os

def MyPow (a,b):
    if b==1:
        return a
    elif b==-1:
        return 1/a
    elif b>1:    
        return a * MyPow(a,b-1)
    else:
        return 1/a * MyPow(a, b+1)
    

def MySum (a,b):
    if a!=0:
        return MySum(a-1,b)+1
    elif b!=0:
        return MySum(a,b-1)+1
    else:
        return 0
    
#семинар 8
