'''
Run this from the folder with all the pictures and videos to sort.
Select the drive where you want the pictures to end up
Relax
'''

import shutil
import pathlib
import os

directory = os.getcwd()

photos = []

videos = []

drive = str.capitalize(input("Which letter drive do you want to use? "))

for filename in os.listdir(directory):
    # exclude directories ("If filename is a file")
    if os.path.isfile(filename):
        full_path = os.path.join(directory, filename)
        month = filename[:6]
        month_folder = month[:4] + '-' + month[4:6]
        extension = full_path[-3:]
        if extension == 'jpg':
            file_type = "Pictures"
        elif extension == 'mp4':
            file_type = "Videos"
        
        destination = f"{drive}:/{file_type}/{month_folder}/"

        if extension == 'jpg' or extension == 'mp4':
            # print('filename is:', filename)
            print('full path is:', full_path)
            # print('month is:', month)
            # print('month_folder is',month_folder)
            # print('extension is:', extension)
            print('has been moved to:')
            print('destination is:', destination)
            print('\n')

            os.makedirs(destination, exist_ok=True)
            shutil.copy(full_path, (destination+filename))
            os.remove(full_path)