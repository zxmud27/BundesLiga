import requests
import json
import csv

class DataCrawler():

    def clear(self):
        """
            delete all values in the csv file
        """
        open("teamproject/BundesligaData.csv", "w")

    def getSeasons(self, FirstDay, FirstSeason, LastDay,LastSeason, league):
        """

        crawling data from Website and saving 
           - hometeam,
           - awayteam,
           - homegoals,
           - awaygoals,
           - date
        into a csv file.

        -----------
        Parameters:
        -----------

        FirstDay : int
            start day of the first season

        FirstSeason : int
            from this season on the data get crawled

        LastDay : int
            last day of the last season

        LastSeason : int
            till this season the data get crawled
    
        league : string
            selection of the league:
                input can only be "b1" , "b2" or "b3"

        -------
        Return:
        -------
    
        saving data into csv file

        """
        self.clear()
        csv = open("teamproject/BundesligaData.csv", "w")
        csv.write(
            "HomeTeam" +
            "," +
            "AwayTeam" +
            "," +
            "HomeGoals" +
            "," +
            "AwayGoals" +
            "," +
            "Date" +
            "\n")
        if league == "b1" or league == "b2" or league == "b3":
            for i in range(FirstSeason, (LastSeason + 1)):
                counter = 0
                startday_counter = 0
                Game = {}
                Date = {}

                GameDay = {}
                HomeTeam = {}
                AwayTeam = {}
                GoalsHome = {}
                GoalsAway = {}

                if FirstSeason == LastSeason:
                    start_season_day = FirstDay
                    end_season_day = LastDay
                elif i == FirstSeason and FirstDay != 1:
                    start_season_day = FirstDay
                    end_season_day = 34
                elif i == LastSeason and LastDay != 34:
                    start_season_day = 1
                    end_season_day = LastDay
                else:
                    start_season_day = 1
                    end_season_day = 34

                if league == "b1":
                    game_data = json.loads(requests.get(f'http://www.openligadb.de/api/getmatchdata/bl1/{i}').text)
                elif league == "b2":
                    game_data = json.loads(requests.get(f'http://www.openligadb.de/api/getmatchdata/bl2/{i}').text)
                elif league == "b3":
                    game_data = json.loads(requests.get(f'http://www.openligadb.de/api/getmatchdata/bl3/{i}').text)


                for game in game_data:
                    startday_counter += 1
                    if (startday_counter / 9) + 1 > start_season_day and (startday_counter / 9) <= end_season_day:

                        Date[counter] = game['MatchDateTime']
                        Team1 = game['Team1']
                        HomeTeam[counter] = Team1['TeamName']

                        Team2 = game['Team2']
                        AwayTeam[counter] = Team2['TeamName']

                        Matchresults = game['MatchResults']

                        Result_half  = Matchresults[0]
                        TeamA_half = Result_half['PointsTeam1']
                        TeamB_half = Result_half['PointsTeam2']

                        if not len(Matchresults) == 1:
                            Result = Matchresults[1]
                            TeamA = Result['PointsTeam1']
                            TeamB = Result['PointsTeam2']
                        else:
                            TeamA = -1
                            TeamB = -1

                        if TeamA_half + TeamB_half > TeamA + TeamB:
                            GoalsHome[counter] = TeamA_half
                            GoalsAway[counter] = TeamB_half
                        else:
                            GoalsHome[counter] = TeamA
                            GoalsAway[counter] = TeamB

                        match = HomeTeam[counter] + "," + AwayTeam[counter] + "," + str(GoalsHome[counter]) + "," + str(GoalsAway[counter]) + "," + Date[counter] + "\n"
                        csv.write(match)
                        counter += 1
        else:
            print('Wrong string for crawling a certain league')

    def getNamelist(self, year,league):
        """

        crawling teamnames of the the year variable

        -----------
        Parameters:
        -----------

        year : int
            match year

        league : string
            selection of the league
                input can only be "b1" , "b2" or "b3"

        -------
        Return:
        -------
    
        name_list: list of strings
            Teamnames in the list are saved to work with

        """


        startday_counter = 0
        name_list = []
        counter = 0
        if league == "b1" or league == "b2" or league == "b3":
            for i in range(year, (year + 1)):
                if league == "b1":
                    game_data = json.loads(requests.get(f'http://www.openligadb.de/api/getmatchdata/bl1/{i}').text)
                elif league == "b2":
                    game_data = json.loads(requests.get(f'http://www.openligadb.de/api/getmatchdata/bl2/{i}').text)
                elif league == "b3":
                    game_data = json.loads(requests.get(f'http://www.openligadb.de/api/getmatchdata/bl3/{i}').text)

                for game in game_data:
                    startday_counter += 1
                    if startday_counter <= 9:

                        Team1 = game['Team1']
                        name_list.append(Team1['TeamName'])

                        Team2 = game['Team2']
                        name_list.append(Team2['TeamName'])
                        counter += 1

                return name_list
        else:
            print('Wrong string for crawling a certain league')



#BLCrawler = DataCrawler()
#BLCrawler.getSeasons(1,2011,22,2018,"b2")
#print(BLCrawler.getNamelist(2019,"b2"))