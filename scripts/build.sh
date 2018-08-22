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
#for d in {01..31}; do
#  for h in {0..22}; do
#    hour_plus_one=$(printf %02d $(($h + 1)))
#    hour=$(printf %02d $(($h)))
#    echo "Building day $(date +"$d Abr %Y - $hour:00:00 to $hour_plus_one:00:00")..."; python3 ../src/run.py -s "$(date "+%Y-04-"$d"T"$hour":00:00.000Z")" -e "$(date "+%Y-04-"$d"T"$hour_plus_one":00:00.000Z")";
#  done
#done

#Maio
#for d in {1..31}; do
#  for h in {0..22}; do
#    hour_plus_one=$(printf %02d $(($h + 1)))
#    hour=$(printf %02d $(($h)))
#    day=$(printf %02d $(($d)))
#    echo "Building day $(date +"$day Mai %Y - $hour:00:00 to $hour_plus_one:00:00")..."; python3 ../src/run.py -s "$(date "+%Y-05-"$day"T"$hour":00:00.000Z")" -e "$(date "+%Y-05-"$day"T"$hour_plus_one":00:00.000Z")";
#  done
#done

#Junho
for d in {1..30}; do
  for h in {0..22}; do
    hour_plus_one=$(printf %02d $(($h + 1)))
    hour=$(printf %02d $(($h)))
    day=$(printf %02d $(($d)))
    echo "Building day $(date +"$day Jun %Y - $hour:00:00 to $hour_plus_one:00:00")..."; python3 ../src/run.py -s "$(date "+%Y-06-"$day"T"$hour":00:00.000Z")" -e "$(date "+%Y-06-"$day"T"$hour_plus_one":00:00.000Z")";
  done
done

#Julho
for d in {1..31}; do
  for h in {0..22}; do
    hour_plus_one=$(printf %02d $(($h + 1)))
    hour=$(printf %02d $(($h)))
    day=$(printf %02d $(($d)))
    echo "Building day $(date +"$day Jul %Y - $hour:00:00 to $hour_plus_one:00:00")..."; python3 ../src/run.py -s "$(date "+%Y-07-"$day"T"$hour":00:00.000Z")" -e "$(date "+%Y-07-"$day"T"$hour_plus_one":00:00.000Z")";
  done
done

#Agosto
for d in {1..31}; do
  for h in {0..22}; do
    hour_plus_one=$(printf %02d $(($h + 1)))
    hour=$(printf %02d $(($h)))
    day=$(printf %02d $(($d)))
    echo "Building day $(date +"$day Ago %Y - $hour:00:00 to $hour_plus_one:00:00")..."; python3 ../src/run.py -s "$(date "+%Y-08-"$day"T"$hour":00:00.000Z")" -e "$(date "+%Y-08-"$day"T"$hour_plus_one":00:00.000Z")";
  done
done

