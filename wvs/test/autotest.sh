#!/bin/bash 
DIR=$1 
if [ ! -n "$DIR" ] ;then 
    echo "you have not choice Application directory !" 
    exit 
fi 

fswatch $DIR | while read file 
do 
    #echo "${file} was modify" >> unittest.log 2>&1 
    echo "${file} was modify" 
    pytest -v -s -m"scan" ${file} 
done


