import csv 
import os.path
from os import path
from Crawler import crawler_fun

def get_all_matches(Jahr):
    # CSV Name
    filename = str(Jahr) + ('.csv')
    teams = []
    
    # Auslesen der Teams
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        # Zähler für gespielte spiele
        k = 0
        # CSV wird gelesen und ausgewertet
        for i in csv_reader:
            # Alle Teamname eingetragen?, wird in den ersten 9 Spielen auf False gesetzt

            # Namen der zwei Teams die gegeneinander spielen an dem Tag
            names = i[0]
            # Torverhältnis nach dem Ende des Spiels
            goals = i[1]

            #Auftrennung von "names" -> Teamname beider Teams wird entnommen
            both_teams = names.strip('["]').split(', ') 
            teama = both_teams[0]
            teama = teama[1:-1]
            teamb = both_teams[1]
            teamb = teamb[1:-1]

            #Auftrennung der Tore, von Team A geschossene Tore : goals_a, von Team B geschossene Tore : goals_b
            all_goals = goals.strip('["]').split(', ') 
            goals_a = int(all_goals[0])
            goals_b = int(all_goals[1])
            
            # Eintragen der Namen in "teams" für die ersten 9 Spiele
            if k < 9:
                
                teamstatsa = []   
                teamstatsa.append(teama)
                teamstatsa.append([[],[],[]])
                teams.append(teamstatsa)

                teamstatsb = []
                teamstatsb.append(teamb)
                teamstatsb.append([[],[],[]])
                teams.append(teamstatsb)
            k += 1
            
            # Zähler für die Position des gesuchten Teams
            c = 0

            # teams[get teamstats][in [1] = all stats][0= won  1 = draw, 2 lose]
            # team[][][]
            if goals_a > goals_b :
                for x in teams:
                    if x[0]== teama:
                        teams[c][1][0].append(teamb)
                    c += 1
                c = 0
                for y in teams:
                    if y[0] == teamb:
                        teams[c][1][2].append(teama)
                    c += 1
                
            elif goals_a < goals_b:
                for x in teams:
                    if x[0] == teamb:
                         teams[c][1][0].append(teama)
                    c += 1
                c = 0
                for y in teams:
                    if y[0] == teama:
                        teams[c][1][2].append(teamb)
                    c += 1

            elif goals_a == goals_b:
                for x in teams:
                    if x[0] == teama:
                        teams[c][1][1].append(teamb)
                    c += 1
                c = 0
                for y in teams:
                    if y[0] == teamb:
                        teams[c][1][1].append(teama)
                    c += 1         

        return teams
            
def get_win_ratio(home, away):
    all_stats = []
    for i in range(9):
        file = 2009 + i
        if not path.exists(str(file) + ('.csv')):
            crawler_fun(file) 
        all_stats.append(get_all_matches(file))

    win = 0
    draw = 0
    lose = 0
    win_ratio = 0
    draw_ratio = 0
    lose_ratio = 0
    played_games = 0 
    counter = 0
    for n in all_stats:
        for x in n:
            if x[0] == home:
                for g in x[1][0]:
                    if g == away:
                        win += 1
                        played_games += 1
                for h in x[1][1]:
                    if h == away:
                        draw += 1
                        played_games += 1
                for j in x[1][2]:
                    if j == away:
                        lose += 1
                        played_games += 1

    if not played_games == 0:
        win_ratio = win / played_games * 100
        draw_ratio = draw / played_games * 100
        lose_ratio = lose / played_games * 100

    ratio = [win_ratio, draw_ratio, lose_ratio]
    print(win , " " , draw , " " , lose)
    print(ratio)
    return ratio

#get_win_ratio('FC Bayern',"Borussia Dortmund")