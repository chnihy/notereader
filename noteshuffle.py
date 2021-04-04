#!python
# note shuffle, a first version of a shuffling program
import random, scales, math, config
from pprint import pprint
from copy import copy

def shuff(x): #JUST MAKING A SHORTCUT FOR SHUFFLING
    random.shuffle(x)
    return(x)

def noteshuffle(scale, sample_size, measure_length, exercises):
    master = config.master

    #MAKING OUR SAMPLE SET
    while True:
        try:
            if int(sample_size) < len(scale):
                sample = random.sample(scale, k=sample_size)
                #print(f"1.NOTESHUFF: SAMPLE: {sample}")
            if int(sample_size) == len(scale) or str(sample_size) == 'max':
                sample = scale
                #print(f"2.NOTESHUFF: SAMPLE: {sample}")
            break
        except ValueError:
            print(f"ERROR! Value Error in Noteshuffle Module")
            continue
    config.sample = sample    
    
    #MAKING OUR MASTER MEASURE
    if measure_length == len(sample):
        for note in sample:
            master.append(note)
    if measure_length > len(sample):
        #ADD ALL OF THE NOTES OF THE SAMPLE FIRST
        for note in sample: 
            master.append(note)
        duplicates = int((measure_length)//(math.sqrt(measure_length)))
        config.duplicates = duplicates
        while True: 
            shuff(sample) #SHUFFLING THE REST
            newitem = sample[0]
            if master.count(newitem) > duplicates:
                continue
            master.append(newitem)
            if len(master) == measure_length:
                break
    if measure_length < len(sample): #TODO THIS WILL NEED MORE WORK, SEE ABOVE
        for note in sample:
            master.append(note)
            if len(master) == measure_length:
                break
            else:
                continue   
    config.master = master

    #MAKING EMPTY EXERCISE LISTS
    biglist = []
    biglist_staff2 = []
    
    #SINGLE STAFF
    if config.clef != "Grand Staff":
        if measure_length < len(sample):
            smaller_master = random.sample(sample, k=measure_length)
            while True:
                measure = copy(smaller_master)
                shuff(measure)
                tuple_measure = tuple((measure)) #MAKING THE SHUFFLED SET OF NOTES A TUPLE, SO THAT BIGLIST CAN BE MADE A SET.
                if tuple_measure not in biglist:
                    biglist.append(tuple_measure)
                if len(biglist) == int(exercises): #math.factorial(measure_length):
                    break
        if measure_length == len(sample):
            while True:
                measure = copy(master)
                shuff(measure)
                tuple_measure = tuple((measure)) #MAKING THE SHUFFLED SET OF NOTES A TUPLE, SO THAT BIGLIST CAN BE MADE A SET.
                if tuple_measure not in biglist:
                    biglist.append(tuple_measure)
                if len(biglist) == int(exercises): #math.factorial(measure_length):
                    break
        if measure_length > len(sample):
            while True:
                measure = copy(master)
                shuff(measure)
                tuple_measure = tuple((measure)) #MAKING THE SHUFFLED SET OF NOTES A TUPLE, SO THAT BIGLIST CAN BE MADE A SET.
                if tuple_measure not in biglist:
                    biglist.append(tuple_measure)
                if len(biglist) == int(exercises): #100:
                    break
                else:
                    continue
    
    #MAKING EXERCISE LIST FOR STAFF1
    if config.clef == "Grand Staff":
        measure_length = config.measure_length_staff1
        if measure_length < len(sample):
                smaller_master = random.sample(sample, k=measure_length)
                while True:
                    measure = copy(smaller_master)
                    shuff(measure)
                    tuple_measure = tuple((measure)) #MAKING THE SHUFFLED SET OF NOTES A TUPLE, SO THAT BIGLIST CAN BE MADE A SET.
                    if tuple_measure not in biglist:
                        biglist.append(tuple_measure)
                    if len(biglist) == int(exercises): #math.factorial(measure_length):
                        break
        if measure_length == len(sample):
            if measure_length < config.measure_length_staff2:
                smaller_master = random.sample(master, k=measure_length)
                while True:
                    measure = copy(smaller_master)
                    shuff(measure)
                    tuple_measure = tuple((measure)) #MAKING THE SHUFFLED SET OF NOTES A TUPLE, SO THAT BIGLIST CAN BE MADE A SET.
                    if tuple_measure not in biglist:
                        biglist.append(tuple_measure)
                    if len(biglist) == int(exercises): #math.factorial(measure_length)
                        break
            else:
                while True:
                    measure = copy(master)
                    shuff(measure)
                    tuple_measure = tuple((measure)) #MAKING THE SHUFFLED SET OF NOTES A TUPLE, SO THAT BIGLIST CAN BE MADE A SET.
                    if tuple_measure not in biglist:
                        biglist.append(tuple_measure)
                    if len(biglist) == int(exercises): #math.factorial(measure_length):
                        break
        if measure_length > len(sample):
            if measure_length < config.measure_length_staff2:
                smaller_sample = random.sample(master, k=measure_length)
                smaller_master = []
                for item in smaller_sample:
                    smaller_master.append(item)
                while True:
                    measure = copy(smaller_master)
                    shuff(measure)
                    tuple_measure = tuple((measure)) #MAKING THE SHUFFLED SET OF NOTES A TUPLE, SO THAT BIGLIST CAN BE MADE A SET.
                    if tuple_measure not in biglist:
                        biglist.append(tuple_measure)
                    if len(biglist) == int(exercises): #math.factorial(measure_length)
                        break
            else:
                while True:
                    measure = copy(master)
                    shuff(measure)
                    tuple_measure = tuple((measure)) #MAKING THE SHUFFLED SET OF NOTES A TUPLE, SO THAT BIGLIST CAN BE MADE A SET.
                    if tuple_measure not in biglist:
                        biglist.append(tuple_measure)
                    if len(biglist) == int(exercises):
                        break
                    else:
                        continue
    for item in biglist: #(random.sample(biglist, k=exercises)): #ADDING THE EXERCISE TO THE CONFIG
        config.exercise_list.append(item)
    
    # APPENDING EXERCISE LIST IF STAFF2 EXISTS
    if config.clef =="Grand Staff":
        measure_length = config.measure_length_staff2
        biglist = biglist_staff2
        
        if measure_length < len(sample):
            sample = random.sample(sample, k=measure_length)
            master = []
            for item in sample:
                master.append(item)

        if measure_length == len(sample):
            while True:
                measure = copy(master)
                shuff(measure)
                tuple_measure = tuple((measure)) #MAKING THE SHUFFLED SET OF NOTES A TUPLE, SO THAT BIGLIST CAN BE MADE A SET.
                if tuple_measure not in biglist:
                    biglist.append(tuple_measure)
                if len(biglist) == int(exercises): #math.factorial(measure_length):
                    break
        
        if measure_length > len(sample):
            if measure_length < config.measure_length_staff1:
                smaller_master2 = random.sample(master, k=measure_length)
                """smaller_master2 = []
                for item in smaller_sample2:
                    smaller_master2.append(item)"""
                while True:
                    measure = copy(smaller_master2)
                    shuff(measure)
                    tuple_measure = tuple((measure)) #MAKING THE SHUFFLED SET OF NOTES A TUPLE, SO THAT BIGLIST CAN BE MADE A SET.
                    if tuple_measure not in biglist:
                        biglist.append(tuple_measure)
                    if len(biglist) == int(exercises): #math.factorial(measure_length)
                        break
            else:
                while True:
                    measure = copy(master)
                    shuff(measure)
                    tuple_measure = tuple((measure)) #MAKING THE SHUFFLED SET OF NOTES A TUPLE, SO THAT BIGLIST CAN BE MADE A SET.
                    if tuple_measure not in biglist:
                        biglist.append(tuple_measure)
                    if len(biglist) == int(exercises): #100:
                        break
                    else:
                        continue
        for item in biglist: #(random.sample(biglist, k=exercises)): #ADDING THE EXERCISE TO THE CONFIG
            config.exercise_list_staff2.append(item)