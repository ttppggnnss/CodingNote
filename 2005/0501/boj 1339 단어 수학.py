import sys
sys.stdin=open('../input.txt','r')

N = int(input())
lst = []
maxl = 0
for n in range(N):
    temp = input()
    lst.append(temp)
    maxl = max(len(temp), maxl)
lst.sort(key=lambda x: len(x), reverse=True)

order = dict()
mul = 10 ** (maxl-1)
for i in range(-maxl,0):
    for char in lst:
        try:
            if order.get(char[i]):
                order[char[i]] += 1 * mul
            else:
                order[char[i]] = 1 * mul
        except:
            pass
    else:
        mul //= 10

orderlist = list(order.items())
orderlist.sort(key=lambda x: x[1], reverse=True)
resultdict = dict()
idx = 9
for letter, val in orderlist:
    resultdict[letter] = idx
    idx -= 1

result = 0
for word in lst:
    temp = 0
    for letter in word:
        temp *= 10
        temp += resultdict.get(letter)
    result += temp

print(result)