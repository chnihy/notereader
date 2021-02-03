#! python3
# Notereader app - main program.  Where the user types stuff in 

from noteshuffle import noteshuffle
from pprint import pprint
import scales, config, attributes, math, os

br = "\n"

def run(selection):
       while True:
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
                                   key = input("\n" + "ENTER SCALE ROOT: "+"\n") #Change to scale root or scale key
                                   if not key[0].isalpha():
                                          raise ValueError
                                   key = key.capitalize()
                                   if "#" in key[1:]:
                                          key = key[0] + "sharp"
                                   if "b" in key[1:]:
                                          key = key[0] + "flat"
                                   if key not in scales.allnotes_master:
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
                                   if scaletype == 'list':
                                          print("------------")
                                          print("\n" + "SCALES" + "\n")
                                          pprint(whitelist_scales)
                                          continue
                                   if scaletype not in whitelist_scales:
                                          raise Exception
                                   if s == "chromatic":
                                          scale = scales.Chromatic(key).scale
                                          break
                                   if s == "major" :
                                          scale = scales.Major(key).scale
                                          break
                                   if s == "minor":
                                          scale = scales.Minor(key).scale
                                          break
                                   if s == "melodic minor":
                                          scale = scales.MelodicMinor(key).scale
                                          break
                                   if s == "major pentatonic":
                                          scale = scales.MajorPentatonic(key).scale
                                          break
                                   if s == "pentatonic":
                                          scale = scales.MinorPentatonic(key).scale
                                   if s == "minor pentatonic":
                                          scale = scales.MinorPentatonic(key).scale
                                          break
                            except Exception:
                                   print("\n" + f"ERROR: {scaletype} is not a valid scale" + "\n")
                                   continue

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
                                   if len(timesig_beattype)>1:
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

                     #TODO SAMPLESIZE/NOTESELECTION
                     """while True:
                            try:
                                   samplesize = int(input("Enter sample size: "))
                                   break
                            except TypeError:
                                   print("Enter a valid number: ")
                                   continue"""
                     
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
              
              #SENDING TO THE SHUFFLER AND PRINTING INFO
              noteshuffle(scale, measure_length, exercises)
              print("\n"+"------------- COMPLETE --------------"+"\n")
              print(f"Clef: {clef}")
              print(f"Time Signature: {config.timesig_beats}/{config.timesig_beattype}")
              print(f"Key Signature: {key_sig}", end="\n")
              print(f"Root: {key}", end="\n")
              print(f"Scale: {key} {scaletype}", end="\n")
              print(f"Sample Set: {set(config.master)}")
              print(f"Rhythm: {notetype}")
              print(f"Measure Length: {measure_length} Notes Per Measure", end="\n")
              print(f"Number of Exercises: {exercises}", end="\n")

              #PROGRAM LOOP/PRINTING
              while True:
                     run = input("\n" + "(R)un again? Or (P)rint?: ")
                     whitelist_run = ["r","ru","run","rn"]
                     whitelist_print = ["p","pr","pri","prin","print","prnt"]
                     if run.lower() in whitelist_run:
                            break 
                     if run.lower() in whitelist_print:
                            os.system('open "xmlwriter_test.xml"')
                            break
                     else:
                            continue
              if run.lower() in whitelist_run:
                     continue
              else:
                     print("\n" + "---------- END ----------" + "\n")
                     break
                     
       #print(config.exercise_list)
