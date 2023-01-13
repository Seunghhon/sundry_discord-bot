#!/bin/bash

screen -list
printf "Select to return to the screen: "
read screen_name
screen -r "$screen_name"

