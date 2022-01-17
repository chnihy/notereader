#python3
#playback - a module for playing midi using SCAMP

from scamp import Session
from scales import midi_nums
import config


def play(): # Key signature?
	# Creating session and parts
	s = Session()
	
	s.fast_forward_to_beat(500) # This makes it NOT play any sound
	
	s.tempo = config.tempo
	
	piano = s.new_part("piano")

	piano.clef_preference = config.clef.lower()

	
	# Transcribing
	s.start_transcribing()	
	
	# Dict of numeric values for rhythm entry in SCAMP
	rhythm_to_num = {"quarter": 1, 
					"eighth": float(1/2), 
					"sixteenth": float(1/4), 
					"thirty second": float(1/8), 
					"triplet": float(1/3), 
					"16th triplet": float(1/6) 
					}
	rhythm_num = rhythm_to_num[config.rhythm]
				
	#TODO SELECT FLATS OR SHAPRS in main.py/main.kv
	if config.flats == True:
		selection = "flats"
	else:
		selection = "sharps"
	
	# SCAMP playback of config.exercise_list
	for measure in config.exercise_list:
		for note in measure:
			# TODO Range numbers!!!
			note_num = midi_nums[selection][note.capitalize() + "4"]

			piano.play_note(note_num, 1, rhythm_num, f"key: {config.key_signature}")
	
	# Printings Score
	performance = s.stop_transcribing()

	# Max divisor ensures that weird subdivisions don't get printed
	divisor_nums = {"quarter": 1,
					"eighth": 2,
					"triplet": 3,
					"sixteenth": 4,
					"16th triplet": 6,
					"thirty second": 8}

	performance.to_score(title = config.title, 
						composer = None, 
						time_signature=f"{config.beats}/{config.beattype}").show()




