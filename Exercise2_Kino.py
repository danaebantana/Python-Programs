import urllib2
import json
import datetime

print 'KINOOOO'
print 'Pick your numbers!'
j = 0
players_picks = []
for i in range(1, 11):
    print "No.", i,
    if divmod(j, 5) == 0 and j != 1:
        x = input()
        while x < 1 or x > 80:
            print "Your numbers must be between 1 and 80. Pick an other number!"
            x = input()
        players_picks.append(x)
    else:
        point_one = 1
        point_two = 0
        x = input()
        while point_one == 1:
            while x < 1 or x > 80:
                print "Your numbers must be between 1 and 80.Give number again!"
                x = input()
            for p in range(j, 0, -1):
                if x == players_picks[p - 1]:
                    point_two = 1
            if point_two == 1:
                print 'You have already picked this number. Pick an other number!'
                x = input()
                point_two = 0
            else:
                point_one = 0
        players_picks.append(x)
    j = j + 1
print 'Your picks are:', players_picks

tday = datetime.datetime.now()
tday_day = tday.day

def compare (l1,l2):
    count = 0
    for i in l1:
        if i in l2:
            count +=1
    return count

num_picks = []
date_picks = []

for i in range(tday_day-1):
    tday = tday - datetime.timedelta(days=1)
    date_str = tday.strftime("%d-%m-%Y")
    url = 'http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    data = json.loads(data)
    lottery_picks = data['draws']['draw']
    daypicks = []
    for k in lottery_picks:
        rslts = k["results"]
        daypicks.append(compare(players_picks, rslts)) #vazei se mia lista poses pitixies eixe ana klhrvsh pou einai 12 klhrwseis thn wra gia 15 vres thn hmera!
    sum = 0
    for i in range(180):
        if daypicks[i] > 4:
            sum = sum + 1
    num_picks.append(sum)
    date_picks.append(date_str)
max = 0
for i in range(tday_day-1):
    if num_picks[i]>max:
        max = num_picks[i]
        index_max = i

print 'The day with the most successful guessings is:', date_picks[index_max], 'with:', num_picks[index_max], 'successful guessings!'
