import math;

def checkPrime(n):
    sq=int(math.sqrt(n));
    for i in range(2,sq+1):
        if(n%i==0):
            return False;
    return True;

def prime():
    n,i=0,0;
    while(n<=10002):
        if(checkPrime(i)):
            n+=1;
        i+=1;
    print(i-1);

prime();