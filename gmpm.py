#! python
#grid_maker_pattern_maker - putting melodic patterns into our grids

import gridmaker as gm
import mpm
import config
import scales
from pprint import pprint
from copy import copy
#from templates import templates, temp_templatesq
from _templates_ import templates, temp_templates

def note(rhythm, dur=1, pitch="G4"):
    note = {"rhythm": rhythm, "dur": dur, "pitch":pitch}
    return note
	
def press_enter(function, message="Press ENTER to continue"):
	while True:
		button = input(message)
		if button == "":
			function()
			break
		else:
			continue

#TEMPLATES
def load_template():
	while True:
		pprint(list(templates.keys()))
		template_name = input("Enter template name or 'list' for list of available templates: ")
		try:
			template = templates[template_name]
			break
		except KeyError:
			print("No template with that name, try again ")
			continue
		break

	#TIME_AND_KEY INPUT
	time_and_key = template["time_and_key"]
	beats = time_and_key["beats"]	
	beat_type = time_and_key["beat_type"]
	root = time_and_key["root"]
	scaletype = time_and_key["scaletype"]
	octaves = time_and_key["octaves"]

	#GRIDMAKER INPUT
	gridmakerinput = template["gridmaker"]
	a = gridmakerinput["a"]
	b = gridmakerinput["b"]
	global select_grid
	select_grid = gridmakerinput["select_grid"]
	reversing = gridmakerinput["reversing"]

	#A PATTERN INPUT
	a_key_pattern_index = akpi = template["a_key_pattern_index"]
	chunk_key_a = akpi["chunk_key"]
	noteRepeats_a = akpi["noteRepeats"]
	root_a = time_and_key["root"]
	scaletype_a = time_and_key["scaletype"]
	gpm_a = True
	scale_descend_a = akpi["scale_descend"]
	#offset_a = akpi["offset"]

	#B PATTERN INPUT
	b_key_pattern_index = bkpi = template["b_key_pattern_index"]
	chunk_key_b = bkpi["chunk_key"]
	noteRepeats_b = bkpi["noteRepeats"]
	root_b = time_and_key["root"]
	scaletype_b = time_and_key["scaletype"]
	gpm_b = True
	scale_descend_b = bkpi["scale_descend"]
	#offset_b = bkpi["offset"]

	#gridmaker function call
	grid_measure_index = gm.gridmaker(beats, beat_type, a, b, select_grid, reversing)
	config.grid_measure_index = grid_measure_index

	#mpm_a function call
	a_key_pattern_index = mpm.melodic_pattern_maker(chunk_key_a, noteRepeats_a, root_a, scaletype_a, octaves, gpm_a, 
														scale_descend_a, offset="default", measure_count=1)
	config.a_key_pattern_index = a_key_pattern_index
	
	a_pattern_mp_measure_index = mpm.mp_measure_maker(a_key_pattern_index, beats=akpi["beats"])
	config.a_pattern_mp_measure_index = a_pattern_mp_measure_index

	#mpm_b function call
	b_key_pattern_index = mpm.melodic_pattern_maker(chunk_key_b, noteRepeats_b, root_b, scaletype_b, octaves, gpm_b, scale_descend_b,  
													offset="default", measure_count=1)
	config.b_key_pattern_index = b_key_pattern_index
	
	b_pattern_mp_measure_index = mpm.mp_measure_maker(b_key_pattern_index, beats=bkpi["beats"])
	config.b_pattern_mp_measure_index = b_pattern_mp_measure_index

	#PUTTING IT ALL TOGETHER
	grid_mp_combiner(template)
	
	#PRINTTEST
	press_enter(print_just_the_notes, message="Press ENTER to print notes: ")

