from teamproject.crawler import CRAWLER
from teamproject.algorithm import algo
from tkinter import *
class Team:

    def __init__(self, name, image, nummer):
        self.name=name
        self.image= PhotoImage(Image)
        self.nummer=nummer

    def getName(self):
        return self.name

    def getNummer(self):
        return self.nummer

    def getImage(self):
        return self.image

    def setLiga(self, arraywithteams, bilder, id):
        teamarray = [ ]
        for i in arraywithteams:
            teamarray.append(Team.__init__(self, crawler.getArrayTeamname[i],crawler.getArrayImages[i],i))
