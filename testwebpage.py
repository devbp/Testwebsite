
import re
from playwright.sync_api import Page,expect
import time
import pytest

@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("before the test runs")

    # Go to the starting url before each test.
    page.goto("https://devpoudel.onrender.com/")
    yield
    
    print("after the test runs")

class TestLandingPage:    

    def test_has_title(self, page:Page):
      
      # Expect a title "to contain" a substring.
      time.sleep(10)
      expect(page).to_have_title(re.compile("Dev Poudel"))

    def test_main_content(self,page:Page) :
      expect(page.locator(".hero-greeting")).to_have_text("Hi, I'm")
      expect(page.locator("h1.hero-name")).to_have_text("Dev Poudel")
      expect(page.locator("h2.hero-title")).to_have_text(
        "Software Engineer · Data Analyst · AI/ML Practitioner")


