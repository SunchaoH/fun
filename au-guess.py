#! python

from random import *
NN=100
for count in range(1,NN):
   flag=1
   mi=1
   ma=100
   target=int(uniform(1,100))
   n=1
   score=100
   SS=0
   while flag == 1:
       guess=int(uniform(mi,ma))
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
   print "count = %d, score = %5.2f, n = %d" %(count, score, n)
