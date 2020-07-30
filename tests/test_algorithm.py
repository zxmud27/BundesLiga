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

test_bayvsBVB()
