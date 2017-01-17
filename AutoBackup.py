import os, shutil
from shutil import copytree
#I am not currently using shutil or copytree, but I intend to use it for copying folders in the future

while True:
        pathVali = os.path.exists(input("\nPlease input the directory: \n"))
        if pathVali == False:
            print("I could not find that directory.  Please check your spelling and try again.")
            continue
        else:
            print("I found that directory.")
        print("This line works")
        break
    
