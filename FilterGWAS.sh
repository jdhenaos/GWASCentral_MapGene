#!/bin/bash

cut -f3 $1 | sort | uniq > .temp

for i in `cat .temp`
do
value=`grep -c $i $1`
if [ $value -ge 2 ];then
echo $i
fi
done
