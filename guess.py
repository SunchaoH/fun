#! python

from random import *
target=int(uniform(1,100))
flag=1
mi=1
ma=100
n=1
score=100
SS=0
while flag == 1:
    print '\033[1;40;47m'
    print "The", n, "th guess, please input an integer number arange from:", mi, ":", ma 
    print '\033[0m'
    guess=int(input())
    tmp=int(guess)
    n=n+1
    if tmp == target:
        flag=0
    elif tmp > target:
        ma=tmp
    else:
        mi=tmp
    
    if tmp-mi>ma-tmp:
        SS=SS+(ma-tmp)/10.0
    else:
        SS=SS+(mi-tmp)/10.0


if n<= 2:
    score=100
elif n <10:
    score=score-2.5*pow(1.5,n-2) - SS
else:
    score=0

print '**********************************************************************'
print '\033[1;31;40m'
if score > 80:
    print '               Congratulation, your score is', score
elif score >60:
    print '               Not too bad, your score is', score
else:
    print '               Um, I am so sorry to tell that your score is', score
print '\033[0m'
print '**********************************************************************'
