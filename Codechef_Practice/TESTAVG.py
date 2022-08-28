n = int(input())

def av(x,y):
    average = (x+y)/2
    return average
for i in range(n):
    a,b,c=map(int,input().split())
    if av(a,b)<35:
        print("Fail")
    elif av(b,c)<35:
        print("Fail")
    elif av(a,c)<35:
        print("Fail")
    else:
        print("Pass")
    
    
