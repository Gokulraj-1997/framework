import pytest
from selenium import webdriver


@pytest.fixture()
def init_driver():
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=opts)

    url = r"https://chat.qspiders.com/"
    driver.get(url)

    yield driver

    driver.close()
