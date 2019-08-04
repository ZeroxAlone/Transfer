#week2 1 不对
"""
Is your secret number 83?
Enter 'h' to indicate the guess is too high.
Enter 'l' to indicate the guess is too low.
Enter 'c' to indicate I guessed correctly. 
Game over. Your secret number was: 83
"""
"""
import random
r=random.randint(0,100)
print("Is your secret number",r,"?")
s=str(input('''Enter 'h' to indicate the guess is too high.
Enter 'l' to indicate the guess is too low.
Enter 'c' to indicate I guessed correctly.
'''))
a=r-1
b=r+1
a!=b
while 0==0:
    if s=="h":
        c=random.randint(0,a)
        c<a
        print("Is your secret number",c,"?")
        s=str(input('''Enter 'h' to indicate the guess is too high.
Enter 'l' to indicate the guess is too low.
Enter 'c' to indicate I guessed correctly.
'''))
    elif s=="l":
        c=random.randint(b,101)
        c>b
        print("Is your secret number",c,"?")

        s=str(input('''Enter 'h' to indicate the guess is too high.
Enter 'l' to indicate the guess is too low.
Enter 'c' to indicate I guessed correctly.
'''))
    elif s=="c":
        break
print("Game over. Your secret number was:",c)
"""
#question set
#1
'''
b=eval(input("balance = "))
a=eval(input("annualInterestRate = "))
m=eval(input("monthlyPaymentRate = "))
for i in range(12):
    b=(b-b*m)*(1+a/12)
print("Month 12 Remaining balance:",round(b,2))

#2
b=eval(input("balance = "))
a=eval(input("annualInterestRate = "))
for i in range(12):
    
    z=b/12-b*(1+a)/(1+a/12)
    d=(b-z*12)*(1+a/12)/12/(b*(1+a))
print("""Result Your Code Should Generate:
-------------------
Lowest Payment: """,z)
'''
#2不对 3不会

#week 2 2
#x**4
'''
def fourthPower(x):
    return x**4
x=eval(input(""))
print(fourthPower(x))
'''
#odd
'''
def odd(x):
    x:int
    a=x%2
    if a==1:
        return True
    if a==0:
        return False
x=eval(input(""))
print(odd(x))
'''
#iterPower
'''
def iterPower(base,exp):
    base:int or float
    exp:int>=0
    return base**exp
base=eval(input(""))
exp=int(input(""))
print(iterPower(base,exp))
'''
#recurPower
'''
def recurPower(base, exp):
    if exp==0:
        return 1
    return recurPower(base, exp-1)*base
base=int(input(""))
exp=int(input(""))
print(recurPower(base,exp))
'''
#gcdIter
'''
a=int(input(""))
b=int(input(""))
c=min(a,b)
l=[]
def gcdIter(a,b):
    for i in range(1,c+1):
        if a%i==0 and b%i==0:
            l.append(i)
    return max(l)
print(gcdIter(a,b))
'''
#gcdRecur 不对
'''
a=int(input(""))
b=int(input(""))
def gcdRecur(a,b):
    d=max(a,b)
    e=min(a,b)
    c=d%e
    if c==0:
        return e
    else:
        gcdRecur(a,b)
print(gcdRecur(a,b))
'''








