#!usr/bin/python27

# Nintendont Game Installer
# Version 1.0.
#
# This script is used to install GameCube ISO's for use with Nintendont after direct disc dump with CleanRip
#
# Script written by bennyman123abc

# IMPORT
import os
import time
from shutil import copyfile

# INIT
operatingSystem = os.name
print os.name
if operatingSystem == "nt":
    clr = "cls"
else:
    clr = "clear"
os.system(clr)

# OPTIONS

print("Type the directory that the ISO files are in here. Ex. 'C:/Users/Windows/Documents/GameCube ISOs' or '/home/ubuntu/GameCube ISOs'")
print("")
inputDir = raw_input("Game Input Directory: ")
os.system(clr)

print("Type the drive or SD card you want to install these games to here. Ex. 'E:/' or '/media/ubuntu/sdcard/'")
print("")
outputDrive = raw_input("Game Installation Drive: ")
os.system(clr)

# CODE

outputExists = os.path.isdir(outputDrive + "games")
if outputExists == False:
    print(outputDrive + "games/ is not a directory. Creating it now!")
    os.makedirs(outputDrive + "games")
elif outputExists == True:
    print(outputDrive + "games/ already exists. Continuing!")
    
for file in os.listdir(inputDir):
    if file.endswith(".iso"):
        posInstalled = False
        base = os.path.basename(file)
        game = os.path.splitext(base)[0]
        installDir = outputDrive + "games/" + game
        if os.path.isdir(installDir) == False:
            print(installDir + "/ does not exist. Creating it now!")
            os.makedirs(installDir)
        elif os.path.isdir(installDir) == True:
            print(installDir + "/ already exists. Continuing!")
            posInstalled = True
        if os.path.exists(installDir + "/" + "game.iso") == True:
            print(game + " is already installed. Continuing!")
            os.remove(inputDir + file)
        elif os.path.exists(installDir + "/" + "game.iso") == False:
            print("Installing " + game + ". This may take a few minutes!")
            copyfile(inputDir + file, installDir + "/" + file)
            os.rename(installDir + "/" + file, installDir + "/" + "game.iso")
            os.remove(inputDir + file)
    elif file.endswith(".bca"):
        os.remove(inputDir + file)
print("Games have finished installing. Quitting in 5 seconds")
time.sleep(5)