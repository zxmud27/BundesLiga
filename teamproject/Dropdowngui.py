from tkinter import *
import tkinter as tk
#from teamproject.algorithm import algo
#from Crawler import CrawlerX
#test GUI aufrufen
# Hello Tutorial
root = tk.Tk()
root.title("Bundesliga Vorhersage")
canvas = tk.Canvas(root, height=600, width=1200)
canvas.pack()
frame = tk.Frame(root, bg='black')
frame.place(relwidth=1, relheight=1)

def nextmatchdayList(): # Potential Parameter to edit with Crawler
    #NextMatchDay  Potentiell in extra Methode, um sie zu varrieren über Crawler
    nextMatchDay = tk.Label(frame,text="Nächster Spieltag", bg='black',fg='white',font='bold')
    nextMatchDay.place(relx=0.75,rely=0.18)
    matchdayTeam1 = tk.Label(frame,text="Team 1", bg='black',fg='white', font='bold') 
    matchdayTeam1.place(relx=0.73,rely=0.25)
    firstMatchVs = tk.Label(frame,text="V.S.", bg='black',fg='white', font='bold') 
    firstMatchVs.place(relx=0.79,rely=0.25)
    matchdayTeam2 = tk.Label(frame,text="Team 2", bg='black',fg='white', font='bold') 
    matchdayTeam2.place(relx=0.83,rely=0.25)
    matchdayTeam3 = tk.Label(frame,text="Team 3", bg='black',fg='white', font='bold') 
    matchdayTeam3.place(relx=0.73,rely=0.3)
    secondMatchVs = tk.Label(frame,text="V.S.", bg='black',fg='white', font='bold') 
    secondMatchVs.place(relx=0.79,rely=0.3)
    matchdayTeam4 = tk.Label(frame,text="Team 4", bg='black',fg='white', font='bold') 
    matchdayTeam4.place(relx=0.83,rely=0.3)
    matchdayTeam5 = tk.Label(frame,text="Team 5", bg='black',fg='white', font='bold') 
    matchdayTeam5.place(relx=0.73,rely=0.35)
    thirdMatchVs = tk.Label(frame,text="V.S.", bg='black',fg='white', font='bold') 
    thirdMatchVs.place(relx=0.79,rely=0.35)
    matchdayTeam6 = tk.Label(frame,text="Team 6", bg='black',fg='white', font='bold') 
    matchdayTeam6.place(relx=0.83,rely=0.35)
    matchdayTeam7 = tk.Label(frame,text="Team 7", bg='black',fg='white', font='bold') 
    matchdayTeam7.place(relx=0.73,rely=0.4)
    fourthMatchVs = tk.Label(frame,text="V.S.", bg='black',fg='white', font='bold') 
    fourthMatchVs.place(relx=0.79,rely=0.4)
    matchdayTeam8 = tk.Label(frame,text="Team 8", bg='black',fg='white', font='bold') 
    matchdayTeam8.place(relx=0.83,rely=0.4)
    matchdayTeam9 = tk.Label(frame,text="Team 9", bg='black',fg='white', font='bold') 
    matchdayTeam9.place(relx=0.73,rely=0.45)
    fifthMatchVs = tk.Label(frame,text="V.S.", bg='black',fg='white', font='bold') 
    fifthMatchVs.place(relx=0.79,rely=0.45)
    matchdayTeam10 = tk.Label(frame,text="Team 10", bg='black',fg='white', font='bold') 
    matchdayTeam10.place(relx=0.83,rely=0.45)
    matchdayTeam11 = tk.Label(frame,text="Team 11", bg='black',fg='white', font='bold') 
    matchdayTeam11.place(relx=0.73,rely=0.5)
    sixthMatchVs = tk.Label(frame,text="V.S.", bg='black',fg='white', font='bold') 
    sixthMatchVs.place(relx=0.79,rely=0.5)
    matchdayTeam12 = tk.Label(frame,text="Team 12", bg='black',fg='white', font='bold') 
    matchdayTeam12.place(relx=0.83,rely=0.5)
    matchdayTeam13 = tk.Label(frame,text="Team 13", bg='black',fg='white', font='bold') 
    matchdayTeam13.place(relx=0.73,rely=0.55)
    seventhMatchVs = tk.Label(frame,text="V.S.", bg='black',fg='white', font='bold') 
    seventhMatchVs.place(relx=0.79,rely=0.55)
    matchdayTeam14 = tk.Label(frame,text="Team 14", bg='black',fg='white', font='bold') 
    matchdayTeam14.place(relx=0.83,rely=0.55)
    matchdayTeam15 = tk.Label(frame,text="Team 15", bg='black',fg='white', font='bold') 
    matchdayTeam15.place(relx=0.73,rely=0.6)
    eightMatchVs = tk.Label(frame,text="V.S.", bg='black',fg='white', font='bold') 
    eightMatchVs.place(relx=0.79,rely=0.6)
    matchdayTeam16 = tk.Label(frame,text="Team 16", bg='black',fg='white', font='bold') 
    matchdayTeam16.place(relx=0.83,rely=0.6)
    matchdayTeam17 = tk.Label(frame,text="Team 17", bg='black',fg='white', font='bold') 
    matchdayTeam17.place(relx=0.73,rely=0.65)
    ninthMatchVs = tk.Label(frame,text="V.S.", bg='black',fg='white', font='bold') 
    ninthMatchVs.place(relx=0.79,rely=0.65)
    matchdayTeam18 = tk.Label(frame,text="Team 18", bg='black',fg='white', font='bold') 
    matchdayTeam18.place(relx=0.83,rely=0.65)
