from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Import Options class for Chrome options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def drajver():
    # Set Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Enable headless mode

    # Create Chrome service and pass the options
    service = Service(executable_path="/home/ec2-user/testing/chromedriver_directory/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)  # Pass options to Chrome
    driver.get("https://app.zoomshift.com/session/new")
    time.sleep(5)
    return service, driver

# LOGIN PART
def logging(driver):
    username = driver.find_element(By.ID, "session_email")
    password = driver.find_element(By.ID, "session_password")
    username.send_keys("dstefanovic@supportyourapp.com")
    password.send_keys("Jabuka540!" + Keys.ENTER)
    time.sleep(5)

# CHECK LOCAL TIME
def check_time(hour, minute):
    current_time = time.localtime()
    return current_time.tm_hour == hour and current_time.tm_min == minute

def once_logged(driver):
    driver.get("https://app.zoomshift.com/vni5ome0/time_clock")
    email = driver.find_element(By.ID, "time_clock_employee_id")
    email.send_keys("dstefanovic@supportyourapp.com" + Keys.ENTER)
    time.sleep(15)

def clocking_in(driver):
    clock_in_button = driver.find_element(By.XPATH, "//button[text()='Clock In']")
    clock_in_button.click()
    driver.close()

def clocking_out(driver):
    clock_out_button = driver.find_element(By.XPATH, "//button[text()='Clock Out']")
    clock_out_button.click()
    driver.close()

if check_time(00,45):
    service, driver = drajver()
    logging(driver)
    once_logged(driver)
    clocking_in(driver)
else:
    # Handle other cases here
    pass
