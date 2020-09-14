# 비밀지도
# 200911 21:05 ~ 21:23

# 풀이 설계
# 0. n 을 확인해서 몇자리 2진수인지 결정한다
# 1. 두 배열에서 각각의 숫자를 2진수로 바꾼다
# 2. 두 배열에서 하나라도 1이면 1 아니면 0 연산을 해주는 새로운 배열을 만든다 ( or 사용하면 될듯 )
# 3. 1이면 # 0이면 공백으로 해서 새로운 배열을 출력한다



#       n       arr1                        arr2                        출력
ex1 =   5,      [9, 20, 28, 18, 11],        [30, 1, 21, 17, 28]         # ["#####","# # #", "### #", "# ##", "#####"]
ex2 =   6,      [46, 33, 33 ,22, 31, 50],   [27 ,56, 19, 14, 14, 10]    # ["######", "### #", "## ##", " #### ", " #####", "### # "]

def num_to_bin(n, num):
    new_num = num
    arr=[]
    for i in range(n):
        quotient, remainder  = divmod(new_num, 2)
        arr.append(remainder)
        new_num = quotient
    return arr[::-1]

# print(num_to_bin(5, 20))

def solution(n, arr1, arr2):
    new_arr1 = [num_to_bin(n, i) for i in arr1]
    new_arr2 = [num_to_bin(n, i) for i in arr2]

    answer = [[' ']* n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if new_arr1[i][j] or new_arr2[i][j]:
                answer[i][j]='#'
    answer = [''.join(i) for i in answer]
    return  answer

print(solution(*ex2))