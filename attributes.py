#! python 
#! note attributes - for adding attributes to generated exercises

import config
from pprint import pprint

def setattr():
    exercise_list = config.exercise_list
    exercises_withattr_list = config.exercises_withattr_list
    if config.clef == "G":
        oct = "4"
    if config.clef == "F":
        oct = "3"
    dur = "1" #TODO MAKE THESE UPDATEABLE FROM NOTEREADER
    voice = "1"  
    notetype = config.notetype
    stem = "up"


    temp_dict = {}
    for i in range(len(exercise_list)):
        r = 1
        for n in range(len(exercise_list[i])):
            ex = exercise_list[i][n]
            #tag = str(id(ex))
            if ex in temp_dict.keys():
                temp_dict[ ex + ("*" * r)] = [oct,dur,voice,notetype,stem]
                r += 1
            else:
                temp_dict[ex] = [oct,dur,voice,notetype,stem]
        exercises_withattr_list[str(i+1)]=temp_dict
        temp_dict = {}

    #pprint(config.exercises_withattr_list) #for checking work