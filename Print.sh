#!/bin/bash

cd 1
for file in `ls`
do
    echo $file
    lpr -o page-left=70 -o page-right=35 -o page-bottom=17 -p $file
done

