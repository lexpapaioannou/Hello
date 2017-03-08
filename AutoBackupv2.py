import os, shutil, time, datetime, threading
from datetime import datetime
from shutil import copytree

savePath = "/Applications/autoBackup/"
path_to_watch = '/Volumes/'
before = dict ([(f, None) for f in os.listdir (path_to_watch)])

def Load():
    set = ['/', '-', '\\', '|']
    for x in range(4):
        b = "Loading... " + set[x]
        print(b, end = "\r")
        time.sleep(.5)

def copytree(src, dest):
    shutil.copytree(src, dest)

def downloader(src, dest):
    dl = threading.Thread(target = copytree, args = (src, dest))
    dl.start()
    while (dl.isAlive()):
            Load()

while True:
    if os.path.exists("/Applications/autoBackup/") == False:
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
    if added and added[0] != '.DS_Store':
        print("Flashdrive detected")
        dest = "/Applications/autoBackup/{}{}".format(added[0], datetime.now())
        path = "/Volumes/" + added[0]
        org = os.stat(path)
        downloader(path, dest)
        print("I created a backup at "+dest)
    if removed:
        print("Flashdrive removed")
    before = after
