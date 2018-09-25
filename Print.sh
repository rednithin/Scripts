#!/bin/bash

for file in `ls`
do
    if [ "$file" != Print.sh ] ; then
        echo $file
        lpr -o page-left=55 -o page-right=25 -o page-bottom=17 -p $file
    fi
done

