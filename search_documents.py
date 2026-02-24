#import glob

#returns the list of files that match a specified pattern
#files = glob.glob('*.txt') 
#for files in files:
    #print(files)
import glob
import pathlib
import os

doc = input("Enter a document: ")
DL = 'C:/User/Chrom/Downloads'
for relPath,dirs,files in os.walk(DL):
 fullPath = os.path.join(DL,relPath,doc)
 print(fullPath)
 if doc in files:
    docu = open(doc, "r")
    content = docu.read()
    print(content)
    docu.close()
