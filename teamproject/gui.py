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
teamfoto = PhotoImage(file='bilder/teamwahl.png')
bayernMuenchen = PhotoImage(file='bilder/fcb.png')
dortmund    = PhotoImage(file='bilder/bvb.png')
moenchengladbach = PhotoImage(file='bilder/bmg.png')
rbLeipzig   = PhotoImage(file='bilder/rbl.png')
leverkusen  = PhotoImage(file='bilder/b04.png')
wolfsburg   = PhotoImage(file='bilder/wob.png')
freiburg = PhotoImage(file='bilder/scf.png')
schalke04   = PhotoImage(file='bilder/s04.png')
hoffenheim  = PhotoImage(file='bilder/tsg.png')
herthaBSC   = PhotoImage(file='bilder/bsc.png')
eintrachtFrankfurt = PhotoImage(file='bilder/sge.png')
augsburg = PhotoImage(file='bilder/fca.png')
mainz05  = PhotoImage(file='bilder/m05.png')
fortunaduesseldorf   = PhotoImage(file='bilder/f95.png')
werderBremen   = PhotoImage(file='bilder/svw.png')
stuttgart = PhotoImage(file='bilder/vfb.png')
hannover = PhotoImage(file='bilder/hn96.png')
nurnberg = PhotoImage(file='bilder/nb.png')
tname1 = dortmund
tname2 = wolfsburg
inputTeamname1 = dortmund
inputTeamname2 = dortmund
global counter1
counter1=0
global counter2
counter2=0
def Ubersetzer(teamname):
    if(teamname == bayernMuenchen):
        return 'FC Bayern'
    elif(teamname == herthaBSC):
        return 'Hertha BSC'
    elif(teamname == werderBremen):
        return 'Werder Bremen'
    elif(teamname == freiburg):
        return 'SC Freiburg'
    elif(teamname == wolfsburg):
        return 'VfL Wolfsburg'
    elif(teamname == fortunaduesseldorf):
        return 'Fortuna Düsseldorf'
    elif(teamname == moenchengladbach):
        return 'Borussia Mönchengladbach'
    elif(teamname == mainz05):
        return '1. FSV Mainz 05'
    elif(teamname == dortmund):
        return 'Borussia Dortmund'
    elif(teamname == hoffenheim):
        return 'TSG 1899 Hoffenheim'
    elif(teamname == nurnberg):
        return '1. FC Nürnberg'
    elif(teamname == hannover):
        return 'Hannover 96'
    elif(teamname == eintrachtFrankfurt):
        return 'Eintracht Frankfurt'
    elif(teamname == schalke04):
        return 'FC Schalke 04'
    elif(teamname == augsburg):
        return 'FC Augsburg'
    elif(teamname == leverkusen):
        return 'Bayer Leverkusen'
    elif(teamname == stuttgart):
        return 'VfB Stuttgart'
    elif(teamname == rbLeipzig):
        return 'RB Leipzig'
def buttonupdate(buttonnummer, teamname):
    if(buttonnummer == 1):
        global firstTeamButton
        firstTeamButton = tk.Button(
            frame,
            image=teamname,
            width=150,
            height=150,
            fg="white",
            bg='black',
            command=lambda: newframe(1))
        firstTeamButton.place(
            relx=0.10, rely=0.2)
        global tname1
        tname1 = teamname
        resetButton(1)
    else:
        global secondTeamButton
        secondTeamButton = tk.Button(
            frame,
            image=teamname,
            width=150,
            height=150,
            fg="white",
            bg='black',
            command=lambda: newframe(2))
        secondTeamButton.place(
            relx=0.35,
            rely=0.2)
        global tname2
        tname2 = teamname
        resetButton(0)
    newWindow.destroy()
def resetButton(buttonnummer):
    if(buttonnummer==1):
        global counter2
        if(counter2==0):
            zweitesTeamButton['state']='normal'
        else:
            secondTeamButton['state']='normal'
    elif(buttonnummer==0):
        global counter1
        if(counter1==0):
            erstesTeamButton['state']='normal'
        else:
            firstTeamButton['state']='normal'
