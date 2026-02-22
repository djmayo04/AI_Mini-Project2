import glob

#returns the list of files that match a specified pattern
files = glob.glob('*.txt') 
for files in files:
    print(files)