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

with open("football.csv","w") as csvFile:
    for line in data:
        line = line.split(" ")
        if line[0] != "Week":
            for temp in line:
                temp += " "
                csvFile.write(temp)
                
        csvFile.write("\n")


driver.quit()