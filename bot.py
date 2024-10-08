import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# navigate to twitter's login page
driver = webdriver.Chrome()
driver.get("https://twitter.com/i/flow/login")

time.sleep(2)
username = driver.find_element(By.TAG_NAME, "input")
username.send_keys("USERNAME")
time.sleep(2)
all_buttons = driver.find_elements(
    By.XPATH, "//button[@role='button']"
)
all_buttons[-3].click()

time.sleep(2)
password = driver.find_element(
    By.XPATH, "//input[@type='password']"
)
password.send_keys("PASSWORD")
time.sleep(2)
all_buttons = driver.find_elements(
    By.XPATH, "//button[@role='button']"
)
all_buttons[-2].click()
keyword = "dog"
driver.get("https://twitter.com/search?q=" + keyword + "&src=typed_query")

time.sleep(2)
for scroll in range(2):
    retweet = driver.find_elements(
        By.XPATH, "//button[@data-testid='retweet']"
    )
    driver.execute_script("arguments[0].click();", retweet[0])


    time.sleep(2)
quote_tweet = driver.find_element(
    By.XPATH, "//a[@role='menuitem']"
)
quote_tweet.click()
time.sleep(2)
quote = driver.find_element(By.XPATH, "//div[contains(@class, 'public-DraftStyleDefault-block')]")
quote.send_keys("cute")

time.sleep(2)
tweet = driver.find_element(
    By.XPATH, "//button[@data-testid='tweetButton']"
)
tweet.click()