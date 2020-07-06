from Algorithmus import *

def test_bayvsBVB():
 win= 10
 tie= 4
 lose= 6
 all = win + tie + lose
 
 my_result = Algorithmus.get_win_ratio('FC Bayern', "Borussia Dortmund", 1, 2009, 34, 2019)
 result = [win/all, tie/all, lose/all]
 
 for i in result:
     assert result[i] == my_result[i]
