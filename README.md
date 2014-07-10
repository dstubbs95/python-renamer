python-renamer
==============

Python script to rename files in current directory by adding numbers to the beginning of a file in the order of modification date.

** REQUIRES PYTHON 3 

** Use at your own risk. I have no bad intent, but this is a script that I wrote for a specific use case. It never did anything crazy for me, but I did not test it any crazy amount. 

================
This is just a short script that I wrote to solve a pretty specific problem that I had. Lets say that you have downloaded a bunch of files into a folder but for some reason an application you are viewing them with doesn't sort by date, but only by name. This python script should alleviate that because it will add numbers to the beginning of the files. The number that it starts with is up to you and it should not mess with files that already start with numbers. In theory, this means that it should be able to be run in the same directory over and over again to keep adding numbers to new downloaded files. All you have to do is tell it which number you would like it to start with based off the most recent number already included.

To install this script I would recoment putting it somewhere in your home directory. From there you can run it by referencing it with the python3 command. For added convinience you could also add a bash script to /usr/local/bin which would simply contain a line like 
"exec python3 /home/user/rename.py". If you're not sure how to do that, then I would recoment just running it using python3.


