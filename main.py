#! python
# main
"""TODO: 
2. Fix file name to be more granular, add date
3. QA/Test and error log
4. Fix those errors
5. Grid makers
- CHORDS
- Mixed rhythms
6. Ryhtmic grid makers/Rests - basically Syncopation 2.0
7. Reads XML and generates: random and grids
8. Data Validation for all inputs, BLACKLISTS, WHITELISTS, REGEX'S, ERRORS
9. GRAND STAFF - for piano sight reading, separate rhythms for bass/treble clef!!!!!OMG
10. Create module called "tdoo", which collects and lists/updates in real time anything tagged tdoo, 
	it will have to parse comments - is that doable?


"""

import notereader, config, xmlwriter, attributes, os, sys
from pprint import pprint
from pathlib import Path

#MAIN PROGRAM LOOP
while True:
	notereader.run("1")

	attributes.setattr()

	xmlwriter.xmlwrite()
	#PROGRAM LOOP/PRINTING - TODO This loop may be wonky and/or redundant, double check later...
	while True:
			try:	
				run = input("\n" + "(R)un again, (P)rint or (Q)uit?: ")
				whitelist_run = ["r","ru","run","rn"]
				whitelist_print = ["p","pr","pri","prin","print","prnt"]
				if run.lower() in whitelist_run:
					os.remove(f"xmlbounces/{config.filename}.xml")
					break 
				if run.lower() in whitelist_print:
					os.system('open '+ f'xmlbounces/{config.filename}.xml')
					continue
				if run.lower() == "q":
					raise Exception
				else:
					continue
			except Exception:
				print("\n" + "---------- END ----------" + "\n")
				sys.exit()
	if run.lower() in whitelist_run:
			continue
	else:
			print("\n" + "---------- END ----------" + "\n")
			break

	