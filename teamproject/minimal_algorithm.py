import pandas as pd

class minimal_class():
    
    def get_minimal_probabilities(self, home,away):
        """
        Evaluating csv file to get
        the win, tie and loose ratio

        -----------
        Parameters:
        -----------

        home : string
            home team name

        away : string
            away team name

        -------
        Return:
        -------
    
        list with three probability:
            [win ratio,draw ratio,lose ratio]
        """
        filename = pd.read_csv("teamproject/BundesligaData.csv",encoding='unicode_escape')

        Hometeam_at_home = [filename[filename["HomeTeam"] == home]]
        Hometeam_at_away = [filename[filename["AwayTeam"] == home]]
        Hometeam_against_Awayteam_at_home = [Hometeam_at_home[0][Hometeam_at_home[0]["AwayTeam"] == away]]
        Hometeam_against_Awayteam_at_away = [Hometeam_at_away[0][Hometeam_at_away[0]["HomeTeam"] == away]]
        
        home_win = 0
        draw = 0
        home_lose = 0
        played_games = 0

        for x in range(0,len(Hometeam_against_Awayteam_at_home[0])):
            if Hometeam_against_Awayteam_at_home[0].HomeGoals.iloc[x] > Hometeam_against_Awayteam_at_home[0].AwayGoals.iloc[x]:
                home_win += 1
            elif Hometeam_against_Awayteam_at_home[0].HomeGoals.iloc[x] == Hometeam_against_Awayteam_at_home[0].AwayGoals.iloc[x]:
                draw += 1
            elif Hometeam_against_Awayteam_at_home[0].HomeGoals.iloc[x] < Hometeam_against_Awayteam_at_home[0].AwayGoals.iloc[x]:
                home_lose += 1
            played_games += 1
         
        for x in range(0,len(Hometeam_against_Awayteam_at_away[0])) :
            if Hometeam_against_Awayteam_at_away[0].HomeGoals.iloc[x] < Hometeam_against_Awayteam_at_away[0].AwayGoals.iloc[x]:
                home_win += 1
            elif Hometeam_against_Awayteam_at_away[0].HomeGoals.iloc[x] == Hometeam_against_Awayteam_at_away[0].AwayGoals.iloc[x]:
                draw += 1
            elif Hometeam_against_Awayteam_at_away[0].HomeGoals.iloc[x] > Hometeam_against_Awayteam_at_away[0].AwayGoals.iloc[x]:
                home_lose += 1
            played_games += 1

        if not played_games == 0:
            win_ratio = home_win / played_games * 100
            draw_ratio = draw / played_games * 100
            lose_ratio = home_lose / played_games * 100

        return [round(win_ratio, 4), round(draw_ratio, 4), round(lose_ratio, 4)]

#print(minimal_class().get_minimal_probabilities('FC Bayern','Borussia Dortmund'))
