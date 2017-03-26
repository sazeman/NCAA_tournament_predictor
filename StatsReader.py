import os

#Source Files
inDir = "D:\\1617StatsFiles\\"

def addCommaToWriteString():
    global writeString
    writeString += ","
    
def addTeamNameToWriteString():
    global readerIndex, writeString
    readerIndex = 12
    isTeamName = True
    while isTeamName:
        if fileText[readerIndex] == " ":
            if fileText[readerIndex + 1] == "(":
                if fileText[readerIndex + 2].isdigit():
                    isTeamName = False
        if isTeamName:
            writeString += fileText[readerIndex]
        readerIndex += 1
        
def addValueToWriteString():
    global readerIndex, writeString
    while fileText[readerIndex] != "\t":
        writeString += fileText[readerIndex]
        readerIndex +=1
        
def clearWriteString():
    global writeString
    writeString = ""
    
def resetReaderIndex():
    global readerIndex
    readerIndex = 0
    
def skipToNextLine():
    global readerIndex
    readerIndex = fileText.find("n", readerIndex)
    

# Moves readerIndex to the index of the next tab in the text file    
def skipToNextTab():
    global readerIndex
    readerIndex = fileText.find("\t", readerIndex)
    readerIndex += 1
    
statCategories = ["Won-Lost Percentage",
                  "Scoring Offense",
                  "Scoring Defense",
                  "Scoring Margin",
                  "Field-Goal Percentage",
                  "Field-Goal Percentage Defense",
                  "Three-Point Field Goals Per Game",
                  "Three-Point Field-Goal Percentage",
                  "Three Pt FG Defense",
                  "Free-Throw Percentage",
                  "Rebound Margin",
                  "Assists Per Game",
                  "Assist Turnover Ratio",
                  "Blocked Shots Per Game",
                  "Steals Per Game",
                  "Turnovers Per Game",
                  "Turnover Margin",
                  "Personal Fouls Per Game",
                  "Total Blocks",
                  "Total Assists",
                  "Total Rebounds",
                  "Free Throw Attempts",
                  "Free Throws Made",
                  "3-pt Field Goal Attempts",
                  "Total 3-point FGM",
                  "Total Steals",
                  "Fewest Turnovers",
                  "Fewest Fouls",
                  "Offensive Rebounds Per Game",
                  "Defensive Rebounds per Game",
                  "Turnovers Forced",
                  "Total Rebounds Per Game"]

#Write header row
writeString = "Team,"
for statCategory in statCategories:
    writeString += statCategory
    addCommaToWriteString()
print(writeString)



for statsFile in os.listdir(inDir):
    resetReaderIndex()    
    clearWriteString()
    
    file = open(inDir + statsFile,"r")
    fileText = file.read() #Create string of file

    addTeamNameToWriteString()
    addCommaToWriteString()

    for statCategory in statCategories:
        readerIndex = fileText.find(statCategory)

        skipToNextTab()    
        skipToNextTab()
        addValueToWriteString()
        addCommaToWriteString()
         
    print(writeString)
