def calculate(x,y):
    if c=='+':
        val=a+b
    elif c=='-':
        val=a-b
    elif c=='*':
        val=a*b
    elif c=='/':
        val=a/b
    else:
        print('invalid operator')






a=int(input())
b=int(input())
c=input("Enter operator\n")
calculate(a,b)
d=int(input())
if d!=None:
    while True:
        calculate(d,val)
print('value=',val)