#! python3
# xmlwriter.py a program to convert the output from noteshuffle.py to musicxml files

import xml.etree.ElementTree as ET
from prettify import prettify
import time, config, notereader, scales, shutil

def SubElementWithText(parent, tag, text): 
    attrib = {}
    element = parent.makeelement(tag, attrib)
    parent.append(element)
    element.text = text
    return element

def xmlwrite():
    scorepartwise = ET.Element("score-partwise", version="3.1")#ROOT

    #IDENTIFICATION BLOCK
    identification = ET.SubElement(scorepartwise, "identification") #not sure how much is necessary here...
    encoding = ET.SubElement(identification, "encoding")
    software = ET.SubElement(encoding, "software ")
    software.text = "MuseScore 3.5.2"
    encodingdate = ET.SubElement(encoding, "encoding-date")
    encodingdate.text = "2021-02-18" #doesn't support importing from config
    supports_accidental = ET.SubElement(encoding, "supports", element="accidental", type="yes")
    supports_beam = ET.SubElement(encoding, "supports", element="beam", type="yes")
    supports_printpage = ET.SubElement(encoding, "supports", element="print", attribute="new-page", type="yes", value="yes")
    supports_printsystem = ET.SubElement(encoding, "supports", element="print", attribute="new-system", type="yes", value="yes")
    supports_stem = ET.SubElement(encoding, "supports", element="stem", type="yes")
    

    #DEFAULTS BLOCK
    defaults = ET.SubElement(scorepartwise, "defaults") #page layout etc...
    scaling = ET.SubElement(defaults, "scaling")#not sure what this should be, but MuseScore needs it to be valid
    millimeters = ET.SubElement(scaling, "millimeters")
    millimeters.text = "8" 
    tenths = ET.SubElement(scaling, "tenths")
    tenths.text = "40"

    pagelayout = ET.SubElement(defaults, "page-layout")
    page_height = ET.SubElement(pagelayout, "page-height")
    page_height.text = "1443.57"
    page_width = ET.SubElement(pagelayout, "page-width")
    page_width.text = "1020.71"
    page_margins_even = ET.SubElement(pagelayout, "page-margins", type="even")
    left_margin = ET.SubElement(page_margins_even, "left-margin")
    left_margin.text = "48.605"
    right_margin = ET.SubElement(page_margins_even, "right-margin")
    right_margin.text = "48.605"
    top_margin = ET.SubElement(page_margins_even, "top-margin")
    top_margin.text = "48.605"
    bottom_margin = ET.SubElement(page_margins_even, "bottom-margin")
    bottom_margin.text = "97.2101"

    page_margins_odd = ET.SubElement(pagelayout, "page-margins", type="odd")
    left_margin = ET.SubElement(page_margins_odd, "left-margin")
    left_margin.text = "48.605"
    right_margin = ET.SubElement(page_margins_odd, "right-margin")
    right_margin.text = "48.605"
    top_margin = ET.SubElement(page_margins_odd, "top-margin")
    top_margin.text = "48.605"
    bottom_margin = ET.SubElement(page_margins_odd, "bottom-margin")
    bottom_margin.text = "97.2101"

    word_font = ET.SubElement(defaults, "word-font")
    word_font.set('font-family','FreeSerif')
    word_font.set('font-size', '10')
    lyrics_font = ET.SubElement(defaults, "lyric-font")
    lyrics_font.set('font-family','FreeSerif')
    lyrics_font.set('font-size','11')

    #TITLE 
    credit = ET.SubElement(scorepartwise, "credit", page="1") #pagenum might need modification in the future
    SubElementWithText(credit, "credit-type", "title")
    credit_words = ET.SubElement(credit, "credit-words", attrib={"default-x": "510","default-y":"1364","justify":"center","valign":"top","font-size":"18"})
    sampl = ""
    config.sample.sort()
    for i in range(len(config.sample)):
        sampl = str(sampl) + ", " + str(config.sample[i])
    credit_words.text = str(config.title) + " " + str(sampl[1:])

    #PARTS LIST BLOCK - TODO CREATE AN INSTRUMENT FUNC
    partlist = ET.SubElement(scorepartwise, "part-list") #instruments...
    scorepart = ET.SubElement(partlist, "score-part", id="P1") #TODO THIS SHOULD CHANGE IF INSTRUMENT CHANGES
    partname = ET.SubElement(scorepart, "part-name")
    partname.text = "Piano"
    partabbreviation = ET.SubElement(scorepart, "part-abbreviation")
    partabbreviation.text = "Pno."
    scoreinstrument = ET.SubElement(scorepart, "score-instrument", id="P1-I1") #I think this will change too
    instrument_name = ET.SubElement(scoreinstrument, "instrument-name")
    instrument_name.text = "Piano"
    midi_device = ET.SubElement(scorepart, "midi-device", id="P1-I1", port="1")#This might change too
    midi_instrument = ET.SubElement(scorepart, "midi-instrument", id="P1-I1") #this too
    midi_channel = ET.SubElement(midi_instrument, "midi-channel")
    midi_channel.text = "1"
    midi_program = ET.SubElement(midi_instrument, "midi-program")
    midi_program.text = "1"
    volume = ET.SubElement(midi_instrument, "volume")
    volume.text = "78"
    pan = ET.SubElement(midi_instrument, "pan")
    pan.text = "0"

    #PARTS BLOCK - WHERE THE NOTES GO
    part = ET.SubElement(scorepartwise, "part", id="P1") #where the notes are written...
    #TODO MAKE A FIST MEASURE FUNC OR LOOP --> FIRST MEASURE HAS KEY SIG/TIME SIG/MEASURE LAYOUT
    exercise_list = config.exercises_withattr_list
    exercise_list_staff2 = config.exercises_withattr_list_staff2
    if config.grid == "yes":
        exercise_list = config.grid_exercise_list
        grid_attributes = config.grid_attributes
    """if config.scalepattern == "yes" and config.grid != "yes":
        exercise_list = config.scale_pattern_exerciselist
        noteattr = config.scale_pattern_attributelist"""
    beats = config.timesig_beats
    beat_type = config.timesig_beattype
    fifths = config.fifths
    clef = config.clef


    #NOTE MAKING FOR SINGLE STAFF/STAFF 1
    for exercise_num in exercise_list: #aka for ex_number in exercise_list.keys() 
        measure = ET.SubElement(part, "measure", number=str(exercise_num), width="555") #this will obviously change from here on out
        
        #SPACER FOR FIRST MEASURE
        if int(exercise_num) == 1:
            first_meas_print = ET.SubElement(measure,"print")
            system_layout = ET.SubElement(first_meas_print, "system-layout")
            system_margins = ET.SubElement(system_layout, "system-margins")
            SubElementWithText(system_margins, "left-margin","0.00")
            SubElementWithText(system_margins, "right-margin","0.00")
            SubElementWithText(system_layout, "top-system-distance", "170.00")

        #LINE BREAKS
        if int(exercise_num) > 1 and int(exercise_num) % 2 != 0:
            print_new_system = ET.SubElement(measure,"print")
            print_new_system.attrib = {"new-system":"yes"}
        
        #SPACER FOR THE REST (EXNUM != 1)
        if int(exercise_num) > 1 and int(exercise_num) % 2 != 0:
            system_layout = ET.SubElement(print_new_system, "system-layout")
            system_margins = ET.SubElement(system_layout, "system-margins")
            SubElementWithText(system_margins, "left-margin","0.00")
            SubElementWithText(system_margins, "right-margin","0.00")
            SubElementWithText(system_layout, "system-distance", "150.00")

        #BARLINE LEFT
        barline = ET.SubElement(measure, "barline", location="left")
        SubElementWithText(barline, "bar-style", "heavy-light")
        repeat = ET.SubElement(barline, "repeat", direction="forward")

        #KEY/CLEF/TIME SIGNATURE #TODO MAKE CLEF VISIBLE OPTIONALLY
        if int(exercise_num) == 1: #CLEF AND TIME SIG FOR FIRST MEASURE    
            attributes = ET.SubElement(measure, "attributes")
            if config.grid != "yes":
                divisions_keys = {"quarter":"1","eighth":"2","16th":"4","32nd":"8","4":"1"}
                divisions = divisions_keys[config.notetype] #TODO, NOTETYPE FOR GRAND STAFF SHOULD BE THE SMALLEST SUBDIV OF THE TWO
            if config.grid == "yes":
                divisions = grid_attributes["divisions"]
            SubElementWithText(attributes, "divisions", divisions)
            key = ET.SubElement(attributes, "key")
            SubElementWithText(key, "fifths", fifths)
            time = ET.SubElement(attributes, "time")
            SubElementWithText(time, "beats", beats)
            SubElementWithText(time, "beat-type", beat_type)
            #clef = ET.SubElement(attributes, "clef")
            #SubElementWithText(clef, "sign", config.clef)
            #SubElementWithText(clef, "line", config.clef_line) #TODO clef if being doubled for some reason...
            if config.clef == "Grand Staff":
                SubElementWithText(attributes, "staves", "2")
                clef1 = ET.SubElement(attributes, "clef", number = "1")
                SubElementWithText(clef1, "sign", "G")
                SubElementWithText(clef1, "line", "2")
                clef2 = ET.SubElement(attributes, "clef", number = "2")
                SubElementWithText(clef2, "sign", "F")
                SubElementWithText(clef2, "line", "4")
            else:
                clef = ET.SubElement(attributes, "clef")
                SubElementWithText(clef, "sign", config.clef)
                SubElementWithText(clef, "line", config.clef_line) #TODO clef if being doubled for some reason..."""
                    
        #REHEARSAL MARK
        direction = ET.SubElement(measure, "direction", placement="above")
        direction_type = ET.SubElement(direction, "direction-type")
        rehearsal = ET.SubElement(direction_type,"rehearsal")
        rehearsal.attrib = {"default-x":"-10.00","relative-y":"30.00","font-weight":"bold","font-size":"14"}
        rehearsal.text = str(exercise_num) + '.'
        direction_type.text = str(exercise_num)
        
        #NOTES FIRST STAFF OR SINGLE STAFF
        if config.grid != "yes" and config.scalepattern != "yes":
            for ex_note in exercise_list[exercise_num].keys(): #
                note = ET.SubElement(measure, "note")
                pitch = ET.SubElement(note, "pitch")
                SubElementWithText(pitch, "step", ex_note[0])
                if 'sharp' in ex_note: #TODO FIFTHS 
                    SubElementWithText(pitch, "alter", "1")
                if 'flat' in ex_note:
                    SubElementWithText(pitch, "alter", "-1")
                noteattr = exercise_list[exercise_num][ex_note]
                SubElementWithText(pitch, "octave", noteattr[0])
                SubElementWithText(note, "duration", noteattr[1])
                SubElementWithText(note, "voice", noteattr[2])
                SubElementWithText(note, "type", noteattr[3])
                if ex_note not in scales.allscales[config.scaletype][config.key_sig]:
                    if 'sharp' in ex_note:
                        SubElementWithText(note, "accidental", "sharp")
                    if 'flat' in ex_note:
                        SubElementWithText(note, "accidental", "flat")
                SubElementWithText(note, "stem", noteattr[4])
                if clef == "Grand Staff": 
                    SubElementWithText(note, "staff", noteattr[5])
            #SECOND STAFF
            if clef == "Grand Staff":
                #BACKUP TAG  
                backup = ET.SubElement(measure, "backup")
                SubElementWithText(backup, "duration", str(int(divisions) * int(config.timesig_beats)))
                #SECOND STAFF NOTES
                for ex_note in exercise_list_staff2[exercise_num].keys():
                    note = ET.SubElement(measure, "note")
                    pitch = ET.SubElement(note, "pitch")
                    SubElementWithText(pitch, "step", ex_note[0])
                    if 'sharp' in ex_note: #TODO FIFTHS 
                        SubElementWithText(pitch, "alter", "1")
                    if 'flat' in ex_note:
                        SubElementWithText(pitch, "alter", "-1")
                    noteattr = exercise_list_staff2[exercise_num][ex_note]
                    SubElementWithText(pitch, "octave", noteattr[0])
                    SubElementWithText(note, "duration", noteattr[1])
                    SubElementWithText(note, "voice", noteattr[2])
                    SubElementWithText(note, "type", noteattr[3])
                    if 'sharp' in ex_note:
                        SubElementWithText(note, "accidental", "sharp")
                    if 'flat' in ex_note:
                        SubElementWithText(note, "accidental", "flat")
                    SubElementWithText(note, "stem", noteattr[4])
                    SubElementWithText(note, "staff", noteattr[5])
                
        #GRID STAFF
        if config.grid == "yes":
            exercise_list = config.grid_exercise_list
            for ex_notes in exercise_list: #numbers in exlist keys
                for ex_note in exercise_list[ex_notes]:
                    print(f"EX LIST: {exercise_list}")
                    print(f"EX NOTES: {ex_notes}")
                    print(f"EX NOTE: {ex_note}")
                    note = ET.SubElement(measure, "note")
                    pitch = ET.SubElement(note, "pitch")
                    SubElementWithText(pitch, "step", "A")
                    SubElementWithText(pitch, "octave", "4")
                    SubElementWithText(note, "duration", grid_attributes[ex_note + "_dur"])
                    SubElementWithText(note, "voice", "1")
                    SubElementWithText(note, "type", ex_note)
                    SubElementWithText(note, "stem", "up")

        #SCALE PATTERN STAFF
        if config.scalepattern == "yes":
            noteattr = config.scale_pattern_attributelist
            for ex in exercise_list:
                for ex_note in exercise_list[ex]:
                    note = ET.SubElement(measure, "note")
                    pitch = ET.SubElement(note, "pitch")
                    SubElementWithText(pitch, "step", ex_note)
                    SubElementWithText(pitch, "octave", noteattr["octave"])
                    SubElementWithText(note, "duration", noteattr["duration"])
                    SubElementWithText(note, "voice", "1")
                    SubElementWithText(note, "type", noteattr["type"])
                    SubElementWithText(note, "stem", "up")


        #BARLINE RIGHT
        barline_right = ET.SubElement(measure,"barline", location="right")
        SubElementWithText(barline_right, "bar-style", "light-heavy")
        repeat_direction = ET.SubElement(barline_right, "repeat", direction="backward") 


    prettify(scorepartwise)#pretty formatting

    tree = ET.ElementTree(scorepartwise) #Making everything above into a tree
    
    #WRITING TO A FILE
    tree.write('./xmlbounces/' + f'{config.filename}.xml', encoding='UTF-8', xml_declaration=True) #write to a file
    
    