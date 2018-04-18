#!/usr/bin/python3
from modules.dataBuildFlowsBro import BuildFlows
from modules.csvCreate import createCsv
import sys, getopt

def main(argv):
    import modules.dates

    try:
       opts, args = getopt.getopt(argv,"hs:e:",["help","start=","end="])
    except getopt.GetoptError:
       print ("-s date\t\t: date in the format yyyy-mm-ddTHH:mm:ss.zzzZ \n-e date\t\t: date in the format yyyy-mm-ddTHH:mm:ss.zzzZ")
       print ("\n\nEXAMPLES:\n\tpython3 run.py -s 2018-04-09T23:00:00.000Z -e 2018-04-09T23:05:00.000Z\n\tpython3 run.py --start=2018-04-09T23:00:00.000Z --end=2018-04-09T23:05:00.000Z")
       sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print ("-s date\t\t: date in the format yyyy-mm-ddTHH:mm:ss.zzzZ \n-e date\t\t: date in the format yyyy-mm-ddTHH:mm:ss.zzzZ")
            print ("\n\nEXAMPLES:\n\tpython3 run.py -s 2018-04-09T23:00:00.000Z -e 2018-04-09T23:05:00.000Z\n\tpython3 run.py --start=2018-04-09T23:00:00.000Z --end=2018-04-09T23:05:00.000Z")
            sys.exit()
        elif opt in ("-s", "--start"):
            start = arg
        elif opt in ("-e", "--end"):
            end = arg

    modules.dates.start_time = start
    modules.dates.end_time = end

    incidents = BuildFlows()

    createCsv(incidents, modules.dates.start_time, modules.dates.end_time) # Cria csv de incidentes

    return True

if __name__ == "__main__":
    main(sys.argv[1:])
