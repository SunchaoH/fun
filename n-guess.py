#! python

from random import *
NN=1000000
from numpy import *
dis=zeros(40)
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

   dis[n-1]=dis[n-1]+1

for i in range (0,40):
    print i+1, dis[i]