def new_template():
	while True:
		template_name = input("Enter new template name: ")
		if template_name.lower() in list(templates.keys()):
			print("Name alread taken, try something else... ")
			continue
		else:
			break
	template = temp_templates[template_name] = {}
	
	#TIME_AND_KEY INPUT
	time_and_key = template["time_and_key"] = {}
	beats = time_and_key["beats"] = input("Enter beats: ")
	beat_type = time_and_key["beat_type"] = input(f"Enter beat Type: {beats}/")
	root = time_and_key["root"] = input("Enter root: ")
	scaletype = time_and_key["scaletype"] = input("Enter scaletype: ")
	octaves = time_and_key["octaves"] = 4

	#GRIDMAKER INPUT
	gridmakerinput = template["gridmaker"] = {}
	a = gridmakerinput["a"] = input("Enter a: ")
	b = gridmakerinput["b"] = input("Enter b: ")
	select_grid = gridmakerinput["select_grid"] = input("Select grid 1 or 2: ")
	reversing = gridmakerinput["reversing"] = input("Reversing grid? y or n: ")

	#A PATTERN INPUT
	a_key_pattern_index = akpi = template["a_key_pattern_index"] = {}
	patternToChunkKey = {"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six"}
	chunk_key_a = []
	pattern = str(input("Enter pattern, ex: 123 or 1231 or 321 etc... " ))
	for num in pattern:
		chunk_key_a.append(patternToChunkKey[num])
	akpi["chunk_key"] = chunk_key_a
	"""yorn = input("Include note repeats (Y or N)?: ")
	if yorn.lower() == "n":
		noteRepeats_a = False
	else: 
		noteRepeats_a = True"""
	akpi["noteRepeats"] = noteRepeats_a = True
	root_a = akpi["root"] = root
	scaletype_a = akpi["scaletype"] = scaletype
	gpm_a = True
	scale_descend_a = akpi["scale_descend"] = True
	#offset_a = akpi["offset"] = 'default'

	#B PATTERN INPUT
	b_key_pattern_index = bkpi = template["b_key_pattern_index"] = {}
	chunk_key_b = []
	pattern = str(input("Enter pattern, ex: 123 or 1231 or 321 etc... " ))
	for num in pattern:
		chunk_key_b.append(patternToChunkKey[num])
	bkpi["chunk_key"] = chunk_key_b
	"""yorn_b = input("Include note repeats (Y or N)?: ")
	if yorn_b.lower() == "n":
		noteRepeats_b = False
	else: 
		noteRepeats_b = True"""
	bkpi["noteRepeats"] = noteRepeats_b = True
	root_b = bkpi["root"] = root
	scaletype_b = bkpi["scaletype"] = scaletype
	gpm_b = True
	scale_descend_b = bkpi["scale_descend"] = True
	#offset_b = bkpi["offset"] = 'default'

	#gridmaker function call
	grid_measure_index = gm.gridmaker(beats, beat_type, a, b, select_grid, reversing)
	config.grid_measure_index = grid_measure_index

	#mpm_a function call
	a_key_pattern_index = mpm.melodic_pattern_maker(chunk_key_a, noteRepeats_a, root_a, scaletype_a, octaves, gpm_a, scale_descend_a,  
															offset="default", measure_count=1)
	config.a_key_pattern_index = a_key_pattern_index
	
	a_pattern_mp_measure_index = mpm.mp_measure_maker(a_key_pattern_index, int(beats))
	config.a_pattern_mp_measure_index = a_pattern_mp_measure_index

	#mpm_b function call
	b_key_pattern_index = mpm.melodic_pattern_maker(chunk_key_b, noteRepeats_b, root_b, scaletype_b, octaves, gpm_b, scale_descend_b,  
													offset="default", measure_count=1)
	config.b_key_pattern_index = b_key_pattern_index
	
	b_pattern_mp_measure_index = mpm.mp_measure_maker(b_key_pattern_index, int(beats))
	config.b_pattern_mp_measure_index = b_pattern_mp_measure_index

	#PUTTING IT ALL TOGETHER
	grid_mp_combiner(template)

	press_enter(save_template, message="Press ENTER to Save Template: ")

	press_enter(print_just_the_notes, message="Press ENTER to print notes ")

