#! python3
# grid - the main launch program for the grid maker

import gridmaker, xmlwriter, config, sys, os

while True:
	gridmaker.run()

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

	xmlwriter.xmlwrite()

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