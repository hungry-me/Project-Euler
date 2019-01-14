import math;

def checkPrime(n):
    sq=int(math.sqrt(n));
    for i in range(2,sq+1):
        if(n%i==0):
            return False;
    return True;

def primeFactor():
    ls=[];
    n=600851475143;
    for i in range(2,int(math.sqrt(n))):
        if(n%i==0 and checkPrime(i)):
            ls.append(i);
    ls.sort();
    print(ls[-1]);

primeFactor();