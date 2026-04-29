import time

from playwright.sync_api import Page, expect

from pages.tablePage import tablePage


# Open page
# Select Language = Java
# Verify only Java courses are visible
def test_tableData(page: Page):
    table = tablePage(page)

    # Open page
    table.open_page()

    # Select Language = Java
    table.select_language()

    # Verify only Java courses are visible
    table.table_validation()

