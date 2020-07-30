from teamproject.minimal_algorithm import * 

import numpy as np

def test_bayvsBVB():
    win= 8
    draw= 4
    lose= 6
    all = win + draw + lose

    my_win_ratio = round(win/all * 100,4) 
    my_draw_ratio = round(draw/all * 100,4)
    my_lose_ratio = round(lose/all * 100,4)

    match =  teamproject.minimal_algorithm.minimal_class()
    my_result = match.get_minimal_probabilities('FC Bayern', "Borussia Dortmund")
    result = [my_win_ratio, my_draw_ratio, my_lose_ratio]

    assert np.array_equal(my_result, result)
