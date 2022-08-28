# cook your dish here
n=int(input())
d={}


for i in range(n):
    k=int(input())
    d[k]=0
    if k<=300:
       d[k]=300*10
    else:
       d[k]=10*k
    
    print(d[k])
    
    
       

     


    

