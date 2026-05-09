from playwright.sync_api import sync_playwright, Playwright


def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://wikipedia.com")
    # other actions...
    # browser.close()

with sync_playwright() as playwright:
    run(playwright)
    input("Press Enter to close...")