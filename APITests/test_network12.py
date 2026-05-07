import time

from playwright.sync_api import Playwright, Page


#https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/69e70531f86ba51a6577f06f

def interceptreq(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fbo")


def test_network2(page:Page):

    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", interceptreq)
    page.get_by_placeholder("email@example.com").fill("vickyipad4@icloud.com")
    page.get_by_placeholder("enter your passsword").fill("Vikas@123")
    page.get_by_role("button", name="Login").click()
    page.locator(".ngx-spinner-overlay").wait_for(state="hidden")

    page.get_by_role("button", name="ORDERS").click()

    page.get_by_role("button", name="View").first.click()

