
import os

path = input("Enter path to folder: ")

listOfFiles = os.listdir(path)

countOfFiles = len(listOfFiles)

os.chdir(path)

for i in range(0, countOfFiles):

    os.rename(path+listOfFiles[i], str(i)+'.jpg')
