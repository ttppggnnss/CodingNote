# 오픈채팅방
# 200911 21:27 ~

# 풀이 설계
# 1. record 를 입력 받아서 split 해준다
# 2. Enter / Leave 를 구분하고 uid 구분하고 닉네임을 구분한다
# 3. uid 를 관리하는 dict 를 만들어서 dict[uid]=닉네임 으로 관리한다
# 4. 마지막 까지 입력받은 후에 전체를 record 와 dict 를 활용하여 출력한다


ex1 = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# result
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]


def solution(record):
    uid_dict = dict()
    answer = []
    for i in record:
        try:
            behavior, uid, nickname = i.split()
            uid_dict[uid] = nickname
        except:
            behavior, uid = i.split()

    for i in record:
        try:
            behavior, uid, nickname = i.split()
        except:
            behavior, uid = i.split()

        if behavior == 'Enter':
            answer.append(uid_dict[uid]+ '님이 들어왔습니다.')
        elif behavior == 'Change':
            pass
        else:
            answer.append(uid_dict[uid]+ '님이 나갔습니다.')
    return answer

print(solution(ex1))