#! python3
# Exercise Generator - creates exercises of shuffled notes

from noteshuffle import get_random_note
from noteshuffle import get_sample_list
import config

def run():
    # Measure length calculator function
    def calculate_measure_length(beats, rhythm):
        rhythm_nums = {"quarter": 1,
                        "eighth": 2,
                        "triplet": 3,
                        "sixteenth": 4,
                        "16th triplet": 6,
                        "thirty second": 8}
        
            
        if config.beattype == 8:
            measure_length = (rhythm_nums[rhythm])//2 * beats
        else:
            measure_length = rhythm_nums[rhythm] * beats
        
        return measure_length
    
    # Exercise list creation function
    def make_exercise_list():
        
        # Defining variables
        measure_length = calculate_measure_length(config.beats, config.rhythm)
        sample_list = get_sample_list(config.sample_size, config.scale)
        
        # Generating exercise list
        exercise_list = []
        counter = 0
        while True:
            
            # start with a new blank exercise list
            exercise = []
            
            # add notes randomly selected from sample list
            for n in range(measure_length):
                exercise.append(get_random_note(sample_list))
            
            # Discard exercise if duplicate exists already
            if exercise in exercise_list:
                continue
            
            # Add non-discarded exs to exlist
            else:
                exercise_list.append(exercise)
                counter += 1

            # counter == number of exercises breaks loop
            if counter == config.num_of_exs:
                break
            
            else:
                continue
        
        return exercise_list

    # Assigning ex list in config
    config.exercise_list = make_exercise_list()

