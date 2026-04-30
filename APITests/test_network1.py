import time

from playwright.sync_api import Playwright, Page


#https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/69e70531f86ba51a6577f06f

def intercept_response(route):
    route.fulfill(json={"message":"No Product in Cart"})


def test_network1(page:Page):

    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("vickyipad4@icloud.com")
    page.get_by_placeholder("enter your passsword").fill("Vikas@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    text = page.locator(".mt-4").text_content()
    time.sleep(10)
    print(text)