__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import zipfile
import os
from os import path
os.path


directory = 'cache'
parent_dir = os.path.dirname(os.path.realpath(__file__))


def clean_cache():
    global target_dir
    target_dir = os.path.join(parent_dir, directory)
    if path.exists(target_dir):
        for file in os.listdir(target_dir):
            file_to_remove = target_dir + '\\' + file
            os.remove(file_to_remove)
    else:
        os.mkdir(target_dir)


def cache_zip(zip_path, cache_dir_path):
    if os.getcwd() != os.path.realpath(__file__):
        os.chdir(os.path.dirname(__file__))
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(cache_dir_path)


def cached_files():
    abs_path_files = []
    for file in os.listdir('cache'):
        abs_path_file = os.path.abspath(directory + '\\' + file)
        abs_path_files = abs_path_files + [abs_path_file]
    return abs_path_files


def find_password(file_paths):
    password_string = ''
    for file in file_paths:
        with open(file) as f:
            if 'password' in f.read():
                password_file = open(file)
                lines = password_file.readlines()
                for line in lines:
                    if 'password' in line:
                        index = line.find(' ')
                        password_string = line[index+1:]
                        return password_string


clean_cache()
print(os.path.realpath(__file__))
print(target_dir)
cache_zip('data.zip', target_dir)

passwordfiles = cached_files()
print(find_password(passwordfiles))
