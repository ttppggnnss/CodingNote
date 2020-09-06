import sys
sys.stdin=open('../input.txt','r')

class Node(object):
    def __init__(self, data):
        self.data=data
        self.next=None

    def __repr__(self):
        return str(self.data)

class LinkedList(object):
    def __init__(self,*args):
        self.head=Node('head')
        self.size=0
        cur=self.head
        for i in range(len(args)):
            cur.next=Node(args[i])
            cur=cur.next
            self.size+=1

    def insert(self,idx,*args):
        cur=self.head
        for i in range(idx):
            cur=cur.next
        nxt=cur.next
        for i in range(len(args)):
            cur.next=Node(args[i])
            cur=cur.next
            self.size+=1
        cur.next=nxt

    def get(self,idx):
        if idx+1>self.size:
            return -1
        else:
            cur=self.head
            for i in range(idx+1):
                cur=cur.next
            return cur.data

    def list(self):
        result=[]
        cur=self.head
        cur=cur.next
        while cur:
            result.append(cur.data)
            cur = cur.next
        return result

    def __repr__(self):
        result = []
        cur=self.head
        while cur:
            result.append(str(cur))
            cur=cur.next
        return ' '.join(result)

for t in range(1,int(input())+1):
    n,m,k = map(int,input().split())
    LL=LinkedList(*map(int,input().split()))
    s=m
    for _ in range(k):
        if s==LL.size:
            LL.insert(LL.size,LL.get(LL.size-1)+LL.get(0))
        else:
            LL.insert(s,LL.get(s-1)+LL.get(s))
        s+=m
        if s>LL.size:
            s=s-LL.size
    print('#%i'%t,*LL.list()[::-1][:10])