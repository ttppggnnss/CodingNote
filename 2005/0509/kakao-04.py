board=[[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]


def solution(board):
    n=len(board)
    visit = [i[:] for i in board]
    for i in range(n):
        if visit[0][i]==0:
            visit[0][i]=i*100
        else:
            break
    for j in range(n):
        if visit[j][0]==0:
            visit[j][0]=j*100
        else:
            break
    for i in range(1,n-1):
        visit[i][n-i]=
    print(visit)

    return

print(solution(board))