def edit_template():
	#CREATES ANOTHER COPY OF TEMPLATES CALLED UPDATED_TEMPLATES, PROBABLY REDUNDANT TODO
	while True:
		global temp_templates
		updated_templates = copy(temp_templates)
		print("Select Template")
		pprint(list(updated_templates.keys()))
		select_template = input(": ")
		try:
			template = updated_templates[select_template]
			break
		except KeyError:
			print("No template with that name, try again ")
			continue
		break
	while True:
		print("Select Module")
		pprint(list(template.keys()))
		select_module = input(": ")
		try:
			module = template[select_module]
			break
		except KeyError:
			print("No module with that name, try again")
			continue
	while True:
		print("Select Attribute: ")
		pprint(list(module.keys()))
		select_attribute = input(": ")
		try:
			attribute = module[select_attribute]
			break
		except KeyError:
			print("No attribute with that name, try again")
			continue
	while True:
		print(f"CURRENT VALUE: {attribute}")
		new_value = input("Enter new value: ")
		try:
			updated_templates[select_template][select_module][select_attribute] = new_value
			print("Attribute updated! ")
			break
		except ValueError:
			print("Value Error, try again... ")
			continue
	overwrite = input("Overwrite? y or n: ")
	if overwrite.lower() == "y":
		temp_templates = copy(updated_templates)
		press_enter(save_template, message="Press ENTER to OVERWRITE: ")
		press_enter(print_just_the_notes, message="SAVED, press ENTER to view notes: ")
	else:
		while True:
			template_name = input("Enter new template name: ")
			if template_name.lower() in list(templates.keys()):
				print("Name alread taken, try something else... ")
				continue
			else:
				temp_templates[template_name] = template
				break
		press_enter(save_template, message="Press ENTER to SAVE")

def delete_template():
	#CREATES ANOTHER COPY OF TEMPLATES CALLED UPDATED_TEMPLATES
	while True:
		global temp_templates
		updated_templates = copy(temp_templates)
		print("Select Template")
		pprint(list(updated_templates.keys()))
		select_template = input(": ")
		try:
			template = updated_templates[select_template]
			break
		except KeyError:
			print("No template with that name, try again ")
			continue
		break
	
	def del_temp():
		updated_templates.pop(select_template)

	press_enter(del_temp, message=f"Press ENTER to delete {select_template}")
	
	print(f"Done! " + f"{list(updated_templates.keys())}")
	
	temp_templates = updated_templates 

	press_enter(save_template, message="Press ENTER to update templates ")
	
	print(f"Done! " + f"{list(templates.keys())}")

def save_template():
	global temp_templates
	global templates
	#header
	fn = open("_templates_.py","w")
	fn.write("#!python" + "\n" + "#templates" + "\n" + "from copy import copy" + "\n")
	fn.close()

	templates = temp_templates #THIS IS STORED IN RECENT MEMORY, WONT BE COMMITTED TO _TEMPLATES_ UNTIL EXIT???
	#writing the new file
	fn = open("_templates_.py", 'a')
	fn.write('templates = {}'.format(templates)) #F STRINGS DONT WORK HERE, only .format()
	fn.close()
	
	#footer
	fn = open("_templates_.py", "a")
	fn.write("temp_templates = copy(templates)")
	fn.close()

	print("Template Saved! ")


#RUN FUNC
def run():
	beats = 4

	gpm = True
	
	#RUN THE GRID MAKER
	grid_measure_index = gm.run()

	#RUN THE MELODIC PATTERN MAKER
	a_pattern_mp_measure_index = mpm.run(True)
	b_pattern_mp_measure_index = mpm.run(True)


	#GRID MAKER test
	print("Grid complete!")
	pprint(grid_measure_index)
	print("")
	#MP test
	print("Key index complete!")
	print("A PATTERN:")
	pprint(a_pattern_mp_measure_index)
	print("")
	print("B PATTERN:")
	pprint(b_pattern_mp_measure_index)

	#PUTTING THEM TOGETHER
	#grid_mp_combiner() #MISSING TEMPLATE VAR

