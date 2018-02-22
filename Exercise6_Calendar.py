import datetime
import time
print "Give your wanted year and month:"
print "Year:",
year = input()
print "Month:",
month = input()
while month<1 or month>12:
    print "Your given month is out of limits.Choose number between 1 and 12!"
    month = input()
given_ym = datetime.date(year,month,1)
start_num = given_ym.isoweekday()
monthinteger = month
name_month = datetime.date(1900, monthinteger, 1).strftime('%B')
print name_month,year
print 'S','\t','M','\t','T','\t','W','\t','T','\t','F','\t','S'
if start_num == 1:
    index = 2
elif start_num == 2:
    index = 3
elif start_num == 3:
    index = 4
elif start_num == 4:
    index = 5
elif start_num == 5:
    index = 6
elif start_num == 6:
    index = 7
elif start_num == 7:
    index = 1
if month <= 7:
    if month % 2 == 1:
        if start_num != 7:
            for i in range (1,32):
                if i == 1:
                    if index % 7 == 0 and index != 1:
                        print (start_num * '\t'), i, '\t'
                        index = 0
                    else:
                        print (start_num * '\t'), i, '\t',
                else:
                    if index % 7 == 0 and index != 1:
                        print i, '\t'
                        index = 0
                    else:
                        print i, '\t',
                index = index + 1
        else:
            for i in range(1, 32):
                if index % 7 == 0 and index != 1:
                    print i, '\t'
                    index = 0
                else:
                    print i, '\t',
                index = index + 1
    elif month % 2 == 0:
        if month != 2:
            if start_num != 7:
                for i in range(1, 31):
                    if i == 1:
                        if index % 7 == 0 and index != 1:
                            print (start_num * '\t'), i, '\t'
                            index = 0
                        else:
                            print (start_num * '\t'), i, '\t',
                    else:
                        if index % 7 == 0 and index != 1:
                            print i, '\t'
                            index = 0
                        else:
                            print i, '\t',
                    index = index + 1
            else:
                for i in range(1, 31):
                    if index % 7 == 0 and index != 1:
                        print i, '\t'
                        index = 0
                    else:
                        print i, '\t',
                    index = index + 1
        else:
            if year % 4 == 0:
                if start_num != 7:
                    for i in range(1, 30):
                        if i == 1:
                            if index % 7 == 0 and index != 1:
                                print (start_num * '\t'), i, '\t'
                                index = 0
                            else:
                                print (start_num * '\t'), i, '\t',
                        else:
                            if index % 7 == 0 and index != 1:
                                print i, '\t'
                                index = 0
                            else:
                                print i, '\t',
                        index = index + 1
                else:
                    for i in range(1, 30):
                        if index % 7 == 0 and index != 1:
                            print i, '\t'
                            index = 0
                        else:
                            print i, '\t',
                        index = index + 1
            else:
                if start_num != 7:
                    for i in range(1, 29):
                        if i == 1:
                            if index % 7 == 0 and index != 1:
                                print (start_num * '\t'), i, '\t'
                                index = 0
                            else:
                                print (start_num * '\t'), i, '\t',
                        else:
                            if index % 7 == 0 and index != 1:
                                print i, '\t'
                                index = 0
                            else:
                                print i, '\t',
                        index = index + 1
                else:
                    for i in range(1, 29):
                        if index % 7 == 0 and index != 1:
                            print i, '\t'
                            index = 0
                        else:
                            print i, '\t',
                        index = index + 1
elif month > 7:
    if month % 2 == 1:
        if start_num != 7:
            for i in range (1,31):
                if i == 1:
                    if index % 7 == 0 and index != 1:
                        print (start_num * '\t'), i, '\t'
                        index = 0
                    else:
                        print (start_num * '\t'), i, '\t',
                else:
                    if index % 7 == 0 and index != 1:
                        print i, '\t'
                        index = 0
                    else:
                        print i, '\t',
                index = index + 1
        else:
            for i in range(1, 31):
                if index % 7 == 0 and index != 1:
                    print i, '\t'
                    index = 0
                else:
                    print i, '\t',
                index = index + 1
    elif month % 2 == 0:
        if start_num != 7:
            for i in range(1, 32):
                if i == 1:
                    if index % 7 == 0 and index != 1:
                        print (start_num * '\t'), i, '\t'
                        index = 0
                    else:
                        print (start_num * '\t'), i, '\t',
                else:
                    if index % 7 == 0 and index != 1:
                        print i, '\t'
                        index = 0
                    else:
                        print i, '\t',
                index = index + 1
        else:
            for i in range(1, 32):
                if index % 7 == 0 and index != 1:
                    print i, '\t'
                    index = 0
                else:
                    print i, '\t',
                index = index + 1
