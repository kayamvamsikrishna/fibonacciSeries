def isFibonacci(a,b,n):
    if n==1:
        print(a,' ',end='')
    elif n==2:
        print(a,' ',b,' ',end='')
    else:
        for i in range(n-2):
            c=a+b
            print(c,' ',end='')
            a,b=b,c
if __name__=='__main__':
    a=int(input('Enter first value='))
    b=int(input('Enter second value='))
    n=int(input('Enter Count='))
    isFibonacci(a,b,n)