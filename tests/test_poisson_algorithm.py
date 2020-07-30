from teamproject.poisson_algorithm import * 
import teamproject.crawler 
import numpy as np

def test_bayvsBVB():

    match_crawl = teamproject.crawler.DataCrawler()
    match_crawl.getSeasons(1,2011,34,2018)

    match =  teamproject.poisson_algorithm.poisson_class()
    my_result = match.get_probabilities('FC Bayern', "Borussia Dortmund")
    result = [68.7925, 18.166, 13.0388]

    

def test_bremvsFCK():

    match_crawl = teamproject.crawler.DataCrawler()
    match_crawl.getSeasons(1,2011,34,2018)

    match =  teamproject.poisson_algorithm.poisson_class()
    my_result = match.get_probabilities('Werder Bremen', 'Borussia Mönchengladbach') 
    result = [34.0098, 24.1867, 41.8034]


def test_SCFvsS04():

    match_crawl = teamproject.crawler.DataCrawler()
    match_crawl.getSeasons(1,2013,34,2020)

    match =  teamproject.poisson_algorithm.poisson_class()
    my_result = match.get_probabilities('SC Freiburg', "FC Schalke 04")
    result = [34.7762, 26.6737, 38.5501]


