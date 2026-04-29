import json
import pytest
from playwright.sync_api import Page, expect
from pages.loginPage import LoginPage
from dotenv import load_dotenv
import os

load_dotenv()

with open("data/login_data.json", "r") as f:
    login_data = json.load(f)["credentials"]

@pytest.mark.parametrize("user", login_data)
def test_login(page: Page, user):

    login = LoginPage(page)
    login.open()
    password = os.getenv(user["password_key"])
    login.login(user["name"], password)



    if user["expected"] == "success":
        login.success_login()


    else:
        login.failure_login()




