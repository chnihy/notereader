#! python3
# grid maker - a program to make musical grid exercises
#TODO Clean up names, 'timsigbeats' > 'beats' etc...
#TODO Add data classes to data > and move validation to data.py module
from copy import copy 
from pprint import pprint
import config, time
import data


def gridmaker(beats, beat_type, a, b, select_grid, reversing):
    #A and B 
    subdivs = {"4":"quarter", \
            "3":"triplet", \
            "8":"eighth", \
            "12":"16thtriplet",\
            "16":"16th", \
            "24":"32ndtriplet",\
            "32":"32nd"\
            }
    a = subdivs[a]
    b = subdivs[b]
    
    #DIVISIONS/DURATIONS - For XML/MUSESCORE
    divisions_key = {"quarter":"1",
                    "eighth":"2",
                    "16th":"4",
                    "32nd":"8",
                    "4":"1"} #SEE BOTTOM OF PAGE FOR CLIPPED OLD DIVs STUFF FOR MUSESCORE
    
    #MAKING CHUNKS
    a_divs = int(divisions_key[a])
    b_divs = int(divisions_key[b])
    chunk_a = [] #these are like list wrappers for groups of notes: 
    chunk_b = [] #same...ex: ("eighth","eighth") or ("16th","16th","16th","16th")
    for q in range(b_divs): 
        chunk_b.append(b)
    for p in range(a_divs):
        chunk_a.append(a)
    
    #MAKING FULL MEASURES of A and B (FOR GPM)
    measure_a = []
    measure_b = []
    for beat in beats: 
        measure_a.append(chunk_a)
        measure_b.append(chunk_b) #TODO Gonna break with 7/8


    grid_measure_index = []
    
    #YE HOLY ALGORITHMS
    def MovingGrid(beats):
        measure = []
        
        if reversing == True:
            #n = 1
            for v in range(beats): 
                for i in range(beats):
                    measure.append(chunk_b)
                measure[v]=chunk_a
                grid_measure_index.append(measure)
                grid_measure_index.append(measure[::-1])
                measure = []
        #else:
        for v in range(beats): #creating measures and adding to ex_list
            for i in range(beats): #creating measure of chunk_b's. Example: [['chunk_b'],['chunk_b'],['chunk_b'],['chunk_b']]
                measure.append(chunk_b)
            measure[v]=chunk_a #add var to measure of chunk_b's
            grid_measure_index.append(measure) #add meas to exercise list
            if reversing == True:
                grid_measure_index.append(measure[::-1])
            measure = [] #clearing
        
        #pprint(grid_measure_index) #testing...    
    
    def StackingGrid(beats):
        measure = []

        for i in range(beats): #bed
	        measure.append(chunk_b)

        for n in range(len(measure)): #variable
            measure[n] = chunk_a
            grid_measure_index.append(copy(measure))
            if reversing == True:
                grid_measure_index.append(copy(measure[::-1]))

        #pprint(grid_measure_index)    
    
    #PRINTING GRIDS
    if select_grid == "1":
        MovingGrid(int(beats))

    if select_grid == "2":
        StackingGrid(int(beats))

    #UPDATE CONFIG
    config.grid_measure_index = grid_measure_index
    config.grid_measure_a = measure_a
    config.grid_measure_b = measure_b
    return(grid_measure_index)

def run():
    while True:
        #TIMESIG_BEATS & beatType
        beats = input("Enter Beats: ")
        beat_type = input(f"Enter beat type: {beats}/")

        #SELECT_A
        subdivs = {"4":"quarter", \
                "3":"triplet", \
                "8":"eighth", \
                "12":"16thtriplet",\
                "16":"16th", \
                "24":"32ndtriplet",\
                "32":"32nd"\
                }
        while True:
            select_a = input("Enter VARIABLE (ex 4, 8 or 16): ")
            try:
                if select_a in subdivs.keys():
                    a = subdivs[select_a]
                    break
                if select_a not in subdivs.keys():
                    raise Exception
                else:
                    continue
            except Exception:
                print("ERROR enter a valid rhythm")
                continue
        #SELECT_B
        while True:
            select_b = input("Enter BED: ")
            try:
                if select_b in subdivs.keys():
                    b = subdivs[select_b]
                    break
                if select_b not in subdivs.keys():
                    raise Exception
                else:
                    continue
            except Exception:
                print("ERROR enter a valid rhythm")
                continue
        
        #SELECT GRID TYPE
        while True:
            select_grid = input("Select Grid Type: 1.Moving or 2.Stacking: ")
            if int(select_grid) == 1 or int(select_grid) == 2:
                break
            else:
                continue
        while True:
            reversing = False
            yorn = input("Reversing Grid? Y or N: ")
            if yorn.lower() == "y":
                reversing = True
                break
            if yorn.lower() == "n":
                break
            else:
                continue

        grid_measure_index = gridmaker(beats, beat_type, a, b, select_grid, reversing)
        
        return(grid_measure_index)
        
        """
        print(f"GRID TYPE: {select_grid} ")
        print(f"REVERSING: {reversing}")
        print(f"VARIABLE: {a}")
        print(f"BED: {b}")
        while True:
            yorn = input("Run Gridmaker? Y or N? ")
            if yorn == "y":
                gridmaker(beats, beat_type, a, b, select_grid, reversing)
            if yorn == "n": 
                break
            else:
                continue
        continue"""













####THIS IS FOR MUSESCORE######
"""if int(select_a)>int(select_b):  #bigger means a SMALLER subdiv. > if A is the smallest subdiv...
        smaller_divs = a
        dur_a = "1"
        dur_b = str(int(divisions_key[a])/int(divisions_key[b]))
        dur_b = dur_b[0] #getting rid of float
    else:
        smaller_divs = b
        dur_b = "1"
        dur_a = str(int(divisions_key[b])/int(divisions_key[a]))
        dur_a = dur_a[0]
    config.divisions = divisions_key[smaller_divs] #divisions is how many subd's per beat, important for xml
    """
