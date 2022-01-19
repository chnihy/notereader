# Notereader
Notereader is a tool in development for music students and teachers.  It generates random sight reading exercises and has lots of customization:
  - Scale
  - Rhythm
  - Time Signature
  - Key

More features will be coming in the future, some planned updates:
  - Packaging for OS/iOS
  - Complexity settings
  - Mixed rhythms
  - Rests
  - Expanded scales (Modes, altered, diminished etc...)
  - Prettier user interface
  - Playback support/Integrated note display
  - Export to MIDI/mp3

# Installation/Running
1. Install Dependecies (you can skip this step if you use the included virtual environment)
2. Download zip
3. cd to notereader directory (activate virtual environment)
4. python3 main.py

# Requirements
Requires installation of Scamp and Kivy packages
  - You can use the included venv which has all dependencies already installed:
    - $ source ./notereader_venv/bin/activate
    - $ python3 main.py

  - Or you can manually install the required packages:
    - pip3 install --user scamp
    - Note: You will also need to install abjad and lilypond as part of SCAMP's xml engraving dependencies 
    - brew install lilypond
    - pip3 install abjad
    - pip3 install kivy
