import time
from multiprocessing import process

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

def test_dynamicTable(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    # identify column: price
    # identify rows: rice
    # assert price of rice

    cols = page.locator("th")
    count = cols.count()
    print(count)
    index= -1
    for i in range(count):
        if cols.nth(i).inner_text() =="Price":
            index = i
            break

    rice_row = page.locator("tr").filter(has_text= "Rice")
    price = rice_row.locator("td").nth(index).inner_text().strip()
    print(price)

def test_langtable(page: Page):
    page.goto("https://practicetestautomation.com/practice-test-table/")

    cols = page.locator("th")
    count = cols.count()
    index= -1
    for i in range(count):
        if cols.nth(i).inner_text() =="Language":
            index = i
            break

    rows = page.locator("//table[@id = 'courses_table']/tbody/tr[not(contains(@style, 'display: none'))]")
    rowcount = rows.count()
    for i in range(rowcount):
        language = rows.nth(i).locator("td").nth(index).inner_text().strip()
        print(language)












