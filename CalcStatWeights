import csv
import random


# File paths
teamsPath = "C:\\1516teams.csv"
statsPath = "C:\\1516stats.csv"
matchupsPath = "C:\\1516matchups.csv"

#global variables, lists, etc
teams = []
bestCorrectPredictions = 0
bestWt = {"winPct":0,"scorOff":0,"scorDef":0,"scorMarg":0,"FGPct":0,
          "FGPctDef":0,"threeFGPG":0,"threeFGPct":0,"threeFGPctDef":0,
          "FTPct":0,"rbdMarg":0,"astPG":0,"astTurnRatio":0,"blocksPG":0,
          "stealsPG":0,"turnsPG":0,"turnMarg":0,"foulsPG":0,"totBlocks":0,
          "totAsts":0,"totRbds":0,"FTAtt":0,"FTMade":0,"threeFGAtt":0,
          "threeFGMade":0,"totSteals":0,"totTurns":0,"totFouls":0,
          "offRbdsPG":0,"defRbdsPG":0,"turnsForced":0,"totRbdsPG":0,"seed":0}

weights = {"winPctWt":0,"scorOffWt":0,"scorDefWt":0,"scorMargWt":0,"FGPctWt":0,
          "FGPctDefWt":0,"threeFGPGWt":0,"threeFGPctWt":0,"threeFGPctDefWt":0,
          "FTPctWt":0,"rbdMargWt":0,"astPGWt":0,"astTurnRatioWt":0,
          "blocksPGWt":0,"stealsPGWt":0,"turnsPGWt":0,"turnMargWt":0,
          "foulsPGWt":0,"totBlocksWt":0,"totAstsWt":0,"totRbdsWt":0,
          "FTAttWt":0,"FTMadeWt":0,"threeFGAttWt":0,"threeFGMadeWt":0,
          "totStealsWt":0,"totTurnsWt":0,"totFoulsWt":0,"offRbdsPGWt":0,
          "defRbdsPGWt":0,"turnsForcedWt":0,"totRbdsPGWt":0,"seedWt":0}

#Get list of teams (as strings) from file
def readTeams(): 
    with open(teamsPath) as teamsFile:
        reader = csv.reader(teamsFile)
        for row in reader:
            teams.append(row[0])    

#creates dictionary for each statistic category, with key "Kentucky", e.g.
def createDict(column):
    with open(statsPath) as statsFile:
        reader = csv.reader(statsFile)
        reader.__next__()
        stat = {rows[0]:float(rows[column]) for rows in reader}
        return stat

def generateWts():
    for weight in weights:
        weights[weight] = random.uniform(-1,1)

#initialize score dict- "Kentucky":0 , e.g.   
def createScoreDict():
    with open(teamsPath) as teamsFile:
        reader = csv.reader(teamsFile)
        scores = {rows[0]: 0 for rows in reader}
        return scores

#self-explanatory: calculates the score by adding stat*weight    
def calculateTeamScore(team):
    score = (winPct[team] * weights["winPctWt"] +
             scorOff[team] * weights["scorOffWt"] +
             scorDef[team] * weights["scorDefWt"] +
             scorMarg[team] * weights["scorMargWt"] +
             FGPct[team] * weights["FGPctWt"] +
             FGPctDef[team] * weights["FGPctDefWt"] +
             threeFGPG[team] * weights["threeFGPGWt"] +
             threeFGPct[team] * weights["threeFGPctWt"] +
             threeFGPctDef[team] * weights["threeFGPctDefWt"] +
             FTPct[team] * weights["FTPctWt"] +
             rbdMarg[team] * weights["rbdMargWt"] +
             astPG[team] * weights["astPGWt"] +
             astTurnRatio[team] * weights["astTurnRatioWt"] +
             blocksPG[team] * weights["blocksPGWt"] +
             stealsPG[team] * weights["stealsPGWt"] +
             turnsPG[team] * weights["turnsPGWt"] +
             turnMarg[team] * weights["turnMargWt"] +
             foulsPG[team] * weights["foulsPGWt"] +
             totBlocks[team] * weights["totBlocksWt"] +
             totAsts[team] * weights["totAstsWt"] +
             totRbds[team] * weights["totRbdsWt"] +
             FTAtt[team] * weights["FTAttWt"] +
             FTMade[team] * weights["FTMadeWt"] +
             threeFGAtt[team] * weights["threeFGAttWt"] +
             threeFGMade[team] * weights["threeFGMadeWt"] +
             totSteals[team] * weights["totStealsWt"] +
             totTurns[team] * weights["totTurnsWt"] +
             totFouls[team] * weights["totFoulsWt"] +
             offRbdsPG[team] * weights["offRbdsPGWt"] +
             defRbdsPG[team] * weights["defRbdsPGWt"] +
             turnsForced[team] * weights["turnsForcedWt"] +
             totRbdsPG[team] * weights["totRbdsPGWt"] +
             seed[team] * weights["seedWt"])
             
    return score

