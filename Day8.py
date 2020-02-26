import re

phoneBook = {}
queries = []

def search(queries, phoneBook) :
    result = ""
    for x in queries :
        if x not in phoneBook :
            result = "Not found"

        else :
            result = x + "=" + phoneBook[x]
        
        print(result)

#Main

n = int(input())

for _ in range(0,n) :
    str = input()       #name
    str = re.split(r'[\s]\s*', str)
    phoneBook[str[0]] = str[1]
#print(phoneBook)

for i in range (0,n):
    str = input()
    queries.append(str)

search(queries, phoneBook)
