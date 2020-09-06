'''
numbers
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand
right
left
right
result
LRLLLRLLRRL
LRLLRRLLLRR
LLRLLRLLRL
'''

def solution(numbers, hand):
    answer = ''
    L=(3,0)
    R=(3,2)
    for i in numbers:
        if i in (1,4,7):
            answer+='L'
            if i==1:
                L=(0,0)
            elif i==4:
                L=(1,0)
            else:
                L=(2,0)
        elif i in (3,6,9):
            answer+='R'
            if i==3:
                R=(0,2)
            elif i==6:
                R=(1,2)
            else:
                R=(2,2)
        else:
            if i==2:
                S=(0,1)
                l=abs(L[0]-S[0])+abs(L[1]-S[1])
                r=abs(R[0]-S[0])+abs(R[1]-S[1])
                if l>r:
                    answer+='R'
                    R=S
                elif l<r:
                    answer+='L'
                    L=S
                else:
                    if hand=='right':
                        answer+='R'
                        R=S
                    else:
                        answer+='L'
                        L=S
            if i==5:
                S=(1,1)
                l=abs(L[0]-S[0])+abs(L[1]-S[1])
                r=abs(R[0]-S[0])+abs(R[1]-S[1])
                if l>r:
                    answer+='R'
                    R=S
                elif l<r:
                    answer+='L'
                    L=S
                else:
                    if hand=='right':
                        answer+='R'
                        R=S
                    else:
                        answer+='L'
                        L=S
            if i==8:
                S=(2,1)
                l=abs(L[0]-S[0])+abs(L[1]-S[1])
                r=abs(R[0]-S[0])+abs(R[1]-S[1])
                if l>r:
                    answer+='R'
                    R=S
                elif l<r:
                    answer+='L'
                    L=S
                else:
                    if hand=='right':
                        answer+='R'
                        R=S
                    else:
                        answer+='L'
                        L=S
            if i==0:
                S=(3,1)
                l=abs(L[0]-S[0])+abs(L[1]-S[1])
                r=abs(R[0]-S[0])+abs(R[1]-S[1])
                if l>r:
                    answer+='R'
                    R=S
                elif l<r:
                    answer+='L'
                    L=S
                else:
                    if hand=='right':
                        answer+='R'
                        R=S
                    else:
                        answer+='L'
                        L=S
    return answer