#!/bin/bash

cut -f3 $1 | sort | uniq > .temp

for i in `cat .temp`
do
grep -m 1 $i $1 >> GWAS_Uniq.txt
done

sort GWAS_Uniq.txt
rm .temp

