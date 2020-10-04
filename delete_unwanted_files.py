import os
import glob

PATH = 'G:\courses\[FreeCourseSite.com] Udemy - Python for Data Science and Machine Learning Bootcamp'
FILE_TYPE = 'VTT'
def remove(path, typ):

    os.chdir(path)
    folders = os.listdir()
    for x in range(len(folders)):
        os.chdir(folders[x])

        for file in glob.glob(f'*.{typ}'):
            os.remove(file)
        os.chdir(path)


remove(
    PATH, FILE_TYPE)
