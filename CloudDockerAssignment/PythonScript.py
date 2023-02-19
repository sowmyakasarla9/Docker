import os
import socket
from collections import Counter

Counter = Counter()

def getMyIPAdress():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return IPAddr

def getNumberOfWords(file):
    totalWordCount = 0
    with open(file, 'r') as file:
        for line in file:
            if (line != '\n'):
                if (file.name.endswith("IF.txt")):
                    Counter.update(line.replace("Â", "").split())
                totalWordCount = totalWordCount + len(line.replace("Â", "").split())
    return totalWordCount

TxtFilesWordCounts = {}
path ="/home/data"
if os.path.exists(path + "/" +"result.txt"):
  os.remove(path + "/" +"result.txt")
finalString="----- a. Text files at location: /home/data -----\n"
for allFile in os.listdir(path):
    if allFile.endswith(".txt"):
        finalString=finalString+allFile+"\n"
        TxtFilesWordCounts[allFile] = getNumberOfWords(path + "/" + allFile)
		
finalString=finalString+"\n"
finalString=finalString+"----- b. Total number of words in each text files -----\n"
wordCountOfAllFiles = 0
fileNames = ""
for eachkey in TxtFilesWordCounts.keys():
    fileNames = fileNames + eachkey + ","
    wordCountOfAllFiles = wordCountOfAllFiles + TxtFilesWordCounts.get(eachkey)
    finalString = finalString +"Number of words in [" + eachkey + "] is : " + str(TxtFilesWordCounts.get(eachkey))+"\n"

finalString = finalString +"\n"
finalString = finalString +"----- c. Total number of words in both files -----\n"
finalString = finalString +"Number of words in both files [" + fileNames[0:len(fileNames) - 1] + "] is: " + str(wordCountOfAllFiles)+"\n"

finalString = finalString +"\n"
finalString = finalString +"----- d. top 3 words with maximum number of counts in IF.txt -----\n"
finalString = finalString +str(Counter.most_common(3))+"\n"

finalString = finalString +"\n"
finalString = finalString +"----- e. IP address -----\n"
finalString = finalString +"IP Address of this machine is:" + getMyIPAdress()

resultsTextFile = open(path + "/" +"result.txt","w")
resultsTextFile.write(finalString)
resultsTextFile.close()
for eachline in open(path + "/" +"result.txt","r").readlines():
    print(eachline.replace("\n",""))