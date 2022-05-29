from playwright.sync_api import Playwright, sync_playwright
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


def run(playwright: Playwright) -> None:
    # Assess
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://www.amazon.com/Echo-Dot/dp/B084J4KNDS/
    page.goto("https://www.amazon.com/Echo-Dot/dp/B084J4KNDS/")
    page.set_default_timeout(30000)
    # Act
    page.locator("[id=\"icp-nav-flyout\"]").click()
    page.locator("text=English - EN").click()
    with page.expect_navigation():
        page.locator("#icp-save-button input[type=\"submit\"]").click()
    page.locator("#nav-global-location-popover-link").click()
    page.locator("[aria-label=\"or enter a US zip code\"]").click()
    page.locator("[aria-label=\"or enter a US zip code\"]").fill("33101")
    page.locator(
        "text=ApplyPlease enter a valid US zip codeThis zip code is not currently available. P >> input[type=\"submit\"]").click()
    with page.expect_navigation():
        page.locator(
            "text=You're now shopping for delivery to:Choose your location33101Delivery options ma >> input[type=\"submit\"]").nth(
            1).click()
    page.locator("input:has-text(\"Add to Cart\")").click()
    with page.expect_navigation():
        page.locator("text=Continue Add selected items to cart No thanks >> input[type=\"submit\"]").nth(2).click()
    page.click("'Go to Cart'")
    page.locator("text=Qty:1").click()
    with page.expect_navigation():
        page.locator("#quantity_4").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
