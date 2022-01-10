#!python
# Scales - a bunch of scales for use in auto-generated scripts
allnotes_master = ["A","A#","Bb","B","C","C#","Db","D","D#","Eb","E","F","F#","Gb","G","G#","Ab"]


allnotes_ranged = { "allnotes" :['A0', 'A#0', 'Bb0', 'B0', 
					'C1', 'C#1', 'Db1', 'D1', 'D#1', 'Eb1', 'E1', 'F1', 'F#1', 'Gb1', 'G1', 'G#1', 'Ab1', 'A1', 'A#1', 'Bb1', 'B1', 
					'C2', 'C#2', 'Db2', 'D2', 'D#2', 'Eb2', 'E2', 'F2', 'F#2', 'Gb2', 'G2', 'G#2', 'Ab2', 'A2', 'A#2', 'Bb2', 'B2', 
					'C3', 'C#3', 'Db3', 'D3', 'D#3', 'Eb3', 'E3', 'F3', 'F#3', 'Gb3', 'G3', 'G#3', 'Ab3', 'A3', 'A#3', 'Bb3', 'B3', 
					'C4', 'C#4', 'Db4', 'D4', 'D#4', 'Eb4', 'E4', 'F4', 'F#4', 'Gb4', 'G4', 'G#4', 'Ab4', 'A4', 'A#4', 'Bb4', 'B4', 
					'C5', 'C#5', 'Db5', 'D5', 'D#5', 'Eb5', 'E5', 'F5', 'F#5', 'Gb5', 'G5', 'G#5', 'Ab5', 'A5', 'A#5', 'Bb5', 'B5', 
					'C6', 'C#6', 'Db6', 'D6', 'D#6', 'Eb6', 'E6', 'F6', 'F#6', 'Gb6', 'G6', 'G#6', 'Ab6', 'A6', 'A#6', 'Bb6', 'B6', 
					'C7', 'C#7', 'Db7', 'D7', 'D#7', 'Eb7', 'E7', 'F7', 'F#7', 'Gb7', 'G7', 'G#7', 'Ab7', 'A7', 'A#7', 'Bb7', 'B7', 
					'C8', 'C#8', 'Db8', 'D8', 'D#8', 'Eb8', 'E8', 'F8', 'F#8', 'Gb8', 'G8', 'G#8', 'Ab8', 'A8', 'A#8', 'Bb8', 'B8',
					'C9', 'C#9', 'Db9', 'D9', 'D#9', 'Eb9', 'E9', 'F9', 'F#9', 'Gb9', 'G9'],
					
					"sharps": ['A0', 'A#0', 'B0', 
					'C1', 'C#1', 'D1', 'D#1', 'E1', 'F1', 'F#1', 'G1', 'G#1', 'A1', 'A#1', 'B1', 
					'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2', 'A2', 'A#2', 'B2', 
					'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3', 
					'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4', 
					'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5', 
					'C6', 'C#6', 'D6', 'D#6', 'E6', 'F6', 'F#6', 'G6', 'G#6', 'A6', 'A#6', 'B6', 
					'C7', 'C#7', 'D7', 'D#7', 'E7', 'F7', 'F#7', 'G7', 'G#7', 'A7', 'A#7', 'B7', 
					'C8', 'C#8', 'D8', 'D#8', 'E8', 'F8', 'F#8', 'G8', 'G#8', 'A8', 'A#8', 'B8',
					'C9', 'C#9', 'D9', 'D#9', 'E9', 'F9', 'F#9', 'G9'],
					
					"flats": ['A0', 'Bb0', 'B0', 
					'C1', 'Db1', 'D1', 'Eb1', 'E1', 'F1', 'Gb1', 'G1', 'Ab1', 'A1', 'Bb1', 'B1', 
					'C2', 'Db2', 'D2', 'Eb2', 'E2', 'F2', 'Gb2', 'G2', 'Ab2', 'A2', 'Bb2', 'B2', 
					'C3', 'Db3', 'D3', 'Eb3', 'E3', 'F3', 'Gb3', 'G3', 'Ab3', 'A3', 'Bb3', 'B3', 
					'C4', 'Db4', 'D4', 'Eb4', 'E4', 'F4', 'Gb4', 'G4', 'Ab4', 'A4', 'Bb4', 'B4', 
					'C5', 'Db5', 'D5', 'Eb5', 'E5', 'F5', 'Gb5', 'G5', 'Ab5', 'A5', 'Bb5', 'B5', 
					'C6', 'Db6', 'D6', 'Eb6', 'E6', 'F6', 'Gb6', 'G6', 'Ab6', 'A6', 'Bb6', 'B6', 
					'C7', 'Db7', 'D7', 'Eb7', 'E7', 'F7', 'Gb7', 'G7', 'Ab7', 'A7', 'Bb7', 'B7',
					'C8', 'Db8', 'D8', 'Eb8', 'E8', 'F8', 'Gb8', 'G8', 'Ab8', 'A8', 'Bb8', 'B8',
					'C9', 'Db9', 'D9', 'Eb9', 'E9', 'F9', 'Gb9', 'G9']
}

