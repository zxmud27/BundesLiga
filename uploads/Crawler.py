import json
import urllib.request
import csv


def crawler_fun(Jahr):

    Endergebnis_Spieltag = []

    Endergebnisse_Jahr = []

    counter = 0
    # CSV file name
    filename = str(Jahr) + ('.csv')

    # loop for every season
    for i in range(1, 35):

        # files from Openligadb
        Spieltaglink = (
            "https://www.openligadb.de/api/getmatchdata/bl1/") + str(Jahr) + ("/") + str(i)

       # extracts files of one match day
        req = urllib.request.urlopen(Spieltaglink)
        jso = json.loads(req.read().decode())

        # function looks for every encounter of one match day

        for f in jso:

            # end result of match
            MaRe = dict.get(f, "MatchResults")

            # verifies if the current match has been played or not
            if not len(MaRe) == 0:
                versuch = dict.get(MaRe[0], "PointsTeam1")
            else:
                versuch = None

            if versuch is not None:
                # name of the playing home team, away team
                Match = []

               # name of the playing home team, away team
                Teamlist = []

                # saves home team
                team1 = dict.get(f, "Team1")
                name1 = dict.get(team1, "TeamName")
                Teamlist.append(name1)

                # saves away team
                team2 = dict.get(f, "Team2")
                name2 = dict.get(team2, "TeamName")
                Teamlist.append(name2)

                Match.append(Teamlist)

                # goals home team, away team
                Goalslist = []

                # goals home team

                goalsteam1 = dict.get(MaRe[0], "PointsTeam1")
                Goalslist.append(goalsteam1)

               # goals away team
                goalsteam2 = dict.get(MaRe[0], "PointsTeam2")
                Goalslist.append(goalsteam2)

                # puts together matches of match day
                Match.append(Goalslist)

                # date and time of match day
                get_datum = dict.get(f, "MatchDateTime")
                Datum = str(get_datum)
                Match.append(Datum)

                if counter < 9:

                    team_icons = []

                    team_one_icon = dict.get(team1, "TeamIconUrl")
                    team_two_icon = dict.get(team2, "TeamIconUrl")

                    # insert icons into the array
                    team_icons.append(team_one_icon)
                    team_icons.append(team_two_icon)

                    Match.append(team_icons)

                # Teamlist, Goallist and date
                # List of Strings, List of Strings, String
                Endergebnis_Spieltag.append(Match)

                counter += 1
        # Insert all played matches of the day
        Endergebnisse_Jahr.append(Endergebnis_Spieltag)
        Endergebnis_Spieltag = []

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        for i in Endergebnisse_Jahr:
            for j in i:
                writer.writerow(j)

#Jahr = input("Von welchem Jahr sollen die Spieldaten geladen werden? ")
# crawler_fun(2018)
