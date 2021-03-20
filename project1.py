#Basic mathmetical calculator.
#salim sadman seger

a = int(input("Enter first number:"))
b = int(input("Enter 2nd number:"))
op = input('Enter the operator:') #op=operator
#a,b,op are variabble
def add(a,b):
    result= a+b
    print(result)
def sub(a, b):
        result = a - b
        print(result)
def div(a,b):
    result= a/b
    print(result)
def mul(a,b):
    result= a*b
    print(result)
def power(a,b):
    result= a**b
    print(result) #b will be the power value
if op=='+':
    add(a,b)
elif op=='-':
    sub(a, b)
elif op=='/':
    div(a,b)
elif op=='*':
    mul(a,b)
elif op == '**':
    power(a,b)
#projrct for how to use or make function
