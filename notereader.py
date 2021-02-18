#! python3
# Notereader app - main program.  Where the user types stuff in 

from noteshuffle import noteshuffle
from pprint import pprint
import exceptions as e
import scales, config, attributes, math, os, sys, time

br = "\n"

def run(selection):
       print("\n" + "---------- NOTE READER ----------" + "\n")
       
       """selection = input("Select type of exercise: \n  \
       1. Shuffle  \
       2. Moving Grid \
       3. Stacking Grid \
       4. Reversing Grid \n"
       )      """
       if selection == "1":
              #CLEF
              while True:
                     try:
                            clef = input("ENTER CLEF (t)reble or (b)ass: "+"\n")
                            whitelist_t = ["t","tr","tre","treb","treble","g"]
                            whitelist_b = ["b","ba","bas","bass","f"]
                            if clef.lower() in whitelist_t:
                                   clef = "G"
                                   clef_line = "2"
                                   break
                            if clef.lower() in whitelist_b:
                                   clef = "F"
                                   clef_line = "4"
                                   break
                            if clef not in (whitelist_b + whitelist_t):
                                   raise Exception  
                     except Exception:
                            print("\n" + "ERROR: Enter a valid clef!" + "\n")
                            continue
              config.clef = clef
              config.clef_line = clef_line
              
              #KEY SIGNATURE
              while True:
                     try:
                            key_sig = input("\n" + "ENTER KEY: "+"\n")
                            if not key_sig[0].isalpha():
                                   raise ValueError
                            key_sig = key_sig.capitalize()
                            if "#" in key_sig[1:]:
                                   key_sig = key_sig[0] + "sharp"
                            if "b" in key_sig[1:]:
                                   key_sig = key_sig[0] + "flat"
                            if key_sig not in scales.allnotes_master:
                                   raise ValueError
                            break
                     except ValueError:
                            print("\n" + "ERROR: Enter a valid key: " +"\n")
                            continue
              config.fifths = scales.Key(key_sig).fifths[key_sig]

              #SCALE ROOT
              while True:
                     try:   
                            root = input("\n" + "ENTER SCALE ROOT: "+"\n") #Change to scale root or scale key
                            if not root[0].isalpha():
                                   raise ValueError
                            root = root.capitalize()
                            if "#" in root[1:]:
                                   root = root[0] + "sharp"
                            if "b" in root[1:]:
                                   root = root[0] + "flat"
                            if root not in scales.allnotes_master:
                                   raise ValueError
                            break
                     except ValueError:
                            print("\n" + "ERROR: Enter a valid key: " +"\n")
                            continue

              #SCALE
              while True:
                     try:
                            scaletype = input("\n" + f"ENTER SCALE TYPE OR 'list' FOR LIST OF SCALES: " + "\n") #TODO DATA VALIDATION, SHARPS AND FLATS AND ERRORS
                            s = scaletype.lower()
                            whitelist_scales = ["chromatic", "major","minor","melodic minor","major pentatonic","pentatonic"]
                            if s == 'list':
                                   print("------------")
                                   print("\n" + "SCALES" + "\n")
                                   pprint(whitelist_scales)
                                   continue
                            if s not in whitelist_scales:
                                   raise Exception
                            if s == "chromatic":
                                   scale = scales.Chromatic(root).scale
                                   break
                            if s == "major" :
                                   scale = scales.Major(root).scale
                                   break
                            if s == "minor":
                                   scale = scales.Minor(root).scale
                                   break
                            if s == "melodic minor":
                                   scale = scales.MelodicMinor(root).scale
                                   break
                            if s == "major pentatonic":
                                   scale = scales.MajorPentatonic(root).scale
                                   break
                            if s == "pentatonic":
                                   scale = scales.MinorPentatonic(root).scale
                                   break
                            if s == "minor pentatonic":
                                   scale = scales.MinorPentatonic(root).scale
                                   break
                     except Exception:
                            print("\n" + f"ERROR: {scaletype} is not a valid scale" + "\n")
                            continue
              config.scaletype = scaletype
              
              #TIME SIGNATURE
              while True:
                     try: #BETTER DATA VALIDATION, REGEX OR PYDANT
                            timesig_beats = input("\n" + "ENTER BEATS PER MEASURE (ex 4): "+"\n")
                            if timesig_beats.isnumeric() == False:
                                   raise ValueError
                            if len(timesig_beats)>2:
                                   raise ValueError 
                            break
                     except ValueError:
                            print("\n" + "ERROR! Enter a valid number " + "\n")
                            continue
              while True:
                     try:
                            timesig_beattype = input("\n" + "ENTER BEAT TYPE (4 or 8): " + "\n" + f"{timesig_beats}/")
                            if timesig_beattype.isnumeric() == False:
                                   raise ValueError
                            if int(timesig_beattype) % 2 != 0:
                                   raise ValueError 
                            break
                     except ValueError:
                            print("\n" + "ERROR! Enter a valid number " + "\n")
                            continue
              config.timesig_beats = timesig_beats
              config.timesig_beattype = timesig_beattype
              
              #RHYTHM TYPE AKA NOTETYPE
              while True:
                     try:
                            notetype = input("\n" + "ENTER RHYTHM OR 'list': "+"\n") 
                            shortcuts = {#"1":"whole",\
                                          #"2":"half",\
                                          "4":"quarter",\
                                          #"6" TODO TRIPLETS ARE HARD BRUH...
                                          "8":"eighth", #TODO BEAM ACTION \
                                          "16":"16th", \
                                          "sixteenth":"16th", # TODO BEAM ACTION \ 
                                          "32":"32nd", \
                                          "thirty second": "32nd"}
                            if not notetype.isalnum:
                                   raise ValueError
                            if notetype.lower() == 'list':
                                   print("\n" #+ "-- whole or 1" + "\n" \
                                          #+ "-- half or 2" + "\n"\
                                          + "-- quarter or 4" + "\n"\
                                          #+ "-- quarter triplets or 6" + "\n"\
                                          + "-- eighth or 8" + "\n"\
                                          #+ "-- eighth triplets or 12" + "\n"\
                                          + "-- sixteenth or 16" + "\n" )
                                          #+ #"-- sixteenth triplets or 24")
                                   #print('\n')
                                   continue
                            if notetype in shortcuts.keys():
                                   notetype = shortcuts[notetype]
                                   break
                            if notetype not in shortcuts and notetype != 'list' :
                                   raise Exception
                            else:
                                   break
                     except ValueError:
                            print("\n" + "ERROR: Enter a valid rhythm, or LIST" + "\n")
                            continue
                     except Exception:  
                            print("\n" + "ERROR: Enter a valid rhythm, or LIST" + "\n")
                            continue
              config.notetype = notetype

              # MEASURE LENGTH - MAKING SURE IT MATCHES SUBDIVS
              measure_length = config.measure_length
              t = int(config.timesig_beats)
              if timesig_beattype == "4":
                     if notetype == "quarter":
                            measure_length = t 
                     if notetype == "eighth":
                            measure_length = t * 2
                     if notetype == "16th":
                            measure_length = t * 4
                     if notetype == "32nd":
                            measure_length = t * 8
              if timesig_beattype == "8": #TODO DATA VALIDATION FOR ODD TIMES, 7 etc. - either need auto-8ths, rests or some kind of message
                     if notetype == "quarter":
                            measure_length = t//2 
                     if notetype == "eighth":
                            measure_length = t
                     if notetype == "16th":
                            measure_length = t * 2
                     if notetype == "32nd":
                            measure_length = t * 4

              #TODO NOTESELECTION
              #SAMPLE SIZE ENTRY
              while True:
                     try:
                            print()
                            sample_size = int(input("ENTER SAMPLE SIZE: " + "\n"))
                            if sample_size > len(scale):
                                   raise Exception
                            if sample_size > measure_length:
                                   raise e.SampleBiggerThanMeasure      
                            break
                     except ValueError:
                            print("Enter a valid number: ")
                            continue
                     except e.SampleBiggerThanMeasure:
                            print(f"ERROR: Sample is bigger than measure length ({measure_length})!")
                            continue
                     except Exception:
                            print(f"ERROR: Sample size too big, max size is {str(len(scale))}")
                            continue
              config.sample_size = sample_size
       
              # NUMBER OF EXERCISES
              while True:
                     try:
                            exercises = input("\n" + "ENTER NUMBER OF EXERCISES: " + "\n")
                            if exercises.lower() == 'max':
                                   if math.factorial(measure_length) > 100:
                                          exercises = 100
                                   else:
                                          exercises = math.factorial(measure_length)
                                   break
                            if int(exercises) > math.factorial(measure_length) and math.factorial(measure_length) <= 100:
                                   print("\n" + f"ERROR: Too many exercises! Max possible exercises is {math.factorial(measure_length)}" + "\n")
                                   continue
                            if int(exercises) > 100:
                                   print("\n" + "ERROR: Too many exercises! Max possible exercises is 100" + "\n")
                                   continue
                            exercises = int(exercises)
                            break
                     except ValueError:
                            print("\n" + "ERROR! Enter a valid number: " + "\n")
                            continue
                     print(f"Num of exercises: {exercises}")
       
       #TITLE CUSTOMIZATION
       while True:
              print()
              title = (f"{root} {scaletype}: ")
              custom_title = input(f"ENTER TITLE: (C)ustom or (D)efault ('{title}...')?: " + "\n")
              if custom_title.lower() == "c":
                     title = input("ENTER CUSTOM TITLE: " + "\n")
                     break
              if custom_title.lower() == "d":
                     break
              else:
                     continue
       config.title = title

