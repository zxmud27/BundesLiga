from teamproject.poisson_algorithm import * 
import teamproject.crawler 
import numpy as np

def test_bayvsBVB():

    match_crawl = teamproject.crawler.DataCrawler()
    match_crawl.getSeasons(1,2011,34,2018)

    match =  teamproject.poisson_algorithm.poisson_class()
    my_result = match.get_probabilities('FC Bayern', "Borussia Dortmund")
    result = [68.7925, 18.166, 13.0388]

    assert np.array_equal(my_result, result)

def test_bremvsFCK():

    match_crawl = teamproject.crawler.DataCrawler()
    match_crawl.getSeasons(1,2011,34,2018)

    match =  teamproject.poisson_algorithm.poisson_class()
    my_result = match.get_probabilities('Werder Bremen', '1. FC Kaiserslautern') 
    result = [61.4789, 23.0318, 15.4891]
    print(my_result)

    assert np.array_equal(my_result, result)

def test_SCFvsS04():

    match_crawl = teamproject.crawler.DataCrawler()
    match_crawl.getSeasons(1,2013,34,2020)

    match =  teamproject.poisson_algorithm.poisson_class()
    my_result = match.get_probabilities('SC Freiburg', "FC Schalke 04")
    result = [34.7762, 26.6737, 38.5501]
    print(my_result)

    assert np.array_equal(my_result, result)

test_SCFvsS04()
