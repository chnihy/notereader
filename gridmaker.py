#! python3
# grid maker - a program to make musical grid exercises
from copy import copy 
from pprint import pprint
import config, time

def run():
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
    
    #VARIABLE SELECTION
    subdivs = {"4":"quarter", \
            "3":"triplet", \
            "8":"eighth", \
            "12":"16thtriplet",\
            "16":"16th", \
            "24":"32ndtriplet",\
            "32":"32nd"\
            }
    counts = {"quarter":1,\
            "eighth":2,\
            "triplet":3,\
            "16th":4,\
            "16thtriplet":6,\
            "32nd":8,\
            "32ndtriplet":12,\
            }

    #SELECT A
    while True:
        print()
        select_a = input("Enter VARIABLE: "+"\n")
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
        except ValueError:
            print("ERROR enter a valid rhythm")
            continue
    #SELECT B
    while True:
        print()
        select_b = input("Enter BED: "+"\n")
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
        except ValueError:
            print("ERROR enter a valid rhythm")
            continue
    
    #SELECT GRID TYPE
    while True:
        try:
            print()
            select_grid = input("Select Grid Type: " + "\n"\
                                "1. MOVING GRID" + "\n"\
                                "2. STACKING GRID" + "\n"\
                                "3. REVERSING GRID" + "\n")
            print()
            if not select_grid.isalnum():
                raise Exception
            if int(select_grid) < 1 or int(select_grid) > 3:
                raise Exception
            else:
                break
        except Exception:
            print("ERROR, make a valid selection ")
            print()
            continue
    
    #DIVISIONS/DURATIONS    
    divisions_key = {"quarter":"1",\
                "eighth":"2",\
                "16th":"4",\
                "32nd":"8",\
                "4":"1"}
    if int(select_a)>int(select_b):
        bigger_divs = a
        dur_a = "1"
        dur_b = str(int(divisions_key[a])/int(divisions_key[b]))
        dur_b = dur_b[0]
    else:
        bigger_divs = b
        dur_b = "1"
        dur_a = str(int(divisions_key[b])/int(divisions_key[a]))
        dur_a = dur_a[0]
    config.dur_a = dur_a
    config.dur_b = dur_b
    divisions = divisions_key[bigger_divs]

    #MAKING GRIDS
    exercise_list = config.grid_exercise_list
    def MovingGrid(b,a, time):
        biglist = []
        list_a = []
        list_b = []
        for q in range(counts[b]):
            list_b.append(b)
        for p in range(counts[a]):
            list_a.append(a)
        for i in range(time):
            biglist.append(list_b)
        for v in range(len(biglist)):
            biglist2 = copy(biglist)
            biglist2[v]=list_a
            exercise_list[v+1] = biglist2

    def StackingGrid(a, b, subdiv):
        lst = []
        for i in range(subdiv):
            lst.append(a)
        for i in range(len(lst)):
            lst[i] = b
            exercise_list[str(i+1)]=lst
            #print(lst)

    """def ReversingGrid(a, b, subdiv):
        lst = []
        for i in range(int(subdiv/2)):
            lst.append(a)
            lst.append(b)
        exercise_list.append(lst)
        #print(lst)
        exercise_list.append(lst[::-1])
        #print(lst[::-1])"""
    #PRINTING GRIDS
    if select_grid == "1":
        #print("Moving Grid: ")
        MovingGrid(b,a, int(config.timesig_beats))
        #pprint(exercise_list)
        #print()
    if select_grid == "2":
        #print("Stacking Grid: ")
        StackingGrid(b, a, int(config.timesig_beats))
        #pprint(exercise_list)
        #print()
    if select_grid == "3":
        print("Not ready for that yet")
        """print("Reversing Grid: ")
        ReversingGrid(b, a, int(config.timesig_beats))
        pprint(exercise_list)
        print()"""

    #FILENAME
    while True:
        print()
        date = time.strftime("%b" + "_" + "%-d" + "_" + "%y", time.localtime())
        filename = (f'grid_'\
                +f'{timesig_beats}-{timesig_beattype}_'
                +f'{a}_notes_{b}_notes_'\
                +f'{date}')
        filename_selection = input(f"ENTER FILE NAME (C)ustom or (D)efault ('{filename}')?: " + "\n")
        if filename_selection.lower() == "c":
                print()
                filename = input("Enter File Name: " + "\n")
                break
        if filename_selection.lower() == "d":
                break
                #else: #TODO CREATE FILENAME ENTRY BLACKLIST
    
    #ATTRIBUTES
    config.clef = "G"
    config.grid = "yes"
    config.clef_line = "2"
    grid_attributes = config.grid_attributes
    grid_attributes["a"] = a
    grid_attributes["b"] = b
    grid_attributes[a + "_dur"] = dur_a
    grid_attributes[b + "_dur"] = dur_b
    grid_attributes["divisions"] = divisions
    config.filename = filename
    config.fifths = "0"
    
    #PRINTOUT
    """print()
    pprint(exercise_list)
    print()
    print("Grid Attributes")
    print(grid_attributes)
    print()
    print(filename)"""