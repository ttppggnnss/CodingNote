# 아이디 수정
# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.


ex1 = "...!@BaT#*..y.abcdefghijklm"
# bat.y.abcdefghi
ex2 = "z-+.^."
# z--
ex3 = "=.="
# aaa
ex4 = "123_.def"
# 123_.def
ex5 = "abcdefghijklmn.p"
# abcdefghijklmn

def solution(new_id):

    new_id1 = new_id.lower()

    new_id2 = ''
    for i in new_id1:
        if i in 'abcdefghijklmnopqrstuvwxyz0123456789-_.':
            new_id2 += i

    while True:
        new_id3 = new_id2[:]
        new_id2 = new_id2.replace('..', '.')
        if new_id3 == new_id2:
            break

    new_id4 = new_id3.strip('.')

    if new_id4 == '':
        new_id5 = 'a'
    else:
        new_id5 = new_id4[:]

    if len(new_id5)>15:
        new_id6 = new_id5[:15].strip('.')
    else:
        new_id6 = new_id5[:]

    if len(new_id6)<3:
        new_id7 = new_id6 + new_id6[-1]
        if len(new_id7)<3:
            new_id7 = new_id7 + new_id7[-1]
    else:
        new_id7 = new_id6[:]

    return new_id7

print(solution(ex5))


# 테스트 통과
