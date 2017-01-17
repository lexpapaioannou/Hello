import os, shutil, getpass, csv, time
from shutil import copytree

user = getpass.getuser()
a = 0
rows = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
savePath = "/applications/autoBackup/"

while True:
    if os.path.exists("/applications/autoBackup/") == False:
        os.makedirs(savePath)
        print("I created a new path at \"/Applications/autoBackup/\"")
        break
    else:
        print("autoBackup is already installed")
        break

os.chdir("/applications/autoBackup")

while True:
    checkSave = os.path.exists("/Applications/autoBackup/savedFlashdrives.csv")
    if checkSave == False:
        print("I could not find a list of flashdrives you have backed up in the past.")
        print("\nPlease input the name of your flashdrive:\n") #This may not be necessary in the future...
        flashdrive = input() #See note above 
        while True:
            if rows[a] != '':
                a += 1
                continue
            else:
                rows[a] = flashdrive
                break
            break
        with open('savedFlashdrives', 'w') as csvfile:
            savedFlashdrives = csv.writer(csvfile, delimiter = ',')
            savedFlashdrives.writerow(rows[0])
            savedFlashdrives.writerow(rows[1])
            savedFlashdrives.writerow(rows[2])
            savedFlashdrives.writerow(rows[3])
            savedFlashdrives.writerow(rows[4])
            savedFlashdrives.writerow(rows[5])
            savedFlashdrives.writerow(rows[6])
            savedFlashdrives.writerow(rows[7])
            savedFlashdrives.writerow(rows[8])
            savedFlashdrives.writerow(rows[9])
            savedFlashdrives.writerow(rows[10])
            savedFlashdrives.writerow(rows[11])
            savedFlashdrives.writerow(rows[12])
            savedFlashdrives.writerow(rows[13])
            savedFlashdrives.writerow(rows[14])
            savedFlashdrives.writerow(rows[15])
            savedFlashdrives.writerow(rows[16])
            savedFlashdrives.writerow(rows[17])
            savedFlashdrives.writerow(rows[18])
            savedFlashdrives.writerow(rows[19])
        
    while True:
            #The noted out code represents a backup in case I can't figure out how to check when a USB comes in
            #Although not preferable, I can possibly write the code so that the user can do it manually
            #I would do this by simply creating a new method and, at the end of the program cycle, either prompt the user (via 'y' or 'n')
            #Or by calling that method.
            #if defaultPathVali == False:
            #    print("I could not find a default path.  Please input a new default path.")    
            #path = input("\nPlease input the directory:\n")
            #pathVali = os.path.exists(path)
            #defaultPathVali = os.path.exists(path+"defaultPath.txt")
            #print(defaultPathVali)
            if pathVali == False:
                print("I could not find that directory.  Please check your spelling and try again.")
                continue
            else:
                print("I found that directory.")

                defPathName = os.path.join(savePath, "defaultPath.txt")
                defaultPath = open(defPathName, 'w')
                defaultPath.write(path)
                defaultPath.close()
            
            break

    while True:
            dest = input("\nPlease input the directory to save your backup:\n")
            destVali = os.path.exists(dest)
            if destVali == False:
                print("I could not find that directory.  Please check your spelling and try again.")
                continue
            else:
                print("I found that directory.")
            
            break
    tmp = "/Applications/autoBackup/"+rows[a]
    shutil.copy(path,flashdrive)
    shutil.move(flashdrive, dest)
    
    print("Your flashdrive has been saved to \"/Applications/autoBackup/"+flashdrive+"\"") 
    
    break
