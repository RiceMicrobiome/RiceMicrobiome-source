#!/usr/bin/python

import sys
import getopt

def main():


def opt_load():


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

	output = 

