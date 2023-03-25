import pandas as pd
import math
 
dt1 = pd.read_csv('game.csv')
teams = pd.read_csv('team.csv')
# del teams['LEAGUE_ID']
# del teams['MIN_YEAR']
# del teams['MAX_YEAR']

#Initial elo values
elos = {"1610612737": 1500, '1610612737': 1500, '1610612738': 1500, '1610612739': 1500, '1610612740': 1500, '1610612741': 1500, '1610612742': 1500,
 '1610612743': 1500, '1610612744':1500, '1610612745':1500, '1610612746': 1500, '1610612747': 1500,'1610612748': 1500,
'1610612749': 1500,'1610612750': 1500,'1610612751': 1500,'1610612752': 1500,'1610612753': 1500,'1610612754': 1500,
'1610612755': 1500,'1610612756': 1500,'1610612757': 1500,'1610612758': 1500,'1610612759': 1500,'1610612760': 1500,'1610612761': 1500,'1610612762': 1500,
'1610612763': 1500,'1610612764': 1500,'1610612765': 1500,'1610612766': 1500}

display = {}

# print(display)
# Function to calculate the Probability

def Probability(rating1, rating2):
 
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400))
 
 
# Function to calculate Elo rating
# K is a constant.
# d determines whether
# Player A wins or Player B.
def EloRating(Ra, Rb, K, d):
 
    # To calculate the Winning
    # Probability of Player B
    Pb = Probability(Ra, Rb)
 
    # To calculate the Winning
    # Probability of Player A
    Pa = Probability(Rb, Ra)
 
    # Case -1 When Player A wins
    # Updating the Elo Ratings
    if (d == 1):
        Ra = Ra + K * (1 - Pa)
        Rb = Rb + K * (0 - Pb)
 
    # Case -2 When Player B wins
    # Updating the Elo Ratings
    else:
        Ra = Ra + K * (0 - Pa)
        Rb = Rb + K * (1 - Pb)
    
    return Ra, Rb

# print(teams.to_string()) 

year = 21959
for row in dt1.itertuples():
    #Note to try and filter out the non-existent franchises
    #(Toronto Huskies 35 and team 36)
    if row[1] > 21960:
        #print('t1:',row[27], ' '+ 't2:',row[53])
        if row[1] != year:
            for k in elos:
                elos[k] = elos[k]*0.75 + 0.25*1505
            year = row[1]
        if row[28] < 0:
            winner = 0
        else:
            winner = 1
        #print(winner)
        elos[str(row[2])], elos[str(row[30])] = EloRating(elos[str(row[2])], elos[str(row[30])], 20, winner)


for row in teams.itertuples():
    display[row[2]] = elos[str(row[1])]

print(display)