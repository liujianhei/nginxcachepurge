#!/bin/bash
while read line
do
    echo $line
    echo "nginx purge $line"
    echo "----------------------"
    for i in 147 148 149 166
    do
        echo "host: 10.10.99.$i"
        echo "status:`squidclient -h 10.10.99.$i -p 80 -m PURGE -v $line 2>&1 |grep "^<center>"|awk -F'[><]' '{print $5}'`"
        echo "----------------------"
    done
done < $1