#compares scores of 2 teams per match-up, +1 to count if predicted correctly
def runMatchups():
    numCorrect = 0
    with open(matchupsPath) as matchupsFile:
        reader = csv.reader(matchupsFile)
        reader.__next__()
        for row in reader:
            if score[row[0]] > score[row[1]]:
                numCorrect = numCorrect + 1
    return numCorrect

#self-explanatory- sets a new "best score" for count and weights
def setNewBestPredictions():
    global bestCorrectPredictions
    bestCorrectPredictions = numCorrectPredictions
    bestWt["winPct"] = weights["winPctWt"]
    bestWt["scorOff"] = weights["scorOffWt"]
    bestWt["scorDef"] = weights["scorDefWt"]
    bestWt["scorMarg"] = weights["scorMargWt"]
    bestWt["FGPct"] = weights["FGPctWt"]
    bestWt["FGPctDef"] = weights["FGPctDefWt"]
    bestWt["threeFGPG"] = weights["threeFGPGWt"]
    bestWt["threeFGPct"] = weights["threeFGPctWt"]
    bestWt["threeFGPctDef"] = weights["threeFGPctDefWt"]
    bestWt["FTPct"] = weights["FTPctWt"]
    bestWt["rbdMarg"] = weights["rbdMargWt"]
    bestWt["astPG"] = weights["astPGWt"]
    bestWt["astTurnRatio"] = weights["astTurnRatioWt"]
    bestWt["blocksPG"] = weights["blocksPGWt"]
    bestWt["stealsPG"] = weights["stealsPGWt"]
    bestWt["turnsPG"] = weights["turnsPGWt"]
    bestWt["turnMarg"] = weights["turnMargWt"]
    bestWt["foulsPG"] = weights["foulsPGWt"]
    bestWt["totBlocks"] = weights["totBlocksWt"]
    bestWt["totAsts"] = weights["totAstsWt"]
    bestWt["totRbds"] = weights["totRbdsWt"]
    bestWt["FTAtt"] = weights["FTAttWt"]
    bestWt["FTMade"] = weights["FTMadeWt"]
    bestWt["threeFGAtt"] = weights["threeFGAttWt"]
    bestWt["threeFGMade"] = weights["threeFGMadeWt"]
    bestWt["totSteals"] = weights["totStealsWt"]
    bestWt["totTurns"] = weights["totTurnsWt"]
    bestWt["totFouls"] = weights["totFoulsWt"]
    bestWt["offRbdsPG"] = weights["offRbdsPGWt"]
    bestWt["defRbdsPG"] = weights["defRbdsPGWt"]
    bestWt["turnsForced"] = weights["turnsForcedWt"]
    bestWt["totRbdsPG"] = weights["totRbdsPGWt"]
    bestWt["seed"] = weights["seedWt"]

def calcScores():
    global numCorrectPredictions
    for team in teams:
    #Sets score for each team
        score[team] = calculateTeamScore(team)
        #compare scores in team matchups, and count correct predictions
        numCorrectPredictions = runMatchups()
        if numCorrectPredictions > bestCorrectPredictions:
            setNewBestPredictions()
            print(bestCorrectPredictions, "/ 63 correct predictions")
            print(bestWt)

#Initialize
readTeams()
score = createScoreDict()

#Create stats dictionaries
winPct = createDict(1)
scorOff = createDict(2)
scorDef = createDict(3)
scorMarg = createDict(4)
FGPct = createDict(5)
FGPctDef = createDict(6)
threeFGPG = createDict(7)
threeFGPct = createDict(8)
threeFGPctDef = createDict(9)
FTPct = createDict(10)
rbdMarg = createDict(11)
astPG = createDict(12)
astTurnRatio = createDict(13)
blocksPG = createDict(14)
stealsPG = createDict(15)
turnsPG = createDict(16)
turnMarg = createDict(17)
foulsPG = createDict(18)
totBlocks = createDict(19)
totAsts = createDict(20)
totRbds = createDict(21)
FTAtt = createDict(22)
FTMade = createDict(23)
threeFGAtt = createDict(24)
threeFGMade = createDict(25)
totSteals = createDict(26)
totTurns = createDict(27)
totFouls = createDict(28)
offRbdsPG = createDict(29)
defRbdsPG = createDict(30)
turnsForced = createDict(31)
totRbdsPG = createDict(32)
seed = createDict(33)
                  
#Loops until target number of correct predictions is reached
while bestCorrectPredictions < 63:
    generateWts()
    calcScores()
