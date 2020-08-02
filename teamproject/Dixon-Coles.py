import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import poisson, skellam
from scipy.optimize import minimize

# importing the tools required for the Poisson regression model
import statsmodels.api as sm
import statsmodels.formula.api as smf


class dc_class():
    filename = pd.read_csv("teamproject/BundesligaData.csv", encoding='unicode_escape')
    filename['Date'] = filename['Date'].str.replace("T", " ")
    filename['Date'] = pd.to_datetime(filename['Date'], format='%Y-%m-%d %H:%M:%S')
    filename['time_diff'] = (max(filename['Date']) - filename['Date']).dt.days
    filename = filename[['HomeTeam', 'AwayTeam', 'HomeGoals', 'AwayGoals', 'win', 'time_diff']]
    filename.head()

    goal_model_data = pd.concat([filename[['HomeTeam', 'AwayTeam', 'HomeGoals']].assign(home=1).rename(
        columns={'HomeTeam': 'team', 'AwayTeam': 'opponent', 'HomeGoals': 'goals'}),
        filename[['AwayTeam', 'HomeTeam', 'AwayGoals']].assign(home=0).rename(
            columns={'AwayTeam': 'team', 'HomeTeam': 'opponent', 'AwayGoals': 'goals'})])

    poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=goal_model_data,
                            family=sm.families.Poisson()).fit()


    """average difference between actual and model predicted scorelines"""
    def poiss_actual_diff(self, filename, max_goals):
        team_pred = [[poisson.pmf(i, team_avg) for i in range(0, max_goals)] \
                     for team_avg in [filename['HomeGoals'].mean(), filename['AwayGoals'].mean()]]
        return np.outer(np.array(team_pred[0]), np.array(team_pred[1])) - \
               np.array([sum((filename['HomeGoals'] == i) & (filename['AwayGoals'] == j))
                         for i in range(max_goals) for j in range(max_goals)]).reshape((6, 6)) / len(filename)


    """correction for low scoring draws"""
    def rho_correction(self, x, y, lambda_x, mu_y, rho):
        if x == 0 and y == 0:
            return 1 - (lambda_x * mu_y * rho)
        elif x == 0 and y == 1:
            return 1 + (lambda_x * rho)
        elif x == 1 and y == 0:
            return 1 + (mu_y * rho)
        elif x == 1 and y == 1:
            return 1 - rho
        else:
            return 1.0


    """finding coefficients that maximise the log-likelihood function"""

    def solve_parameters_decay(self, dataset, xi=0.001, debug=False, init_vals=None, options={'disp': True, 'maxiter': 100},
                               constraints=[{'type': 'eq', 'fun': lambda x: sum(x[:20]) - 20}], **kwargs):
        teams = np.sort(dataset['HomeTeam'].unique())
        away_teams = np.sort(dataset['AwayTeam'].unique())
        if not np.array_equal(teams, away_teams):
            raise ValueError("something not right")
        n_teams = len(teams)
        if init_vals is None:
            init_vals = np.concatenate((np.random.uniform(0, 1, (n_teams)),
                                        np.random.uniform(0, -1, (n_teams)),
                                        np.array([0, 1.0])
                                        ))

        def dc_log_like_decay(x, y, alpha_x, beta_x, alpha_y, beta_y, rho, gamma, t, xi=xi):
            lambda_x, mu_y = np.exp(alpha_x + beta_y + gamma), np.exp(alpha_y + beta_x)
            return np.exp(-xi * t) * (np.log(self.rho_correction(x, y, lambda_x, mu_y, rho)) +
                                      np.log(poisson.pmf(x, lambda_x)) + np.log(poisson.pmf(y, mu_y)))


        def estimate_paramters(params):
            score_coefs = dict(zip(teams, params[:n_teams]))
            defend_coefs = dict(zip(teams, params[n_teams:(2*n_teams)]))
            rho, gamma = params[-2:]
            log_like = [dc_log_like_decay(row.HomeGoals, row.AwayGoals, score_coefs[row.HomeTeam], defend_coefs[row.HomeTeam],
                                      score_coefs[row.AwayTeam], defend_coefs[row.AwayTeam],
                                      rho, gamma, row.time_diff, xi=xi) for row in dataset.itertuples()]
            return -sum(log_like)
        opt_output = minimize(estimate_paramters, init_vals, options=options, constraints = constraints)
        if debug:
            return opt_output
        else:
            return dict(zip(["attack_"+team for team in teams] +
                        ["defence_"+team for team in teams] +
                        ['rho', 'home_adv'],
                        opt_output.x))

    #params_xi = solve_parameters_decay(filename)

    #params_xi

    """Now we greate match score matrices"""

    def calc_means(self, param_dict, homeTeam, awayTeam):
        return [np.exp(param_dict['attack_' + homeTeam] + param_dict['defence_' + awayTeam] + param_dict['home_adv']),
                np.exp(param_dict['defence_' + homeTeam] + param_dict['attack_' + awayTeam])]

    def dixon_coles_simulate_match(self, params_dict, homeTeam, awayTeam, max_goals=10):
        team_avgs = self.calc_means(params_dict, homeTeam, awayTeam)
        team_pred = [[poisson.pmf(i, team_avg) for i in range(0, max_goals + 1)] for team_avg in team_avgs]
        output_matrix = np.outer(np.array(team_pred[0]), np.array(team_pred[1]))
        correction_matrix = np.array([[self.rho_correction(home_goals, away_goals, team_avgs[0],
                                                      team_avgs[1], self.params['rho']) for away_goals in range(2)]
                                      for home_goals in range(2)])
        output_matrix[:2, :2] = output_matrix[:2, :2] * correction_matrix
        return output_matrix