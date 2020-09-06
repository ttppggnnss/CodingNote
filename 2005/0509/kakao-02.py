expression='100-200*300-500+20'
'''
expression
"100-200*300-500+20"	
"50*6-3*2"
result
60420
300
'''


def solution(expression):
    answer = 0
    numbers=[]
    op=[]
    a=''
    for i in expression:
        if i in '+-*':
            op.append(i)
            numbers.append(a)
            a=''
        else:
            a+=i
    numbers.append(a)
    def plus(numbers):
        numbers2=numbers[:]
        while '+' in op:
            a=op.index('+')
            op.pop(a)
            numbers2[a]=str(int(numbers2[a])+int(numbers2.pop(a+1)))
        return numbers2
    def minus(numbers):
        numbers2 = numbers[:]
        while '-' in op:
            a=op.index('-')
            op.pop(a)
            numbers2[a]=str(int(numbers2[a])-int(numbers2.pop(a+1)))
        return numbers2
    def multi(numbers):
        numbers2 = numbers[:]
        while '*' in op:
            a=op.index('*')
            op.pop(a)
            numbers2[a]=str(int(numbers2[a])*int(numbers2.pop(a+1)))
        return numbers2
    op2=op[:]
    a1=abs(int(plus(minus(multi(numbers)))[0]))
    op=op2[:]
    a2=abs(int(plus(multi(minus(numbers)))[0]))
    op=op2[:]
    a3=abs(int(minus(multi(plus(numbers)))[0]))
    op=op2[:]
    a4=abs(int(minus(plus(multi(numbers)))[0]))
    op=op2[:]
    a5=abs(int(multi(plus(minus(numbers)))[0]))
    op=op2[:]
    a6=abs(int(multi(minus(plus(numbers)))[0]))
    answer=max(a1,a2,a3,a4,a5,a6)
    return answer
print(solution(expression))