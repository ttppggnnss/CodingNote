import re

for i in range(2):
    reList = re.sub('(\w{%i})' %i, '\g<1> ', 's').split()
    print(reList)