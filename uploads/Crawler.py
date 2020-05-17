import json , urllib.request
def crawler_fun(Jahr):


    Endergebnis_Spieltag = []

    Endergebnisse_Jahr = []

    # Schleife für alle Spieltage
    for i in range(1,34):

        # Daten von Openligadb
        Spieltaglink = ("https://www.openligadb.de/api/getmatchdata/bl1/") + str(Jahr) + ("/") + str(i)

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

            # Tore von der Heimmannschaft , Gastmannschaft
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

            # Zusammenfügen der Spiele am Spieltag
            Endergebnis_Spieltag.append(Goalslist)
            # Spieltag einfügen in alle gespielte Spiele
            Endergebnisse_Jahr.append(Endergebnis_Spieltag)
            
    
    #print(Endergebnis_Spieltag)
    #print(Endergebnisse_Jahr) 
    return Endergebnisse_Jahr
    
   
# Test Jahr
crawler_fun(2018)

#Jahr = input("Von welchem Jahr sollen die Spieldaten geladen werden? ")
#crawler_fun(Jahr)