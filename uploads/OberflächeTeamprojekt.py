from tkinter import *
import tkinter as tk
from Algorithmus import get_win_ratio
#from Crawler import CrawlerX

#Hello Tutorial
root = tk.Tk()
root.title("GUI")
canvas = tk.Canvas(root, height=400, width=400)
canvas.pack()
frame = tk.Frame(root, bg='gray13')
frame.place(relwidth=1, relheight=1)
#Algo Objekt, Crawler Objekt
#algo1 = Algo()
#craw1 = CrawlerX()
#Images
teamfoto = PhotoImage(file='teamwahl.png')
bayernMuenchen = PhotoImage(file='fcb.png')
dortmund    = PhotoImage(file='bvb.png')
moenchengladbach = PhotoImage(file='bmg.png')
rbLeipzig   = PhotoImage(file='rbl.png')
leverkusen  = PhotoImage(file='b04.png')
wolfsburg   = PhotoImage(file='wob.png')
freiburg = PhotoImage(file='scf.png')
schalke04   = PhotoImage(file='s04.png')
hoffenheim  = PhotoImage(file='tsg.png')
#koeln       = PhotoImage(file='koe.png')
herthaBSC   = PhotoImage(file='bsc.png')
#unionBerlin  = PhotoImage(file='fcu.png')
eintrachtFrankfurt = PhotoImage(file='sge.png')
augsburg = PhotoImage(file='fca.png')
mainz05  = PhotoImage(file='m05.png')
fortunaduesseldorf   = PhotoImage(file='f95.png')
werderBremen   = PhotoImage(file='svw.png')
#paderborn07 = PhotoImage(file='scp.png')
stuttgart = PhotoImage(file='vfb.png')
hannover = PhotoImage(file='hn96.png')
nurnberg = PhotoImage(file='nb.png')
def Ubersetzer(teamname):
   if(teamname==bayernMuenchen):
      return 'FC Bayern'
   elif(teamname==herthaBSC):
      return 'Hertha BSC'
   elif(teamname==werderBremen):
      return 'Werder Bremen'
   elif(teamname==freiburg):
      return 'SC Freiburg'
   elif(teamname==wolfsburg):
      return 'VfL Wolfsburg'
   elif(teamname==fortunaduesseldorf):
      return 'Fortuna Düsseldorf'
   elif(teamname==moenchengladbach):
      return 'Borussia Mönchengladbach'
   elif(teamname==mainz05):
      return '1. FSV Mainz 05'
   elif(teamname==dortmund):
      return 'Borussia Dortmund'
   elif(teamname==hoffenheim):
      return 'TSG 1899 Hoffenheim'
   elif(teamname==nurnberg):
      return '1. FC Nürnberg'
   elif(teamname==hannover):
      return 'Hannover 96'
   elif(teamname==eintrachtFrankfurt):
      return 'Eintracht Frankfurt'
   elif(teamname==schalke04):
      return 'FC Schalke 04'
   elif(teamname==augsburg):
      return 'FC Augsburg' 
   elif(teamname==leverkusen):
      return 'Bayer Leverkusen'
   elif(teamname==stuttgart):
      return 'VfB Stuttgart'
   elif(teamname==rbLeipzig):
      return 'RB Leipzig'
def buttonupdate(buttonnummer, teamname):
   if(buttonnummer==1):
      erstesTeamButton = tk.Button(frame,image= teamname,width=10, height=10, fg="white", bg='gray13',command=lambda: newframe(1))
      erstesTeamButton.place(relx=0.20,rely=0.52, relwidth=0.20, relheight=0.20) 
      global tname1 
      tname1=teamname
      newWindow.destroy()
      
   else:
      zweitesTeamButton = tk.Button(frame,image= teamname,width=10, height=10, fg="white", bg='gray13',command=lambda:newframe(2))
      zweitesTeamButton.place(relx=0.60,rely=0.52, relwidth=0.20, relheight=0.20)
      global tname2
      tname2 = teamname
      newWindow.destroy()

