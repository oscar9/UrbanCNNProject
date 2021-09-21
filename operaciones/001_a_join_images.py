import os
import sys
import glob

###
### INIT VARIABLES
###

# Base folder
DATA_FOLDER = 'E:\\TFM_MUESTRAS\\' 

# Name of the test folder
TEST_FOLDER = "Test_005\\"

# Folder with city folders images
TRAINING_DIR = DATA_FOLDER + TEST_FOLDER + "images\\" 

# New folder to be created with joined images
PROCESS_NAME = 'process_101_valenciaall' 


###
### PROCESS
###
TRAINING_FOLDER = 'training_' + PROCESS_NAME
VALIDATION_FOLDER = 'validation_' + PROCESS_NAME
NEW_TRAINING_FOLDER = DATA_FOLDER + TEST_FOLDER + TRAINING_FOLDER
NEW_VALIDATION_FOLDER = DATA_FOLDER + TEST_FOLDER + VALIDATION_FOLDER

builtup_dir = os.path.join(TRAINING_DIR)
print (builtup_dir)
print('total builtup images:', len(os.listdir(builtup_dir)))

import random

# All files ending with .txt
tif_files = glob.glob(TRAINING_DIR+"*\\*.tif")
print (tif_files[:10])

random.shuffle(tif_files)

"""
builtup_files = os.listdir(builtup_dir)
print(builtup_files[:10])
tif_files = []
for bfile in builtup_files:
    if bfile.endswith(".tif"):
        tif_files.append(os.path.join(NEW_TRAINING_FOLDER + bfile))
print (tif_files[:10])
"""

import shutil, os

# Initialize new test folder
testFolder = NEW_TRAINING_FOLDER
if not os.path.exists(testFolder):
  os.makedirs(testFolder)

# Divide  by 4 types
print ("Divide by 4 types")
builtup_names = [
    "0_espacioabierto", 
    "1_industrial", 
    "2_atomistic",
    "4_formal"
    ]

dic_all_files_types = {
    builtup_names[0]:[],
    builtup_names[1]:[],
    builtup_names[2]:[],
    builtup_names[3]:[]
    }

for f in tif_files:
    if f.endswith("0.tif"):
        dic_all_files_types["0_espacioabierto"].append(f)
    if f.endswith("1.tif"):
        dic_all_files_types["1_industrial"].append(f)
    if f.endswith("2.tif"):
        dic_all_files_types["2_atomistic"].append(f)
    if f.endswith("4.tif"):
        dic_all_files_types["4_formal"].append(f)

# Split for training
# Reserve 10,000 samples for validation
#x_val = x_train[-10000:]
#y_val = y_train[-10000:]
#x_train = x_train[:-10000]
#y_train = y_train[:-10000]

dic_validation_files = {}
dic_training_files = {}
for key in dic_all_files_types.keys():
    percentaje = int(len(dic_all_files_types[key])*0.20)
    dic_training_files[key] =  dic_all_files_types[key][:-percentaje]
    dic_validation_files[key] =  dic_all_files_types[key][-percentaje:]

#print (dic_training_files)
#print (dic_validation_files)


# Initialize folders in test and copy values
print ("Start copy process")
for key in dic_training_files.keys():
   
    # Training
    training_type_folder =  os.path.join(NEW_TRAINING_FOLDER,key)
    print ("tr", training_type_folder)
    if not os.path.exists(training_type_folder):
        os.makedirs(training_type_folder)
    training_files = dic_training_files[key]
    for f in training_files:
            shutil.copy(f, training_type_folder)

    # Validation
    validation_type_folder =  os.path.join(NEW_VALIDATION_FOLDER,key)
    if not os.path.exists(validation_type_folder):
        os.makedirs(validation_type_folder)
    validation_files = dic_validation_files[key]
    for f in validation_files:
            shutil.copy(f, validation_type_folder)

