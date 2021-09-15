#! python3
# config - where global variables are stored

#EXERCISE SELECTION
grid = ""
scalepattern = ""
sightreader = ""
custom = ""
randomizer = ""

#HEADER CONSTRUCTION
time_signature = ""
timesig_beats = ""
timesig_beattype = ""
key_sig = ""
fifths = "" #key signature
clef = ""
clef_line = ""
staves = ""

#MEASURE CONSTRUCTION
divs = "" #SUBDIVISIONS - CHANGE TO "DIVISIONS"
measure_length = ""
measure_length_staff1 = ""
measure_length_staff2 = ""
shortstaff = ""

#NOTE CONSTRUCTION
notetype = ""
notetype_staff1 = ""
notetype_staff2 = ""
grid_notetype_a = ""
grid_notetype_b = ""
notetype_int = ""
notetype_staff2_int = ""
dur_a = ""
dur_b = ""

#SCALE CONSTRUCTION
root = "" #SCALE ROOT
scaletype = "" #MAJ, MIN ETC...

#RANDOMIZER SAMPLE CONSTRUCTION
sample_size = "" 
master = []
sample = []
duplicates = "" #TOLERATED DUPLICATES IN SAMPLE

#EXERCISE LISTS AND NOTE ATTRIBUTES
exercise_list = []
grid_exercise_list = []
grid_measure_a = []
grid_measure_b = []
grid_attributes = {}
measure = []
exercise_list_staff2 = []
exercises_withattr_list = {}
exercises_withattr_list_staff2 = {}
scale_pattern_exerciselist = {"1":[]}
scale_pattern_attributelist = {}


#KEY INDEXES
key_pattern_index = {}
grid_measure_index = []
a_pattern_mp_measure_index = {}
b_pattern_mp_measure_index = {}

#FILENAME AND TITLE
filename = ""
title = ""

def clear(): #TODO - ORGANIZE AND CROSS CHECK WITH ABOVE ATTRBTS.
	global grid
	global scalepattern 
	global sightreader
	global custom
	global randomizer
	global time_signature
	global timesig_beats
	global timesig_beattype
	global key_sig
	global fifths
	global clef
	global clef_line
	global staves
	global divs
	global measure_length
	global measure_length_staff1
	global measure_length_staff2
	global shortstaff
	global notetype
	global notetype_staff1
	global notetype_staff2
	global grid_notetype_a
	global grid_notetype_b
	global notetype_int
	global notetype_staff2_int
	global dur_a
	global dur_b
	global root
	global scaletype
	global sample_size
	global master
	global sample
	global duplicates
	global exercise_list
	global grid_exercise_list
	global grid_measure_a
	global grid_measure_b
	global grid_attributes
	global exercise_list_staff2
	global exercises_withattr_list
	global exercises_withattr_list_staff2
	global scale_pattern_exerciselist
	global scale_pattern_attributelist
	global key_pattern_index
	global key_pattern_index_descending
	global filename
	global title

	#EXERCISE SELECTION
	grid = ""
	scalepattern = ""
	sightreader = ""
	custom = ""
	randomizer = ""

	#HEADER CONSTRUCTION
	time_signature = ""
	timesig_beats = ""
	timesig_beattype = ""
	key_sig = ""
	fifths = "" #key signature
	clef = ""
	clef_line = ""
	staves = ""

	#MEASURE CONSTRUCTION
	divs = "" #SUBDIVISIONS - CHANGE TO "DIVISIONS"
	measure_length = ""
	measure_length_staff1 = ""
	measure_length_staff2 = ""
	shortstaff = ""

	#NOTE CONSTRUCTION
	notetype = ""
	notetype_staff1 = ""
	notetype_staff2 = ""
	grid_notetype_a = ""
	grid_notetype_b = ""
	notetype_int = ""
	notetype_staff2_int = ""
	dur_a = ""
	dur_b = ""

	#SCALE CONSTRUCTION
	root = "" #SCALE ROOT
	scaletype = "" #MAJ, MIN ETC...

	#RANDOMIZER SAMPLE CONSTRUCTION
	sample_size = "" 
	master = []
	sample = []
	duplicates = "" #TOLERATED DUPLICATES IN SAMPLE

	#EXERCISE LISTS AND NOTE ATTRIBUTES
	exercise_list = []
	grid_exercise_list = []
	grid_attributes = {}
	grid_measure_a = []
	grid_measure_b = []
	exercise_list_staff2 = []
	exercises_withattr_list = {}
	exercises_withattr_list_staff2 = {}
	scale_pattern_exerciselist = {"1":[]}
	scale_pattern_attributelist = {}
	key_pattern_index = []
	key_pattern_index_descending = []

	#FILENAME AND TITLE
	filename = ""
	title = ""
