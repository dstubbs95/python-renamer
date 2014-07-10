#This python script will add a number at the begining of the file
#name. It will allow you to choose the number to start with and
#counts up on its own from there. It numbers the files in order
#based on the date which they were last modified. It should also not 
#mess with files which already have a number at the beginning.
#This should make it possible to run this over and over again
#in the same directory to add numbers to files as needed


#Created by: Daniel Stubbs

import os, sys

#Tell the user what the current directory is
print("This script should be run from within the directory of the files which you want to rename reside. Make sure that the only files in the directory are the ones which you want to rename, it will rename all of them.")
print("The current directory is: " + os.getcwd())


#Determine if the current directory is the correct one
go = 0
while go == 0:
	go = str(input("Is this the right directory? (yes/no): "))
#If it is the right one then rename the files with numbers
if go == "yes":
	files_raw = os.listdir(os.getcwd())
	#Rebuild files array without files that already have numbers
	files =[]
	for item in files_raw:
		if not item[0].isdigit():
			files.append(item)
	#Get the number to start with
	inc = int(input("Which number would you like to start with?: "))
	#initialize array to combine time with name
	array = []
	for item in files:
		#get the modified times and combine them with the name and save them as array 
		array.append(str(os.stat(item).st_mtime) + "_+" + item)	
	#sort the array by file creation date
	array.sort()
	#remove the date from the array now that its sorted
	final_array = []
	for item in array:
		final_array.append(item.partition("_+")[2])
	#rename the files using the incriments given above
	i = 0
	for item in files:
		os.rename(item, str(inc) + final_array[i])
		i += 1 
		inc += 1
	#report that everything went well
	print("Yay! Your files have been numbered.")
	
#If it isn't the right directory then quit
elif go == "no":
	print("Ok, then get to the right directory")
#If for some reason we don't know what the hell is going on then quit before files get broken
else: 
	print("I could not determine what you wanted me to do")

