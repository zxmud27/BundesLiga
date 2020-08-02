import tkinter as tk
import teamproject.crawler
import teamproject.minimal_algorithm
import teamproject.poisson_algorithm

class GUI:
    global buttoncolor
    global backgroundcolor
    global fontcolor
    global mode

    def __init__(self, master,mode):
        self.mode = mode
        self.master = master
        master.title("Bundesliga Vorhersage")
        
        master.geometry("1200x600")
        #lightmode
        if(self.mode == 1):
            self.buttoncolor= "gray38"
            self.backgroundcolor="white"
            self.fontcolor="black"
            
        #darkmode  
        elif(self.mode == 0):
            self.buttoncolor= "brown4"
            self.backgroundcolor= "black"
            self.fontcolor= "white"
            
        master.config(bg=self.backgroundcolor)

        
        #Labels for the next upcoming matchday
       
        nextMatchDay = tk.Label(master,text="Next matchday", bg=self.backgroundcolor,fg=self.fontcolor,font='bold')
        nextMatchDay.place(relx=0.75,rely=0.18)
        matchdayTeam1 = tk.Label(master,text="Team 1", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        matchdayTeam1.place(relx=0.73,rely=0.25)
        firstMatchVs = tk.Label(master,text="V.S.", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        firstMatchVs.place(relx=0.79,rely=0.25)
        matchdayTeam2 = tk.Label(master,text="Team 2", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        matchdayTeam2.place(relx=0.83,rely=0.25)
        matchdayTeam3 = tk.Label(master,text="Team 3", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        matchdayTeam3.place(relx=0.73,rely=0.3)
        secondMatchVs = tk.Label(master,text="V.S.", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        secondMatchVs.place(relx=0.79,rely=0.3)
        matchdayTeam4 = tk.Label(master,text="Team 4", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        matchdayTeam4.place(relx=0.83,rely=0.3)
        matchdayTeam5 = tk.Label(master,text="Team 5", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        matchdayTeam5.place(relx=0.73,rely=0.35)
        thirdMatchVs = tk.Label(master,text="V.S.", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        thirdMatchVs.place(relx=0.79,rely=0.35)
        matchdayTeam6 = tk.Label(master,text="Team 6", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        matchdayTeam6.place(relx=0.83,rely=0.35)
        matchdayTeam7 = tk.Label(master,text="Team 7", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        matchdayTeam7.place(relx=0.73,rely=0.4)
        fourthMatchVs = tk.Label(master,text="V.S.", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        fourthMatchVs.place(relx=0.79,rely=0.4)
        matchdayTeam8 = tk.Label(master,text="Team 8", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        matchdayTeam8.place(relx=0.83,rely=0.4)
        matchdayTeam9 = tk.Label(master,text="Team 9", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        matchdayTeam9.place(relx=0.73,rely=0.45)
        fifthMatchVs = tk.Label(master,text="V.S.", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        fifthMatchVs.place(relx=0.79,rely=0.45)
        matchdayTeam10 = tk.Label(master,text="Team 10", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        matchdayTeam10.place(relx=0.83,rely=0.45)
        matchdayTeam11 = tk.Label(master,text="Team 11", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        matchdayTeam11.place(relx=0.73,rely=0.5)
        sixthMatchVs = tk.Label(master,text="V.S.", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        sixthMatchVs.place(relx=0.79,rely=0.5)
        matchdayTeam12 = tk.Label(master,text="Team 12", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        matchdayTeam12.place(relx=0.83,rely=0.5)
        matchdayTeam13 = tk.Label(master,text="Team 13", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        matchdayTeam13.place(relx=0.73,rely=0.55)
        seventhMatchVs = tk.Label(master,text="V.S.", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        seventhMatchVs.place(relx=0.79,rely=0.55)
        matchdayTeam14 = tk.Label(master,text="Team 14", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        matchdayTeam14.place(relx=0.83,rely=0.55)
        matchdayTeam15 = tk.Label(master,text="Team 15", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        matchdayTeam15.place(relx=0.73,rely=0.6)
        eightMatchVs = tk.Label(master,text="V.S.", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        eightMatchVs.place(relx=0.79,rely=0.6)
        matchdayTeam16 = tk.Label(master,text="Team 16", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        matchdayTeam16.place(relx=0.83,rely=0.6)
        matchdayTeam17 = tk.Label(master,text="Team 17", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        matchdayTeam17.place(relx=0.73,rely=0.65)
        ninthMatchVs = tk.Label(master,text="V.S.", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        ninthMatchVs.place(relx=0.79,rely=0.65)
        matchdayTeam18 = tk.Label(master,text="Team 18", bg=self.backgroundcolor,fg=self.fontcolor, font='bold') 
        matchdayTeam18.place(relx=0.83,rely=0.65)

        #labes for the win/lose/draw percentages
        winHome = tk.Label(master, text="Win Home:", bg=self.backgroundcolor, fg=self.fontcolor,height=3,width=8)
        winHome.place(relx=0.1, rely=0.6)
        pWH = tk.Label(master, text="%", bg=self.backgroundcolor, fg=self.fontcolor,height=3,width=8) 
        pWH.place(relx=0.1, rely=0.65)
        draw = tk.Label(master, text="Draw:", bg=self.backgroundcolor, fg=self.fontcolor,height=3,width=8)
        draw.place(relx=0.25, rely=0.6)
        pDraw = tk.Label(master, text="%", bg=self.backgroundcolor, fg=self.fontcolor,height=3,width=8)
        pDraw.place(relx=0.25, rely=0.65)
        winAway = tk.Label(master, text="Win Away:", bg=self.backgroundcolor, fg=self.fontcolor,height=3,width=8)
        winAway.place(relx=0.4, rely=0.6)
        pWA = tk.Label(master, text="%", bg=self.backgroundcolor, fg=self.fontcolor,height=3,width=8)
        pWA.place(relx=0.4, rely=0.65)

        #Label for the season input field 
        self.searched = tk.StringVar()
        selectionofseasonText = tk.Label(master,text="Season selection", bg=self.backgroundcolor, fg=self.fontcolor )
        selectionofseasonText.place(relx=0.8,rely=0.01,relwidth=0.2,relheight=0.015)
        selectionofseason= tk.Entry(master, textvariable=self.searched)
        selectionofseason.place(relx=0.87,rely=0.03,relwidth=0.061)

        #vs Label between 2 teams
        vsLabel = tk.Label(
            master,
            text="V.S.",
            bg=self.backgroundcolor,
            fg=self.fontcolor, width=3, height=1, font='bold')
        vsLabel.place(relx=0.26, rely=0.27)
        untilLabel = tk.Label(master, text="until", bg=self.backgroundcolor, fg=self.fontcolor,height=2,width=3, font='bold')
        untilLabel.place(relx=0.33, rely=0.009)

        """dropdown lists for selecting seasons and matchdays for the crawler

        """

        #list with all seasons
        seasons_Start = [
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
        seasons_End = seasons_Start[::1]

        # List with all match days
        matchdays_Start = []
        for i in range(0, 34):
            matchdays_Start.append(i+1)

        # reversed list with all match days
        matchdays_End = matchdays_Start[::-1]

        self.clicked_day_Start = tk.StringVar()
        self.clicked_day_Start.set(matchdays_Start[0])
        matchdays_start_menu = tk.OptionMenu(master, self.clicked_day_Start, *matchdays_Start,)
        matchdays_start_menu.place(relx=0.2, rely=0.015)

        self.clicked_season_Start = tk.StringVar()
        self.clicked_season_Start.set(seasons_Start[0])
        season_start_menu = tk.OptionMenu(master, self.clicked_season_Start, *seasons_Start)
        season_start_menu.place(relx=0.25, rely=0.015)

        self.clicked_day_End = tk.StringVar()
        self.clicked_day_End.set(matchdays_End[0])
        matchdays_end_menu = tk.OptionMenu(root, self.clicked_day_End, *matchdays_End)
        matchdays_end_menu.place(relx=0.38, rely=0.015)

        self.clicked_season_End = tk.StringVar()
        self.clicked_season_End.set(seasons_End[-1])
        season_end_menu = tk.OptionMenu(root, self.clicked_season_End,*seasons_End)
        season_end_menu.place(relx=0.43, rely=0.015)



        """
        dropdown list for selecting the league for the crawler
        """
        #list with all leagues
        liga_dropdown = [
        "1. Bundesliga",
        "2. Bundesliga",
        "3. Bundesliga",
        "1. Handball Bundesliga"
        ]

        self.click_liga_dropdown = tk.StringVar()
        self.click_liga_dropdown.set(liga_dropdown[0])
        liga_menu = tk.OptionMenu(master, self.click_liga_dropdown, *liga_dropdown)
        liga_menu.place(relx=0.6, rely=0.015)

        #Lists which get filled with teams by the crawler
        
        

        #dropdown lists for selecting the teams
        

        #list with all algorithms
        algo_dropdown=[
        "Minimal Algorithm   ",
        "Poisson Algorithm    "
        ]

        #dropdown list for selecting an algorithm
        self.click_algo_dropdown = tk.StringVar()
        self.click_algo_dropdown.set("Choose an algorithm")
        algo_menu = tk.OptionMenu(master, self.click_algo_dropdown, *algo_dropdown)
        algo_menu.place(relx=0.21, rely=0.4)   

        #dropdown list for choosing the algorithm
        #click_registryPatterninput_dropdown = tk.StringVar()
        #click_registryPatterninput_dropdown.set("Choose an algorithm")
        #algo_menu = tk.OptionMenu(master, click_registryPatterninput_dropdown, *registryPatterninput)
        #algo_menu.place(relx=0.01, rely=0.3)

        #button for starting the crawler
        CrawlerButton = tk.Button(
            master,
            text="Start Crawler",
            width=25,
            height=2,
            fg=self.fontcolor,
            bg=self.buttoncolor,
            command = lambda: self.crawler_load())
        CrawlerButton.place(relx=0.20, rely=0.15)

        #Button for starting the prediction
        startButton = tk.Button(
            master,
            text="Start prediction",
            width=25,
            height=2,
            fg=self.fontcolor,
            bg=self.buttoncolor,
            command = lambda: self.algorithm_load())
        startButton.place(relx=0.202, rely=0.5)

        changeModeButton = tk.Button(master, text="Change Mode", width=20, height=2, fg=self.fontcolor, bg=self.buttoncolor,command=lambda: self.changemode())
        changeModeButton.place(relx=0.01, rely=0.01)

        
        #Methode außerhalb vom Konstruktor
        

        # Die jeweiligen Buttons mit der Variable buttoncolor, backgroundcolor und fontcolor ersetzen. Über die Farben kann man noch sprechen


    def changemode(self):
        if(self.mode == 0) :
            GUI(root,1)
        elif(self.mode == 1):
            GUI(root,0)

        
        


    def algorithm_load(self):
        if self.click_algo_dropdown.get() == "Minimal Algorithm   ":
            algo_m = teamproject.minimal_algorithm.minimal_class()
            stats = algo_m.get_minimal_probabilities(self.click_teams1_dropdown.get(),self.click_teams2_dropdown.get())
            pWH = tk.Label(self.master, text=str(stats[0]) + "%", bg=self.backgroundcolor, fg=self.fontcolor,height=3,width=8) 
            pWH.place(relx=0.1, rely=0.65)
            pDraw = tk.Label(self.master, text=str(stats[1]) + "%", bg=self.backgroundcolor, fg=self.fontcolor,height=3,width=8)
            pDraw.place(relx=0.25, rely=0.65)
            pWA = tk.Label(self.master, text=str(stats[2]) + "%", bg=self.backgroundcolor, fg=self.fontcolor,height=3,width=8)
            pWA.place(relx=0.4, rely=0.65)
        elif self.click_algo_dropdown.get() == "Poisson Algorithm    ":
            algo_p = teamproject.poisson_algorithm.poisson_class()
            stats = algo_p.get_probabilities(self.click_teams1_dropdown.get(),self.click_teams2_dropdown.get())
            pWH = tk.Label(self.master, text=str(stats[0]) + "%", bg=self.backgroundcolor, fg=self.fontcolor,height=3,width=8) 
            pWH.place(relx=0.1, rely=0.65)
            pDraw = tk.Label(self.master, text=str(stats[1]) + "%", bg=self.backgroundcolor, fg=self.fontcolor,height=3,width=8)
            pDraw.place(relx=0.25, rely=0.65)
            pWA = tk.Label(self.master, text=str(stats[2]) + "%", bg=self.backgroundcolor, fg=self.fontcolor,height=3,width=8)
            pWA.place(relx=0.4, rely=0.65)


        """

        starts the crawler and creates dropdown menu for selecting the teams

        -----------
        Parameters:
        -----------


        -------
        Return:
        -------
        match history in the given time period
        crawled teams in dropdownmenus
        
        """
    def crawler_load(self):
        teams1_list = []
        teams2_list = []
        teams1_list = teamproject.crawler.DataCrawler().getNamelist(int(self.searched.get()),self.click_liga_dropdown.get())
        teams2_list = teamproject.crawler.DataCrawler().getNamelist(int(self.searched.get()),self.click_liga_dropdown.get())
        self.click_teams1_dropdown = tk.StringVar()
        self.click_teams1_dropdown.set(teams1_list[0])
        team1_menu = tk.OptionMenu(self.master, self.click_teams1_dropdown, *teams1_list)
        team1_menu.place(relx=0.12, rely=0.265)
        self.click_teams2_dropdown = tk.StringVar()
        self.click_teams2_dropdown.set(teams2_list[1])

        team2_menu = tk.OptionMenu(self.master, self.click_teams2_dropdown, *teams2_list)
        team2_menu.place(relx=0.315, rely=0.265)
        crawler_class = teamproject.crawler.DataCrawler()
        crawler_class.getSeasons(int(self.clicked_day_Start.get()),
                                                int(self.clicked_season_Start.get()), 
                                                int(self.clicked_day_End.get()), 
                                                int(self.clicked_season_End.get()), 
                                                self.click_liga_dropdown.get())
    
        
root = tk.Tk()
GUI(root,0)
root.mainloop()        




