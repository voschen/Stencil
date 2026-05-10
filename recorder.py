from playwright.sync_api import sync_playwright, Playwright



def handle_click(data):
    print("clicked:", data)


def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    context.expose_function("sendToPython", handle_click)

    page.add_init_script(script="""
        document.addEventListener('click', (e) => {
            console.log('CLICK CAUGHT')
            window.sendToPython(e.target.tagName)
        }, true)
    """, )
    
    page.goto("http://wikipedia.com")
    page.evaluate("window.sendToPython('test')")
    page.pause()




with sync_playwright() as playwright:
    
    run(playwright)