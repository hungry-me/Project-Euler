def hcf(a,b):
    if(b==0):
        return a;
    return hcf(b,a%b);

def lcm(a,b):
    return (a*b)//hcf(a,b);

def smallMul():
    n=20;
    res=1;
    for i in range(2,n+1):
        res=lcm(res,i);
    print(res);

smallMul();