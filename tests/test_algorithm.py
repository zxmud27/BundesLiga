from teamproject.algorithm import *
import numpy as np

def test_bayvsBVB():
 win= 8
 draw= 4
 lose= 6
 all = win + draw + lose

 my_win_ratio = round(win/all * 100,4) 
 my_draw_ratio = round(draw/all * 100,4)
 my_lose_ratio = round(lose/all * 100,4)

 match = algo('FC Bayern', "Borussia Dortmund", 1, 2009, 34, 2018)
 my_result = match.get_win_ratio()
 result = [my_win_ratio, my_draw_ratio, my_lose_ratio]

 assert np.array_equal(my_result, result)
