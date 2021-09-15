#python
#data validation for program - testing mostly

#DATA TOP CLASS
class Data:
	def __init__(self):
		pass

#TIME SUBCLASS
class Time:
	def __init__(self, beats, beat_type):
		self.beats = beats
		if str(beats) != "4":
			print(f"You need to enter 4 for BEATS")
			raise ValueError
		else:
			pass
		self.beat_type = beat_type
		if str(beat_type) != "4":
			print(f"Sorry, you need to enter the number 4 for BEAT TYPE")
		else:
			pass
		self.timesig = f"{beats}/{beat_type}"
	
	def update(self, *args):
		if 'beats' in args:
			self.beats = input("Enter new value: ")
		if 'beat_type' in args:
			self.beat_type = input("Enter new value: ")
		else:
			pass

#NOTES SUBCLASS
