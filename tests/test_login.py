from model.login_page import LoginPage
import pytest
import os 
from dotenv import load_dotenv

load_dotenv(".env")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


def test_login_successfully(page):
    login_page = LoginPage(page)
    login_page.login(USERNAME, PASSWORD)
    successful_message = login_page.flash_message.inner_text()
    expected_successful_message = "You logged into a secure area!"
    assert expected_successful_message in successful_message
    
    login_header = login_page.successful_login_header.inner_text()
    excepted_login_header = "Secure Area"
    assert excepted_login_header in login_header

@pytest.mark.parametrize(
        ("expected_message", "username", "password"),
        [
            ("Your username is invalid!", "tomsmith1", "SuperSecretPassword!"),
            ("Your password is invalid!", "tomsmith", "SuperSecretPassword1!")            
        ]
)
def test_login_unsuccessful(expected_message, username, password, page):
    login_page = LoginPage(page)
    login_page.login(username, password)
    flash_message = login_page.flash_message.inner_text()
    assert expected_message in flash_message

