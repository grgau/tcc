#!/usr/bin/python3

from modules.dataBuildFlows import BuildFlows
from modules.csvCreate import createCsv
from modules.ml.classifyData import classify
import sys, getopt
import os

def main(argv):
	import modules.dates

	os.system('clear')

	start = None
	end = None
	cl = None
	dataset = '/home/pedroh/dataset_2018.csv'

	try:
		opts, args = getopt.getopt(argv,"hs:e:c",["help","start=","end=","classify"])
	except getopt.GetoptError:
		print ("-s date\t\t: date in the format yyyy-mm-ddTHH:mm:ss.zzzZ \n-e date\t\t: date in the format yyyy-mm-ddTHH:mm:ss.zzzZ")
		print ("\n\nEXAMPLES:\n\tpython3 run.py -s 2018-04-09T23:00:00.000Z -e 2018-04-09T23:05:00.000Z\n\tpython3 run.py --start=2018-04-09T23:00:00.000Z --end=2018-04-09T23:05:00.000Z\n\t python3 run.py -c\n\t python3 run.py --classify")
		sys.exit(2)

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print ("-s date\t\t: date in the format yyyy-mm-ddTHH:mm:ss.zzzZ \n-e date\t\t: date in the format yyyy-mm-ddTHH:mm:ss.zzzZ")
			print ("\n\nEXAMPLES:\n\tpython3 run.py -s 2018-04-09T23:00:00.000Z -e 2018-04-09T23:05:00.000Z\n\tpython3 run.py --start=2018-04-09T23:00:00.000Z --end=2018-04-09T23:05:00.000Z\n\t python3 run.py -c\n\t python3 run.py --classify")
			sys.exit()
		elif opt in ("-s", "--start"):
			start = arg
		elif opt in ("-e", "--end"):
			end = arg
		elif opt in ("-c", "--classify"):
			cl = arg

	if cl is None and start is not None and end is not None:
		modules.dates.start_time = start
		modules.dates.end_time = end
		dataToClassify = BuildFlows()
		createCsv(dataToClassify, modules.dates.start_time, modules.dates.end_time) # Cria csv de incidentes
	elif start is None and end is None and cl is not None:
		classify(dataset)
	else:
		modules.dates.start_time = start
		modules.dates.end_time = end
		dataToClassify = BuildFlows()
		createCsv(dataToClassify, modules.dates.start_time, modules.dates.end_time) # Cria csv de incidentes
		classify(dataset)

	return True

if __name__ == "__main__":
	main(sys.argv[1:])
