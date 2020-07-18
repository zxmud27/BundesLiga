from Algorithmus import *
import numpy as np
def test_bayvsBVB():
 win= 10
 tie= 4
 lose= 6
 all = win + tie + lose
 
 my_result = Algorithmus.get_win_ratio('FC Bayern', "Borussia Dortmund", 1, 2009, 34, 2019)
 result = [win/all, tie/all, lose/all]
 assert np.array_equal(my_result, result)
