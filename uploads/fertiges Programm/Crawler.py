import json , urllib.request
import csv

class CrawlerX:
    def __init__(self):
        pass
    def crawler_fun(self,Jahr):
        Endergebnis_Spieltag = []
        Endergebnisse_Jahr = []
        # CSV Name
        filename = str(Jahr) + ('.csv')
        # Schleife für alle Spieltage
        for i in range(1,35):
            # Daten von Openligadb
            Spieltaglink = ("https://www.openligadb.de/api/getmatchdata/bl1/") + str(Jahr) + ("/") + str(i)
            # zieht Daten eines Spieltages
            req = urllib.request.urlopen(Spieltaglink)
            jso = json.loads(req.read().decode())
            # Funktion schaut jede Begegnung eines Spieltages an
            for f in jso:
                # Endergebnis des Matchs
                MaRe = dict.get(f, "MatchResults")
                # überprüfen ob das aktuell zu betrachtende Spiel gespielt wurden
                if not len(MaRe) == 0:
                    versuch = dict.get(MaRe[0], "PointsTeam1")
                else:
                    versuch = None

                if versuch != None:
                    # Namen der spielenden Heimmannschaft , Gastmannschaft
                    Match = []

                    # Namen der spielenden Heimmannschaft , Gastmannschaft
                    Teamlist = []

                    # Speichert Heimmannschaft
                    team1 = dict.get(f, "Team1")
                    name1 = dict.get(team1, "TeamName")
                    Teamlist.append(name1)

                    # Speichert Gastmannschaft
                    team2 = dict.get(f, "Team2")
                    name2 = dict.get(team2, "TeamName")
                    Teamlist.append(name2)

                    Match.append(Teamlist)

                    # Tore von der Heimmannschaft , Gastmannschaft
                    Goalslist = []
        
                    # Tore Heimmannschaft
            
                    goalsteam1 = dict.get(MaRe[0], "PointsTeam1")
                    Goalslist.append(goalsteam1)

                    # Tore Gastmannschaft
                    goalsteam2 = dict.get(MaRe[0], "PointsTeam2")
                    Goalslist.append(goalsteam2)

                    # Zusammenfügen der Spiele am Spieltag
                    Match.append(Goalslist)
            
                    # Datum des Spieltages mit Uhrzeit
                    get_datum = dict.get(f,"MatchDateTime")
                    Datum = str(get_datum)
                    Match.append(Datum)

                    # Teamlist, Goallist und des Datums in einer Liste
                    # List of Strings, List of Strings, String
                    Endergebnis_Spieltag.append(Match)

            # Spieltag einfügen in alle gespielte Spiele
            Endergebnisse_Jahr.append(Endergebnis_Spieltag)
            Endergebnis_Spieltag = []
    
    
        with open(filename ,'w', newline='') as f:
            writer = csv.writer(f)
            for i in Endergebnisse_Jahr:
                for j in i:
                    writer.writerow(j)

   # Jahr = input("Von welchem Jahr sollen die Spieldaten geladen werden? ")
    crawler_fun("hi",2019)
 