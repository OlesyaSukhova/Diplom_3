import pytest
import requests
from selenium import webdriver

from curl import *

from faker import Faker
fake = Faker()


@pytest.fixture(params=['chrome', 'firefox'])
def driver (request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(main_page_url)
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.set_window_size(1680, 1080)
        driver.get(main_page_url)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def generate_user_data():
    credentials = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }
    response = requests.post(f'{base_endpoint}{create_user_endpoint}', json=credentials)
    assert response.status_code == 200
    access_token = response.json().get("accessToken")
    auth_headers = {
         'Authorization': access_token
    }
    yield credentials
    requests.delete(f'{base_endpoint}{user_info_endpoint}', headers=auth_headers)

