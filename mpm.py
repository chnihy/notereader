#! python3
#Melodic patterns
#ERROR LOG:
#TODO Turn on/off note doubling - create a func called skip()

import scales, config, os
from scales import allscales
from pprint import pprint
from copy import copy

def br():
	print("\n"*20)

def contrary(chunk):
			return(chunk[::-1])

gpm = False #is this module being called by the gpm? Default is no

#MELODIC PATTERN MAKER - GENERATES KEY_PATTERN_INDEX, our chunks of patterns...
def melodic_pattern_maker(chunk_key, noteRepeats, root, scaletype, octaves, gpm, scale_descend=True, offset="default",
						measure_count=1):
	
	key_pattern_index_ascending = [] #clear
	key_pattern_index_descending = []
	scale = allscales[scaletype][root.capitalize()] #TODO create scales or store them??? 
	xn = 0 #ex num counter
	
	#RANGE
	r = 4  #range counter - TODO this will be modifiable for Treble/Bass clef
	rangenum = str(r)
	range_break = len(scale) * octaves
	
	#YE HOLY ALGORITHM
	while True:
		n = 0 #index error counters
		q = 0
		m = 0
		p = 0
		
		for i in range(len(scale)):
			#COUNTER/CONTAINER RESETS
			xn += 1 #exercise number counter
			chunk = []
			temp_rangenum = str(r+1)
			for slots in range(len(chunk_key)): #empty placeholders
				chunk.append("")
			pool = {} #holding pool for notes

			#BUILDING OUR NOTES
			one = scale[i] + rangenum #ONE
			
			try:
				two = scale[i+1] + rangenum #TWO
			except IndexError: 
				r += 1
				rangenum = str(r) #INCREASE RANGE GLOBALLY WHEN 'ONE' is last
				two = scale[0] + rangenum
			
			try:
				three = scale[i+2] + rangenum #THREE
			except IndexError: #IF JUST THREE this is first Index Error
				three = scale[n] + temp_rangenum #So that only Three goes up an octave in this chunk
				n += 1
			
			if 'four' in chunk_key:
				try:
					four = scale[i+3] + rangenum
				except IndexError: #... IF FOUR, this is first IndexError
					four = scale[q] + temp_rangenum
					q += 1	
			if 'five' in chunk_key:
				try:
					five = scale[i+4] + rangenum
				except IndexError: #... IF FIVE, this is first IndexError
					five = scale[p] + temp_rangenum
					p += 1
			if 'six' in chunk_key:
				try:
					six = scale[i+5] + rangenum
				except IndexError: #... IF SIX, this is first IndexError
					six = scale[m] + temp_rangenum
					m += 1

			#FILLING OUR NOTE POOL
			pool['one'] = one
			pool['two'] = two
			pool['three'] = three
			if 'four' in chunk_key:
				pool['four'] = four
			if 'five' in chunk_key:
				pool['five'] = five
			if 'six' in chunk_key:
				pool['six'] = six


			#BUILDING OUR CHUNK
			for note in pool.keys():
				for var in range(len(chunk_key)):
					if note == chunk_key[var]:
						chunk[var] = pool[note]
			
			#ADDING TO KEY PATTERN INDEX
			if noteRepeats == False:
				if i % 2 == 0:
					key_pattern_index_ascending.append(chunk)
				else:
					pass
			else:
				key_pattern_index_ascending.append(chunk)
			#exercise_list[ex_num] = chunk
			 

		#RANGE BREAK - TODO may need modification
		if xn == int(range_break):
			break
		else:
			continue
			
	contr = False
	#MAKING OUR DESCENDING CHUNKS (in contrary or complimentary form)
	if scale_descend == True:
		n = 0
		if contr == False: #COMPLIMENTARY
			if offset == "default":
				offset = 6 
			templist = []
			for chunk in key_pattern_index_ascending[::-1]:
				templist.append(contrary(chunk)) #this is correct, contrary() method flips chunks agnostically
			for i in range(len(key_pattern_index_ascending)):
				try:
					key_pattern_index_descending.append(templist[i+ offset])
				except IndexError:
					key_pattern_index_descending.append(templist[n])
					n += 1
		else:
			if offset == "default":
				offset = 0
			for i in range(len(key_pattern_index_ascending)):
				try:
					key_pattern_index_descending.append(key_pattern_index_ascending[i+offset])
				except IndexError:
					key_pattern_index_descending.append(key_pattern_index_ascending[n])
					n += 1
	if gpm == False:
		key_pattern_index = {"ascending":key_pattern_index_ascending[:len(scale * measure_count)],  #indexes need to be trimmed to fit range
						"descending":key_pattern_index_descending[:len(scale * measure_count)]}
	else:
		key_pattern_index = {"ascending":key_pattern_index_ascending,  
							"descending":key_pattern_index_descending}
	return(key_pattern_index)

#MELODIC PATTERN MEASURE MAKER - Generates MP_MEASURE_INDEX, all possible measures filled with pattern chunks
def mp_measure_maker(key_pattern_index, beats=4):
	measure = []	
	mp_measure_index = {"ascending":[],"descending":[]}
	kp = 0

	#YE HOLY ALGORITHM
	for i in range(len(key_pattern_index['ascending'])):
		measure = []
		measure_descend = []
		for b in range(beats):
			try:
				chunk = key_pattern_index['ascending'][kp] 
				chunk_descending = key_pattern_index['descending'][kp]
				measure.append(chunk)
				measure_descend.append(chunk_descending)
				kp += 1
			except IndexError:
				kp = 0
				chunk = key_pattern_index['ascending'][kp]
				chunk_descending = key_pattern_index['descending'][kp]
				measure.append(chunk)
				measure_descend.append(chunk_descending)
				kp += 1
		mp_measure_index['ascending'].append(measure)
		mp_measure_index['descending'].append(measure_descend)
		kp -= (beats-1)

	return(mp_measure_index)


""" DEMOTED
#INPUT CONSOLE
def run(gpm):
	while True:
		patternToChunkKey = {"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six"}
		chunk_key = []
		
		###INPUT
		pattern = str(input("Enter pattern, ex: 123 or 1231 or 321 etc... " ))
		for num in pattern:
			chunk_key.append(patternToChunkKey[num])
		root = input("Enter root note: ")
		scaletype = input("Enter scale type, ex. major: ")
		octaves = str(input("Enter number of octaves: "))
		beats = input("Enter beats per measure: ")
		offset = input("Enter descending offset: ")
		noteRepeats = True
		yorn = input("Include note repeats (Y or N)?: ")
		if yorn.lower() == "n":
			noteRepeats = False
		else: 
			pass

		####OUTPUT
		print(f"Pattern: {chunk_key}")
		print(f"SCALE: {root.upper()} {scaletype}")
		print(f"RANGE: {octaves} Oct")
		print(f"NOTE REPEATS: {noteRepeats}")
		print(f"BEATS: {beats}")
		print(f"OFFSET: {offset}")
		keyboardEntry = input("Press ENTER to print pattern or ANY KEY to change: ")
		if keyboardEntry == "":
			key_pattern_index = melodic_pattern_maker(chunk_key, noteRepeats, root, scaletype, octaves, gpm=True, scale_descend=True)
			mp_measure_index = mp_measure_maker(key_pattern_index, beats=4)
			break
		else:
			continue
	return(mp_measure_index)
	
	"""