import re

phoneBook = {}
queries = []

def search(queries, phoneBook) :
    result = ""
    for x in queries :
        if x not in phoneBook :
            print("Not found")

        else :
            print(f"{x}={phoneBook[x]}")
            #result = x + "=" + phoneBook[x]
        
        #print(result)

#Main

n = int(input())

for _ in range(0,n) :
    str = input()       #name
    str = re.split(r'[\s]\s*', str)
    phoneBook[str[0]] = int(str[1])
#print(phoneBook)

str.clear()

while True:
    try:
        str = input()
        queries.append(str)
    except EOFError: 
        break

search(queries, phoneBook)