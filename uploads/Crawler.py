import json , urllib.request
def crawler_fun(Jahr, Spieltag):

    Endergebnis_Spieltag = []
    # Daten von Openligadb
    Spieltaglink = ("https://www.openligadb.de/api/getmatchdata/bl1/") + str(Jahr) + ("/") + str(Spieltag)

    # zieht Daten eines Spieltages
    req = urllib.request.urlopen(Spieltaglink)
    jso = json.loads(req.read().decode())

    # Funktion schaut jede Begegnung eines Spieltages an
    
    for f in jso:
        
        # Namen der spielenden Heimmannschaft , Gastmannschaft
        Teamlist = []

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

        Endergebnis_Spieltag.append(Teamlist)

        # Ergebnis Heimmannschaft , Gastmannschaft
        Goalslist = []

        # Endergebnis
        MaRe = dict.get(f, "MatchResults")
        
        # Tore Heimmannschaft
        goalsteam1 = dict.get(MaRe[0], "PointsTeam1")
        Heimtor = str(goalsteam1)
        Goalslist.append(Heimtor)

        # Tore Gastmannschaft
        goalsteam2 = dict.get(MaRe[0], "PointsTeam2")
        Gasttor = str(goalsteam2)
        Goalslist.append(Gasttor)

        Endergebnis_Spieltag.append(Goalslist)
    
    print(Endergebnis_Spieltag) 
    return Endergebnis_Spieltag
    
   
#Jahr = input("Gibt mir das Jahr an! ")
#Tag = input("Vom welchen Spieltag willst du die Daten erhalten? ")

crawler_fun(2018,1)
