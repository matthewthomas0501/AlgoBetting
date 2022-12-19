
"""Perform a Google search using Selenium and a headless Chrome browser."""
import subprocess
from pathlib import Path

from bs4 import BeautifulSoup
import requests
import selenium
import selenium.webdriver
from selenium.webdriver.common.by import By



def test_selenium_hello():
    """Perform a Google search using Selenium and a headless Chrome browser."""






    #Need to do this for the first one because the div class for the second one
    #Has a break line and is not the same name
    url="https://sportsbook.draftkings.com/leagues/football/nfl"

    url_nfl = "https://sportsbook.draftkings.com//sites/US-NJ-SB/api/v5/eventgroups/88808?format=json"
    url_cfp = "https://sportsbook.draftkings.com//sites/US-NJ-SB/api/v5/eventgroups/87637?format=json"
    url_nhl = "https://sportsbook.draftkings.com//sites/US-NJ-SB/api/v5/eventgroups/42133?format=json"
    
    req=requests.get(url_nfl).json()
    # print(req_nfl)
    req = req['eventGroup']['offerCategories'][0]['offerSubcategoryDescriptors'][0]['offerSubcategory']['offers']

    # print(req)
    away_team = "matt"
    home_team = "matt"
    #Getting odds data from draft kings api
    for i in req:
        
        if 'label' in i[0]['outcomes'][0]: #HAVE TO DO SPECIAL THINGS WHEN DRAFT KINGS SHUTS DOWN CERTAIN ODDS
            away_team = i[0]['outcomes'][0]['label']
            home_team = i[0]['outcomes'][1]['label']
        
        for j in range(len(i)):

            if j == 0:
                if 'line' in i[0]['outcomes'][0]:
                    print(f"Spread: {i[0]['outcomes'][0]['line']} for {away_team}")
                    print(f"Spread Odds: {i[0]['outcomes'][0]['oddsAmerican']}")
            if j == 1:
                if 'line' in i[1]['outcomes'][0]:
                    print(i[1]['outcomes'][0]['line'])
                    print(i[1]['outcomes'][0]['oddsAmerican'])
                    print("under")
                    print(i[1]['outcomes'][1]['line'])
                    print(i[1]['outcomes'][1]['oddsAmerican'])
            if j == 2:
                if 'oddsAmerican' in i[2]['outcomes'][0]:
                    away_team = i[2]['outcomes'][0]['label']
                    print(f"{away_team} Money Line: {i[2]['outcomes'][0]['oddsAmerican']}")

        
        print(home_team)
        for j in range(len(i)):

            if j == 0:
                if 'line' in i[0]['outcomes'][1]:
                    
                    print(f"Spread: {i[0]['outcomes'][1]['line']} for {home_team}")
                    print(f"Spread Odds: {i[0]['outcomes'][1]['oddsAmerican']}")
            if j == 2:
                if 'oddsAmerican' in i[2]['outcomes'][0]:
                    home_team = i[2]['outcomes'][1]['label']
                    print(f"{home_team} Money Line: {i[2]['outcomes'][1]['oddsAmerican']}")

        
        print("\n")
    


if __name__ == "__main__":
    test_selenium_hello()
