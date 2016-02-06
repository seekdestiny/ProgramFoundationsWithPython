import os

def rename_files():
    mypath = "/home/jifeiqian/android-work/ProgramFoundationWithPython/data/prank/"
    file_list = os.listdir(mypath)
    #print(file_list)

    saved_path = os.getcwd()
    os.chdir(mypath)
    for filename in file_list:
        os.rename(filename, filename.translate(None, "0123456789"))

    os.chdir(saved_path)
rename_files()