allscales =	{"major" : {'A': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
					'Ab': ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G'],
					'A#': ['A#', 'C', 'D', 'D#', 'F', 'G', 'A'],
					'B': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'],
					'Bb': ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A'],
					'C': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
					'C#': ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C'],
					'D': ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
					'Db': ['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C'],
					'D#': ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D'],
					'E': ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
					'Eb': ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D'],
					'F': ['F', 'G', 'A', 'Bb', 'C', 'D', 'E'],
					'F#': ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F'],
					'G': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
					'Gb': ['Gb', 'Ab', 'Bb', 'B', 'Db', 'Eb', 'F'],
					'G#': ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G']},
			"minor": {'A': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
					'Ab': ['Ab', 'Bb', 'B', 'Db', 'Eb', 'E', 'Gb'],
					'A#': ['A#', 'C', 'C#', 'D#', 'F', 'F#', 'G#'],
					'B': ['B', 'C#', 'D', 'E', 'F#', 'G', 'A'],
					'Bb': ['Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'Ab'],
					'C': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
					'C#': ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B'],
					'D': ['D', 'E', 'F', 'G', 'A', 'A#', 'C'],
					'Db': ['Db', 'Eb', 'E', 'Gb', 'Ab', 'A', 'B'],
					'D#': ['D#', 'F', 'F#', 'G#', 'A#', 'B', 'C#'],
					'E': ['E', 'F#', 'G', 'A', 'B', 'C', 'D'],
					'Eb': ['Eb', 'F', 'Gb', 'Ab', 'Bb', 'B', 'Db'],
					'F': ['F', 'G', 'Ab', 'Bb', 'C', 'Db', 'Eb'],
					'F#': ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E'],
					'G': ['G', 'A', 'A#', 'C', 'D', 'D#', 'F'],
					'Gb': ['Gb', 'Ab', 'A', 'B', 'Db', 'D', 'E'],
					'G#': ['G#', 'A#', 'B', 'C#', 'D#', 'E', 'F#']},
			"melodic minor":{'A': ['A', 'B', 'C', 'D', 'E', 'F', 'G#'],
					'Ab': ['Ab', 'Bb', 'B', 'Db', 'Eb', 'E', 'G'],
					'A#': ['A#', 'C', 'C#', 'D#', 'F', 'F#', 'A'],
					'B': ['B', 'C#', 'D', 'E', 'F#', 'G', 'A#'],
					'Bb': ['Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'A'],
					'C': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'B'],
					'C#': ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'C'],
					'D': ['D', 'E', 'F', 'G', 'A', 'A#', 'C#'],
					'Db': ['Db', 'Eb', 'E', 'Gb', 'Ab', 'A', 'C'],
					'D#': ['D#', 'F', 'F#', 'G#', 'A#', 'B', 'D'],
					'E': ['E', 'F#', 'G', 'A', 'B', 'C', 'D#'],
					'Eb': ['Eb', 'F', 'Gb', 'Ab', 'Bb', 'B', 'D'],
					'F': ['F', 'G', 'Ab', 'Bb', 'C', 'Db', 'E'],
					'F#': ['F#', 'G#', 'A', 'B', 'C#', 'D', 'F'],
					'G': ['G', 'A', 'A#', 'C', 'D', 'D#', 'F#'],
					'Gb': ['Gb', 'Ab', 'A', 'B', 'Db', 'D', 'F'],
					'G#': ['G#', 'A#', 'B', 'C#', 'D#', 'E', 'G']},
			"major pentatonic":{'A': ['A', 'B', 'C#', 'E', 'F#'],
					'Ab': ['Ab', 'Bb', 'C', 'Eb', 'F'],
					'A#': ['A#', 'C', 'D', 'F', 'G'],
					'B': ['B', 'C#', 'D#', 'F#', 'G#'],
					'Bb': ['Bb', 'C', 'D', 'F', 'G'],
					'C': ['C', 'D', 'E', 'G', 'A'],
					'C#': ['C#', 'D#', 'F', 'G#', 'A#'],
					'D': ['D', 'E', 'F#', 'A', 'B'],
					'Db': ['Db', 'Eb', 'F', 'Ab', 'Bb'],
					'D#': ['D#', 'F', 'G', 'A#', 'C'],
					'E': ['E', 'F#', 'G#', 'B', 'C#'],
					'Eb': ['Eb', 'F', 'G', 'Bb', 'C'],
					'F': ['F', 'G', 'A', 'C', 'D'],
					'F#': ['F#', 'G#', 'A#', 'C#', 'D#'],
					'G': ['G', 'A', 'B', 'D', 'E'],
					'Gb': ['Gb', 'Ab', 'Bb', 'Db', 'Eb'],
					'G#': ['G#', 'A#', 'C', 'D#', 'F']},
			"pentatonic":{'A': ['A', 'C', 'D', 'E', 'G'],
					'Ab': ['Ab', 'B', 'Db', 'Eb', 'Gb'],
					'A#': ['A#', 'C#', 'D#', 'F', 'G#'],
					'B': ['B', 'D', 'E', 'F#', 'A'],
					'Bb': ['Bb', 'Db', 'Eb', 'F', 'Ab'],
					'C': ['C', 'Eb', 'F', 'G', 'Bb'],
					'C#': ['C#', 'E', 'F#', 'G#', 'B'],
					'D': ['D', 'F', 'G', 'A', 'C'],
					'Db': ['Db', 'E', 'Gb', 'Ab', 'B'],
					'D#': ['D#', 'F#', 'G#', 'A#', 'C#'],
					'E': ['E', 'G', 'A', 'B', 'D'],
					'Eb': ['Eb', 'Gb', 'Ab', 'Bb', 'Db'],
					'F': ['F', 'Ab', 'Bb', 'C', 'Eb'],
					'F#': ['F#', 'A', 'B', 'C#', 'E'],
					'G': ['G', 'A#', 'C', 'D', 'F'],
					'Gb': ['Gb', 'A', 'B', 'Db', 'E'],
					'G#': ['G#', 'B', 'C#', 'D#', 'F#']}
					}
midi_nums = {"flats": 
				{'A0': 21,
					'A1': 33,
					'A2': 45,
					'A3': 57,
					'A4': 69,
					'A5': 81,
					'A6': 93,
					'A7': 105,
					'A8': 117,
					'Ab1': 32,
					'Ab2': 44,
					'Ab3': 56,
					'Ab4': 68,
					'Ab5': 80,
					'Ab6': 92,
					'Ab7': 104,
					'Ab8': 116,
					'B0': 23,
					'B1': 35,
					'B2': 47,
					'B3': 59,
					'B4': 71,
					'B5': 83,
					'B6': 95,
					'B7': 107,
					'B8': 119,
					'Bb0': 22,
					'Bb1': 34,
					'Bb2': 46,
					'Bb3': 58,
					'Bb4': 70,
					'Bb5': 82,
					'Bb6': 94,
					'Bb7': 106,
					'Bb8': 118,
					'C1': 24,
					'C2': 36,
					'C3': 48,
					'C4': 60,
					'C5': 72,
					'C6': 84,
					'C7': 96,
					'C8': 108,
					'C9': 120,
					'D1': 26,
					'D2': 38,
					'D3': 50,
					'D4': 62,
					'D5': 74,
					'D6': 86,
					'D7': 98,
					'D8': 110,
					'D9': 122,
					'Db1': 25,
					'Db2': 37,
					'Db3': 49,
					'Db4': 61,
					'Db5': 73,
					'Db6': 85,
					'Db7': 97,
					'Db8': 109,
					'Db9': 121,
					'E1': 28,
					'E2': 40,
					'E3': 52,
					'E4': 64,
					'E5': 76,
					'E6': 88,
					'E7': 100,
					'E8': 112,
					'E9': 124,
					'Eb1': 27,
					'Eb2': 39,
					'Eb3': 51,
					'Eb4': 63,
					'Eb5': 75,
					'Eb6': 87,
					'Eb7': 99,
					'Eb8': 111,
					'Eb9': 123,
					'F1': 29,
					'F2': 41,
					'F3': 53,
					'F4': 65,
					'F5': 77,
					'F6': 89,
					'F7': 101,
					'F8': 113,
					'F9': 125,
					'G1': 31,
					'G2': 43,
					'G3': 55,
					'G4': 67,
					'G5': 79,
					'G6': 91,
					'G7': 103,
					'G8': 115,
					'G9': 127,
					'Gb1': 30,
					'Gb2': 42,
					'Gb3': 54,
					'Gb4': 66,
					'Gb5': 78,
					'Gb6': 90,
					'Gb7': 102,
					'Gb8': 114,
					'Gb9': 126},
			"sharps":
				{'A#0': 22,
						'A#1': 34,
						'A#2': 46,
						'A#3': 58,
						'A#4': 70,
						'A#5': 82,
						'A#6': 94,
						'A#7': 106,
						'A#8': 118,
						'A0': 21,
						'A1': 33,
						'A2': 45,
						'A3': 57,
						'A4': 69,
						'A5': 81,
						'A6': 93,
						'A7': 105,
						'A8': 117,
						'B0': 23,
						'B1': 35,
						'B2': 47,
						'B3': 59,
						'B4': 71,
						'B5': 83,
						'B6': 95,
						'B7': 107,
						'B8': 119,
						'C#1': 25,
						'C#2': 37,
						'C#3': 49,
						'C#4': 61,
						'C#5': 73,
						'C#6': 85,
						'C#7': 97,
						'C#8': 109,
						'C#9': 121,
						'C1': 24,
						'C2': 36,
						'C3': 48,
						'C4': 60,
						'C5': 72,
						'C6': 84,
						'C7': 96,
						'C8': 108,
						'C9': 120,
						'D#1': 27,
						'D#2': 39,
						'D#3': 51,
						'D#4': 63,
						'D#5': 75,
						'D#6': 87,
						'D#7': 99,
						'D#8': 111,
						'D#9': 123,
						'D1': 26,
						'D2': 38,
						'D3': 50,
						'D4': 62,
						'D5': 74,
						'D6': 86,
						'D7': 98,
						'D8': 110,
						'D9': 122,
						'E1': 28,
						'E2': 40,
						'E3': 52,
						'E4': 64,
						'E5': 76,
						'E6': 88,
						'E7': 100,
						'E8': 112,
						'E9': 124,
						'F#1': 30,
						'F#2': 42,
						'F#3': 54,
						'F#4': 66,
						'F#5': 78,
						'F#6': 90,
						'F#7': 102,
						'F#8': 114,
						'F#9': 126,
						'F1': 29,
						'F2': 41,
						'F3': 53,
						'F4': 65,
						'F5': 77,
						'F6': 89,
						'F7': 101,
						'F8': 113,
						'F9': 125,
						'G#1': 32,
						'G#2': 44,
						'G#3': 56,
						'G#4': 68,
						'G#5': 80,
						'G#6': 92,
						'G#7': 104,
						'G#8': 116,
						'G1': 31,
						'G2': 43,
						'G3': 55,
						'G4': 67,
						'G5': 79,
						'G6': 91,
						'G7': 103,
						'G8': 115,
						'G9': 127}
}


class Fifths():
	def __init__(self, key):
		self.key = key
		self.fifths = {"Cmajor": "0",
				"Aminor": "0",
				"Gmajor": "1",
				"Eminor": "1",
				"Dmajor": "2",
				"Bminor":"2",
				"Amajor": "3",
				"F#minor":"3",
				"Emajor": "4",
				"C#minor":"4",
				"Bmajor": "5",
				"G#minor": "5",
				"F#major": "6",
				"D#minor":"6",
				"C#": "7",
				"A#minor": "7",
				"Fmajor": "-1",
				"Dminor":"-1",
				"Bbmajor": "-2",
				"Gminor": "-2",
				"Ebmajor": "-3",
				"Cminor": "-3",
				"Abmajor": "-4",
				"Fminor":"-4",
				"Dbmajor": "-5",
				"Bbminor":"-5",
				"Gbmajor": "-6",
				"Ebminor":"-6" 
				}

class Scale:
	def __init__(self, key, *args):
		self.key = key
		self.rawscale = []
		if 'b' in key or key == 'F' or key == 'C':
			self.rawscale = ["A","Bb","B","C","Db","D","Eb","E","F","Gb","G","Ab"]
		elif '#' in key or key == 'A' 'B' 'D' 'E' or 'G':
			self.rawscale = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]

	def allnotes(self):
		self.allnotes = ["A","Bb","B","C","Db","D","Eb","E","F","Gb",\
                        "G","Ab","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
		return self.allnotes

	"""def chromatic(self):
		self.chromatic = [] #NEW BLANK SCALE
		s = self.rawscale
		keyindex = s.index(self.key)
		k = keyindex
		n = 0 #counter
		for i in range(len(s)):
			try:
				self.chromatic.append(s[k+i])
			except IndexError:
				self.chromatic.append(s[0+n])
				n+=1
		#return self.chromatic"""

"""class Allscales(Scale):
	def __init__(self,key):
		super().__init__(key)
	def all_majorscales():
		return {'A': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],\
		'Ab': ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G'],\
		'A#': ['A#', 'C', 'D', 'D#', 'F', 'G', 'A'],\
		'B': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'],\
		'Bb': ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A'],\
		'C': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],\
		'C#': ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C'],\
		'D': ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],\
		'Db': ['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C'],\
		'D#': ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D'],\
		'E': ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],\
		'Eb': ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D'],\
		'F': ['F', 'G', 'A', 'Bb', 'C', 'D', 'E'],\
		'F#': ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F'],\
		'G': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],\
		'Gb': ['Gb', 'Ab', 'Bb', 'B', 'Db', 'Eb', 'F'],\
		'G#': ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G']}\"""
	
	def major(self):
		s = self.chromatic
		keyindex = s.index(self.key)
		k = keyindex
		self.major =[s[k],s[k+2],s[k+4],s[k+5],s[k+7],s[k+9],s[k+11]]
		#return self.major

	def minor(self):
		s = self.chromatic
		keyindex = s.index(self.key)
		k = keyindex
		self.minor =[s[k],s[k+2],s[k+3],s[k+5],s[k+7],s[k+8],s[k+10]]
		#return self.harmonic_minor

	def melodic_minor(self):
		s = self.chromatic
		keyindex = s.index(self.key)
		k = keyindex
		self.melodic_minor =[s[k], s[k+2],s[k+3],s[k+5],s[k+7],s[k+8],s[k+11]]
		#return self.melodic_minor

	def major_pentatonic(self):
		s = self.major
		keyindex = s.index(self.key)
		k = keyindex
		s = s
		self.major_pentatonic =[s[k], s[k+1],s[k+2], s[k+4],s[k+5]]
		#return self.major_pentatonic

	def minor_pentatonic(self):
		s = self.minor
		keyindex = s.index(self.key)
		k = keyindex
		self.minor_pentatonic =[s[k], s[k+2],s[k+3], s[k+4],s[k+6]]
		#return self.minor_pentatonic
	
	def allscales(self):
		self.chromatic()
		self.major()
		self.minor()
		self.melodic_minor()
		self.major_pentatonic()
		self.minor_pentatonic()
		self.allscales =  [self.chromatic, self.major, self.minor, self.melodic_minor, self.major_pentatonic, self.minor_pentatonic]

		if "allnotes" in args:
			allnotes(self)
			#return(self.allnotes)
		if "chromatic" in args:
			chromatic(self)
			#return(self.chromatic)
		if "major" in args:
			chromatic(self)
			major(self)
			#return(self.major)
		if "harmonic_minor" in args:
			chromatic(self)
			harmonic_minor(self)
			#return(self.harmonic_minor)
		if "melodic_minor" in args:
			chromatic(self)
			melodic_minor(self)
			#return(self.melodic_minor)
		if "major_pentatonic" in args:
			chromatic(self)
			major(self)
			major_pentatonic(self)
			#return(major_pentatonic)
		if "minor_pentatonic" in args:
			chromatic(self)
			harmonic_minor(self)
			minor_pentatonic(self)
			return(minor_pentatonic)

#TODO: MODES, BEBOPS, CLASSES FOR ALL SCALES"""

class Chromatic(Scale):
	def __init__(self,key):
		super().__init__(key)	
		self.chromatic = [] #NEW BLANK SCALE
		s = self.rawscale
		keyindex = s.index(self.key)
		k = keyindex
		n = 0 #counter
		for i in range(len(s)):
			try:
				self.chromatic.append(s[k+i])
			except IndexError:
				self.chromatic.append(s[0+n])
				n+=1
		self.scale = self.chromatic
	#def scale(self):
		#return self.chromatic

class Major(Chromatic):
    def __init__(self, key): 
        super().__init__(key)
        s = self.chromatic
        keyindex = s.index(self.key)
        k = keyindex
        self.major =[s[k], s[k+2],s[k+4],s[k+5],s[k+7],s[k+9],s[k+11]]
        self.scale = self.major
    #def scale(self):
        #return self.maj_scale


class Minor(Chromatic):
    def __init__(self, key):
        super().__init__(key)
        s = self.chromatic
        keyindex = s.index(self.key)
        k = keyindex
        self.minor =[s[k], s[k+2],s[k+3],s[k+5],s[k+7],s[k+8],s[k+10]]
        self.scale = self.minor
	#def scale(self):
        #return self.minor

class MelodicMinor(Chromatic):
    def __init__(self, key):
        super().__init__(key)
        s = self.chromatic
        keyindex = s.index(self.key)
        k = keyindex
        self.melodic_minor =[s[k], s[k+2],s[k+3],s[k+5],s[k+7],s[k+8],s[k+11]]
        self.scale = self.melodic_minor
    #def scale(self):
        #return self.melodic_minor

class MajorPentatonic(Major):
	def __init__(self, key):
		super().__init__(key)
		s = self.major
		keyindex = s.index(self.key)
		k = keyindex
		self.major_pentatonic =[s[k], s[k+1],s[k+2], s[k+4],s[k+5]]
		self.scale = self.major_pentatonic

class MinorPentatonic(Minor):
	def __init__(self, key):
		super().__init__(key)
		s = self.minor
		keyindex = s.index(self.key)
		k = keyindex
		self.minor_pentatonic =[s[k], s[k+2],s[k+3], s[k+4],s[k+6]]
		self.scale = self.minor_pentatonic
