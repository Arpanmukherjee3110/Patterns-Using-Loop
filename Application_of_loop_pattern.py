class Sample: 
    def loop1(n):
        k=""
        for i in range(1, n+1,1):
            for j in  range(1,i+1,1):
                k=k+str(j)
            print(k)
            k="" 
        print()    
    def loop2(n):
        k=""
        for i in range(1, n+1):
            for j in range(1,i+1):
                if j%2==0:
                    k=k+"*"
                else:
                    k=k+"#"
            print(k)
            k="" 
        print()        
    def loop3(n):
        Str=""
        for i in range(0,n):
            for j in range(-1,i):
                Str=Str+"* "
            print(Str)
            Str=""
        print()        
    def loop4(n):
        sum=0
        st=""
        for i in range(1,n+1):
            for l in range(n,i,-1):
                st=st+" "
            for j in range(i):
                sum=i+j
                while(sum>9):
                    sum=sum-10
                st=st+str(sum)
            for k in range(2*i-1,i,-1):
                if sum==0:
                    sum=10
                sum=sum-1
                st=st+str(sum)
            print(st)
            sum=0
            st=""
        print() 
    def loop5(n):
        for i in range(1,n+1):
            sp=""
            for space in range(n,i,-1):
                sp=sp+" "
            for j in range(1,i+1):
                sp=sp+str(j)
            print(sp)
            sp=""
        print()        
    def loop6(n):
        for i in range(1,n+1):
            sp=""
            for space in range(n,i,-1):
                sp=sp+" "
            for j in range(1,i+1):
                if j%2==0:
                    sp=sp+"*"
                else:
                    sp=sp+"#"
            print(sp)
            sp=""
        print()        
    def loop7(n):
        sp=""
        for i in range(1,n+1):
            for space in range(n,i,-1):
                sp=sp+" "
            for j in range(i,0,-1):
                sp=sp+str(j)
            print(sp)
            sp=""
        print()            
    def loop8(n):
        for i in range(1,n+1):
            sp=""
            for space in range(n,i,-1):
                sp=sp+" "
            for j in range(i,0,-1):
                if j%2==0:
                    sp=sp+"*"
                else:
                    sp=sp+"#"
            print(sp)
            sp=""
        print()
    def loop9(n):
        sp=""
        for i in range(1,n+1):
            for space in range(n,i,-1):
                sp=sp+" "
            for j in range(i,0,-1):
                sp=sp+str(j)
            for k in range(2,i+1):
                sp=sp+str(k)
            print(sp)
            sp=""
        print()
    def loop10(n):
        for i in range(1,n+1):
            sp=""
            for space in range(n,i,-1):
                sp=sp+" "
            for j in range(1,i+1):
                sp=sp+str(j)
            for k in range(i-1,0,-1):
                sp=sp+str(k)
            print(sp)
            sp=""
        print()
    def loop11(n):
        for i in range(1,n+1):
            sp=""
            for space in range(n,i,-1):
                sp=sp+" "
            for j in range(i,0,-1):
                if j%2==0:
                    sp=sp+"*"
                else:
                    sp=sp+"#"
            for k in range(2,i+1):
                if k%2==0:
                    sp=sp+"*"
                else:
                    sp=sp+"#"
            print(sp)
            sp=""
        print()
    def loop12(n):
        for i in range(1,n+1):
            sp=""
            for space in range(n,i,-1):
                sp=sp+" "
            for j in range(i,0,-1):
                sp=sp+"*"
            for k in range(2,i+1):
                sp=sp+"*"
            print(sp)
            sp=""
        print()           
            
print("Press 1 to print all the patterns")
print("Press 2 to print user specified patterns") 
n=int(input())
if n==1:
    print("Enter number of rows")
    c=int(input())
    Sample.loop1(c)
    Sample.loop2(c)
    Sample.loop3(c)
    Sample.loop4(c)
    Sample.loop5(c)
    Sample.loop6(c)
    Sample.loop7(c)
    Sample.loop8(c)
    Sample.loop9(c)
    Sample.loop10(c)
    Sample.loop11(c)
    Sample.loop12(c)
if n==2:
    for i in range(12):
        print("Press --",i+1," to print pattern-",i+1)
    m=int(input())
    if m==1:
       print("Enter number of rows")
       c=int(input())
       Sample.loop1(c)
    if m==2:
       print("Enter number of rows")
       c=int(input())
       Sample.loop2(c) 
    if m==3:
       print("Enter number of rows")
       c=int(input())
       Sample.loop3(c) 
    if m==4:
       print("Enter number of rows")
       c=int(input())
       Sample.loop4(c) 
    if m==5:
       print("Enter number of rows")
       c=int(input())
       Sample.loop5(c) 
    if m==6:
       print("Enter number of rows")
       c=int(input())
       Sample.loop6(c)
    if m==7:
       print("Enter number of rows")
       c=int(input())
       Sample.loop7(c)
    if m==8:
       print("Enter number of rows")
       c=int(input())
       Sample.loop8(c)
    if m==9:
       print("Enter number of rows")
       c=int(input())
       Sample.loop9(c)
    if m==10:
       print("Enter number of rows")
       c=int(input())
       Sample.loop10(c)
    if m==11:
       print("Enter number of rows")
       c=int(input())
       Sample.loop11(c)
    if m==12:
       print("Enter number of rows")
       c=int(input())
       Sample.loop12(c)
    if m>12:
        print("Sorry no such option") 
if n>2:
    print("Sorry no such option")