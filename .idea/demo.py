import math

def p(d1,k):
    c=d1-1
    print("Interval of the domain=[",d1,",",k,"]")
    print("Domain",'\t',"Range")
    while c<k:  
        c=c+1
        d=c             #d:=domain
        r=f(d)          #r:=range

        print(d,'\t',r)
        
def f(x):

    y=math.pow(x,2)-4

    return y

