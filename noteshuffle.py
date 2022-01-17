#!python
# Note shuffling module
# Get a single random note or a list

from random import randint
import random, config

# Random note selector function
def get_random_note(scale):
    random_note = scale[randint(0, len(scale)-1)]
    return random_note


# Returns a random sample list of notes
def get_sample_list(sample_size, scale):
    counter = 0
    sample_list = []
    
    # No need to shuffle if they're the same size
    if sample_size == len(scale):
        sample_list = scale

    else:
        while True:
            note = get_random_note(scale)
            
            # Remove duplicates
            if note not in sample_list:
                sample_list.append(note)
                counter += 1
            
            else:
                continue
            
            if counter == sample_size:
                break
    
    return sample_list


