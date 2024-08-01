from model.login_page import LoginPage
import pytest


def test_login_successfully(page):
    login_page = LoginPage(page)
    login_page.login("tomsmith", "SuperSecretPassword!")
    successful_message = login_page.flash_message.inner_text()
    expected_successful_message = "You logged into a secure area!"
    assert expected_successful_message in successful_message
    
    login_header = login_page.successful_login_header.inner_text()
    excepted_login_header = "Secure Area"
    assert excepted_login_header in login_header


def test_login_uncessfully(page):
    login_page = LoginPage(page)    
    login_page.login("tomsmith1", "SuperSecretPassword!")
    error_message = login_page.flash_message.inner_text()
    expected_error_message = "Your username is invalid!"
    assert expected_error_message in error_message


@pytest.mark.parametrize(
        ("expected_message", "username", "password"),
        [
            ("You logged into a secure area!", "tomsmith", "SuperSecretPassword!"),
            ("Your username is invalid!", "tomsmith1", "SuperSecretPassword!")
        ]
)
def test_login(expected_message, username, password, page):
    login_page = LoginPage(page)
    login_page.login(username, password)
    flash_message = login_page.flash_message.inner_text()
    assert expected_message in flash_message

