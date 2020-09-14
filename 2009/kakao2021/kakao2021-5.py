# 공익광고 삽입

# 풀이 설계
# 1. 전체 time 을 초 단위로 바꾼다 dict 만든다
# 2. 1초 단위로 logs 에 있는 값들을 1씩 더한다
# 3. adv_time 을 00부터 adv_time 이 최대한 들어가는 시간 까지 광고 재생 시간을 구한다
# 4. 계속 계산하면서 값이 커지면 시작 시간을 바꾼다
# 5. 시작 시간을 다시 시 분 초로 바꾼다

ex1 = "02:03:55",	"00:14:15",	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]	# "01:30:59"
ex2 = "99:59:59",	"25:00:00",	["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]	# "01:00:00"
ex3 = "50:00:00",	"50:00:00",	["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]	# "00:00:00"


def toSeconds(time):
    time = time.split(':')
    time = 3600*int(time[0]) + 60*int(time[1]) + int(time[2])
    return time

def solution(play_time, adv_time, logs):
    if play_time==adv_time:
        return "00:00:00"
    logs = sorted(logs)
    # print(logs)

    play_time_sec = toSeconds(play_time)
    # print(play_time_sec)

    adv_time_sec = toSeconds(adv_time)
    # print(adv_time_sec)

    logs_sec = []
    candi = []
    for i in logs:
        j = i.split('-')
        j[0] = toSeconds(j[0])
        j[1] = toSeconds(j[1])
        if j[0]+adv_time_sec<=play_time_sec:
            candi.append(set(range(j[0], j[0]+adv_time_sec)))
        if j[1]-adv_time_sec>=0:
            candi.append(set(range(j[1]-adv_time_sec, j[1])))
        logs_sec.append(j)

    result = 0
    answer = 0

    for i in candi:
        count = 0
        for j in logs_sec:
            count+= len(i.intersection(range(j[0]+1, j[1]+1)))
        if result<count:
            result = count
            answer = min(i)

    m, s = divmod(answer, 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)

print(solution(*ex1))

# 포기
