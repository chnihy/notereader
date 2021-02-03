#!python
# Scales - a bunch of scales for use in auto-generated scripts
allnotes_master = ["A","Bflat","B","C","Dflat","D","Eflat","E","F","Gflat",\
    			"G","Aflat","Asharp","B","C","Csharp","D","Dsharp","E","F","Fsharp","G","Gsharp"]

class Key:
	def __init__(self, key):
		self.key = key
		self.fifths = {"C": "0", \
				"G": "1", \
				"D": "2",\
				"A": "3", \
				"E": "4", \
				"B": "5", \
				"Fsharp": "6", \
				"Csharp": "7", \
				"F": "-1", \
				"Bflat": "-2", \
				"Eflat": "-3", \
				"Aflat": "-4", \
				"Dflat": "-5", \
				"Gflat": "-6" }

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

	def chromatic(self):
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
		#return self.chromatic

	def major(self):
		s = self.chromatic
		keyindex = s.index(self.key)
		k = keyindex
		self.major =[s[k], s[k+2],s[k+4],s[k+5],s[k+7],s[k+9],s[k+11]]
		#return self.major

	def minor(self):
		s = self.chromatic
		keyindex = s.index(self.key)
		k = keyindex
		self.minor =[s[k], s[k+2],s[k+3],s[k+5],s[k+7],s[k+8],s[k+10]]
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

		"""if "allnotes" in args:
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
			return(minor_pentatonic)"""

#TODO: MODES, BEBOPS, CLASSES FOR ALL SCALES

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
