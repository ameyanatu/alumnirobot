import os
import traceback
from robot.api.deco import keyword, library
from robot.libraries.BuiltIn import BuiltIn
from datetime import datetime

# Selenium imports
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Playwright imports
from playwright.sync_api import sync_playwright

from alumnium import Alumni
from faker import Faker

@library
class AlumniRobotLibrary:
    def __init__(
        self,
        backend="selenium",
        browser="chrome",
        headless=True,
        ai_provider="openai",
        ai_model=None,
        api_key=None,
        api_base=None,
        screenshot_dir="alumni_failures"
    ):
        self.backend = backend.lower()
        self.browser = browser.lower()
        self.headless = headless
        self.driver = None
        self.page = None
        self.al = None
        self.playwright = None
        self.screenshot_dir = screenshot_dir
        self.custom_keywords = {}

        # AI model/provider setup
        if ai_provider:
            os.environ["ALUMNIUM_AI_PROVIDER"] = ai_provider
        if ai_model:
            os.environ["ALUMNIUM_AI_MODEL"] = ai_model
        if api_key:
            if ai_provider == "openai":
                os.environ["OPENAI_API_KEY"] = api_key
            elif ai_provider == "anthropic":
                os.environ["ANTHROPIC_API_KEY"] = api_key
            elif ai_provider == "google":
                os.environ["GOOGLE_API_KEY"] = api_key
            elif ai_provider == "deepseek":
                os.environ["DEEPSEEK_API_KEY"] = api_key
        if api_base:
            os.environ["ALUMNIUM_API_BASE"] = api_base

        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

        self.faker = Faker()

    @keyword
    def open_browser_and_init_alumni(self, url):
        """Open browser (Selenium or Playwright) and initialize Alumni."""
        if self.backend == "selenium":
            if self.browser == "chrome":
                options = ChromeOptions()
                if self.headless:
                    options.add_argument("--headless")
                self.driver = Chrome(options=options)
            elif self.browser == "firefox":
                options = FirefoxOptions()
                if self.headless:
                    options.add_argument("--headless")
                self.driver = Firefox(options=options)
            else:
                raise ValueError(f"Unsupported Selenium browser: {self.browser}")
            self.driver.get(url)
            self.al = Alumni(self.driver)
        elif self.backend == "playwright":
            self.playwright = sync_playwright().start()
            if self.browser == "chrome" or self.browser == "chromium":
                browser = self.playwright.chromium.launch(headless=self.headless)
            elif self.browser == "firefox":
                browser = self.playwright.firefox.launch(headless=self.headless)
            elif self.browser == "webkit":
                browser = self.playwright.webkit.launch(headless=self.headless)
            else:
                raise ValueError(f"Unsupported Playwright browser: {self.browser}")
            self.page = browser.new_page()
            self.page.goto(url)
            self.al = Alumni(self.page)
        else:
            raise ValueError(f"Unsupported backend: {self.backend}")

    @keyword
    def alumni_do(self, command):
        """Run a natural language command with self-healing and logging."""
        try:
            self.al.do(command)
        except Exception as e:
            self._diagnose_and_report_failure("alumni_do", command, e)
            raise

    @keyword
    def alumni_check(self, check_command):
        """Run a check with self-healing and logging."""
        try:
            self.al.check(check_command)
        except Exception as e:
            self._diagnose_and_report_failure("alumni_check", check_command, e)
            raise

    @keyword
    def alumni_get(self, get_command):
        """Run a get command with error handling."""
        try:
            return self.al.get(get_command)
        except Exception as e:
            self._diagnose_and_report_failure("alumni_get", get_command, e)
            raise

    @keyword
    def alumni_quit(self):
        """Quit browser/context."""
        if self.backend == "selenium" and self.driver:
            self.driver.quit()
        elif self.backend == "playwright" and self.playwright:
            self.playwright.stop()

    @keyword
    def generate_test_data(self, data_type="user", schema=None):
        """
        Generate dynamic test data using Faker.
        - data_type: 'user', 'address', or 'custom'
        - schema: comma-separated string of fields for 'custom'
        """
        if data_type == "user":
            return {
                "name": self.faker.name(),
                "username": self.faker.user_name(),
                "email": self.faker.email(),
                "password": self.faker.password()
            }
        elif data_type == "address":
            return {
                "street": self.faker.street_address(),
                "city": self.faker.city(),
                "state": self.faker.state(),
                "zip": self.faker.zipcode()
            }
        elif data_type == "custom" and schema:
            fields = [field.strip() for field in schema.split(",")]
            data = {}
            for field in fields:
                # Map field names to Faker methods (add more as needed)
                if field == "name":
                    data["name"] = self.faker.name()
                elif field == "username":
                    data["username"] = self.faker.user_name()
                elif field == "email":
                    data["email"] = self.faker.email()
                elif field == "password":
                    data["password"] = self.faker.password()
                elif field == "company":
                    data["company"] = self.faker.company()
                elif field == "street":
                    data["street"] = self.faker.street_address()
                elif field == "city":
                    data["city"] = self.faker.city()
                elif field == "state":
                    data["state"] = self.faker.state()
                elif field == "zip":
                    data["zip"] = self.faker.zipcode()
                elif field == "phone":
                    data["phone"] = self.faker.phone_number()
                # Add more mappings as needed
                else:
                    data[field] = f"Field '{field}' not recognized"
            return data
        else:
            return {}


    @keyword
    def register_custom_keyword(self, name, func):
        """Register a custom Python function as a Robot keyword."""
        self.custom_keywords[name] = func
        setattr(self, name, keyword(func))

    def _diagnose_and_report_failure(self, action, command, exception):
        """On failure, capture screenshot, HTML, and log error details."""
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(self.screenshot_dir, f"{action}_{ts}.png")
        html_path = os.path.join(self.screenshot_dir, f"{action}_{ts}.html")

        # Screenshot and HTML capture for Selenium
        if self.backend == "selenium" and self.driver:
            try:
                self.driver.save_screenshot(screenshot_path)
                with open(html_path, "w", encoding="utf-8") as f:
                    f.write(self.driver.page_source)
            except Exception:
                pass
        # Screenshot and HTML capture for Playwright
        elif self.backend == "playwright" and self.page:
            try:
                self.page.screenshot(path=screenshot_path)
                with open(html_path, "w", encoding="utf-8") as f:
                    f.write(self.page.content())
            except Exception:
                pass

        # Log to Robot Framework log
        BuiltIn().log(
            f"\n[AlumniRobotLibrary] Failure in {action}('{command}'):\n"
            f"{exception}\n"
            f"Screenshot: {screenshot_path}\n"
            f"HTML: {html_path}\n"
            f"Traceback:\n{traceback.format_exc()}",
            level='ERROR'
        )


