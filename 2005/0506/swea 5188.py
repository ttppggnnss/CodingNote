import sys
sys.stdin=open('../input.txt', 'r')

def push(i,j, res=0):
    if i==n-1 and j==n-1:
        global ans
        ans=min(res+board[i][j],ans)
        return
    if j<n-1:
        push(i,j+1,res+board[i][j])
    if i<n-1:
        push(i+1,j,res+board[i][j])

for t in range(1, int(input())+1):
    n=int(input())
    board=[[*map(int,input().split())] for _ in range(n)]
    ans=9**9
    push(0,0)
    print('#%i'%t, ans)