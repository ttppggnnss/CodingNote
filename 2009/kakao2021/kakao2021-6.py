# 짝맞추기

# 풀이 설계
# 1. 남아있는 짝 개수를 구한다
# 2. 현재 위치에서 각각 짝을 맞추기 위해 몇 번 이동해야 하는지 계산한다.
# 3. 남아있는 짝 개수와 이동 개수를 더한다
# 4. 그 중 최소값이 답이다.


ex1 = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],	1, 	0, 	# 14
ex2 = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]],	0,	1,	# 16

def solution(board, r, c):
    count = 0
    pair = set()
    for i in range(4):
        for j in range(4):
            if board[i][j]>0:
                count += 1
                pair.add(board[i][j])
    import itertools
    orders = itertools.permutations(list(pair), len(pair))
    for i in orders:
        print(i)
    answer = ''
    return answer

print(solution(*ex1))