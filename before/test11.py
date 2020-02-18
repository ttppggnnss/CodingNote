import sys;sys.stdin=open("input11.txt","r")
import time
# start = time.time()  # 시작 시간 저장

#input()
sentence=input()
n=len(sentence)
pi=[-1,0]
start=0
for i in range(n-1):
    if sentence[start]==sentence[i+1]:
        start+=1
        pi.append(start)
    else:
        start=0
        if sentence[start]==sentence[i+1]:
            while sentence[start]==sentence[i+1]:
                start+=1
        pi.append(start)
print(n-pi[-1])
print(pi)
print(n)

# print("time :", time.time()-start)  # 현재시각 - 시작시간 = 실행 시간