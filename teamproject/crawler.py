import requests
import json
import csv

class DataCrawler:

    def __init__(self, csvPath):
        """Initialize instance of DataCrawler

        csvPath to where csv-file will be saved"""
        self.csvPath = csvPath

    def clear(self):
        """Delete all values in the csv-file

        """
        csv = open(self.csvPath, "w")

    def getSeasons(self, FirstSeason, LastSeason):
        self.clear()
        csv = open(self.csvPath, "w")
        csv.write(
            "HomeTeam" +
            "," +
            "AwayTeam" +
            "," +
            "HomeGoals" +
            "," +
            "AwayGoals" +
            "," +
            "Data" +
            "," +
            "IconLink" +
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

CVS_Path = "BundesligaData.csv"
BLCrawler = DataCrawler(CVS_Path)
BLCrawler.getSeasons(2009, 2018)
