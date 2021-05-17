__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil 
import zipfile
import pathlib

folder = os.getcwd()
folder_cache = folder + "/cache"
zip_file = folder + "/data.zip"


#function 1
def clean_cache():
    folder_check = os.listdir(folder)
    if 'cache' in folder_check:
        #delete folder
        shutil.rmtree(folder_cache) 
    #create folder
    os.mkdir(folder_cache)
    return


#function 2 zip
def cache_zip(zip_file, folder_cache):
    with zipfile.ZipFile(zip_file, 'r',) as zip_ref:
        zip_ref.extractall(folder_cache)
    return 


#function 3 files
def cached_files():
    list_files = []
    with os.scandir(folder_cache) as list_of_entries:
        for entry in list_of_entries:
            if entry.is_file():
                result = os.path.abspath(entry)
                list_files.append(result)
                
    return list_files


#function 4 password
def find_password(list_files):
    for file_name in list_files:
        file = open(file_name, 'r')
        for line in file:
            #print("Line:\n" + line)
            if 'password' in line:
                print(line[line.find(' ')+1:])
                return line
