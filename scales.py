#!python
# Scales - a bunch of scales for use in auto-generated scripts
allnotes_master = ["A","Bflat","B","C","Dflat","D","Eflat","E","F","Gflat",\
    			"G","Aflat","Asharp","B","C","Csharp","D","Dsharp","E","F","Fsharp","G","Gsharp"]

allscales =	{"major" : {'A': ['A', 'B', 'Csharp', 'D', 'E', 'Fsharp', 'Gsharp'],
					'Aflat': ['Aflat', 'Bflat', 'C', 'Dflat', 'Eflat', 'F', 'G'],
					'Asharp': ['Asharp', 'C', 'D', 'Dsharp', 'F', 'G', 'A'],
					'B': ['B', 'Csharp', 'Dsharp', 'E', 'Fsharp', 'Gsharp', 'Asharp'],
					'Bflat': ['Bflat', 'C', 'D', 'Eflat', 'F', 'G', 'A'],
					'C': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
					'Csharp': ['Csharp', 'Dsharp', 'F', 'Fsharp', 'Gsharp', 'Asharp', 'C'],
					'D': ['D', 'E', 'Fsharp', 'G', 'A', 'B', 'Csharp'],
					'Dflat': ['Dflat', 'Eflat', 'F', 'Gflat', 'Aflat', 'Bflat', 'C'],
					'Dsharp': ['Dsharp', 'F', 'G', 'Gsharp', 'Asharp', 'C', 'D'],
					'E': ['E', 'Fsharp', 'Gsharp', 'A', 'B', 'Csharp', 'Dsharp'],
					'Eflat': ['Eflat', 'F', 'G', 'Aflat', 'Bflat', 'C', 'D'],
					'F': ['F', 'G', 'A', 'Bflat', 'C', 'D', 'E'],
					'Fsharp': ['Fsharp', 'Gsharp', 'Asharp', 'B', 'Csharp', 'Dsharp', 'F'],
					'G': ['G', 'A', 'B', 'C', 'D', 'E', 'Fsharp'],
					'Gflat': ['Gflat', 'Aflat', 'Bflat', 'B', 'Dflat', 'Eflat', 'F'],
					'Gsharp': ['Gsharp', 'Asharp', 'C', 'Csharp', 'Dsharp', 'F', 'G']},
			"minor": {'A': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
					'Aflat': ['Aflat', 'Bflat', 'B', 'Dflat', 'Eflat', 'E', 'Gflat'],
					'Asharp': ['Asharp', 'C', 'Csharp', 'Dsharp', 'F', 'Fsharp', 'Gsharp'],
					'B': ['B', 'Csharp', 'D', 'E', 'Fsharp', 'G', 'A'],
					'Bflat': ['Bflat', 'C', 'Dflat', 'Eflat', 'F', 'Gflat', 'Aflat'],
					'C': ['C', 'D', 'Eflat', 'F', 'G', 'Aflat', 'Bflat'],
					'Csharp': ['Csharp', 'Dsharp', 'E', 'Fsharp', 'Gsharp', 'A', 'B'],
					'D': ['D', 'E', 'F', 'G', 'A', 'Asharp', 'C'],
					'Dflat': ['Dflat', 'Eflat', 'E', 'Gflat', 'Aflat', 'A', 'B'],
					'Dsharp': ['Dsharp', 'F', 'Fsharp', 'Gsharp', 'Asharp', 'B', 'Csharp'],
					'E': ['E', 'Fsharp', 'G', 'A', 'B', 'C', 'D'],
					'Eflat': ['Eflat', 'F', 'Gflat', 'Aflat', 'Bflat', 'B', 'Dflat'],
					'F': ['F', 'G', 'Aflat', 'Bflat', 'C', 'Dflat', 'Eflat'],
					'Fsharp': ['Fsharp', 'Gsharp', 'A', 'B', 'Csharp', 'D', 'E'],
					'G': ['G', 'A', 'Asharp', 'C', 'D', 'Dsharp', 'F'],
					'Gflat': ['Gflat', 'Aflat', 'A', 'B', 'Dflat', 'D', 'E'],
					'Gsharp': ['Gsharp', 'Asharp', 'B', 'Csharp', 'Dsharp', 'E', 'Fsharp']},
			"melodic minor":{'A': ['A', 'B', 'C', 'D', 'E', 'F', 'Gsharp'],
					'Aflat': ['Aflat', 'Bflat', 'B', 'Dflat', 'Eflat', 'E', 'G'],
					'Asharp': ['Asharp', 'C', 'Csharp', 'Dsharp', 'F', 'Fsharp', 'A'],
					'B': ['B', 'Csharp', 'D', 'E', 'Fsharp', 'G', 'Asharp'],
					'Bflat': ['Bflat', 'C', 'Dflat', 'Eflat', 'F', 'Gflat', 'A'],
					'C': ['C', 'D', 'Eflat', 'F', 'G', 'Aflat', 'B'],
					'Csharp': ['Csharp', 'Dsharp', 'E', 'Fsharp', 'Gsharp', 'A', 'C'],
					'D': ['D', 'E', 'F', 'G', 'A', 'Asharp', 'Csharp'],
					'Dflat': ['Dflat', 'Eflat', 'E', 'Gflat', 'Aflat', 'A', 'C'],
					'Dsharp': ['Dsharp', 'F', 'Fsharp', 'Gsharp', 'Asharp', 'B', 'D'],
					'E': ['E', 'Fsharp', 'G', 'A', 'B', 'C', 'Dsharp'],
					'Eflat': ['Eflat', 'F', 'Gflat', 'Aflat', 'Bflat', 'B', 'D'],
					'F': ['F', 'G', 'Aflat', 'Bflat', 'C', 'Dflat', 'E'],
					'Fsharp': ['Fsharp', 'Gsharp', 'A', 'B', 'Csharp', 'D', 'F'],
					'G': ['G', 'A', 'Asharp', 'C', 'D', 'Dsharp', 'Fsharp'],
					'Gflat': ['Gflat', 'Aflat', 'A', 'B', 'Dflat', 'D', 'F'],
					'Gsharp': ['Gsharp', 'Asharp', 'B', 'Csharp', 'Dsharp', 'E', 'G']},
			"major pentatonic":{'A': ['A', 'B', 'Csharp', 'E', 'Fsharp'],
					'Aflat': ['Aflat', 'Bflat', 'C', 'Eflat', 'F'],
					'Asharp': ['Asharp', 'C', 'D', 'F', 'G'],
					'B': ['B', 'Csharp', 'Dsharp', 'Fsharp', 'Gsharp'],
					'Bflat': ['Bflat', 'C', 'D', 'F', 'G'],
					'C': ['C', 'D', 'E', 'G', 'A'],
					'Csharp': ['Csharp', 'Dsharp', 'F', 'Gsharp', 'Asharp'],
					'D': ['D', 'E', 'Fsharp', 'A', 'B'],
					'Dflat': ['Dflat', 'Eflat', 'F', 'Aflat', 'Bflat'],
					'Dsharp': ['Dsharp', 'F', 'G', 'Asharp', 'C'],
					'E': ['E', 'Fsharp', 'Gsharp', 'B', 'Csharp'],
					'Eflat': ['Eflat', 'F', 'G', 'Bflat', 'C'],
					'F': ['F', 'G', 'A', 'C', 'D'],
					'Fsharp': ['Fsharp', 'Gsharp', 'Asharp', 'Csharp', 'Dsharp'],
					'G': ['G', 'A', 'B', 'D', 'E'],
					'Gflat': ['Gflat', 'Aflat', 'Bflat', 'Dflat', 'Eflat'],
					'Gsharp': ['Gsharp', 'Asharp', 'C', 'Dsharp', 'F']},
			"pentatonic":{'A': ['A', 'C', 'D', 'E', 'G'],
					'Aflat': ['Aflat', 'B', 'Dflat', 'Eflat', 'Gflat'],
					'Asharp': ['Asharp', 'Csharp', 'Dsharp', 'F', 'Gsharp'],
					'B': ['B', 'D', 'E', 'Fsharp', 'A'],
					'Bflat': ['Bflat', 'Dflat', 'Eflat', 'F', 'Aflat'],
					'C': ['C', 'Eflat', 'F', 'G', 'Bflat'],
					'Csharp': ['Csharp', 'E', 'Fsharp', 'Gsharp', 'B'],
					'D': ['D', 'F', 'G', 'A', 'C'],
					'Dflat': ['Dflat', 'E', 'Gflat', 'Aflat', 'B'],
					'Dsharp': ['Dsharp', 'Fsharp', 'Gsharp', 'Asharp', 'Csharp'],
					'E': ['E', 'G', 'A', 'B', 'D'],
					'Eflat': ['Eflat', 'Gflat', 'Aflat', 'Bflat', 'Dflat'],
					'F': ['F', 'Aflat', 'Bflat', 'C', 'Eflat'],
					'Fsharp': ['Fsharp', 'A', 'B', 'Csharp', 'E'],
					'G': ['G', 'Asharp', 'C', 'D', 'F'],
					'Gflat': ['Gflat', 'A', 'B', 'Dflat', 'E'],
					'Gsharp': ['Gsharp', 'B', 'Csharp', 'Dsharp', 'Fsharp']}
					}


