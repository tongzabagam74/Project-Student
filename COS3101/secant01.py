def f(x):
    a = pow(x,3)+( 3*pow(x,2))-(9*x)-11
    return a

flag = 1
inx = 0
p0 = 50
p1 = 40
print("inx         p2           f(p2)")
while(flag):
    p2 = p1-(f(p1)*(p1-p0))/(f(p1)-f(p0))
    inx = inx+1
    if(f(p2) == 0 or abs(f(p2))<0.0000000001):
        print("found root")
        flag = 0
    else:
        p0 = p1
        p1 = p2;
    print(inx,"           ",p2,"           ",f(p2))
