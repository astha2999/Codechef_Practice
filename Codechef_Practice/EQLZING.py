# cook your dish here
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    if a>b:
       d= a-b
       if d%2==0:
           q=d/2
           a=a-q
           b=b+a-q
           print("YES")
       else:
            print("NO")
    elif b>a:
       d= b-a
       if d%2==0:
           q=d/2
           a=a+q
           b=b-q
           print("YES")
       else:
            print("NO")
    else:
        print("YES")
         
         
           
           
            
       

     


    

