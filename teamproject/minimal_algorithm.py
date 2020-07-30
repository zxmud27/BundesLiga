import pandas as pd

class minimal_class():

    filename = pd.read_csv("BundesligaData.csv",encoding='unicode_escape')

    def get_minimal_probabilities(home,away):
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

        -------
        Return:
        -------
    
        list with three probability:
            [win ratio,tie ratio,loose ratio]
        """
        filename = pd.read_csv("BundesligaData.csv",encoding='unicode_escape')
        Hometeam_home_games = [filename[filename["HomeTeam"] == home]]
        Hometeam_away_games = [filename[filename["AwayTeam"] == home]]
        Awayteam_home_games = [Hometeam_away_games[0][Hometeam_away_games[0]["HomeTeam"] == away]]
        Awayteam_away_games = [Hometeam_home_games[0][Hometeam_home_games[0]["AwayTeam"] == away]]
        
        print(Awayteam_home_games)
        print(Awayteam_away_games)
        home_win = 0
        draw = 0
        home_lose = 0
        played_games = 0

        for x in Awayteam_home_games:
            if ["HomeGoals"] > ["AwayGoals"]:
                home_win += 1
            elif x["HomeGoals"] == x["AwayGoals"]:
                draw += 1
            elif x["HomeGoals"] < x["AwayGoals"]:
                home_lose += 1
            played_games += 1

        for x in Awayteam_away_games[0]:
            if x["HomeGoals"] < x["AwayGoals"]:
                home_win += 1
            elif x["HomeGoals"] == x["AwayGoals"]:
                draw += 1
            elif x["HomeGoals"] > x["AwayGoals"]:
                home_lose += 1
            played_games += 1
        
        if not played_games == 0:
            win_ratio = home_win / played_games * 100
            draw_ratio = draw / played_games * 100
            lose_ratio = home_lose / played_games * 100
        
        print([round(win_ratio, 4), round(draw_ratio, 4), round(lose_ratio, 4)])
        return [round(win_ratio, 4), round(draw_ratio, 4), round(lose_ratio, 4)]

        



minimal_class.get_minimal_probabilities("Hertha BSC","1. FC Köln")
