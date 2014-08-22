#!/usr/bin/python

import sys
import getopt

def main():
	n, type = opt_load()
	calculator(n, type)


def opt_load():
	## Load the files in based on the command line arguments
	n = 0
	type = ""
	opts, args = getopt.getopt(sys.argv[1:], "n:t:")
	for o, a in opts:
		if o == '-n':
			n = int(a)
		elif o == '-t':
			type = a
		else:
			print script_info['usage']
			sys.exit(2)
	return(n, type)

def calculator(samples, type):
	taq = 0.5
	fprimer = 2.5
	buffer = 5.0
	water = 13.5
	if type == "RP":
		water = 9.5

	taq *= samples
	fprimer *= samples
	buffer *= samples
	water *= samples

	total = taq + fprimer + buffer + water

	print "Reagent", "\t", "Volume (ul)"
	print "Water", "\t\t", water
	print "Buffer", "\t\t", buffer
	print "F Primer", "\t", fprimer
	print "Polymerase", "\t", taq
	print "--------------------"
	print "Total", "\t\t", total

main()