def newframe(buttonnummer):
    global counter1
    if(counter1==1):
        firstTeamButton['state']='disabled'
    else:
        erstesTeamButton['state']='disabled'
    global counter2
    if(counter2==1):
        secondTeamButton['state']='disabled'
    else:
        zweitesTeamButton['state']='disabled'
    if(buttonnummer==1):
        counter1=1
    else:
        counter2=1

    global newWindow
    newWindow = tk.Toplevel(root)
    canvas = tk.Canvas(newWindow, height=900, width=400)
    canvas.pack()
    teamset(buttonnummer)
def teamset(buttonnummer):
    frame2 = tk.Frame(newWindow, bg='black')
    frame2.place(relwidth=1, relheight=1)
    BM = tk.Button(
        frame2,
        image=bayernMuenchen,
        bg='black',
        command=lambda: buttonupdate(
            buttonnummer,
            bayernMuenchen))
    BM.place(relx=0.0, rely=0.0, relwidth=1/2, relheight=1/9)
    DM = tk.Button(
        frame2,
        image=dortmund,
        bg='black',
        command=lambda: buttonupdate(
            buttonnummer,
            dortmund))
    DM.place(relx=0.5, rely=0.0, relwidth=1/2, relheight=1/9)
    MG = tk.Button(
        frame2,
        image=moenchengladbach,
        bg='black',
        command=lambda: buttonupdate(
            buttonnummer,
            moenchengladbach))
    MG.place(relx=0.0, rely=1/9, relwidth=1/2, relheight=1/9)
    RL = tk.Button(
        frame2,
        image=rbLeipzig,
        bg='black',
        command=lambda: buttonupdate(
            buttonnummer,
            rbLeipzig))
    RL.place(relx=0.5, rely=1/9, relwidth=1/2, relheight=1/9)
    LK = tk.Button(
        frame2,
        image=leverkusen,
        bg='black',
        command=lambda: buttonupdate(
            buttonnummer,
            leverkusen))
    LK.place(relx=0.0, rely=2/9, relwidth=1/2, relheight=1/9)
    WB = tk.Button(
        frame2,
        image=wolfsburg,
        bg='black',
        command=lambda: buttonupdate(
            buttonnummer,
            wolfsburg))
    WB.place(relx=0.5, rely=2/9, relwidth=1/2, relheight=1/9)
    FB = tk.Button(
        frame2,
        image=freiburg,
        bg='black',
        command=lambda: buttonupdate(
            buttonnummer,
            freiburg))
    FB.place(relx=0.0, rely=3/9, relwidth=1/2, relheight=1/9)
    S4 = tk.Button(
        frame2,
        image=schalke04,
        bg='black',
        command=lambda: buttonupdate(
            buttonnummer,
            schalke04))
    S4.place(relx=0.5, rely=3/9, relwidth=1/2, relheight=1/9)
    HH = tk.Button(
        frame2,
        image=hoffenheim,
        bg='black',
        command=lambda: buttonupdate(
            buttonnummer,
            hoffenheim))
    HH.place(relx=0.0, rely=4/9, relwidth=1/2, relheight=1/9)
    HN = tk.Button(
        frame2,
        image=hannover,
        bg='black',
        command=lambda: buttonupdate(
            buttonnummer,
            hannover))
    HN.place(relx=0.5, rely=4/9, relwidth=1/2, relheight=1/9)
    HBSC = tk.Button(
        frame2,
        image=herthaBSC,
        bg='black',
        command=lambda: buttonupdate(
            buttonnummer,
            herthaBSC))
    HBSC.place(relx=0.0, rely=5/9, relwidth=1/2, relheight=1/9)
    ST = tk.Button(
        frame2,
        image=stuttgart,
        bg='black',
        command=lambda: buttonupdate(
            buttonnummer,
            stuttgart))
    ST.place(relx=0.5, rely=5/9, relwidth=1/2, relheight=1/9)
    EF = tk.Button(
        frame2,
        image=eintrachtFrankfurt,
        bg='black',
        command=lambda: buttonupdate(
            buttonnummer,
            eintrachtFrankfurt))
    EF.place(relx=0.0, rely=6/9, relwidth=1/2, relheight=1/9)
    AB = tk.Button(
        frame2,
        image=augsburg,
        bg='black',
        command=lambda: buttonupdate(
            buttonnummer,
            augsburg))
    AB.place(relx=0.5, rely=6/9, relwidth=1/2, relheight=1/9)
    M5 = tk.Button(
        frame2,
        image=mainz05,
        bg='black',
        command=lambda: buttonupdate(
            buttonnummer,
            mainz05))
    M5.place(relx=0.0, rely=7/9, relwidth=1/2, relheight=1/9)
    FD = tk.Button(
        frame2,
        image=fortunaduesseldorf,
        bg='black',
        command=lambda: buttonupdate(
            buttonnummer,
            fortunaduesseldorf))
    FD.place(relx=0.5, rely=7/9, relwidth=1/2, relheight=1/9)
    WB = tk.Button(
        frame2,
        image=werderBremen,
        bg='black',
        command=lambda: buttonupdate(
            buttonnummer,
            werderBremen))
    WB.place(relx=0.0, rely=8/9, relwidth=1/2, relheight=1/9)
    NN = tk.Button(
        frame2,
        image=nurnberg,
        bg='black',
        command=lambda: buttonupdate(
            buttonnummer,
            nurnberg))
    NN.place(relx=0.5, rely=8/9, relwidth=1/2, relheight=1/9)
