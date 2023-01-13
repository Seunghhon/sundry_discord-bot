#!/bin/bash

while true; do
    ls | grep .py
    printf "Select a filename to run: "
    read filename
    if [ -f $filename ]; then
        break
    else
        printf "File not found"
    fi
done

screen -dmS $filename python3 $filename

