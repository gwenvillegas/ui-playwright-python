from dataclasses import dataclass
from playwright.sync_api import Page

@dataclass
class LoginPage:
    page: Page

    @property
    def url(self):
        return "https://the-internet.herokuapp.com/login"
    
    @property
    def username(self):
        return self.page.locator("#username")

    @property
    def password(self):
        return self.page.locator("#password")
    
    @property
    def login_button(self):
        return self.page.locator("#login > button")
      
    @property
    def flash_message(self):
        return self.page.locator("#flash")
    
    @property
    def successful_login_header(self):
        return self.page.locator("h2")    
    
    def login(self, username, password):
        self.page.goto(self.url)
        self.username.type(username)
        self.password.type(password)
        self.login_button.click()


