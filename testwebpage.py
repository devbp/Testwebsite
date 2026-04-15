
import re
from playwright.sync_api import Page,expect
import time
import pytest
 
@pytest.fixture(scope="function",autouse=True)
def landpage(page:Page):
            
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

    def test_click_contact(self, page:Page):

       contact=page.get_by_role("link",name="Contact").click()
       page.get_by_role("textbox",name="name").fill("Peter")
       page.get_by_placeholder("your@email.com").fill("toyou.dev@gmail.com")
       page.get_by_role("textbox",name="message").fill("hello this is a test messgae")
       page.get_by_role("button",name="Send Message").click()
    
    def test_all_Locators(self,page:Page):
       for loc in page.get_by_role("link").all():
           loc.click()
           #locator.all().

    #def test_menu(self,page:Page):
    #   print(page.get_by_role('link').all())
    #   for li in  page.get_by_role('link').all():
    #     li.click();
    #     time.sleep(2)