class Fifths:
	def __init__(self, key):
		self.key = key
		self.fifths = {"Cmajor": "0",
				"Aminor": "0",
				"Gmajor": "1",
				"Eminor": "1",
				"Dmajor": "2",
				"Bminor":"2",
				"Amajor": "3",
				"Fsharpminor":"3",
				"Emajor": "4",
				"Csharpminor":"4",
				"Bmajor": "5",
				"Gsharpminor": "5",
				"Fsharpmajor": "6",
				"Dsharpminor":"6",
				"Csharp": "7",
				"Asharpminor": "7",
				"Fmajor": "-1",
				"Dminor":"-1",
				"Bflatmajor": "-2",
				"Gminor": "-2",
				"Eflatmajor": "-3",
				"Cminor": "-3",
				"Aflatmajor": "-4",
				"Fminor":"-4",
				"Dflatmajor": "-5",
				"Bflatminor":"-5",
				"Gflatmajor": "-6",
				"Eflatminor":"-6" 
				}

class Scale:
	def __init__(self, key, *args):
		self.key = key
		self.rawscale = []
		if 'flat' in key or key == 'F' or key == 'C':
			self.rawscale = ["A","Bflat","B","C","Dflat","D","Eflat","E","F","Gflat","G","Aflat"]
		elif 'sharp' in key or key == 'A' 'B' 'D' 'E' or 'G':
			self.rawscale = ["A","Asharp","B","C","Csharp","D","Dsharp","E","F","Fsharp","G","Gsharp"]

	def allnotes(self):
		self.allnotes = ["A","Bflat","B","C","Dflat","D","Eflat","E","F","Gflat",\
                        "G","Aflat","Asharp","B","C","Csharp","D","Dsharp","E","F","Fsharp","G","Gsharp"]
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
		return {'A': ['A', 'B', 'Csharp', 'D', 'E', 'Fsharp', 'Gsharp'],\
		'Aflat': ['Aflat', 'Bflat', 'C', 'Dflat', 'Eflat', 'F', 'G'],\
		'Asharp': ['Asharp', 'C', 'D', 'Dsharp', 'F', 'G', 'A'],\
		'B': ['B', 'Csharp', 'Dsharp', 'E', 'Fsharp', 'Gsharp', 'Asharp'],\
		'Bflat': ['Bflat', 'C', 'D', 'Eflat', 'F', 'G', 'A'],\
		'C': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],\
		'Csharp': ['Csharp', 'Dsharp', 'F', 'Fsharp', 'Gsharp', 'Asharp', 'C'],\
		'D': ['D', 'E', 'Fsharp', 'G', 'A', 'B', 'Csharp'],\
		'Dflat': ['Dflat', 'Eflat', 'F', 'Gflat', 'Aflat', 'Bflat', 'C'],\
		'Dsharp': ['Dsharp', 'F', 'G', 'Gsharp', 'Asharp', 'C', 'D'],\
		'E': ['E', 'Fsharp', 'Gsharp', 'A', 'B', 'Csharp', 'Dsharp'],\
		'Eflat': ['Eflat', 'F', 'G', 'Aflat', 'Bflat', 'C', 'D'],\
		'F': ['F', 'G', 'A', 'Bflat', 'C', 'D', 'E'],\
		'Fsharp': ['Fsharp', 'Gsharp', 'Asharp', 'B', 'Csharp', 'Dsharp', 'F'],\
		'G': ['G', 'A', 'B', 'C', 'D', 'E', 'Fsharp'],\
		'Gflat': ['Gflat', 'Aflat', 'Bflat', 'B', 'Dflat', 'Eflat', 'F'],\
		'Gsharp': ['Gsharp', 'Asharp', 'C', 'Csharp', 'Dsharp', 'F', 'G']}\"""
	
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
