#!python
#testing gmpm sandbox
from pprint import pprint
from copy import copy
import config

test = [
		[["a","a","a","a"],["b","b"],["b","b"],["b","b"]],
		[["b","b"],["a","a","a","a"],["b","b"],["b","b"]],
		[["b","b"],["b","b"],["a","a","a","a"],["b","b"]],
		[["b","b"],["b","b"],["b","b"],["a","a","a","a"]]
		]

for measure in range(len(test)):
	measure_counter = 0
	for chunk_index in range(len(test[measure_counter])):
		print(" ")
		for note_index in range(len(test[measure_counter][chunk_index])):
			print(test[measure_counter][chunk_index][note_index], end="")

