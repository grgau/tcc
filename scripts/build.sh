#!/bin/bash

# First day: 14/03/2018 as 18:26:00

#Março
for d in {14..31}; do echo "Building day $(date +"$d Mar %Y")..."; python3 ../src/run.py -s "$(date "+%Y-03-"$d"T00:00:00.000Z")" -e "$(date "+%Y-03-"$d"T23:59:59.000Z")"; done &

#Abril
for d in {01..30}; do echo "Building day $(date +"$d Abr %Y")..."; python3 ../src/run.py -s "$(date "+%Y-04-"$d"T00:00:00.000Z")" -e "$(date "+%Y-04-"$d"T23:59:59.000Z")"; done &
