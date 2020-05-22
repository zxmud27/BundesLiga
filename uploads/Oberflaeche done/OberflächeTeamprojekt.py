from tkinter import *
import tkinter as tk
#Hello Tutorial
root = tk.Tk()
root.title("GUI")
canvas = tk.Canvas(root, height=400, width=400)
canvas.pack()
frame = tk.Frame(root, bg='cornflowerblue')
frame.place(relwidth=1, relheight=1)

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
koeln       = PhotoImage(file='koe.png')
herthaBSC   = PhotoImage(file='bsc.png')
unionBerlin    = PhotoImage(file='fcu.png')
eintrachtFrankfurt   = PhotoImage(file='sge.png')
augsburg = PhotoImage(file='fca.png')
mainz05  = PhotoImage(file='m05.png')
fortunaduesseldorf   = PhotoImage(file='f95.png')
werderBremen   = PhotoImage(file='svw.png')
paderborn07 = PhotoImage(file='scp.png')


def buttonupdate(buttonnummer, teamname):
   print("duspast")
   if(buttonnummer==1):
      erstesTeamButton = tk.Button(frame,image= teamname,width=10, height=10, fg="white", bg="royalblue",command=lambda: newframe(1))
      erstesTeamButton.place(relx=0.20,rely=0.52, relwidth=0.2, relheight=0.2) 
   else:
      zweitesTeamButton = tk.Button(frame,image= teamname,width=10, height=10, fg="white", bg="royalblue",command=lambda:newframe(2))
      zweitesTeamButton.place(relx=0.60,rely=0.52, relwidth=0.2, relheight=0.2)

def newframe(buttonnummer):
   newWindow = tk.Toplevel(root)
   canvas = tk.Canvas(newWindow, height=400, width=400)
   canvas.pack()
   frame2 = tk.Frame(newWindow, bg='cornflowerblue')
   frame2.place(relwidth=1, relheight=1)
   BM =  tk.Button(frame2,image=bayernMuenchen,text="FC Bayern München",width=200,height=100,bg="royalblue",command=lambda: buttonupdate(buttonnummer,bayernMuenchen))
   BM.place(relx=0.0,rely=0.0)
   koln =  tk.Button(frame2,image=koeln,text="FC Bayern München",width=200,height=100,bg="royalblue",command=lambda: buttonupdate(buttonnummer,koeln))
   koln.place(relx=0.5,rely=0.5)

erstesTeamButton = tk.Button(frame,image=dortmund,width=10, height=10, fg="white", bg="royalblue", command=lambda: newframe(1))
erstesTeamButton.place(relx=0.20,rely=0.52, relwidth=0.2, relheight=0.2)  


zweitesTeamButton = tk.Button(frame,image=wolfsburg,width=10, height=10, fg="white", bg="royalblue", command=lambda: newframe(2))
zweitesTeamButton.place(relx=0.60,rely=0.52, relwidth=0.2, relheight=0.2)

#Checkbox Inhalt ausgeben in Konsole über Button Befehl.
#buttonstatus = IntVar()
#IncludeSeasonButtonCheckBox = tk.Checkbutton(frame, text="Include current Season", bg="cornflowerblue", variable=buttonstatus)
#IncludeSeasonButtonCheckBox.deselect()
#IncludeSeasonButtonCheckBox.place(relx=0.35,rely=0.165, relwidth=0.4, relheight=0.03)
#def buttonclick():
#     print(buttonstatus.get())
#erstesTeamButton = tk.Button(frame, text="erstes Team",width=10, height=10, fg="white", bg="royalblue",command=buttonclick)
#erstesTeamButton.place(relx=0.20,rely=0.52, relwidth=0.2, relheight=0.2)
CrawlerButton = tk.Button(frame, text="Start Crawler",width=30, height=5, fg="white", bg="royalblue", padx=10, pady=5)
CrawlerButton.place(relx=0.06,rely=0.13, relwidth=0.2, relheight=0.1)

IncludeSeasonButtonCheckBox = tk.Checkbutton(frame, text="Include current Season", bg="cornflowerblue")
IncludeSeasonButtonCheckBox.place(relx=0.35,rely=0.165, relwidth=0.4, relheight=0.03)


predictButton = tk.Button(frame, text="Predict",width=10, height=10, fg="white", bg="royalblue")
predictButton.place(relx=0.4,rely=0.75, relwidth=0.2, relheight=0.08)

startTrain = tk.Button(frame, text="Start Training",width=10, height=10, fg="white", bg="royalblue")
startTrain.place(relx=0.4,rely=0.38, relwidth=0.2, relheight=0.08)
#Labels
winHome = tk.Label(frame, text="Win Home", bg='cornflowerblue')
winHome.place(relx=0.20,rely=0.85, relwidth=0.2, relheight=0.04)
pWH = tk.Label(frame, text="PercentWH", bg='cornflowerblue')
pWH.place(relx=0.20,rely=0.9, relwidth=0.2, relheight=0.04)

draw = tk.Label(frame, text="Draw", bg='cornflowerblue')
draw.place(relx=0.45,rely=0.85, relwidth=0.1, relheight=0.04)
pDraw = tk.Label(frame, text="PercentDRAW", bg='cornflowerblue')
pDraw.place(relx=0.40,rely=0.9, relwidth=0.2, relheight=0.04)

winAway = tk.Label(frame, text="Win Away", bg='cornflowerblue')
winAway.place(relx=0.63,rely=0.85, relwidth=0.14, relheight=0.04)
pWA = tk.Label(frame, text="PercentWA", bg='cornflowerblue')
pWA.place(relx=0.6,rely=0.9, relwidth=0.2, relheight=0.04)

#currentSeason = tk.Label(frame, text="Include Current Season", bg='cornflowerblue', fg='white')
#currentSeason.place(relx=0.4,rely=0.165, relwidth=0.3, relheight=0.03)
punkt1 = tk.Label(frame, text="Oberer Schwarzer Punkt", bg="black", fg="black")
punkt1.place(relx=0.5,rely=0.60, relwidth=0.02, relheight=0.02)
punkt2 = tk.Label(frame, text="Unterer Schwarzer Punkt", bg="black", fg="black")
punkt2.place(relx=0.5,rely=0.63, relwidth=0.02, relheight=0.02)


root.mainloop()
#Hello World
#class Application(tk.Frame):
 #   def __init__(self, master=None):
  #      super().__init__(master)
   #     self.master = master
    #    self.pack()
     #   self.create_widgets()
      #  self.winfo_width=200
       # self.winfo_height=200

#    def create_widgets(self):
 #       self.hi_there = tk.Button(self)
 #       self.hi_there["text"] = "Hello World\n(click me)"
  #      self.hi_there["command"] = self.say_hi
   #     self.hi_there.pack(side="top")
#
 #       self.quit = tk.Button(self, text="QUIT", fg="red",
  #                            command=self.master.destroy)
   #     self.quit.pack(side="bottom")
#
   #    self.button1 =tk.Button(self)
    #    self.button1["text"] = "Button 1\n(Klick mich nicht!)"
    #    self.button1["command"] = self.say_hi
    #    self.button1.pack(side="bottom")

 #   def say_hi(self):
  #      print("hi there, everyone!")
#
#root = tk.Tk()
#app = Application(master=root)
#app.mainloop()