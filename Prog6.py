def getSum(n):
    res=0;
    for i in range(1,n+1):
        res+=i*i;
    return res;

def getSumSq(n):
    res=(n*(n+1))//2;
    return res*res;

def sumSquare():
    s1=getSum(100);
    s2=getSumSq(100);
    print(s2-s1);

sumSquare();