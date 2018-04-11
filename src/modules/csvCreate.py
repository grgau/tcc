def createCsv(sec_incident):
    import csv
    with open("../../data/incidents-teste.csv", "w") as csv_file:
        csv.register_dialect("custom", delimiter=",", skipinitialspace=True)
        writer = csv.writer(csv_file, dialect="custom")
        for incident in sec_incident:
            writer.writerow(incident)
    csv_file.close()
