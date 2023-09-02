import sys
from unittest import result
'''
try:
    filename = sys.argv[1]
except IndexError:
    print('must enter filename')
    sys.exit()
    '''

filename = "test.asm"

try:
    f =  open(filename,'r')
except Exception:
    print("file does not exist")
    sys.exit()

source = f.read()
f.close()


parsedScript = []
lines = source.split('\n')

try:
    while True:
        lines.remove('')
except ValueError:
    pass


for line in lines:
    parsedScript.append(line.split(" "))

    for i,element in reversed(list(enumerate(parsedScript[-1]))):
        if element == '':
            del parsedScript[-1][i]

    if parsedScript[-1][0] == parsedScript[-1][0].upper():
        parsedScript[-1].insert(0,'')
    
    if len(parsedScript[-1]) == 2:
        parsedScript[-1].append('')

print(parsedScript)
    
h = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def binary(num,length):
    result = ""
    for i in range(length):
        result += str(num%2)
        num //= 2
    return result

def hexideci(num,length):
    result = ""
    for i in range(length):
        result += h[num%16]
        num //= 16
    return result


def padTo(string,length):
    string2 = string
    while len(string2) < length:
        string2 += " "
    return string2



instructionSet = {"HLT":0,"LDA":1,"STA":2,"ADD":3,"SUB":4,"BRA":5,"BRZ":6}

maxMemory = 32
memory = [0 for i in range(maxMemory)]
locations = {}

for i,line in enumerate([line for line in parsedScript if line[1] == "DAT"]):
    if line[2]:
        memory[-i-1] = binary(int(line[2]),8)
    else:
        memory[-i-1] = binary(int(0),8)
    locations[line[0]] = maxMemory-1-i

for i,line in enumerate([line for line in parsedScript if line[1] != "DAT"]):
    if line[0] != '':
        locations[line[0]] = i+1

print(locations)

for i,line in enumerate([line for line in parsedScript if line[1] != "DAT"]):
    try:
        memory[i+1] = binary(instructionSet[line[1]],3)+binary(locations[line[2]],5)
    except KeyError:
        memory[i+1] = binary(instructionSet[line[1]],3)+binary(int(line[2]),5)


f = open('out.txt','w+')

print("b10:b16:b2  - data")
for i in range(maxMemory):
    print(f"{padTo(str(i),2)}:{hexideci(i,2)}:{binary(i,5)} - {memory[i]}")
    f.write(f"{padTo(str(i),2)}:{hexideci(i,2)}:{binary(i,5)} - {memory[i]}\n")

f.close()
    