def staticGUI():
    global erstesTeamButton
    erstesTeamButton = tk.Button(
        frame,
        image=dortmund,
        width=150,
        height=150,
        bg='black',
        command=lambda: newframe(1))
    erstesTeamButton.place(relx=0.10, rely=0.2)
    global zweitesTeamButton
    zweitesTeamButton = tk.Button(
        frame,
        image=wolfsburg,
        width=150,
        height=150,
        bg='black',
        command=lambda: newframe(2))
    zweitesTeamButton.place(
        relx=0.35,
        rely=0.2,)
    CrawlerButton = tk.Button(
        frame,
        text="Start Crawler",
        width=25,
        height=2,
        fg="white",
        bg='brown4')
    CrawlerButton.place(relx=0.09, rely=0.52)
    IncludeSeasonButtonCheckBox = tk.Checkbutton(
        frame, text="Include current Season", bg='black',fg='red',height=1,width=17,font='bold')
    IncludeSeasonButtonCheckBox.place(
        relx=0.09, rely=0.61)
    startTrain = tk.Button(
        frame,
        text="Start Training",
        width=25,
        height=2,
        fg="white",
        bg='brown4')
    startTrain.place(relx=0.3, rely=0.6)
    poissonAlgoButton = tk.Button(
        frame,
        text="Poisson-Algorithmus",
        width=25,
        height=2,
        fg="white",
        bg='brown4')
    poissonAlgoButton.place(relx=0.3, rely=0.52)    
    # Labels
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

    #Labels Mini-Algo
    winHome = tk.Label(frame, text="Win Home:", bg='black', fg='white',height=3,width=8)
    winHome.place(relx=0.47, rely=0.7)
    pWH = tk.Label(frame, text="PercentWH", bg='black',
                   fg='white',height=3,width=8)  # Übersetzer für team1 und team2
    pWH.place(relx=0.53, rely=0.7)
    draw = tk.Label(frame, text="Draw:", bg='black', fg='white',height=3,width=8)
    draw.place(relx=0.47, rely=0.75)
    pDraw = tk.Label(frame, text="PercDRAW", bg='black', fg='white',height=3,width=8)
    pDraw.place(relx=0.53, rely=0.75)
    winAway = tk.Label(frame, text="Win Away:", bg='black', fg='white',height=3,width=8)
    winAway.place(relx=0.47, rely=0.8)
    pWA = tk.Label(frame, text="PercentWA", bg='black', fg='white',height=3,width=8)
    pWA.place(relx=0.53, rely=0.8)
    #Labels Poisson-Algo
    winHomePoisson = tk.Label(frame, text="Win Home:", bg='black', fg='white',height=3,width=8)
    winHomePoisson.place(relx=0.47, rely=0.47)
    pWHPoisson = tk.Label(frame, text="PercentWH", bg='black',
                   fg='white',height=3,width=8)  # Übersetzer für team1 und team2
    pWHPoisson.place(relx=0.53, rely=0.47)
    drawPoisson = tk.Label(frame, text="Draw:", bg='black', fg='white',height=3,width=8)
    drawPoisson.place(relx=0.47, rely=0.52 )
    pDrawPoisson = tk.Label(frame, text="PercDRAW", bg='black', fg='white',height=3,width=8)
    pDrawPoisson.place(relx=0.53, rely=0.52)
    winAwayPoisson = tk.Label(frame, text="Win Away:", bg='black', fg='white',height=3,width=8)
    winAwayPoisson.place(relx=0.47, rely=0.57)
    pWAPoisson = tk.Label(frame, text="PercentWA", bg='black', fg='white',height=3,width=8)
    pWAPoisson.place(relx=0.53, rely=0.57)

    #Grafik Labels
    vsLabel = tk.Label(
        frame,
        text="V.S.",
        bg='black',
        fg='white', width=3, height=1, font='bold')
    vsLabel.place(relx=0.27, rely=0.3)
    untilLabel = tk.Label(frame, text="until", bg='black', fg='white',height=2,width=3, font='bold')
    untilLabel.place(relx=0.27, rely=0.12)