def newframe(buttonnummer):
   global newWindow 
   newWindow= tk.Toplevel(root)
   canvas = tk.Canvas(newWindow, height=900, width=400)
   canvas.pack()
   frame2 = tk.Frame(newWindow, bg='gray13')
   frame2.place(relwidth=1, relheight=1)
   BM =  tk.Button(frame2,image=bayernMuenchen,bg='gray13',command=lambda: buttonupdate(buttonnummer,bayernMuenchen))
   BM.place(relx=0.0,rely=0.0,relwidth=1/2,relheight=1/9)
   DM = tk.Button(frame2,image=dortmund,bg='gray13',command=lambda: buttonupdate(buttonnummer,dortmund))
   DM.place(relx=0.5,rely=0.0,relwidth=1/2,relheight=1/9)
   MG = tk.Button(frame2,image=moenchengladbach,bg='gray13',command=lambda: buttonupdate(buttonnummer,moenchengladbach))
   MG.place(relx=0.0,rely=1/9,relwidth=1/2,relheight=1/9)
   RL = tk.Button(frame2,image=rbLeipzig,bg='gray13',command=lambda: buttonupdate(buttonnummer,rbLeipzig))
   RL.place(relx=0.5,rely=1/9,relwidth=1/2,relheight=1/9)
   LK = tk.Button(frame2,image=leverkusen,bg='gray13',command=lambda: buttonupdate(buttonnummer,leverkusen))
   LK.place(relx=0.0,rely=2/9,relwidth=1/2,relheight=1/9)
   WB = tk.Button(frame2,image=wolfsburg,bg='gray13',command=lambda: buttonupdate(buttonnummer,wolfsburg))
   WB.place(relx=0.5,rely=2/9,relwidth=1/2,relheight=1/9)
   FB = tk.Button(frame2,image=freiburg,bg='gray13',command=lambda: buttonupdate(buttonnummer,freiburg))
   FB.place(relx=0.0,rely=3/9,relwidth=1/2,relheight=1/9)
   S4 = tk.Button(frame2,image=schalke04,bg='gray13',command=lambda: buttonupdate(buttonnummer,schalke04))
   S4.place(relx=0.5,rely=3/9,relwidth=1/2,relheight=1/9)
   HH = tk.Button(frame2,image=hoffenheim,bg='gray13',command=lambda: buttonupdate(buttonnummer,hoffenheim))
   HH.place(relx=0.0,rely=4/9,relwidth=1/2,relheight=1/9)
   HN =  tk.Button(frame2,image=hannover,bg='gray13',command=lambda: buttonupdate(buttonnummer,hannover))
   HN.place(relx=0.5,rely=4/9,relwidth=1/2,relheight=1/9)
   HBSC= tk.Button(frame2,image=herthaBSC,bg='gray13',command=lambda: buttonupdate(buttonnummer,herthaBSC))
   HBSC.place(relx=0.0,rely=5/9,relwidth=1/2,relheight=1/9)
   ST = tk.Button(frame2,image=stuttgart,bg='gray13',command=lambda: buttonupdate(buttonnummer,stuttgart))
   ST.place(relx=0.5,rely=5/9,relwidth=1/2,relheight=1/9)
   EF = tk.Button(frame2,image=eintrachtFrankfurt,bg='gray13',command=lambda: buttonupdate(buttonnummer,eintrachtFrankfurt))
   EF.place(relx=0.0,rely=6/9,relwidth=1/2,relheight=1/9)
   AB = tk.Button(frame2,image=augsburg,bg='gray13',command=lambda: buttonupdate(buttonnummer,augsburg))
   AB.place(relx=0.5,rely=6/9,relwidth=1/2,relheight=1/9)
   M5 = tk.Button(frame2,image=mainz05,bg='gray13',command=lambda: buttonupdate(buttonnummer,mainz05))
   M5.place(relx=0.0,rely=7/9,relwidth=1/2,relheight=1/9)
   FD = tk.Button(frame2,image=fortunaduesseldorf,bg='gray13',command=lambda: buttonupdate(buttonnummer,fortunaduesseldorf))
   FD.place(relx=0.5,rely=7/9,relwidth=1/2,relheight=1/9)
   WB = tk.Button(frame2,image=werderBremen,bg='gray13',command=lambda: buttonupdate(buttonnummer,werderBremen))
   WB.place(relx=0.0,rely=8/9,relwidth=1/2,relheight=1/9)
   NN = tk.Button(frame2,image=nurnberg,bg='gray13',command=lambda: buttonupdate(buttonnummer,nurnberg))
   NN.place(relx=0.5,rely=8/9,relwidth=1/2,relheight=1/9)


