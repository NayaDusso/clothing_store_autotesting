from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, ".login")
    CONTACT_LINK = (By.CSS_SELECTOR, "#contact-link > a")
    BASKET_LINK = (By.CSS_SELECTOR, ".shopping_cart > a")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#search_query_top")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#searchbox > button")
    HEADER_LOGO_LINK = (By.CSS_SELECTOR, "#header_logo > a")
    NEWSLETTER_INPUT  = (By.CSS_SELECTOR, "#newsletter-input")
    NEWSLETTER_SUBMIT = (By.NAME, "submitNewsletter")