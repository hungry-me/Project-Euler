def fibbo():
    a,b=1,2;
    sm=0;
    while(a<=4000000):
        if(a%2==0):
            sm+=a;
        a,b=b,a+b;
    print(sm);

fibbo();