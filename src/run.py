#!/usr/bin/python3
from modules.dataBuildFlowsBro import BuildFlows
from modules.csvCreate import createCsv

def main():
    import modules.dates
    modules.dates.start_time = '2018-04-09T23:00:00.000Z'
    modules.dates.end_time = '2018-04-09T23:05:00.000Z'

    incidents = BuildFlows()

    createCsv(incidents, modules.dates.start_time, modules.dates.end_time) # Cria csv de incidentes

    return True

if __name__ == "__main__":
    main()
