# 택시 합승

# 풀이 설계
# 1. 모든 점에 대해서
# 2. 그 점에서 A, B, S 까지의 각각 최소 값을 구한다 (다익스트라 ?)
# 3. 전체 합의 최소값이 답이 된다

# 나중에 코드 다시 봐야겠다
# 다익스트라 복붙한거라 코드를 정확하게 이해해볼 필요 있을 듯



#     n,        s,      a,      b,      fares,                                                                                                          # result
ex1 = 6,    	4,  	6,  	2,  	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]	    # 82
ex2 = 7,    	3,  	4,  	1,  	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]	                                                        # 14
ex3 = 6,    	4,  	5,  	6,  	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]	                                    # 18

import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances

def solution(n, s, a, b, fares):
    answer = []

    graph = {i:{} for i in range(1, n+1)}
    # print(graph)
    for i in fares:
        graph[i[0]][i[1]]=i[2]
        graph[i[1]][i[0]]=i[2]

    for i in range(1, n+1):
        distance=dijkstra(graph, i)
        result = distance[s]+distance[a]+distance[b]
        answer.append(result)

    return min(answer)



print(solution(*ex1))


# 정확성 통과
# 효율성 통과

