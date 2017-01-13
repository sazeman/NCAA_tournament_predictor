import csv
import random

# File paths for source data
teamsPath = "C:\\teams2014_2015.csv"
statsPath = "C:\\stats2014_2015.csv"
matchupsPath = "C:\\matchups2014_2015.csv"

# Global variables, lists, etc
teams = []
bestCorrectPredictions = 0
bestWt = {"seed": 0, "gmsPly": 0, "winPct": 0, "scorMar": 0,
          "threeFGPct": 0, "astTORatio": 0, "foulsPG": 0, "threeFGPG": 0,
          "fgPct": 0, "totRPG": 0, "ftPct": 0, "assistsPG": 0, "pointsPG": 0,
          "oppPPG": 0, "offRebsPG": 0, "stealsPG": 0, "blocksPG": 0}

weights = {"seedWt": 0, "gmsPlyWt": 0, "winPctWt": 0, "scorMarWt": 0,
          "threeFGPctWt": 0, "astTORatioWt": 0, "foulsPGWt": 0, "threeFGPGWt": 0,
          "fgPctWt": 0, "totRPGWt": 0, "ftPctWt": 0, "assistsPGWt": 0, "pointsPGWt": 0,
          "oppPPGWt": 0, "offRebsPGWt": 0, "stealsPGWt": 0, "blocksPGWt": 0}

# Get list of teams (as strings) from file
def readTeams(): 
    with open(teamsPath) as teamsFile:
        reader = csv.reader(teamsFile)
        for row in reader:
            teams.append(row[0])    

# Creates dictionary for each statistic category, with key "Kentucky", e.g.
def createDict(column):
    with open(statsPath) as statsFile:
        reader = csv.reader(statsFile)
        reader.__next__()
        stat = {rows[0]:float(rows[column]) for rows in reader}
        return stat

# Generate random weight
def generateWts():
    for weight in weights:
        weights[weight] = random.uniform(-100,100)

# Gets list of weights for each statistic
def createWtLst(column):
    weights = []
    with open(weightsPath) as weightsFile:
        reader = csv.reader(weightsFile)
        reader.next()
        for row in reader:
            weights.append(row[column])
        return map(float, weights)

# Create dict of team "scores" (Initially set to 0)  
def createScoreDict():
    with open(teamsPath) as teamsFile:
        reader = csv.reader(teamsFile)
        scores = {rows[0]: 0 for rows in reader}
        return scores

# Calculate score  
def calculateTeamScore(team):
    score = (seed[team] * weights["seedWt"] +
                 gmsPly[team] * weights["gmsPlyWt"] +
                 winPct[team] * weights["winPctWt"] +
                 scorMar[team] * weights["scorMarWt"] +
                 threeFGPct[team] * weights["threeFGPctWt"] +
                 astTORatio[team] * weights["astTORatioWt"] +
                 foulsPG[team] * weights["foulsPGWt"] +
                 threeFGPG[team] * weights["threeFGPGWt"] +
                 fgPct[team] * weights["fgPctWt"] +
                 totRPG[team] * weights["totRPGWt"] +
                 ftPct[team] * weights["ftPctWt"] +
                 assistsPG[team] * weights["assistsPGWt"] +
                 pointsPG[team] * weights["pointsPGWt"] +
                 oppPPG[team] * weights["oppPPGWt"] +
                 offRebsPG[team] * weights["offRebsPGWt"] +
                 stealsPG[team] * weights["stealsPGWt"] +
                 blocksPG[team] * weights["blocksPGWt"])
    return score

# Compares scores of 2 teams per match-up, +1 to count if predicted correctly
def runMatchups():
    numCorrect = 0
    with open(matchupsPath) as matchupsFile:
        reader = csv.reader(matchupsFile)
        reader.__next__()
        for row in reader:
            if score[row[0]] > score[row[1]]:
                numCorrect = numCorrect + 1
    return numCorrect

# Sets new best weights and prediction total
def setNewBestPredictions():
    global bestCorrectPredictions
    bestCorrectPredictions = numCorrectPredictions
    bestWt["seed"] = weights["seedWt"]
    bestWt["gmsPly"] = weights["gmsPlyWt"]
    bestWt["winPct"] = weights["winPctWt"]
    bestWt["scorMar"] = weights["scorMarWt"]
    bestWt["threeFGPct"] = weights["threeFGPctWt"]
    bestWt["astTORatio"] = weights["astTORatioWt"]
    bestWt["foulsPG"] = weights["foulsPGWt"]
    bestWt["threeFGPG"] = weights["threeFGPGWt"]
    bestWt["fgPct"] = weights["fgPctWt"]
    bestWt["totRPG"] = weights["totRPGWt"]
    bestWt["ftPct"] = weights["ftPctWt"]
    bestWt["assistsPG"] = weights["assistsPGWt"]
    bestWt["pointsPG"] = weights["pointsPGWt"]
    bestWt["oppPPG"] = weights["oppPPGWt"]
    bestWt["offRebsPG"] = weights["offRebsPGWt"]
    bestWt["stealsPG"] = weights["stealsPGWt"]
    bestWt["blocksPG"] = weights["blocksPGWt"]

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

#Create stats dicitonaries
seed = createDict(1)
gmsPly = createDict(5)
winPct = createDict(4)
scorMar = createDict(11)
threeFGPct = createDict(14)
astTORatio = createDict(15)
foulsPG = createDict(16)
threeFGPG = createDict(17)
fgPct = createDict(18)
totRPG = createDict(19)
ftPct = createDict(20)
assistsPG = createDict(21)
pointsPG = createDict(8)
oppPPG = createDict(10)
offRebsPG = createDict(22)
stealsPG = createDict(24)
blocksPG = createDict(26)

#Loops until target number of correct predictions is reached
while bestCorrectPredictions < 60:
    generateWts()
    calcScores()
