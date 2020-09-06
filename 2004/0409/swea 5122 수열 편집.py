import sys
sys.stdin=open('../input.txt','r')


class Node(object):
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList(object):
    def __init__(self):
        self.head=None
        self.count=0

    def append(self,node):
        if self.head==None:
            self.head=node
        else:
            cur=self.head
            while cur.next!=None:
                cur=cur.next
            cur.next=node

    def get(self,idx):
        cur=self.head
        cur_i=0
        while cur_i<idx:
            cur=cur.next
            if not cur:
                return -1
            cur_i+=1
        return cur.data


    def insert(self, idx, node):
        cur=self.head
        pre=None
        cur_i=0
        if idx==0:
            if self.head:
                nxt=self.head
                self.head=node
                self.head.next=nxt
            else:
                self.head=node
        else:
            while cur_i<idx:
                if cur:
                    pre=cur
                    cur=cur.next
                else:
                    break
                cur_i+=1
            if cur_i==idx:
                node.next=cur
                pre.next=node
            else:
                return -1

    def delete(self, idx):
        cur_i=0
        cur=self.head
        pre=None
        nxt=self.head.next
        if idx==0:
            self.head=nxt
        else:
            while cur_i<idx:
                if cur.next:
                    pre=cur
                    cur=nxt
                    nxt=nxt.next
                else:
                    break
                cur_i+=1
            if cur_i==idx:
                pre.next=nxt
            else:
                return -1

for tc in range(1,int(input())+1):
    n,m,l=map(int,input().split())
    data=[*map(int,input().split())]
    L=LinkedList()
    for i in range(n):
        L.append(Node(data[i]))
    for i in range(m):
        c=[*input().split()]
        if c[0]=='I':
            L.insert(int(c[1]),Node(int(c[2])))
        if c[0]=='D':
            L.delete(int(c[1]))
        if c[0]=='C':
            L.delete(int(c[1]))
            L.insert(int(c[1]),Node(int(c[2])))
    print('#%i'%tc,L.get(l))