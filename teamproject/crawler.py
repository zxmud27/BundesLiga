import requests
import json
import csv

class DataCrawler:

    def clear(self):
        """Delete all values in the csv-file

        """
        open("BundesligaData.csv", "w")

    def getSeasons(self, FirstDay, FirstSeason, LastDay,LastSeason):
        self.clear()
        csv = open("BundesligaData.csv", "w")
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

        for i in range(FirstSeason, (LastSeason + 1)):
            counter = 0
            Game = {}
            Date = {}

            GameDay = {}
            HomeTeam = {}
            AwayTeam = {}
            GoalsHome = {}
            GoalsAway = {}

            if i == FirstSeason and FirstDay != 1 :
                game_data = json.loads(requests.get(f"http://www.openligadb.de/api/getmatchdata/bl1/"+str(FirstSeason)+"/"+str(FirstDay)).text)
            elif i == LastSeason and LastDay != 34 :
                game_data = json.loads(requests.get(f"http://www.openligadb.de/api/getmatchdata/bl1/"+ str(LastSeason) +"/"+str(LastDay)).text)
            else:
                game_data = json.loads(requests.get(f'http://www.openligadb.de/api/getmatchdata/bl1/{i}').text)

            for game in game_data:
                for x in game:
                    Date[counter] = game['MatchDateTime']
                    Team1 = game['Team1']
                    HomeTeam[counter] = Team1['TeamName']

                    Team2 = game['Team2']
                    AwayTeam[counter] = Team2['TeamName']

                    Matchresults = game['MatchResults']
                    Result = Matchresults[0]
                    GoalsHome[counter] = Result['PointsTeam1']
                    GoalsAway[counter] = Result['PointsTeam2']

                match = HomeTeam[counter] + "," + AwayTeam[counter] + "," + str(GoalsHome[counter]) + "," + str(GoalsAway[counter]) + "," + Date[counter] + "\n"
                csv.write(match)
                counter += 1


BLCrawler = DataCrawler()
BLCrawler.getSeasons(1,2009,3,2018)