#COMBINING ALGORITHM
def grid_mp_combiner(template, custom_start_note = False, custom_motion = "default"):
	#VARIABLES
	scaletype = template["time_and_key"]["scaletype"]
	root = template["time_and_key"]["root"]
	scale = scales.allscales[scaletype][root.capitalize()]

	#STARTING NOTE
	yorn_csm = input("Custom start note? y or n: ") #TODO MAKE THIS CALLABLE
	if yorn_csm == "y":
		custom_start_note = True
	else:
		pass
	
	while True:
		yorn_cm = input("Select motion: 1. ASCENDING  2. DESCENDING (not available yet) 3. STAY or press ENTER for DEFAULT : ")
		if yorn_cm == "1":
			custom_motion = "ascending"
			break
		if yorn_cm == "2":
			custom_motion = "descending"
			break
		if yorn_cm == "3":
			custom_motion = "stay"
			break
		if yorn_cm == "":
			custom_motion == "ascending"
			break
		else:
			print("Error, try again")
			continue
	
	moving_guide = [["a","b","b","b"],	
					["b","a","b","b"],
					["b","b","a","b"],
					["b","b","b","a"]]
	stacking_guide = [["a","b","b","b"],	 #TODO - REDO THIS OR MOVE TO DATA
					["a","a","b","b"],
					["a","a","a","b"],
					["a","a","a","a"]]
	
	select_grid = template["gridmaker"]["select_grid"]
	if select_grid == "1":
		grid_guide = moving_guide
	else:
		grid_guide = stacking_guide

	grid_measure_index = config.grid_measure_index
	a_pattern_mp_measure_index = config.a_pattern_mp_measure_index
	b_pattern_mp_measure_index = config.b_pattern_mp_measure_index
	exercise_list = []
	

	#YE HOLY ALGORITHM
	#MEASURE MAKER
	for exercise_num in range(len(grid_measure_index)):
		#VARIABLES
		measure = [] 
		grid_measure_select = grid_measure_index[exercise_num]
		
		#CUSTOM START NOTE
		if custom_start_note == True: 
			if exercise_num == 0:
				while True:
					print(scale)
					start_note = input("Enter start note: ")
					try:
						mp_measure_counter = scale.index(start_note.capitalize())
						break
					except ValueError: 
						print("Not in scale, try again")
						continue
			if custom_motion == "stay" and exercise_num != 0:
				mp_measure_counter = scale.index(start_note.capitalize())
			if custom_motion != "stay" and exercise_num != 0: #custom start note, not stay, not first ex
				mp_measure_counter += 1 
		if custom_start_note == False:
			if custom_motion == "stay":
				mp_measure_counter = 0
			else:
				mp_measure_counter = exercise_num

		#CHUNK MAKER
		for beat_chunk_counter in (range(len(grid_measure_select))):	
			#VARIABLES
			chunk = [] 
			grid_guide_var = grid_guide[exercise_num][beat_chunk_counter]
			grid_measure_chunk = grid_measure_index[exercise_num][beat_chunk_counter]
			
			#BUILDING CHUNK
			for n in range(len(grid_measure_chunk)):
				#VARIABLES
				grid_chunk_note = grid_measure_chunk[n]
				if grid_guide_var == "a":
					try:
						mp_chunk_note = a_pattern_mp_measure_index["ascending"][mp_measure_counter][beat_chunk_counter][n]
					except IndexError:							#TODO CREATE MOTION SELECT VAR >>> CUSTOM MOTION
						mp_measure_counter = 0
						mp_chunk_note = a_pattern_mp_measure_index["ascending"][mp_measure_counter][beat_chunk_counter][n]
				else:
					try:
						mp_chunk_note = b_pattern_mp_measure_index["ascending"][mp_measure_counter][beat_chunk_counter][n]
					except IndexError:
						mp_measure_counter = 0
						mp_chunk_note = b_pattern_mp_measure_index["ascending"][mp_measure_counter][beat_chunk_counter][n]
				
				#ADD NOTE TO CHUNK
				chunk.append(note(rhythm=grid_chunk_note,dur=1, pitch=mp_chunk_note))
			
			#BUILDING MEASURE
			measure.append(chunk)
				
		#BUILDING EXERCISE LIST
		exercise_list.append(measure)
		"""if custom_motion == "ascend/descend":
			mp_measure_counter += 1
		if custom_motion == "stay":
			pass"""

	#ADD EX LIST TO CONFIG
	config.exercise_list = exercise_list
	exercise_num = 0
#PRINTING
def print_just_the_notes():
	exercise_list = config.exercise_list
	print("\n"*10)
	for measure in exercise_list:
		print(str(exercise_list.index(measure) + 1), end=" ")
		for chunk in measure:
			print("[", end="")
			for note in chunk:
				if note == chunk[0]:
					print(note["pitch"], end="")
				else:
					print(" " + note["pitch"], end="")
			print("]", end=" ")
		print("",end="\n")

def print_test():
	#GRID MAKER test
	print("GRID MEASURE INDEX!")
	pprint(config.grid_measure_index)
	print("")
	
	#MP test
	print("MP MEASURE INDEXES!")
	print("A PATTERN:")
	pprint(config.a_pattern_mp_measure_index)
	print("")
	print("B PATTERN:")
	pprint(config.b_pattern_mp_measure_index)



