import random

team1 = "Team A"
team2 = "Team B"

num_matches = 10
num_rounds = 5

team1_score = 0
team2_score = 0

team1_skill = {}
offense = int(input("Enter the offensive ability of team A: "))
defense = int(input("Enter the defensive ability of team A: "))
if(offense > 100 or offense < 0 and defense >100 or defense <0 ):
    print("Invalid atributes. Please try again.")
    quit()
team1_skill["offense"] = offense
team1_skill["defense"] = defense

team2_skill = {}
offense = int(input("Enter the offensive ability of team B: "))
defense = int(input("Enter the defensive ability of team B: "))
if(offense > 100 or offense < 0 and defense >100 or defense <0 ):
    print("Invalid atributes. Please try again.")
    quit()
team2_skill["offense"] = offense
team2_skill["defense"] = defense


team1_res = []

for matches in range(num_matches):
    for round in range(num_rounds):
        if random.uniform(0.7,1) < (team1_skill["offense"] / 100):
            print("Team A gets the balls\n")
            team2_defense = team2_skill["defense"] * random.uniform(0.5, 1.1)
            if random.random()  < (team1_skill["offense"] / (team1_skill["offense"] + team2_defense)):
                team1_score += 1
                print(f"Round {round+1}: {team1} scores! {team1}: {team1_score}, {team2}: {team2_score}\n")
            else:
                 print(f"Round {round+1}: {team1} misses! {team1}: {team1_score}, {team2}: {team2_score}\n")

        else:
            print("Team B gets the balls\n")
            team1_defense = team1_skill["defense"] * random.uniform(0.5, 1.1)
            if random.random() < (team2_skill["offense"] / (team2_skill["offense"] + team1_defense)):
                team2_score += 1
                print(f"Round {round+1}: {team2} scores! {team1}: {team1_score}, {team2}: {team2_score}\n")
            else:
                print(f"Round {round+1}: {team2} misses! {team1}: {team1_score}, {team2}: {team2_score}\n")


    if team1_score > team2_score:
        print(f"\n{team1} wins! Final score: {team1}: {team1_score}, {team2}: {team2_score}")
        team1_res.append(1)
    elif team2_score > team1_score:
        print(f"\n{team2} wins! Final score: {team1}: {team1_score}, {team2}: {team2_score}")
        team1_res.append(-1)
    else:
        print(f"\nIt's a tie! Final score: {team1}: {team1_score}, {team2}: {team2_score}")
        team1_res.append(0)
    team1_score=0
    team2_score=0

team1_win=0
draw=0
team2_win=0
for i in team1_res:
    if(i==1):
        team1_win+=1
    elif(i==0):
        draw+=1
    else:
        team2_win+=1
print("\n")    
print("winning percentage of team A: ",team1_win/10,"\n")
print("winning percentage of team B: ",team2_win/10,"\n")
print("Total No of draws: ",draw)
