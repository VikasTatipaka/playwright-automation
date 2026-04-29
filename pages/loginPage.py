from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page

class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.username= page.get_by_label("Username")
        self.password= page.get_by_label("Password")
        self.submit = page.locator("#submit")
        self.success = page.locator("h1")
        self.failure = page.locator("#error")
        self.logout = page.locator("//a[normalize-space()='Log out']")

    def open(self):
        self.page.goto("https://practicetestautomation.com/practice-test-login/")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.submit.click()

    def success_login(self):
        expect(self.success).to_contain_text("Logged In Successfully")
        expect(self.logout).to_be_visible()

    def failure_login(self):
        expect(self.failure).to_be_visible()




