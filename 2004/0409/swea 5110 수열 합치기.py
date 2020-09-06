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

for tc in range(1,int(input())+1):
    n,m=map(int,input().split())
    LL=LinkedList(*map(int,input().split()))
    for i in range(m-1):
        inp = LinkedList(*map(int,input().split()))
        for j in range(LL.size):
            if LL.get(j)>inp.get(0):
                LL.insert(j,*inp.list())
                break
        else:
            LL.insert(LL.size,*inp.list())
    print('#%i'%tc,*LL.list()[::-1][:10])