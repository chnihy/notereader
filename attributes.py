#! python 
#! note attributes - for adding attributes to generated exercises

import config
from pprint import pprint

def setattr():
    exercise_list = config.exercise_list
    
    exercises_withattr_list = config.exercises_withattr_list
    
    notetype = config.notetype
    
    if config.clef == "Grand Staff":
        exercise_list_staff2 = config.exercise_list_staff2
        exercises_withattr_list_staff2 = config.exercises_withattr_list_staff2
        notetype_staff2 = config.notetype_staff2
        notetype_staff1 = config.notetype_staff1
    
    if config.grid == "yes":
        exercise_list = config.grid_exercise_list

    #OCTAVES
    oct = ""
    if config.clef == "G" or config.clef == "Grand Staff":
        oct = "4"
    
    if config.clef == "F":
        oct = "3"
    
    #DIVISIONS AND DURATIONS
    divs_keys = {"quarter":"1",\
                "eighth":"2",\
                "16th":"4",\
                "32nd":"8"}
    
    if config.clef == "Grand Staff":
        divs = divs_keys[notetype] #MASTER DIVISIONS - FROM SMALLER SUBDIV
        config.divs = divs
        
        if config.notetype_staff1 == config.notetype: #STAFF 1 IS SMALLER SUBDIV
            dur_staff1 = "1"
            config.test = dur_staff1
        
        if config.notetype_staff1 != config.notetype: #STAFF 2 IS SMALLER SUBDIV
            dur_staff1 = str(int(divs) / int(divs_keys[config.notetype_staff1]))[0]
            config.test = dur_staff1
        
        if config.notetype_staff2 == config.notetype:
            dur_staff2 = "1"
            config.test2 = dur_staff2
        
        if config.notetype_staff2 != config.notetype:
            dur_staff2 = str(int(divs) / int(divs_keys[config.notetype_staff2]))[0]
            config.test2 = dur_staff2
    
    else:
        dur_staff1 = "1"
        
    if config.grid == "yes":
        dur_a = config.dur_a
        dur_b = config.dur_b
    

    #VOICE, STEMS, STAFF NUMBERS
    voice = "1"  
    stem = "up"
    staff_num = "1"

    #ATTRIBUTE LIST FOR FIRST OR ONLY STAFF
    if config.grid != "yes":
        temp_dict = {}
        for i in range(len(exercise_list)):
            if config.clef == "Grand Staff":
                notetype = notetype_staff1
            r = 1
            for n in range(len(exercise_list[i])):
                ex = exercise_list[i][n]
                if ex in temp_dict.keys():
                    temp_dict[ex + ("*" * r)] = [oct, dur_staff1, voice, notetype, stem, staff_num]
                    r += 1   
                else:
                    temp_dict[ex] = [oct, dur_staff1, voice, notetype, stem, staff_num]
            exercises_withattr_list[str(i+1)]=temp_dict
            temp_dict = {}
        
    #ATTRIBUTE FOR SECOND STAFF IF IT EXISTS
        if config.clef == "Grand Staff":
            oct = "3"
            stem = "down"
            staff_num = "2"
            temp_dict = {}
            for i in range(len(exercise_list_staff2)):
                r = 1
                for n in range(len(exercise_list_staff2[i])):
                    ex = exercise_list_staff2[i][n]
                    if ex in temp_dict.keys():
                        temp_dict[ex + ("*" * r)] = [oct, dur_staff2, voice, notetype_staff2, stem, staff_num]
                        r += 1
                    else:
                        temp_dict[ex] = [oct, dur_staff2, voice, notetype_staff2, stem, staff_num]
                exercises_withattr_list_staff2[str(i+1)]=temp_dict    
                temp_dict = {}
    