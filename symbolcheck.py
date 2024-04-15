import re
file = open('C:\\Users\Patterns\Desktop\Documents\symbol_check.txt','r')
lines = file.readlines()
special_char = re.compile('[=<>%&]')
count=0
for line in lines:
    messages = line.split('VARCHAR2(100):=')
    # print(messages)
    if  special_char.search(messages[1]) == None:
        pass
    else:
        count+=1
        print(messages[1])

print(count)