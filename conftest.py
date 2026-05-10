import pytest
from selenium import webdriver

import random
import string


@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()


@pytest.fixture
def url():
    url = "https://qa-desk.education-services.ru"

    return url


@pytest.fixture
def random_email():
    user = "".join(random.choices(string.ascii_lowercase, k=10))
    domain = "".join(random.choices(string.ascii_lowercase, k=5))
    email = f"{user}@{domain}.com"

    return email
