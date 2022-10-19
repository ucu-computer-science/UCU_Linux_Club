#!/bin/bash

coef=0
for entry in $1/*
do
    echo $entry
    count=$(cat "$entry" | wc -l)
    let coef=coef+count
done
echo $coef

