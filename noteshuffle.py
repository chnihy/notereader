#!python
# note shuffle, a first version of a shuffling program
import random, copy, scales, math, config
from pprint import pprint

def shuff(x): #JUST MAKING A SHORTCUT FOR SHUFFLING
    random.shuffle(x)
    return(x)

def noteshuffle(scale, measure_length, num_of_exercises):
    #SAMPLESIZE MEANS HOW MANY UNIQUE PITCHES
    #MEASURE LENGTH IS THE NUMBER OF NOTES THAT CAN FIT IN ONE MEASURE
    if int(measure_length) <= len(scale):
        master = random.sample(scale, k=measure_length) #TAKING A RANDOM SAMPLE OF SIZE K FROM SCALE
    else:
        master = random.sample((scale*measure_length), k = measure_length) #IF S>SCALE, MAKE MULTIPLE SCALES SO THERE CAN BE DUP'S
    config.master = master
    biglist = [] #BIG BLANK LIST 
    config.biglist = []
    if measure_length <= len(scale):
        while len(biglist)<(math.factorial(measure_length)): 
            var = copy.copy(master)
            shuff(var)
            tvar = tuple((var)) #MAKING THE SHUFFLED SET OF NOTES A TUPLE, SO THAT BIGLIST CAN BE MADE A SET.
            if tvar not in biglist:
                biglist.append(tvar)
            else:
                continue
    else:
        while len(biglist)<10000: 
            var = copy.copy(master)
            shuff(var)
            tvar = tuple((var)) #MAKING THE SHUFFLED SET OF NOTES A TUPLE, SO THAT BIGLIST CAN BE MADE A SET.
            biglist.append(tvar)    
        biglist = set(biglist) #making biglist a set to remove duplicates

    # CREATING CONFIG EXERCISE LISTS
    config.exercise_list = []
    while True:
        try:
            for item in set((random.sample(biglist, k=num_of_exercises))):
                config.exercise_list.append(item)
            break
        except ValueError:
            print("Error, enter a smaller number of exercises")
            continue