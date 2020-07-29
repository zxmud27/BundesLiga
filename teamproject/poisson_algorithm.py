import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson,skellam

# importing the tools required for the Poisson regression model
import statsmodels.api as sm
import statsmodels.formula.api as smf

class poisson_class():

    #def __init__(self, HomeTeam):
        #self.HomeTeam = HomeTeam
        #self.AwayTeam = AwayTeam

    filename = pd.read_csv("BundesligaData.csv",encoding='unicode_escape')
    filename.head()
    goal_model_data =  pd.concat([filename[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(
                    columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}),
                   filename[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(
                    columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'})])
                    
    poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=goal_model_data, 
                                family=sm.families.Poisson()).fit()

    def simulate_match(self, foot_model, homeTeam, awayTeam, max_goals=10):
        home_goals_avg = foot_model.predict(pd.DataFrame(data={'team': homeTeam, 
                                                                'opponent': awayTeam,'home':1},
                                                          index=[1])).values[0]
        away_goals_avg = foot_model.predict(pd.DataFrame(data={'team': awayTeam, 
                                                                'opponent': homeTeam,'home':0},
                                                          index=[1])).values[0]
        team_pred = [[poisson.pmf(i, team_avg) for i in range(0, max_goals+1)] for team_avg in [home_goals_avg, away_goals_avg]]
        return(np.outer(np.array(team_pred[0]), np.array(team_pred[1])))

    def get_probabilities(self, team1,team2):
        teams_goal_prob_matrix = self.simulate_match(
            self.poisson_model,
            team1,
            team2,
            10)

        prob_win_home = np.sum(np.tril(teams_goal_prob_matrix, -1))

        prob_win_away = np.sum(np.triu(teams_goal_prob_matrix, 1))

        prob_draw = np.sum(np.diag(teams_goal_prob_matrix))
        
        return [prob_win_home,prob_win_away,prob_draw]

test = poisson_class()
print(test.get_probabilities("Hannover 96","Fortuna Düsseldorf"))