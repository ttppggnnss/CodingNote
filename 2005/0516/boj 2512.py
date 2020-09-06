import sys
sys.stdin=open('../input.txt', 'r')

n = int(input())
nums = [*map(int, input().split())]
end = int(input())
if sum(nums)<=end:
    ans=nums[0]
else:
    ans=sum(nums)//n
print(ans)