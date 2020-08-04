from teamproject.poisson_algorithm import * 
import teamproject.crawler 
import numpy as np

def test_bayvsBVB():

    match_crawl = teamproject.crawler.DataCrawler()
    match_crawl.getSeasons(1,2011,34,2018,"1. Bundesliga")

    match =  teamproject.poisson_algorithm.poisson_class()
    my_result = match.get_probabilities('FC Bayern', "Borussia Dortmund")
    result = [68.8, 18.2, 13.0]
    bool_result = True
    my_result[0] = np.float(my_result[0])
    my_result[1] = np.float(my_result[1])
    my_result[2] = np.float(my_result[2])
    for i in range(0,3):
        if not result[i] == my_result[i]:
            bool_result = False
    assert bool_result

def test_bremvsFCK():

    match_crawl = teamproject.crawler.DataCrawler()
    match_crawl.getSeasons(1,2011,34,2018,"1. Bundesliga")

    match =  teamproject.poisson_algorithm.poisson_class()
    my_result = match.get_probabilities('Werder Bremen', 'Borussia Mönchengladbach') 
    result = [34.0, 24.2, 41.8]
    my_result[0] = np.float(my_result[0])
    my_result[1] = np.float(my_result[1])
    my_result[2] = np.float(my_result[2])
    bool_result = True
    for i in range(0,3):
        if not result[i] == my_result[i]:
            bool_result = False
    assert bool_result

def test_SCFvsS04():

    match_crawl = teamproject.crawler.DataCrawler()
    match_crawl.getSeasons(1,2013,34,2020,"1. Bundesliga")

    match =  teamproject.poisson_algorithm.poisson_class()
    my_result = match.get_probabilities('SC Freiburg', "FC Schalke 04")
    my_result[0] = np.float(my_result[0])
    my_result[1] = np.float(my_result[1])
    my_result[2] = np.float(my_result[2])
    result = [34.8, 26.7, 38.6]
    bool_result = True
    for i in range(0,3):
        if not result[i] == my_result[i]:
            bool_result = False

    assert bool_result
