__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil 
import zipfile
import pathlib



folder = os.getcwd()
folder_cache = folder + "/cache"
zip_file = folder + "/data.zip"

print(folder)
print(folder_cache)
print(zip_file)

#function 1
def clean_cache():
    folder_check = os.listdir(folder)
    if 'cache' in folder_check:
        #delete folder
        shutil.rmtree(folder_cache) 
        #create folder
        os.mkdir(folder_cache) 
    else:
        #create folder
        os.mkdir(folder_cache)
    return

folder_check = os.listdir(folder)
print(folder_check)

#function 2 zip
def cache_zip(zip_file, folder_cache):
    with zipfile.ZipFile(zip_file, 'r',) as zip_ref:
        zip_ref.extractall(folder_cache)
    return 

# read the entries        
def cached_files():
    #folder = os.getcwd()
    #folder_cache = folder + "/cache"
    list_files = []
    with os.scandir(folder_cache) as listOfEntries:
        for entry in listOfEntries:
            if entry.is_file():
                result = os.path.abspath(entry.name)
                #print(result)
                list_files.append(result)
                
    return list_files
                    
#function 4 password

def find_password(cached_files):
    #for x in cached_files:
     #   s = open(x, 'r')
      #  file = s.read()
       # for x in file:
         #   if 'password' in file:
    return 

#print(find_password(list_files_cache))