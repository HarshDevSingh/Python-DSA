def fib(n):
    count=0
    n1,n2=0,1
    num=0
    while count < n and n>1 and int(n)==n:
        num=n1+n2
        n1,n2=n2,num
        count +=1
    else:
        print("only positive integer is expected")
    return num
print(fib(10))

def fibr(n):
    if n==1 or n==0:
        return n
    else:
        return fibr(n-1)+fibr(n-2)

print(fibr(11))
