import random
print "LET'S PLAY BINGOOOOO"
sum = 0
for h in range (1000):
    NUMS = [i for i in range (1,81)]
    PLAYERS_PICKS = []
    LIST = []
    r = 0
    for i in range(100):
        list = [i for i in range(1, 81)]
        random.shuffle(list)
        for i in range(5):
            PLAYERS_PICKS.append(list.pop())
        LIST.append([PLAYERS_PICKS[0 + r], PLAYERS_PICKS[1 + r], PLAYERS_PICKS[2 + r], PLAYERS_PICKS[3 + r],PLAYERS_PICKS[4 + r]])
        r = r + 5
    print LIST
    random.shuffle(NUMS)
    flag = 0
    CHOSEN = []
    count = 4
    while flag == 0 :
        count = count + 1
        if count == 5:
            for i in range(5):
                CHOSEN.append(NUMS.pop())
            print "The first 5 numbers are:",CHOSEN
        else:
            x = NUMS.pop()
            CHOSEN.append(x)
            print "The",count,"th number is:", x
        num_chosen = len(CHOSEN)
        for i in range(100):
            k=0
            for w in range (5):
                for j in range(num_chosen):
                    if LIST[i][w] == CHOSEN[j]:
                        k = k+1
            if k == 5:
                flag = 1
                winning_player = i + 1
    if flag == 1:
        print 'Player no.',winning_player,': BINGO'
    sum = sum + count
print "The average of numbers that have to be announced in order to 'BINGO' in 1000 games is:", sum / 1000

