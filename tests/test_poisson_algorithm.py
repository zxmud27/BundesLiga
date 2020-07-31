from teamproject.poisson_algorithm import * 
import teamproject.crawler 
import numpy as np

def test_bayvsBVB():

    match_crawl = teamproject.crawler.DataCrawler()
    match_crawl.getSeasons(1,2011,34,2018)

    match =  teamproject.poisson_algorithm.poisson_class()
    my_result = match.get_probabilities('FC Bayern', "Borussia Dortmund")
    result = [68.7, 17.7, 13.6]
    bool_result = True
    my_result[0] = np.float(my_result[0])
    my_result[1] = np.float(my_result[1])
    my_result[2] = np.float(my_result[2])
    for i in range(0,3):
        #print([result[i],my_result[i]])
        if not result[i] == my_result[i]:
            bool_result = False
    
    #print(bool_result)
    assert bool_result

def test_bremvsFCK():

    match_crawl = teamproject.crawler.DataCrawler()
    match_crawl.getSeasons(1,2011,34,2018)

    match =  teamproject.poisson_algorithm.poisson_class()
    my_result = match.get_probabilities('Werder Bremen', 'Borussia Mönchengladbach') 
    result = [31.4, 23.6, 45.1]
    my_result[0] = np.float(my_result[0])
    my_result[1] = np.float(my_result[1])
    my_result[2] = np.float(my_result[2])
    bool_result = True
    for i in range(0,3):
        #print([result[i],my_result[i]])
        if not result[i] == my_result[i]:
            bool_result = False
    #print(bool_result)
    assert bool_result

def test_SCFvsS04():

    match_crawl = teamproject.crawler.DataCrawler()
    match_crawl.getSeasons(1,2013,34,2020)

    match =  teamproject.poisson_algorithm.poisson_class()
    my_result = match.get_probabilities('SC Freiburg', "FC Schalke 04")
    my_result[0] = np.float(my_result[0])
    my_result[1] = np.float(my_result[1])
    my_result[2] = np.float(my_result[2])
    result = [34.8, 26.7, 38.6]
    bool_result = True
    for i in range(0,3):
        #print([result[i],my_result[i]])
        if not result[i] == my_result[i]:
            bool_result = False
    #print(bool_result)
    assert bool_result

    #pytestmy_result[0] = np.float(my_result[0])
    #pytestmy_result[1] = np.float(my_result[1])
    #pytestmy_result[2] = np.float(my_result[2])
    #pytestprint(type(my_result[0]))
    #pytestprint(type(my_result[1]))
    #pytestprint(type(my_result[2]))
    #pytestprint(type(result[0]))
    #pytestprint(type(result[1]))
    #pytestprint(type(result[2]))