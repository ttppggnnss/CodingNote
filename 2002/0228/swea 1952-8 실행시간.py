# 실행시간
for t in range(int(input())):
    cost = list(map(int, input().split()))
    monthly = list(map(int, input().split()))
    min_cost = cost[3]

    cost_list = [0] * 13
    for i in range(12):
        if monthly[i] * cost[0] > cost[1]:
            cost_list[i + 1] = cost_list[i] + cost[1]
        else:
            cost_list[i + 1] = cost_list[i] + cost[0] * monthly[i]

    last_cost = [0] * 13
    last_cost[:3] = cost_list[:3]
    for i in range(2, 12):
        last_cost[i + 1] = min(cost_list[i + 1], last_cost[i - 2] + cost[2],
                               cost_list[i + 1] - cost_list[i] + last_cost[i])

    print('#{0} {1}'.format(t + 1, min(min_cost, last_cost[-1])))