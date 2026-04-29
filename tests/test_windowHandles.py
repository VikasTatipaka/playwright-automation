import time

from playwright.sync_api import Page, expect


def test_windowHandle(page: Page):
    page.goto("https://www.hyrtutorials.com/p/window-handles-practice.html")


    with page.expect_popup() as new_window:
        page.locator("#newWindowBtn").click()

    child = new_window.value
    child.wait_for_load_state()
    child.locator("#firstName").fill("John")
    child.locator("#lastName").fill("Smith")
    child.locator("#malerb").check()
    child.locator("#englishchbx").click()
    child.locator("#email").fill("johnsmith@gmail.com")
    child.locator("#password").fill("password123")
    child.get_by_role("button", name="Register").click()
    expect(child.locator("#msg")).to_contain_text("Registration is Successful")
    time.sleep(10)

def test_miltwindows(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    page.locator("#confirmbtn").click()
    page.on("dialog", lambda dialog: dialog.accept())

def test_frames(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    frames = page.frame_locator("#courses-iframe")

    expect(frames.locator("body")).to_contain_text("An Academy to")








