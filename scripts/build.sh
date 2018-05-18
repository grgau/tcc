#!/bin/bash

# First day: 14/03/2018 as 18:26:00

#Março
#for d in {15..31}; do
#  for h in {0..22}; do
#    hour_plus_one=$(printf %02d $(($h + 1)))
#    hour=$(printf %02d $(($h)))
#    echo "Building day $(date +"$d Mar %Y - $hour:00:00 to $hour_plus_one:00:00")..."; python3 ../src/run.py -s "$(date "+%Y-03-"$d"T"$hour":00:00.000Z")" -e "$(date "+%Y-03-"$d"T"$hour_plus_one":00:00.000Z")";
#  done
#done

#Abril
for d in {19..31}; do
  for h in {0..22}; do
    hour_plus_one=$(printf %02d $(($h + 1)))
    hour=$(printf %02d $(($h)))
    echo "Building day $(date +"$d Abr %Y - $hour:00:00 to $hour_plus_one:00:00")..."; python3 ../src/run.py -s "$(date "+%Y-04-"$d"T"$hour":00:00.000Z")" -e "$(date "+%Y-04-"$d"T"$hour_plus_one":00:00.000Z")";
  done
done
