#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo usage: $0 "<"enter file">"
    exit
fi

python3 backtracking.py $1
