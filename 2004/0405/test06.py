directory = [
"/",
"/hello",
"/hello/tmp",
"/root",
"/root/abcd",
"/root/abcd/etc",
"/root/abcd/hello"
]

command = [
"mkdir /root/tmp",
"cp /hello /root/tmp",
"rm /hello"
]

# result = [
# "/",
# "/root",
# "/root/abcd",
# "/root/abcd/etc",
# "/root/abcd/hello",
# "/root/tmp",
# "/root/tmp/hello",
# "/root/tmp/hello/tmp"
# ]

def solution(directory, command):
    answer = directory[:]
    for i in command:
        o = i.split()
        if o[0]=='mkdir':
            answer.append(o[1])
        if o[0]=='cp':
            directory2=[i.lstrip('o[1]') for i in answer if i.find(o[1])==0]
            for k in directory2:
                if o[2]=='/':
                    answer.append(k)
                else:
                    answer.append(o[2]+k)
        if o[0]=='rm':
            answer=[i for i in answer if i.find(o[1])!=0]
    return sorted(answer)

print(solution(directory,command))