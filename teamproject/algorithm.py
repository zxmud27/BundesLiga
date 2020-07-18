import csv
import os.path
from os import path
from teamproject.crawler import CRAWLER
from urllib.request import urlretrieve

class algo:

    def __init__(self,home, away, start_day, start_year, end_day, end_year):
        self.home = home
        self.away = away
        self.start_day = start_day
        self.start_year = start_year
        self.end_day = end_day
        self.end_year = end_year

    def get_all_matches(self,start_season_day, start_season_year, end_season_day):

        """

        Evaluating the stats of team from the csv file:
            win
            tie
            loose
        
        -----------
        Parameters:
        -----------

        start_season_day : int
            first match day the algorithm uses to evaluate the win , tie and loose ratio of all team 
    
        start_season_year : int
            first match year the algorithm uses to evaluate the win , tie and loose ratio of all team 

        end_season_day : int
            the algorithm evaluates the win, tie and loose ratio of all teams untill the last day of the match year
        
        -------
        Return:
        -------
    
        list with three lists:
            [[teamA][teamB]] [[scoreA][scoreB][matchtime and matchday]]
    
        """


        # CSV Name
        folder = "teamproject/match_year/"
        filename = str(start_season_year) + ('.csv')
        teams = []

        # Reading the teams
        with open(folder+filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            # Counter for played games
            k = 0
            startday_counter = 0
            # CSV file is read and evaluated
            for i in csv_reader:

                startday_counter += 1
                if (startday_counter / 9) + \
                        1 > start_season_day and (startday_counter / 9) <= end_season_day:
                    # are all teamnames signed in? is set to false in the first 9 games
                    # Name of the 2 competing teams
                    names = i[0]
                    # goals ratio after the match
                    goals = i[1]

                    # Auftrennung von "names" -> Teamname beider Teams wird
                    # entnommen
                    both_teams = names.strip('["]').split(', ')
                    teama = both_teams[0]
                    teama = teama[1:-1]
                    teamb = both_teams[1]
                    teamb = teamb[1:-1]

                    # Seperation of goals, team a's goals: goals_a, team b's goals:
                    # goals_b
                    all_goals = goals.strip('["]').split(', ')
                    goals_a = int(all_goals[0])
                    goals_b = int(all_goals[1])

                    # enters names in "teams" for the first 9 matches
                    if k < 9:

                        teamstatsa = []
                        teamstatsa.append(teama)
                        teamstatsa.append([[], [], []])
                        teams.append(teamstatsa)

                        teamstatsb = []
                        teamstatsb.append(teamb)
                        teamstatsb.append([[], [], []])
                        teams.append(teamstatsb)
                    k += 1

                    # counter for position of the wanted team
                    c = 0

                    # teams[get teamstats][in [1] = all stats][0= won  1 = draw, 2 lose]
                    # team[][][]
                    if goals_a > goals_b:
                        for x in teams:
                            if x[0] == teama:
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


    def get_win_ratio(self):
        """
        Evaluating lists from get_all_matches() function
        to evaluate the win, tie and loose ratio

        -----------
        Parameters:
        -----------

        home : string
            home team name

        away : string
            away team name

        start_day : int
            first match day 
    
        start_year : int
            first match year  

        end_day : int
            last match day
        
        end_year : int
            last match year
        -------
        Return:
        -------
    
        list with three arguments:
            [[win ratio][tie ratio][loose ratio]]
    
        """
        folder = "teamproject/match_year/"
        all_stats = []
        match_year = self.start_year
        while match_year <= self.end_year:
            if not path.exists(folder+str(match_year) + ('.csv')):
                match = CRAWLER(match_year)
                match.csvcreater()
            if self.start_year == self.end_year:
                all_stats.append(self.get_all_matches(self.start_day, match_year, self.end_day))
            elif match_year == self.start_year:
                all_stats.append(self.get_all_matches(self.start_day, match_year, 34))
            elif match_year < self.end_year:
                all_stats.append(self.get_all_matches(1, match_year, 34))
            elif match_year == self.end_year:
                all_stats.append(self.get_all_matches(1, match_year, self.end_day))
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
                if x[0] == self.home:
                    for g in x[1][0]:
                        if g == self.away:
                            win += 1
                            played_games += 1
                    for h in x[1][1]:
                        if h == self.away:
                            draw += 1
                            played_games += 1
                    for j in x[1][2]:
                        if j == self.away:
                            lose += 1
                            played_games += 1

        if not played_games == 0:
            win_ratio = win / played_games * 100
            draw_ratio = draw / played_games * 100
            lose_ratio = lose / played_games * 100

        ratio = [round(win_ratio, 4), round(draw_ratio, 4), round(lose_ratio, 4)]
        print(win, " ", draw, " ", lose)
        print(ratio)
        return ratio

    def teamnames_and_icon_links(self,year):
        """
        saving teamnames and icon list into a list

        -----------
        Parameters:
        -----------

        year : int
            season year to get the icons and teams

        -------
        Return:
        -------
    
        list : string
            with names of the team and icons inside
                [[name of team][icon link]]
    
        """
        folder = "teamproject/match_year/"
        filename = str(year) + ('.csv')
        teams = []

        with open(folder+filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            # Counter for played games
            k = 0
            startday_counter = 0
            # CSV file is read and evaluated
            name_icon_list = []
            for i in csv_reader:
    
                k += 1
                if k <= 9:
                    # Name of the 2 competing teams
                    names = i[0]
                    # Icons of the 2 competing teams
                    icon = i[3]

                    # Auftrennung von "names" -> Teamname beider Teams wird
                    # entnommen
                    both_teams = names.strip('["]').split(', ')
                    teama = both_teams[0]
                    teama = teama[1:-1]
                    teamb = both_teams[1]
                    teamb = teamb[1:-1]

                    both_icons = icon.strip('[]').split(', ')
                    icon_a = both_icons[0]
                    icon_a = icon_a[1:-1]
                    icon_b = both_icons[1]
                    icon_b = icon_b[1:-1]
                    
                    cache = []
                    cache.append(teama)
                    cache.append(icon_a)
                    name_icon_list.append(cache)
                    cache = []
                    cache.append(teamb)
                    cache.append(icon_b)
                    name_icon_list.append(cache)

                    #print(name_icon_list)
            return name_icon_list


 
    def icon_download(self,list_with_icons):
        """
        downloading and saving icons of the teams

        -----------
        Parameters:
        -----------

        list : string
            icon links

        -------
        Return:
        -------
    
        saving png
    
        """
        for i in range(0,18):
            name = list_with_icons[i][0]
            url = list_with_icons[i][1]
            filename = name + ".png"
            if not os.path.isfile(filename):
                urlretrieve(url, filename)


game1 = algo('FC Bayern', "Borussia Dortmund", 1, 2009, 34, 2018)
game1.get_win_ratio()
#my_list = game1.teamnames_and_icon_links(2017)
#print(my_list)
#game1.icon_download(my_list)