erstesTeamButton = tk.Button(frame,image=dortmund,width=10, height=10, bg='gray13', command=lambda: newframe(1))
erstesTeamButton.place(relx=0.20,rely=0.52, relwidth=0.20, relheight=0.20)  


zweitesTeamButton = tk.Button(frame,image=wolfsburg,width=100, height=10, bg='gray13', command=lambda: newframe(2))
zweitesTeamButton.place(relx=0.60,rely=0.52, relwidth=0.20, relheight=0.20)

#Checkbox Inhalt ausgeben in Konsole über Button Befehl.
#buttonstatus = IntVar()
#IncludeSeasonButtonCheckBox = tk.Checkbutton(frame, text="Include current Season", bg="cornflowerblue", variable=buttonstatus)
#IncludeSeasonButtonCheckBox.deselect()
#IncludeSeasonButtonCheckBox.place(relx=0.35,rely=0.165, relwidth=0.4, relheight=0.03)
#def buttonclick():
#     print(buttonstatus.get())
#erstesTeamButton = tk.Button(frame, text="erstes Team",width=10, height=10, fg="white", bg='gray13',command=buttonclick)
#erstesTeamButton.place(relx=0.20,rely=0.52, relwidth=0.2, relheight=0.2)
CrawlerButton = tk.Button(frame, text="Start Crawler",width=30, height=5, fg="white", bg='brown4', padx=10, pady=5 )
CrawlerButton.place(relx=0.06,rely=0.25, relwidth=0.2, relheight=0.1)

IncludeSeasonButtonCheckBox = tk.Checkbutton(frame, text="Include current Season", bg='gray13',fg="white")
IncludeSeasonButtonCheckBox.place(relx=0.35,rely=0.285, relwidth=0.4, relheight=0.03)
tname1=dortmund
tname2=wolfsburg
predictButton = tk.Button(frame, text="Predict",width=10, height=10, fg="white", bg='brown4',command=lambda:winrateLabels(tname1,tname2))
predictButton.place(relx=0.4,rely=0.75, relwidth=0.2, relheight=0.08)
startTrain = tk.Button(frame, text="Start Training",width=10, height=10, fg="white", bg='brown4')
startTrain.place(relx=0.4,rely=0.38, relwidth=0.2, relheight=0.08)
#Methode 
def winrateLabels(team1, team2):
   stats = get_win_ratio(Ubersetzer(team1),Ubersetzer(team2),clicked_day_Start,clicked_season_Start,clicked_day_End,clicked_season_End)

   #algo1.get_win_ratio(Ubersetzer(team1),Ubersetzer(team2))
   # Winrate
   pWH = tk.Label(frame, text=stats[0], bg='gray13',fg='white') #Übersetzer für team1 und team2
   pWH.place(relx=0.20,rely=0.9, relwidth=0.2, relheight=0.04)
   # Drawrate
   pDraw = tk.Label(frame, text=stats[1], bg='gray13',fg='white')
   pDraw.place(relx=0.40,rely=0.9, relwidth=0.2, relheight=0.04)
   # Loserate
   pWA = tk.Label(frame, text=stats[2], bg='gray13',fg='white')
   pWA.place(relx=0.6,rely=0.9, relwidth=0.2, relheight=0.04)


