import csv 
import os.path
from os import path
from Crawler import crawler_fun

def get_all_matches(start_season_day ,start_season_year,end_season_day):
    # CSV Name
    filename = str(start_season_year) + ('.csv')
    teams = []
    
     # Reading the teams
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
         # Counter for played games
        k = 0
        startday_counter = 0
         # CSV file is read and evaluated
        for i in csv_reader:
            
            startday_counter += 1
            if (startday_counter / 9) + 1 > start_season_day and (startday_counter / 9) <= end_season_day :
                # are all teamnames signed in? is set to false in the first 9 games
                # Name of the 2 competing teams
                names = i[0]
                # goals ratio after the match
                goals = i[1]

                #Auftrennung von "names" -> Teamname beider Teams wird entnommen
                both_teams = names.strip('["]').split(', ') 
                teama = both_teams[0]
                teama = teama[1:-1]
                teamb = both_teams[1]
                teamb = teamb[1:-1]

                #Seperation of goals, team a's goals: goals_a, team b's goals: goals_b
                all_goals = goals.strip('["]').split(', ') 
                goals_a = int(all_goals[0])
                goals_b = int(all_goals[1])
            
                # enters names in "teams" for the first 9 matches
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
            
                # counter for position of the wanted team
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
            
def get_win_ratio(home, away, start_day, start_year ,end_day, end_year):
    all_stats = []
    match_year = start_year 
    while match_year <= end_year:
        if not path.exists(str(match_year) + ('.csv')):
            crawler_fun(match_year) 
        if match_year == start_year == end_year:
            all_stats.append(get_all_matches(start_day ,match_year,end_day))
        elif match_year == start_year:
            all_stats.append(get_all_matches(start_day,match_year,34))
        elif match_year == end_year:
            all_stats.append(get_all_matches(1,match_year,end_day))
        match_year += 1
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

#get_win_ratio('FC Bayern',"Borussia Dortmund",1,2018,10,2018)
#get_all_matches(1,2018,3)