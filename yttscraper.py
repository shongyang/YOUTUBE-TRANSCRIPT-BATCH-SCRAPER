from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import re
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")
with open("links.txt", "r") as bible:
    for b in bible:
        driver.get(b)
        time.sleep(2)
        # opens 'More actions' menu
        more_action_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@aria-label = 'More actions']")
            )
        )
        more_action_btn.click()
        # clicks on 'open transcription' button
        open_trancript_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//paper-listbox[@id = 'items']/ytd-menu-service-item-renderer",
                )
            )
        )
        open_trancript_btn.click()
        time.sleep(3)

        namedvideo = driver.find_element_by_xpath("//*[@id='container']/h1").text
        named = re.sub(r'[\\/*?:"<>|]', "", str(namedvideo))
        print(named)
        f = open(named + ".txt", "w")
        f.close()
        elements = driver.find_elements_by_css_selector("div.cue")

        for element in elements:
            with open(named + ".txt", "a") as order:
                order.write((element.text + " ").replace("\n", " "))
            print(element)
            f.close()
        time.sleep(1)

driver.quit()
