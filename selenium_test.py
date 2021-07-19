from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import youtube_dl

import pandas as pd

class SeleniumTest:

    def __init__(self):
        self.ydl = youtube_dl.YoutubeDL()

        self.run()
        pass

    def run(self):
        DRIVER_PATH = '/usr/bin/chromedriver'
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        driver.get('https://www.youtube.com/results?search_query=noteblock')
        web_elems = driver.find_elements_by_id("thumbnail")
        for elem in web_elems:
            url = elem.get_property("href")
            info_dict = self.ydl.extract_info(url, download=False)
            print(info_dict.get("title",None))
            pass


if __name__ == "__main__":
    sel = SeleniumTest()