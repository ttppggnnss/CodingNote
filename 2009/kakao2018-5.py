# 캐시
# 2020/09/11 00:00 ~00:30?

#    캐시크기(cacheSize)	    도시이름(cities)	                                                                                                    실행시간
ex1 = 3,	                ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']	                        # 50
ex2 = 3,	                ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']	                                # 21
ex3 = 2,	                ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']	# 60
ex4 = 5,	                ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']	# 52
ex5 = 2,	                ['Jeju', 'Pangyo', 'NewYork', 'newyork']	                                                                        # 16
ex6 = 0,	                ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']	                                                                    # 25


# 입력 형식
# 캐시 크기(cacheSize)와 도시이름 배열(cities)을 입력받는다.
# cacheSize는 정수이며, 범위는 0 ≦ cacheSize ≦ 30 이다.
# cities는 도시 이름으로 이뤄진 문자열 배열로, 최대 도시 수는 100,000개이다.
# 각 도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자로 구성되며, 대소문자 구분을 하지 않는다. 도시 이름은 최대 20자로 이루어져 있다.

# 출력 형식
# 입력된 도시이름 배열을 순서대로 처리할 때, 총 실행시간을 출력한다.

# 조건
# 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.
# cache hit일 경우 실행시간은 1이다.
# cache miss일 경우 실행시간은 5이다.

# 풀이 설계
# 0. 대소문자 구분 안하니까 도시를 전부 소문자로 바꿔준다
# 1. 캐시 크기에 따라 리스트에 빈 문자열을 집어넣는다.
# 2. 도시 이름을 입력받는다.
# 3. 캐시 크기를 초과하지 않으면
#       중복된 것이 없으면 5 더하고 비어있는 부분에 순서대로 채운다
#       중복된 것이 있으면 1 더하고 다음 도시로 넘어간다 (중복된 도시를 삭제하고 마지막에 append 한다)
# 4. 캐시 크기 초과하면
#       중복된 것 있으면 1 더하고 다음 도시로 넘어간다
#       중복된 것 없으면 제일 처음에 나온 도시를 삭제하고 pop(0) 마지막에 append 한다




def solution(cacheSize, cities):
    answer = 0

    if cacheSize == 0:
        return 5*len(cities)

    DB = ['']*cacheSize

    new_cities = [i.lower() for i in cities]

    for city in new_cities:
        if city in DB:
            answer += 1
            DB.remove(city)
            DB.append(city)
            continue
        else:
            if DB.count('')>0:
                num = DB.index('')
                DB[num] = city

            else:
                DB.pop(0)
                DB.append(city)
            answer += 5

    return answer

print(solution(*ex6))


# 참고할 만한 풀이
# def solution(cacheSize, cities):
#     import collections
#     cache = collections.deque(maxlen=cacheSize)
#     time = 0
#     for i in cities:
#         s = i.lower()
#         if s in cache:
#             cache.remove(s)
#             cache.append(s)
#             time += 1
#         else:
#             cache.append(s)
#             time += 5
#     return time