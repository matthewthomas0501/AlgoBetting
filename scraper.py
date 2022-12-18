
"""Perform a Google search using Selenium and a headless Chrome browser."""
import subprocess
from pathlib import Path

import selenium
import selenium.webdriver
from selenium.webdriver.common.by import By


def test_selenium_hello():
    """Perform a Google search using Selenium and a headless Chrome browser."""

    # Configure Selenium
    #
    # Pro-tip: remove the "headless" option and set a breakpoint.  A Chrome
    # browser window will open, and you can play with it using the developer
    # console.
    options = selenium.webdriver.chrome.options.Options()
    #options.add_argument("--headless")

    # chromedriver is not in the PATH, so we need to provide selenium with
    # a full path to the executable.
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
    #
    # https://selenium-python.readthedocs.io/waits.html#implicit-waits
    driver.implicitly_wait(1)

    # Load Google search main page
    driver.get("https://www.actionnetwork.com/odds")


    
    input_element = driver.find_elements(by=By.XPATH, value="//div[@class='best-odds__game-info']")
    
    #input_element = driver.find_element("xpath", "//div[@class='best-odds__game-info']")
    
    for games in input_element:
        data = games.text.split("\n")
        if len(data) == 6:
            print(f"Game in Progress {data[0]} playing {data[3]}")
            team_1 = int(data[2])
            team_2 = int(data[5])
            if team_1 > team_2:
                print(f"{data[0]} winning {team_1} to {team_2}")
            else:
                print(f"{data[3]} winning {team_2} to {team_1}")
        print("\n")
        # print(data)
        
    
    

   
    driver.quit()


if __name__ == "__main__":
    test_selenium_hello()
