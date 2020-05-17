import json
def crawler(Jahr, Spieltag):

    # Teams einer Saison
    Teamlist = []
    Goalslist = []

    # Daten von Openligadb
    Spieltaglink = ("https://www.openligadb.de/api/getmatchdata/bl1/") + str(Jahr) + ("/") + str(Spieltag)

    # zieht Daten eines Spieltages
    req = json.get(Spieltaglink)
    jso = json.loads(req.text)

    # Funktion schaut jede Begegnung eines Spieltages an

    for f in jso:

        # Speichert Heimmannschaft
        team1 = dict.get(f, "Team1")
        name1 = dict.get(team1, "TeamName")
        Heim = str(name1)
        Teamlist.append(Heim)

        # Speichert Gastmannschaft
        team2 = dict.get(f, "Team2")
        name2 = dict.get(team2, "TeamName")
        Gast = str(name2)
        Teamlist.append(Gast)

        # Endergebnis
        MaRe = dict.get(f, "MatchResults")

        # Tore Heimmannschaft
        goalsteam1 = dict.get(MaRe, "PointsTeam1")
        Heimtor = str(goalsteam1)
        Goalslist.append(Heimtor)

        # Tore Gastmannschaft
        goalsteam2 = dict.get(MaRe, "PointsTeam2")
        Gasttor = str(goalsteam2)
        Goalslist.append(Gasttor)

    return Teamlist
    return Goalslist
