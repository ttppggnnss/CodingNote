import sys
sys.stdin=open('../input.txt','r')

class Node(object):
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=Node('head')
        self.length=0

    def insert(self,idx,datum):
        cur=self.head
        for i in range(idx):
            cur=cur.next
        new=Node(datum)
        new.next=cur.next
        cur.next=new
        self.length+=1

    def get(self,idx):
        if idx+1>self.length:
            return -1
        else:
            cur=self.head
            for i in range(idx+1):
                cur=cur.next
            return cur.data

for t in range(1,int(input())+1):
    n,m,l=map(int,input().split())
    L=LinkedList()
    data=[*map(int,input().split())]
    for i in range(n):
        L.insert(i,data[i])
    for i in range(m):
        idx,datum=map(int,input().split())
        L.insert(idx,datum)
    print('#%i'%t,L.get(l))