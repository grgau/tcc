#!/usr/bin/python3

import csv

def createCsv(sec_incident, start, end):
    name = "incidents__" + start + "_" + end + ".csv"
    path = '../../data/new/' + start.split('-',3)[1] + '/'

    with open(path+name, "w") as csv_file:
        csv.register_dialect("custom", delimiter=",", skipinitialspace=True)
        writer = csv.writer(csv_file, dialect="custom")
        for incident in sec_incident:
            writer.writerow(incident)
    csv_file.close()

    return
