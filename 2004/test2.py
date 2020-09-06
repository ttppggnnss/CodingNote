sticker=[[1,2],[3,4]]
sticker2=[list(i) for i in zip(*sticker[::-1])]
sticker3=list(zip(*sticker))[::-1]
for i in sticker:
    print(*i)
print()
for i in sticker2:
    print(*i)
print()
for i in sticker3:
    print(*i)

print('1'=='1'=='1'=='1')
print('x'+'1'+'x'+'0')