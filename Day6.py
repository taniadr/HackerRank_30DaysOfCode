# Enter your code here. Read input from STDIN. Print output to STDOUT
def quebra(wordsSet):
    for x in wordsSet :
        auxLine = x
        even = ""
        odd = ""
        #print ('Case: ', x)
        for i in range (0,len(auxLine)) :
            if i%2 == 0:
                even += auxLine[i]
            else:
                odd += auxLine[i]
        print(even, odd)

arrayList = []
readNLines = int(input())
while readNLines > 0 :
    line = input()
    if (line):
        arrayList.append(line)
    readNLines -= 1
quebra(arrayList[:])

