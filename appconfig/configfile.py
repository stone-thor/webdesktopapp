#!/usr/bin/env python3

from pathlib import Path
import os, os.path
import json

# this is intentionally dirty, and will be changed later
# when inegration into the operating system is implemented
# for the time being, having a "config" dir inside the application is acceptable

DEFAULT_CONFIG_BASE_PATH = "." 
DEFAULT_CONFIG_DIR_NAME = "config"

# this is also intentionally dirty.
def get_default_config_base_path():
    return os.path.join(DEFAULT_CONFIG_BASE_PATH, DEFAULT_CONFIG_DIR_NAME)


class ConfigFile:
    
    def __init__(self, basepath, filename, extension = "json"):
        file_path = os.path.join(basepath, filename + os.path.extsep + extension)

        if (not os.path.exists(basepath)):
            print( "creating dir: " + basepath )
            mkdir(basepath)
        print( "dir exists: " + basepath )
        
        # if file does not exist
        if (not os.path.exists(file_path)):
            print("creating file: " + file_path) 
            #create empty json file
            Path(file_path).touch()
        print( "file exists: " + os.path.abspath(file_path))

        # assign and open file
        print("opening file" + file_path)
        print("cwd: " + os.getcwd())
        self.file = open(file_path, "r")
        
    # return full config as dict
    def getConfig(self):
        data = json.load(self.file)
        # the user should be able to reread the file at any given point
        # and json.load runs to the end of the file without resetting
        # hence the reset here
        self.file.seek(0)
        return data
        
    def __del__(self):
        self.file.close()