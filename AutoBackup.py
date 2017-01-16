import os, shutil
from shutil import copytree

while True:
	path = (input("Please input the directory: "))
	print(path) 
	if os.path.exists("/Users/Lex/desktop/flashdrive"):
		#read 
		print("I found the directory.")
		break 
	else:
		print("I could not find the directory.  Please check your spelling.")
		break #should be a continue outside of debugging