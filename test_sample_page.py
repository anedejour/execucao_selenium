import random
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support import expected_conditions as EC


def test_sample_page():
    file_path = pathlib.Path(__file__).parent.resolve()
    driver = webdriver.Chrome()
    driver.get(f"http://127.0.0.1:5500/sample-exercise.html")

    generate_button = driver.find_element(by=By.NAME, value="generate")
    sleep(3)
    generate_button.click()
    sleep(4)
    
    code = driver.find_element(by=By.ID, value="my-value")
    code_text = code.text

    text_box = driver.find_element(by=By.ID, value="input")
    text_box.clear()
    text_box.send_keys(code_text)

    driver.find_element(by=By.NAME, value="button").click()
    sleep(2)

    alert = driver.switch_to.alert
    alert.accept()
    sleep(4)

    result = driver.find_element(by=By.ID, value="result")
    assert  result.text == f"It Works! {code_text}!"
    sleep(2)