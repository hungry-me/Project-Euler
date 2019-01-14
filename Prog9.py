def pythagoras(n):
    for i in range(1,(n//3)+1):
        for j in range(1,(n//2)):
            k=n-i-j;
            if(i*i+j*j==k*k):
                res=i*j*k;
                print(res);
                exit(1);

pythagoras(1000);