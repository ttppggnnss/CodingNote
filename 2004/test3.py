a='/root/hello'
print(a.find('/root'))


c=''
for i in a[::-1]:
    c+=i
    if i=='/':
        break
print(c[::-1])