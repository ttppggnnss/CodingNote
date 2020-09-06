directory=[
"/"
]
command = [
"mkdir /a",
"mkdir /a/b",
"mkdir /a/b/c",
"cp /a/b /",
"rm /a/b/c"
]

# result = [
# "/",
# "/a",
# "/a/b",
# "/b",
# "/b/c"
# ]

def lastdir(a):
    c=''
    for i in a[::-1]:
        c+=i
        if i=='/':
            break
    return c[::-1]

def solution(directory, command):
    answer = directory[:]
    for i in command:
        o = i.split()
        if o[0]=='mkdir':
            answer.append(o[1])
        if o[0]=='cp':
            directory2=[(lastdir(o[1])+'/'+i.lstrip(o[1])).rstrip('/') for i in answer if i.find(o[1])==0]
            for k in directory2:
                if o[2]=='/':
                    answer.append(k)
                else:
                    answer.append(o[2]+k)
        if o[0]=='rm':
            answer=[i for i in answer if i.find(o[1])!=0]
    return sorted(answer)

print(solution(directory,command))