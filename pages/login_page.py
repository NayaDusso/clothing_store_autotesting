from .base_page import BasePage
from .locators import LoginPageLocators
from random import choice
from string import digits



class LoginPage(BasePage):

    def send_email_for_registration(self):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_CREATE_INPUT)
        random_email = "semen_sokolow" + str(''.join(choice(digits) for i in range(5))) + "@yahoo.com"
        email_input.send_keys(random_email)
        submit_registration = self.browser.find_element(*LoginPageLocators.SUBMIT_CREATE)
        submit_registration.click()
