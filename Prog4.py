def checkPallindrome(n):
    n=str(n);
    rev=n[::-1];
    if(n==rev):
        return True;
    return False;

def largeProd():
    for i in range(999,800,-1):
        for j in range(999,800,-1):
            n=i*j;
            if(checkPallindrome(n)):
                print(n);
                exit(1);

largeProd();
