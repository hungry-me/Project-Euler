import math;

def checkPrime(n):
    sq=int(math.sqrt(n));
    for i in range(2,sq+1):
        if(n%i==0):
            return False;
    return True;

def sumPrime(n):
    res=0;
    for i in range(2,n+1):
        if(checkPrime(i)):
            res+=i;
    print(res);

sumPrime(2000000);