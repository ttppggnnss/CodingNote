import sys
sys.stdin=open('../input.txt','r')

def test(x, g):
    if closeEnough(g*g, x/g):
        return g
    else:
        return test(x, betterGuess(x, g))

def closeEnough(a,b):
    return abs(a-b) < 0.1

def betterGuess(x,g):
    return ((g*g + x/g) /2)

for t in range(1,int(input())+1):
    n=input();n2=len(n);n=int(n)
    ans=test(n,n//(2*10**(n2//3)))
    print('#%i'%t,ans)