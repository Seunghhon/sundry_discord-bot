#!/bin/bash

# Screen restart
screen -list
printf "Select screen to restart: "
read screen
screen -r $screen -X quit
screen -dmS $screen python3 $screen

