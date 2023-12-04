from generic.excel_library import read_locators

loc_file_path = "../project_files/Book 1 (3).xlsx"
loc_sheet_name = "login_credentials"


class LoginPage:
    locators = read_locators()

    def __init__(self, driver):
        self.driver = driver

    def username(self, username):
        self.driver.find_element(*self.locators["username_loc"]).send_keys(username)

    def password(self, password):
        self.driver.find_element(*self.locators["password_loc"]).send_keys(password)

    def signup_button(self):
        self.driver.find_element(*self.locators["login_btn"]).click()
