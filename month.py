import datetime
import math
def leapYear(year):
    if (year%4 ==0 and year%100 !=0) or (year%100 !=0 and year%400 ==0):
        c=1
    else:
        c=0
    return c

a=datetime.datetime.now().strftime('%Y %m %d')
[b,c,d]=a.split()
year = int(b)
month=int(c)
day=int(d)


mdic=[31, 28, 31, 30 ,31, 30, 31, 31, 30 , 31 ,30 ,31]
#year=input("year\n")
#month=input("month\n")
#day=input("day\n")
totalDay=0
for i in range(0,month-1):
    totalDay=mdic[i]+totalDay
totalDay=totalDay+day

if month >3 :
    totalDay=totalDay+leapYear(year)
print "Date:" , day, "/", month, "/", year
print "totalDay=", totalDay
