#!/bin/bash 
DIR=$1 
if [ ! -n "$DIR" ] ;then 
    echo "you have not choice Application directory !" 
    exit 
fi 

#php easyswoole stop php easyswoole start --d 
fswatch $DIR | while read file 
do 
    #echo "${file} was modify" >> unittest.log 2>&1 
    echo "${file} was modify" 
    pytest -v -s -m"scan" ${file} 
    #php easyswoole reload 
done


