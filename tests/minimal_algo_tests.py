from teamproject.minimal_algorithm import * 
import teamproject.crawler 
import numpy as np


def test_bayvsBVB():
    win= 8
    draw= 3
    lose= 5
    all = win + draw + lose

    my_win_ratio = round(win/all * 100,4) 
    my_draw_ratio = round(draw/all * 100,4)
    my_lose_ratio = round(lose/all * 100,4)

    match_crawl = teamproject.crawler.DataCrawler()
    match_crawl.getSeasons(1,2011,34,2018)

    match =  teamproject.minimal_algorithm.minimal_class()
    my_result = match.get_minimal_probabilities('FC Bayern', "Borussia Dortmund")
    result = [my_win_ratio, my_draw_ratio, my_lose_ratio]

    assert np.array_equal(my_result, result)

def test_bremvsFCK():
    win= 1
    draw=1
    lose=0
    all = win + draw + lose

    my_win_ratio = round(win/all * 100,4) 
    my_draw_ratio = round(draw/all * 100,4)
    my_lose_ratio = round(lose/all * 100,4)

    match_crawl = teamproject.crawler.DataCrawler()
    match_crawl.getSeasons(1,2011,34,2018)

    match =  teamproject.minimal_algorithm.minimal_class()
    my_result = match.get_minimal_probabilities('Werder Bremen', "1. FC Kaiserslautern")
    result = [my_win_ratio, my_draw_ratio, my_lose_ratio]

    assert np.array_equal(my_result, result)

def test_StuttvsSChalk():
    win= 4
    draw=4
    lose=4
    all = win + draw + lose
    
    my_win_ratio = round(win/all * 100,4) 
    my_draw_ratio = round(draw/all * 100,4)
    my_lose_ratio = round(lose/all * 100,4)
   
        
    match_crawl = teamproject.crawler.DataCrawler()
    match_crawl.getSeasons(1,2013,34,2020)

    match =  teamproject.minimal_algorithm.minimal_class()
    my_result = match.get_minimal_probabilities('SC Freiburg', "FC Schalke 04")
    result = [my_win_ratio, my_draw_ratio, my_lose_ratio]

    assert np.array_equal(my_result, result)