def winrateLabels(
        team1,
        team2,
        clicked_day_Start,
        clicked_season_Start,
        clicked_day_End,
        clicked_season_End):
    stats_from_algorithm = algo(
        Ubersetzer(team1), Ubersetzer(team2), int(
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
def dropDownMenu():
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

    clicked_season_Start = StringVar()
    clicked_season_Start.set(seasons_Start[0])
    season_start_menu = OptionMenu(frame, clicked_season_Start, *seasons_Start)
    season_start_menu.place(relx=0.16, rely=0.12)

    clicked_day_Start = StringVar()
    clicked_day_Start.set(matchdays_Start[0])
    matchdays_start_menu = tk.OptionMenu(frame, clicked_day_Start, *matchdays_Start,)
    matchdays_start_menu.place(relx=0.11, rely=0.12)

    clicked_season_End = StringVar()
    clicked_season_End.set(seasons_End[-1])
    season_end_menu = OptionMenu(root, clicked_season_End,*seasons_End)
    season_end_menu.place(relx=0.41, rely=0.12)

    clicked_day_End = StringVar()
    clicked_day_End.set(matchdays_End[-1])
    matchdays_end_menu = OptionMenu(root, clicked_day_End, *matchdays_End)
    matchdays_end_menu.place(relx=0.36, rely=0.12)
    
    miniAlgoButton = tk.Button(
        frame,
        text="Minimaler-Algorithmus",
        width=25,
        height=2,
        fg="white",
        bg='brown4',
        command=lambda: winrateLabels(
            tname1,
            tname2,
            clicked_day_Start,
            clicked_season_Start,
            clicked_day_End,
            clicked_season_End))
    miniAlgoButton.place(relx=0.3, rely=0.75)
    poissonAlgoButton = tk.Button(
        frame,
        text="Poisson-Algorithmus",
        width=25,
        height=2,
        fg="white",
        bg='brown4')
    poissonAlgoButton.place(relx=0.3, rely=0.52)   


dropDownMenu()
staticGUI()
root.mainloop()