def staticGUI():
    CrawlerButton = tk.Button(
        frame,
        text="Start Crawler",
        width=25,
        height=2,
        fg="white",
        bg='brown4')
    CrawlerButton.place(relx=0.20, rely=0.15)
    changeModeButton = tk.Button(frame, text="Lightmode", width=20, height=2, fg="white", bg="brown4")# , command =lambda: changemode()
    changeModeButton.place(relx=0.01, rely=0.01)
    startButton = tk.Button(
        frame,
        text="Starte Vorhersage",
        width=25,
        height=2,
        fg="white",
        bg='brown4')
    startButton.place(relx=0.202, rely=0.5)   
    #Labels Mini-Algo
    winHome = tk.Label(frame, text="Win Home:", bg='black', fg='white',height=3,width=8)
    winHome.place(relx=0.1, rely=0.6)
    pWH = tk.Label(frame, text="PercentWH", bg='black',
                   fg='white',height=3,width=8)  # Übersetzer für team1 und team2
    pWH.place(relx=0.1, rely=0.65)
    draw = tk.Label(frame, text="Draw:", bg='black', fg='white',height=3,width=8)
    draw.place(relx=0.25, rely=0.6)
    pDraw = tk.Label(frame, text="PercDRAW", bg='black', fg='white',height=3,width=8)
    pDraw.place(relx=0.25, rely=0.65)
    winAway = tk.Label(frame, text="Win Away:", bg='black', fg='white',height=3,width=8)
    winAway.place(relx=0.4, rely=0.6)
    pWA = tk.Label(frame, text="PercentWA", bg='black', fg='white',height=3,width=8)
    pWA.place(relx=0.4, rely=0.65)

   

    #Grafik Labels
    vsLabel = tk.Label(
        frame,
        text="V.S.",
        bg='black',
        fg='white', width=3, height=1, font='bold')
    vsLabel.place(relx=0.26, rely=0.27)
    untilLabel = tk.Label(frame, text="until", bg='black', fg='white',height=2,width=3, font='bold')
    untilLabel.place(relx=0.33, rely=0.009)
def winrateLabels(
        team1,
        team2,
        clicked_day_Start,
        clicked_season_Start,
        clicked_day_End,
        clicked_season_End):
    stats_from_algorithm = algo(
        team1, team2, int(
            clicked_day_Start.get()), int(
            clicked_season_Start.get()), int(
                clicked_day_End.get()), int(
                    clicked_season_End.get()))
    stats = stats_from_algorithm.get_win_ratio()
    # algo1.get_win_ratio(Ubersetzer(team1),Ubersetzer(team2))
    # Winrate
    # Übersetzer für team1 und team2
    pWH = tk.Label(frame, text=stats[0], bg='black', fg='white')
    pWH.place(relx=0.20, rely=0.9, relwidth=0.2, relheight=0.04)
    # Drawrate
    pDraw = tk.Label(frame, text=stats[1], bg='black', fg='white')
    pDraw.place(relx=0.40, rely=0.9, relwidth=0.2, relheight=0.04)
    # Loserate
    pWA = tk.Label(frame, text=stats[2], bg='black', fg='white')
    pWA.place(relx=0.6, rely=0.9, relwidth=0.2, relheight=0.04)
