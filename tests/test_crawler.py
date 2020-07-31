import teamproject.crawler 
import numpy as np
import csv

def test_games_played():
    
    # in one match year are 34 match games
    match_year_days = 34
    # one match day contain 9 games 
    match_day = 9
    # all games in one year
    all_games_in_a_year = match_year_days * match_day + 1
    
    match_crawl = teamproject.crawler.DataCrawler()
    match_crawl.getSeasons(1,2012,34,2012)

    with open("teamproject/BundesligaData.csv","r") as f:
        reader = csv.reader(f,delimiter = ",")
        data = list(reader)
        row_count = len(data)

    assert row_count == all_games_in_a_year

def test_games_played_two():
    
    # in one match year are 34 match games
    match_year_days = 22
    # one match day contain 9 games 
    match_day = 9
    # all games in one year
    all_games_in_a_year = match_year_days * match_day + 1
    
    match_crawl = teamproject.crawler.DataCrawler()
    match_crawl.getSeasons(1,2012,22,2012)

    with open("teamproject/BundesligaData.csv","r") as f:
        reader = csv.reader(f,delimiter = ",")
        data = list(reader)
        row_count = len(data)

    assert row_count == all_games_in_a_year


def test_games_played_three():
    
    # in one match year are 34 match games
    match_year_days = 20
    # one match day contain 9 games 
    match_day = 9
    # all games in one year
    all_games_in_a_year = match_year_days * match_day + 1
    
    match_crawl = teamproject.crawler.DataCrawler()
    match_crawl.getSeasons(3,2013,22,2013)

    with open("teamproject/BundesligaData.csv","r") as f:
        reader = csv.reader(f,delimiter = ",")
        data = list(reader)
        row_count = len(data)

    #assert row_count == all_games_in_a_year

test_games_played_three()