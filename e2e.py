from selenium import webdriver
from selenium.webdriver.common.by import By
import main_score,webbrowser

#The function works only if the site is in the air
def test_score_service(url_path):
    driver = webdriver.Edge()
    driver.get(url_path)
    score = driver.find_element(By.ID,value='score').text
    driver.quit()
    score = int(score)
    if score >= 0 and score<=1000:
        return True
    else:       return False

def main_function():
    try:
        test_score_service('http://127.0.0.1:5000/')
        return -1
    except:
        return 0
