import re

for i in range(2):
    reList = re.sub('(\w{%i})' %i, '\g<1> ', 's').split()
    # print(reList)


a = list(range(1, 10))
print(a)
# b = list(zip(*a))
# print(b)

c = 'ab'
print(*c)