#FILENAME CUMSTOMIZATION
       while True:
              print()
              date = time.strftime("%D",time.localtime())
              filename = (f'{root.lower()}{scaletype}_'\
                     +f'{timesig_beats}-{timesig_beattype}_'\
                     +f'{notetype}_notes_'\
                     +f'{date}')
              try:
                     filename_selection = input(f"ENTER FILE NAME (C)ustom or (D)efault ('{filename}')?: " + "\n")
                     path = '/xmlbounces/'
                     if filename_selection.lower() == "c":
                            filename = input("Enter File Name: " + "\n")
                            break
                     if filename_selection.lower() == "d":
                            if filename + '.xml' in os.listdir(path):
                                   raise Exception
                            else:
                                   break
              except Exception:
                     filename_selection = input(f"WARNING: {filename} already exists! Overwrite? (Y or N): ")
                     if filename_selection.lower() == 'y':
                            break
                     if filename_selection.lower()== 'n':
                            continue
                     #else: #TODO CREATE FILENAME ENTRY BLACKLIST
       config.filename = filename

       #SENDING TO THE SHUFFLER AND PRINTING INOF
       noteshuffle(scale, sample_size, measure_length, exercises)

       #SUMMARY PRINT OUT
       print("\n"+"------------- COMPLETE --------------"+"\n")
       print(f"File name: \"/{config.filename}.xml\"")
       print(f"Title: \"{title}\"")
       print(f"Clef: {clef}")
       print(f"Time Signature: {config.timesig_beats}/{config.timesig_beattype}")
       print(f"Key Signature: {key_sig}", end="\n")
       print(f"Scale: {root} {scaletype}", end="\n")
       print(f"Sample Size: {sample_size}", end="\n")
       print(f"Sample Set: {config.sample}",end="\n")
       if measure_length > sample_size:
              print(f"Duplicates Allowed: {int(config.duplicates)}",end="\n")
       print(f"Rhythm: {notetype}",end="\n")
       print(f"Measure Length: {measure_length} Notes Per Measure", end="\n")
       print(f"Number of Exercises: {exercises}", end="\n")       
#print(config.exercise_list)
