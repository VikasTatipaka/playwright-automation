from playwright.sync_api import Page


class tablePage:
    def __init__(self, page: Page):
        self.page = page
        self.lang = page.locator("//label[normalize-space()='Java']")

    def open_page(self):
        self.page.goto("https://practicetestautomation.com/practice-test-table/")

    def select_language(self):
        self.lang.click()

    def table_validation(self):
        cols = self.page.locator("th")
        count = cols.count()
        index = -1
        for i in range(count):
            if cols.nth(i).inner_text() == "Language":
                index = i
                break
        rows = self.page.locator("//table[@id = 'courses_table']/tbody/tr[not(contains(@style, 'display: none'))]")
        row_count = rows.count()

        for i in range(row_count):
            language = rows.nth(i).locator("td").nth(index).inner_text().strip()
            assert language == "Java"
