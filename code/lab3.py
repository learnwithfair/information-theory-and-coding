import string

message = 'AABABBBABAABABBBABBABB'
dictionary = {}
tmp, i, last = '', 1, 0
Flag = True
for x in message:
    tmp += x
    Flag = False
    if tmp not in dictionary.keys():
        dictionary[tmp] = i
        tmp = ''
        i += 1
        Flag = True

if not Flag:
    last = dictionary[tmp]

res = []
for char, idx in dictionary.items():
    tmp, s = '', ''
    for x, j in zip(char[:-1], range(len(char))):
        tmp += x
        if tmp in dictionary.keys():
            take = dictionary[tmp]
            s = str(take) + char[j + 1:]
    if len(char) == 1:
        s = char
    res.append(s)
if last:
    res.append(str(last))

alphabet = string.ascii_uppercase
mark = dict(zip(alphabet, range(len(alphabet))))

final_res = []
for x in res:
    tmp = ""
    for char in x:
        if char.isalpha():
            tmp += bin(mark[char])[2:]
        else:
            tmp += bin(int(char))[2:]
    final_res.append(tmp)
   

print(res)

# Find the length of the longest binary string
max_size = max(len(binary_str) for binary_str in final_res)
encoded_res = []
for x in final_res:
    encoded_res.append(x.zfill(max_size))    
print("Encoded: ", encoded_res)
