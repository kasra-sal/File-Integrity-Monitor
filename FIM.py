#!/usr/bin/python3

import hashlib
import os
import time
from datetime import datetime
import logging




def calculate_hash(path):
    '''
    This function chooses an algorithm, in this case SHA512, and calculates the hash of a file.
    A try except block has been used to prevent any FileNotFoundErrors from breaking the program
    :param path: defined later in the code
    :return: returns the hash digest of the file
    '''
    # Defining hash algorithm : SHA512
    hasher = hashlib.sha512()
    try:
        with open(path, 'rb') as file:
            # Opening the folders/files in the path
            temp = file.read()
            # If the chosen file is a folder, it will keep iterating deeper until it hits a file
            while len(temp) > 0:
                # Updating the new file in hash algorithm to be hashed
                hasher.update(temp)
                temp = file.read()
    except FileNotFoundError:
        pass
    return hasher.hexdigest()

def hash_file_dictionary(path):
    '''
    This will calculate the hash of a file found in path using the calculate_hash function defined above and stores
    them inside "base" dictionary. This allows us to have a base data to work with in which later on we will compare
    the hashes of files with the base dictionary to detect any integrity changes.
    :param path: defined later in the code
    :return: returns the base dictionary for comparison
    '''
    # Defining a base dictionary that will be set up in k:v => file:hash format
    base = {}
    # iterating through files within the path.
    for dir, subdir, files in os.walk(path):
        # for each file in files directory, their path will be defined and a hash will be calculated based on calculate hash function
        for file in files:
            # Grabbing the path of the file
            file_path = os.path.join(dir, file)
            # Storing the file, and it's hash in the following format : {file:hash}
            base[file_path] = calculate_hash(file_path)
    return base

def integrity_monitor(path, hash_list):
    '''
    Main structure of the code, it will continuously monitor the hash of the current file with hash that is present in
    the base dictionary. If they don't match it will log the change inside FIM.log file and produce the respective behaviour
    based on the state.
    The states are as follows:
        - Hash of the new file doesn't match the hash of base dictionary for the same file
            - In the console, it will warn that the file has been changed and logs it into the FIM.log with the following format
                - 'Date' A file has been changed : 'Name_of_File' old hash of 'Old_Hash' with new hash of 'New_hash'
        - File is missing the base dictionary
            - In the console, it will warn that a new file has been found and logs it into the FIM.log with the following format
                - 'Date' New file found : 'Name_of_File' with hash value of 'New_hash'
        - File is present and Hash matches that of the base dictionary
            - Nothing gets logged.

    :param path: defined later in the code
    :param hash_list: the base dictionary grabbed from hash_file_dictionary function
    :return: No returns
    '''
    # Initializing the log file
    logging.basicConfig(filename='FIM.log', level=logging.INFO, filemode='a')

    for dir, subdir, files in os.walk(path):
        for file in files:
            file_path = os.path.join(dir, file)
            file_hash = calculate_hash(file_path)
            # it will check if the file_path is in hash_list
            if file_path in hash_list:
                if file_hash != hash_list[file_path]:
                    print(f"{datetime.now().replace(microsecond=0)} File has been changed: ", file_path)
                    logging.info(f'{datetime.now().replace(microsecond=0)} A file has been changed : {file_path} old hash of {hash_list[file_path]} with new hash of {file_hash}')
            else:
                print(f"{datetime.now().replace(microsecond=0)} New file found: ", file_path)
                logging.info(f'{datetime.now().replace(microsecond=0)} New file found : {file_path} with hash value of {calculate_hash(file_path)}')


                
if __name__ == '__main__':            
    # The path that is being fed into the functions
    monitored_directory = '/home/user/Downloads' # Replace this path with the path you want to monitor

    # Grabbing the base dictionary to feed it into integrity_monitor function as "hash_list"
    base = hash_file_dictionary(monitored_directory)
    while True:
        integrity_monitor(monitored_directory, base)
        # Time.sleep is to tell python how long to wait before rerunning this loop
        # Adjust as needed
        time.sleep(1)