#Labels
winHome = tk.Label(frame, text="Win Home", bg='gray13',fg='white')
winHome.place(relx=0.20,rely=0.85, relwidth=0.2, relheight=0.04)
pWH = tk.Label(frame, text="PercentWH", bg='gray13',fg='white') #Übersetzer für team1 und team2
pWH.place(relx=0.20,rely=0.9, relwidth=0.2, relheight=0.04)
draw = tk.Label(frame, text="Draw",bg='gray13',fg='white')
draw.place(relx=0.45,rely=0.85, relwidth=0.1, relheight=0.04)
pDraw = tk.Label(frame, text="PercentDRAW", bg='gray13',fg='white')
pDraw.place(relx=0.40,rely=0.9, relwidth=0.2, relheight=0.04)

winAway = tk.Label(frame, text="Win Away", bg='gray13',fg='white')
winAway.place(relx=0.63,rely=0.85, relwidth=0.14, relheight=0.04)
pWA = tk.Label(frame, text="PercentWA", bg='gray13',fg='white')
pWA.place(relx=0.6,rely=0.9, relwidth=0.2, relheight=0.04)

#currentSeason = tk.Label(frame, text="Include Current Season", bg='cornflowerblue', fg='white')
#currentSeason.place(relx=0.4,rely=0.165, relwidth=0.3, relheight=0.03)
punkt1 = tk.Label(frame, text="Oberer Schwarzer Punkt", bg='gray13', fg='gray13')
punkt1.place(relx=0.5,rely=0.60, relwidth=0.02, relheight=0.02)
punkt2 = tk.Label(frame, text="Unterer Schwarzer Punkt", bg='gray13', fg='gray13')
punkt2.place(relx=0.5,rely=0.63, relwidth=0.02, relheight=0.02)

def show():  
      createLabel()
  
def createLabel():
   myLable = Label(root, text=clicked1.get())
   myLable.place(relx=0.42,rely=0.95)
#Lists with all seasons
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
#reversed list with all seasons
seasons_End = seasons_Start[::-1]

#List with all match days 
matchdays_Start = []
for i in range(0, 34):
   matchdays_Start.append(i+1)

#reversed list with all match days
matchdays_End = matchdays_Start[::-1]

clicked_season_Start = StringVar()  
clicked_season_Start.set(seasons_Start[0])
season_start_menu = OptionMenu(root, clicked_season_Start, *seasons_Start)
season_start_menu.place(relx=0.05,rely=0.12)

clicked_season_End = StringVar()  
clicked_season_End.set(seasons_End[0])
season_end_menu = OptionMenu(root, clicked_season_End, *seasons_End)
season_end_menu.place(relx=0.58,rely=0.12)

clicked_day_Start = StringVar()  
clicked_day_Start.set(matchdays_Start[0])
matchdays_start_menu = OptionMenu(root, clicked_day_Start, *matchdays_Start)
matchdays_start_menu.place(relx=0.28,rely=0.12)

clicked_day_End = StringVar()  
clicked_day_End.set(matchdays_End[0])
matchdays_end_menu = OptionMenu(root, clicked_day_End, *matchdays_End)
matchdays_end_menu.place(relx=0.8,rely=0.12)

untilLabel = tk.Label(frame, text="until",bg='gray13',fg='white')
untilLabel.place(relx=0.46,rely=0.14, relwidth=0.06, relheight=0.03)

selector = tk.Button(root, text="Choose", fg="white", bg='brown4', command=lambda: show())
selector.place(relx=0.0,rely=0.00, relwidth=1, relheight=0.1) #choose button
#selector.place(relx=0.4,rely=0.45, relwidth=0.2, relheight=0.08)


root.mainloop()