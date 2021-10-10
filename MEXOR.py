#Question Code MEXOR
for i in range(int(input())):
    x=int(input())
    ans=1
    if x==0:
        print(1)
    elif x==1 or x==2:
        print(2)
    else:
        while ans*2<=x:
            ans*=2
        if ans==x:
            print(x)
        elif x==2*ans-1:
            print(x+1)
        else:
            print(ans)