def matchdayDropDown():
    seasons_Start = [
        2009,
        2010,
        2011,
        2012,
        2013,
        2014,
        2015,
        2016,
        2017,
        2018,
        2019
    ]
    # reversed list with all seasons
    seasons_End = seasons_Start[::1]

    # List with all match days
    matchdays_Start = []
    for i in range(0, 34):
        matchdays_Start.append(i+1)

    # reversed list with all match days
    matchdays_End=[]
    for j in range(0,34):
        matchdays_End.append(j+1)
    #matchdays_End = matchdays_Start[::-1]

    clicked_day_Start = StringVar()
    clicked_day_Start.set(matchdays_Start[0])
    matchdays_start_menu = tk.OptionMenu(frame, clicked_day_Start, *matchdays_Start,)
    matchdays_start_menu.place(relx=0.2, rely=0.015)

    clicked_season_Start = StringVar()
    clicked_season_Start.set(seasons_Start[0])
    season_start_menu = OptionMenu(frame, clicked_season_Start, *seasons_Start)
    season_start_menu.place(relx=0.25, rely=0.015)

    clicked_day_End = StringVar()
    clicked_day_End.set(matchdays_End[-1])
    matchdays_end_menu = OptionMenu(root, clicked_day_End, *matchdays_End)
    matchdays_end_menu.place(relx=0.38, rely=0.015)

    clicked_season_End = StringVar()
    clicked_season_End.set(seasons_End[-1])
    season_end_menu = OptionMenu(root, clicked_season_End,*seasons_End)
    season_end_menu.place(relx=0.43, rely=0.015)
    
def sportDropDown():
    liga_dropdown = [
        "Erste Liga",
        "Zweite Liga",
        "Dritte Liga"
    ]
    click_liga_dropdown = StringVar()
    click_liga_dropdown.set("Auswahl der Liga")
    liga_menu = tk.OptionMenu(frame, click_liga_dropdown, *liga_dropdown)
    liga_menu.place(relx=0.6, rely=0.015)
    
    sports_dropdown = [
        "Fußball",
        "Handball",
    ]
    click_sports_dropdown = StringVar()
    click_sports_dropdown.set("Auswahl der Sportart")
    sport_menu = tk.OptionMenu(frame, click_sports_dropdown, *sports_dropdown)
    sport_menu.place(relx=0.73, rely=0.015)
def seasonTextfield():
    #Catch Strings ->  https://docs.python.org/3/tutorial/errors.html
     selectionofseasonText = tk.Label(frame,text="Saisonauswahl", bg='black', fg='white' )
     selectionofseasonText.place(relx=0.8,rely=0.01,relwidth=0.2,relheight=0.015)
     selectionofseason= tk.Entry(frame)
     #selectionofseason.insert(1, "Saisonauswahl")
     selectionofseason.place(relx=0.87,rely=0.03,relwidth=0.061) # Auslesen von Wert mit StartCrawler Buttón
def teamDropdown(teams_dropdown): #Array -> also die Dropdownliste vom Crawler mit den teams
    click_teams_dropdown = StringVar()
    click_teams_dropdown.set("Wähle das Team")
    team1_menu = tk.OptionMenu(frame, click_teams_dropdown, *teams_dropdown)
    team1_menu.place(relx=0.12, rely=0.265)
    click_teams_dropdown = StringVar()
    click_teams_dropdown.set("Wähle das Team")
    team2_menu = tk.OptionMenu(frame, click_teams_dropdown, *teams_dropdown)
    team2_menu.place(relx=0.315, rely=0.265)
def algoDropdownR(registryPatterninput): #using when registrypattern is implemented
    click_registryPatterninput_dropdown = StringVar()
    click_registryPatterninput_dropdown.set("Wähle den Algorithmus")
    algo_menu = tk.OptionMenu(frame, click_registryPatterninput_dropdown, *registryPatterninput)
    algo_menu.place(relx=0.01, rely=0.3)
def algoDropdown():
    algo_dropdown=[
        "Minimaler Algorithmus",
        "Poisson Algorithmus"
    ]
    click_algo_dropdown = StringVar()
    click_algo_dropdown.set("Wähle den Algorithmus")
    algo_menu = tk.OptionMenu(frame, click_algo_dropdown, *algo_dropdown)
    algo_menu.place(relx=0.21, rely=0.4)
nextmatchdayList()
algoDropdown() 
teams=["hadelan peterpan", "leagueisCancer", "salami aleikum"] #Beispiel Array <- teams müssen inserted werden in teamDropdown(teams)
teamDropdown(teams)
seasonTextfield()
matchdayDropDown()
sportDropDown()
staticGUI()
root.mainloop()