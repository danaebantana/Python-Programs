import random
import string

Letters = string.ascii_uppercase
Square = [[0 for i in range(100)] for j in range(100)]
for i in range(100):
    for j in range(100):
        Square[i][j] = random.choice(Letters)

for i in range(100):
    k = 0
    for j in range(100):
        if k < 99:
            print ''.join(map(str, Square[i][j])),
            k = k + 1
        else:
            print ''.join(map(str, Square[i][j]))

words = []
file_in=open("new.txt","r")
for line in file_in:
    words.append(line)
file_in.close ()
words = map(lambda s: s.strip(), words)
length_list = len(words)

Horiz = [0 for i in range(100)]
Vertic = [0 for i in range(100)]
for i in range(100):
    x = ''
    y = ''
    for j in range(100):
        x = x + Square[i][j]
        y = y + Square[j][i]
    Horiz[i] = x
    Vertic[i] = y

Total_Sum = []
for k in range(length_list):
    HCount = []
    VCount = []
    word = words[k]
    for i in range(100):
        HCount.append(Horiz[i].count(word))
        VCount.append(Vertic[i].count(word))
    sum = 0
    for i in range(100):
        sum = sum + HCount[i] + VCount[i]
    Total_Sum.append(sum)

print 'The words that appear in the 100*100 square are:'
k = 0
for i in range(length_list):
   if Total_Sum[i] > 0:
       print words[i]
       k = k + 1
if k == 0:
    print 'No word found!'