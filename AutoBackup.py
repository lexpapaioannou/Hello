import os, shutil, getpass, time, datetime
from datetime import datetime
from shutil import copytree

user = getpass.getuser()
a = 0
rows = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
savePath = "/Applications/autoBackup/"
path_to_watch = '/Volumes/'
before = dict ([(f, None) for f in os.listdir (path_to_watch)])

while True:
    if os.path.exists("/applications/autoBackup/") == False:
        os.makedirs(savePath)
        print("I created a new folder at \"/Applications/autoBackup/\"")
        break
    else:
        print("autoBackup is already installed")
        break

os.chdir("/Applications/autoBackup")

while 1:
    time.sleep (1)
    after = dict ([(f, None) for f in os.listdir (path_to_watch)])
    added = [f for f in after if not f in before]
    removed = [f for f in before if not f in after]
    if added:
        print("Flashdrive detected")
        dest = "/Applications/autoBackup/{}{}".format(added[0], datetime.now())
        path = "/Volumes/" + added[0]
        print("Loading...")
        shutil.copytree(path,dest)
        print("I created a backup at "+dest)
    if removed:
        print("Flashdrive removed")
    before = after
