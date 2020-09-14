# 블랙잭

# 기본 룰
# 1. 딜러가 카드를 한 장 뽑아 플레이어에게 준다.
# 2. 딜러가 카드를 한 장 뽑아 딜러 앞에 뒤집어 놓는다.
# 3. 딜러가 카드를 한 장 뽑아 플레이어에게 준다.
# 4. 딜러가 카드를 한 장 뽑아 딜러 앞에 보이도록 놓는다.
# 5. 플레이어에게 카드를 더 받을지 말지 물어본다.
#     5.1 플레이어가 최초로 받은 카드 두 장의 합이 21인 경우에는 더 이상 카드를 받지 않고, 딜러의 카드를 확인하여 승패를 결정한다.
#     5.2 플레이어가 받은 모든 카드의 합이 21보다 작으면 계속해서 한 장씩 더 받을 수 있다.
#     5.3 플레이어가 받은 모든 카드의 합이 21을 넘어가면 플레이어가 즉시 게임에서 진다.
# 6. 플레이어가 더이상 카드를 받지 않으면 딜러 앞의 뒤집어놓은 카드를 공개한 후, 딜러의 카드 합이 17 이상이 될 때까지 계속해서 딜러가 카드를 한 장씩 받는다.
#     6.1 딜러가 받은 모든 카드의 합이 21을 넘으면 딜러가 즉시 게임에서 진다.
#     6.2 이때 딜러는 플레이어가 가진 카드의 합을 고려하지 않으며, 딜러가 가진 카드의 합이 17 이상이 되면 받기를 중단한다.
# 7. 승패를 가린다. 카드 합이 21에 더 가까운 사람이 이기며, 카드 합이 서로 같으면 비긴다.

# 플레이어 전략
# 1. 딜러의 보이는 카드가 1이거나 7 이상인 경우, 플레이어는 카드 합이 17 이상이 될 때까지 받는다.
# 2. 딜러의 보이는 카드가 4, 5, 6인 경우, 플레이어는 카드를 받지 않는다.
# 3. 딜러의 보이는 카드가 2, 3인 경우, 플레이어는 카드 합이 12 이상이 될 때까지 받는다.

# 플레이어 이기면 +2점 지면 -2점 블랙잭으로 이기면 +3점
# 카드를 더 뽑을 수 없는 경우 해당 판 무효하고 현재까지의 점수 return

ex1 = [12, 7, 11, 6, 2, 12]	# 2
ex2 = [1, 4, 10, 6, 9, 1, 8, 13]	# 1
ex3 = [10, 13, 10, 1, 2, 3, 4, 5, 6, 2]	# -2
ex4 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]	# -2

def solution(cards):
    answer = 0
    new_cards = cards[::-1]

    cards = []
    for i in new_cards:
        if i<=10:
            cards.append(i)
        else:
            cards.append(10)

    while True:
        player = []
        dealer = []

        # 1
        try:
            player.append(cards.pop())
        except:
            return answer
        # 2
        try:
            dealer.append(cards.pop())
        except:
            return answer
        # 3
        try:
            player.append(cards.pop())
        except:
            return answer
        # 4
        try:
            dealer.append(cards.pop())
        except:
            return answer
        # 5-1
        player_score = sum(player)
        if player_score==21:
            answer += 2
            continue

        if 1 in player and sum(player)+10<=21:
            player_score = sum(player)+10

        if player_score==21:
            answer += 3
            continue

        # 5-2
        if dealer[1]==1 or dealer[1]>=7:
            while player_score<17:
                try:
                    player.append(cards.pop())
                except:
                    return answer
                player_score = sum(player)
                if 1 in player and sum(player) + 10 <= 21:
                    player_score = sum(player) + 10
        if dealer[1] in [4, 5, 6]:
            pass
        if dealer[1] in [2, 3]:
            while player_score<12:
                try:
                    player.append(cards.pop())
                except:
                    return answer
                player_score = sum(player)
                if 1 in player and sum(player) + 10 <= 21:
                    player_score = sum(player) + 10
        # 5-3
        if player_score>21:
            answer -= 2
            continue
        # 6
        dealer_score = sum(dealer)
        if 1 in dealer and sum(dealer)+10<=21:
            dealer_score = sum(dealer)+10
        while dealer_score<17:
            try:
                dealer.append(cards.pop())
            except:
                return answer
            dealer_score = sum(dealer)
            if 1 in dealer and sum(dealer) + 10 <=21:
                dealer_score = sum(dealer)+10
        # 6-1
        if sum(dealer)>21:
            answer += 2
            continue

        # 7
        if abs(player_score-21) > abs(dealer_score-21):
            answer -= 2
            continue
        elif abs(player_score-21) < abs(dealer_score-21):
            answer += 2
            continue

    return answer

print(solution(ex4))