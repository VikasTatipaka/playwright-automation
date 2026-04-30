from playwright.sync_api import Playwright, expect

from utils.apiBase import APIutils


# https://rahulshettyacademy.com/api/ecom/auth/login
#
# {"userEmail":"vickyipad4@icloud.com","userPassword":"Vikas@123"}
# {"message":"No Product in Cart"}
# {
#     "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OWU3MDUzMWY4NmJhNTFhNjU3N2YwNmYiLCJ1c2VyRW1haWwiOiJ2aWNreWlwYWQ0QGljbG91ZC5jb20iLCJ1c2VyTW9iaWxlIjo2NDc4NjUxNzU3LCJ1c2VyUm9sZSI6ImN1c3RvbWVyIiwiaWF0IjoxNzc3NTM1NzgyLCJleHAiOjE4MDkwOTMzODJ9.nyGrPQsotNOckYShEXuXOcRibnTWYVg1Bf283O3fTAs",
#     "userId": "69e70531f86ba51a6577f06f",
#     "message": "Login Successfully"
# }

def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    apiutils= APIutils()
    order_id= apiutils.createOrder(playwright)

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("vickyipad4@icloud.com")
    page.get_by_placeholder("enter your passsword").fill("Vikas@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    row = page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")