def LastFibon(n):
    if n in [0,1]:
        return 1
    return LastFibon(n-1)+LastFibon(n-2)

def is_simple(n):
    if n>2 and n%2!=0:
        for i in range(3,n//2):
            if n%i==0:
                return False
        return True
    else:
        return False
    
def ReverseRange(num):
    print(num, end=' ')
    if num>0:
        ReverseRange(num-1)
    