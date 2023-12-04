from datetime import datetime
import pytest
from source_code.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

data = [("6282538696", "Gokul@123"), ("6733874846", "hsj@123"), ("9048708320", "aksh@123")]


@pytest.mark.parametrize("username,password", data)
def test_login(init_driver, username, password):
    try:
        driver = init_driver
        lp = LoginPage(driver)
        lp.username(username)
        lp.password(password)
        lp.signup_button()

        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_to_be("https://chat.qspiders.com/student-dashboard"))


    except Exception as error_msg:
        from datetime import datetime

        td = datetime.now()
        # print(error_msg)
        path = r"C:\Users\gokul\PycharmProjects\pythonProject1\pythonProject\pythonProject\framework\screenshots"
        driver.save_screenshot(path + f"\error_{td.strftime('%Y%m%d%H%M%S')}.png")

        raise error_msg
