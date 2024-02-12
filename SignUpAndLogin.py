import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_login_page(self, url):
        time.sleep(2)
        self.driver.get(url)
        time.sleep(2)
        self.driver.maximize_window()

    def click_sign_up_button(self, by='xpath', value="(//a[normalize-space()='Sign up'])[1]"):
        username_field = self.driver.find_element(by, value)
        username_field.click()
        time.sleep(2)

    def enter_username(self, username, by='xpath', value="(//input[@id='sign-username'])[1]"):
        username_field = self.driver.find_element(by, value)
        username_field.send_keys(username)
        time.sleep(2)

    def enter_password(self, password, by='xpath', value="(//input[@id='sign-password'])[1]"):
        password_field = self.driver.find_element(by, value)
        password_field.send_keys(password)
        time.sleep(2)

    def click_signup_button(self, by='xpath', value="(//button[normalize-space()='Sign up'])[1]"):
        login_button = self.driver.find_element(by, value)
        login_button.click()
        time.sleep(2)


def run_login_test():
    from selenium.webdriver.chrome.service import Service
    chrome_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service)
    login_page = LoginPage(driver)

    try:
        login_page.navigate_to_login_page("https://www.demoblaze.com/")
        login_page.click_sign_up_button()
        login_page.enter_username("username")
        login_page.enter_password("password")
        login_page.click_signup_button()
        print("Signup test passed!")
    except Exception as e:
        print(f"Sign Up test failed: {e}")
    finally:
        driver.quit()


# Run the test
run_login_test()
