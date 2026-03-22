from playwright.sync_api import sync_playwright
import time

class BrowserAutomationEngine:
    def __init__(self):
        self.pw = None
        self.browser = None
        self.page = None

    def start(self, url):
        print(f"[INFO]: Starting Playwright (Sync Mode)...")
        self.pw = sync_playwright().start()
        # launch(headless=False) lets you see it happen
        self.browser = self.pw.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto(url)
        print(f"[INFO]: Browser opened at {url}")

    def run_logic(self):
        print("[LOG]: Scanning page for search input...")
        # Wait for the element to be ready
        self.page.wait_for_selector("input#searchInput")
        
        # Act
        self.page.fill("input#searchInput", "Artificial Intelligence")
        self.page.keyboard.press("Enter")
        
        # Verify
        self.page.wait_for_load_state("networkidle")
        print(f"[STATUS]: Success! Current Page: {self.page.title()}")
        
        # Proof for the manager
        self.page.screenshot(path="success.png")
        print("[INFO]: success.png created.")
        time.sleep(2) # Just so you can see it before it closes

    def stop(self):
        if self.browser:
            self.browser.close()
        if self.pw:
            self.pw.stop()
        print("[INFO]: Session closed cleanly.")

def main():
    engine = BrowserAutomationEngine()
    try:
        engine.start("https://www.wikipedia.org")
        engine.run_logic()
    except Exception as e:
        print(f"[ERROR]: {e}")
    finally:
        engine.stop()

if __name__ == "__main__":
    main()