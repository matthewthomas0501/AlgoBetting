import subprocess
from pathlib import Path

from bs4 import BeautifulSoup
import requests
import selenium
import selenium.webdriver
from selenium.webdriver.common.by import By


options = selenium.webdriver.chrome.options.Options()
    
node_modules_bin = subprocess.run(
    ["npm", "bin"],
    stdout=subprocess.PIPE,
    universal_newlines=True,
    check=True
)
node_modules_bin_path = node_modules_bin.stdout.strip()
chromedriver_path = Path(node_modules_bin_path) / "chromedriver"

driver = selenium.webdriver.Chrome(
    options=options,
    executable_path=str(chromedriver_path),
)

# An implicit wait tells WebDriver to poll the DOM for a certain amount of
# time when trying to find any element (or elements) not immediately
# available. Once set, the implicit wait lasts for the life of the
# WebDriver object.

driver.implicitly_wait(1)


driver.get("https://www.pro-football-reference.com/years/2022/games.htm")

# Find the search input box, which looks like this:
#   <input name="q" type="text">

# sortable stats_table now_sortable
input_element = driver.find_elements("xpath", "//table[@class='sortable stats_table now_sortable']")
# print(input_element[0].text)

data = input_element[0].text.split("\n")

CURRENT_WEEK = 16
long_names = {"Los","San","New","Las","Green","New","Tampa","Kansas"}
with open("football.csv","w") as csvFile:
    csvFile.write("Week,Day,Date,Time,Winner,@,Loser,Boxscore,PtsW,PtsL,YdsW,TOW,YdsL,TOL\n")
    for line in data:
        line = line.split(" ")
        
        if line[0] != "Week" and int(line[0]) < CURRENT_WEEK:
            
            if "@" in line:
                team_name = ""
                location = line.index("@")
                remove = []
                for i in range(4,location):
                    team_name+=line[i]
                    team_name+=" "
                    remove.append(line[i])
                
                for i in remove:
                    # print("removed this ",i)
                    line.remove(i)
                
                team_name = team_name[:-1]
                line.insert(4,team_name)

                location = line.index("boxscore")
                team_name = ""
                remove = []
                for i in range(6,location):
                    team_name+=line[i]
                    team_name+=" "
                    remove.append(line[i])
                
                for i in remove:
                    # print("removed this ",i)
                    line.remove(i)

                team_name = team_name[:-1]
                line.insert(6,team_name)
                # print("HAS @")
            else:
                # print("no lol \n")
                if line[4] in long_names:
                    line.insert(7,"<")
                else:
                    line.insert(6,"<")

                team_name = ""
                location = line.index("<")
                remove = []
                for i in range(4,location):
                    team_name+=line[i]
                    team_name+=" "
                    remove.append(line[i])
                
                for i in remove:
                    # print("removed this ",i)
                    line.remove(i)
                
                team_name = team_name[:-1]
                line.insert(4,team_name)

                location = line.index("boxscore")
                team_name = ""
                remove = []
                for i in range(6,location):
                    team_name+=line[i]
                    team_name+=" "
                    remove.append(line[i])
                
                for i in remove:
                    # print("removed this ",i)
                    line.remove(i)

                team_name = team_name[:-1]
                line.insert(6,team_name)

            print(line)
            counter = 0
            for temp in line:
                if counter == 13:
                    csvFile.write(temp)
                else:
                    temp += ","
                    csvFile.write(temp)
                counter+=1
                
            csvFile.write("\n")
        


driver.quit()