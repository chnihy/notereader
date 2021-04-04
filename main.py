#! python
# main
"""TODO: 
- QA/Test and error log:
	7/8 is fucked
- Triplets
- Basslines/Hand Patterns = Alberti, Hannons, 
- recycle repeats: so if sample < measure, the same note isn't repeated the whole page
- CHORDS
- Mixed rhythms
- Ryhtmic grid makers/Rests - basically Syncopation 2.0
- Reads XML and generates: random and grids
- Data Validation for all inputs, BLACKLISTS, WHITELISTS, REGEX'S, ERRORS
- Create module called "tdoo", which collects and lists/updates in real time anything tagged tdoo, 
	it will have to parse comments - is that doable?


"""

import notereader, config, xmlwriter, attributes, os, sys, time, gridmaker
from pprint import pprint
from pathlib import Path

#MAIN PROGRAM LOOP
while True:
	config.clear() #clearing all global attributes
	program_select = input("1. Grid Maker or 2. Note Reader: ")
	if program_select == "1":
		gridmaker.run()
	if program_select == "2":
		notereader.run("1")
	
	#FILENAME VALIDATION
	path = './xmlbounces'
	while True:
		if config.filename + '.xml' in os.listdir(path):
			print()
			filename_selection = input(f"WARNING: '{config.filename}.xml' already exists! Overwrite? (Y or N): ")
			if filename_selection.lower() == 'n':
				print()
				newfilename = input("Enter New File Name: " + "\n")
				if newfilename == config.filename:
					print()
					print("ERROR - file name already taken!")
					continue
				else:
					config.filename = newfilename
					break
			if filename_selection.lower()== 'y':
				break
		else:
			break
	
	attributes.setattr()
	print()
	print("ATTRIBUTES STAFF 1")
	pprint(config.exercises_withattr_list)
	print()
	print("ATTRIBUTES STAFF 2")
	pprint(config.exercises_withattr_list_staff2)
	print()
	print("MEASURE LENGTH STAFF 1: ")
	print(config.measure_length_staff1)
	print()
	print("MEASURE LENGTH STAFF 2: ")
	print(config.measure_length_staff2)
	print()
	print("CONFIG.NOTETYPE: ")
	print(config.notetype)
	print()
	print("DIVS ")
	print(config.divs)
	print()
	print("NOTETYPE_STAFF1 ")
	print(config.notetype_staff1)
	print()
	print("NOTETYPE_STAFF2 ")
	print(config.notetype_staff2)
	print()
	print("DUR_1 ")
	print(config.test)
	print()
	print("DUR_2 ")
	print(config.test2)
	
	xmlwriter.xmlwrite()
	
	#PROGRAM LOOP/PRINTING - TODO This loop may be wonky and/or redundant, double check later...
	while True:
			try:	
				run = input("\n" + "(R)un again, (P)rint or (Q)uit?: ")
				whitelist_run = ["r","ru","run","rn"]
				whitelist_print = ["p","pr","pri","prin","print","prnt"]
				if run.lower() in whitelist_run:
					print()
					delete = input(f"Delete file '{config.filename}.xml'? Y or N: ")
					while True:
						if delete.lower() == "y":
							os.remove(f"xmlbounces/{config.filename}.xml")
							break
						if delete.lower() == "n":
							break
					break
				if run.lower() in whitelist_print:
					os.system('open '+ f'xmlbounces/{config.filename}.xml')
					continue
				if run.lower() == "q":
					raise Exception
				else:
					continue
			except Exception:
				print()
				delete = input(f"Delete file '{config.filename}.xml'? Y or N: ")
				while True:
					if delete.lower() == "y":
						os.remove(f"xmlbounces/{config.filename}.xml")
						break
					if delete.lower() == "n":
						break
				print("\n" + "---------- END ----------" + "\n")
				sys.exit()
	if run.lower() in whitelist_run:
			continue
	else:
			print("\n" + "---------- END ----------" + "\n")
			break

	