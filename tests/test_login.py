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

    password_key = user["password_key"]

    if password_key == "EMPTY_PASSWORD":
        password = ""
    else:
        password = os.getenv(password_key)
        assert password is not None, f"{password_key} is missing in environment variables"

    login.login(user["name"], password)



    if user["expected"] == "success":
        login.success_login()


    else:
        login.failure_login()




